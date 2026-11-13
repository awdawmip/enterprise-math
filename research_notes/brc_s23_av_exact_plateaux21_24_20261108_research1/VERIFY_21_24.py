#!/usr/bin/env python3
"""Exact rational proof certificate for consecutive S23/AV plateaux 21--24."""
from fractions import Fraction as F
Q=10**26;LO=545569623581288298975349314;HI=LO+1
HMAX=9128696

def log_bounds(z):
 s,p=F(0),z
 for m in range(45):
  s+=2*p/(2*m+1);p*=z*z
 return s,s+2*p/(91*(1-z*z))
a,b=log_bounds(F(1,3));c,d=log_bounds(F(1,9));e,f=log_bounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f)
assert (3*b-e)/(c+e)<F(HI,Q)

def enc(A,B):
 return A*Q+B*(LO if B>=0 else HI),A*Q+B*(HI if B>=0 else LO)
el,eu=enc(-431,79);tl,tu=enc(-60,11)
dl,du=enc(2074774,-380295);gl,gu=enc(371,-68)
assert 0<dl<du<el<eu and tl>4800*eu and gl>6*eu
assert eu*(HMAX+79)<25*Q
assert 79*60-431*11==-1
small=[]
for beta in range(-24,25):
 if beta==0:continue
 floor=abs(beta)*tl//eu
 assert floor==abs(beta)*tu//el
 alpha=-floor if beta>0 else floor+1
 dv,dj=79*alpha+11*beta,431*alpha+60*beta
 lo,hi=enc(-dj,dv)
 assert 0<lo<hi<el
 cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
 if cost<=HMAX:small.append((beta,alpha,dv,dj,cost,lo,hi))
assert [s[:5] for s in small]==[
 (-3,14444,1141043,6225184,7366227),
 (-2,9630,760748,4150410,4911158),
 (-1,4815,380374,2075205,2455579),
 (1,-4814,-380295,-2074774,2455069),
 (2,-9629,-760669,-4149979,4910648),
 (3,-14443,-1140964,-6224753,7365717)]
w={}
for i in range(1,25):
 ai=i*dl//eu
 assert ai*eu<i*dl and i*du<(ai+1)*el
 V=i*380295+79*ai;K=i*2074774+431*ai
 low,high=enc(K,-V)
 assert 0<low<high<el
 w[i]=(V,K,low,high)
V=lambda i:w[i][0]
K=lambda i:w[i][1]
assert HMAX==V(24)+510
# 7/12/19 witness offsets beat all six narrow gaps (global in HMAX).
assert all(s[5]>w[i][3] for i in (7,12,19) for s in small)
# In the whole high strip v>V19, no sub-eps displacement can originate:
assert max(HMAX-s[4] for s in small if s[2]>0)<V(19)+1
assert HMAX-(V(19)+1)<min(-s[3] for s in small if s[2]<0)

for i in range(21,25):
 H=V(i)+510
 M=K(i)+V(i)-(V(i-1)+1)
 # Low stripes identical at all 4 endpoints; last low stripe uses w19.
 blocks=[(0,V(7),7),(V(7)+1,V(12),12),(V(12)+1,V(19),19)]
 blocks += [(V(s-1)+1,V(s),s) for s in range(20,i+1)]
 for left,right,k in blocks:
  assert right<=V(k) and K(k)>H
  assert K(k)+V(k)-left<=M, (i,k)
 # Each of the last 510 source rows has a certified gamma-short shift.
 for m in range(1,7):
  L=V(i)+68+79*m
  KK=K(i)+371+431*m
  low,high=enc(KK,-L)
  assert 0<low<high<gl and KK>H
  assert KK+L-(V(i)+1)<=M
  if m==6:assert L>=H
 left=H*Q//LO+1
 right=HI*H//Q+1
 assert LO*left>H*Q and right*Q>HI*H
 assert max(left,right)<=M
 print('PASS_PLATEAU',i,'h_start',V(i-1)+511,'h_end',H,'N',M,
       'blocks',len(blocks),'exterior',left,right)
print('PASS_S23_AV_EXACT_PLATEAUX_21_TO_24','candidate_b',48,'embedded',6)
