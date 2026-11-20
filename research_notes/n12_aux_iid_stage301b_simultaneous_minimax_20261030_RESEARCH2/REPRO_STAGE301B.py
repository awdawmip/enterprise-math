#!/usr/bin/env python3
"""Exact rational certificate for Stage301-B; no numeric optimizer needed."""
from fractions import Fraction as F
from itertools import product

B = list(product((0, 1), repeat=3))
P = (F(1,4), F(3,4))
POL = list(product((0,1), repeat=6))  # per x: action1, action2|y1=0, action2|y1=1

def source(s, policy):
    p = P[s]
    out = []
    for x,y,z in B:
        a1, a2 = policy[3*x], policy[3*x+1+y]
        v = (p if a1 else F(1,2))
        w = (p if a2 else F(1,2))
        out.append(F(1,2)*(v if y else 1-v)*(w if z else 1-w))
    return out

def port(b):
    a = 16 - 3*b
    return [F((a,b,b,a)[sum(bits)], 32) for bits in B]

def tv(u,v):
    return sum(abs(x-y) for x,y in zip(u,v))/2

def risk(policy,b,tagged):
    p0, p1 = source(0,policy),source(1,policy)
    q = port(b)
    return (tv(p0,q)+tv(p1,q))/2 if tagged else tv([(a+c)/2 for a,c in zip(p0,p1)],q)

pool_b, tag_b = F(15,4), F(13,4)
pool = [(risk(pi,pool_b,False),i) for i,pi in enumerate(POL)]
tag = [(risk(pi,tag_b,True),i) for i,pi in enumerate(POL)]
assert max(x for x,_ in pool) == F(3,32)
assert max(x for x,_ in tag) == F(17,64)
assert sum(1 for x,_ in pool if x == F(3,32)) >= 1
assert sum(1 for x,_ in tag if x == F(17,64)) == 4
assert POL[46] == (1,0,1,1,1,0) and POL[63] == (1,1,1,1,1,1)
assert risk(POL[46],tag_b,True) == risk(POL[63],tag_b,True) == F(17,64)
signs = (
 ((-1,1,-1,-1,1,-1,-1,-1),(-1,-1,-1,1,-1,-1,1,-1)),
 ((1,-1,-1,-1,1,-1,-1,-1),(-1,-1,-1,1,-1,-1,-1,1)),
)
for j,idx in enumerate((46,63)):
    p0,p1 = source(0,POL[idx]),source(1,POL[idx])
    for b in (F(0),F(13,4),F(15,4),F(4)):
        q = port(b)
        lower = sum(sum(u*(v[k]-q[k]) for k,u in enumerate(s)) for v,s in zip((p0,p1),signs[j]))/4
        expected = F(15,32)-b/16 if j==0 else F(1,16)+b/16
        assert lower == expected and risk(POL[idx],b,True) >= lower
def mixture(atoms):
    return [sum(w*theta**sum(bits)*(1-theta)**(3-sum(bits)) for w,theta in atoms) for bits in B]
mu_pool=((F(1,2),F(3,8)),(F(1,2),F(5,8)))
mu_tag=((F(3,8),F(1,4)),(F(1,4),F(1,2)),(F(3,8),F(3,4)))
assert mixture(mu_pool) == port(pool_b)
assert mixture(mu_tag) == port(tag_b)
assert len(POL)==64
for pi in POL:
    for s in (0,1):
        p = source(s,pi)
        assert sum(p)==1 and all(t>0 for t in p)
for r in (pool_b,tag_b):
    q = port(r)
    assert sum(q)==1 and all(t>0 for t in q)
print('POLICIES_EXHAUSTED=64; SOURCE_LAWS_CHECKED=128')
print('POOLED_SIMULTANEOUS_MINIMAX=3/32; ATTAINING_MIXTURE=1/2@3/8+1/2@5/8')
print('TAGGED_SIMULTANEOUS_MINIMAX=17/64; ATTAINING_MIXTURE=3/8@1/4+1/4@1/2+3/8@3/4')
print('TAGGED_DUAL_SUPPORTS=15/32-b/16,1/16+b/16')
print('STAGE301B_SIMULTANEOUS_MINIMAX_EXACT_PASS')
