#!/usr/bin/env python3
"""M18 Phase32 machine caller plus frozen M17 numerical regression."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'evidence/migration18/tests.json');p.add_argument('--new-only',action='store_true');a=p.parse_args()
    names=['test_phase32_cli_exact'] if a.new_only else [
        'test_multiplication_lab','test_angular_dispersion','test_certified_hex','test_certified_hex_browser',
        'test_angular_browser','test_multiplicative_exact','test_multiplicative_readouts','test_multiplicative_machine',
        'test_certified_hex_phase32','test_phase32_lab','test_phase32_exact','test_phase32_cli_exact']
    modules=[load(ROOT/'tools/nollm_visual_toolkit/tests'/f'{n}.py','m18_'+n) for n in names]
    expected_skips=[]
    if not a.new_only and not (ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit/phase32_lab.html').exists():
        legacy=modules[names.index('test_phase32_lab')]
        for n in ('test_deterministic_html_and_config','test_site_three_pages_and_manifest'):
            setattr(legacy.Tests,n,unittest.skip('unchanged production Phase32 HTML absent from source slice')(getattr(legacy.Tests,n)))
            expected_skips.append(n)
    groups={n:unittest.defaultTestLoader.loadTestsFromModule(m).countTestCases() for n,m in zip(names,modules)}
    suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(m) for m in modules)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    policy=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),
                          'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py',
                          'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],cwd=ROOT,capture_output=True,text=True)
    print(policy.stdout,end='');print(policy.stderr,file=sys.stderr,end='')
    report=dict(schema='M18_PHASE32_MACHINE_CLI_TEST_RUN_V1',tests=result.testsRun,
                passed=result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped),
                failures=len(result.failures),errors=len(result.errors),skips=len(result.skipped),groups=groups,
                expected_source_slice_skips=expected_skips,new_tests=groups['test_phase32_cli_exact'],
                numerical_skips=sum(not any(t.id().endswith('.'+n) for n in expected_skips) for t,_ in result.skipped),
                policy_exit=policy.returncode,finite_cases=modules[-1].COUNTS,
                legacy_render_stub='ONE_NEW_ROUTING_TEST_ONLY_NOT_BROWSER_ACCEPTANCE',
                scope='Phase32 exact textual CLI and no-display config/report/data; not Phase32 browser/full installation/main admission')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() and len(result.skipped)==len(expected_skips) and policy.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
