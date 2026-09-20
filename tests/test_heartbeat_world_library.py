"""Library wiring regression tests; not new mathematical theorem tests."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('heartbeat_library',ROOT/'tools/heartbeat_world_library.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

class LibraryTests(unittest.TestCase):
    def test_catalog_counts(self):
        x=lib.validate(ROOT)
        self.assertEqual((x['methods'],x['exports'],x['theorem_candidates']),(2,17,12))
        self.assertFalse(x['mathematical_admission'])
        self.assertFalse(x['scheduler_queue_rewritten'])
    def test_no_redefinition(self):
        data=lib.resolve(ROOT)
        for t in data['theorems']:
            ledger=json.loads((ROOT/t['ledger']).read_text())
            original=next(r for r in ledger.get('laws',ledger.get('theorems',[])) if r['id']==t['id'])
            self.assertEqual(original,t['original_record'])
    def test_priority_limits(self):
        p=lib.resolve(ROOT)['priority']
        self.assertTrue(p['nonpreemption'])
        self.assertFalse(p['grants_claim']);self.assertFalse(p['grants_driver_authority'])
        self.assertIn('FREE_PHASE_A',p['discovery_firewall'])
        self.assertEqual(p['world_contract']['spatial_dimension'],6)
        self.assertEqual(p['world_contract']['time_dimension'],1)
    def test_cli_exact_theorem(self):
        raw=subprocess.check_output([sys.executable,str(ROOT/'tools/heartbeat_world_library.py'),'theorems','--query','HBW-LS-005'],text=True)
        self.assertEqual([r['id'] for r in json.loads(raw)],['HBW-LS-005'])
    def test_source_drift_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            data=lib.resolve(ROOT);paths={lib.CATALOG,data['catalog']['priority_ref']}
            for e in data['catalog']['entries']:
                paths.update(e[k] for k in ('module','test','ledger','proof','inventory_ref'))
            for p in paths:
                q=root/p;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/p,q)
            p=root/data['catalog']['entries'][0]['module'];p.write_text(p.read_text()+'\n# changed\n')
            with self.assertRaisesRegex(ValueError,'source changed'):lib.validate(root)
    def test_traversal_rejected(self):
        with self.assertRaises(ValueError):lib._path(ROOT,'../outside')

if __name__=='__main__':unittest.main(verbosity=2)
