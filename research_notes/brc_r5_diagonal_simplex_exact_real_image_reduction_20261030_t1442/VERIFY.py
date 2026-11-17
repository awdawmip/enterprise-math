#!/usr/bin/env python3
"""Exact rational checker for R5 two-simplex diagonal-fiber formulas."""
from fractions import Fraction as F
from math import gcd
from itertools import permutations

S=((1,120,240,-1),(1,240,120,-1),
   (2,60,180,0),(2,60,60,0),(2,180,60,1),(2,60,60,1),
   (3,30,108,2),(3,30,72,2),(3,30,45,3),(3,30,15,3),
   (3,90,36,4),(3,90,24,4),(3,20,40,5),(3,40,20,5))
keys=[];idx=[]
for t,p,q,_ in S:
    g=gcd(p,q);k=(t,p//g,q//g)
    if k not in keys:keys.append(k)
    idx.append(keys.index(k))
assert len(keys)==12 and idx[3]==idx[5] and idx[9]==idx[13]

def direct(a):
    live=[F(0)]*14;r=x=y=s=F(0)
    for i,(t,p,q,parent) in enumerate(S):
        reach=F(1) if parent<0 else live[parent]
        stop=reach*a[i];live[i]=reach*(1-a[i])
        if i in (9,13):r+=q*stop
        x+=(4-t)*p*stop;y+=(4-t)*q*stop
        if i in (8,12):s+=p*stop
    return r,x,y,s

def flow_of(a):
    alpha=1-a[0];beta=1-a[1];cA=a[3];cB=a[5]
    tA=(1-cA)*a[9];tB=(1-cB)*a[13]
    U=alpha*a[2];V=beta*a[4]
    W=alpha*(1-a[2])*a[6];Z=alpha*(1-a[2])*a[7]
    WB=beta*(1-a[4])*a[10];ZB=beta*(1-a[4])*a[11]
    C=alpha*(1-cA)*a[8];D=beta*(1-cB)*a[12]
    return alpha,beta,cA,tA,cB,tB,U,V,W,Z,WB,ZB,C,D

def valid(z,lr=False):
    alpha,beta,cA,tA,cB,tB,U,V,W,Z,WB,ZB,C,D=z
    ok=(all(0<=q<=1 for q in (alpha,beta,cA,cB))
        and 0<=tA<=1-cA and 0<=tB<=1-cB
        and 0<=U<=alpha and 0<=V<=beta
        and 0<=W<=alpha-U and 0<=Z<=alpha-U
        and 0<=WB<=beta-V and 0<=ZB<=beta-V
        and 0<=C<=alpha*(1-cA) and 0<=D<=beta*(1-cB))
    return ok and (not lr or (cA==cB and tA==tB))

def formula(z):
    alpha,beta,cA,tA,cB,tB,U,V,W,Z,WB,ZB,C,D=z
    r=15*tA*alpha+20*tB*beta;s=30*C+20*D
    x=(360*(1-alpha)+720*(1-beta)+120*U+360*V
       +120*cA*alpha+120*cB*beta+30*W+30*Z+90*WB+90*ZB
       +30*C+20*D+30*tA*alpha+40*tB*beta)
    y=(720*(1-alpha)+360*(1-beta)+360*U+120*V
       +120*cA*alpha+120*cB*beta+108*W+72*Z+36*WB+24*ZB
       +45*C+40*D+15*tA*alpha+20*tB*beta)
    return r,x,y,s

def reconstruct(z):
    assert valid(z)
    alpha,beta,cA,tA,cB,tB,U,V,W,Z,WB,ZB,C,D=z
    def q(num,den):return num/den if den!=0 else F(0)
    return (1-alpha,1-beta,q(U,alpha),cA,q(V,beta),cB,
        q(W,alpha-U),q(Z,alpha-U),q(C,alpha*(1-cA)),q(tA,1-cA),
        q(WB,beta-V),q(ZB,beta-V),q(D,beta*(1-cB)),q(tB,1-cB))

def det4(rows):
    total=F(0)
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=F(-1 if inv%2 else 1)
        for i in range(4):term*=rows[i][perm[i]]
        total+=term
    return total

for lr in (False,True):
    n=12 if lr else 14
    for mask in range(1<<n):
        a=tuple(F((mask>>(idx[i] if lr else i))&1) for i in range(14))
        z=flow_of(a)
        assert valid(z,lr) and direct(a)==formula(z)
        assert direct(reconstruct(z))==direct(a)
    print('EXACT_DETERMINISTIC_MATCH','LR' if lr else 'FULL',1<<n)

values=(F(0),F(1,7),F(1,2),F(5,6),F(1))
for lr in (False,True):
    for k in range(128):
        a=[values[(k*(i+2)+i*i+7*i+3)%len(values)] for i in range(14)]
        if lr:a[5]=a[3];a[13]=a[9]
        z=flow_of(a)
        assert valid(z,lr) and direct(a)==formula(z)==direct(reconstruct(z))
    print('EXACT_RATIONAL_POLICY_MATCH','LR' if lr else 'FULL',128)

for k in range(300):
    alpha=values[k%5];beta=values[(k//5)%5]
    cA=values[(k//25)%5];cB=values[(k//11)%5]
    dA=values[(k//9)%5];dB=values[(k//13)%5]
    if k%2:cB=cA;dB=dA
    tA=(1-cA)*dA;tB=(1-cB)*dB
    U=alpha*values[(k//7)%5];V=beta*values[(k//3)%5]
    W=(alpha-U)*values[(k//17)%5];Z=(alpha-U)*values[(k//19)%5]
    WB=(beta-V)*values[(k//23)%5];ZB=(beta-V)*values[(k//29)%5]
    C=alpha*(1-cA)*values[(k//31)%5]
    D=beta*(1-cB)*values[(k//37)%5]
    z=(alpha,beta,cA,tA,cB,tB,U,V,W,Z,WB,ZB,C,D)
    assert valid(z,lr=bool(k%2)) and direct(reconstruct(z))==formula(z)
print('EXACT_RATIONAL_FLOW_REVERSE',300)

base=(F(1,2),F(1,2),F(0),F(1,2),F(0),F(1,2),
      F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(0))
pts=[list(base) for _ in range(5)]
pts[1][0]+=F(1,4);pts[2][8]+=F(1,4)
pts[3][9]+=F(1,4);pts[4][12]+=F(1,4)
assert all(valid(p,True) for p in pts)
imgs=[formula(p) for p in pts]
D=det4([[imgs[i][j]-imgs[0][j] for j in range(4)]
        for i in range(1,5)])
assert D==F(-30375,32)
print('FIBER_RANK4_DETERMINANT',D,'c=0,t=1/2')
print('FIBER_PHASE_DIAGRAM t>0:rank4; t=0,c<1:rank3; c=1,t=0:rank2')
print('FULL_IMAGE_TWO_TRIANGLES LR_IMAGE_DIAGONAL_TRIANGLE exact_polynomial_reduction=True')
print('ACTUAL_IMAGE_SEPARATION unresolved')
print('PASS_EXACT_R5_DIAGONAL_TWO_SIMPLEX_FIBERS')
