#!/usr/bin/env python3
"""Frozen R5 primitive-16 all-threshold exact local cyclotomic certificate.

Q[z]/Phi_16(z) = Q[z]/(z^8+1); independent DP checks 48 thresholds.
All scientific inputs are inherited from the cited pinned predecessor.
"""
from fractions import Fraction as Q
import json
from math import gcd

Z=(Q(0),)*8
I=(Q(1),)+(Q(0),)*7
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def scale(a,n): return tuple(n*x for x in a)
def mon(k):
    k%=16
    return tuple(Q(1) if i==k else Q(-1) if i+8==k else Q(0) for i in range(8))
def mul(a,b):
    v=[Q(0)]*16
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:v[(i+j)%16]+=x*y
    return tuple(v[i]-v[i+8] for i in range(8))
def inv_one_minus(k):
    order=16//gcd(16,k)
    v=Z
    for j in range(1,order):
        v=add(v,scale(mon(j*k),Q(-j,order)))
    assert mul(add(I,neg(mon(k))),v)==I
    return v

S0=set(range(214,219))
S1={214,216,217,218,219,220,221}
S2=set(range(215,222))
U=S0|S1|S2
sets=[(S0,1),(S1,1),(S2,1),(U,-2)]
assert U==set(range(214,222))
def numerator_one(S):
    pref=I
    for p in sorted(S): pref=mul(pref,add(I,neg(mon(p))))
    residues={p%16 for p in S}
    assert len(residues)==len(S)
    coeff=[pref]
    for r in range(1,16):
        if r in residues:continue
        dest=[Z]*(len(coeff)+1)
        for k,a in enumerate(coeff):
            dest[k]=add(dest[k],a)
            dest[k+1]=add(dest[k+1],neg(mul(a,mon(r))))
        coeff=dest
    return coeff
G=[Z]*11
for S,sgn in sets:
    for j,a in enumerate(numerator_one(S)):
        G[j]=add(G[j],scale(a,sgn))

expected=[
[16,10,-4,-10,-16,-18,-20,-22],
[-100,-76,-40,0,40,80,104,116],
[280,266,216,130,24,-90,-184,-250],
[-376,-444,-444,-372,-248,-84,92,252],
[232,380,476,496,440,320,148,-44],
[8,-136,-256,-344,-376,-352,-272,-152],
[-88,-24,44,108,152,172,164,136],
[24,12,4,-4,-8,-12,-20,-20],
[32,26,16,2,-8,-22,-24,-30],
[-20,-20,-16,-8,0,8,16,20],
[8,6,4,2,0,-2,-4,-6],
]
assert G==[tuple(Q(x) for x in row) for row in expected]
nonzero=[j+1 for j,a in enumerate(G) if a!=Z]
assert nonzero==list(range(1,12))
assert all(a!=Z for a in G)

# Separate recurrence implementation: first expand the infinite products
# at degree n, then sum n<m, with no use of polynomial G.
M=48
calc=[Z]*(M+1)
for S,sgn in sets:
    coeff=[Z]*M
    coeff[0]=I
    for p in sorted(S):
        for i in range(1,M):
            coeff[i]=add(coeff[i],mul(mon(p),coeff[i-1]))
    w=I
    for p in S: w=mul(w,add(I,neg(mon(p))))
    acc=Z
    for m in range(1,M+1):
        acc=add(acc,coeff[m-1])
        calc[m]=add(calc[m],scale(mul(w,acc),sgn))
for m in range(1,M+1):
    pred=G[(m-1)%16] if (m-1)%16 < len(G) else Z
    assert calc[m]==pred,m

# Predecessor m=1 result, with a different denominator convention.
prior=add(add(mul(mul(inv_one_minus(219),inv_one_minus(220)),
                  inv_one_minus(221)),inv_one_minus(215)),inv_one_minus(214))
prior=add(prior,scale(I,-2))
D=I
for p in range(214,222):
    D=mul(D,add(I,neg(mon(p))))
assert mul(prior,D)==G[0]
assert prior==(Q(-1),Q(1,2),Q(0),Q(1,2),Q(-1),Q(0),Q(0),Q(1))

free16=[p for p in range(214,315) if p%16==0]
assert free16==[224,240,256,272,288,304]
allsets=[S0,S1,S2,set(range(223,291)),set(range(296,313))]
for mask in range(1,32):
    union=set().union(*(allsets[i] for i in range(5) if (mask>>i)&1))
    if all(p not in union for p in free16):
        assert mask in {1,2,3,4,5,6,7}
    else:
        assert mask not in {1,2,3,4,5,6,7}
for d in range(19,315):
    assert sum(p%d==0 for p in range(214,315))<=5

classes={
    "both":11*12, "primitive16_only":11*5,
    "primitive17_only":5*12, "neither":5*5
}
assert sum(classes.values())==272
out={
    "schema":"R5_PRIMITIVE16_ALL_M_V1",
    "status":"EXACT_CHECKS_PASS",
    "cyclotomic_ring":"Q[z]/(z^8+1)",
    "nonzero_threshold_m_mod16":nonzero,
    "zero_threshold_m_mod16":[0,12,13,14,15],
    "polynomial_degree":10,
    "exact_numerator_coefficients":[[str(v) for v in row] for row in G],
    "independent_dp_thresholds":[1,M],
    "prior_m1_formula_verified":True,
    "least_period_at_remainder_O_m_N4":{
        "base":360360,
        "formula":"360360 * 2**I(m mod 16 in 1..11) * 17**I(m mod 17 in 1..12)",
        "classes_mod272":classes,
        "periods":{
            "both":12252240,
            "primitive16_only":720720,
            "primitive17_only":6126120,
            "neither":360360
        }
    },
    "review":"NOT_REVIEWED",
    "formal_task_result":"NOT_CREATED"
}
print(json.dumps(out,indent=2,sort_keys=True))
