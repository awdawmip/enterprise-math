#!/usr/bin/env python3
"""External exact finite two-law BRC source; controlled T4 positive rational witness."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

q_source={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
        'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
original={}
for s,j,k in product(q_source,range(2),range(2)):
    q=q_source[s]/4
    original[s,j,k]=(q*ratios[s][j],q)
assert len(original)==16
assert all(p>0 and q>0 for p,q in original.values())
assert sum(p for p,q in original.values())==sum(q for p,q in original.values())==1

# Add a hidden upstream H only to the four BU leaves; all source marginals stay fixed.
extended={}
for (s,j,k),(p,q) in original.items():
    if s=='BU':
        for h in (0,1):
            extended[s,j,k,h]=(p*(F(3,4) if h else F(1,4)),
                                q*(F(1,4) if h else F(3,4)))
    else:
        extended[s,j,k,None]=(p,q)
assert len(extended)==20
assert all(p>0 and q>0 for p,q in extended.values())
assert sum(p for p,q in extended.values())==sum(q for p,q in extended.values())==1
for key,pq in original.items():
    assert tuple(sum(val[i] for (s,j,k,h),val in extended.items()
                     if (s,j,k)==key) for i in (0,1))==pq

def obs(s,j,k,h,a,with_j,with_y):
    coarse={'AU':'T3_P_AU','AV':'T2_Q','BU':'T3_Q_BU','BV':'T2_Q'}[s]
    jb=j if s=='BU' and with_j else None
    y=(k if a==0 else h) if s=='BU' else 0
    return (coarse,jb,y) if with_y else (coarse,jb)

def push(law,a,with_j,with_y):
    d=defaultdict(F)
    for (s,j,k,h),mass in extended.items():
        d[obs(s,j,k,h,a,with_j,with_y)]+=mass[law]
    return dict(d)

def tv(x,y):
    return sum((abs(x.get(z,0)-y.get(z,0)) for z in set(x)|set(y)),F(0))/2

assert push(0,0,False,False)==push(1,0,False,False)
assert push(0,0,False,False)[('T3_Q_BU',None)]==F(1,4)
assert tv(push(0,0,False,False),push(1,0,False,False))==0
assert tv(push(0,0,True,True),push(1,0,True,True))==F(1,10)
assert tv(push(0,1,True,True),push(1,1,True,True))==F(11,80)

Pj=[sum(p for (s,jj,k,h),(p,q) in extended.items()
        if s=='BU' and jj==j) for j in (0,1)]
Qj=[sum(q for (s,jj,k,h),(p,q) in extended.items()
        if s=='BU' and jj==j) for j in (0,1)]
assert Pj==[F(1,40),F(9,40)] and Qj==[F(1,8),F(1,8)]
for j in (0,1):
    for i,masses,expected in ((0,Pj,F(3,4)),(1,Qj,F(1,4))):
        pH=sum(pq[i] for (s,jj,k,h),pq in extended.items()
               if s=='BU' and jj==j and h==1)/masses[j]
        pk=sum(pq[i] for (s,jj,k,h),pq in extended.items()
               if s=='BU' and jj==j and k==1)/masses[j]
        assert pH==expected and pk==F(1,2)

def errors(theta):
    return (sum(Pj[j]*abs(theta[j]-F(3,4)) for j in (0,1)),
            sum(Qj[j]*abs(theta[j]-F(1,4)) for j in (0,1)))

assert errors((F(1,4),F(17,28)))==(F(5,112),F(5,112))
for t0,t1 in product((F(0),F(1,7),F(5,7),F(1)),repeat=2):
    th=(F(1,4)+t0/2,F(1,4)+t1/2)
    ep,eq=errors(th)
    assert F(5,14)*ep+F(9,14)*eq==F(5,112)+t0/28
assert F(1,4)*(F(3,4)-F(1,4))/2==F(1,16)

print('Original: 16 positive P/Q leaves; extended: 20 positive leaves; 16-leaf marginal exact.')
print('BU j masses P =',Pj,'Q =',Qj)
print('P(H=1|BU,j)=3/4; Q(H=1|BU,j)=1/4; original k remains fair.')
print('TV passive repaired =',F(1,10),'TV controlled repaired =',F(11,80))
print('Sharp observer-preserving two-law controlled reconstruction radius =',F(5,112))
print('PASS_BRC_N4_CONTROLLED_T4_INTERVENTION_20LEAF_EXACT_RADIUS_20261030')
