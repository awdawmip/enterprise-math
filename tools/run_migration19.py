#!/usr/bin/env python3
"""M19 Phase32 report replay, retaining the pinned M18 gate without weakening it."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'tools/nollm_visual_toolkit')]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--new-only', action='store_true')
    args = parser.parse_args()
    out = ROOT/'evidence/migration19'
    out.mkdir(parents=True, exist_ok=True)
    retained = None
    if not args.new_only:
        run = subprocess.run([sys.executable, str(ROOT/'tools/run_migration18.py'),
                              '--out', str(out/'retained_tests.json')], cwd=ROOT,
                             capture_output=True, text=True)
        (out/'retained_tests.log').write_text(run.stdout+run.stderr, encoding='utf-8')
        if run.returncode:
            print(run.stdout); print(run.stderr, file=sys.stderr)
            return run.returncode
        retained = json.loads((out/'retained_tests.json').read_text())
    path = ROOT/'tools/nollm_visual_toolkit/tests/test_phase32_report.py'
    spec = importlib.util.spec_from_file_location('m19_phase32_report_tests', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    new = dict(tests=result.testsRun, passed=result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped),
               failures=len(result.failures), errors=len(result.errors), skips=len(result.skipped))
    record = dict(schema='M19_PHASE32_REPORT_REPLAY_TEST_RUN_V1',
                  new=new, retained=None if retained is None else {k:retained[k] for k in new},
                  total={k:new[k]+(retained[k] if retained else 0) for k in new},
                  finite_cases=module.COUNTS,
                  expected_template_skips=[] if retained is None else retained['expected_source_slice_skips'],
                  retained_policy_exit=None if retained is None else retained['policy_exit'],
                  source_scope='Phase32 machine reader + actual core.read_data; no new arithmetic/default/browser admission')
    (out/('new_tests.json' if args.new_only else 'tests.json')).write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))
    return 0 if result.wasSuccessful() and not result.skipped else 1


if __name__ == '__main__':
    raise SystemExit(main())
