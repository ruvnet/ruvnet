"""Guard against stale dashboard values when published snapshots change."""
import importlib.util
import json
import copy
import subprocess
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts'))
spec=importlib.util.spec_from_file_location('visual',ROOT/'scripts/render-visual-profile.py')
visual=importlib.util.module_from_spec(spec)
spec.loader.exec_module(visual)

class VisualProfileTest(unittest.TestCase):
    def test_dashboard_uses_canonical_npm_and_separate_providers(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for rel in ['data/metrics.json','data/registry-stats.json','data/github-stats.json','data/ecosystem-running-totals.json','data/snapshots/2026-10-02/github-baseline-2026-09-07.json','scripts/templates/ruvnet-dashboard.svg']:
                dest=root/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,dest)
            original=visual.ROOT
            try:
                visual.ROOT=root
                running=json.loads((root/'data/ecosystem-running-totals.json').read_text())
                running['download_milestone'].update(npm_observed_total=98000000,crates_io_cumulative=3000000,combined_observed=101000000,remaining=0)
                running['npm_billion_goal']['observed_download_events_lower_bound']=123456789
                (root/'data/ecosystem-running-totals.json').write_text(json.dumps(running))
                visual.render()
                svg=(root/'assets/ruvnet/dashboard.svg').read_text()
                self.assertIn('123,456,789',svg)
                self.assertNotIn('101,000,000',svg)
                self.assertIn('NPM EVENTS / LOWER BOUND',svg)
                self.assertIn('CRATES.IO CUMULATIVE:',svg)
                self.assertIn('RELEASE ASSETS OBSERVED:',svg)
                self.assertIn('HISTORICAL NPM CHART /',svg)
                from profile_downloads import verify_downloads
                parsed=ET.fromstring(svg)
                verify_downloads(parsed,running)
                desc=parsed.find('{http://www.w3.org/2000/svg}desc')
                original_desc=desc.text
                desc.text=desc.text.replace('observed events 22805.', 'observed events 22806.')
                if running['npm_billion_goal'].get('provisional_observed_downloads')==22805:
                    with self.assertRaisesRegex(AssertionError,'Stale provisional provider'):
                        verify_downloads(parsed,running)
                desc.text=original_desc
                next(e for e in parsed.iter() if e.get('id')=='npm-observed-total').text='101,000,000'
                with self.assertRaisesRegex(AssertionError,'Stale SVG download claim'):
                    verify_downloads(parsed,running)
            finally:visual.ROOT=original

    def test_keyed_revision_is_checked_against_its_source(self):
        from profile_downloads import validate_goal_revision
        running=json.loads((ROOT/'data/ecosystem-running-totals.json').read_text())
        read_json=lambda p:json.loads((ROOT/p).read_text())
        validate_goal_revision(running,read_json)
        broken=copy.deepcopy(running)
        broken['npm_billion_goal']['baseline_covered_day_revision_adjustment']+=1
        with self.assertRaisesRegex(AssertionError,'Incorrect covered-day revision'):
            validate_goal_revision(broken,read_json)

    def test_provisional_window_cannot_be_rendered_as_confirmed_total(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            for name in ['data','docs','scripts']:
                shutil.copytree(ROOT/name,root/name,ignore=shutil.ignore_patterns('__pycache__'))
            shutil.copyfile(ROOT/'README.md',root/'README.md')
            running=json.loads((root/'data/ecosystem-running-totals.json').read_text())
            running['npm']['unknown_days']=['2026-11-15']
            running['npm']['observed_downloads']=98765
            (root/'data/ecosystem-running-totals.json').write_text(json.dumps(running))
            subprocess.run(['node',str(root/'scripts/render-registry-metrics.mjs')],cwd=root,check=True,capture_output=True)
            windows=json.loads((root/'data/metrics.json').read_text())['current_windows']
            self.assertIsNone(windows['npm_14_day_confirmed_download_events'])
            self.assertEqual(windows['npm_14_day_observed_download_events_lower_bound'],98765)

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
            for rel in ['data/metrics.json','data/registry-stats.json','data/github-stats.json','data/ecosystem-running-totals.json','data/snapshots/2026-10-02/github-baseline-2026-09-07.json','scripts/templates/ruvnet-dashboard.svg']:
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
                final=output.read_text();self.assertNotIn('123,456,789',final);self.assertNotIn('91,172,864',final)
                canonical=json.loads((root/'data/ecosystem-running-totals.json').read_text())['npm_billion_goal']['observed_download_events_lower_bound']
                self.assertIn(f'{canonical:,}',final)
                growth=(root/'assets/ruvnet/npm-cumulative-growth.svg').read_text()
                expected=sum(row['downloads'] for row in visual.chart_rows(r['npm']))
                self.assertIn(f'{expected:,}',growth)
                self.assertIn('not lifetime downloads',growth)
                self.assertNotIn('91,172,864',growth)
                self.assertIn('12,345',final);self.assertIn('data-download-watermark=',final)
                self.assertIn('70,000 ★',final);self.assertIn('-1,415 stars',final)
                ns={'s':visual.NS}
                before=ET.fromstring(first).find('.//s:path[@id="realchart"]',ns).get('d')
                after=ET.fromstring(final).find('.//s:path[@id="realchart"]',ns).get('d')
                self.assertNotEqual(before,after)
                self.assertIn('M40 686L254 708',final)
                self.assertNotIn('<script',final)
            finally:visual.ROOT=original


class GoalReconciliationTest(unittest.TestCase):
    def test_provisional_provider_day_cannot_be_latest_confirmed(self):
        from profile_downloads import canonical
        running=json.loads((ROOT/'data/ecosystem-running-totals.json').read_text())
        self.assertTrue(running['npm_billion_goal']['provisional_dates'])
        running['npm']['daily_latest']['day']=running['npm_billion_goal']['provisional_dates'][0]
        with self.assertRaisesRegex(AssertionError,'Provisional provider day'):
            canonical(running)

    def test_covered_revisions_and_disjoint_increment_are_not_added_twice(self):
        from profile_downloads import validate_goal_reconciliation
        import hashlib
        prior={'npm_billion_goal':{'baseline_covered_day_revision_adjustment':5}}
        old={'values':{'example':1}}; new={'values':{'example':2}}
        key='npm|example|downloads|2026-11-15'; inc='npm|example|downloads|2026-11-16'
        digest=lambda x:hashlib.sha256(json.dumps(x,indent=2).encode()+b'\n').hexdigest()
        source={'schema_version':2,'prior_summary':'prior','prior_summary_sha256':digest(prior),'covered_dates':[{'day':'2026-11-15','prior_source':'old'}],'covered_revisions':[{'key':key,'prior':1,'current':2,'prior_source':'old','source':'new','source_sha256':digest(new)}],'increment_cells':{inc:4},'through':'2026-11-16','verified_at':'2026-11-17T12:00:00Z'}
        goal={'reconciliation_source':'source','baseline_through':'2026-11-15','baseline_covered_day_revision_adjustment':6,'nonoverlapping_daily_increment':4,'increment_dates':['2026-11-16'],'verified_at':source['verified_at'],'baseline_source':'baseline','baseline_download_events':100,'observed_download_events_lower_bound':110}
        data={'source':source,'prior':prior,'old':old,'new':new,'baseline':{'reported_through':'2026-11-15','daily_totals':[{'day':'2026-11-15','downloads':100}]},'data/ecosystem-daily-ledger.json':{'values':{key:2,inc:4}}}
        data['prior_cells']={'values':{key:1}};source.update(prior_covered_ledger='prior_cells',prior_covered_ledger_sha256=digest(data['prior_cells']))
        validate_goal_reconciliation({'npm_billion_goal':goal},data.__getitem__)
        goal['baseline_covered_day_revision_adjustment']=7
        with self.assertRaises(AssertionError):validate_goal_reconciliation({'npm_billion_goal':goal},data.__getitem__)
        goal['baseline_covered_day_revision_adjustment']=6;source['increment_cells'][key]=2
        with self.assertRaises(AssertionError):validate_goal_reconciliation({'npm_billion_goal':goal},data.__getitem__)

    def test_complete_day_can_exclude_only_verified_later_creation(self):
        from profile_downloads import validate_latest_cohort
        latest = {'day':'2026-11-16','collected_packages':1,'expected_packages':1}
        point = {'day':'2026-11-16','values':{'existing':5},'excluded_created_after_target_day':{'new':'2026-11-18T04:48:05Z'}}
        validate_latest_cohort(latest, point, 2, ['existing','new'], {'new':'2026-11-18T04:48:05Z'})
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2, ['existing','different'], {'new':'2026-11-18T04:48:05Z'})
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2, ['existing','new'], {'new':'2026-11-17T00:00:00Z'})
        point['day']='2026-11-15'
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2)
        point['day']='2026-11-16'
        point['excluded_created_after_target_day']['new']='not-a-date'
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2, ['existing','new'], {'new':'not-a-date'})
        point['excluded_created_after_target_day']['new']='2026-11-17T00:30:00+01:00'
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2)
        point['excluded_created_after_target_day']['new']='2026-11-15T00:00:00Z'
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2)
        point['excluded_created_after_target_day']={}
        with self.assertRaises(AssertionError):validate_latest_cohort(latest, point, 2)

if __name__=='__main__':unittest.main()
