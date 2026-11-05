#!/usr/bin/env python3
"""R5 exact time octagon, balanced slice and declaration-residual hexagon."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from random import Random
Q=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
a,b=F(47,180),F(67,162)
def v(u,w): return tuple((u*Q[0][j]+w*Q[1][j])/2 for j in range(3))
def times(g,u,w,x): return (1+g+(3*u+5*w)/8+x[0]/2+x[1]+3*x[2]/2,1+g+(u+w)/2+sum(x))
def masses(g,u,w,x,j):
    vv=v(u,w);m={r:F(0) for r in R}
    m[F(1)]+=1-g;m[F(3,4)]+=(g-u)/2;m[F(5,4)]+=(g-w)/2
    for k,r in enumerate((F(1,2),F(1),F(3,2))):m[r]+=vv[k]-x[k]
    m[F(1,10)]+=(509*x[0]+9*x[2])/900+j
    m[F(1)]+=F(382,900)*(x[0]+x[2])+x[1]-2*j
    m[F(19,10)]+=(9*x[0]+509*x[2])/900+j
    assert all(z>=0 for z in m.values()) and sum(m.values())==1
    assert sum((r*m[r] for r in R),F(0))==1
    return m
def obs(m,t):return (1-sum((r*m[r]*t[r] for r in R),F(0)),sum((m[r]*t[r] for r in R),F(0)))
def cross(o,x,y):return (x[0]-o[0])*(y[1]-o[1])-(x[1]-o[1])*(y[0]-o[0])
def hull(ps):
    lo=[];up=[]
    for p in sorted(set(ps)):
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in sorted(set(ps),reverse=True):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]
ps=[]
for g,c,d,z0,z1,z2 in product((F(0),F(1)),repeat=6):
    u,w=g*c,g*d;vv=v(u,w)
    ps.append(times(g,u,w,tuple(vv[k]*z for k,z in enumerate((z0,z1,z2)))))
H=hull(ps)
assert len(set(ps))==26
assert H==[(F(1),F(1)),(F(483,160),F(221,80)),(F(519,160),F(239,80)),
          (F(613,160),F(293,80)),(F(4),F(4)),(F(559,160),F(293,80)),
          (F(211,80),F(117,40)),(F(203,80),F(113,40))]
facets=[]
for p,q in zip(H,H[1:]+H[:1]):
    dx,dy=q[0]-p[0],q[1]-p[1];aa,bb=-dy,dx;cc=aa*p[0]+bb*p[1]
    L=lcm(aa.denominator,bb.denominator,cc.denominator)
    A,B,C=(int(L*t) for t in (aa,bb,cc));G=gcd(gcd(abs(A),abs(B)),abs(C))
    facets.append((A//G,B//G,C//G))
assert facets==[(-282,323,41),(-160,160,-41),(-216,188,-139),(-2,1,-4),
                (2,-3,-4),(236,-274,-179),(80,-80,-23),(146,-123,23)]
assert all(A*x+B*y>=C for x,y in ps for A,B,C in facets)
h=F(9,10);vec=((h-1,F(1)),(F(2),F(-2)),(-h-1,F(1)))
assert tuple(sum(z[k] for z in vec) for k in (0,1))==(0,0)
area=sum(abs(x[0]*y[1]-x[1]*y[0]) for i,x in enumerate(vec) for y in vec[i+1:])
assert area==F(27,5)
rng=Random(202611060642)
for _ in range(600):
    g=F(rng.randrange(41),40);u=g*F(rng.randrange(41),40);w=g*F(rng.randrange(41),40)
    vv=v(u,w);z=[[F(rng.randrange(41),40) for _ in range(3)] for i in range(2)]
    xx=[[u_i*Q[i][k]*z[i][k]/2 for k in range(3)] for i,u_i in enumerate((u,w))]
    x=tuple(xx[0][k]+xx[1][k] for k in range(3))
    j=a*xx[0][1]+b*xx[1][1];A=u/10;B=9*w/40
    jl=x[1]*(a*A+b*B)/(A+B) if A+B else F(0)
    eps=j-jl;assert abs(eps)<=F(19,1800)
    m,ml=masses(g,u,w,x,j),masses(g,u,w,x,jl)
    t={r:F(rng.randrange(41),40) for r in R};p,q=obs(m,t);pl,ql=obs(ml,t)
    tm,t0,tp=t[F(1,10)],t[F(1)],t[F(19,10)]
    assert q-ql==eps*(tm-2*t0+tp)
    assert (p+q)-(pl+ql)==eps*h*(tm-tp)
    assert (p-pl,q-ql)==tuple(eps*sum(vec[i][k]*tval for i,tval in enumerate((tm,t0,tp))) for k in (0,1))
    tt=times(g,u,w,x)
    assert all(aa*tt[0]+bb*tt[1]>=cc for aa,bb,cc in facets)
    theta=F(rng.randrange(41),40);uniform={r:theta for r in R}
    assert obs(m,uniform)==obs(ml,uniform)==(1-theta,theta)
    assert all(F(0)<=x[k]/vv[k]<=1 for k in range(3) if vv[k])
print('PASS_EXACT_R5_BALANCED_SLICE_TIME_OCTAGON_RESIDUAL_HEXAGON')
print('policies=64 distinct_time_points=26 time_vertices=8 facets=8 profiles=600')
print('vertices='+str([(str(x),str(y)) for x,y in H]))
print('facets='+str(facets))
print('area_coefficient='+str(area)+' max_area='+str(area*F(19,1800)**2))
