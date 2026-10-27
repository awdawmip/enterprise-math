#!/usr/bin/env python3
"""EC48I: exact symbolic phase diagram for the R5 one-collision BRC tree.
Every affine coefficient and sample is a fractions.Fraction; no floating point.
Theorem concerns an external finite P/Q decision tree, not native X6 dynamics.
"""
from fractions import Fraction as F
from itertools import product

# A policy's signed objective J(s_a,s_b) = c0+c1*s_a+c2*s_b.
def const(n):
    return (F(n),F(0),F(0))
def add(*xs):
    return tuple(sum((v[i] for v in xs),F(0)) for i in range(3))
def evaluate(v,sa,sb):
    return v[0]+v[1]*sa+v[2]*sb

# (Q, LR, time) at nonterminals, ratios kept exact.
H={'':(F(1),F(1),0), 'a':(F(1,2),F(3,2),1),
   'b':(F(1,2),F(1,2),1), 'ax':(F(1,4),F(1),2),
   'ay':(F(1,4),F(2),2), 'bu':(F(1,8),F(1),2),
   'bv':(F(3,8),F(1,3),2)}
# Action 0 = decide P, 1 = decide Q, 2 = continue.
def stop(h,action):
    q,r,t=H[h]
    assert action in (0,1)
    return const(q*(375 if action==0 else 298*r)+q*t*(37*r-17))
def select(h,action,continuation):
    return continuation if action==2 else stop(h,action)

# Optimal terminal decisions minimize 375 vs 298*r for each LR.
# The kernel K_s=(s,1-2s,s) with LR (1/2,1,3/2) has
# terminal expected J per Q = 358-72*s, including t=3 time cost.
C_ax=(F(179,2),F(-18),F(0))
C_bu=(F(179,4),F(0),F(-9))
C_ay=const(F(1,4)*(375+3*(37*2-17)))
C_bv=const(F(3,8)*(298*F(1,3)+3*(37*F(1,3)-17)))
assert C_ay==const(F(273,2)) and C_bv==const(F(32))

full=[]; coarse=[]
for ay,bv,ax,bu,aa,bb,root in product((0,1,2),repeat=7):
    vax=select('ax',ax,C_ax)
    vbu=select('bu',bu,C_bu)
    vay=select('ay',ay,C_ay)
    vbv=select('bv',bv,C_bv)
    va=select('a',aa,add(vax,vay))
    vb=select('b',bb,add(vbu,vbv))
    value=select('',root,add(va,vb))
    full.append(value)
    if ax==bu:
        coarse.append(value)
assert len(full)==3**7==2187
assert len(coarse)==3**6==729

def minimal_affine_by_slope(rows):
    out={}
    for v in rows:
        slope=v[1:]
        if slope not in out or v[0]<out[slope][0]:
            out[slope]=v
    return out

f=minimal_affine_by_slope(full)
c=minimal_affine_by_slope(coarse)
EXPECTED_FULL={(F(0),F(0)): (F(281),F(0),F(0)),
               (F(0),F(-9)):(F(567,2),F(0),F(-9)),
               (F(-18),F(0)):(F(286),F(-18),F(0)),
               (F(-18),F(-9)):(F(577,2),F(-18),F(-9))}
EXPECTED_COARSE={**EXPECTED_FULL,(F(-18),F(0)):(F(287),F(-18),F(0))}
assert f==EXPECTED_FULL
assert c==EXPECTED_COARSE

def formulas(sa,sb):
    a=F(5)-18*sa
    b=F(5,2)-9*sb
    full_value=F(281)+min(F(0),a)+min(F(0),b)
    coarse_value=F(281)+min(F(0),b,a+1,a+b)
    gap=min(18*sa-5,F(1),F(5,2)-9*sb) if sa>F(5,18) and sb<F(5,18) else F(0)
    assert coarse_value-full_value==gap
    return full_value,coarse_value,gap

S=[F(1,100),F(1,12),F(1,6),F(1,5),F(5,18),F(3,10),
   F(1,3),F(2,5),F(7,16),F(49,100)]
for sa,sb in product(S,repeat=2):
    vf,vc,gap=formulas(sa,sb)
    assert all(F(0)<s<F(1,2) for s in (sa,sb))
    assert vf==min(evaluate(v,sa,sb) for v in full)
    assert vc==min(evaluate(v,sa,sb) for v in coarse)

# Independent exact Q/P conservation, positivity, and explicit policy witnesses.
def tree(sa,sb):
    q={'':F(1),'a':F(1,2),'b':F(1,2),'ax':F(1,4),
       'ay':F(1,4),'bu':F(1,8),'bv':F(3,8)}
    r={'':F(1),'a':F(3,2),'b':F(1,2),'ax':F(1),
       'ay':F(2),'bu':F(1),'bv':F(1,3)}
    for parent,s in (('ax',sa),('bu',sb)):
        for suffix,rr,prob in [('l',F(1,2),s),('m',F(1),1-2*s),('h',F(3,2),s)]:
            q[parent+suffix]=q[parent]*prob
            r[parent+suffix]=rr
    for parent in ('ay','bv'):
        q[parent+'m']=q[parent]
        r[parent+'m']=r[parent]
    children={'':('a','b'),'a':('ax','ay'),'b':('bu','bv'),
              'ax':('axl','axm','axh'),'bu':('bul','bum','buh'),
              'ay':('aym',),'bv':('bvm',)}
    assert len(q)==15 and all(x>0 for x in q.values())
    for h,cs in children.items():
        assert sum((q[k] for k in cs),F(0))==q[h]
        assert sum((q[k]*r[k] for k in cs),F(0))==q[h]*r[h]
    leaves=[k for k in q if k not in children]
    assert len(leaves)==8
    assert sum((q[k] for k in leaves),F(0))==1
    assert sum((q[k]*r[k] for k in leaves),F(0))==1
    return q,r

def observe(stops,q,r):
    ep=eq=tp=tq=F(0)
    for node,time,decision in stops:
        p=q[node]*r[node]
        if decision=='Q':ep+=p
        else: eq+=q[node]
        tp+=time*p
        tq+=time*q[node]
    return ep,eq,tp,tq

sa,sb=F(2,5),F(1,10)
q,r=tree(sa,sb)
full_policy=[('axl',3,'Q'),('axm',3,'Q'),('axh',3,'P'),
             ('ay',2,'P'),('bu',2,'Q'),('bvm',3,'Q')]
coarse_policy=[('axl',3,'Q'),('axm',3,'Q'),('axh',3,'P'),
               ('ay',2,'P'),('b',1,'Q')]
full_obs=observe(full_policy,q,r)
coarse_obs=observe(coarse_policy,q,r)
assert full_obs==(F(7,20),F(7,20),F(19,8),F(21,8))
assert coarse_obs==(F(7,20),F(7,20),F(2),F(7,4))
LAM=(298,375,37,-17)
def J(o):return sum((F(a)*v for a,v in zip(LAM,o)),F(0))
assert (J(full_obs),J(coarse_obs))==(F(1394,5),F(1399,5))
assert formulas(sa,sb)==(F(1394,5),F(1399,5),F(1))
for sa,sb in [(F(1,3),F(1,6)),(F(2,5),F(1,10)),(F(1,10),F(2,5))]:
    tree(sa,sb)
print('EC48I EXACT PHASE DIAGRAM VERIFIED')
print('NONTERMINAL TABLES full=2187 coarse=729; terminal decisions universally greedy')
print('SYMBOLIC LOWER ENVELOPE FULL', sorted(f.values()))
print('SYMBOLIC LOWER ENVELOPE COARSE', sorted(c.values()))
print('FULL = 281 + min(0,5-18*sa) + min(0,5/2-9*sb)')
print('COARSE = 281 + min(0,5/2-9*sb,6-18*sa,15/2-18*sa-9*sb)')
print('GAP = min(18*sa-5,1,5/2-9*sb) if sa>5/18 and sb<5/18; otherwise 0')
print('ALL-PARAMETER PROOF: exhaustive AFFINE coefficient envelopes over unchanged finite policy space')
print('GRID',len(S)**2,'exact pointwise checks passed')
print('OFF-NEIGHBORHOOD witness sa=2/5 sb=1/10: full',full_obs,'coarse',coarse_obs,'J',J(full_obs),J(coarse_obs))
print('TREE CONSERVATION AND STRICT POSITIVITY: PASS')
