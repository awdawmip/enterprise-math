#!/usr/bin/env python3
"""R556 exact GF(65537) quotient-resultant exclusion, 1574 candidate cyclotomics, chunkable."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,os,sys
import numpy as np
from numba import njit
from sympy import Poly,Symbol,cyclotomic_poly
import R556_VERIFY as B
UP=Path(__file__).resolve().parents[1]/"r555_signed_brc_fixed_k14_half_density_20261105_emr3"
sys.path.insert(0,str(UP))
import R555_MODULAR as M
P=65537;d=29;D=812
@njit
def power(x,n,p):
 v=1
 while n:
  if n&1:v=v*x%p
  x=x*x%p;n//=2
 return v
@njit
def gcd_degree(A,B):
 N=len(A);a=np.zeros(N,dtype=np.int64);b=np.zeros(N,dtype=np.int64)
 na=len(A)-1;nb=len(B)-1
 for i in range(len(A)):a[i]=A[i]
 for i in range(len(B)):b[i]=B[i]
 while nb>=0:
  inv=power(b[nb],P-2,P)
  while na>=nb:
   scale=a[na]*inv%P;offset=na-nb
   for j in range(nb+1):a[offset+j]=(a[offset+j]-scale*b[j])%P
   while na>=0 and a[na]==0:na-=1
  a,b=b,a
  na,nb=nb,na
 return na
def verify():
 co,a,p2=B.polynomials()
 assert len(co)==30 and p2==40920
 Q=[(v.numerator*pow(v.denominator,-1,P))%P for v in reversed([F(v,co[0]) for v in co])]
 assert Q[-1]==1 and Q[0]!=0
 values=[]
 for z in range(d*d+1):
  Z=[v*pow(z,d-i,P)%P for i,v in enumerate(Q)]
  values.append(M.resultant_mod(Q,Z))
 E=M.interpolate_consecutive(values)
 assert len(E)==d*d+1
 xx=Symbol("x");raw=Poly.from_list(Q[::-1],gens=xx,modulus=P)
 for z in (d*d+1,d*d+5):
  Z=[v*pow(z,d-i,P)%P for i,v in enumerate(Q)]
  assert M.evaluate(E,z)==M.resultant_mod(Q,Z)==int(raw.resultant(Poly.from_list(Z[::-1],gens=xx,modulus=P)))%P
 R=E
 for _ in range(d):
  R,rem=M.divrem(R,[P-1,1]);assert rem==[0]
 assert len(R)==D+1 and M.evaluate(R,1)!=0
 digest=hashlib.sha256(",".join(map(str,R)).encode()).hexdigest()
 assert digest=="704303ec06de0fd5ab4c78be0d3f235be0aaaaa7a6a07939ebcf427dc57ddeb3",digest
 phi=M.totient_sieve(2*D*D)
 candidates=[q for q in range(2,2*D*D+1) if phi[q]<=D]
 assert len(candidates)==1574 and max(candidates)==3570
 start=int(os.getenv("START","0"));end=int(os.getenv("END",str(len(candidates))))
 assert 0<=start<=end<=len(candidates)
 Rn=np.array(R,dtype=np.int64)
 assert gcd_degree(Rn,np.array([1,1],dtype=np.int64))==0
 for idx in range(start,end):
  q=candidates[idx]
  ff=Poly(cyclotomic_poly(q,xx),xx,modulus=P)
  f=np.array([int(v)%P for v in reversed(ff.all_coeffs())],dtype=np.int64)
  assert len(f)-1==phi[q] and gcd_degree(Rn,f)==0,(idx,q)
 print("R556_MODULAR_EXCLUSION_PASS range=",start,end,"count=",end-start,"total=1574 q_bound=1318688 p=65537 R_sha256=",digest,flush=True)
if __name__=="__main__":verify()
