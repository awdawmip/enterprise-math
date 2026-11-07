#!/usr/bin/env python3
"""Exact Fraction verification of a four-class nonlumpable LR STOP-time hull equality."""
from fractions import Fraction as Q
from itertools import product

R = (Q(1, 4), Q(1, 2), Q(3, 4), Q(2))
K0 = tuple(Q(n, 18) for n in (5, 2, 5, 6))
K1 = tuple(Q(n, 18) for n in (3, 6, 3, 6))
KB = tuple((a+b)/2 for a,b in zip(K0,K1))


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    p=sorted(set(points))
    if len(p)<=1:
        return p
    lo=[]
    for x in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],x)<=0:
            lo.pop()
        lo.append(x)
    hi=[]
    for x in p[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],x)<=0:
            hi.pop()
        hi.append(x)
    return lo[:-1]+hi[:-1]


def lr_increment(bits):
    start,late=bits[0],bits[1:]
    dp=dq=Q(start)
    for j in range(4):
        flow=start*late[j]*KB[j]
        dp+=flow*R[j]
        dq+=flow
    return dp,dq


def full_increment(bits):
    starts,late=bits[:2],bits[2:]
    dp=dq=Q(sum(starts),2)
    for i,kernel in enumerate((K0,K1)):
        for j in range(4):
            flow=Q(1,2)*starts[i]*late[4*i+j]*kernel[j]
            dp+=flow*R[j]
            dq+=flow
    return dp,dq


def put(kernel, strike):
    return sum((k*max(Q(0),strike-r) for k,r in zip(kernel,R)),Q(0))


def call(kernel, strike):
    return sum((k*max(Q(0),r-strike) for k,r in zip(kernel,R)),Q(0))


assert all(k>0 for k in K0+K1)
assert all(sum(k for k in K)==1 for K in (K0,K1,KB))
assert all(sum((k*r for k,r in zip(K,R)),Q(0))==1 for K in (K0,K1,KB))
assert K0!=K1
assert sum(abs(a-b) for a,b in zip(K0,K1))/2==Q(2,9)
assert all(1-Q(5,4)+call(K,Q(5,4))==0 for K in (K0,K1))
assert all(Q(4,5)-1+put(K,Q(4,5))==0 for K in (K0,K1))
assert call(K0,Q(5,8))-call(K1,Q(5,8))==Q(1,72)

lr_points=[lr_increment(x) for x in product((0,1),repeat=5)]
full_points=[full_increment(x) for x in product((0,1),repeat=10)]
assert len(lr_points)==32 and len(full_points)==1024
lr_h=hull(lr_points)
full_h=hull(full_points)
expected=[(Q(0),Q(0)),(Q(5,3),Q(4,3)),(Q(11,6),Q(14,9)),(Q(35,18),Q(16,9)),(Q(2),Q(2)),(Q(4,3),Q(5,3))]
assert lr_h==full_h==expected
assert len(set(lr_points))==17 and len(set(full_points))==191
assert all(all(cross(expected[i],expected[(i+1)%6],p)>=0 for i in range(6)) for p in full_points)

print('K0=', '/'.join(str(z) for z in K0))
print('K1=', '/'.join(str(z) for z in K1))
print('Kbar=', '/'.join(str(z) for z in KB))
print('TV(K0,K1)=',Q(2,9))
print('likelihood_classes=', '/'.join(str(z) for z in R))
print('thresholds: lambda_plus=5/4, lambda_minus=4/5')
print('residual_call_at_5/8=',Q(1,72))
print('full_boolean_policies=1024, lr_boolean_policies=32')
print('unique_observer_pairs: full=191, lr=17')
print('common_hull_vertices_delta_TP_delta_TQ=', '; '.join(str((str(a),str(b))) for a,b in expected))
print('PASS_EXACT_R5_FOURCLASS_NONLUMPABLE_TIME_HULL_EQUALITY')
