#!/usr/bin/env python3
"""Independent algorithm B: original per-event inequalities at primitive 11/13 roots.
No max-of-load kernel identities. Computes R_m and DR_m in exact integer ring.
Usage: python VERIFY_DIRECT.py 11 1 7 8 9 10 11 18 19 20 21 22
       python VERIFY_DIRECT.py 13 1 9 10 11 12 13 22 23 24 25 26
Requires numpy, numba. Output JSON rows with full cyclotomic vectors.
"""
import sys,json
import numpy as np
from numba import njit

@njit
def shift(v,p,d):
 return np.array([v[(i-p)%d] for i in range(d)], dtype=np.int64)

@njit
def mul(a,b,d):
 out=np.zeros(d,np.int64)
 for i in range(d):
  for j in range(d):out[(i+j)%d]+=a[i]*b[j]
 return out

@njit
def factor(ps,d):
 f=np.zeros(d,np.int64);df=np.zeros(d,np.int64);f[0]=1
 for p in ps:
  old=f.copy();old_d=df.copy()
  for i in range(d):
   idx=(i-p)%d
   f[i]=old[i]-old[idx]
   df[i]=old_d[i]-old_d[idx]-p*old[idx]
 return f,df

@njit
def hom(ps,m,d):
 arr=np.zeros((m,d),np.int64);darr=np.zeros((m,d),np.int64);arr[0,0]=1
 for p in ps:
  v=np.zeros((m,d),np.int64);dv=np.zeros((m,d),np.int64);v[0,0]=1
  for n in range(1,m):
   for k in range(d):
    h=(k-p)%d
    v[n,k]=arr[n,k]+v[n-1,h]
    dv[n,k]=darr[n,k]+dv[n-1,h]+p*v[n-1,h]
  arr=v;darr=dv
 return arr,darr

@njit
def calculate(m,d):
 r=220 if d==11 else 221
 H,dH=hom(np.array([216,217,218],np.int64),m,d)
 V,_=hom(np.array([219,220,221],np.int64),m,d)
 P0=np.zeros(d,np.int64);DP0=np.zeros(d,np.int64)
 P1=np.zeros(d,np.int64);P2=np.zeros(d,np.int64)
 P01=np.zeros(d,np.int64);P02=np.zeros(d,np.int64)
 P12=np.zeros(d,np.int64);P012=np.zeros(d,np.int64)
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u-a):
    phase=214*a+215*b
    P0+=shift(H[u,:],phase,d)
    DP0+=shift(dH[u,:],phase,d)+phase*shift(H[u,:],phase,d)
 for u in range(m):
  for j in range(m-u):
   HJ=mul(H[u,:],V[j,:],d)
   for a in range(m-u-j):
    P1+=shift(HJ,214*a,d)
    P2+=shift(HJ,215*a,d)
 for u in range(m):
  for j in range(m-u):
   HJ=mul(H[u,:],V[j,:],d)
   for a in range(m-u):
    for b in range(m-u):
     c0=(a+b+u < m)
     c1=(a+u+j < m)
     c2=(b+u+j < m)
     n=c0+c1+c2
     if n<2:continue
     x=shift(HJ,214*a+215*b,d)
     if c0 and c1:P01+=x
     if c0 and c2:P02+=x
     if c1 and c2:P12+=x
     if n==3:P012+=x
 w0,dw0=factor(np.array([214,215,216,217,218],np.int64),d)
 w1,_=factor(np.array([p for p in [214,216,217,218,219,220,221] if p!=r],np.int64),d)
 w2,_=factor(np.array([p for p in [215,216,217,218,219,220,221] if p!=r],np.int64),d)
 w,_=factor(np.array([p for p in [214,215,216,217,218,219,220,221] if p!=r],np.int64),d)
 R0=mul(w0,P0,d)
 DR0=mul(w0,DP0,d)+mul(dw0,P0,d)
 bracket=mul(w1,P1,d)+mul(w2,P2,d)-mul(w,P01+P02+P12,d)+mul(w,P012,d)
 dr=DR0-r*bracket
 return R0[:d-1]-R0[d-1],dr[:d-1]-dr[d-1]
if __name__=='__main__':
 d=int(sys.argv[1]);ms=[int(x) for x in sys.argv[2:]]
 if d not in (11,13):raise ValueError('d=11 or d=13')
 print(json.dumps([{'m':m,'R0':calculate(m,d)[0].tolist(),'DR':calculate(m,d)[1].tolist()} for m in ms]))
