"""Guard against stale dashboard values when published snapshots change."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('visual',ROOT/'scripts/render-visual-profile.py')
visual=importlib.util.module_from_spec(spec)
spec.loader.exec_module(visual)

class VisualProfileTest(unittest.TestCase):
    def test_partial_month_is_counted_once_and_dated(self):
        n=json.loads((ROOT/'data/registry-stats.json').read_text())['npm']
        year,month=map(int,n['monthly_downloads'][-1]['month'].split('-'))
        next_month=f'{year+(month==12):04d}-{month%12+1:02d}'
        n['current_month']={'month':next_month,'downloads':7654321,'period_end':next_month+'-05'}
        rows=visual.chart_rows(n)
        self.assertEqual(len(rows),len(n['monthly_downloads'])+1)
        self.assertEqual(sum(x['downloads'] for x in rows),sum(x['downloads'] for x in n['monthly_downloads'])+7654321)
        self.assertTrue(rows[-1]['partial'])
        self.assertEqual(visual.chart_end(n),next_month+'-05')
        n['current_month']['month']=n['monthly_downloads'][-1]['month']
        with self.assertRaises(AssertionError):visual.chart_rows(n)

    def test_published_values_and_chart_refresh_together(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for rel in ['data/metrics.json','data/registry-stats.json','data/github-stats.json','data/snapshots/2026-10-02/github-baseline-2026-09-07.json','scripts/templates/ruvnet-dashboard.svg']:
                dest=root/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,dest)
            original=visual.ROOT
            try:
                visual.ROOT=root;visual.render()
                output=root/'assets/ruvnet/dashboard.svg'
                first=output.read_text();visual.render();self.assertEqual(first,output.read_text())
                registry=root/'data/registry-stats.json';r=json.loads(registry.read_text())
                r['npm']['downloads']=123456789
                r['npm']['monthly_downloads'][-1]['downloads']=20000000
                r['generated_at']='2026-11-05T00:00:00Z'
                r['npm']['downloads_verified_at']='2026-11-05T00:00:00Z'
                registry.write_text(json.dumps(r))
                github=root/'data/github-stats.json';g=json.loads(github.read_text())
                g['account']['followers']=12345
                for entry in g['flagships']:
                    if entry['name']=='ruflo':entry['stars']=70000
                github.write_text(json.dumps(g));visual.render()
                final=output.read_text();self.assertIn('123,456,789',final);self.assertNotIn('91,172,864',final)
                growth=(root/'assets/ruvnet/npm-cumulative-growth.svg').read_text()
                expected=sum(row['downloads'] for row in visual.chart_rows(r['npm']))
                self.assertIn(f'{expected:,}',growth)
                self.assertIn('not lifetime downloads',growth)
                self.assertNotIn('91,172,864',growth)
                self.assertIn('12,345',final);self.assertIn('2026-11-05',final)
                self.assertIn('70,000 ★',final);self.assertIn('-1,415 stars',final)
                ns={'s':visual.NS}
                before=ET.fromstring(first).find('.//s:path[@id="realchart"]',ns).get('d')
                after=ET.fromstring(final).find('.//s:path[@id="realchart"]',ns).get('d')
                self.assertNotEqual(before,after)
                self.assertIn('M40 686L254 708',final)
                self.assertNotIn('<script',final)
            finally:visual.ROOT=original

if __name__=='__main__':unittest.main()
