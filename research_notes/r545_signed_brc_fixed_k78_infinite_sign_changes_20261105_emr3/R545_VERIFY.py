#!/usr/bin/env python3
"""Exact rational complex-disk certificate for R462 signed-BRC k=7 and k=8.
The only role of approximate root discovery was to select the fixed rational centers
below. All proof-critical checks in this executable use integer/Fraction arithmetic.
"""
from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations

def z(a=0,b=0): return F(a),F(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]*a[0]+a[1]*a[1]
def lower(a,S=10**8):
 q=norm2(a)
 return F(isqrt(q.numerator*S*S//q.denominator),S)
def upper(a,S=10**8):
 q=norm2(a); b=lower(a,S)
 return b if b*b==q else b+F(1,S)
def catalan(k):return comb(2*k,k)//(k+1)
def coeff(k,t):
 r=2*k+1
 if not 2<=t<=r:return 0
 return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*catalan(k-q) for q in range(min((t-1)//2,k)+1))
def get_P(k):
 d=2*k-1; c=catalan(k)
 p={t:F(coeff(k,t),c) for t in range(2,2*k+2)}
 # Use y = X/p_2. Q(y) = P(p_2*y)/p_2**d
 a=[(-1)**(j-1)*p[j+2]/p[2] for j in range(1,d+1)]
 return [F(1)]+[-v for v in a],a,p

def taylor(P,c):
 out=[z(0)]
 for value in P:
  nxt=[z(0)]*(len(out)+1)
  for j,b in enumerate(out):
   nxt[j]=add(nxt[j],mul(c,b));nxt[j+1]=add(nxt[j+1],b)
  nxt[0]=add(nxt[0],z(value))
  out=nxt
 assert out[-1]==z(0)
 return out[:-1]

CENTERS={
 7:[('3.177694','3.914665'),('3.177694','-3.914665'),
 ('3.416839','0'),('1.369903','1.106593'),('1.369903','-1.106593'),
 ('0.860594','0.558719'),('0.860594','-0.558719'),
 ('0.638895','0.339317'),('0.638895','-0.339317'),
 ('0.513530','0.221335'),('0.513530','-0.221335'),
 ('0.430964','0.137353'),('0.430964','-0.137353')],
 8:[('4.036005','5.081137'),('4.036005','-5.081137'),
 ('3.822386','0'),('1.725441','1.382801'),('1.725441','-1.382801'),
 ('1.045791','0.694653'),('1.045791','-0.694653'),
 ('0.757781','0.424162'),('0.757781','-0.424162'),
 ('0.598650','0.285452'),('0.598650','-0.285452'),
 ('0.498072','0.196595'),('0.498072','-0.196595'),
 ('0.427067','0.126002'),('0.427067','-0.126002')]
}

def certify(k):
 P,a,p=get_P(k); d=len(P)-1;centers=[z(*v) for v in CENTERS[k]]
 eps=F(1,1000)
 assert len(centers)==d
 assert centers[0][0]==centers[1][0] and centers[0][1]==-centers[1][1]
 ratio=[]
 for ix,c in enumerate(centers):
  b=taylor(P,c)
  # Q(c+w) = b0 + b1*w + ...; strict first-order Rouche
  lhs=upper(b[0])+sum(upper(b[j])*eps**j for j in range(2,d+1))
  rhs=lower(b[1])*eps
  assert rhs>lhs,(k,ix,'rouche fail',lhs,rhs)
  ratio.append(lhs/rhs)
 pairs=list(combinations(range(d),2))
 assert all(lower(sub(centers[i],centers[j]))>2*eps for i,j in pairs)
 dom=min(lower(centers[i])-eps for i in (0,1))
 rem=max(upper(centers[i])+eps for i in range(2,d))
 assert dom>rem and centers[0][1]>eps and centers[1][1]<-eps
 if k==7:assert dom>5 and rem<F(7,2)
 if k==8:assert dom>F(64,10) and rem<F(39,10)
 assert max(ratio)<F(1,50)
 # recurrence on y-scale: f_m / p2^m obeys a_j=(-1)^(j-1)*p_(j+2)/p2
 seq=[F(1)]
 for m in range(1,513): seq.append(sum(a[j-1]*seq[m-j] for j in range(1,min(m,d)+1)))
 ch=[m for m in range(1,len(seq)) if seq[m]*seq[m-1]<0]
 assert ch and seq[0]>0
 print('R545_K_CERT_PASS',k,'degree',d,'catalan',catalan(k),'p2',p[2])
 print('rational_disk_radius',eps,'disk_count',d,'disjoint_pairs',len(pairs),'max_rouche_ratio_bound_lt_1/50')
 print('dominant_y_lower',dom,'other_y_upper',rem)
 print('recurrence_exact_first_513_signchanges',len(ch),'first',ch[:16])
 print('signs_first_48',''.join('+' if v>0 else '-' if v<0 else '0' for v in seq[:48]))
 return ch
if __name__=='__main__':
 for k in (7,8):certify(k)
 print('R545_EXACT_RATIONAL_CERT_PASS')
