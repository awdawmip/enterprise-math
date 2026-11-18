#!/usr/bin/env python3
"""Compare targeted old tests against the exact pre-migration main snapshot.

No test is skipped or marked as passed because it failed before. The gate is
explicitly NO_NEW_REGRESSION; existing failures are printed with their evidence.
A complete clean-suite claim is not made when any baseline failure remains.
"""
from pathlib import Path
import hashlib
import json, os, subprocess, sys, tempfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='366a7517c3baf91ade267c972833fe722902519c'
FILES=['tests/test_lattice_geometry.py','tests/test_material_loop_geometry.py',
 'tests/test_p012_geometry.py','tests/test_p022_hcp_geometry.py',
 'tests/test_p023_operation_quotient.py','tests/test_partial_operation_quotient.py',
 'tests/test_x6_current_publication_integrity_isolation.py']

# dd7b10b retired fixed-heading admission. These four tests specify its
# successor contract; their opposite expectations are not equivalent failures.
X6_REVISION = 'dd7b10b680fc7a0c69e551ccf793f7e77d131b65'
X6_TEST_FILE = 'tests/test_x6_current_publication_integrity_isolation.py'
X6_TEST_BLOB = 'fcc87fd7e0528ab7d2bf028deba0e982896aecc4'
X6_CLASS = 'X6CurrentPublicationIntegrityIsolationTests'
X6_JUNIT_CLASS = X6_TEST_FILE.removesuffix('.py').replace('/', '.') + '.' + X6_CLASS
X6_SUCCESSORS = {
    'test_six_exact_records_and_four_actual_errors_are_pinned':
        'test_six_original_records_and_heading_diagnostics_remain_historical',
    'test_only_the_six_current_definitions_change_and_are_blocked':
        'test_retired_style_rows_have_no_remaining_publication_or_dispatch_effect',
    'test_twenty_four_errors_require_the_new_validated_isolation':
        'test_retired_heading_errors_need_no_envelope_or_audit_exception',
    'test_missing_and_invented_error_suppressions_fail_strict_audit':
        'test_retired_missing_style_is_ignored_but_invented_error_still_fails',
}


def compare_population(old, new):
    retired = {(X6_JUNIT_CLASS, name) for name in X6_SUCCESSORS}
    successors = {(X6_JUNIT_CLASS, name) for name in X6_SUCCESSORS.values()}
    removed = old.keys() - new.keys()
    missing = successors - new.keys()
    assert removed == retired and not missing, (
        'Changed regression population', 'missing or unexpected retirements', sorted(removed ^ retired),
        'missing ratified successors', sorted(missing))
    for key in new.keys() - old.keys():
        assert new[key] is None, ('Failed successor contract' if key in successors else 'New failing test',
                                  key, new[key])
    for key in old.keys() & new.keys():
        if new[key] is not None:
            # Only the checkout path is normalized in run(). Match every
            # character of a retained failure; a new failure always fails.
            assert old[key] == new[key], ('New or changed failure', key, new[key], old[key])


def verify_successor_evidence(root, tmp):
    # The candidate run already executed the exact ratified suite in this case.
    raw = (root / X6_TEST_FILE).read_bytes()
    digest = hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest()
    if digest == X6_TEST_BLOB:
        return 'CURRENT_TEST_FILE_MATCHES_RATIFIED_BLOB'

    # Later test improvements are allowed. Independently run the four ratified
    # assertions against the candidate implementation, even if a current test
    # was weakened under its old name. Keep the original test's repository ROOT.
    if subprocess.run(['git', 'cat-file', '-e', X6_TEST_BLOB], cwd=root).returncode:
        subprocess.run(['git', 'fetch', '--no-tags', '--depth=1', 'origin', X6_REVISION],
                       cwd=root, check=True)
    approved = subprocess.check_output(['git', 'cat-file', 'blob', X6_TEST_BLOB], cwd=root)
    with tempfile.NamedTemporaryFile(dir=root / 'tests', prefix='test_ratified_x6_', suffix='.py') as test:
        test.write(approved)
        test.flush()
        targets = [f'{test.name}::{X6_CLASS}::{name}' for name in X6_SUCCESSORS.values()]
        observed = run(root, tmp / 'x6-successors.xml', targets)
        assert len(observed) == len(targets) and {name for _, name in observed} == set(X6_SUCCESSORS.values())
        assert all(value is None for value in observed.values()), ('Ratified X6 contract failed', observed)
    return 'RATIFIED_ASSERTIONS_EXECUTED_ON_CANDIDATE'


def run(root, out, targets=FILES):
    env=dict(os.environ,PYTHONPATH=str(root/'src'))
    result=subprocess.run([sys.executable,'-m','pytest','-q',*targets,'--junitxml='+str(out)],cwd=root,env=env)
    if result.returncode not in (0,1):raise RuntimeError('Test infrastructure failure: '+str(result.returncode))
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

def main():
    tmp=Path(tempfile.mkdtemp(prefix='em-coordinate-regression-',dir=os.environ.get('RUNNER_TEMP')))
    base=tmp/'baseline'
    subprocess.run(['git','fetch','--no-tags','--depth=1','origin',BASE],cwd=ROOT,check=True)
    subprocess.run(['git','worktree','add','--detach',str(base),BASE],cwd=ROOT,check=True)
    try:
        old=run(base,tmp/'baseline.xml')
        new=run(ROOT,tmp/'candidate.xml')
        compare_population(old, new)
        evidence = verify_successor_evidence(ROOT, tmp)
        old_fail={k:v for k,v in old.items() if v is not None}
        new_fail={k:v for k,v in new.items() if v is not None}
        result={'status':'NO_NEW_COORDINATE_REGRESSION','baseline_commit':BASE,
          'baseline_tests_executed':len(old),'candidate_tests_executed':len(new),
          'baseline_failures':len(old_fail),
          'candidate_failures':len(new_fail),'candidate_passed':len(new)-len(new_fail),
          'complete_suite_green':not new_fail,
          'unchanged_test_ids':len(old.keys() & new.keys()),
          'additional_passing_tests':sorted('.'.join(k) for k in new.keys() - old.keys()
                                            if k not in {(X6_JUNIT_CLASS, n) for n in X6_SUCCESSORS.values()}),
          'successor_contracts':{'revision': X6_REVISION, 'evidence': evidence,
            'tests': X6_SUCCESSORS, 'superseded_baseline_failures': sorted(
                '.'.join(key) for key in old_fail.keys() - new.keys())},
          'retained_failures':[{'test':'.'.join(k),'detail':v} for k,v in new_fail.items()]}
        if len(old) == len(new):
            result['tests_executed_each'] = len(old)
        print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
    finally:
        subprocess.run(['git','worktree','remove','--force',str(base)],cwd=ROOT,check=True)

if __name__=='__main__':main()
