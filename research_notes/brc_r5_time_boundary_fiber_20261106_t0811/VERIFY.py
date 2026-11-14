#!/usr/bin/env python3
"""Exact rational certificate: R5 all time-boundary fibers equal."""
from fractions import Fraction as Q
from itertools import product
q3=((Q(13,20),Q(1,5),Q(3,20)),(Q(1,40),Q(9,20),Q(21,40)))
alpha,beta=Q(47,180),Q(67,162)
d=beta-alpha
assert d==Q(247,1620)
VTX=((Q(1),Q(1)),(Q(483,160),Q(221,80)),(Q(519,160),Q(239,80)),
     (Q(613,160),Q(293,80)),(Q(4),Q(4)),(Q(559,160),Q(293,80)),
     (Q(211,80),Q(117,40)),(Q(203,80),Q(113,40)))
FACETS=((-282,323,41),(-160,160,-41),(-216,188,-139),(-2,1,-4),
        (2,-3,-4),(236,-274,-179),(80,-80,-23),(146,-123,23))
DEGENERACY=("X1_ZERO","A_ZERO","X1_FULL","X1_FULL",
            "X1_FULL","X1_FULL","B_ZERO","X1_ZERO")
def observed(flow):
    g,u0,u1,x0,x1,x2=flow
    return (Q(1)+g+Q(3,8)*u0+Q(5,8)*u1+x0/2+x1+Q(3,2)*x2,
            Q(1)+g+(u0+u1)/2+x0+x1+x2)
def central_limits(flow):
    _,u0,u1,_,x1,_=flow
    a,b=u0/10,Q(9,40)*u1
    lo=max(alpha*x1,beta*x1-d*a)
    hi=min(beta*x1,alpha*x1+d*b)
    assert lo<=hi
    return lo,hi,a,b
def degenerate(flow,tag):
    _,_,_,_,x1,_=flow
    _,_,a,b=central_limits(flow)
    return {"X1_ZERO":x1==0,"X1_FULL":x1==a+b,
            "A_ZERO":a==0,"B_ZERO":b==0}[tag]
def lerp(p,q,t):
    return tuple((Q(1)-t)*pi+t*qi for pi,qi in zip(p,q))
policies=[]
for g,a0,a1,z0,z1,z2 in product((0,1),repeat=6):
    u0,u1=g*a0,g*a1
    v=[(q3[0][j]*u0+q3[1][j]*u1)/2 for j in range(3)]
    x=[v[j]*z for j,z in enumerate((z0,z1,z2))]
    flow=(Q(g),Q(u0),Q(u1),*x)
    policies.append((flow,observed(flow)))
assert len(policies)==64
assert len({T for _,T in policies})==26
for flow,T in policies:
    for a,b,c in FACETS:
        assert a*T[0]+b*T[1]>=c
for n,(a,b,c) in enumerate(FACETS):
    tight=[(flow,T) for flow,T in policies if a*T[0]+b*T[1]==c]
    unique_flows={flow for flow,T in tight}
    unique_times={T for flow,T in tight}
    ends={VTX[n],VTX[(n+1)%8]}
    assert unique_times==ends,(n,unique_times,ends)
    assert len(unique_flows)==2
    p=next(flow for flow,T in tight if T==VTX[n])
    q=next(flow for flow,T in tight if T==VTX[(n+1)%8])
    tag=DEGENERACY[n]
    assert degenerate(p,tag) and degenerate(q,tag)
    for t in (Q(0),Q(1,7),Q(1,3),Q(1,2),Q(2,3),Q(1)):
        f=lerp(p,q,t)
        assert degenerate(f,tag)
        jlo,jhi,A,B=central_limits(f)
        assert jlo==jhi
        x1=f[4]
        assert (A+B)*jlo-x1*(alpha*A+beta*B)==0
        assert observed(f)==lerp(VTX[n],VTX[(n+1)%8],t)
    print(f"facet={n+1}; endpoints={len(unique_flows)}; tight_policies={len(tight)}; degeneracy={tag}; J_singleton=YES")
print("PASS_EXACT_R5_ALL_TIME_BOUNDARY_FIBERS_EQUAL")
