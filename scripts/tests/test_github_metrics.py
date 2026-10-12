import importlib.util
import copy
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('github_metrics',ROOT/'scripts/render-github-metrics.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class GithubMetricsTest(unittest.TestCase):
    def test_full_inventory_excludes_forks_and_refreshes_flagships(self):
        rows=[{'id':i,'full_name':'ruvnet/'+name,'fork':fork,'stargazers_count':stars,'forks_count':3,'subscribers_count':2} for i,name,fork,stars in [(1,'RuView',False,10),(2,'ruflo',False,20),(3,'fork',True,1000)]]
        inventory={'user':{'login':'ruvnet','public_repos':3,'followers':5},'repositories':rows}
        github={'flagships':[{'name':'ruflo','stars':1},{'name':'RuView','stars':2}]}
        result=module.reconcile(github,inventory)
        self.assertEqual(result['account']['stars_across_owned_nonfork'],30)
        self.assertEqual(result['account']['public_forks'],1)
        self.assertEqual(result['flagships'][0]['stars'],20)
        broken=copy.deepcopy(inventory);broken['repositories'].pop()
        with self.assertRaises(AssertionError):module.reconcile(github,broken)
        broken=copy.deepcopy(inventory);broken['repositories'][1]['id']=1
        with self.assertRaises(AssertionError):module.reconcile(github,broken)
