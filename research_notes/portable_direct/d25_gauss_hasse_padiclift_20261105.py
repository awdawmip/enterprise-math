#!/usr/bin/env python3
"""Exact Gauss-Hasse p^2 carry and first-jet certificate; auxiliary classical ring."""
from math import comb
Q=[1,-140,294,-140,1]; A=[1,-6,1]; L=[0,16,0,-16]; C0=[1,2,-7]
def add(a,b,n):
 r=[0]*max(len(a),len(b))
 for i,v in enumerate(a):r[i]=(r[i]+v)%n
 for i,v in enumerate(b):r[i]=(r[i]+v)%n
 return r
def mul(a,b,n):
 r=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  if v%n:
   for j,w in enumerate(b):r[i+j]=(r[i+j]+v*w)%n
 return r
def scl(a,c,n):return [c*x%n for x in a]
def sub(a,b,n):return add(a,scl(b,-1,n),n)
def der(a,n):return [i*a[i]%n for i in range(1,len(a))] or [0]
def pw(a,k,n):
 r=[1]
 while k:
  if k&1:r=mul(r,a,n)
  k//=2
  if k:a=mul(a,a,n)
 return r
def rem(a,n):
 a=[x%n for x in a]
 for i in range(len(a)-1,3,-1):
  z=a[i]
  if z:
   for j in range(4):a[i-4+j]=(a[i-4+j]-z*Q[j])%n
 return (a[:4]+[0]*4)[:4]
def rm(a,b,n):return rem(mul(a,b,n),n)
def rp(a,k,n):
 r=[1]
 while k:
  if k&1:r=rm(r,a,n)
  k//=2
  if k:a=rm(a,a,n)
 return rem(r,n)
def run(p):
 n=p*p;m=(p-1)//2;e=(5*p-1)//8;d=4*e
 f=[1]
 for k in range(1,e+1):f.append(f[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,n)%n)
 B=[0]*(d+1)
 for k in range(e+1):
  ff=f[k]*pow(16,k,n)%n
  for r in range(2*k+1):
   w=ff*comb(2*k,r)*(-1)**r
   for j in range(4*(e-k)+1):B[k+r+j]=(B[k+r+j]+w*comb(4*(e-k),j))%n
 H=[comb(m,j)**2%n for j in range(m+1)]
 ah=mul(pw(A,p,n),H,n)
 assert len(B)==len(ah)==d+1
 D=sub(B,ah,n);assert all(x%p==0 for x in D)
 S=[x//p for x in D]
 assert S==S[::-1] and S[0]==0 and S[1]==9%p
 dS=add(mul(L,der(S,p),p),mul(C0,S,p),p)
 dS=(dS+[0]*(d+3-len(dS)))[:d+3]
 assert dS==dS[::-1]
 C=add(mul(L,der(H,n),n),mul(C0,H,n),n)
 DB=add(mul(L,der(B,n),n),mul(C0,B,n),n)
 DS=add(mul(L,der(S,n),n),mul(C0,S,n),n)
 left=mul(pw(A,p+1,n),C,n)
 right=sub(mul(A,DB,n),scl(add(mul(A,DS,n),mul(L,mul(der(A,n),B,n),n),n),p,n),n)
 z=max(len(left),len(right))
 assert left+[0]*(z-len(left))==right+[0]*(z-len(right))
 if p%24==5:
  R=rem(C,n);assert all(x%p==0 for x in R)
  inv9=pow(9,-1,n)
  fv=sum(f[k]*pow(inv9,k,n) for k in range(e+1))%n
  fp=sum(k*f[k]*pow(inv9,k-1,n) for k in range(1,e+1))%n
  Bf=rp([1,1],d,n)
  DBf=add(scl(rm(Bf,A,n),16*fp*inv9,n),
           scl(rm(rp([1,1],d-1,n),add(scl(L,d,n),mul(C0,[1,1],n),n),n),fv,n),n)
  fiber=sub(rm(A,DBf,n),scl(add(rm(A,rem(DS,n),n),
         rm(L,rm(der(A,n),rm(scl(Bf,fv,n),n),n),n),n),p,n),n)
  assert rem(left,n)==rem(fiber,n)
  return p,tuple(x//p for x in R)
 return p,None
if __name__=="__main__":
 for p in (5,13,29,37,53,61,101,149,173,197):print("PASS",run(p))
