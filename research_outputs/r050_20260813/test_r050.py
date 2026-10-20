#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("check_r050", ROOT/"check_r050.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class R050ExactTests(unittest.TestCase):
    def test_freeze(self):
        self.assertGreater(m.check_freeze(),0)
    def test_matrices(self):
        self.assertGreater(m.check_matrices(),0)
    def test_transfer_derivations(self):
        self.assertGreater(m.check_m1_transfer_identity(),0)
        self.assertGreater(m.check_m6_transfer_identity(),0)
    def test_ledgers(self):
        self.assertGreater(m.check_ledgers(),0)

if __name__=="__main__":
    unittest.main()
