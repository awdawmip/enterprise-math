#!/usr/bin/env python3
"""Proof-supporting exact rational interval certificates: S23 K=17, 1/4<=s<=1/3.
Scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
The inequalities checked are sufficient bounds; all decisive comparisons use Fraction, not floats.
"""
from fractions import Fraction as Q
from math import isqrt
N, SCALE = 34, 10**48
A, B = Q(11,21), Q(10,21)
def I(x): return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y):
 x,y=I(x),I(y);return x[0]+y[0],x[1]+y[1]
def neg(x):x=I(x);return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 x,y=I(x),I(y);p=[a*b for a in x for b in y];return min(p),max(p)
def div(x,y):
 y=I(y);assert y[0]>0
 return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
 x=Q(x);assert x>0
 k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
 l,h=Q(k,SCALE),Q(k+1,SCALE)
 assert l*l<=x<h*h
 return l,h
def lnq(x):
 x=Q(x);assert x>0
 v=(x-1)/(x+1);assert abs(v)<Q(1,3)
 term=v;total=Q(0)
 for j in range(N):
  total+=2*term/Q(2*j+1);term*=v*v
 err=2*abs(term)/(Q(2*N+1)*(1-v*v))
 return total-err,total+err
def lni(x):
 x=I(x);assert x[0]>0
 return lnq(x[0])[0],lnq(x[1])[1]
def quant(x):
 x=I(x);return (Q(x[0].numerator*SCALE//x[0].denominator,SCALE),Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE))
def info(s):
 s=Q(s);u=mul(s,sqrt_i(A*B))
 ct=neg(lni(add(1-s,mul(2,u))))
 fh=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
 H=lni(A/B);J=lni((1-B*s)/(1-A*s));rho=quant(div(J,add(H,J)))
 cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
 return ct,fh,cb
def checkpos(label,x):
 assert x[0]>0,(label,float(x[0]),float(x[1]))
 print(label,'GT',f'{x[0]*10**13//1}/10000000000000')

def check_linear(mon_label,bcoef,tcoef,l,r):
 # Convex CT,CB: lower derivative of bcoef CB-tcoef CT >= bcoef*left_sect(CB) - tcoef*right_sect(CT)
 delta=Q(1,10000)
 ctl,_,cbl=info(l);ctr,_,cbr=info(r)
 _,_,cbprev=info(l-delta);ctnext,_,_=info(r+delta)
 L=div(sub(cbl,cbprev),delta);R=div(sub(ctnext,ctr),delta)
 checkpos(mon_label+'_LEFT',sub(mul(bcoef,cbl),mul(tcoef,ctl)))
 checkpos(mon_label+'_SLOPE',sub(mul(bcoef,L),mul(tcoef,R)))

def check_decrease(m,n,l,r):
 delta=Q(1,10000)
 _,_,cbl=info(l);_,_,cbprev=info(l-delta)
 ctr,fhr,cbr=info(r);ctnext,_,cbnext=info(r+delta)
 L=div(sub(cbl,cbprev),delta)
 U=div(sub(add(mul(m,ctnext),mul(n,cbnext)),add(mul(m,ctr),mul(n,fhr))),delta)
 checkpos(f'G_{m}_{n}_DECREASE_{l}_{r}',sub(mul(17,L),U))

def start_positive(m,n,s):
 ct,h,cb=info(s)
 checkpos(f'{m}T{n}B_ABOVE_B_AT_{s}',sub(add(mul(m,ct),mul(n,h)),mul(17,cb)))
def end_negative(m,n,s):
 ct,h,cb=info(s)
 checkpos(f'{m}T{n}B_BELOW_B_AT_{s}',sub(mul(17-n,cb),mul(m,ct)))

def main():
 quarter=Q(1,4);two_seven=Q(2,7);three_ten=Q(3,10);third=Q(1,3)
 # 16CB-9CT>0 everywhere in [1/4,1/3]; separate minor segments if needed.
 for l,r in [(quarter,Q(2,7)),(Q(2,7),three_ten),(three_ten,third)]:
  check_linear('D16_9_'+str(l)+'_'+str(r),16,9,l,r)
 # 7CB-4CT>0 everywhere from 2/7; 12CB-7CT>0 from 3/10.
 for l,r in [(two_seven,three_ten),(three_ten,third)]:check_linear('D7_4_'+str(l)+'_'+str(r),7,4,l,r)
 check_linear('D12_7',12,7,three_ten,third)
 # True mixed Chernoff envelopes must decrease against 17B, using common t bounds.
 for m,n,start,end in [(8,3,quarter,two_seven),(7,5,two_seven,three_ten),(10,0,three_ten,third)]:
  steps=8
  for i in range(steps):
   l=start+(end-start)*Q(i,steps);r=start+(end-start)*Q(i+1,steps)
   check_decrease(m,n,l,r)
 # Root existence bracketing, then endpoint jumps.
 start_positive(8,3,quarter)
 end_negative(8,3,Q(251,1000))
 start_positive(7,5,two_seven)
 end_negative(7,5,Q(287,1000))
 start_positive(10,0,three_ten)
 end_negative(10,0,Q(301,1000))
 # Boundary 1/3: winner (9,2) among all combinations; >17B.
 start_positive(9,2,third)
 print('PASS_BRC_S23_K17_PHASE_S14_TO_S13_20261105')
if __name__=='__main__':main()
