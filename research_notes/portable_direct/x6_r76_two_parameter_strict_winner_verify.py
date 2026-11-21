#!/usr/bin/env python3
"""Exact rational checks for X6 R76. Conditional BRC model, not native X6."""
from fractions import Fraction as F
from itertools import combinations, product
import json

ATLAS = [
(1, 1, 0, 0), (2, 0, 2, -1), (3, 1, -3, 1), (3, 2, -3, 1),
(3, 3, -1, 0), (4, 1, 3, -1), (4, 3, -4, 1), (4, 4, -1, 0),
(5, 3, 2, -1), (5, 4, -4, 1), (5, 5, -1, 0), (6, 5, -4, 1),
(6, 6, -1, 0), (7, 3, -7, 2), (7, 6, -4, 1), (7, 7, -1, 0),
(9, 7, 2, -1), (10, 9, -5, 1), (11, 10, -5, 1), (16, 15, -6, 1),
(22, 21, -7, 1), (27, 24, -14, 3), (39, 36, -16, 3),
(43, 39, -20, 4), (47, 42, -24, 5), (49, 45, -21, 4),
(71, 66, -28, 5), (125, 114, -56, 11),
]
PAIRS=list(combinations(range(4),2))
STAR=(114,-56,11)
LOW=(10,-5,1)
HIGH=(45,-21,4)

def moment(a):
    return tuple(sum(a[d-2]*(d**k-d) for d in (2,3,4)) for k in (1,2,3,4))

def population(a):
    return max(sum(max(0,x) for x in a),sum(max(0,-x) for x in a))

def pair_radius(a,weights):
    z=moment(a)
    return max(F(abs(z[j]-z[i]),2)/(weights[i]+weights[j]) for i,j in PAIRS)

def fine_bound(a,u):
    z=moment(a)
    return max(F(abs(z[2]),2)/(1+u),F(abs(z[3]),4),F(abs(z[3]-z[2]),2)/(1+u))

def m_value(u):
    return min(max(F(1,2),1/(1+u)),3/(1+u))

def threshold(u):
    return 12+11*u if u<=1 else (F(23) if u<=5 else 4*u+3)

assert population(STAR)==125 and moment(STAR)==(0,24,0,0)
assert population(LOW)==11 and moment(LOW)==(0,2,0,2)
assert population(HIGH)==49 and moment(HIGH)==(0,12,6,0)
assert all(population(row[1:])==row[0] for row in ATLAS)
assert len(ATLAS)==28

# Direct finite check of the new independent congruence lower bound.
checked=0
for a in product(range(-12,13),repeat=3):
    if a==(0,0,0): continue
    checked+=1
    z=moment(a)
    assert z[2]%6==0 and z[3]%2==0
    if z[2]==0 and z[3]==0:
        # Primitive integer kernel is exactly STAR times an integer.
        assert a[0]*STAR[1]==a[1]*STAR[0]
        assert a[0]*STAR[2]==a[2]*STAR[0]
    else:
        for u in (F(1,10),F(1),F(5),F(12)):
            assert fine_bound(a,u)>=m_value(u)

rows=[]
for u in (F(1,10),F(1,2),F(1),F(2),F(5),F(6),F(10),F(50)):
    T=threshold(u)
    for t in (F(1,10),F(1),T-F(1,7),T,T+F(1,7),2*T):
        weights=(F(1),t,u,F(1))
        E=F(12)/(t+min(F(1),u))
        candidate=[pair_radius(a[1:],weights) for a in ATLAS]
        before=min(candidate[:-1]); after=min(candidate)
        assert candidate[-1]==E
        # Strict-winner theorem: all positive t, u (tested rational profiles).
        if t>T:
            assert candidate[-1]<before
        elif t==T:
            assert candidate[-1]==before
        else:
            assert candidate[-1]>after
        # Exact large-t formula including 124-port side of the jump.
        if (u<=5 and t>=1) or (u>5 and t>=2*u+1):
            assert before==m_value(u)
            assert after==min(m_value(u),E)
        rows.append({'u':str(u),'t':str(t),'threshold':str(T),
                     'eta_124':str(before),'eta_125':str(after),
                     'star_radius':str(E),
                     'star_strict':candidate[-1]<before})

result={'schema':'X6_R76_TWO_PARAMETER_BRC_AUTHOR_CHECK_V1',
        'atlas_source':'R72 x6_r72_d4_sharp_saturation_results.json (28 candidates)',
        'tested_integer_vectors':checked,'tested_exact_rational_weight_profiles':len(rows),
        'assertions':'PASS','example_rows':[r for r in rows if r['u'] in ('1','6') and r['t']==r['threshold']],
        'proof_scope':'general symbolic proof in companion research note; finite checks are author verification',
        'unreviewed':True}
print(json.dumps(result,indent=2,ensure_ascii=False))
with open('x6_r76_two_parameter_strict_winner_results.json','w') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
