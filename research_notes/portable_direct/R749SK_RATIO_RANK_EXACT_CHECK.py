#!/usr/bin/env python3
"""R749SK exact rational checks: rank-minimal posterior ratio carrier on X6 eight-lift signed supports.
Compatible with R749SJ frozen conditional forced/unsigned kernels. No native event assertion.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
import json

axes=range(6)
supports=[frozenset(c) for c in combinations(axes,2)]
edges=[(A,B) for A in supports for B in supports if len(A&B)==1]
assert len(edges)==120

def rank(mat):
    if not mat:return 0
    m=[list(map(Q,row)) for row in mat]
    i=0
    for j in range(len(m[0])):
        piv=next((k for k in range(i,len(m)) if m[k][j]),None)
        if piv is None:continue
        m[i],m[piv]=m[piv],m[i]
        v=m[i][j]
        m[i]=[a/v for a in m[i]]
        for k in range(len(m)):
            if k!=i and m[k][j]:
                z=m[k][j]
                m[k]=[m[k][l]-z*m[i][l] for l in range(len(m[0]))]
        i+=1
        if i==len(m):break
    return i

def w(x,mask):
    return Q(prod(x[i] for i in mask)) if mask else Q(1)

def coeff(values,cube,masks):
    return [sum(values[id(x)]*w(x,mask) for x in cube)/8 for mask in masks]

count=0
rankchecks=0
model_rows=0
for A,B in edges:
    old=next(iter(A-B)); shared=sorted(B); b=shared[0]
    C=A^B
    assert len(C)==2 and len(B&C)==1
    initial=sorted(A|B)
    masks=[tuple(initial[i] for i in range(3) if (bits>>i)&1) for bits in range(8)]
    cube=[dict(zip(initial,s)) for s in product((-1,1),repeat=3)]
    for p in (Q(0),Q(1,2),Q(1)):
        theta=8*p/(1+7*p)
        ell={id(x):Q(2+x[old]+x[b],4) for x in cube}
        N={id(x):ell[id(x)]*theta*x[old]*x[b] for x in cube}
        D={id(x):ell[id(x)] for x in cube}
        ccN=coeff(N,cube,masks)
        ccD=coeff(D,cube,masks)
        expectedN=[Q(0) for _ in range(8)];expectedD=[Q(0) for _ in range(8)]
        expectedD[0]=Q(1,2)
        for i,mask in enumerate(masks):
            if mask in ((old,),(b,)):
                expectedD[i]=Q(1,4);expectedN[i]=theta/4
            if mask==tuple(sorted((old,b))):expectedN[i]=theta/2
        assert ccN==expectedN and ccD==expectedD, (A,B,p,ccN,ccD)
        for x in cube:
            a=x[old]; bb=x[b]
            sumN=Q(0)
            for new,prob in ((a,(1+theta)/2),(-a,(1-theta)/2)):
                sumN+=ell[id(x)]*prob*new*bb
            assert sumN==N[id(x)]
            model_rows+=1
        coeff_rows=[ccN[1:],ccD[1:]] if theta>0 else []
        r=rank(coeff_rows)
        assert r==(0 if p==0 else 2)
        rankchecks+=1
        for idx in range(8):
            weights=[Q(1,2)*Q(1,8)+Q(1,2)*(Q(1) if j==idx else Q(0)) for j in range(8)]
            d=sum(weights[k]*D[id(x)] for k,x in enumerate(cube))
            n=sum(weights[k]*N[id(x)] for k,x in enumerate(cube))
            assert d>0
            u=sum(weights[k]*(x[old]+x[b]) for k,x in enumerate(cube))
            v=sum(weights[k]*x[old]*x[b] for k,x in enumerate(cube))
            assert n/d==theta*(2*v+u)/(2+u)
            count+=1
assert count==120*3*8 and model_rows==120*3*8
result={"status":"PASS",
"model":"R749SF conditional forced signed-Port edge, augmented hidden-sign gate",
"unsigned_directed_supports":len(edges),"parameters":["0","1/2","1"],
"forced_kernel_row_checks":model_rows,
"exact_mixture_ratio_checks":count,
"exact_walsh_coefficient_and_rank_checks":rankchecks,
"minimal_affine_coordinate_ranks":{"p=0":0,"p=1/2":2,"p=1":2},
"u_coordinate":"m_a + m_b","v_coordinate":"m_ab",
"posterior_ratio":"theta*(2v+u)/(2+u)","native_event_permission":False}
print(json.dumps(result,indent=2,sort_keys=True))
