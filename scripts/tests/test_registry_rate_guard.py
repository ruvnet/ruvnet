import importlib.util
import io
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('registry_rate_guard', Path(__file__).resolve().parents[1] / 'refresh-registry-metrics.py')
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


class RegistryRateGuardTests(unittest.TestCase):
    def test_inventory_and_crates_requests_remain_available(self):
        for url in ('https://registry.npmjs.org/-/v1/search?text=maintainer:ruvnet', 'https://crates.io/api/v1/crates?page=1'):
            with self.subTest(url=url), patch.object(collector.urllib.request, 'urlopen', return_value=io.BytesIO(b'{"objects": []}')) as network:
                body, receipt = collector.fetch_json(url)
                self.assertEqual(body, {'objects': []})
                self.assertEqual(receipt['source'], url)
                self.assertEqual(len(receipt['response_sha256']), 64)
                network.assert_called_once()
