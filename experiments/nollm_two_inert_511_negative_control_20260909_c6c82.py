#!/usr/bin/env python3
"""Exact rejected all-chiral selector witness; run beside the main experiment."""
from pathlib import Path
import hashlib, importlib.util, json, math, sys
from itertools import product
import numpy as np
root=Path(__file__).resolve().parent
paths=[root/'experiment.py',root/'nollm_two_inert_511_20260909_c6c82.py']
p=next((q for q in paths if q.exists()),None)
if p is None:raise FileNotFoundError("two-inert experiment required")
expected="db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4"
if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise ValueError("source mismatch")
spec=importlib.util.spec_from_file_location("two_inert",p)
m=importlib.util.module_from_spec(spec);sys.modules["two_inert"]=m;spec.loader.exec_module(m)
key=(1,1,0,2);scale=5;A=scale*m.H(*key);u=tuple(scale*v for v in m.ANCHORS[key])
good=m.section(A,u);poly=m.m.vertices(A)
lo=[math.ceil(min(v[i] for v in poly)) for i in (0,1)]
hi=[math.floor(max(v[i] for v in poly)) for i in (0,1)]
X=np.array(list(product(range(lo[0],hi[0]+1),range(lo[1],hi[1]+1))),dtype=np.int64)
bad=X[m.member(X,A,None)]
badkeys=set(map(tuple,m.m.coset_keys(bad,A)))
missing=[list(map(int,x)) for x,k in zip(good,m.m.coset_keys(good,A)) if tuple(k) not in badkeys]
assert len(bad)==len(badkeys)==1373 and len(good)==1375
assert missing==[[-23,-9],[23,9]] and u==(-15,10)
result=dict(status="PASS_NEGATIVE_CONTROL",basis=A.tolist(),expected=1375,
            naive_selected=1373,repaired=1375,missing_repaired_points=missing,anchor=u)
(root/"negative_control.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
