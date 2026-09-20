#!/usr/bin/env python3
"""M14 retained arithmetic + installed-console package gate."""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(cmd):
    return subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)

def main():
    retained=run([sys.executable,str(ROOT/'tools/run_migration12.py')])
    installed=run([sys.executable,str(ROOT/'tools/test_migration14_installed.py')])
    if retained.returncode or installed.returncode:
        sys.stdout.write(retained.stdout);sys.stderr.write(retained.stderr)
        sys.stdout.write(installed.stdout);sys.stderr.write(installed.stderr)
        return 1
    retained_record=json.loads((ROOT/'evidence/migration12/tests.json').read_text())
    installed_record=json.loads((ROOT/'evidence/migration14/installed_console.json').read_text())
    record={
      'schema':'M14_INSTALLED_PACKAGE_VALIDATION_V1',
      'retained_tests':retained_record['tests'],
      'retained_failures':retained_record['failures'],
      'retained_errors':retained_record['errors'],
      'retained_skips':retained_record['skips'],
      'installed_checks':installed_record['checks'],
      'package_data_mode':installed_record['package_data_mode'],
      'enterprise_math_runtime':installed_record['enterprise_math_runtime'],
      'production_workbench_template_accepted':installed_record['production_workbench_template'],
      'full_enterprise_math_package_tested':False,
      'native_browser_navigation_tested':False,
      'scope':'M14 exact-extra packaging and installed nollm-viz console/data-reader dispatch; production package-data/native browser remain pending',
    }
    out=ROOT/'evidence/migration14/validation.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
