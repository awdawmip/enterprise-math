#!/usr/bin/env python3
"""Exact 16-leaf G(t0,t1) validation; model-local probability, not native heartbeat."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
q={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
   'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
raw={L:{} for L in ('P','Q')}
for s,j,k in product(q,(0,1),(0,1)):
    raw['Q'][s,j,k]=q[s]/4
    raw['P'][s,j,k]=q[s]*r[s][j]/4
assert all(len(raw[L])==16 and sum(raw[L].values())==1 and
           all(x>0 for x in raw[L].values()) for L in raw)
assert len(set(r['AU']+r['BU']))==4
E,A,B3,B40,B41='E','A','B3','B40','B41'
def tv(x,y):
    return sum((abs(x.get(z,F(0))-y.get(z,F(0)))
                for z in set(x)|set(y)),F(0))/2
def observe(s,j,k,u,v):
    if s in ('AV','BV'): return {E:F(1)}
    if s=='AU': return {A:F(1)}
    t=u if j==0 else v
    return {B3:1-t,(B40 if k==0 else B41):t}
def laws(u,v):
    out={}
    for L in ('P','Q'):
        z=defaultdict(lambda:F(0))
        for (s,j,k),m in raw[L].items():
            for obs,w in observe(s,j,k,u,v).items(): z[obs]+=m*w
        out[L]=dict(z)
    return out
for u,v in product((F(0),F(1,3),F(2,3),F(1)),repeat=2):
    d=laws(u,v); p=d['P']; z=d['Q']
    assert p=={E:F(7,12),A:F(1,6),B3:F(1,4)-(u+9*v)/40,
               B40:(u+9*v)/80,B41:(u+9*v)/80}
    assert z=={E:F(7,12),A:F(1,6),B3:F(1,4)-(u+v)/8,
               B40:(u+v)/16,B41:(u+v)/16}
    assert tv(p,z)==abs(v-u)/10
    assert {E:p[E],A:p[A],'B':p[B3]+p[B40]+p[B41]}=={
           E:z[E],A:z[A],'B':F(1,4)}
    mid={w:(p[w]+z[w])/2 for w in p}
    assert mid=={E:F(7,12),A:F(1,6),
        B3:F(1,4)*(1-(3*u+7*v)/10),
        B40:F(1,4)*(3*u+7*v)/20,
        B41:F(1,4)*(3*u+7*v)/20}
    assert tv(p,mid)==tv(z,mid)==abs(v-u)/20
    assert (p==z)==(u==v)
g=laws(F(0),F(1))
assert g['P'][B40]+g['P'][B41]==F(9,40)
assert g['Q'][B40]+g['Q'][B41]==F(1,8)
# Deterministic G4 stopped atoms: AV,BV,AU0,AU1,BU0,BU10,BU11.
def stopped(s,j,k):
    if s in ('AV','BV'): return s
    if s=='AU': return (s,j)
    return (s,0) if j==0 else (s,1,k)
assert len({stopped(s,j,k) for s,j,k in raw['P']})==7
assert len({stopped('BU',j,k) for j,k in product((0,1),repeat=2)})==3
print('G4_T4_EVENT_P',F(9,40),'Q',F(1,8))
print('G4_FULL_TV_PQ',tv(g['P'],g['Q']))
print('G4_SHARP_COMMON_DECODER_RADIUS',F(1,20))
print('FAMILY_EXACT_RATIONAL_CASES',16)
print('FAMILY_PROVED_FORMULAS','TV=abs(v-u)/10; radius=abs(v-u)/20')
print('G4_STOPPED_ATOMS',7)
print('PASS_BRC_N4_LAWFUL_G4_PHASE_20261030')
