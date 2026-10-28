#!/usr/bin/env python3
"""Exact rational reproduction of the N4 AU-bit minimax witness (not a proof checker)."""
from fractions import Fraction as F
import json
Z,O=F(0),F(1)
N={1:{'A':(F(1,2),F(1,2)),'B':(F(1,2),F(3,2))},
   2:{'AU':(F(1,6),O),'AV':(F(1,3),F(1,4)),'BU':(F(1,4),O),'BV':(F(1,4),F(2))}}
for t in (3,4):
    N[t]={}
    for h,(q,r) in N[t-1].items():
        skew=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h] if t==3
              else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
        for j,sgn in [('0',-1),('1',1)]:
            N[t][h+j]=(q/2,r*(1+sgn*skew))
for t in N:
    assert sum((q for q,r in N[t].values()),Z)==O
    assert sum((q*r for q,r in N[t].values()),Z)==O
    assert all(q>0 and r>0 for q,r in N[t].values())
def row(c=Z,p=Z):
    assert 0<=c<=1 and 0<=p<=1-c
    return (p,O-c-p,c)
def policy(witness):
    a,b=F(1,20),O
    d={(1,'A'):row(a),(1,'B'):row(b)}
    rates=[('AU',F(53,64) if witness else Z),
           ('BU',F(53,64) if witness else O),
           ('AV',O if witness else Z),
           ('BV',F(149,1920) if witness else Z)]
    for h,c in rates:d[2,h]=row(c)
    for h in N[3]:
        d[3,h]=row(Z, O if (not witness and h.startswith('AU')) else Z)
    for h in N[4]:d[4,h]=row()
    return d
def law(d):
    out={'Q':{},'P':{}}
    for leaf,(q,r) in N[4].items():
        alive=O
        for t in range(1,5):
            p,qq,c=d[t,leaf[:t]]
            z=int(t>=3 and leaf.startswith('AU'))
            for k,v in [('P',p),('Q',qq)]:
                key=(t,k,z)
                for name,weight in [('Q',q),('P',q*r)]:
                    out[name][key]=out[name].get(key,Z)+weight*alive*v
            alive*=c
        assert alive==Z
    for dct in out.values():assert sum(dct.values(),Z)==O
    return out
def tv(p,q):
    return sum((abs(p.get(k,Z)-q.get(k,Z)) for k in p.keys()|q.keys()),Z)/2
def atoms(d,law):
    a=d[law]
    return [sum((v for (t,k,z),v in a.items() if t==tt and z==zz),Z)
            for tt,zz in [(1,0),(2,0),(3,0),(3,1)]]
target,witness=law(policy(False)),law(policy(True))
E=F(53,7680)
expected={'Q':([F(19,40),F(11,40),F(1,4),Z],
               [F(19,40),F(11,40),F(1867,7680),E]),
          'P':([F(19,80),F(41,80),F(1,4),Z],
               [F(19,80),F(3883,7680),F(1,4),E])}
for name in ('Q','P'):
    assert atoms(target,name)==expected[name][0]
    assert atoms(witness,name)==expected[name][1]
    assert tv(target[name],witness[name])==E
assert policy(True)[2,'AU']==policy(True)[2,'BU']
assert all(policy(True)[3,h]==row() for h in N[3])
print(json.dumps({'status':'PASS_EXACT_N4_AU_WALL_WITNESS',
                  'd2_d23':'53/7680','P_TV':str(tv(target['P'],witness['P'])),
                  'Q_TV':str(tv(target['Q'],witness['Q'])),
                  'full_policy_lower_bound':'Analytic proof in PROOF.md; NOT numerical exhaustion',
                  'native_X6_bridge':'NOT_ESTABLISHED'},indent=2))
