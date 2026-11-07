#!/usr/bin/env python3
"""Exact polynomial Cartier obstruction and unique z^p integration constant."""

def mod_inverses(p):
 inv=[0]*p;inv[1]=1
 for n in range(2,p):inv[n]=(-(p//n)*inv[p%n])%p
 return inv
from math import comb

def polysum(a,b,p):
 c=[0]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]=(c[i]+v)%p
 for i,v in enumerate(b):c[i]=(c[i]+v)%p
 return c

def prod(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  if v:
   for j,w in enumerate(b):c[i+j]=(c[i+j]+v*w)%p
 return c

def poly_h(p,r):return [((-1)**i)*comb(r,i)%p for i in range(r+1)]
def test(p,which):
 inv=mod_inverses(p)
 if which=='A':
  m=(p-1)//6;h=2*m+1;d=m;jmax=4*m-1;r=(p+1)//2
  q=[comb(m,i)*comb(2*m,i)%p for i in range(d+1)]
  v=inv[18%p]*inv[m+1]*inv[2*m+1]%p
  c=(-1)**m*pow(comb(2*m,m),-1,p)%p
  lam=c*inv[18%p]%p;mu=-inv[18%p]%p
  args=(m+1,2*m+1)
 else:
  k=(p-3)//8 if p%8==3 else (p-5)//8
  h=3*k+2;d=k;jmax=p-3*k-3
  r=(p+1)//2 if p%8==3 else (p+3)//2
  q=[comb(k,i)*comb(3*k+1,i)%p for i in range(d+1)]
  v=3*inv[64%p]*inv[k+1]*inv[3*k+2]%p
  c=-pow(comb(3*k+1,k),-1,p)%p
  lam=c*3*inv[64%p]%p;mu=-3*inv[64%p]%p
  args=(k+1,3*k+2)
 tail=[0]*p
 for j in range(jmax+1):
  tail[p-1-j]=v
  if j<jmax:v=v*(j+1)**2*inv[args[0]+j+1]*inv[args[1]+j+1]%p
 # J=z (1-z)^r (Q R' - Q' R)
 qt=prod(q,[i*tail[i]%p for i in range(1,p)],p)
 qr=prod([i*q[i]%p for i in range(1,len(q))],tail,p)
 W=polysum(qt,[-u for u in qr],p)
 J=[0]+prod(poly_h(p,r),W,p)
 # F=(1-z)^(r-1)Q(lam*z^(h-1)+mu*z^(p-1))
 HQ=prod(poly_h(p,r-1),q,p)
 F=[0]*(p+len(HQ))
 for i,v in enumerate(HQ):
  F[h-1+i]=(F[h-1+i]+lam*v)%p
  F[p-1+i]=(F[p-1+i]+mu*v)%p
 assert len(J)-1<2*p
 assert F[p-1]==0,(p,which,'cartier_obstruction',F[p-1])
 for n in range(max(len(F),len(J)-1)):
  dJ=(n+1)*J[n+1]%p if n+1<len(J) else 0
  f=F[n] if n<len(F) else 0
  assert dJ==f,(p,which,n,dJ,f)
 P=[0]*len(J)
 for n,f in enumerate(F):
  if n!=p-1 and n+1<len(P):P[n+1]=f*inv[(n+1)%p]%p
 c=J[p]%p
 assert all((J[n]-P[n])%p==(c if n==p else 0) for n in range(len(J))), (p,which,c)
 x=pow(2 if which=='A' else 9,-1,p)
 Qx=sum(q[i]*pow(x,i,p) for i in range(len(q)))%p
 Rx=sum(tail[i]*pow(x,i,p) for i in range(p))%p
 DQx=sum(i*q[i]*pow(x,i,p) for i in range(len(q)))%p
 Px=sum(P[i]*pow(x,i,p) for i in range(len(P)))%p
 denominator=pow((1-x)%p,r,p)
 assert denominator!=0
 assert Qx==0,(p,which,'CM root not zero',Qx)
 assert (denominator*DQx*Rx+Px+c*x)%p==0,(p,which,'CM value',DQx,Rx,Px,c)
 return c,DQx*Rx%p

if __name__=='__main__':
 cases={p:(test(p,'A'),test(p,'B')) for p in (13,19,43,67,373)}
 print('PASS exact polynomial identity, only z^p integration constant, CM-specialized observer:',cases)
 assert [cases[p][0][0] for p in (13,19,43,67,373)]==[2,14,22,54,355]
 assert [cases[p][1][0] for p in (13,19,43,67,373)]==[0,11,15,50,150]
