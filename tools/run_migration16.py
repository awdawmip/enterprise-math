#!/usr/bin/env python3
"""M16 power-of-two phase-carrier extension gate; no caller/default cutover."""
from __future__ import annotations
import importlib.util, json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def main():
    retained=subprocess.run([sys.executable,str(ROOT/'tools/run_migration12.py')],cwd=ROOT,text=True,capture_output=True)
    if retained.returncode:
        sys.stdout.write(retained.stdout);sys.stderr.write(retained.stderr);return 1
    module=load(ROOT/'tools/nollm_visual_toolkit/tests/test_certified_hex_phase32.py','m16_phase32')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    policy=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),
        'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py',
        'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],cwd=ROOT)
    old=json.loads((ROOT/'evidence/migration12/tests.json').read_text())
    record={'schema':'M16_PHASE_CARRIER_VALIDATION_V1','retained_tests':old['tests'],
        'new_tests':result.testsRun,'total_tests':old['tests']+result.testsRun,
        'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),
        'retained_failures':old['failures'],'retained_errors':old['errors'],'retained_skips':old['skips'],
        'policy_exit':policy.returncode,'default_modulus':65536,'new_max_modulus':2**32,
        'reuse':'EXTEND_EXISTING_TOOL: same BRC division/root + dyadic/shared-radical certifier',
        'caller_cutover':False,'phase32_lab_migrated':False,
        'scope':'Generic power-of-two exact phase carrier required before Phase32 actual caller migration; no browser/default/native-X6 claim'}
    out=ROOT/'evidence/migration16';out.mkdir(parents=True,exist_ok=True);(out/'tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped and policy.returncode==0 else 1
if __name__=='__main__':raise SystemExit(main())
