#!/usr/bin/env python3
"""Compare targeted old tests against the exact pre-migration main snapshot.

No test is skipped or marked as passed because it failed before. The gate is
explicitly NO_NEW_REGRESSION; existing failures are printed with their evidence.
A complete clean-suite claim is not made when any baseline failure remains.
"""
from pathlib import Path
import json, os, subprocess, sys, tempfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='366a7517c3baf91ade267c972833fe722902519c'
FILES=['tests/test_lattice_geometry.py','tests/test_material_loop_geometry.py',
 'tests/test_p012_geometry.py','tests/test_p022_hcp_geometry.py',
 'tests/test_p023_operation_quotient.py','tests/test_partial_operation_quotient.py',
 'tests/test_x6_current_publication_integrity_isolation.py']

# dd7b10b680fc7a0c69e551ccf793f7e77d131b65 retired fixed-heading
# admission and replaced these four historical style-hold assertions. Compare
# their explicit successors; all baseline and candidate tests still execute.
# No other rename, class, path, added case or removed case is accepted here.
STYLE_HOLD_MIGRATION='dd7b10b680fc7a0c69e551ccf793f7e77d131b65'
STYLE_HOLD_CLASS='tests.test_x6_current_publication_integrity_isolation.X6CurrentPublicationIntegrityIsolationTests'
BASELINE_TEST_SUCCESSORS={
 (STYLE_HOLD_CLASS,'test_six_exact_records_and_four_actual_errors_are_pinned'):
   (STYLE_HOLD_CLASS,'test_six_original_records_and_heading_diagnostics_remain_historical'),
 (STYLE_HOLD_CLASS,'test_only_the_six_current_definitions_change_and_are_blocked'):
   (STYLE_HOLD_CLASS,'test_retired_style_rows_have_no_remaining_publication_or_dispatch_effect'),
 (STYLE_HOLD_CLASS,'test_twenty_four_errors_require_the_new_validated_isolation'):
   (STYLE_HOLD_CLASS,'test_retired_heading_errors_need_no_envelope_or_audit_exception'),
 (STYLE_HOLD_CLASS,'test_missing_and_invented_error_suppressions_fail_strict_audit'):
   (STYLE_HOLD_CLASS,'test_retired_missing_style_is_ignored_but_invented_error_still_fails'),
}

def read_report(root,out):
    cases=list(ET.parse(out).getroot().iter('testcase'))
    assert cases,'NO_TESTS_RAN'
    records={}
    for case in cases:
        key=(case.get('classname'),case.get('name'))
        assert key not in records
        problem=case.find('failure')
        error=case.find('error')
        skipped=case.find('skipped')
        assert error is None and skipped is None,'Test errors/skips require explicit investigation'
        records[key]=None if problem is None else (problem.get('message','')+'\n'+(problem.text or '')).replace(str(root),'$ROOT')
    return records

def run(root,out):
    env=dict(os.environ,PYTHONPATH=str(root/'src'))
    result=subprocess.run([sys.executable,'-m','pytest','-q',*FILES,'--junitxml='+str(out)],cwd=root,env=env)
    if result.returncode not in (0,1):raise RuntimeError('Test infrastructure failure: '+str(result.returncode))
    return read_report(root,out)

def compare(old,new):
    historical={}
    required_pass=set()
    migrated=0
    for key,value in old.items():
        successor=BASELINE_TEST_SUCCESSORS.get(key,key)
        assert successor not in historical,'Duplicate historical test successor: '+repr(successor)
        historical[successor]=value
        migrated+=successor!=key
        if successor!=key:
            required_pass.add(successor)
    assert historical.keys()==new.keys(),('Changed regression population',
      'missing',sorted(historical.keys()-new.keys()),'added',sorted(new.keys()-historical.keys()))
    # These four assertions changed policy meaning, not just spelling. Their
    # successors must pass; an old failure is no exception for the new policy.
    assert all(new[key] is None for key in required_pass),('Changed-policy successor failed',
      sorted(key for key in required_pass if new[key] is not None))
    old_fail={k:v for k,v in historical.items() if v is not None}
    new_fail={k:v for k,v in new.items() if v is not None}
    assert new_fail.keys() <= old_fail.keys(),'New failing test: '+repr(new_fail.keys()-old_fail.keys())
    for key,value in new_fail.items():
        # Only the checkout path is normalized; every failure message and
        # detail must match, not merely a generic AssertionError heading.
        assert value==old_fail[key],('Changed failure',key,value,old_fail[key])
    return {'status':'NO_NEW_COORDINATE_REGRESSION','baseline_commit':BASE,
      'tests_executed_each':len(old),'baseline_failures':len(old_fail),
      'candidate_failures':len(new_fail),'candidate_passed':len(new)-len(new_fail),
      'complete_suite_green':not new_fail,
      'historical_test_migration':{'source_commit':STYLE_HOLD_MIGRATION,'matched_cases':migrated},
      'retained_failures':[{'test':'.'.join(k),'detail':v} for k,v in new_fail.items()]}

def main():
    tmp=Path(tempfile.mkdtemp(prefix='em-coordinate-regression-',dir=os.environ.get('RUNNER_TEMP')))
    base=tmp/'baseline'
    subprocess.run(['git','fetch','--no-tags','--depth=1','origin',BASE],cwd=ROOT,check=True)
    subprocess.run(['git','worktree','add','--detach',str(base),BASE],cwd=ROOT,check=True)
    try:
        old=run(base,tmp/'baseline.xml')
        new=run(ROOT,tmp/'candidate.xml')
        result=compare(old,new)
        print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
    finally:
        subprocess.run(['git','worktree','remove','--force',str(base)],cwd=ROOT,check=True)

if __name__=='__main__':main()
