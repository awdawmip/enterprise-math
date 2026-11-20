#!/usr/bin/env python3
"""R5 low-excess-212 exact checker. stdlib only.
Place frozen EXACT_R5_ALL_101_BUDGETS.json, stages_18.json and prior
RESULT_R5_MIXED_ERASURE_RIGIDITY.json beside this script.
Re-run the original VERIFY_R5_MIXED_ERASURE_RIGIDITY.py for the
independent 32,640-pair recomputation of the predecessor's masks.
"""
import hashlib
import json
from pathlib import Path

P=Path(__file__).resolve().parent
SCIENCE_SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
assert hashlib.sha256((P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()).hexdigest()==SCIENCE_SHA
prior=json.loads((P/"RESULT_R5_MIXED_ERASURE_RIGIDITY.json").read_text())
sets=list(map(set,prior["minimal_sets"]))
assert len(sets)==5
assert sets[0]==set(range(214,219))
assert sets[1]=={214,216,217,218,219,220,221}
assert sets[2]=={215,216,217,218,219,220,221}
assert sets[3]==set(range(223,291)) and sets[4]==set(range(296,313))
weights=[72,72,72,223,296]
slack={k:k-sum(weights[i] for i in range(5) if k in sets[i]) for k in range(214,315)}
assert min(slack.values())==0
assert {k for k,s in slack.items() if s==0}=={216,223,296}
assert {k for k,s in slack.items() if s==1}=={217,224,297}
assert {k for k,s in slack.items() if s<213 and k not in (216,217,218,223,224,225,296,297,298)}==set(range(226,291))|set(range(299,313))|{214,215,219,220,221}
assert slack[222]==222

def early_min(r):
    feasible=[]
    for a in range(r+1):
        for b in range(r+1):
            for d in range(r+1):
                if min(a+b,a+d,b+d)>=r:
                    feasible.append((214*a+215*b+219*d-216*r,a,b,d))
    return min(feasible)
assert early_min(1)==(213,1,1,0)
assert early_min(2)==(216,1,1,1)
for r in range(3,12):
    assert early_min(r)[0]>=213

def multiset_coefficients(m, hi, cutoff):
    dp=[[0]*(cutoff+1) for _ in range(m+1)]
    dp[0][0]=1
    for value in range(hi+1):
        for count in range(1,m+1):
            for total in range(value,cutoff+1):
                dp[count][total]+=dp[count-1][total-value]
    return dp[m]

def mul(a,b,cutoff):
    out=[0]*(cutoff+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:cutoff+1-i]):
                if y:out[i+j]+=x*y
    return out

def spectrum(m,cutoff=212):
    return mul(mul(multiset_coefficients(m,2,cutoff),
                   multiset_coefficients(m,67,cutoff),cutoff),
               multiset_coefficients(m,16,cutoff),cutoff)

def independent_small(m,D):
    parts=[]
    for hi in (2,67,16):
        counts=[0]*(D+1)
        def enum(start,n,weight):
            if n==0:
                counts[weight]+=1
            else:
                for v in range(start,min(hi,D-weight)+1):
                    enum(v,n-1,weight+v)
        enum(0,m,0)
        parts.append(counts)
    return mul(mul(parts[0],parts[1],D),parts[2],D)[D]

res={"schema":"R5_NONADAPTIVE_LOW_EXCESS_212_V1",
     "frozen_sha256":SCIENCE_SHA,
     "original_pin":"awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551",
     "bound_excess_inclusive":212,
     "first_outside_block_excess":213,
     "gaussian_factors_top_minus_bottom":[2,67,16],
     "coefficients":{}}
for m in (1,2,3,17):
    coefficients=spectrum(m)
    for D in range(9):
        assert coefficients[D]==independent_small(m,D)
    assert coefficients[0:2]==[1,3]
    assert coefficients[2]==(6 if m==1 else 9)
    res["coefficients"][str(m)]={
       "D0_to_D15":[str(v) for v in coefficients[:16]],
       "D212":str(coefficients[212]),
       "sum_D0_to_D212":str(sum(coefficients))}
print(json.dumps(res,indent=2,ensure_ascii=False))
print("PASS: immutable frozen input; 5 masks; dual slacks; early minima; q-spectrum; small independent enumeration")
