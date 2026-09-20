#!/usr/bin/env python3
"""M07 CLI exact-scale gate layered on the M06 multiplicative-cell migration."""
from __future__ import annotations
import importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def main():
    exact=load(ROOT/'tools/nollm_visual_toolkit/tests/test_multiplicative_exact.py','m07_m06_exact')
    legacy=load(ROOT/'evidence/migration06/frozen_test_multiplicative.py','m07_m06_legacy')
    cli=load(ROOT/'tools/nollm_visual_toolkit/tests/test_multiplicative_cli_exact.py','m07_cli')
    expected_skips=0
    if not (ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit/multiplicative_lab.html').exists():
        legacy.MultiplicativeTests.test_deterministic_html=unittest.skip(
            'unchanged package-data template not materialized in source slice')(
            legacy.MultiplicativeTests.test_deterministic_html)
        expected_skips=1
    suite=unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromModule(exact),
        unittest.defaultTestLoader.loadTestsFromModule(legacy),
        unittest.defaultTestLoader.loadTestsFromModule(cli),
    ])
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={
        'schema':'M07_MULTIPLICATIVE_CLI_EXACT_TEST_RUN_V1',
        'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),
        'new_cli_tests':10,'m06_tests':35,
        'expected_source_slice_skip':expected_skips,
        'exact_scale_syntax':['INTEGER','FRACTION','DECIMAL'],
        'float_reverse_inference':False,
        'machine_output_scope':'--report/--hex-data only; legacy HTML/preview not represented as exact',
        'failure_atomicity':'exact field and requested hex exportability validated before any output write',
    }
    out=ROOT/'evidence/migration07';out.mkdir(parents=True,exist_ok=True)
    (out/'test_run.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if result.wasSuccessful() and len(result.skipped)==expected_skips else 1
if __name__=='__main__':raise SystemExit(main())
