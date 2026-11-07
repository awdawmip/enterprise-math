#!/usr/bin/env python3
"""R547: k=10 signed BRC fixed-k all-order oscillation, exact Rouché certificate."""
from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations
def z(a=0,b=0): return F(a),F(b)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[0],a[1]-b[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def n2(a): return a[0]*a[0]+a[1]*a[1]
def lower(a,S=10**9):
 q=n2(a);return F(isqrt(q.numerator*S*S//q.denominator),S)
def upper(a,S=10**9):
 b=lower(a,S);return b if b*b==n2(a) else b+F(1,S)
def C(k):return comb(2*k,k)//(k+1)
def H(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
def normalized(k):
 d=2*k-1; p={t:F(H(k,t),C(k)) for t in range(2,2*k+2)}
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
 ('6.033407511','7.862167698'),('6.033407511','-7.862167698'),
 ('4.657220455','0'),
 ('2.609715406','2.026761208'),('2.609715406','-2.026761208'),
 ('1.493590960','0.999922175'),('1.493590960','-0.999922175'),
 ('1.041245200','0.608875824'),('1.041245200','-0.608875824'),
 ('0.798547648','0.415230381'),('0.798547648','-0.415230381'),
 ('0.648447311','0.301731971'),('0.648447311','-0.301731971'),
 ('0.548156241','0.224296888'),('0.548156241','-0.224296888'),
 ('0.477055946','0.164036187'),('0.477055946','-0.164036187'),
 ('0.421223550','0.109574467'),('0.421223550','-0.109574467'),
]
def certify():
 k=10;P,a,p=normalized(k);d=len(P)-1;eps=F(1,1000)
 centers=[z(*v) for v in CENTERS]
 assert len(centers)==d
 assert centers[0][0]==centers[1][0] and centers[0][1]==-centers[1][1]
 ratios=[]
 for ix,c in enumerate(centers):
  b=taylor(P,c)
  lhs=upper(b[0])+sum(upper(b[j])*eps**j for j in range(2,d+1))
  rhs=lower(b[1])*eps
  assert rhs>lhs,(k,ix,'ROUCHE_FAIL',float(lhs/rhs))
  ratios.append(lhs/rhs)
 pairs=list(combinations(range(d),2))
 assert all(lower(sub(centers[i],centers[j]))>2*eps for i,j in pairs)
 dom=min(lower(centers[i])-eps for i in (0,1))
 rem=max(upper(centers[i])+eps for i in range(2,d))
 assert dom>F(9) and rem<F(5) and dom>rem
 assert max(ratios)<F(1,39)
 assert centers[0][1]>eps and centers[1][1]<-eps
 seq=[F(1)]
 for m in range(1,1025):
  seq.append(sum(a[j-1]*seq[m-j] for j in range(1,min(m,d)+1)))
 changes=[m for m in range(1,len(seq)) if seq[m]*seq[m-1]<0]
 plus=sum(x>0 for x in seq);minus=sum(x<0 for x in seq)
 print('R547_EXACT_ROUCHE_PASS','k',k,'degree',d,'Catalan',C(k),'p2',p[2])
 print('disk_count',d,'disjoint_pairs',len(pairs),'radius',eps)
 print('max_rouche_ratio_lt_1/39',max(ratios)<F(1,39))
 print('dominant_y_gt',9,'other_y_lt',5,'dominant_X_gt',9*p[2],'other_X_lt',5*p[2])
 print('first_1025',plus,minus,'zero',sum(x==0 for x in seq),'adjacent_changes',len(changes),'first_changes',changes[:24])
 assert plus>0 and minus>0 and not any(x==0 for x in seq)
 return dict(k=k,d=d,plus=plus,minus=minus,changes=len(changes))
if __name__=='__main__':certify()
