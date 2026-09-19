#!/usr/bin/env python3
"""Reproduce slice 03 without silently skipping missing oracle dependencies.

This runs 58 source-slice tests, NOT full EM initialization, M02 browser tests,
HTML tests, whole-repository tests or independent review. M02 remains pinned.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]


def module_at(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    try:
        import mpmath
    except ImportError:
        raise SystemExit('mpmath is required for independent test oracles; no skips accepted')
    base=ROOT/'tools/nollm_visual_toolkit/tests'
    old=module_at(base/'test_multiplication_lab.py','m03_old_tests')
    omitted={'test_generated_html_reproducible_and_offline','test_gallery_embeds_preview_without_network'}
    suite=unittest.TestSuite(old.MultiplicationLabTests(n) for n in unittest.defaultTestLoader.getTestCaseNames(old.MultiplicationLabTests) if n not in omitted)
    for filename,name in [('test_angular_dispersion.py','m03_angular_tests'),('test_certified_hex.py','m03_exact_tests')]:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module_at(base/filename,name)))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    gate=subprocess.run([sys.executable,str(ROOT/'tools/check_exact_arithmetic_policy.py'),
        'tools/nollm_visual_toolkit/nollm_visual_toolkit/certified_hex.py',
        'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py'],cwd=ROOT)
    report={'schema':'M03_LOCAL_TEST_RUN_V1','tests':result.testsRun,'failures':len(result.failures),
            'errors':len(result.errors),'skips':len(result.skipped),'exact_gate_exit':gate.returncode,
            'mpmath_test_oracle_version':mpmath.__version__,'excluded_html_tests':sorted(omitted),
            'scope':'source slice only; browser, full package, repository and independent review not rerun'}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() and not result.skipped and gate.returncode==0 else 1

if __name__=='__main__':raise SystemExit(main())
