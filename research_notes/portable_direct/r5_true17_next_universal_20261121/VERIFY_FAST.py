#!/usr/bin/env python3
"""Exact R5 incidence for primitive 17th roots, compiled integer cyclic-ring implementation.
Requires numpy and numba. Exact in the declared m <= 68 verification range.
"""
import numpy as np, numba as nb, json,sys
@nb.njit
def root_factor(ps):
 w=np.zeros(17,np.int64);d=np.zeros(17,np.int64);w[0]=1
 for p in ps:
  k=p%17;wn=w.copy();dn=d.copy()
  for i in range(17):
   wn[i]-=w[(i-k)%17]
   dn[i]-=d[(i-k)%17]+p*w[(i-k)%17]
  w=wn;d=dn
 return w,d
@nb.njit
def mul(a,b):
 c=np.zeros(17,np.int64)
 for i in range(17):
  if a[i]:
   for j in range(17):
    if b[j]:c[(i+j)%17]+=a[i]*b[j]
 return c
@nb.njit
def hgrp(ps,m):
 h=np.zeros((m,17),np.int64);dh=np.zeros((m,17),np.int64);h[0,0]=1
 for p in ps:
  hh=np.zeros((m,17),np.int64);dd=np.zeros((m,17),np.int64);hh[0,0]=1
  for n in range(1,m):
   for i in range(17):
    j=(i-p)%17
    hh[n,i]=h[n,i]+hh[n-1,j]
    dd[n,i]=dh[n,i]+dd[n-1,j]+p*hh[n-1,j]
  h=hh;dh=dd
 return h,dh
@nb.njit
def compute(m):
 h,dh=hgrp(np.array([216,217,218],np.int64),m)
 v,_=hgrp(np.array([219,220,221],np.int64),m)
 prod=np.zeros((m,m,17),np.int64)
 for u in range(m):
  for j in range(m):prod[u,j,:]=mul(h[u,:],v[j,:])
 P0=np.zeros(17,np.int64);DP0=np.zeros(17,np.int64)
 P1=np.zeros(17,np.int64);P2=np.zeros(17,np.int64)
 P01=np.zeros(17,np.int64);P02=np.zeros(17,np.int64)
 P12=np.zeros(17,np.int64);P012=np.zeros(17,np.int64)
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u-a):
    q=(214*a+215*b)%17;val=214*a+215*b
    for i in range(17):
     P0[i]+=h[u,(i-q)%17]
     DP0[i]+=dh[u,(i-q)%17]+val*h[u,(i-q)%17]
 for u in range(m):
  for j in range(m-u):
   for a in range(m-u-j):
    k1=(214*a)%17;k2=(215*a)%17
    for i in range(17):
     P1[i]+=prod[u,j,(i-k1)%17]
     P2[i]+=prod[u,j,(i-k2)%17]
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u):
    c0=a+b+u<m;q=(214*a+215*b)%17
    for j in range(m-u):
     c1=a+u+j<m;c2=b+u+j<m
     x01=c0 and c1;x02=c0 and c2;x12=c1 and c2;x012=c0 and c1 and c2
     if not (x01 or x02 or x12):continue
     for i in range(17):
      x=prod[u,j,(i-q)%17]
      if x01:P01[i]+=x
      if x02:P02[i]+=x
      if x12:P12[i]+=x
      if x012:P012[i]+=x
 w0,dw0=root_factor(np.array([214,215,216,217,218],np.int64))
 w1,_=root_factor(np.array([214,216,217,218,219,220],np.int64))
 w2,_=root_factor(np.array([215,216,217,218,219,220],np.int64))
 w,_=root_factor(np.array([214,215,216,217,218,219,220],np.int64))
 r0=mul(w0,P0)
 dr0=mul(w0,DP0)+mul(dw0,P0)
 bracket=mul(w1,P1)+mul(w2,P2)-mul(w,P01+P02+P12)+mul(w,P012)
 dra=dr0-221*bracket
 one=np.zeros(17,np.int64);one[0]=1
 drtotal=dra-5202*((m+16)//17)*(one-r0)
 def red(x):return x[:16]-x[16]
 return red(r0),red(dr0),red(bracket),red(dra),red(drtotal)
if __name__=='__main__':
 ms=[int(x) for x in sys.argv[1:]] or [13,14,15,16,17,30,31,32,33,34,47,48,49,50,51,64,65,66,67,68]
 rows=[]
 for m in ms:
  if m>68:raise ValueError('The published exact-int64 verification scope is m<=68')
  a=compute(m)
  rows.append(dict(m=m,R0=a[0].tolist(),DR0=a[1].tolist(),bracket=a[2].tolist(),DRA=a[3].tolist(),DR=a[4].tolist()))
 print(json.dumps({'status':'PASS','arithmetic':'exact integer cyclic ring / cyclotomic reduction (m<=68)','rows':rows}))
