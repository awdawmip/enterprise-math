#!/usr/bin/env python3
"""Exact 8-source observer-span check for R749SML; Python stdlib only.

All entries are fractions, ranks use Gauss-Jordan elimination over Q.
The finite grid validates the implementation; the accompanying proof covers all real channel parameters.
"""
from fractions import Fraction as Q
from itertools import product
import json
from collections import Counter

SIGNS = (-1, 1)
STATES = list(product(SIGNS, repeat=3))  # x,y,t
OUTS = list(product(SIGNS, repeat=3))  # u,v,w
GRID = (Q(-1), Q(-1,2), Q(0), Q(1,2), Q(1))

def kernels(alpha, beta, gamma):
    f, p = [], []
    for u, v, w in OUTS:
        rf, rp = [], []
        for x, y, t in STATES:
            z = lambda i: y if i == 1 else t
            rf.append((2+alpha*u*x)*(2+beta*v*z(u))*(2+gamma*w*y*t)/64)
            rp.append((2+gamma*w*y*t)/128 * sum(
                (2+i*x)*(1+alpha*u*i)*(2+beta*v*z(i)) for i in SIGNS
            ))
        f.append(rf)
        p.append(rp)
    return f, p

def rank(rows):
    a = [list(map(Q, row)) for row in rows]
    m,n=len(a),len(a[0]);pivot=0
    for j in range(n):
        k=next((i for i in range(pivot,m) if a[i][j]), None)
        if k is None:continue
        a[pivot],a[k]=a[k],a[pivot]
        t=a[pivot][j]
        a[pivot]=[q/t for q in a[pivot]]
        for i in range(m):
            if i!=pivot and a[i][j]:
                t=a[i][j]
                a[i]=[a[i][l]-t*a[pivot][l] for l in range(n)]
        pivot+=1
        if pivot==m:break
    return pivot

def predicted_joint_rank(a,b,c):
    if b==0:return (2 if a else 1)*(2 if c else 1)
    if c:return 5 if a==0 else 8
    if a==0 or a==1:return 4
    return 6

def predicted_single_ranks(a,b,c):
    if b==0:
        r=(2 if a else 1)*(2 if c else 1)
        return r,r
    return ((3 if c==0 else 4) if a==0 else (4 if c==0 else 8),
            (2 if c==0 else 4) if a==0 else (4 if c==0 else 8))

def apply(mat, prior):
    return [sum(v*p for v,p in zip(row,prior)) for row in mat]

def total_variation(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))/2

def witness(h, f, p):
    muplus=[(1+Q(h(x,y,t),6))/8 for x,y,t in STATES]
    muminus=[(1-Q(h(x,y,t),6))/8 for x,y,t in STATES]
    assert min(muplus+muminus)>0
    return total_variation(apply(f,muplus),apply(f,muminus)),total_variation(apply(p,muplus),apply(p,muminus))

def run():
    counts=Counter(); n=0; maxrank=0
    for a,b,c in product(GRID,repeat=3):
        f,p=kernels(a,b,c)
        for ch in (f,p):
            assert all(q>=0 for row in ch for q in row)
            assert all(sum(ch[i][j] for i in range(8))==1 for j in range(8))
        rf,rp=rank(f),rank(p)
        assert (rf,rp)==predicted_single_ranks(a,b,c), (a,b,c,rf,rp)
        rj=rank(f+p)
        assert rj==predicted_joint_rank(a,b,c), (a,b,c,rj)
        counts[str(rj)]+=1;n+=1;maxrank=max(rj,maxrank)
    f,p=kernels(Q(-1),Q(1,2),Q(0))
    tv_one=witness(lambda x,y,t: y*(1+2*x),f,p)
    tv_two=witness(lambda x,y,t: y*(1-2*x),f,p)
    assert tv_one==(Q(0),Q(1,24)),tv_one
    assert tv_two==(Q(1,24),Q(0)),tv_two
    # Basis span certificates in the three nontrivial singular strata.
    one=lambda x,y,t: Q(1)
    x=lambda x,y,t: Q(x)
    y=lambda x,y,t: Q(y)
    t=lambda x,y,t: Q(t)
    xy=lambda x,y,t: Q(x*y)
    xt=lambda x,y,t: Q(x*t)
    yt=lambda x,y,t: Q(y*t)
    xdiff=lambda x,y,t: Q(x*(y-t))
    cases=[
        (Q(-1),Q(1,2),Q(0),(one,x,y,t,xy,xt),6),
        (Q(0),Q(1,2),Q(0),(one,y,t,xdiff),4),
        (Q(0),Q(1,2),Q(1,2),(one,y,t,yt,xdiff),5),
    ]
    for a,b,c,funcs,r in cases:
        ff,pp=kernels(a,b,c)
        rows=[[func(*s) for s in STATES] for func in funcs]
        assert rank(rows)==r and rank(rows+ff+pp)==r
    return {
        'result':'PASS','arithmetic':'exact rational Fraction, no floats',
        'grid_parameters':[str(q) for q in GRID],
        'parameter_triples':n,
        'normalized_single_channel_source_columns':n*2*8,
        'joint_rank_counts':dict(sorted(counts.items(),key=lambda q:int(q[0]))),
        'individual_and_joint_rank_verifications':n*3,
        'nontrivial_basis_span_certificates':len(cases),
        'positive_prior_witness_F_invisible_P_visible_TV': [str(q) for q in tv_one],
        'positive_prior_witness_P_invisible_F_visible_TV': [str(q) for q in tv_two],
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'scope':'conditional signed-Port observer; no native V29/V39 certification'
    }

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
