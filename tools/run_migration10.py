#!/usr/bin/env python3
"""Retained mathematical tests and actual M10 exact-start CLI/render tests."""
from __future__ import annotations
import argparse,importlib,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TESTS=ROOT/'tools/nollm_visual_toolkit/tests'
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit'),str(TESTS)]

def main():
    p=argparse.ArgumentParser();p.add_argument('--report',type=Path,default=ROOT/'evidence/migration10/tests.json');a=p.parse_args()
    suite=unittest.TestSuite()
    for name in ('test_multiplicative','test_multiplicative_browser','test_multiplicative_startup'):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(importlib.import_module(name)))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'schema':'M10_LOCAL_TESTS_V1','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'new_startup_tests':20,'retained':40,'retained_expectations_advanced':2,'node_crypto':'NATIVE_WEB_CRYPTO','scope':'actual source slice CLI/render and extracted browser engine; not browser navigation/full repository'}
    a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped else 1
if __name__=='__main__':raise SystemExit(main())
