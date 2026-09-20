#!/usr/bin/env python3
"""Reproduce the M13 machine-report reader source slice; no installation or remote execution."""
from __future__ import annotations
import argparse,importlib.util,json,shutil,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'evidence/migration13/tests.json')
    args=parser.parse_args()
    import mpmath
    if shutil.which('node') is None:raise RuntimeError('Node is required; no skipped acceptance')
    names=('test_multiplication_lab','test_angular_dispersion','test_certified_hex',
           'test_certified_hex_browser','test_angular_browser','test_multiplicative_exact',
           'test_multiplicative_readouts','test_multiplicative_machine','test_multiplicative_report')
    modules=[load(ROOT/'tools/nollm_visual_toolkit/tests'/f'{name}.py','m13_'+name) for name in names]
    counts={name:unittest.defaultTestLoader.loadTestsFromModule(mod).countTestCases()
            for name,mod in zip(names,modules)}
    suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(mod) for mod in modules)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    policy=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),
            'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py',
            'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py'],cwd=ROOT)
    record={'schema':'M13_MACHINE_REPORT_VALIDATION_V1','tests':result.testsRun,
            'new_reader_tests':counts['test_multiplicative_report'],'retained_tests':148,
            'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),
            'groups':counts,'finite_cases':{**modules[-3].COUNTS,**modules[-2].COUNTS,**modules[-1].COUNTS},'policy_exit':policy.returncode,
            'scope':'Existing core.read_data report import, deterministic replay, explicit browser seed projection and retained exact arithmetic; no HTML/DOM/native navigation/full-package or independent review',
            'retained_expectations_advanced_this_slice':0,
            'vm_host':'M10 exact readout function excerpts; unchanged modulus only; legacy dispatch stubs throw; no DOM/WebCrypto claim'}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped and policy.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
