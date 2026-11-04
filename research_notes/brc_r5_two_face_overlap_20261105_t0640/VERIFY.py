#!/usr/bin/env python3
"""R5 exact rational two-face tangent match; four-dimensional support separation."""
from fractions import Fraction as F
from itertools import product
R_RAW=['1/4','1/2','1','3/2','7/4']
S_RAW=['1/16','1/4','1/2','1','3/2','7/4','2']
K_RAW=[['209/1000','23/125','107/500','23/125','209/1000'],['191/1000','27/125','93/500','27/125','191/1000']]
U_RAW=[[['227/1250','1/10000','1/10000','1/10000','269/10000','1/10000','1/10000'],['249719/1884375','1/10000','1/10000','522091/30150000','6329/2010000','1/10000','12347/402000'],['3203/33750','1/10000','1/10000','1/10000','1/10000','32021/270000','1/10000'],['1/10000','1/10000','1/10000','117/1280','1/10000','1/10000','2947/32000'],['1/10000','74591/18760000','60197/2010000','1/10000','1/10000','1/10000','9830719/56280000']],[['570523/3731250','203/1990000','203/1990000','1122121/29850000','1/10000','1/10000','1/10000'],['20444/124375','1/10000','1/10000','1/10000','1/10000','40203/1990000','61737/1990000'],['1/10000','1/10000','9/80000','14831/80000','1/10000','1/10000','1/10000'],['1/10000','1/10000','1/10000','3419767/31840000','203/1990000','203/1990000','27533/254720'],['203/1990000','1343829/55720000','1/10000','81537/15920000','1/10000','1/10000','17981823/111440000']]]
R=list(map(F,R_RAW));S=list(map(F,S_RAW))
K=[[F(v) for v in row] for row in K_RAW]
U=[[[F(v) for v in row] for row in h] for h in U_RAW]
W=[F(1,2),F(1,2)]
LO=(0,1);HI=(3,4)
assert len(S)==7 and len(U)==2 and sum(W)==1
for h in range(2):
    assert sum(K[h])==1
    assert sum(K[h][j]*R[j] for j in range(5))==1
    for j in range(5):
        assert all(u>0 for u in U[h][j])
        assert sum(U[h][j])==K[h][j]
        assert sum(s*u for s,u in zip(S,U[h][j]))==K[h][j]*R[j]
        assert sum((s/R[j])*(u/K[h][j]) for s,u in zip(S,U[h][j]))==1
assert K[0]!=K[1]
def f_lo(h,t):
    return t-1+sum(K[h][j]*max(F(0),t-R[j]) for j in range(5))
def f_hi(h,t):
    return 1-t+sum(K[h][j]*max(F(0),R[j]-t) for j in range(5))
for h in range(2):
    assert f_lo(h,F(23,28))==0
    assert f_hi(h,F(33,28))==0
def effective(h,Js):
    L=1+sum(K[h][j] for j in Js)
    mu={s:F(0) for s in S}
    for j in range(5):
        if j in Js:
            for s,u in zip(S,U[h][j]):mu[s]+=u
        else:mu[R[j]]+=K[h][j]
    assert sum(mu.values())==1 and sum(s*v for s,v in mu.items())==1
    return L,{s:(mu[s]-(1 if s==1 else 0))/L for s in S}
for Js in (LO,HI):
    LA,DA=effective(0,Js);LB,DB=effective(1,Js)
    assert DA==DB and LA!=LB
print('PASS_TWO_FACE_ALL_ATOM_SIGNED_PROFILES')
def bellman(n,detail=False):
    a,b,c,d=map(F,n)
    C=lambda r:max(a*r,b)
    base=C(F(1))+c+d
    V=[[c*R[j]+d+sum(U[h][j][i]*C(s) for i,s in enumerate(S))/K[h][j]-C(R[j]) for j in range(5)] for h in range(2)]
    zh=[c+d+sum(K[h][j]*(C(R[j])-C(F(1))+max(F(0),V[h][j])) for j in range(5)) for h in range(2)]
    zlr=c+d+sum(sum(W[h]*K[h][j] for h in range(2))*(C(R[j])-C(F(1)))+max(F(0),sum(W[h]*K[h][j]*V[h][j] for h in range(2))) for j in range(5))
    full=base+sum(W[h]*max(F(0),zh[h]) for h in range(2))
    lr=base+max(F(0),zlr)
    assert full>=lr
    return (full,lr,zh,V,zlr) if detail else (full,lr)
def direct(n):
    a,b,c,d=map(F,n)
    C=lambda r:max(a*r,b)
    base=C(F(1))+c+d
    G=[[c*R[j]+d+sum(U[h][j][i]*C(s) for i,s in enumerate(S))/K[h][j]-C(R[j]) for j in range(5)] for h in range(2)]
    fo=[]
    for h in range(2):
        best=max(max(F(0),c+d+sum(K[h][j]*(C(R[j])-C(F(1))+mask[j]*G[h][j]) for j in range(5))) for mask in product((0,1),repeat=5))
        fo.append(best)
    full=base+sum(W[h]*fo[h] for h in range(2))
    lr_cont=max(sum(W[h]*(c+d+sum(K[h][j]*(C(R[j])-C(F(1))+mask[j]*G[h][j]) for j in range(5))) for h in range(2)) for mask in product((0,1),repeat=5))
    lr=base+max(F(0),lr_cont)
    return full,lr
n=(F(-1),F(-1),F(-1,4),F(1,32))
hF,hLR,zh,V,zlr=bellman(n,True)
assert (hF,hLR)==(F(-43861931587,38399040000),F(-1398408419,1199970000))
assert hF-hLR==F(7393,320000) and direct(n)==(hF,hLR)
assert all(z>0 for z in zh)
ep=eq=tp=tq=F(0)
for h in range(2):
    for j in range(5):
        leaves=[(s,W[h]*U[h][j][i],3) for i,s in enumerate(S)] if V[h][j]>0 else [(R[j],W[h]*K[h][j],2)]
        for r,q,t in leaves:
            if r<=1:ep+=r*q
            else:eq+=q
            tp+=t*r*q;tq+=t*q
WITNESS=(ep,eq,tp,tq)
assert WITNESS==(F(2069975993,14399640000),F(1856086801,3599910000),F(3573,1600),F(4823,2000))
assert sum(a*b for a,b in zip(n,WITNESS))==hF
bound=(hF-hLR)/sum(map(abs,n))
assert bound==F(7393,730000)
for a,b in [(-1,-1),(-1,-F(1,4)),(-1,-F(3,4))]:
    for c in [F(-1,4),F(0),F(1,4)]:
        for d in [F(-1,8),F(0),F(1,8)]:
            nn=(F(a),F(b),c,d)
            assert bellman(nn)==direct(nn)
print('R5_OVERLAP_EXACT_RATIOS',len(R),len(S),'Q_MASS_ROWS',len(U)*len(U[0]))
print('TANGENT_THRESHOLD_LO',F(23,28),'HI',F(33,28))
print('SIGNED_TANGENT_EQUALITY_LO_AND_HI EXACT_ALL_ATOMS')
print('SEPARATING_NORMAL',tuple(map(str,n)))
print('FULL_SUPPORT',hF)
print('LR_SUPPORT',hLR)
print('GAP',hF-hLR)
print('FULL_WITNESS',tuple(map(str,WITNESS)))
print('LINF_DISTANCE_LOWER_BOUND',bound)
print('INDEPENDENT_ENUM_DIRECTIONS',27)
print('PASS_EXACT_R5_TWO_FACE_OVERLAP_NONSUFFICIENCY')
