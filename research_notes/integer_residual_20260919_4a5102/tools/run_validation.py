#!/usr/bin/env python3
"""Run local tests and produce a bounded, reproducible evidence report."""
import hashlib
import io
import json
from pathlib import Path
import platform
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tests'))
import test_integer_residual as tests

stream = io.StringIO()
suite = unittest.defaultTestLoader.loadTestsFromModule(tests)
result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
text = stream.getvalue()
print(text)
report = {'schema':'EM_INTEGER_RESIDUAL_VALIDATION_V1','python':platform.python_version(),
          'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
          'skipped':len(result.skipped),'success':result.wasSuccessful(),
          'enumerated_cases':tests.COUNTS,'enumerated_case_total':sum(tests.COUNTS.values()),
          'source_commit':'a6ef14fdc1dec284f9ca40875ae3acfb85e1b4b7',
          'coverage':'THREE_UNCHANGED_UPSTREAM_MODULES_PLUS_CANDIDATE_ADAPTER_AND_AST_INVENTORY_ONLY',
          'full_repository_regression_executed':False,
          'files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('src','tests','tools') for p in sorted((ROOT/folder).rglob('*.py'))}}
(ROOT/'evidence').mkdir(parents=True, exist_ok=True)
(ROOT/'evidence/test_output.txt').write_text(text)
(ROOT/'evidence/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(not result.wasSuccessful())
