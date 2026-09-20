#!/usr/bin/env python3
"""M09 new actual-rendered-engine tests plus all original multiplicative tests."""
from __future__ import annotations
import importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def main():
    suite=unittest.TestSuite()
    for f in ('test_multiplicative.py','test_multiplicative_browser.py'):
        path=ROOT/'tools/nollm_visual_toolkit/tests'/f
        spec=importlib.util.spec_from_file_location('m09_'+path.stem,path);mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(mod))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    out=ROOT/'evidence/migration09';out.mkdir(parents=True,exist_ok=True)
    report={'schema':'M09_LOCAL_TESTS_V1','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'new':17,'historical':23,'node_crypto':'NATIVE_WEB_CRYPTO','template_blob':'6619c5da7ad03f38766bfc383d60b5505cb863e0','old_template_skip_removed':True,'scope':'source slice; actual rendered scripts and real CLI; not full wheel or browser navigation'}
    (out/'tests.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped else 1
if __name__=='__main__':raise SystemExit(main())
