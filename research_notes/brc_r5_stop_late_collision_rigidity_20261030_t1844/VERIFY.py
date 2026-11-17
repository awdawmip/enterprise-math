#!/usr/bin/env python3
"""Exact Fraction checker for R5 late-collision rigidity on a stop-only diamond.
No numerical optimization and no network calls. The all-real theorem is in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product

P=(F(7,40),F(9,40),F(3,40),F(21,40))
Q=(F(7,20),F(3,20),F(3,20),F(7,20))
piP=(sum(P[:2]),sum(P[2:]))
piQ=(sum(Q[:2]),sum(Q[2:]))
r=(F(1,2),F(3,2))

def vector(s,y,d,t):
    ep=eq=tp=tq=F(0)
    for x,u in product(range(2),repeat=2):
        i=2*x+u
        k=(1-s[x])*(F(1,4)+F(x,8)+d[x])+s[x]*(F(1,4)+F(x,8)+x*y[i]*t[u])
        stop=(1-s[x])*2+s[x]*(4-y[i])
        ep+=P[i]*k;eq+=Q[i]*k
        tp+=P[i]*stop;tq+=Q[i]*stop
    return (ep,eq,tp,tq)

def sgn(v):return 1 if v>0 else -1

def function_for_u(t,u):
    eps=r[u]*abs(t[u])/2
    A=F(5) if u==0 else F(-5)
    B=-A*r[u]+eps
    return (F(sgn(t[u])),F(0),A,B)

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def support(d,t,full,L):
    ymax=4 if full else 2
    best=None; policy=None
    for s in product((0,1),repeat=2):
        for yy in product((0,1),repeat=ymax):
            y=yy if full else (yy[0],yy[1],yy[0],yy[1])
            v=vector(s,y,d,t)
            score=dot(L,v)
            if best is None or score>best:
                best=score;policy=(s,yy,v)
    return best,policy

def late_gain(x,u,t,L):
    i=2*x+u
    return L[0]*P[i]*x*t[u]+L[1]*Q[i]*x*t[u]-L[2]*P[i]-L[3]*Q[i]

def formula_gap(t,u):
    return (F(3,80) if u==0 else F(9,80))*abs(t[u])

all_params=[
 ((F(0),F(0)), (F(0),F(0))),
 ((F(1,8),F(-1,8)),(F(1,8),F(0))),
 ((F(-1,5),F(2,5)),(F(-1,5),F(1,4))),
 ((F(7,10),F(3,5)),(F(1,2),F(-1,4))),
 ((F(-1,5),F(-1,3)),(F(-1,4),F(-1,8))),
 ((F(1,2),F(1,3)),(F(5,9),F(-1,3))),
 ((F(0),F(0)),(F(0),F(1,3))),
 ((F(0),F(0)),(F(-1,8),F(0))),
 ((F(1,3),F(1,4)),(F(-1,10),F(3,7))),
]
num_cases=0
for d,t in all_params:
    assert F(-1,4)<d[0]<F(3,4) and F(-3,8)<d[1]<F(5,8)
    assert all(F(-3,8)<z<F(5,8) for z in t)
    assert sum(P)==sum(Q)==1
    assert piP==(F(2,5),F(3,5)) and piQ==(F(1,2),F(1,2))
    assert P[0]/Q[0]==P[2]/Q[2]==r[0]
    assert P[1]/Q[1]==P[3]/Q[3]==r[1]
    for x,u,ybit in product(range(2),range(2),range(2)):
        assert 0<F(1,4)+F(x,8)+x*ybit*t[u]<1
        assert 0<F(1,4)+F(x,8)+d[x]<1
    for u in range(2):
        if t[u]==0:continue
        L=function_for_u(t,u)
        full,pfull=support(d,t,True,L)
        lr,plr=support(d,t,False,L)
        assert full-lr==formula_gap(t,u),(d,t,u,full-lr,formula_gap(t,u))
        assert pfull[0]==(1,1) and plr[0]==(1,1)
        assert pfull[1][2+u]==1
        g0=late_gain(0,u,t,L);g1=late_gain(1,u,t,L)
        assert g0<0 and g1>0
        other=1-u
        assert late_gain(0,other,t,L)<0 and late_gain(1,other,t,L)<0
        assert (g0,g1)==(-abs(t[u])*P[u]/2,abs(t[u])*P[2+u]/2)
        for x in range(2):
            assert F(5)*Q[2*x+other]-piP[x]>0
        num_cases+=1

s_vals=(F(0),F(1,4),F(2,3),F(1))
y_vals=(F(0),F(1,3),F(3,5),F(1))
d=(F(1,10),F(1,20));t=(F(0),F(0))
num_equiv=0
for s0,s1 in product(s_vals,repeat=2):
    s=(s0,s1)
    for y0,y1,y2,y3 in product(y_vals,repeat=4):
        y=(y0,y1,y2,y3)
        ys=[]
        for u in (0,1):
            denom=sum(Q[2*x+u]*s[x] for x in (0,1))
            ys.append(sum(Q[2*x+u]*s[x]*y[2*x+u] for x in (0,1))/denom if denom else F(0))
        assert all(0<=z<=1 for z in ys)
        full=vector(s,y,d,t)
        lr=vector(s,(ys[0],ys[1],ys[0],ys[1]),d,t)
        assert full==lr,(s,y,ys,full,lr)
        num_equiv+=1

def det(M):
    n=len(M); a=[row[:] for row in M]; val=F(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:
            a[i],a[pivot]=a[pivot],a[i];val=-val
        z=a[i][i];val*=z
        for j in range(i+1,n):
            if a[j][i]:
                factor=a[j][i]/z
                for k in range(i,n):a[j][k]-=factor*a[i][k]
    return val

def lrpoint(s,yy,d):return vector(s,(yy[0],yy[1],yy[0],yy[1]),d,(F(0),F(0)))
vbase=lrpoint((0,0),(0,0),d)
points=[lrpoint((1,0),(0,0),d),lrpoint((0,1),(0,0),d),
        lrpoint((1,1),(1,0),d),lrpoint((1,1),(0,1),d)]
M=[[v[j]-vbase[j] for v in points] for j in range(4)]
actual=det(M)
assert actual==d[0]*d[1]/40,(actual,d[0]*d[1]/40)
print('PINNED_WEIGHTS P=',','.join(map(str,P)),'Q=',','.join(map(str,Q)))
print('CHECKED_SIGNED_GAPS',num_cases,'RATIONAL_PARAMETERS',len(all_params))
print('CHECKED_REAL_BEHAVIOR_CONSTRUCTION_RATIONAL_INSTANCES',num_equiv)
print('FOUR_DIMENSIONAL_AFFINE_DETERMINANT',actual,'FORMULA_d0d1_over_40',d[0]*d[1]/40)
print('PASS_EXACT_R5_STOP_ONLY_LATE_COLLISION_RIGIDITY')
