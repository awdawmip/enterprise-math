#!/usr/bin/env python3
"""Exact primitive-11/13 R5 Laurent residue, genuine event intersections.
Algorithm A: maximum-load threshold kernel convolution in Z[z]/(z^d-1),
projected to Q[z]/Phi_d. Requires numpy and numba.
Usage: python VERIFY_KERNELS.py 11 44 > KERNEL_11.json
       python VERIFY_KERNELS.py 13 52 > KERNEL_13.json
No floating point arithmetic is used. Scope d in {11,13}, M<=78.
"""
import sys, json
import numpy as np
from numba import njit

@njit
def sh(x,p,d):
 y=np.empty(d,np.int64); n=p%d
 for i in range(d):y[i]=x[(i-n)%d]
 return y

@njit
def mul(x,y,d):
 z=np.zeros(d,np.int64)
 for i in range(d):
  if x[i]:
   for j in range(d):
    if y[j]:z[(i+j)%d]+=x[i]*y[j]
 return z

@njit
def conv(a,b,M,d):
 c=np.zeros((M,d),np.int64)
 for i in range(M):
  for j in range(M-i):c[i+j,:]+=mul(a[i,:],b[j,:],d)
 return c

@njit
def pref(a,d):
 b=np.empty_like(a);s=np.zeros(d,np.int64)
 for i in range(a.shape[0]):s+=a[i,:];b[i,:]=s
 return b

@njit
def hom(prices,M,d):
 h=np.zeros((M,d),np.int64);dh=np.zeros((M,d),np.int64);h[0,0]=1
 for p in prices:
  a=np.zeros((M,d),np.int64);b=np.zeros((M,d),np.int64);a[0,0]=1
  for i in range(1,M):
   for k in range(d):
    j=(k-p)%d
    a[i,k]=h[i,k]+a[i-1,j]
    b[i,k]=dh[i,k]+b[i-1,j]+p*a[i-1,j]
  h=a;dh=b
 return h,dh

@njit
def factor(prices,d):
 a=np.zeros(d,np.int64);da=np.zeros(d,np.int64);a[0]=1
 for p in prices:
  old=a.copy();oldd=da.copy()
  for k in range(d):
   j=(k-p)%d
   a[k]=old[k]-old[j]
   da[k]=oldd[k]-oldd[j]-p*old[j]
 return a,da

@njit
def exact(M,d,r):
 H,dH=hom(np.array([216,217,218],np.int64),M,d)
 V,_=hom(np.array([219,220,221],np.int64),M,d)
 X=np.zeros((M,d),np.int64);Y=np.zeros((M,d),np.int64)
 for n in range(M):X[n,(214*n)%d]=1;Y[n,(215*n)%d]=1
 M01=np.zeros((M,d),np.int64);M02=np.zeros((M,d),np.int64);M12=np.zeros((M,d),np.int64)
 for s in range(M):
  for j in range(s+1):
   M01[s,:]+=sh(V[j,:],215*s,d)
   M02[s,:]+=sh(V[j,:],214*s,d)
  for b in range(s):
   M01[s,:]+=sh(V[s,:],215*b,d)
   M02[s,:]+=sh(V[s,:],214*b,d)
  for b in range(s+1):M12[s,(214*s+215*b)%d]+=1
  for a in range(s):M12[s,(214*a+215*s)%d]+=1
 T=np.zeros((M,d),np.int64)
 for a in range(M):
  for b in range(M):
   for j in range(M):
    g=max(a+b,a+j,b+j)
    if g<M:T[g,:]+=sh(V[j,:],214*a+215*b,d)
 p1=pref(conv(conv(H,X,M,d),V,M,d),d)
 p2=pref(conv(conv(H,Y,M,d),V,M,d),d)
 p01=pref(conv(conv(H,X,M,d),M01,M,d),d)
 p02=pref(conv(conv(H,Y,M,d),M02,M,d),d)
 p12=pref(conv(conv(H,V,M,d),M12,M,d),d)
 p012=pref(conv(H,T,M,d),d)
 w0,dw0=factor(np.array([214,215,216,217,218],np.int64),d)
 w1,_=factor(np.array([p for p in [214,216,217,218,219,220,221] if p!=r],np.int64),d)
 w2,_=factor(np.array([p for p in [215,216,217,218,219,220,221] if p!=r],np.int64),d)
 w,_=factor(np.array([p for p in [214,215,216,217,218,219,220,221] if p!=r],np.int64),d)
 p0=np.zeros((M,d),np.int64);dp0=np.zeros((M,d),np.int64)
 for u in range(M):
  for a in range(M-u):
   for b in range(M-u-a):
    q=214*a+215*b
    p0[u+a+b,:]+=sh(H[u,:],q,d)
    dp0[u+a+b,:]+=sh(dH[u,:],q,d)+q*sh(H[u,:],q,d)
 p0=pref(p0,d);dp0=pref(dp0,d)
 leading=np.zeros((M,d-1),np.int64);D=np.zeros((M,d-1),np.int64)
 for k in range(M):
  R0=mul(w0,p0[k,:],d)
  DR0=mul(w0,dp0[k,:],d)+mul(dw0,p0[k,:],d)
  bk=mul(w1,p1[k,:],d)+mul(w2,p2[k,:],d)-mul(w,p01[k,:]+p02[k,:]+p12[k,:],d)+mul(w,p012[k,:],d)
  dR=DR0-r*bk
  leading[k,:]=R0[:d-1]-R0[d-1]
  D[k,:]=dR[:d-1]-dR[d-1]
 return leading,D

def main():
 d=int(sys.argv[1]) if len(sys.argv)>1 else 11
 M=int(sys.argv[2]) if len(sys.argv)>2 else 4*d
 if d not in (11,13):raise ValueError('Implemented for d=11 or 13 only')
 if not 1<=M<=78:raise ValueError('Conservative int64 verification range M=1..78')
 r=220 if d==11 else 221
 r0,dr=exact(M,d,r)
 rows=[{'m':i+1,'R0':r0[i].tolist(),'DR':dr[i].tolist()} for i in range(M)]
 print(json.dumps({'d':d,'M':M,'root':f'primitive {d}th',
  'R0_nonzero_residues_first_cycle':[i+1 for i in range(d) if np.any(r0[i])],
  'rows':rows}))
if __name__=='__main__':main()
