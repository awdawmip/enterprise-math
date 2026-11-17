#!/usr/bin/env python3
"""Exact complete facet certificate of 2D FULL/LR STOP-time hull equality.
Uses Fraction hull construction; independent 2^18 FULL deterministic enumeration.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm, gcd
RU=(F(3,4),F(5,4))
RV=(F(1,2),F(1),F(3,2))
def k(t,u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)
def hull(points):
    ps=sorted(set(points))
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in ps:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(ps):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]
def lr_points(A,B,t0,t1):
    Q={(0,0):A,(1,0):F(1,2)-A,(0,1):B,(1,1):F(1,2)-B}
    masses=[]
    for x,u,v in product((0,1),(0,1),range(3)):
        q=Q[x,u]*k((t0,t1)[x],u)[v]
        masses.append((x,u,v,RV[v]*q,q))
    pts=[]
    for bits in range(128):
        tp=tq=F(0)
        for x,u,v,p,q in masses:
            e=(bits>>x)&1;m=(bits>>(2+u))&1;l=(bits>>(4+v))&1
            tau=2 if not e else (3 if not m else (4 if not l else 5))
            tp+=p*tau;tq+=q*tau
        pts.append((tp,tq))
    return pts
def supports(A,B,t0,t1,cP,cQ):
    Q={(0,0):A,(1,0):F(1,2)-A,(0,1):B,(1,1):F(1,2)-B}
    L=[max(F(0),cP*r+cQ) for r in RV]
    G={(x,u):cP*RU[u]+cQ+sum(k((t0,t1)[x],u)[v]*L[v] for v in range(3)) for x,u in product((0,1),repeat=2)}
    full=2*(cP+cQ)+sum(max(F(0),sum(Q[x,u]*(cP*RU[u]+cQ+max(F(0),G[x,u])) for u in (0,1))) for x in (0,1))
    lr=2*(cP+cQ)+max(sum(max(F(0),sum(Q[x,u]*(cP*RU[u]+cQ+h[u]*G[x,u]) for u in (0,1))) for x in (0,1)) for h in product((0,1),repeat=2))
    assert full>=lr
    return full,lr

A,B,t0,t1=F(49,100),F(1,100),F(1,16),F(1,8)
Q={(0,0):A,(1,0):F(1,2)-A,(0,1):B,(1,1):F(1,2)-B}
rows=[]
for x,u,v in product((0,1),(0,1),range(3)):
    q=Q[x,u]*k((t0,t1)[x],u)[v];p=RV[v]*q
    assert p>0 and q>0
    rows.append((x,u,v,p,q))
assert sum(r[3] for r in rows)==sum(r[4] for r in rows)==1
rx=[sum(Q[x,u]*RU[u] for u in (0,1))/sum(Q[x,u] for u in (0,1)) for x in (0,1)]
assert rx[0]!=rx[1]
poly=hull(lr_points(A,B,t0,t1))
assert len(poly)==10

def prim_normal(p,n):
    # For CCW hull an outward normal is (dy,-dx).
    dx=n[0]-p[0];dy=n[1]-p[1]
    den=lcm(dy.denominator,dx.denominator)
    nx=int(dy*den);ny=-int(dx*den)
    d=gcd(abs(nx),abs(ny))
    return nx//d,ny//d

facets=[]
for j,p in enumerate(poly):
    n=poly[(j+1)%len(poly)]
    nx,ny=prim_normal(p,n)
    beta=nx*p[0]+ny*p[1]
    assert nx*n[0]+ny*n[1]==beta
    assert all(nx*z[0]+ny*z[1]<=beta for z in lr_points(A,B,t0,t1))
    f,l=supports(A,B,t0,t1,F(nx),F(ny))
    assert l==beta and f==beta
    facets.append((nx,ny,beta))

# SECOND CHECK: independently verify every FULL deterministic policy pair lies
# inside each LR polygon facet using exact scaled integers; no Bellman formulas.
den=lcm(*(n.denominator for row in rows for n in row[3:]))
introws=[(x,u,v,int(p*den),int(q*den)) for x,u,v,p,q in rows]
assert all(beta*den==int(beta*den) for _,_,beta in facets)
beta_int=[int(beta*den) for _,_,beta in facets]
count=0
for bits in range(1<<18):
    tp=tq=0
    for x,u,v,p,q in introws:
        e=(bits>>x)&1
        m=(bits>>(2+2*x+u))&1
        l=(bits>>(6+6*x+3*u+v))&1
        tau=2 if not e else (3 if not m else (4 if not l else 5))
        tp+=p*tau;tq+=q*tau
    assert all(nx*tp+ny*tq<=beta_int[j] for j,(nx,ny,_) in enumerate(facets))
    count+=1
print('PARAMETERS A=',A,'B=',B,'t0=',t0,'t1=',t1)
print('TIME2_LR_RATIOS',rx)
print('TOTAL_QP_MASS',sum(r[4] for r in rows),sum(r[3] for r in rows),'STRICT_POSITIVE_LEAVES',len(rows))
print('LR_POLYGON_VERTICES',len(poly),'FULL_POLICIES_EXHAUSTED',count,'LR_POLICIES_EXHAUSTED',128)
for j,(p,(nx,ny,beta)) in enumerate(zip(poly,facets)):
    print('FACET',j,'VERTEX',p,'NORMAL',(nx,ny),'SUPPORT',beta,'GAP',F(0))
print('PASS_EXACT_R5_OFFDIAGONAL_TIME_HULL_EQUALITY_FACETS_AND_FULL_EXHAUSTION')
