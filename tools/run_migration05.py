#!/usr/bin/env python3
"""M05 source-slice suite plus reconstructed-package import checks."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--report',type=Path,default=ROOT/'evidence/migration05/numerical_package.json');a=p.parse_args();import mpmath
 suite=unittest.TestSuite();base=ROOT/'tools/nollm_visual_toolkit/tests'
 for f in ('test_multiplication_lab.py','test_angular_dispersion.py','test_certified_hex.py','test_certified_hex_browser.py'):
  suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module(base/f,'m05_'+f[:-3])))
 result=unittest.TextTestRunner(verbosity=2).run(suite)
 gate=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py','tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],cwd=ROOT)
 pkg=subprocess.run([sys.executable,str(ROOT/'tools/test_migration05_package.py')],cwd=ROOT)
 r={'schema':'M05_NUMERICAL_PACKAGE_TEST_RUN_V1','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'python_exact_policy_exit':gate.returncode,'reconstructed_package_exit':pkg.returncode,'browser_navigation':'NOT_COVERED_BY_THIS_RUNNER','scope':'M04 arithmetic/browser-record tests plus modified gallery static test and exact-blob reconstructed top-level package/CLI/local-server validation'}
 a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));return 0 if result.wasSuccessful() and not result.skipped and gate.returncode==0 and pkg.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
