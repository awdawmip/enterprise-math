#!/usr/bin/env python3
"""R546 frozen signed-BRC k=9 exact rational Rouché certificate (no float in proof)."""
from fractions import Fraction as F
from math import comb,isqrt
from itertools import combinations
def z(a=0,b=0): return F(a),F(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]*a[0]+a[1]*a[1]
def lower(a,S=10**8):
 q=norm2(a);return F(isqrt(q.numerator*S*S//q.denominator),S)
def upper(a,S=10**8):
 q=norm2(a);b=lower(a,S);return b if b*b==q else b+F(1,S)
def C(k):return comb(2*k,k)//(k+1)
def H(k,t):
 r=2*k+1
 if not (2<=t<=r):return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
def poly(k):
 d=2*k-1;p={t:F(H(k,t),C(k)) for t in range(2,2*k+2)}
 a=[(-1)**(j-1)*p[j+2]/p[2] for j in range(1,d+1)]
 return [F(1)]+[-v for v in a],a,p
def taylor(P,c):
 out=[z(0)]
 for v in P:
  nxt=[z(0)]*(len(out)+1)
  for j,b in enumerate(out):
   nxt[j]=add(nxt[j],mul(c,b));nxt[j+1]=add(nxt[j+1],b)
  nxt[0]=add(nxt[0],z(v));out=nxt
 assert out[-1]==z(0)
 return out[:-1]
CENTERS=[
 ('4.987574458','6.397700798'),('4.987574458','-6.397700798'),
 ('4.239048304','0'),('2.137768258','1.688666202'),('2.137768258','-1.688666202'),
 ('1.256608602','0.841661503'),('1.256608602','-0.841661503'),
 ('0.891775713','0.513743230'),('0.891775713','-0.513743230'),
 ('0.693474041','0.349446695'),('0.693474041','-0.349446695'),
 ('0.569768654','0.249906965'),('0.569768654','-0.249906965'),
 ('0.486291428','0.178263380'),('0.486291428','-0.178263380'),
 ('0.423881361','0.116970197'),('0.423881361','-0.116970197')]
def certify():
 k=9;P,a,p=poly(k);d=len(P)-1;eps=F(1,1000)
 centers=[z(*v) for v in CENTERS]
 assert len(centers)==d
 assert centers[0][0]==centers[1][0] and centers[0][1]==-centers[1][1]
 ratios=[]
 for ix,c in enumerate(centers):
  b=taylor(P,c)
  lhs=upper(b[0])+sum(upper(b[j])*eps**j for j in range(2,d+1))
  rhs=lower(b[1])*eps
  assert rhs>lhs,(k,ix,'ROUCHE_FAIL')
  ratios.append(lhs/rhs)
 pairs=list(combinations(range(d),2))
 assert all(lower(sub(centers[i],centers[j]))>2*eps for i,j in pairs)
 dom=min(lower(centers[i])-eps for i in (0,1))
 rem=max(upper(centers[i])+eps for i in range(2,d))
 assert dom>8 and rem<F(17,4) and dom>rem
 assert centers[0][1]>eps and centers[1][1]<-eps
 assert max(ratios)<F(1,40)
 seq=[F(1)]
 for m in range(1,1025):
  seq.append(sum(a[j-1]*seq[m-j] for j in range(1,min(m,d)+1)))
 changes=[m for m in range(1,len(seq)) if seq[m]*seq[m-1]<0]
 plus=sum(x>0 for x in seq);minus=sum(x<0 for x in seq)
 assert plus==516 and minus==509 and len(changes)==295 and not any(x==0 for x in seq)
 print('R546_RATIONAL_ROUCHE_PASS','degree',d,'Catalan',C(k),'p2',p[2])
 print('disk_count',d,'disjoint_pairs',len(pairs),'radius',eps)
 print('max_Rouche_ratio_lt_1/40',max(ratios)<F(1,40))
 print('dominant_y_lower',dom,'other_y_upper',rem)
 print('dominant_X_gt',8*p[2],'other_X_lt',F(17,4)*p[2])
 print('first_1025',plus,minus,'adjacent_sign_changes',len(changes),'first_changes',changes[:24])
if __name__=='__main__':certify()
