#!/usr/bin/env python3
"""S23/AV H20 five-block exact rational certificate (stdlib only)."""
from fractions import Fraction as F
Q=10**26
LO=545569623581288298975349314
HI=LO+1
H=7607279

def log_bounds(z):
    s,p=F(0),z
    for m in range(45):
        s+=2*p/(2*m+1)
        p*=z*z
    return s,s+2*p/(91*(1-z*z))
a,b=log_bounds(F(1,3))
c,d=log_bounds(F(1,9))
e,f=log_bounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f)
assert (3*b-e)/(c+e)<F(HI,Q)

def enc(A,B):
    return A*Q+B*(LO if B>=0 else HI),A*Q+B*(HI if B>=0 else LO)
el,eu=enc(-431,79)
tl,tu=enc(-60,11)
dl,du=enc(2074774,-380295)
gl,gu=enc(371,-68)
assert 0<dl<du<el<eu and tl>4800*eu and gl>6*eu
assert eu*(H+79)<21*Q
assert 79*60-431*11==-1
# Every 0<x<eps difference has integer b with -21<b<21.
small=[]
for beta in range(-20,21):
    if beta==0:continue
    z=abs(beta)*tl//eu
    assert z==abs(beta)*tu//el
    alpha=-z if beta>0 else z+1
    dv,dj=79*alpha+11*beta,431*alpha+60*beta
    l,u=enc(-dj,dv)
    assert 0<l<u<el
    cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    if cost<=H:small.append((beta,alpha,dv,dj,cost,l,u))
assert [s[:5] for s in small]==[
 (-3,14444,1141043,6225184,7366227),
 (-2,9630,760748,4150410,4911158),
 (-1,4815,380374,2075205,2455579),
 (1,-4814,-380295,-2074774,2455069),
 (2,-9629,-760669,-4149979,4910648),
 (3,-14443,-1140964,-6224753,7365717)]
W={}
for i in range(1,21):
    ai=i*dl//eu
    assert ai*eu<i*dl and i*du<(ai+1)*el
    V,K=i*380295+79*ai,i*2074774+431*ai
    low,high=enc(K,-V)
    assert 0<low<high<el
    W[i]=(V,K,low,high)
V=lambda i:W[i][0]
K=lambda i:W[i][1]
M=K(20)+V(20)-V(19)-1
assert (V(20)+510,M)==(H,41880515)
assert all(s[5]>W[i][3] for i in (7,12,19) for s in small)
assert all(s[5]>W[14][3] for s in small if s[0]!=2)
assert H-(V(12)+1)<4149979 # bad beta=2 excluded from block 14
assert max(H-s[4] for s in small if s[2]>0)<V(19)+1
assert H-(V(19)+1)<min(-s[3] for s in small if s[2]<0)
blocks=[(0,V(7),7),(V(7)+1,V(12),12),
        (V(12)+1,V(14),14),(V(14)+1,V(19),19),
        (V(19)+1,V(20),20)]
for left,right,i in blocks:
    assert right<=V(i) and K(i)>H and K(i)+V(i)-left<=M
    print('PASS_BLOCK',i,left,right,K(i)+V(i)-left)
for m in range(1,7):
    L=V(20)+68+79*m
    KK=K(20)+371+431*m
    low,high=enc(KK,-L)
    assert 0<low<high<gl and KK>H
    assert KK+L-(V(20)+1)<=M
    if m==6:assert L>=H
left=H*Q//LO+1
right=HI*H//Q+1
assert LO*left>H*Q and right*Q>HI*H and max(left,right)<=M
print('PASS_SUBEPS',40,len(small))
print('PASS_TOP_AND_EXTERIOR',left,right)
print('PASS_H20_EXACT_UPPER_AND_INHERITED_LOWER',V(19)+511,H,M)
