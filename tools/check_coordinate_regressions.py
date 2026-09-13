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

def run(root,out):
    env=dict(os.environ,PYTHONPATH=str(root/'src'))
    result=subprocess.run([sys.executable,'-m','pytest','-q',*FILES,'--junitxml='+str(out)],cwd=root,env=env)
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
        assert old.keys()==new.keys(),'Changed regression population'
        old_fail={k:v for k,v in old.items() if v is not None}
        new_fail={k:v for k,v in new.items() if v is not None}
        assert new_fail.keys() <= old_fail.keys(),'New failing test: '+repr(new_fail.keys()-old_fail.keys())
        for key,value in new_fail.items():
            # Compare failure messages, not the surrounding traceback location.
            assert value.split('\n',1)[0]==old_fail[key].split('\n',1)[0],('Changed failure',key)
        result={'status':'NO_NEW_COORDINATE_REGRESSION','baseline_commit':BASE,
          'tests_executed_each':len(old),'baseline_failures':len(old_fail),
          'candidate_failures':len(new_fail),'candidate_passed':len(new)-len(new_fail),
          'complete_suite_green':not new_fail,
          'retained_failures':[{'test':'.'.join(k),'message':v.split('\n',1)[0]} for k,v in new_fail.items()]}
        print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
        for key,value in new_fail.items():print('UNCHANGED_BASELINE_FAILURE',key,value,flush=True)
    finally:
        subprocess.run(['git','worktree','remove','--force',str(base)],cwd=ROOT,check=True)

if __name__=='__main__':main()
