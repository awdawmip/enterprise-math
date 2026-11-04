#!/usr/bin/env python3
"""Companion joint CM first jet. Requires d25_gauss_hasse_padiclift_20261105.py and d25_finite_euler_padic_second_digit_20261105.py in same directory."""
from math import comb
from d25_gauss_hasse_padiclift_20261105 import A,Lop,C0,add,mul,scalar,deriv,remq,ringmul,ringpow,power,truncpoly
from d25_finite_euler_padic_second_digit_20261105 import verify
def check(p):
 n=p*p;m=(p-1)//2;ell=(5*p-1)//8;d=4*ell;N=(p+1)//2
 o=verify(p);B,_=truncpoly(p)
 H=[comb(m,j)**2%n for j in range(m+1)]
 S=[((b-c)%n)//p for b,c in zip(B,mul(power(A,p,n),H,n))]
 DS=add(mul(Lop,deriv(S,n),n),mul(C0,S,n),n)
 C=add(mul(Lop,deriv(H,n),n),mul(C0,H,n),n)
 lhs=ringmul(ringpow(A,p+1,n),remq(C,n),n)
 u=pow(8*pow(9,-1,n)%n,N,n);J=o["J_at_1"]
 F=(u*J+p*o["Kvalue"])%n
 Fprime=(u*(o["Gprime"]-9*N*pow(8,-1,n)*J)+p*o["Kprime"])%n
 coefP=scalar(ringmul(ringpow(A,2,n),[1,1],n),16*pow(9,-1,n),n)
 a0=add(mul(C0,[1,1],n),scalar(Lop,d,n),n)
 coef0=ringmul(A,a0,n)
 term=add(scalar(coefP,Fprime,n),scalar(coef0,F,n),n)
 term=ringmul(ringpow([1,1],d-1,n),term,n)
 src=add(ringmul(A,remq(DS,n),n),ringmul(Lop,ringmul(deriv(A,n),scalar(ringpow([1,1],d,n),u*J,n),n),n),n)
 rhs=add(term,scalar(src,-p,n),n)
 assert lhs==remq(rhs,n),(p,lhs,remq(rhs,n))
 return p,lhs
if __name__=="__main__":
 for p in (5,29,53,101,149):print("PASS",check(p))
