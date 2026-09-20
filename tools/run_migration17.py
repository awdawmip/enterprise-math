#!/usr/bin/env python3
"""M17 Phase32 actual-caller gate layered on published M16 carrier support."""
from __future__ import annotations
import importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def main():
    retained=subprocess.run([sys.executable,str(ROOT/'tools/run_migration16.py')],cwd=ROOT,text=True,capture_output=True)
    if retained.returncode:
        sys.stdout.write(retained.stdout);sys.stderr.write(retained.stderr);return 1
    old=load(ROOT/'evidence/migration17/frozen_test_phase32_lab.py','m17_old_phase32')
    new=load(ROOT/'tools/nollm_visual_toolkit/tests/test_phase32_exact.py','m17_exact_phase32')
    expected_skips=0
    template=ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit/phase32_lab.html'
    if not template.exists():
        old.Tests.test_deterministic_html_and_config=unittest.skip('unchanged phase32_lab.html absent from source slice')(old.Tests.test_deterministic_html_and_config)
        old.Tests.test_site_three_pages_and_manifest=unittest.skip('unchanged phase32_lab.html absent from source slice')(old.Tests.test_site_three_pages_and_manifest)
        expected_skips=2
    suite=unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromModule(old),unittest.defaultTestLoader.loadTestsFromModule(new)])
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    m16=json.loads((ROOT/'evidence/migration16/tests.json').read_text())
    record={'schema':'M17_PHASE32_CALLER_VALIDATION_V1','retained_m16_tests':m16['total_tests'],
            'phase32_original_tests':17,'new_phase32_tests':12,'total_tests':m16['total_tests']+result.testsRun,
            'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),
            'expected_source_slice_skips':expected_skips,
            'source_slice_skip_reason':'unchanged phase32_lab.html package data absent; numerical/API tests not skipped',
            'phase_modulus':2**32,'exact_pitch':'explicit positive integer ratio; never inferred from config.pitch',
            'tie_rule':'MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC',
            'base_tie_rule_preserved_as_certificate':True,'default_changed':False,'browser_changed':False,
            'reuse':'M16 certified population + M06 lexicographic tie adapter + AngularDispersion/BRC readout'}
    out=ROOT/'evidence/migration17';out.mkdir(parents=True,exist_ok=True);(out/'tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if result.wasSuccessful() and len(result.skipped)==expected_skips else 1
if __name__=='__main__':raise SystemExit(main())
