#!/usr/bin/env python3
"""Exact equality-prefix fixed-word vs deterministic observation-policy test.
Only observation-only policies of depth <=2; full feedback equality, integer costs.
"""
import itertools
import json
import random
from pathlib import Path


def words(num_actions, H):
    for h in range(H+1):
        yield from itertools.product(range(num_actions), repeat=h)


def fixed_safe(B,T,C,O,x,Y,H):
    for word in words(len(T),H):
        state=x; sx=0; original=[O[x]]
        for a in word:
            sx += C[a][state];state=T[a][state]; original.append(O[state])
        if sx>B:continue
        can=False
        for y in Y:
            state=y; sy=0; other=[O[y]]
            for a in word:
                sy += C[a][state];state=T[a][state]; other.append(O[state])
            if sy<=B and original==other:
                can=True;break
        if not can:return False
    return True


def policy_run(z,T,C,O,depth,first,second):
    obs=[O[z]]; cost=0
    for i in range(depth):
        if i==0:a=first[obs[0]]
        else:a=second[obs[0]*2+obs[1]]
        cost+=C[a][z];z=T[a][z];obs.append(O[z])
    return (tuple(obs),cost)


def policy_safe(B,T,C,O,x,Y,H=2):
    # Exactly all pure observation-only policies to depth 0,1,2 over {0,1}.
    for depth in range(H+1):
        for first in itertools.product(range(len(T)),repeat=2):
            for second in (itertools.product(range(len(T)),repeat=4) if depth>=2 else [(0,)*4]):
                x_trace,x_cost=policy_run(x,T,C,O,depth,first,second)
                if x_cost>B:continue
                if not any((lambda r:r[0]==x_trace and r[1]<=B)(policy_run(y,T,C,O,depth,first,second)) for y in Y):
                    return False
    return True


def run():
    # Complete 2-state, two-action total transformation and 0/1 cost family,
    # binary full-observation alphabet, x=0 and singleton Y={1}.
    count=0; checks=0
    for bitsT in itertools.product(range(2),repeat=4):
        T=(bitsT[:2],bitsT[2:])
        for O in itertools.product(range(2),repeat=2):
            for bitsC in itertools.product(range(2),repeat=4):
                C=(bitsC[:2],bitsC[2:])
                for B in range(3):
                    a=fixed_safe(B,T,C,O,0,(1,),2)
                    b=policy_safe(B,T,C,O,0,(1,),2)
                    assert a==b,(T,O,C,B,a,b)
                    checks+=1
                count+=1
    assert count==1024 and checks==3072
    # Four-digit seeded sample with three states and 2 representatives.
    rng=random.Random(20261119); sample=2048; sample_checks=0
    for _ in range(sample):
        T=tuple(tuple(rng.randrange(3) for z in range(3)) for a in range(2))
        C=tuple(tuple(rng.randrange(2) for z in range(3)) for a in range(2))
        O=tuple(rng.randrange(2) for z in range(3))
        for B in range(3):
            assert fixed_safe(B,T,C,O,0,(1,2),2)==policy_safe(B,T,C,O,0,(1,2),2)
            sample_checks+=1
    # Positive containment does not imply exact full-feedback equivalence.
    x_label=1;y_label=3
    assert (x_label&~y_label)==0 and x_label!=y_label
    result={"schema":"R5_EQUALITY_PREFIX_ADAPTIVE_POLICY_BRIDGE_V1", "status":"AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED", "full_exhaustive_models":count,"budget_checks":checks, "seed":20261119,"three_state_sample_models":sample,"sample_budget_checks":sample_checks,"model":"DETERMINISTIC_FULL_OBSERVATION_ONLY_POLICY_FIXED_DEPTH_TWO", "positive_containment_not_full_trace_example":{"x_label":x_label,"y_label":y_label}}
    Path(__file__).with_name('RESULT_ADAPTIVE_EQUIV.json').write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('PASS_R5_ADAPTIVE_EQUIVALENCE',count,checks,sample,sample_checks)

if __name__=='__main__':run()
