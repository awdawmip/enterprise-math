#!/usr/bin/env python3
"""Author-side exact interval certificate for S23 K=17, 1/3 <= s <= 2/5.
Requires only Python Fraction + isqrt; scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from fractions import Fraction as Q
from math import isqrt
A,B = Q(11,21),Q(10,21)
N,SCALE=34,10**48

def I(x): return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y):
 x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x): x=I(x);return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 x,y=I(x),I(y);p=[a*b for a in x for b in y];return min(p),max(p)
def div(x,y):
 y=I(y);assert y[0]>0;return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
 x=Q(x);assert x>0
 k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
 l,h=Q(k,SCALE),Q(k+1,SCALE)
 assert l*l<=x<h*h
 return l,h
def lnq(x):
 x=Q(x);assert x>0
 v=(x-1)/(x+1);assert abs(v)<Q(1,3)
 total=Q(0);term=v
 for j in range(N): total+=2*term/Q(2*j+1);term*=v*v
 err=2*abs(term)/(Q(2*N+1)*(1-v*v))
 return total-err,total+err
def lni(x):
 x=I(x);assert x[0]>0;return (lnq(x[0])[0],lnq(x[1])[1])
def quant(x):
 x=I(x);return (Q(x[0].numerator*SCALE//x[0].denominator,SCALE),Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE))
def info(s):
 s=Q(s);u=mul(s,sqrt_i(A*B))
 ct=neg(lni(add(1-s,mul(2,u))))
 h=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
 H=lni(A/B);J=lni((1-B*s)/(1-A*s));rho=quant(div(J,add(H,J)))
 cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
 return ct,h,cb

def checkpos(label,x):
 assert x[0]>0,(label,float(x[0]),float(x[1]))
 print(label,'GT',f'{x[0]*10**13//1}/10000000000000')

def check_linear(label,bcoef,tcoef,l,r):
 delta=Q(1,10000)
 ctl,_,cbl=info(l); ctr,_,cbr=info(r)
 _,_,cbprev=info(l-delta); ctnext,_,_=info(r+delta)
 L=div(sub(cbl,cbprev),delta);R=div(sub(ctnext,ctr),delta)
 checkpos(label+'_LEFT',sub(mul(bcoef,cbl),mul(tcoef,ctl)))
 checkpos(label+'_SLOPE',sub(mul(bcoef,L),mul(tcoef,R)))

def check_decrease(m,n,l,r):
 delta=Q(1,10000)
 _,_,cbl=info(l); _,_,cbprev=info(l-delta)
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
 third=Q(1,3);three_eight=Q(3,8);two_five=Q(2,5)
 for m,n,l,r in [(9,2,third,three_eight),(8,4,three_eight,two_five)]:
  for i in range(12):
   x=l+(r-l)*Q(i,12);y=l+(r-l)*Q(i+1,12)
   check_decrease(m,n,x,y)
 check_linear('D17_10_FIRST',17,10,third,three_eight)
 check_linear('D17_10_SECOND',17,10,three_eight,two_five)
 start_positive(9,2,third)
 end_negative(9,2,Q(334,1000))
 start_positive(8,4,three_eight)
 end_negative(8,4,Q(376,1000))
 start_positive(10,1,two_five)
 print('PASS_BRC_S23_K17_CELL_1_3_TO_2_5_TWO_SWITCHES_AND_BOUNDARY_JUMP_20261105')
if __name__=='__main__':main()
