#!/usr/bin/env python3
"""Exact Fraction verification of four S23 overwrite-only forward TV moduli."""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
PAIRS=((3,31),(7,27),(11,23),(15,19))

def branch(p,q,r):
    return (p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r))

def observed(z,mask,beta):
    x=list(z)
    for k in range(5):
        if mask & (1<<k): x[k]=beta
    raw=[branch(x[A[i]],x[B[i]],x[C[i]]) for i in range(6)]
    return [tuple(sum(F(M[j][i],20)*raw[i][k] for i in range(6))
             for k in range(4)) for j in range(6)]

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def masks(pair):
    return sorted(pair,key=lambda m:(m&4)!=0)

def bank(z,w,pair,bn,be):
    n,e=masks(pair)
    return max(tv(p,q) for mask,beta in ((n,bn),(e,be))
               for p,q in zip(observed(z,mask,beta),observed(w,mask,beta)))

def theoretical(pair,eps,bn,be):
    n,e=masks(pair)
    a,b=1-bn,1-be
    return max(a*(2*eps-eps*eps),
               b*b*eps if e==31 else b*(2*eps-eps*eps))

def witness_N(eps):
    z=[F(0)]*11; w=z.copy()
    for i in (2,5,6): w[i]=eps
    return z,w,0

def witness_E(pair,eps):
    n,e=masks(pair)
    z=[F(0)]*11; w=z.copy()
    if e==31:
        w[7]=eps; return z,w,2
    if e==15:
        w[4]=eps; w[10]=eps; return z,w,5
    w[3]=eps; w[7]=eps
    return z,w,2

def run():
    betas=(F(0),F(1,5),F(1,2),F(4,5),F(1))
    radii=(F(0),F(1,10),F(1,3),F(1,2),F(3,4),F(1))
    wc=rc=fc=0
    for pair in PAIRS:
        n,e=masks(pair)
        assert (n&3)==3 and (n&4)==0 and (e&7)==7
        for bn,be,eps in product(betas,betas,radii):
            z,w,row=witness_N(eps)
            nv=tv(observed(z,n,bn)[row],observed(w,n,bn)[row])
            assert nv==(1-bn)*(2*eps-eps**2)
            z,w,row=witness_E(pair,eps)
            ev=tv(observed(z,e,be)[row],observed(w,e,be)[row])
            assert ev==((1-be)**2*eps if e==31 else (1-be)*(2*eps-eps**2))
            assert theoretical(pair,eps,bn,be)==max(nv,ev)
            wc+=2
        rng=Random(20261103+e*21+n)
        for _ in range(350):
            z=[F(rng.randrange(13),12) for i in range(11)]
            w=[F(rng.randrange(13),12) for i in range(11)]
            bn=F(rng.randrange(13),12)
            be=F(rng.randrange(13),12)
            eps=max(abs(x-y) for x,y in zip(z,w))
            assert bank(z,w,pair,bn,be)<=theoretical(pair,eps,bn,be)
            rc+=1
            v=z.copy()
            v[0]=1-z[0]; v[1]=1-z[1]
            assert bank(z,v,pair,bn,be)==0
            fc+=1
    eps=F(1,2)
    assert theoretical((3,31),eps,F(1),F(0))==F(1,2)
    for p in PAIRS[1:]:
        assert theoretical(p,eps,F(1),F(0))==F(3,4)
    out={"status":"PASS_BRC_S23_OVERWRITE_ONLY_SHARP_FORWARD_MODULI_20261103",
         "arithmetic":"Python Fraction exact rational",
         "witness_checks":wc,"pair_random_checks":rc,
         "two_hidden_coordinate_checks":fc,
         "pairs":[list(p) for p in PAIRS],
         "mask_3_31_example":{"eps":"1/2","beta_N":"1","beta_E":"0","modulus":"1/2"},
         "other_three_example":{"eps":"1/2","beta_N":"1","beta_E":"0","modulus":"3/4"},
         "frozen_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34"}
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=="__main__": run()
