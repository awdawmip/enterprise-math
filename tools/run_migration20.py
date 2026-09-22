#!/usr/bin/env python3
"""M20 shared BigInt carrier plus unchanged M18 regression in isolated groups.

M19's independent report-reader tests are not part of this focused source slice.
The Chromium arithmetic check is a separate command; neither gate is UI admission.
"""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
GROUPS=('test_multiplication_lab','test_angular_dispersion','test_certified_hex',
        'test_certified_hex_browser','test_angular_browser','test_multiplicative_exact',
        'test_multiplicative_readouts','test_multiplicative_machine','test_certified_hex_phase32',
        'test_phase32_lab','test_phase32_exact','test_phase32_cli_exact')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--new-only',action='store_true');args=p.parse_args()
    out=ROOT/'evidence/migration20';out.mkdir(parents=True,exist_ok=True)
    retained=None
    if not args.new_only:
        folder=out/'retained';folder.mkdir(exist_ok=True)
        for name in GROUPS:
            with (folder/f'{name}.log').open('w') as log:
                run=subprocess.run([sys.executable,str(ROOT/'tools/test_migration20_retained_group.py'),name],
                                   cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
            if run.returncode:
                print('retained group failed:',name,file=sys.stderr);return run.returncode
        rows=[json.loads((folder/f'{n}.json').read_text()) for n in GROUPS]
        retained={k:sum(r[k] for r in rows) for k in ('tests','passed','failures','errors','skips')}
    path=ROOT/'tools/nollm_visual_toolkit/tests/test_certified_hex_browser_phase32.py'
    spec=importlib.util.spec_from_file_location('m20_browser_tests',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    with (out/'new_tests.log').open('w') as log:
        result=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    policy=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),
                           'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py',
                           'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],
                          cwd=ROOT,capture_output=True,text=True)
    (out/'exact_policy.log').write_text(policy.stdout+policy.stderr)
    new=dict(tests=result.testsRun,passed=result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped),
             failures=len(result.failures),errors=len(result.errors),skips=len(result.skipped))
    record=dict(schema='M20_BROWSER_UINT32_TEST_RUN_V1',new=new,retained=retained,
                total=None if retained is None else {k:new[k]+retained[k] for k in new},
                exact_policy_exit=policy.returncode,execution='NODE_NATIVE_WEBCRYPTO_FULL_RECORD_COMPARISON',
                m19_reader_regression='NOT_EXECUTED_IN_THIS_SLICE',
                original_phase32_ui='NOT_MIGRATED_BY_THIS_NUMERICAL_SLICE')
    (out/('new_only.json' if args.new_only else 'tests.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped and policy.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
