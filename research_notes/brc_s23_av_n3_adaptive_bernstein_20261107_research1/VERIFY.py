#!/usr/bin/env python3
"""Exact n=3 S23 bivariate Bernstein certificate, 2026-11-07.
Frozen source 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Fixed near-optimal symmetric kernel from PR #1777 @72c42391354a2decdacca583134e8f1f97130dc0.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, lcm
M=10**9
H=sorted(h for h in product(range(4),repeat=3) if sum(h)==3)
MULT=[factorial(3)//(factorial(h[0])*factorial(h[1])*factorial(h[2])) for h in H]
K=[[0,0,0,1000000000,0,0,0,0,0,0],
   [0,169391357,0,0,0,96190545,0,0,734418098,0],
   [1481481,0,37451970,0,39559539,118031741,214867295,409153994,0,179453980],
   [0,0,73659142,0,4532537,0,7354927,35290451,333009025,546153918]]
assert len(H)==10 and sum(MULT)==27 and all(len(r)==10 and min(r)>=0 and sum(r)==M for r in K)

def residual(a,c):
 z=(1-a)*c;p=(a,z,(1-a)*(1-c))
 w=[comb(3,k)*z**(3-k)*(1-z)**k for k in range(4)]
 return [MULT[j]*p[0]**h[0]*p[1]**h[1]*p[2]**h[2]-sum(w[k]*K[k][j] for k in range(4))/M for j,h in enumerate(H)]

def init():
 nodes=[F(1,2)+F(i,8) for i in range(4)]
 U=[[F(1),F(0),F(0),F(0)],[-F(5,6),F(3),-F(3,2),F(1,3)],
    [F(1,3),-F(3,2),F(3),-F(5,6)],[F(0),F(0),F(0),F(1)]]
 val=[[residual(a,c) for c in nodes] for a in nodes]
 cp=[[[sum(U[i][p]*U[j][q]*val[p][q][h] for p in range(4) for q in range(4)) for j in range(4)] for i in range(4)] for h in range(10)]
 den=lcm(*(v.denominator for h in cp for row in h for v in row))
 B=[[[int(v*den) for v in row] for row in h] for h in cp]
 for a,c in [(F(11,16),F(13,16)),(F(17,32),F(19,32)),(F(5,8),F(3,4))]:
  u=(a-F(1,2))/F(3,8);v=(c-F(1,2))/F(3,8)
  bu=[comb(3,i)*u**i*(1-u)**(3-i) for i in range(4)]
  bv=[comb(3,j)*v**j*(1-v)**(3-j) for j in range(4)]
  assert [sum(F(B[h][i][j],den)*bu[i]*bv[j] for i in range(4) for j in range(4)) for h in range(10)]==residual(a,c)
 return B,den

def hull(B):return max(sum(max(0,B[h][i][j]) for h in range(10)) for i in range(4) for j in range(4))

def bisect(B,axis):
 L=[[[0]*4 for _ in range(4)] for _ in range(10)];R=[[[0]*4 for _ in range(4)] for _ in range(10)]
 for h in range(10):
  for v in range(4):
   p=[B[h][i][v] if axis==0 else B[h][v][i] for i in range(4)]
   lo=[8*p[0],4*(p[0]+p[1]),2*(p[0]+2*p[1]+p[2]),p[0]+3*p[1]+3*p[2]+p[3]]
   hi=[lo[3],2*(p[1]+2*p[2]+p[3]),4*(p[2]+p[3]),8*p[3]]
   for i in range(4):
    if axis==0:L[h][i][v]=lo[i];R[h][i][v]=hi[i]
    else:L[h][v][i]=lo[i];R[h][v][i]=hi[i]
 return L,R

def main():
 T=F(23738203887,10**11);B,den=init();stack=[(B,den,0)]
 leaves=splits=maxdepth=0;maxleaf=F(0)
 while stack:
  block,d,depth=stack.pop();num=hull(block)
  if num*T.denominator<=T.numerator*d:
   leaves+=1;maxleaf=max(maxleaf,F(num,d));maxdepth=max(maxdepth,depth)
  else:
   assert depth<90
   l,r=bisect(block,depth%2);stack.extend([(r,8*d,depth+1),(l,8*d,depth+1)]);splits+=1
 witness=sum(max(F(0),v) for v in residual(F(141,250),F(7,8)))
 lower=F(5211,21952)
 old=F(8352195663312870519501,35184372088832000000000)
 assert leaves==splits+1 and lower<=witness<=maxleaf<=T<old
 assert witness==F(1899056310874087867,8000000000000000000)
 print('PASS_S23_N3_ADAPTIVE_EXACT_BERNSTEIN_20261107')
 print('FULL_ORDERED_OUTPUTS 27; HISTOGRAM_ORBITS 10; INPUT_ROWS 4')
 print('ADAPTIVE leaves',leaves,'splits',splits,'maxdepth',maxdepth)
 print('MAX_ACCEPTED_HULL_APPROX',format(float(maxleaf),'.16f'))
 print('CERTIFIED_ALL_REAL_UPPER',T,'DECIMAL',format(float(T),'.11f'))
 print('FIXED_KERNEL_RATIONAL_WITNESS',witness,'DECIMAL',format(float(witness),'.16f'))
 print('MINIMAX_INTERVAL',lower,'<=delta_3<=',T)
 print('MINIMAX_GAP',T-lower,'DECIMAL',format(float(T-lower),'.16f'))
 print('PREVIOUS_CERTIFIED_UPPER',format(float(old),'.16f'))
 print('All certificate comparisons: unbounded integers/Fraction; all real (a,c) in [1/2,7/8]^2')
if __name__=='__main__':main()
