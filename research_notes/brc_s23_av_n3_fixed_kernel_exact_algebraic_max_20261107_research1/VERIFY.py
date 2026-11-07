#!/usr/bin/env python3
"""Exact global algebraic maximum of PR #1777's n=3 rational reconstruction kernel.
Imports the existing exact Bernstein source in its sibling research note.
All certificate inequalities use Fraction or unbounded integers.
"""
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path

source=Path(__file__).resolve().parents[1]/'brc_s23_av_n3_adaptive_bernstein_20261107_research1'/'VERIFY.py'
base=run_path(str(source))
init,bisect,hull,residual=tuple(base[x] for x in ('init','bisect','hull','residual'))
assert tuple(base['K'][0])==(0,0,0,10**9,0,0,0,0,0,0)
assert tuple(base['K'][1])==(0,169391357,0,0,0,96190545,0,0,734418098,0)
assert tuple(base['K'][2])==(1481481,0,37451970,0,39559539,118031741,214867295,409153994,0,179453980)
assert tuple(base['K'][3])==(0,0,73659142,0,4532537,0,7354927,35290451,333009025,546153918)
U0,U1,V0,V1=F(5,32),F(6,32),F(31,32),F(1)
W=F(1899056310874087867,8000000000000000000)

def local_signs(B,den):
 signs=(-1,-1,-1,0,-1,-1,1,-1,1,-1)
 mins=[]
 for h,sign in enumerate(signs):
  vals=[sign*q for row in B[h] for q in row]
  if sign:assert min(vals)>0;mins.append(min(vals))
  else:assert all(q==0 for row in B[h] for q in row)
 dc=[3*(B[6][i][j+1]+B[8][i][j+1]-B[6][i][j]-B[8][i][j]) for i in range(4) for j in range(3)]
 assert min(dc)>0
 return min(mins),min(dc),den

def exact_partition(B,den):
 # Dyadic rectangles: every accepted leaf either is the analytic region or
 # has its exact bivariate Bernstein TV hull bounded by rational W.
 stack=[(B,den,0,F(0),F(1),F(0),F(1))]
 leaves=splits=inside_count=outside_count=maxdepth=0
 greatest=F(0)
 while stack:
  B,d,depth,x0,x1,y0,y1=stack.pop()
  inside=U0<=x0 and x1<=U1 and V0<=y0 and y1<=V1
  if inside:
   inside_count+=1;leaves+=1;maxdepth=max(maxdepth,depth)
  else:
   h=hull(B)
   if h*W.denominator<=W.numerator*d:
    outside_count+=1;leaves+=1;maxdepth=max(maxdepth,depth)
    greatest=max(greatest,F(h,d))
   else:
    assert depth<90
    l,r=bisect(B,depth%2)
    if depth%2==0:
     mid=(x0+x1)/2
     stack.extend(((r,8*d,depth+1,mid,x1,y0,y1),(l,8*d,depth+1,x0,mid,y0,y1)))
    else:
     mid=(y0+y1)/2
     stack.extend(((r,8*d,depth+1,x0,x1,mid,y1),(l,8*d,depth+1,x0,x1,y0,mid)))
    splits+=1
 assert leaves==splits+1 and inside_count==1 and greatest<W
 return leaves,splits,inside_count,outside_count,maxdepth,greatest

def local_box(B,den):
 # Explicit 5 binary subdivision decisions per axis select [5/32,6/32]x[31/32,1].
 for axis,index in ((0,5),(1,31)):
  for bit in range(4,-1,-1):
   left,right=bisect(B,axis)
   B=right if (index>>bit)&1 else left
   den*=8
 return B,den

def boundary_polynomial():
 # Lagrange interpolation of R_6(a,7/8)+R_8(a,7/8) at four rationals.
 points=[F(i,4) for i in range(4)]
 vals=[sum(residual(x,F(7,8))[j] for j in (6,8)) for x in points]
 def mul(a,b):
  c=[F(0)]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):c[i+j]+=x*y
  return c
 coefficients=[F(0)]*4
 for j,x in enumerate(points):
  basis=[F(1)];d=F(1)
  for i,y in enumerate(points):
   if i!=j:basis=mul(basis,[-y,F(1)]);d*=x-y
  for k,v in enumerate(basis):coefficients[k]+=vals[j]*v/d
 assert coefficients==[F(-112812037553,512000000000),F(570396283443,512000000000),F(187512022509,512000000000),F(-819362611823,512000000000)]
 assert sum(coefficient*F(141,250)**i for i,coefficient in enumerate(coefficients))==W
 q=lambda x:coefficients[1]+2*coefficients[2]*x+3*coefficients[3]*x*x
 assert q(F(141,250))>0 and q(F(282001,500000))<0
 assert 2*coefficients[2]+6*coefficients[3]*F(143,256)<0
 assert 2*coefficients[2]+6*coefficients[3]*F(73,128)<0
 return coefficients

def main():
 B,den=init()
 B_local,d_local=local_box(B,den)
 sign,deriv,d_local=local_signs(B_local,d_local)
 coeffs=boundary_polynomial()
 counts=exact_partition(B,den)
 print('PASS_S23_N3_FIXED_KERNEL_EXACT_ALGEBRAIC_MAX_20261107')
 print('FROZEN_SCIENCE','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
 print('ANALYTIC_RECTANGLE_A_C', F(143,256), F(73,128), F(221,256), F(7,8))
 print('LOCAL_BERNSTEIN_SIGN_POSITIVE_MIN',sign,'/',d_local)
 print('LOCAL_DERIVATIVE_V_POSITIVE_MIN',deriv,'/',d_local)
 print('EXACT_PARTITION (leaves,splits,local,exterior,maxdepth,exterior_max)',counts)
 print('BOUNDARY_CUBIC_COEFFICIENTS_LOW_TO_HIGH',coeffs)
 print('CRITICAL_ALPHA_UNIQUE_ROOT_OF','117051801689*a^2-17858287858*a-27161727783=0', 'IN', (F(141,250),F(282001,500000)))
 from decimal import Decimal, localcontext
 with localcontext() as ctx:
  ctx.prec=60
  A=Decimal(117051801689);B=Decimal(17858287858);C=Decimal(27161727783)
  alpha=(B+(B*B+4*A*C).sqrt())/(2*A)
  maximum=sum(Decimal(x.numerator)/Decimal(x.denominator)*alpha**i for i,x in enumerate(coeffs))
  print('CRITICAL_ALPHA_DECIMAL',alpha)
  print('EXACT_MAX_F_ALPHA_DECIMAL',maximum)
 print('CERTIFICATE_RESULT all lawful real (a,c), E_K(a,c)<=f(alpha), equality at (alpha,7/8)')
 print('CERTIFIED_MINIMAX_BOUND 5211/21952 <= delta_3 <= f(alpha)')
if __name__=='__main__':main()
