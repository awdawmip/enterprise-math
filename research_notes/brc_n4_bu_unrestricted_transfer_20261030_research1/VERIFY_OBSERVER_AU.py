#!/usr/bin/env python3
"""Exact rational 16-leaf checks of an AU-marked observer fidelity obstruction.
All scientific claims are confined to the stated external N=4 two-law model.
"""
from collections import defaultdict
from fractions import Fraction as F
from random import Random
import sympy as S

q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
LR={'AU':(F(9,10),F(11,10)), 'AV':(F(1,4),F(1,4)),
    'BU':(F(1,5),F(9,5)), 'BV':(F(2),F(2))}
leaves=[(c,j,k,q2[c]/4,q2[c]*LR[c][j]/4)
        for c in q2 for j in range(2) for k in range(2)]
assert len(leaves)==16
assert all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(q for _,_,_,q,p in leaves)==sum(p for _,_,_,q,p in leaves)==1
assert set(LR['BU']).isdisjoint({x for c in ('AU','AV','BV') for x in LR[c]})

def target(a,b):
    return {'first':{'A':a,'B':b},
            'second':{'AU':F(1),'AV':F(0),'BU':F(0),'BV':F(0)},
            'third':{(c,j):F(0) for c in q2 for j in range(2)},
            'dec1':{root:F(0) for root in ('A','B')},
            'dec2':{c:F(0) for c in q2},
            'dec3':{(c,j):F(1) if c=='AU' else F(0) for c in q2 for j in range(2)},
            'dec4':{(c,j,k):F(1) for c in q2 for j in range(2) for k in range(2)}}

def collapsed(g):
    return {'first':g['first'].copy(),'second':g['second'].copy(),
            'third':{(c,j):F(0) for c in q2 for j in range(2)},
            'dec1':{root:F(0) for root in ('A','B')},
            'dec2':{c:F(0) for c in q2},
            'dec3':{(c,j):F(0) if c=='BU' else F(1) for c in q2 for j in range(2)},
            'dec4':{(c,j,k):F(0) for c in q2 for j in range(2) for k in range(2)}}

def observed(g,law):
    d=defaultdict(F)
    for c,j,k,Q,P in leaves:
        m=P if law=='P' else Q
        x=g['first'][c[0]];y=g['second'][c];z=g['third'][(c,j)]
        cases=[(1,m*(1-x),g['dec1'][c[0]]),
               (2,m*x*(1-y),g['dec2'][c]),
               (3,m*x*y*(1-z),g['dec3'][(c,j)]),
               (4,m*x*y*z,g['dec4'][(c,j,k)])]
        for t,mass,p_dec in cases:
            bu=int(c=='BU' and t>=3)
            au=int(c=='AU' and t>=3)
            d[(t,'P',bu,au)]+=mass*p_dec
            d[(t,'Q',bu,au)]+=mass*(1-p_dec)
    assert sum(d.values())==1
    return d

def K_push(d):
    out=defaultdict(F)
    for (t,decision,bu,au),m in d.items():
        if t<=2: key=(t,'Q',0,0)
        else: key=(3,'Q' if bu else 'P',bu,au)
        out[key]+=m
    return out

def canon(d):return {k:v for k,v in d.items() if v}
def TV(a,b):return sum(abs(a.get(x,0)-b.get(x,0)) for x in set(a)|set(b))/2

a,b=F(961,1000),F(151,1000)
f=target(a,b)
assert all(canon(observed(f,law))==canon(K_push(observed(f,law))) for law in ('P','Q'))

rng=Random(202610300700)
def rat():return F(rng.randrange(24),23)
for i in range(40):
    c=rat()
    g={'first':{'A':rat(),'B':rat()},
       'second':{'AU':c,'BU':c,'AV':rat(),'BV':rat()},
       'third':{(cat,j):rat() for cat in q2 for j in range(2)},
       'dec1':{r:rat() for r in ('A','B')},
       'dec2':{cat:rat() for cat in q2},
       'dec3':{(cat,j):rat() for cat in q2 for j in range(2)},
       'dec4':{(cat,j,k):rat() for cat in q2 for j in range(2) for k in range(2)}}
    g['dec2']['BU']=g['dec2']['AU']
    kg=collapsed(g)
    for law in ('P','Q'):
        ref=observed(f,law)
        raw=observed(g,law)
        got=observed(kg,law)
        assert canon(got)==canon(K_push(raw))
        assert TV(ref,got)<=TV(ref,raw)
        assert got[(3,'P',0,1)]==g['first']['A']*c/F(6)
        assert got[(3,'Q',1,0)]==g['first']['B']*c/F(4)
        e=TV(ref,got)
        A,B=g['first']['A'],g['first']['B']
        assert abs(B-b)<=3*e
        assert abs(a-A*c)<=6*e
        assert B*c<=4*e
print('PASS_REFINED_AU_AND_BU_K_PUSHFORWARD 40 lawful S2 policies x 2 laws')

# exact semialgebraic consequence of the observable event bounds
E=S.sqrt(26521161)/15000-S.Rational(413,1250)
D=S.Rational(7789,1000)
L=(S.Integer(7789)-S.sqrt(50220529))/36000
e=S.symbols('e',real=True)
poly=18*e**2-D*e+S.Rational(a.numerator,a.denominator)*S.Rational(b.numerator,b.denominator)
assert S.factor(poly.subs(e,L))==0
assert S.factor(S.discriminant(poly,e)-S.Rational(50220529,1000000))==0
assert bool(L>S.Rational(1,60))
assert bool(L<S.Rational(b.numerator,b.denominator)/3)
assert bool(L<S.Rational(a.numerator,a.denominator)/6)
assert bool(E<S.Rational(517,40000))
assert S.Rational(517,40000)<S.Rational(1,60)
# q(e)>0 below the least root, excluding all e<L by 4e >= (b-3e)(a-6e)
print('PASS_SHARP_EVENT_LOWER',str(L),float(L))
print('PASS_STRICT_OLD_OPTIMUM_SEPARATION',str(E),float(E))

# Exact lawful original S23 upper witness: both laws differ only by BU T2 -> T3 transfer.
g=collapsed(f)
g['second']['AU']=g['second']['BU']=F(1)
for law in ('P','Q'):
    tv=TV(observed(f,law),observed(g,law))
    assert tv==F(151,4000), (law,tv)
print('PASS_REFINED_BOTH_LAW_UPPER',F(151,4000))
print('PASS_BRC_N4_AU_MARKED_OBSERVER_STRICT_MINIMAX_SEPARATION_20261030')
