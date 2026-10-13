"""The milestone period and reporting-lag rules must survive daily refreshes."""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import io
import shutil
import urllib.error
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
    def test_new_npm_package_404_is_retried_without_inventing_zero(self):
        url='https://api.npmjs.org/downloads/range/2025-10-01:2026-10-11/new-package'
        error=urllib.error.HTTPError(url,404,'Not Found',{},None)
        with patch.object(refresh.urllib.request,'urlopen',side_effect=[error,io.BytesIO(b'{"downloads": 17}')]), patch.object(refresh.time,'sleep') as sleep:
            body,receipt=refresh.fetch_json(url)
        self.assertEqual(body['downloads'],17)
        self.assertEqual(receipt['source'],url)
        sleep.assert_called_once()
        with patch.object(refresh.urllib.request,'urlopen',side_effect=error) as fetch, patch.object(refresh.time,'sleep'):
            with self.assertRaisesRegex(refresh.NpmRangeNotFound,'previous verified data retained'):
                refresh.fetch_json(url)
        self.assertEqual(fetch.call_count,8)

    def test_registry_milestone_refreshes_from_evidence_idempotently(self):
        registry=json.loads((ROOT/'data/registry-stats.json').read_text())
        evidence=json.loads((ROOT/registry['npm']['downloads_evidence_path']).read_text())
        registry['crates_io']['cumulative_downloads'] += 123
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'data').mkdir()
            for name in ['ecosystem-running-totals.json','ecosystem-daily-ledger.json']:
                shutil.copyfile(ROOT/'data'/name,root/'data'/name)
            with patch.object(refresh,'ROOT',root):
                refresh.update_running_totals(registry,evidence)
                first=(root/'data/ecosystem-running-totals.json').read_bytes()
                refresh.update_running_totals(registry,evidence)
                self.assertEqual(first,(root/'data/ecosystem-running-totals.json').read_bytes())
            m=json.loads(first)['download_milestone']
            expected=sum(row['downloads'] for row in evidence['daily_totals'] if row['day']<=evidence['reported_through'])
            self.assertEqual(m['combined_observed'],expected+registry['crates_io']['cumulative_downloads'])
            self.assertEqual(m['npm_verified_at'],registry['npm']['downloads_verified_at'])
            self.assertEqual(m['remaining'],max(0,m['target']-m['combined_observed']))

    def test_daily_ledger_upserts_complete_window_idempotently(self):
        today = dt.date(2026, 10, 8)
        row = result(positive_through='2026-10-07', requested_end='2026-10-07')
        row['receipt']['source'] = 'https://api.npmjs.org/downloads/range/example'
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = root / 'data'
            data.mkdir()
            ledger = {
                'schema_version': '1.0', 'observed_from': '2026-09-01',
                'values': {'npm|example|downloads|2026-10-07': 99},
                'package_provenance': {}, 'coverage': {}}
            (data / 'ecosystem-daily-ledger.json').write_text(json.dumps(ledger))
            with patch.object(refresh, 'ROOT', root):
                refresh.update_daily_ledger([row], today, '2026-10-08T12:00:00Z')
                first = (data / 'ecosystem-daily-ledger.json').read_bytes()
                refresh.update_daily_ledger([row], today, '2026-10-08T12:00:00Z')
                second = (data / 'ecosystem-daily-ledger.json').read_bytes()
            updated = json.loads(first)
            self.assertEqual(first, second)
            self.assertEqual(updated['observed_from'], '2026-09-01')
            self.assertEqual(updated['observed_through'], '2026-10-07')
            self.assertEqual(updated['values']['npm|example|downloads|2026-10-07'], 1)
            self.assertEqual(updated['coverage']['collected_packages'], 1)

    def test_daily_ledger_records_missing_package_without_inventing_zero(self):
        today = dt.date(2026, 10, 8)
        row = result(positive_through='2026-10-07', requested_end='2026-10-07')
        row['receipt']['source'] = 'https://api.npmjs.org/downloads/range/example'
        error = {'package': 'new-package', 'error': 'HTTP 404', 'checked_at': '2026-10-08T12:00:00Z'}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); data = root / 'data'; data.mkdir()
            (data / 'ecosystem-daily-ledger.json').write_text(json.dumps({
                'schema_version': '1.0', 'observed_from': '2026-09-01',
                'values': {}, 'package_provenance': {}, 'coverage': {}}))
            with patch.object(refresh, 'ROOT', root):
                refresh.update_daily_ledger([row], today, '2026-10-08T12:00:00Z',
                                            expected_packages=2, errors=[error])
            updated = json.loads((data / 'ecosystem-daily-ledger.json').read_text())
            self.assertEqual(updated['coverage']['expected_packages'], 2)
            self.assertEqual(updated['coverage']['collected_packages'], 1)
            self.assertEqual(updated['coverage']['errors'], [error])
            self.assertFalse(any('|new-package|' in key for key in updated['values']))

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
