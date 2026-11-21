#!/usr/bin/env python3
"""Independent threshold-series kernel verification for genuine R5 incidence at zeta_17.
Uses maxima of original loads and one convolution generating function for all thresholds.
No per-threshold intersection-mask enumeration. Exact int64 for 1 <= m <= 68.
Requires numpy and numba.
"""
import json,sys
import numpy as np
from numba import njit
@njit
def sh(x,p):
 n=p%17;y=np.empty(17,np.int64)
 for i in range(17):y[i]=x[(i-n)%17]
 return y
@njit
def mul(x,y):
 z=np.zeros(17,np.int64)
 for i in range(17):
  for j in range(17):z[(i+j)%17]+=x[i]*y[j]
 return z
@njit
def poly_conv(a,b,m):
 c=np.zeros((m,17),np.int64)
 for i in range(m):
  for j in range(m-i):c[i+j,:]+=mul(a[i,:],b[j,:])
 return c
@njit
def pref(a):
 b=np.empty_like(a);s=np.zeros(17,np.int64)
 for i in range(a.shape[0]):
  s+=a[i,:];b[i,:]=s
 return b
@njit
def hom(prices,m):
 h=np.zeros((m,17),np.int64);dh=np.zeros((m,17),np.int64);h[0,0]=1
 for p in prices:
  a=np.zeros((m,17),np.int64);b=np.zeros((m,17),np.int64);a[0,0]=1
  for i in range(1,m):
   for k in range(17):
    j=(k-p)%17
    a[i,k]=h[i,k]+a[i-1,j]
    b[i,k]=dh[i,k]+b[i-1,j]+p*a[i-1,j]
  h=a;dh=b
 return h,dh
@njit
def factor(prices):
 a=np.zeros(17,np.int64);da=np.zeros(17,np.int64);a[0]=1
 for p in prices:
  old=a.copy();oldd=da.copy()
  for k in range(17):
   j=(k-p)%17
   a[k]=old[k]-old[j]
   da[k]=oldd[k]-oldd[j]-p*old[j]
 return a,da
@njit
def exact(m):
 # Indexed by t^n. The event cutoff P_m is coefficient t^(m-1).
 H,dH=hom(np.array([216,217,218],np.int64),m)
 V,_=hom(np.array([219,220,221],np.int64),m)
 X=np.zeros((m,17),np.int64);Y=np.zeros((m,17),np.int64)
 for n in range(m):X[n,(214*n)%17]=1;Y[n,(215*n)%17]=1
 M01=np.zeros((m,17),np.int64);M02=np.zeros((m,17),np.int64)
 M12=np.zeros((m,17),np.int64)
 # max(b,j), max(a,j), max(a,b). Tie = first case only.
 for s in range(m):
  for j in range(s+1):
   M01[s,:]+=sh(V[j,:],215*s)
   M02[s,:]+=sh(V[j,:],214*s)
  for b in range(s):
   M01[s,:]+=sh(V[s,:],215*b)
   M02[s,:]+=sh(V[s,:],214*b)
  for b in range(s+1):M12[s,(214*s+215*b)%17]+=1
  for a in range(s):M12[s,(214*a+215*s)%17]+=1
 # Genuine triangle: max(a+b,a+j,b+j), no union-cardinality cutoff.
 T=np.zeros((m,17),np.int64)
 for a in range(m):
  for b in range(m):
   for j in range(m):
    g=max(a+b,a+j,b+j)
    if g<m:T[g,:]+=sh(V[j,:],214*a+215*b)
 p1=pref(poly_conv(poly_conv(H,X,m),V,m))
 p2=pref(poly_conv(poly_conv(H,Y,m),V,m))
 p01=pref(poly_conv(poly_conv(H,X,m),M01,m))
 p02=pref(poly_conv(poly_conv(H,Y,m),M02,m))
 p12=pref(poly_conv(poly_conv(H,V,m),M12,m))
 p012=pref(poly_conv(H,T,m))
 W0,DW0=factor(np.array([214,215,216,217,218],np.int64))
 W1,_=factor(np.array([214,216,217,218,219,220],np.int64))
 W2,_=factor(np.array([215,216,217,218,219,220],np.int64))
 W,_=factor(np.array([214,215,216,217,218,219,220],np.int64))
 p0=np.zeros((m,17),np.int64);dp0=np.zeros((m,17),np.int64)
 for u in range(m):
  for a in range(m-u):
   for b in range(m-u-a):
    q=214*a+215*b
    p0[u+a+b,:]+=sh(H[u,:],q)
    dp0[u+a+b,:]+=sh(dH[u,:],q)+q*sh(H[u,:],q)
 p0=pref(p0);dp0=pref(dp0)
 result=np.zeros((m,16),np.int64);bracket=np.zeros((m,16),np.int64)
 d0=np.zeros((m,16),np.int64)
 for k in range(m):
  r0=mul(W0,p0[k,:])
  dr0=mul(W0,dp0[k,:])+mul(DW0,p0[k,:])
  bk=mul(W1,p1[k,:])+mul(W2,p2[k,:])-mul(W,p01[k,:]+p02[k,:]+p12[k,:])+mul(W,p012[k,:])
  one=np.zeros(17,np.int64);one[0]=1
  dr=dr0-221*bk-5202*((k+17)//17)*(one-r0)
  result[k,:]=dr[:16]-dr[16]
  bracket[k,:]=bk[:16]-bk[16]
  d0[k,:]=dr0[:16]-dr0[16]
 return result,bracket,d0
if __name__=='__main__':
 m=int(sys.argv[1]) if len(sys.argv)>1 else 68
 if m<1 or m>68:raise ValueError('Exact int64 verification range: 1..68')
 d,b,d0=exact(m)
 print(json.dumps({'method':'independent maximum-load generating-kernel convolution',
   'max_m':m,
   'rows':[{'m':k+1,'DR':d[k].tolist(),'bracket':b[k].tolist(),'DR0':d0[k].tolist()} for k in range(m)]}))
