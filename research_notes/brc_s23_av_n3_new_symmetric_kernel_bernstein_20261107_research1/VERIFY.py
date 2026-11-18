#!/usr/bin/env python3
"""Exact, standalone rational certificate for a symmetric S23 n=3 kernel.
Scientific input enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
The same unknown (a,c) applies to all three trials; outputs are 27 ordered labels.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, lcm

M=100_000_000_000
H=sorted(h for h in product(range(4),repeat=3) if sum(h)==3)
MULT=[factorial(3)//(factorial(h[0])*factorial(h[1])*factorial(h[2])) for h in H]
K=[
 [0,0,0,100000000000,0,0,0,0,0,0],
 [0,0,0,0,0,0,1720234471,0,98279765529,0],
 [148148148,444444444,11111111111,0,22222222222,12444444444,16550113883,31952904549,0,5126611199],
 [0,0,0,0,0,0,5098696849,2445569945,32400594768,60055138438],
]
assert len(H)==10 and sum(MULT)==27 and all(len(row)==10 and min(row)>=0 and sum(row)==M for row in K)
# Conservative target strictly below predecessor exact algebraic maximum ~0.237382038860788688...
T=F(2373817396,10000000000)
# predecessor strict rational witness W; old exact max > W
OLD_W=F(1899056310874087867,8000000000000000000)
assert T < OLD_W

def residual(a,c):
 z=(1-a)*c
 p=(a,z,(1-a)*(1-c))
 w=[comb(3,k)*z**(3-k)*(1-z)**k for k in range(4)]
 return [MULT[j]*p[0]**h[0]*p[1]**h[1]*p[2]**h[2]-sum(w[k]*K[k][j] for k in range(4))/M for j,h in enumerate(H)]

def init():
 # a and c evaluated at u,v=0,1/3,2/3,1; inverse Bernstein interpolation matrix
 nodes=[F(1,2)+F(i,8) for i in range(4)]
 U=[[F(1),F(0),F(0),F(0)],[-F(5,6),F(3),-F(3,2),F(1,3)],
    [F(1,3),-F(3,2),F(3),-F(5,6)],[F(0),F(0),F(0),F(1)]]
 val=[[residual(a,c) for c in nodes] for a in nodes]
 cp=[[[sum(U[i][p]*U[j][q]*val[p][q][h] for p in range(4) for q in range(4)) for j in range(4)] for i in range(4)] for h in range(10)]
 den=lcm(*(v.denominator for h in cp for row in h for v in row))
 B=[[[int(v*den) for v in row] for row in h] for h in cp]
 # Check interpolation on non-grid rationals; arithmetic is exact.
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
 B,den=init();stack=[(B,den,0)];splits=leaves=maxdepth=0;maxleaf=F(0)
 while stack:
  block,d,depth=stack.pop();num=hull(block)
  if num*T.denominator<=T.numerator*d:
   leaves+=1;maxdepth=max(maxdepth,depth);maxleaf=max(maxleaf,F(num,d))
  else:
   assert depth<100 and splits<50000,('BUDGET',splits,depth,float(F(num,d)))
   left,right=bisect(block,depth%2);stack.extend([(right,8*d,depth+1),(left,8*d,depth+1)]);splits+=1
 assert leaves==splits+1 and maxleaf<=T<OLD_W
 assert F(5211,21952)<T
 print('PASS_S23_N3_NEW_SYMMETRIC_KERNEL_GLOBAL_BERNSTEIN')
 print('lawful real a,c in [1/2,7/8]; output orbit multiplicities',MULT,'total',sum(MULT))
 print('K denominator',M,'row sums',[sum(r) for r in K])
 print('Bernstein leaves',leaves,'splits',splits,'max_depth',maxdepth)
 print('worst certified Bernstein hull',maxleaf,'decimal',format(float(maxleaf),'.16f'))
 print('NEW_UNIFORM_UPPER',T,'decimal',format(float(T),'.16f'))
 print('OLD_FIXED_KERNEL_RATIONAL_WITNESS',OLD_W,'decimal',format(float(OLD_W),'.16f'))
 print('MINIMAX_LOWER',F(5211,21952),'remaining_gap',T-F(5211,21952))
if __name__=='__main__':main()
