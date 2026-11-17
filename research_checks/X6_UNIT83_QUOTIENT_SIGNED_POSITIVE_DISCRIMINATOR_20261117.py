#!/usr/bin/env python3
"""Independent exact 6-axis length-3 signed/positive quotient-fiber discriminator.
Frozen reference: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3.
This is a new finite comparison; it does not rerun frozen native benchmarks.
"""
from collections import Counter
from itertools import combinations, product
from math import factorial
import json, hashlib
from pathlib import Path

D=6
ZERO=(0,)*D
STEPS_SIGNED=[(i,delta) for i in range(D) for delta in (-1,1)]
STEPS_POSITIVE=[(i,1) for i in range(D)]

def canonical(z):
    m=min(z)
    return tuple(x-m for x in z)

def pushforward(steps,length):
    current=Counter({ZERO:1})
    for _ in range(length):
        nxt=Counter()
        for z,cnt in current.items():
            for i,d in steps:
                w=list(z);w[i]+=d
                nxt[tuple(w)]+=cnt
        current=nxt
    observed=Counter()
    for z,cnt in current.items(): observed[canonical(z)]+=cnt
    return current,observed

signed_end,signed_obs=pushforward(STEPS_SIGNED,3)
positive_end,positive_obs=pushforward(STEPS_POSITIVE,3)
checks=0;rows=[]

def require(condition, description):
    if not condition:
        raise AssertionError(description)
for zeros in combinations(range(D),3):
    r=tuple(0 if i in zeros else 1 for i in range(D))
    zn=tuple(x-1 for x in r)
    zp=r
    require(canonical(zn)==r==canonical(zp), "same observer");checks+=1
    require(sum(abs(x) for x in zn)==3==sum(abs(x) for x in zp), "shortest length");checks+=1
    actual_endpoints={z:c for z,c in signed_end.items() if canonical(z)==r}
    require(actual_endpoints=={zn:factorial(3),zp:factorial(3)}, "signed fiber");checks+=1
    require(signed_obs[r]==12 and positive_obs[r]==6, "pushforward mass");checks+=1
    pos_endpoints={z:c for z,c in positive_end.items() if canonical(z)==r}
    require(pos_endpoints=={zp:6}, "positive fiber");checks+=1
    rows.append({"zeros":list(zeros),"relative_r":list(r),"signed_endpoints":[list(zn),list(zp)],"signed_counts":[6,6],"positive_endpoint":list(zp),"positive_count":6})
require(sum(signed_end.values())==12**3, "all signed labeled words")
require(sum(positive_end.values())==6**3, "all positive labeled words")
checks += 2
result={"schema":"EM_X6_UNIT83_TYPED_QUOTIENT_FIBER_CHECK_V1","science_pin":"fd2bcff10ca6e147348b6c1236027fc0d2877df3","native_steps":"12 signed one-axis steps","positive_steps":"6 positive one-axis steps","length":3,"selected_relative_observers":20,"signed_total_labeled_paths":sum(signed_end.values()),"positive_total_labeled_paths":sum(positive_end.values()),"checks":checks,"failed_checks":0,"relative_observer_signature_count_signed":len(signed_obs),"relative_observer_signature_count_positive":len(positive_obs),"fiber_witnesses":rows}
blob=json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
Path(__file__).with_name('X6_UNIT83_SIGNED_POSITIVE_QUOTIENT_RESULTS_20261117.json').write_bytes(blob+b'\n')
print(json.dumps({k:v for k,v in result.items() if k!='fiber_witnesses'},ensure_ascii=False,indent=2))
print('sha256',hashlib.sha256(blob+b'\n').hexdigest())
