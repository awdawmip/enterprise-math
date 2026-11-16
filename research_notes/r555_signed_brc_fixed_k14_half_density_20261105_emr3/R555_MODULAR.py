#!/usr/bin/env python3
"""R555: exact prime-field elimination of all cyclotomic root ratios of Q_14."""
from R555_VERIFY import polynomials
from fractions import Fraction as F
from sympy import Symbol,Poly,cyclotomic_poly
from time import perf_counter
import os, hashlib
from math import isqrt
P=65537;x=Symbol('x');u=Symbol('u')
assert pow(3,65536,P)==1 and pow(3,32768,P)==P-1
def trim(a):
 while len(a)>1 and a[-1]%P==0:a.pop()
 return a
def divrem(a,b):
 a=trim(a[:]);b=trim(b[:]);assert b!=[0]
 if len(b)==1:return [0],[0]
 inv=pow(b[-1],-1,P);q=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b) and a!=[0]:
  j=len(a)-len(b);t=a[-1]*inv%P;q[j]=t
  for i,v in enumerate(b):a[i+j]=(a[i+j]-t*v)%P
  a=trim(a)
 return trim(q),trim(a)
def resultant_mod(a,b):
 a=trim(a[:]);b=trim(b[:]);factor=1
 while True:
  m=len(a)-1;n=len(b)-1
  if n==0:return factor*pow(b[0],m,P)%P
  _,r=divrem(a,b)
  if r==[0]:return 0
  factor=factor*pow(-1,m*n,P)*pow(b[-1],m-(len(r)-1),P)%P
  a,b=b,r
def interpolate_consecutive(ys):
 n=len(ys);tab=ys[:];diff=[];invfactorial=1
 for j in range(n):
  if j:invfactorial=invfactorial*pow(j,-1,P)%P
  diff.append(tab[0]*invfactorial%P)
  tab=[(tab[i+1]-tab[i])%P for i in range(len(tab)-1)]
 answer=[0]*n;basis=[1]
 for j,c in enumerate(diff):
  for i,b in enumerate(basis):answer[i]=(answer[i]+c*b)%P
  if j<n-1:
   nxt=[0]*(len(basis)+1)
   for i,b in enumerate(basis):nxt[i]=(nxt[i]-j*b)%P;nxt[i+1]=(nxt[i+1]+b)%P
   basis=nxt
 return trim(answer)
def gcd_mod(a,b):
 a=trim(a[:]);b=trim(b[:])
 while b!=[0]:a,b=b,divrem(a,b)[1]
 return a
def evaluate(a,z):
 acc=0
 for v in reversed(a):acc=(acc*z+v)%P
 return acc
def totient_sieve(n):
 phi=list(range(n+1))
 for p in range(2,n+1):
  if phi[p]==p:
   for j in range(p,n+1,p):phi[j]-=phi[j]//p
 return phi
def mobius_sieve(n):
 mu=[1]*(n+1)
 for p in range(2,n+1):
  if all(p%j for j in range(2,isqrt(p)+1)):
   for j in range(p,n+1,p):mu[j]=-mu[j]
   for j in range(p*p,n+1,p*p):mu[j]=0
 return mu
def cyclo_mod(q,mu):
 # Exact identity Phi_q=product_{e|q}(x^e-1)^{mu(q/e)} in F_65537[x].
 num=[1];den=[1]
 for d in range(1,isqrt(q)+1):
  if q%d:continue
  for e in (d,q//d) if d*d!=q else (d,):
   v=mu[q//e]
   if not v:continue
   a=num if v==1 else den
   b=[0]*(len(a)+e)
   for i,t in enumerate(a):
    b[i]=(b[i]-t)%P;b[i+e]=(b[i+e]+t)%P
   if v==1:num=b
   else:den=b
 out,rem=divrem(num,den)
 assert rem==[0],(q,"cyclotomic quotient")
 return out

def modular_cert(co):
 st=perf_counter();d=len(co)-1;D=d*(d-1)
 Q=[F(v,co[0]).numerator*pow(F(v,co[0]).denominator,-1,P)%P for v in co][::-1]
 assert Q[0]!=0 and Q[-1]==1
 QQ=Poly.from_list(Q[::-1],gens=x,modulus=P)
 values=[]
 for v in range(d*d+1):
  B=[a*pow(v,d-i,P)%P for i,a in enumerate(Q)]
  values.append(resultant_mod(Q,B))
 E=interpolate_consecutive(values)
 assert len(E)==d*d+1
 for v in (d*d+1,d*d+3):
  B=[a*pow(v,d-i,P)%P for i,a in enumerate(Q)]
  assert evaluate(E,v)==resultant_mod(Q,B)
  assert evaluate(E,v)==int(QQ.resultant(Poly.from_list(B[::-1],gens=x,modulus=P)))%P
 R=E
 for _ in range(d):
  R,rem=divrem(R,[P-1,1]);assert rem==[0]
 assert len(R)==D+1 and evaluate(R,1)!=0
 print("R555_MOD_INTERPOLATION_PASS deg_R=702",flush=True)
 upper_q=2*D*D;phi=totient_sieve(upper_q)
 candidates=[q for q in range(2,upper_q+1) if phi[q]<=D]
 mu=mobius_sieve(max(candidates))
 digest=hashlib.sha256(','.join(map(str,R)).encode()).hexdigest()
 assert digest=="c84af0f4ea7c4cb3f40087cac608edbeb118893d1def03dbffe79e53e57824bc",digest
 start=int(os.getenv("START","0"));end=int(os.getenv("END",str(len(candidates))))
 assert 0<=start<=end<=len(candidates)
 for idx in range(start,end):
  q=candidates[idx]
  f=cyclo_mod(q,mu)
  assert len(f)-1==phi[q]
  assert len(gcd_mod(R,f))==1,(q,"cyclotomic factor")
 assert (D,upper_q,len(candidates),max(candidates))==(702,985608,1356,2940)
 print("R555_MOD_CYCLOTOMIC_CHUNK_PASS p=65537 deg_R=702 q_bound=985608 q_candidates=1356 max_q=2940 range=",start,end,"R_sha256=",digest,"runtime_s=",round(perf_counter()-st,3))
if __name__=="__main__":
 co,a,p2=polynomials();modular_cert(co)
