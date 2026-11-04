#!/usr/bin/env python3
"""Companion joint CM first jet. Requires d25_gauss_hasse_padiclift_20261105.py and d25_finite_euler_padic_second_digit_20261105.py in same directory."""
from math import comb
import d25_gauss_hasse_padiclift_20261105 as base
from d25_finite_euler_padic_second_digit_20261105 import verify
A=base.A
Lop=getattr(base,"Lop",None) or base.L
C0=base.C0
add=base.add
mul=base.mul
scalar=getattr(base,"scalar",None) or base.scl
deriv=getattr(base,"deriv",None) or base.der
remq=getattr(base,"remq",None) or base.rem
ringmul=getattr(base,"ringmul",None) or base.rm
ringpow=getattr(base,"ringpow",None) or base.rp
power=getattr(base,"power",None) or base.pw

def truncpoly(p):
 ell=(5*p-1)//8;n=p*p;d=4*ell
 f=[1]
 for k in range(1,ell+1):f.append(f[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,n)%n)
 B=[0]*(d+1)
 for k in range(ell+1):
  ff=f[k]*pow(16,k,n)%n
  for r in range(2*k+1):
   w=ff*comb(2*k,r)*(-1)**r
   for j in range(4*(ell-k)+1):B[k+r+j]=(B[k+r+j]+w*comb(4*(ell-k),j))%n
 return B,f
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
