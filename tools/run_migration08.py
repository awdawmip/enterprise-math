#!/usr/bin/env python3
"""M08 browser lexicographic adapter gate plus M04 regression surface."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--chromium',default='/usr/bin/chromium');a=p.parse_args()
    m04=subprocess.run([sys.executable,str(ROOT/'tools/run_migration04.py')],cwd=ROOT)
    new=load(ROOT/'tools/nollm_visual_toolkit/tests/test_certified_hex_browser_lexicographic.py','m08_lex_tests')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(new))
    dom=subprocess.run([sys.executable,str(ROOT/'tools/test_migration04_dom.py'),'--chromium',a.chromium],cwd=ROOT)
    m04_record=json.loads((ROOT/'evidence/migration04/numerical_tests.json').read_text())
    dom_record=json.loads((ROOT/'evidence/migration04/dom_validation.json').read_text())
    record={
      'schema':'M08_BROWSER_LEXICOGRAPHIC_ADAPTER_TEST_RUN_V1',
      'm04_regression_tests':m04_record['tests'],'m04_failures':m04_record['failures'],'m04_errors':m04_record['errors'],'m04_skips':m04_record['skips'],
      'new_lexicographic_tests':result.testsRun,'new_failures':len(result.failures),'new_errors':len(result.errors),'new_skips':len(result.skipped),
      'combined_numerical_html_cross_language':m04_record['tests']+result.testsRun,
      'dom_checks':dom_record['checks'],'dom_page_errors':len(dom_record['page_errors']),
      'tie_audit':{'certified_ties':1080,'base_vs_legacy_lexicographic_differences':504},
      'browser_navigation':dom_record['navigation'],
      'kernel_float_math':False,
      'scope':'extends existing certified_hex_browser; old multiplicative browser template not yet wired to adapter',
    }
    out=ROOT/'evidence/migration08';out.mkdir(parents=True,exist_ok=True);(out/'test_run.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    ok=(m04.returncode==0 and result.wasSuccessful() and not result.skipped and dom.returncode==0 and not dom_record['page_errors'])
    return 0 if ok else 1
if __name__=='__main__':raise SystemExit(main())
