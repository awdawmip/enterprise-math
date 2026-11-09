#!/usr/bin/env python3
"""Exact p^3 Jacobi spectral two-node certificate for D25; author-side."""
import json
from math import comb, isqrt

def direct_f(p,z,mod):
 c=t=acc=1
 for k in range(1,p):
  c=c*(8*k-7)*(8*k-5)*pow(64*k*k,-1,mod)%mod
  t=t*z%mod
  acc=(acc+c*t)%mod
 return acc

def jacobi(n,z,mod):
 c=t=acc=1
 for k in range(1,n+1):
  c=c*(k-1-n)*(2*n+2*k-1)*pow(2*k*k,-1,mod)%mod
  t=t*z%mod
  acc=(acc+c*t)%mod
 return acc

def curvature(p,z):
 u0,u1,u2=1,0,0
 t=1;acc=0
 for k in range(1,p):
  i=k-1;r=(8*i+1)*(8*i+3)*pow(64,-1,p)%p
  v=pow(k*k,-1,p)
  u0,u1,u2=u0*r*v%p,(u1*r+u0)*v%p,(u2*r+u1)*v%p
  t=t*z%p
  acc=(acc+u2*t)%p
 return acc

def mul(x,y,m):
 return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)

def legendre(n,p):
 m=p**3;t=(0,2*pow(3,-1,m))
 minus=(t[0]-1,t[1]);plus=(t[0]+1,t[1])
 pm=[(1,0)];pp=[(1,0)]
 for k in range(n):
  pm.append(mul(pm[-1],minus,m));pp.append(mul(pp[-1],plus,m))
 res=(0,0)
 for k in range(n+1):
  prod=mul(pm[k],pp[n-k],m);v=comb(n,k)**2
  res=((res[0]+prod[0]*v)%m,(res[1]+prod[1]*v)%m)
 inv=pow(pow(2,n,m),-1,m)
 return(res[0]*inv%m,res[1]*inv%m)

def check(p,independent=False):
 assert p>3 and p%8==5
 m=p**3;z=pow(9,-1,m);a=(5*p-1)//8;b=(7*p-3)//8
 assert a<b<p
 f=direct_f(p,z,m);A=jacobi(a,z,m);B=jacobi(b,z,m)
 assert (12*f-7*A-5*B)%(p*p)==0
 wa=7*(2-7*p)*pow(24*(1-p),-1,m)%m
 wb=5*(2+5*p)*pow(24*(1-p),-1,m)%m
 la=(-5*p*pow(32,-1,m)-25*p*p*pow(64,-1,m))%m
 lb=(7*p*pow(32,-1,m)-49*p*p*pow(64,-1,m))%m
 assert (wa+wb)%m==1 and (wa*la+wb*lb)%m==0
 K=curvature(p,z%p);weighted=(wa*A+wb*B)%m
 corrected=(weighted-35*p*p*pow(1024,-1,m)*K)%m
 assert corrected==f
 if independent:
  assert legendre(2*a,p)==(A,0)
  assert legendre(2*b,p)==(B,0)
 return {'p':p,'a':a,'b':b,'p3':m,'F':f,'J_a_mod_p2':A%(p*p),
         'J_b_mod_p2':B%(p*p),'K_mod_p':K,'weighted':weighted,
         'corrected':corrected,'F_div_p2_mod_p':f//(p*p) if f%(p*p)==0 else None,
         'independent_Legendre':independent,'PASS':True}

if __name__=='__main__':
 primes=[5,13,29,37,53,61,109,157,181,373]
 output=[check(p,p in (13,37,61,109,373)) for p in primes]
 print(json.dumps({'schema':'D25_SPECTRAL_JACOBI_P3_EXACT_V1','all_passed':True,
                   'count':len(output),'independent_legendre_count':5,'results':output},
                  indent=2))
