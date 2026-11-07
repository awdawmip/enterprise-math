#!/usr/bin/env python3
"""Rigorous rational endpoint certificate: K=17, 1/5<=s<=1/4, S23 typed T/B."""
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
def info(s):
 s=Q(s);u=mul(s,sqrt_i(A*B))
 ct=neg(lni(add(1-s,mul(2,u))))
 fh=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
 H=lni(A/B);J=lni((1-B*s)/(1-A*s));rho=div(J,add(H,J))
 cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
 return ct,fh,cb
def positive(label,x):
 assert x[0]>0,(label,float(x[0]))
 print(label,'GT',f'{x[0]*10**12//1}/1000000000000')
def check_decrease(m,n,l,r):
 delta=Q(1,10000)
 ctl,fhl,cbl=info(l); _,_,cb_prev=info(l-delta)
 ctr,fhr,cbr=info(r);ct_next,_,cb_next=info(r+delta)
 # Convex functions: CB right-derivative >= left secant; C(m,n) right-derivative <= right secant.
 lower=div(sub(cbl,cb_prev),delta)
 upper=div(sub(add(mul(m,ct_next),mul(n,cb_next)),
               add(mul(m,ctr),mul(n,fhr))),delta)
 positive(f'G_{m}_{n}_DECREASE_{l}_{r}',sub(mul(17,lower),upper))
def main():
 l=Q(1,5); u=Q(1,4); z=Q(2,9); d=Q(1,10000)
 ct0,fh0,cb0=info(l); ct1,fh1,cb1=info(u)
 # Competitor exclusion for m=6,7,8 via 11 CB - 6 CT >0 on the full closed interval.
 _,_,cb_left=info(l-d);ct_right,_,_=info(u+d)
 L=div(sub(cb0,cb_left),d);R=div(sub(ct_right,ct1),d)
 positive('11CB_MINUS_6CT_LEFT',sub(mul(11,cb0),mul(6,ct0)))
 positive('11CB_MINUS_6CT_SECANT',sub(mul(11,L),mul(6,R)))
 # monotonicity of true common-t envelopes of (5,8), (9,1) vs all-B
 check_decrease(5,8,l,Q(41,200))
 check_decrease(5,8,Q(41,200),z)
 check_decrease(5,8,z,u)
 check_decrease(9,1,z,u)
 ct_a,fh_a,cb_a=info(Q(1,5))
 ct_b,fh_b,cb_b=info(Q(20015,100000))
 positive('5T8B_ABOVE_B_AT_1_5',sub(add(mul(5,ct_a),mul(8,fh_a)),mul(17,cb_a)))
 positive('5T8B_BELOW_B_AT_20015_100000',sub(mul(9,cb_b),mul(5,ct_b)))
 for lab,s,positive_side in [('9T1B_ABOVE_B_AT_2_9',z,True),('9T1B_BELOW_B_AT_2224_10000',Q(2224,10000),False)]:
  ct,fh,cb=info(s)
  positive(lab,sub(add(mul(9,ct),fh),mul(17,cb)) if positive_side else sub(mul(16,cb),mul(9,ct)))
 # at 1/4 newly feasible (8,3), (4,10); compare using rigorous bounds
 positive('8T3B_ABOVE_B_AT_1_4',sub(add(mul(8,ct1),mul(3,fh1)),mul(17,cb1)))
 positive('8T3B_ABOVE_4T10B_AT_1_4',sub(add(mul(8,ct1),mul(3,fh1)),add(mul(4,ct1),mul(10,cb1))))
 positive('9T1B_BELOW_B_AT_1_4',sub(mul(16,cb1),mul(9,ct1)))
 print('PASS_S23_K17_CELL_1_5_TO_1_4_TWO_SWITCHES_AND_BOUNDARY_JUMP_20261105')
if __name__=='__main__':main()
