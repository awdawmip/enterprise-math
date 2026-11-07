#!/usr/bin/env python3
"""Reproduce the EC49EXU bounded exact signed-X6 threshold batch.
Run from the same-PR sibling directory structure; Python3 and g++ C++17.
A timeout is unresolved and is never classified as a proof of E>=80.
"""
import hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'EC49EXT_H8_M5_TRIPLE_173_EXACT_DP'))
from VERIFY_EC49EXT import catalog,build_input,words
EXJ=ROOT/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'
exe=Path('/tmp/ec49exu_exact_dp')
subprocess.run(['g++','-O3','-std=c++17',str(EXJ/'EXACT_OR_MASK_DP.cpp'),'-o',str(exe)],check=True)
cases=[c for c in catalog() if 575<c['words']<=700]
assert len(cases)==102
timeout=float(os.environ.get('CASE_TIMEOUT','8'))
for c in cases:
    t=time.monotonic()
    schedule=c['schedule']
    inp,nodes,nwords=build_input(schedule)
    assert nwords==c['words']
    assert sum(len(words(h,*schedule[h-2])) for h in range(2,9))==c['words']
    colors=int(inp.splitlines()[0].split()[1]); assert colors<=24
    rec=dict(index=c['index'],words=nwords,nodes=nodes,colors=colors,
             input_sha256=hashlib.sha256(inp.encode()).hexdigest(),cutoff=80)
    try:
        proc=subprocess.run([str(exe),'80'],input=inp,text=True,
                            capture_output=True,timeout=timeout,check=True)
        rec['stdout']=proc.stdout.strip()
        if re.fullmatch(r'BOUND_PASS minimum_total_at_least=80 nodes=[0-9]+ colors=[0-9]+',rec['stdout']):
            rec['status']='EXCLUDED_E_LT_80'
        elif re.search(r'total=([0-9]+)',rec['stdout']):
            rec['status']='LOWER_COST_FEASIBLE';rec['cost']=int(re.search(r'total=([0-9]+)',rec['stdout']).group(1))
        else: rec['status']='UNRECOGNIZED_OUTPUT'
    except subprocess.TimeoutExpired:rec['status']='TIMEOUT_UNRESOLVED'
    rec['seconds']=round(time.monotonic()-t,3)
    print(json.dumps(rec,sort_keys=True),flush=True)
