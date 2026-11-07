#!/usr/bin/env python3
"""Compare targeted old tests against the exact pre-migration main snapshot.

No test is skipped or marked as passed because it failed before. The gate is
explicitly NO_NEW_REGRESSION; existing failures are printed with their evidence.
A complete clean-suite claim is not made when any baseline failure remains.
"""
from pathlib import Path
import hashlib, json, os, subprocess, sys, tempfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='366a7517c3baf91ade267c972833fe722902519c'
FILES=['tests/test_lattice_geometry.py','tests/test_material_loop_geometry.py',
 'tests/test_p012_geometry.py','tests/test_p022_hcp_geometry.py',
 'tests/test_p023_operation_quotient.py','tests/test_partial_operation_quotient.py',
 'tests/test_x6_current_publication_integrity_isolation.py']

# This is a semantic contract transition, not a rename/equivalence table.
# dd7b10b6 retired heading-only admission failures while retaining substantive
# content, immutable-byte, record-schema and real fault-isolation protections.
EVOLUTION_COMMIT='dd7b10b680fc7a0c69e551ccf793f7e77d131b65'
EVOLUTION_FILE='tests/test_x6_current_publication_integrity_isolation.py'
EVOLUTION_POLICY='research_task_publication_contract_v2.json'
BEFORE_TEST_BLOB='702e367b7fafb73a4a366ee2c2c90e32790301bf'
AFTER_TEST_BLOB='fcc87fd7e0528ab7d2bf028deba0e982896aecc4'
EVOLUTION_CLASS='tests.test_x6_current_publication_integrity_isolation.X6CurrentPublicationIntegrityIsolationTests'
BEFORE_CASES={
 'test_six_exact_records_and_four_actual_errors_are_pinned',
 'test_only_the_six_current_definitions_change_and_are_blocked',
 'test_twenty_four_errors_require_the_new_validated_isolation',
 'test_missing_and_invented_error_suppressions_fail_strict_audit',
}
AFTER_CASES={
 'test_six_original_records_and_heading_diagnostics_remain_historical',
 'test_retired_style_rows_have_no_remaining_publication_or_dispatch_effect',
 'test_retired_heading_errors_need_no_envelope_or_audit_exception',
 'test_retired_missing_style_is_ignored_but_invented_error_still_fails',
}

def require(condition,message):
    if not condition:raise AssertionError(message)

def git_blob_sha1(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def validate_evolution_sources(baseline,current):
    require(git_blob_sha1(baseline/EVOLUTION_FILE)==BEFORE_TEST_BLOB,
            'Historical semantic-evolution test source changed')
    require(git_blob_sha1(current/EVOLUTION_FILE)==AFTER_TEST_BLOB,
            'Current semantic-evolution test source requires explicit review')
    policy=json.loads((current/EVOLUTION_POLICY).read_text(encoding='utf-8'))
    invariants=policy.get('core_invariants',[])
    require(policy.get('body_style_required') is False
            and 'mandatory_body_sections' not in policy
            and 'V2_PUBLICATION_REQUIRES_FILLED_MANDATORY_BODY_SECTIONS' not in invariants
            and 'V2_PUBLICATION_REQUIRES_SUBSTANTIVE_NONPLACEHOLDER_BODY' in invariants,
            'Current publication policy does not support the registered semantic evolution')

def parse_report(root,out):
    cases=list(ET.parse(out).getroot().iter('testcase'))
    require(cases,'NO_TESTS_RAN')
    records={}
    for case in cases:
        key=(case.get('classname'),case.get('name'))
        require(all(isinstance(x,str) and x for x in key),'Missing test identity')
        require(key not in records,'Duplicate test identity: '+repr(key))
        problem=case.find('failure')
        error=case.find('error')
        skipped=case.find('skipped')
        require(error is None and skipped is None,
                'Test errors/skips require explicit investigation')
        records[key]=None if problem is None else (problem.get('message','')+'\n'+(problem.text or '')).replace(str(root),'$ROOT')
    return records

def run(root,out):
    env=dict(os.environ,PYTHONPATH=str(root/'src'))
    result=subprocess.run([sys.executable,'-m','pytest','-q',*FILES,'--junitxml='+str(out)],cwd=root,env=env)
    if result.returncode not in (0,1):raise RuntimeError('Test infrastructure failure: '+str(result.returncode))
    return parse_report(root,out)

def compare_results(old,new,baseline,current):
    removed=set(old)-set(new)
    added=set(new)-set(old)
    before={(EVOLUTION_CLASS,name) for name in BEFORE_CASES}
    after={(EVOLUTION_CLASS,name) for name in AFTER_CASES}
    evolutions=[]
    if removed or added:
        # Unknown additions, deletions and renames still fail. Accept only this
        # complete, source-pinned transition, never fuzzy or pairwise aliases.
        require(removed==before and added==after,
                ('Changed regression population outside registered semantic evolution',
                 sorted(removed),sorted(added)))
        validate_evolution_sources(baseline,current)
        require(all(new[key] is None for key in after),
                'Current semantic-evolution tests must all pass')
        evolutions.append({
          'id':'TASKBOOK_HEADING_ADMISSION_RETIREMENT',
          'source_commit':EVOLUTION_COMMIT,
          'test_file':EVOLUTION_FILE,'policy_file':EVOLUTION_POLICY,
          'before_test_blob':BEFORE_TEST_BLOB,'after_test_blob':AFTER_TEST_BLOB,
          'same_semantics_claimed':False,
          'reason':'Fixed-heading admission was retired; substantive content and real publication defects remain checked.',
          'historical_cases':[{'test':'.'.join(k),'outcome':'passed' if old[k] is None else 'failed',
                              'detail':old[k]} for k in sorted(before)],
          'current_cases':[{'test':'.'.join(k),'outcome':'passed'} for k in sorted(after)],
        })
    else:
        before=set();after=set()
    # Preserve population equality for everything outside the reviewed change.
    require(set(old)-before==set(new)-after,'Changed shared regression population')
    old_fail={k:v for k,v in old.items() if v is not None}
    new_fail={k:v for k,v in new.items() if v is not None}
    require(new_fail.keys() <= old_fail.keys(),
            'New failing test: '+repr(new_fail.keys()-old_fail.keys()))
    for key,value in new_fail.items():
        # Normalize only checkout paths; failure messages and details must match.
        require(value==old_fail[key],('Changed failure',key,value,old_fail[key]))
    return {'status':'NO_NEW_COORDINATE_REGRESSION_WITH_DECLARED_SEMANTIC_EVOLUTION'
             if evolutions else 'NO_NEW_COORDINATE_REGRESSION',
      'baseline_commit':BASE,'tests_executed_each':len(old),
      'baseline_tests_executed':len(old),'candidate_tests_executed':len(new),
      'regression_population_unchanged':not evolutions,
      'shared_test_identities_compared':len(set(old)-before),
      'semantic_evolutions':evolutions,
      'baseline_failures':len(old_fail),'candidate_failures':len(new_fail),
      'candidate_passed':len(new)-len(new_fail),
      'candidate_suite_green':not new_fail,
      'complete_suite_green':not old_fail and not new_fail,
      'baseline_failure_evidence':[{'test':'.'.join(k),'detail':v} for k,v in sorted(old_fail.items())],
      'retained_failures':[{'test':'.'.join(k),'detail':v} for k,v in sorted(new_fail.items())]}

def main():
    tmp=Path(tempfile.mkdtemp(prefix='em-coordinate-regression-',dir=os.environ.get('RUNNER_TEMP')))
    base=tmp/'baseline'
    subprocess.run(['git','fetch','--no-tags','--depth=1','origin',BASE],cwd=ROOT,check=True)
    subprocess.run(['git','worktree','add','--detach',str(base),BASE],cwd=ROOT,check=True)
    try:
        old=run(base,tmp/'baseline.xml')
        new=run(ROOT,tmp/'candidate.xml')
        result=compare_results(old,new,base,ROOT)
        print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
    finally:
        subprocess.run(['git','worktree','remove','--force',str(base)],cwd=ROOT,check=True)

if __name__=='__main__':main()
