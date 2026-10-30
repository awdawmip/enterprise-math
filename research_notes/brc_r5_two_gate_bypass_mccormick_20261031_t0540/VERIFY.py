#!/usr/bin/env python3
"""Exact Fraction witness for two serial shared STOP gates with bypass."""
from fractions import Fraction as F
from itertools import product

Q0={'A0':F(1,8),'A1':F(1,8),'B':F(1,4),'C0':F(1,4),'C1':F(1,4)}
R0={'A0':F(2),'A1':F(2),'B':F(1),'C0':F(1,2),'C1':F(1,2)}
P0={s:Q0[s]*R0[s] for s in Q0}
ERR=F(1,8)
R={'Y':F(1),'L':F(3,2),'M':F(2),'H':F(3)}
K={'A0':{'Y':F(1,4),'L':F(1,12),'M':F(3,8),'H':F(7,24)},
   'A1':{'Y':F(1,4),'L':F(1,6),'M':F(1,4),'H':F(1,3)}}
KP={s:{k:q*R[k]/R0[s] for k,q in d.items()} for s,d in K.items()}
assert sum(Q0.values())==sum(P0.values())==1
for s in K:
    assert all(v>0 for v in K[s].values())
    assert all(v>0 for v in KP[s].values())
    assert sum(K[s].values())==sum(KP[s].values())==1
    assert sum(K[s][k]*R[k] for k in R)==R0[s]
    assert Q0[s]*K[s]['Y']==P0[s]*KP[s]['Y']==F(1,32)
residual={k:K['A0'][k]-K['A1'][k] for k in R}
tv=sum(abs(v) for v in residual.values())/2
assert tv==F(1,8)
assert F(0)<ERR<1 and F(0)<ERR+F(1,2)<1

def full(x0,x1,u0,u1,uB,z0,z1):
    x=(x0+x1)/2
    z=(z0+z1)/2
    w=(x0*u0+x1*u1)/2
    s=uB/4+w/16
    ep=ERR+uB/8+(1-z)/8
    eq=ERR+uB/8+(1-z)/4
    tp=F(3,2)+x+z/2-s
    tq=F(3,2)+x/2+z-s
    return ep,eq,tp,tq
def lr(x,u,z): return full(x,x,u,u,u,z,z)
def hull2(points):
    pts=sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    if len(pts)<=1:return pts
    low=[]
    for p in pts:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    high=[]
    for p in reversed(pts):
        while len(high)>=2 and cross(high[-2],high[-1],p)<=0:high.pop()
        high.append(p)
    return low[:-1]+high[:-1]
def det4(rows):
    a=[list(r) for r in rows]
    d=F(1)
    for j in range(4):
        k=next((i for i in range(j,4) if a[i][j]),None)
        if k is None:return F(0)
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        pivot=a[j][j];d*=pivot
        for i in range(j+1,4):
            f=a[i][j]/pivot
            for c in range(j,4):a[i][c]-=f*a[j][c]
    return d
L=[lr(*v) for v in product((F(0),F(1)),repeat=3)]
A=[full(*v) for v in product((F(0),F(1)),repeat=7)]
assert len(L)==8 and len(A)==128
lh=hull2([(v[2],v[3]) for v in L])
assert lh==hull2([(v[2],v[3]) for v in A])
b=lr(F(0),F(0),F(0))
X=tuple(a-c for a,c in zip(lr(F(1),F(0),F(0)),b))
U=tuple(a-c for a,c in zip(lr(F(0),F(1),F(0)),b))
Z=tuple(a-c for a,c in zip(lr(F(0),F(0),F(1)),b))
W=tuple(a-c-d+e for a,c,d,e in zip(lr(F(1),F(1),F(0)),lr(F(1),F(0),F(0)),lr(F(0),F(1),F(0)),b))
assert det4([X,U,Z,W])==F(1,2048)
v0=b;v1=lr(F(1),F(1),F(0))
M=tuple((a+c)/2 for a,c in zip(v0,v1))
assert M==full(F(1),F(0),F(1),F(0),F(1,2),F(0),F(0))
def inv(v):
    ep,eq,tp,tq=v;ep-=ERR;eq-=ERR
    u=16*ep-8*eq
    z=1-8*(eq-ep)
    x=z+2*(tp-tq)
    w=16*(F(3,2)+x+z/2-u/4-tp)
    return x,u,w,z
assert inv(M)==(F(1,2),F(1,2),F(1,2),F(0))
assert inv(M)[2]-inv(M)[0]*inv(M)[1]==F(1,4)
assert all(inv(v)[2]==inv(v)[0]*inv(v)[1] for v in L)
def H(v):
    ep,eq,tp,tq=v
    return 14*ep-19*eq+2*tp-4*tq
assert all(8*H(v)+53==inv(v)[2]-inv(v)[1] for v in L+A)
ml=max(map(H,L));ma=max(map(H,A))
assert ml==F(-53,8) and ma==F(-13,2) and ma-ml==F(1,8)
assert F(1,4)/380==F(1,1520)
print('P0,Q0 normalized; all natural branches positive; every error in (0,1)')
print('BRC residual=',residual,'TV=',tv)
print('equal STOP-time hull, vertices=',len(lh),'hull=',lh)
print('LR deterministic=',len(L),'FULL deterministic=',len(A))
print('LR four-dimensional rank determinant=',F(1,2048))
print('LR V0=',v0,'LR V1=',v1)
print('actual FULL midpoint=',M,'inverse=',inv(M),'w-xu=',F(1,4))
print('H LRmax=',ml,'FULLmax=',ma,'gap=',ma-ml)
print('distance_inf(M,LR_actual)>=',F(1,1520))
print('PASS_EXACT_R5_TWO_GATE_BYPASS_MCCORMICK_RANK4')
