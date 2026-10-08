"""The milestone period and reporting-lag rules must survive daily refreshes."""
import datetime as dt
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('registry_refresh', ROOT / 'scripts/refresh-registry-metrics.py')
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


def result(package='example', positive_through='2026-10-05', requested_end='2026-10-07', count=1):
    start = dt.date.fromisoformat(refresh.PERIOD_START)
    end = dt.date.fromisoformat(requested_end)
    points = []
    for offset in range((end - start).days + 1):
        day = (start + dt.timedelta(days=offset)).isoformat()
        points.append({'day': day, 'downloads': count if day <= positive_through else 0})
    return {
        'package': package,
        'body': {'package': package, 'start': start.isoformat(), 'end': requested_end, 'downloads': points},
        'receipt': {'response_sha256': '0' * 64, 'retrieved_at': '2026-10-08T12:00:00Z'},
    }


class RegistryRefreshTest(unittest.TestCase):
    def test_zero_tail_does_not_advance_or_shrink_rolling_window(self):
        rows = [result('one'), result('two', count=2)]
        evidence, months = refresh.summarize_ranges(rows, refresh.PERIOD_START, '2026-10-07')
        self.assertEqual(evidence['reported_through'], '2026-10-05')
        self.assertEqual(evidence['trailing_all_zero_days_excluded'], ['2026-10-06', '2026-10-07'])
        self.assertEqual(evidence['rolling_start'], '2025-10-06')
        self.assertEqual(sum(row['rolling_365_days'] for row in evidence['packages']), 365 * 3)
        self.assertEqual(sum(months.values()), 370 * 3)
        self.assertEqual(months['2026-10'], 5 * 3)

    def test_fixed_period_is_preserved_when_reporting_advances(self):
        earlier, old_months = refresh.summarize_ranges([result()], refresh.PERIOD_START, '2026-10-07')
        later, new_months = refresh.summarize_ranges(
            [result(positive_through='2026-10-08', requested_end='2026-10-09')],
            refresh.PERIOD_START, '2026-10-09')
        self.assertEqual(earlier['requested_start'], later['requested_start'])
        self.assertEqual(sum(new_months.values()) - sum(old_months.values()), 3)
        self.assertEqual(later['rolling_start'], '2025-10-09')
        self.assertEqual(later['packages'][0]['rolling_365_days'], 365)
        self.assertGreater(sum(new_months.values()), later['packages'][0]['rolling_365_days'])

    def test_invalid_or_incomplete_data_is_rejected(self):
        cases = []
        missing = result(); missing['body']['downloads'].pop(); cases.append(missing)
        negative = result(); negative['body']['downloads'][0]['downloads'] = -1; cases.append(negative)
        boolean = result(); boolean['body']['downloads'][0]['downloads'] = True; cases.append(boolean)
        wrong_day = result(); wrong_day['body']['downloads'][0]['day'] = '2025-10-02'; cases.append(wrong_day)
        wrong_package = result(); wrong_package['body']['package'] = 'other'; cases.append(wrong_package)
        all_zero = result(count=0); cases.append(all_zero)
        for row in cases:
            with self.subTest(row=row['body']['package']):
                with self.assertRaises(ValueError):
                    refresh.summarize_ranges([row], refresh.PERIOD_START, '2026-10-07')
        with self.assertRaises(ValueError):
            refresh.summarize_ranges([result(), result()], refresh.PERIOD_START, '2026-10-07')

    def test_source_failure_does_not_write_or_render(self):
        receipt = {'retrieved_at': '2026-10-08T12:00:00Z'}
        with patch.object(refresh, 'npm_inventory', return_value=(['example'], [receipt])), \
                patch.object(refresh, 'fetch_json', side_effect=RuntimeError('API unavailable')), \
                patch.object(refresh, 'save') as save, \
                patch.object(refresh.subprocess, 'run') as run:
            with self.assertRaisesRegex(RuntimeError, 'API unavailable'):
                refresh.main()
            save.assert_not_called()
            run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
