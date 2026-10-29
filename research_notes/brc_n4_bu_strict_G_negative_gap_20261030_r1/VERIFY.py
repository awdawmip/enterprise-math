#!/usr/bin/env python3
"""Exact rational gap in the external BRC N=4 BU 16-leaf model.

L0/L3 legality and S2->S23 contraction are inherited, not certified here.
The K dual and 16-leaf H upper witness are checked independently.
"""
from fractions import Fraction as F
from collections import defaultdict

a,b=F(961,1000),F(151,1000)
X=a+3*b
D=b-(1-a)/3
C=(7-a-21*b)/(4*X+2)
R=7*(X-1)/(6*X)
E=D*C/4
H=b*(2*a-7*b)/(8*(a+2*b))
q1,q2=F(214,625),F(14977,40000)
eps=F(1,1500000)

def L0(u):return (4*a-14*b-3*a*u-X*u*u)/(2*(23-2*u))
def L3(u):return u*(a-X*u)/(2*(7-2*u))
def K(u):return b*u/(4+u)

assert F(0)<R<q1<q2<C<1 and q1<F(3,7)
margins={
    'L0_q1': L0(q1)-E,
    'L3_q1': L3(q1)-E,
    'L3_q2': L3(q2)-E,
    'K_q2': K(q2)-E,
}
expected={
    'L0_q1':F(70817303,11122732500000),
    'L3_q1':F(9259803,3147732500000),
    'L3_q2':F(2170463043,3190586960000000),
    'K_q2':F(269,369042400),
}
assert margins==expected
assert all(v>eps for v in margins.values())
assert E+eps < H and H-E==F(9919,3223176000)
# L0'(u) <0 for 0<=u<=3/7 by its strictly negative polynomial numerator.
# L3'(u) has numerator 2*X*u^2-14*X*u+7*a, which is strictly
# decreasing for u in [0,1]; hence L3 has no interior local minimum.
assert X>0 and (4*X*1-14*X)<0

qmass={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
likelihood={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
            'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,l,qmass[cat]/4,qmass[cat]*likelihood[cat][j]/4)
        for cat in ('AU','AV','BU','BV') for j in range(2) for l in range(2)]
assert len(leaves)==16 and all(Q>0 and P>0 for _,_,_,Q,P in leaves)
assert sum(v[3] for v in leaves)==sum(v[4] for v in leaves)==1

def observed(law,first,second):
    out=defaultdict(F)
    for cat,j,l,Q,P in leaves:
        mass=Q if law=='Q' else P
        stage1=first[cat[0]]
        stage2=second[cat]
        z=int(cat=='BU')
        out[(1,'Q',0)]+=mass*(1-stage1)
        out[(2,'Q',0)]+=mass*stage1*(1-stage2)
        out[(3,'Q' if z else 'P',z)]+=mass*stage1*stage2
    assert sum(out.values())==1
    return out

def TV(v,w):
    return sum(abs(v.get(k,F())-w.get(k,F())) for k in set(v)|set(w))/2

uH=(2*a-7*b)/(2*a+4*b)
A,B=a,b
U=b*(1+uH) # unnormalized first-stage AV survivor mass
V=b           # unnormalized first-stage BV survivor mass
assert F(0)<uH<1 and F(0)<=U<=A<=1 and F(0)<=V<=B<=1
target1={'A':a,'B':b}
target2={'AU':F(1),'AV':F(0),'BU':F(0),'BV':F(0)}
candidate1={'A':A,'B':B}
candidate2={'AU':uH,'AV':U/A,'BU':uH,'BV':V/B}
for law in ('P','Q'):
    target=observed(law,target1,target2)
    cand=observed(law,candidate1,candidate2)
    assert TV(target,cand)==H,(law,TV(target,cand),H)
    print('16_LEAF_TV',law,TV(target,cand))
print('FROZEN_PARAMS',a,b,'R',R,'C',C,'E',E,'H',H,'H_MINUS_E',H-E)
print('CUTS',q1,q2,'EPS',eps)
for name,val in margins.items():print('EXACT_MARGIN',name,val)
print('CERTIFICATE','E + 1/1500000 <= d2,d23 <= H',E+eps,H)
print('PASS_BRC_N4_BU_STRICT_G_NEGATIVE_GAP_20261030')
