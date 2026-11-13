#!/usr/bin/env python3
"""R621 exact frozen-R462 signed BRC K, S6 profile and closed-source checks.
Python standard-library arbitrary-precision integers; no floating point.
"""
from itertools import permutations, product
from math import comb, factorial
import json

def C(n,k):
    return comb(n,k) if 0<=k<=n else 0

def add(a,b):
    o=[0]*max(len(a),len(b))
    for i,x in enumerate(a): o[i]+=x
    for i,x in enumerate(b): o[i]+=x
    while len(o)>1 and o[-1]==0: o.pop()
    return o

def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    while len(o)>1 and o[-1]==0: o.pop()
    return o

def frozen_K(i):
    d=[-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),
       C(7,i-2),-C(9,i-3)]
    out=[0]
    for j,x in enumerate(d,1):
        n=i+1-j
        if n>=0: out=add(out,[-x*C(n,k) for k in range(n+1)])
    return [0]*(i-1)+out

K=[frozen_K(i) for i in range(1,13)]
nu=lambda p: next(i for i,c in enumerate(p) if c)
alpha=[p[nu(p)] for p in K]
assert [nu(p) for p in K]==list(range(12))
assert alpha==[2,-1,-8,-11,6,53,106,119,83,36,9,1]
assert K[0]==[2,3] and K[1]==[0,-1,4,4]

# 0-based axes 0..5, sign 0=positive / 1=negative, pi maps base-axis to spatial axis.
def idx(pi,st): return 2*pi.index(st[0])+st[1]
def weight(pi,path):
    out=[1]
    for a in path: out=mul(out,K[idx(pi,a)])
    return out
def level(pi,path): return sum(idx(pi,a)+1 for a in path)
def gstep(g,a): return (g[a[0]],a[1])
def gpi(g,pi): return tuple(g[i] for i in pi)

perms=list(permutations(range(6)))
ident=tuple(range(6))
trans=[]
for j in range(5):
    g=list(ident);g[j],g[j+1]=g[j+1],g[j];trans.append(tuple(g))
assert len(perms)==factorial(6)==720
assert len({tuple(idx(pi,(j,s)) for j in range(6) for s in range(2)) for pi in perms})==720

single=0; pairs=0
steps=list(product(range(6),range(2)))
for pi in perms:
    for g in trans:
        gp=gpi(g,pi)
        for a in steps:
            assert idx(pi,a)==idx(gp,gstep(g,a))
            assert level(pi,(a,))==level(gp,(gstep(g,a),))
            assert weight(pi,(a,))==weight(gp,(gstep(g,a),))
            single+=1
        for a in steps:
            for b in steps:
                path=(a,b); rotated=(gstep(g,a),gstep(g,b))
                assert level(pi,path)==level(gp,rotated)
                assert weight(pi,path)==weight(gp,rotated)
                pairs+=1

assert K[0]!=K[2] and mul(K[0],K[1])!=mul(K[2],K[3])
apair=[alpha[2*j]*alpha[2*j+1] for j in range(6)]
assert apair==[-2,88,318,12614,2988,9]

def closed_table(maxR):
    counts={(0,0):1}; signed={(0,0):1}
    for j,a in enumerate(apair):
        nc={};ns={}
        for (r,h),n in counts.items():
            for k in range(maxR-r+1):
                key=(r+k,h+j*k)
                ways=comb(2*(r+k),2*k)*comb(2*k,k)
                nc[key]=nc.get(key,0)+n*ways
                ns[key]=ns.get(key,0)+signed[r,h]*ways*a**k
        counts,signed=nc,ns
    return counts,signed

counts,signed=closed_table(27)
for r in range(28):
    for h in range(5*r+1):
        assert counts[r,h]==counts[r,5*r-h]
for r in range(1,28):
    c=comb(2*r,r)*(-2)**r
    assert signed[r,0]==c
    assert signed[r,1]==c*(-44*r*r)
    assert signed[r,2]==c*r*r*(484*(r-1)**2-159)
assert all(v!=0 for (r,h),v in signed.items() if r>0)
assert (counts[7,0],signed[7,0])==(3432,-439296)
assert (counts[3,3],signed[3,3])==(920,-17585440)
assert counts[7,0]+counts[3,3]==4352

evidence={
  "schema":"EM_R621_S6_ORIENTED_SIGNED_BRC_EXACT_V1",
  "science_pin":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
  "source_blob":"7fa7a762f758b30c6090468ac43487daa34abad8",
  "arithmetic":"Python standard-library exact integers",
  "leaders":alpha,"pair_leaders":apair,"orientation_states":len(perms),
  "orientation_fixed_width_bits":10,
  "single_step_checks":single,"length_two_checks":pairs,
  "closed_R_checked":[0,27],
  "signed_nonzero_R_checked":[1,27],
  "level21":{"v7":{"count":counts[7,0],"leader_sum":signed[7,0]},
             "v15":{"count":counts[3,3],"leader_sum":signed[3,3]}},
  "pass":"R621_S6_COVARIANT_PROFILE_EXACT_PASS"
}
print(json.dumps(evidence,ensure_ascii=False,indent=2))
