#!/usr/bin/env python3
"""Validate migration 02 locally. No installation, network or GitHub Actions.

Pure-kernel checks require Node. Add --browser for actual Chromium integration
(Playwright and an already-installed Chromium required). The bundle is a source
slice, not a full Enterprise Math checkout; its isolated EM initializer is not
production and must never be copied into the real repository.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT/'research_notes/integer_residual_migration02_20260919'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser', action='store_true')
    parser.add_argument('--chromium', default=shutil.which('chromium') or shutil.which('google-chrome'))
    parser.add_argument('--out', type=Path, default=ROOT/'out/migration02')
    args = parser.parse_args()
    if not shutil.which('node'):
        parser.error('Node is required; missing JS execution is not a passing migration')
    if sys.flags.optimize:
        parser.error('Run validation without -O so certificate assertions execute')
    args.out.mkdir(parents=True, exist_ok=True)
    sys.path[:0] = [str(ROOT/'tools/nollm_visual_toolkit'), str(ROOT/'src')]
    suite = unittest.defaultTestLoader.discover(str(ROOT/'tools/nollm_visual_toolkit/tests'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    tests_ok = result.wasSuccessful() and not result.skipped
    cmd = [sys.executable, str(ROOT/'tools/check_exact_arithmetic_policy.py'),
           str(ROOT/'tools/nollm_visual_toolkit/nollm_visual_toolkit/angular_dispersion.py')]
    gate = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=30)
    (args.out/'python_exact_gate.log').write_text(gate.stdout+gate.stderr)
    browser_exit = None
    if args.browser and tests_ok and gate.returncode == 0:
        cmd = [sys.executable, str(ROOT/'tools/nollm_visual_toolkit/tests/run_angular_browser_integration.py'),
               '--baseline', str(NOTE/'fixtures/multiplication_ui_baseline.py'), '--out', str(args.out/'browser_validation.json')]
        if args.chromium:
            cmd.extend(['--chromium', args.chromium])
        browser_run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=180)
        (args.out/'browser.log').write_text(browser_run.stdout+browser_run.stderr)
        browser_exit = browser_run.returncode
        print(browser_run.stdout)
        if browser_exit:
            print(browser_run.stderr, file=sys.stderr)
    init = ROOT/'src/enterprise_math/__init__.py'
    raw = init.read_bytes()
    init_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    summary = {
        'schema':'M02_LOCAL_RUN_V1', 'tests':result.testsRun, 'failures':len(result.failures),
        'errors':len(result.errors), 'skipped':len(result.skipped),
        'node':subprocess.check_output(['node','--version'], text=True).strip(),
        'python_exact_module_gate_exit':gate.returncode,
        'javascript_gate':'EXECUTED_CROSS_LANGUAGE_AND_BROWSER_TESTS_NOT_PYTHON_AST',
        'browser_requested':args.browser, 'browser_exit':browser_exit,
        'enterprise_initializer_blob':init_blob,
        'full_pinned_enterprise_initializer':init_blob=='66ceedcbfcba6a1447fd1297385700b1de63930a',
        'not_claimed':['whole-repository regression','independent review','main integration']}
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return 0 if tests_ok and gate.returncode == 0 and (not args.browser or browser_exit == 0) else 1


if __name__ == '__main__':
    raise SystemExit(main())
