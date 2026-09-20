#!/usr/bin/env python3
"""M04 numerical/HTML tests. DOM harness and true navigation have distinct gates."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
 import mpmath # Missing dependency fails, never silently skipped.
 suite=unittest.TestSuite();base=ROOT/'tools/nollm_visual_toolkit/tests'
 for f in ('test_multiplication_lab.py','test_angular_dispersion.py','test_certified_hex.py','test_certified_hex_browser.py'):
  suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module(base/f,'m04_'+f[:-3])))
 result=unittest.TextTestRunner(verbosity=2).run(suite)
 gate=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py','tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],cwd=ROOT)
 r={'schema':'M04_NUMERICAL_HTML_TEST_RUN_V1','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'python_exact_policy_exit':gate.returncode,'browser_navigation':'NOT_COVERED_BY_THIS_RUNNER','scope':'Python source slice, both HTML generation tests, Node native Web Crypto full-record differential; not whole repository or independent review'}
 if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps(r,indent=2));return 0 if result.wasSuccessful() and not result.skipped and gate.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
