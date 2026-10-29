#!/usr/bin/env python3
"""Exact rational counterexample at b/a>rho in external BRC N=4 BU model.
Author-side executable evidence, NOT independent native Driver review."""
from collections import defaultdict
from fractions import Fraction as Q

a=Q(1,2)
b=Q(872,10793)
cstar=Q(9,25)
A=Q(503,1000)
B=Q(399,5000)
c=Q(1,3)
U=Q(53,500)
V=B

f=(a+3*b)*cstar*cstar+(3*a+8*b)*cstar+14*b-4*a
assert f==0
r=b/a
assert r==(1-cstar)*(4+cstar)/(3*cstar*cstar+8*cstar+14)
# cstar < c0=(sqrt(5889)-73)/10 implies r>rho, verified without floating point.
assert 25*5889>383**2
assert cstar < Q(383,5)/10-Q(73,10)
assert Q(0)<A<1 and Q(0)<B<1 and Q(0)<=U<=A and Q(0)<=V<=B and Q(0)<c<1
h=b*cstar/(4+cstar)

qmass={'AU':Q(1,6),'AV':Q(1,3),'BU':Q(1,4),'BV':Q(1,4)}
ratio={'AU':(Q(9,10),Q(11,10)), 'AV':(Q(1,4),Q(1,4)),
       'BU':(Q(1,5),Q(9,5)), 'BV':(Q(2),Q(2))}
leaves=[(kind,j,k,qmass[kind]/4,qmass[kind]*ratio[kind][j]/4)
        for kind in qmass for j in (0,1) for k in (0,1)]
assert len(leaves)==16 and all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1

def law_observation(law,target):
    result=defaultdict(Q)
    for kind,j,k,q,p in leaves:
        wt=q if law=='Q' else p
        x=(a if kind[0]=='A' else b) if target else (A if kind[0]=='A' else B)
        y=(Q(1) if kind=='AU' else Q(0)) if target else {
          'AU':c,'BU':c,'AV':U/A,'BV':V/B}[kind]
        assert 0<=x<=1 and 0<=y<=1
        result[(1,'Q',0)] += wt*(1-x)
        result[(2,'Q',0)] += wt*x*(1-y)
        if target:
            assert kind=='AU' or y==0
            decision,source='P',0
        else:
            decision,source=('Q' if kind=='BU' else 'P'),int(kind=='BU')
        result[(3,decision,source)] += wt*x*y
    assert sum(result.values())==1
    return dict(result)

def tv(f,g):
    return sum(abs(f.get(z,Q(0))-g.get(z,Q(0))) for z in f.keys()|g.keys())/2

vq=tv(law_observation('Q',True),law_observation('Q',False))
vp=tv(law_observation('P',True),law_observation('P',False))
e=max(vq,vp)
assert vq==Q(133,20000),vq
assert vp==Q(6470029,971370000),vp
assert h==Q(72,10793),h
assert h-e==Q(9971,971370000)>0,(h,e,h-e)

s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
H=B*c/4
rq=a/6-A*c/6-U/3-V/4
rp=a/6-A*c/6-U/12-V/2
dq=(s,H-s-rq,rq,-H)
dp=(t,H-t-rp,rp,-H)
assert sum(map(abs,dq))/2==vq
assert sum(map(abs,dp))/2==vp

print('PASS_EXACT_RATIONAL_16_LEAF_OBSERVATION_ENUMERATION')
print('target_a',a,'b',b,'cstar',cstar,'h',h)
print('competitor_A',A,'B',B,'c',c,'U',U,'V',V)
print('TV_Q',vq,'TV_P',vp,'e',e,'strict_improvement',h-e)
print('PASS_BRC_N4_BU_POST_RHO_ROOT_EXTRAPOLATION_FALSIFIED')
