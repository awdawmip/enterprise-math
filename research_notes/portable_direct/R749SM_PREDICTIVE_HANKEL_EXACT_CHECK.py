"""R749SM exact signed-Port support/controller predictor: standard library only."""
from fractions import Fraction as Q
from itertools import product, combinations
import json

AXES = range(6)
SIGNS = (-1, 1)
P = Q(1, 2)
THETA = 8*P/(1+7*P)

def legal(A, B, C):
    return len(A)==len(B)==len(C)==2 and len(A&B)==len(B&C)==1 and A!=B and C!=B

def forced(A, B):
    return A ^ B

def update(A, B, signs, C):
    assert legal(A, B, C)
    new = next(iter(C-B))
    retained = {a: signs[a] for a in B}
    if C == forced(A, B):
        old = signs[new]
        return [(tuple(sorted({**retained, new: x}.items())),
                 (1 + THETA*x*old)/2) for x in SIGNS]
    return [(tuple(sorted({**retained, new: x}.items())), Q(1,2)) for x in SIGNS]

def propagate(A, B, dist, C):
    out = {}
    for tup, mass in dist.items():
        for nxt, weight in update(A, B, dict(tup), C):
            out[nxt] = out.get(nxt, Q(0)) + mass*weight
    assert sum(out.values()) == 1
    return out

def rank(mat):
    a = [[Q(x) for x in row] for row in mat]
    rows, cols = len(a), len(a[0]); r=0
    for c in range(cols):
        piv = next((i for i in range(r,rows) if a[i][c]), None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        v=a[r][c];a[r]=[x/v for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                v=a[i][c];a[i]=[a[i][j]-v*a[r][j] for j in range(cols)]
        r+=1
        if r==rows: break
    return r

def determinant(mat):
    a = [[Q(x) for x in row] for row in mat]
    n=len(a); assert all(len(row)==n for row in a)
    out=Q(1)
    for c in range(n):
        piv=next((i for i in range(c,n) if a[i][c]),None)
        if piv is None:return Q(0)
        if piv!=c:a[c],a[piv]=a[piv],a[c];out=-out
        t=a[c][c];out*=t
        for i in range(c+1,n):
            factor=a[i][c]/t
            for j in range(c,n):a[i][j]-=factor*a[c][j]
    return out

A0=frozenset((0,1));B0=frozenset((1,2)); C0=frozenset((2,3));C1=frozenset((3,4))
assert legal(A0,B0,C0) and C0!=forced(A0,B0)
assert legal(B0,C0,C1) and C1!=forced(B0,C0)
S=(C0,C1)
next_options={1:frozenset((2,4)),-1:frozenset((4,5))}
second_options={
 1:{1:frozenset((2,3)),-1:frozenset((2,5))},
 -1:{1:frozenset((3,5)),-1:frozenset((0,5))},
}
assert next_options[1]==forced(*S)
for a in SIGNS:
    C=next_options[a]
    assert legal(*S,C)
    assert second_options[a][1]==forced(S[1],C)
    for b in SIGNS:assert legal(S[1], C, second_options[a][b])

# All 120 unsigned directed supports have eight legal unsigned successor supports,
# each with two normalized signed outcomes at p=1/2.
source_edges=0; legal_choices=0; signed_rows=0
for A in map(frozenset, combinations(AXES,2)):
    for B in map(frozenset, combinations(AXES,2)):
        if len(A&B)!=1:continue
        source_edges += 1
        choices=[C for C in map(frozenset, combinations(AXES,2)) if legal(A,B,C)]
        assert len(choices)==8
        legal_choices+=len(choices)
        for values in product(SIGNS,repeat=3):
            signs=dict(zip(sorted(A|B),values))
            for C in choices:
                row=update(A,B,signs,C)
                assert len(row)==2 and sum(w for _,w in row)==1
                signed_rows+=1
assert source_edges==120 and legal_choices==960 and signed_rows==7680

# The two nonforced updates erase signs 0,1 but may retain them in private controller memory.
Z=list(product(SIGNS,repeat=2))
for z0,z1 in Z:
    start={tuple(sorted({0:z0,1:z1,2:s2}.items())):Q(1,2) for s2 in SIGNS}
    d1=propagate(A0,B0,start,C0)
    d2=propagate(B0,C0,d1,C1)
    assert len(d2)==8 and set(d2.values())=={Q(1,8)}
    for a,b in product(SIGNS,repeat=2):
        first=next_options[a]
        mid=propagate(*S,d2,first)
        last=propagate(S[1],first,mid,second_options[a][b])
        assert len(mid)==len(last)==8 and set(mid.values())==set(last.values())=={Q(1,8)}

# Private sign memories z0,z1; public first bit observes parity, second observes z0.
word1=[(-1,),(1,)]
word2=list(product(SIGNS,repeat=2))
L0=[[Q(1) for z in Z]]
L1=[[Q(2+a*z0*z1,4) for z0,z1 in Z] for (a,) in word1]
L2=[[Q(2+a*z0*z1,4)*Q(2+b*z0,4) for z0,z1 in Z] for a,b in word2]
assert rank(L0)==1 and rank(L1)==2 and rank(L2)==4
assert determinant(L2)==Q(1,16)
assert all(sum(L2[i][j] for i in range(4))==1 for j in range(4))
# Exact Walsh reconstruction for 625 rational priors and every observed word.
prior_tests=0
for weights in product(range(1,6),repeat=4):
    mu=[Q(w,sum(weights)) for w in weights]
    m_parity=sum(mu[i]*Z[i][0]*Z[i][1] for i in range(4))
    m0=sum(mu[i]*Z[i][0] for i in range(4))
    m1=sum(mu[i]*Z[i][1] for i in range(4))
    for k,(a,b) in enumerate(word2):
        exact=sum(L2[k][j]*mu[j] for j in range(4))
        assert exact == Q(1,4)*(1+Q(a,2)*m_parity+Q(b,2)*m0+Q(a*b,4)*m1)
    prior_tests+=1
print(json.dumps({"status":"PASS","model":"controlled-R749SF-sign-lift-p=1/2","unsigned_directed_supports":source_edges,"unsigned_next_support_pairs":legal_choices,"signed_conditional_rows":signed_rows,"private_histories":4,"first_step_rank":rank(L1),"two_step_rank":rank(L2),"two_step_determinant":"1/16","affine_predictive_coordinate_counts":{"H0":0,"H1":1,"H2":3},"positive_rational_prior_tests":prior_tests,"all_path_signed_marginals_uniform":True,"native_event_permission":False},sort_keys=True))
