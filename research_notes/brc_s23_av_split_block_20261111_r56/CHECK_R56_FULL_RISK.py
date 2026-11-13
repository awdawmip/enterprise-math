#!/usr/bin/env python3
"""R56 split-block full S23 risk crosscheck with pinned R55 evidence.
Fetch VERIFY_R55_FULL.py and R55_AFFINE_RUNS.tsv from R55 bundle/PR first.
"""
from VERIFY_R56 import split_ages, LO, HI, D
from VERIFY_R55_FULL import stages, compile_risk, M, H, independent_ages
from pathlib import Path
import json

stage_list=list(stages()); rows=[];check=0; used=set()
for n0,n1,s,a,i,c,j in stage_list:
    age, cost=split_ages(j,LO,D,M,H)
    assert age==split_ages(j,HI,D,M,H)[0]
    assert age==independent_ages(j,LO,D,M,H)
    rows.append((n0,n1,s,a,i,c,j,age));check+=1;used.add(j)
raw,risk=compile_risk(rows)
assert raw==Path(__file__).parent.joinpath('R55_AFFINE_RUNS.tsv').read_bytes()
result=dict(schema='R56_FULL_RISK_CROSSCHECK',stages=check,distinct_j=len(used),risk=risk,source_method='R56_two_block_Farey',oracle='R55_full_compiler_and_independent_ages',risk_reference='R55_AFFINE_RUNS.tsv')
Path(__file__).parent.joinpath('R56_RISK_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS_R56_FULL_RISK',result)
