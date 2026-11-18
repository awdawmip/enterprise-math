#!/usr/bin/env python3
"""Independent exact verifier for P46 geometric simplicity and End^0=Q(i).

Researcher: EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY
Research units R22 and R23.

The point counts are exact finite-field enumerations.  The root-of-unity
ratio test implements the finite R15 protocol for every possible order m
with phi(m)<=64.  The field-intersection witnesses are exact reductions at
prime ideals of Z[i].
"""
from __future__ import annotations

import json
from typing import Dict, List, Sequence, Tuple

import numpy as np
import sympy as sp

X,Y,t=sp.symbols('X Y t')
A_EXPR=t**4+24*t**3+192*t**2+528*t+144
D_EXPR=t**2+12*t+24

FIELD_MODULI={
 (17,1):[6],(17,2):[13,15],(17,3):[16,6,4],(17,4):[2,11,16,6],
 (29,1):[23],(29,2):[20,24],(29,3):[23,1,19],(29,4):[8,7,7,1],
}
EXPECTED_COUNTS={
 17:{1:(14,26,-12),2:(308,260,48),3:(5054,4946,108),4:(83776,84552,-776)},
 29:{1:(30,34,-4),2:(900,884,16),3:(24390,24898,-508),4:(705600,708168,-2568)},
}
EXPECTED_L={
 17:[1,12,48,-36,-814,-612,13872,58956,83521],
 29:[1,4,0,148,1298,4292,0,97556,707281],
}
G17=[(1,0),(6,2),(4,16),(-74,78),(-255,136)]
G29=[(1,0),(2,6),(-20,-8),(162,-86),(609,580)]

# ---------- exact polynomial arithmetic over F_l ----------
def trim(a,p):
 a=[int(x)%p for x in a]
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def addp(a,b,p):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]=(c[i]+x)%p
 for i,x in enumerate(b):c[i]=(c[i]+x)%p
 return trim(c,p)

def subp(a,b,p):return addp(a,[(-x)%p for x in b],p)

def mulp(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c,p)

def divmodp(a,b,p):
 a=trim(a,p);b=trim(b,p)
 if b==[0]:raise ZeroDivisionError
 q=[0]*max(1,len(a)-len(b)+1);inv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  k=len(a)-len(b);u=a[-1]*inv%p;q[k]=u
  for j,x in enumerate(b):a[j+k]=(a[j+k]-u*x)%p
  a=trim(a,p)
 return trim(q,p),trim(a,p)

def monicp(a,p):
 a=trim(a,p);u=pow(a[-1],-1,p)
 return [(u*x)%p for x in a]

def gcdp(a,b,p):
 a,b=trim(a,p),trim(b,p)
 while b!=[0]:_,r=divmodp(a,b,p);a,b=b,r
 return monicp(a,p)

def modp(a,f,p):return divmodp(a,f,p)[1]

def powmodp(a,n,f,p):
 out=[1];a=modp(a,f,p)
 while n:
  if n&1:out=modp(mulp(out,a,p),f,p)
  a=modp(mulp(a,a,p),f,p);n>>=1
 return trim(out,p)

def rabin(poly_low,p):
 f=monicp(poly_low,p);n=len(f)-1;x=[0,1];xr=modp(x,f,p)
 last=powmodp(x,p**n,f,p);gcds={};ok=last==xr
 for q in sorted(sp.factorint(n)):
  r=powmodp(x,p**(n//q),f,p);g=gcdp(f,subp(r,x,p),p)
  gcds[str(q)]=g;ok=ok and g==[1]
 return ok,{'p':p,'degree':n,'monic_coefficients_low':f,
            'x_reduced':xr,'x_pn_remainder':last,'prime_divisor_gcds':gcds}

def squarefree_high(h,p):
 low=list(reversed([int(c)%p for c in h]));der=[i*low[i]%p for i in range(1,len(low))]
 g=gcdp(low,der,p);return g==[1],g

# ---------- vectorized exact finite fields ----------
class FF:
 def __init__(self,p,n,mod):
  self.p=p;self.n=n;self.q=p**n;self.mod=np.array([x%p for x in mod],dtype=np.int64)
  ids=np.arange(self.q,dtype=np.int64);C=np.zeros((self.q,n),dtype=np.int64);z=ids.copy()
  for j in range(n):C[:,j]=z%p;z//=p
  self.C=C;self.weights=p**np.arange(n,dtype=np.int64)
 def enc(self,a):return np.sum((a%self.p)*self.weights,axis=-1).astype(np.int64)
 def mul(self,a,b):
  a=np.asarray(a,dtype=np.int64);b=np.asarray(b,dtype=np.int64)
  shape=np.broadcast_shapes(a.shape[:-1],b.shape[:-1]);a=np.broadcast_to(a,shape+(self.n,));b=np.broadcast_to(b,shape+(self.n,))
  z=np.zeros(shape+(2*self.n-1,),dtype=np.int64)
  for i in range(self.n):
   for j in range(self.n):z[...,i+j]=(z[...,i+j]+a[...,i]*b[...,j])%self.p
  for k in range(2*self.n-2,self.n-1,-1):
   c=z[...,k].copy()
   for j in range(self.n):z[...,k-self.n+j]=(z[...,k-self.n+j]-c*self.mod[j])%self.p
  return z[...,:self.n]%self.p
 def eval_all(self,coef):
  out=np.zeros_like(self.C)
  for c in reversed(coef):out=self.mul(out,self.C);out[...,0]=(out[...,0]+c)%self.p
  return out
 def roots(self):
  ids=self.enc(self.mul(self.C,self.C));r=np.full(self.q,-1,dtype=np.int64);r[ids]=np.arange(self.q,dtype=np.int64);return r

def count_pair(p,n):
 mod=FIELD_MODULI[(p,n)];ok,cert=rabin(mod+[1],p)
 if not ok:raise AssertionError((p,n,'bad field modulus'))
 F=FF(p,n,mod);A=F.eval_all([144,528,192,24,1]);D=F.eval_all([24,12,1]);aid=F.enc(A);roots=F.roots();rid=roots[aid]
 sq=rid>=0;zero=aid==0;nz=sq&(~zero);affE=int(zero.sum()+2*nz.sum())
 r=np.zeros((F.q,n),dtype=np.int64);r[sq]=F.C[rid[sq]];c=(-pow(288,-1,p))%p
 h=(c*F.mul(r,D))%p;hid=F.enc(h);chi=np.where(hid==0,0,np.where(roots[hid]>=0,1,-1));chim1=1 if F.q%4==1 else -1
 affC=int(zero.sum()+np.sum(nz*(2+(1+chim1)*chi)));chic=1 if roots[c]>=0 else -1;chineg=1 if roots[(-c)%p]>=0 else -1
 NE=affE+2;NC=affC+2+chic+chineg
 return {'p':p,'n':n,'q':F.q,'modulus_low':mod+[1],'modulus_rabin':cert,'N_E':NE,'N_C46':NC,'power_sum_P46':NE-NC}

def local_L(p,s):
 c=[1]
 for k in range(1,5):
  u=s[k-1]
  for i in range(1,k):u+=c[i]*s[k-i-1]
  assert u%k==0;c.append(-u//k)
 return c+[p*c[3],p*p*c[2],p**3*c[1],p**4]

# ---------- complete root-of-unity quotient exclusion ----------
def powersums_mod(f,l,N):
 d=len(f)-1;a=[x%l for x in f];s=[0]*(N+1);s[0]=d%l
 for n in range(1,N+1):
  u=0
  for j in range(1,min(n,d+1)):u=(u+a[j]*s[n-j])%l
  if n<=d:u=(u+n*a[n])%l
  s[n]=(-u)%l
 return s

def powered_poly(f,m,l,s):
 d=len(f)-1;q=[None]+[s[m*k]%l for k in range(1,d+1)];b=[1]
 for k in range(1,d+1):
  u=q[k]
  for j in range(1,k):u=(u+b[j]*q[k-j])%l
  b.append(-u*pow(k,-1,l)%l)
 return b

def candidate_orders():return [m for m in range(2,8193) if int(sp.totient(m))<=64]

def ratio_witnesses(f,p):
 M=candidate_orders();aux=[int(q) for q in sp.primerange(11,500) if q!=p];N=8*max(M);cache={l:powersums_mod(f,l,N) for l in aux};rows=[]
 for m in M:
  for l in aux:
   h=powered_poly(f,m,l,cache[l]);ok,g=squarefree_high(h,l)
   if ok:
    rows.append({'m':m,'phi_m':int(sp.totient(m)),'ell':l,'powered_polynomial_coefficients_high_mod_ell':h,'gcd_with_derivative_low_mod_ell':g});break
  else:return False,rows
 return len(rows)==len(M),rows

# ---------- Q(i) field certificates ----------
def conj(g):return [(a,-b) for a,b in g]
def zmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zpoly_mul(f,g):
 f=list(reversed(f));g=list(reversed(g));o=[(0,0)]*(len(f)+len(g)-1);o=list(o)
 for i,a in enumerate(f):
  for j,b in enumerate(g):u=zmul(a,b);o[i+j]=(o[i+j][0]+u[0],o[i+j][1]+u[1])
 return list(reversed(o))
def specialize(g,l,r):return [(a+b*r)%l for a,b in g]
def real_imag_coprime(g):
 n=len(g)-1;a=sp.Poly(sum(x*X**(n-i) for i,(x,y) in enumerate(g)),X,domain=sp.QQ);b=sp.Poly(sum(y*X**(n-i) for i,(x,y) in enumerate(g)),X,domain=sp.QQ)
 return sp.gcd(a,b).degree()==0

def resolvent(g):
 _,a,b,c,d=g
 add=lambda x,y:(x[0]+y[0],x[1]+y[1]);neg=lambda x:(-x[0],-x[1])
 ac4d=add(zmul(a,c),(-4*d[0],-4*d[1]));bd=zmul(b,d);a2d=zmul(zmul(a,a),d);c2=zmul(c,c)
 const=add(add((4*bd[0],4*bd[1]),neg(a2d)),neg(c2))
 return [(1,0),neg(b),ac4d,const]
def factor_pattern(h,l):
 P=sp.Poly(sum((c%l)*X**(len(h)-1-i) for i,c in enumerate(h)),X,modulus=l);sf=sp.gcd(P,P.diff()).degree()==0;degs=[]
 for q,e in sp.factor_list(P.as_expr(),modulus=l)[1]:degs += [int(sp.degree(q,X))]*int(e)
 return sorted(degs),sf

def main():
 checks={};counts={};locals={};da=int(sp.discriminant(A_EXPR,t));dd=int(sp.discriminant(D_EXPR,t));res=int(sp.resultant(A_EXPR,D_EXPR,t))
 checks['discriminants_exact']=da==-(2**16)*(3**5) and dd==(2**4)*3 and res==-(2**8)*(3**3)
 for p in (17,29):
  R=[count_pair(p,n) for n in range(1,5)];counts[str(p)]=R;checks[f'point_counts_{p}']=all((r['N_E'],r['N_C46'],r['power_sum_P46'])==EXPECTED_COUNTS[p][r['n']] for r in R)
  L=local_L(p,[r['power_sum_P46'] for r in R]);locals[str(p)]=L;checks[f'local_polynomial_{p}']=L==EXPECTED_L[p];checks[f'good_split_ordinary_{p}']=da%p and dd%p and res%p and p%4==1 and L[4]%p!=0
 f17=EXPECTED_L[17];f29=EXPECTED_L[29]
 checks['gaussian_norm_factorization_17']=zpoly_mul(G17,conj(G17))==[(c,0) for c in f17]
 checks['gaussian_norm_factorization_29']=zpoly_mul(G29,conj(G29))==[(c,0) for c in f29]
 ok17,c17=rabin(list(reversed(specialize(G17,5,2))),5);ok29,c29=rabin(list(reversed(specialize(G29,101,10))),101)
 checks['g17_irreducible_over_Qi']=ok17;checks['g29_irreducible_over_Qi']=ok29
 checks['f17_irreducible_over_Q']=ok17 and real_imag_coprime(G17);checks['f29_irreducible_over_Q']=ok29 and real_imag_coprime(G29)
 f7=X**8+5*X**6+245*X**2+2401;checks['p7_certificate_fails_at_m2']=sp.expand(f7.subs(X,-X)-f7)==0 and f7.subs(X,0)!=0
 rr17,w17=ratio_witnesses(f17,17);rr29,w29=ratio_witnesses(f29,29);M=candidate_orders()
 checks['candidate_order_set_complete']=len(M)==126 and max(M)==240 and all((int(sp.totient(m))>64) or m in set(M) for m in range(2,8193))
 checks['absolute_simplicity_ratio_certificate_17']=rr17;checks['absolute_simplicity_ratio_certificate_29']=rr29
 R29=resolvent(G29);okR,cR=rabin(list(reversed(specialize(R29,17,4))),17);checks['g29_resolvent_irreducible_over_Qi']=okR
 pairs=[];allpairs=True
 for s17,h17 in (('+',G17),('-',conj(G17))):
  for s29,h29 in (('+',G29),('-',conj(G29))):
   a17=specialize(h17,37,6);a29=specialize(h29,37,6);p17,sf17=factor_pattern(a17,37);p29,sf29=factor_pattern(a29,37);good=sf17 and sf29 and p17==[2,2] and p29==[1,3];allpairs &= good
   pairs.append({'pairing':f'g17{s17}__g29{s29}','ell':37,'i_mod_ell':6,'g17_coefficients_high_mod_ell':a17,'g29_coefficients_high_mod_ell':a29,'g17_factor_degrees':p17,'g29_factor_degrees':p29,'both_squarefree':sf17 and sf29,'distinguished':good})
 checks['all_four_Qi_field_pairings_nonisomorphic']=allpairs
 checks['P46_geometrically_simple']=checks['good_split_ordinary_17'] and checks['f17_irreducible_over_Q'] and rr17
 checks['End0_P46_equals_Qi']=checks['P46_geometrically_simple'] and checks['good_split_ordinary_29'] and checks['f29_irreducible_over_Q'] and rr29 and okR and allpairs
 out={'schema':'EM_FREE_F6D046_P46_GEOMETRIC_ENDOMORPHISM_VERIFICATION_V1','researcher_id':'EM-FREE-F6D046','research_units':['EM-FREE-F6D046-R22-P46-CORRECTED-ABSOLUTE-SIMPLICITY','EM-FREE-F6D046-R23-P46-ASYMMETRIC-ENDOMORPHISM-INTERSECTION'],'all_passed':all(bool(v) for v in checks.values()),'check_count':len(checks),'checks':checks,'correction':{'invalidated_attempt':'p=7 absolute-simplicity lift','first_failing_witness':'m=2; f_7(X)=f_7(-X)','replacement_good_reductions':[17,29]},'curve_invariants':{'disc_A':da,'disc_D':dd,'resultant_A_D':res},'point_count_records':counts,'local_L_polynomials_coefficients_ascending':locals,'characteristic_polynomials_coefficients_high':{'17':f17,'29':f29},'quartic_irreducibility_certificates':{'g17_mod_(5,i-2)':c17,'g29_mod_(101,i-10)':c29},'unit_root_order_bound':{'degree_pair_field_bound':64,'m_bound':8192,'candidate_count':len(M),'candidate_max':max(M),'candidates':M},'root_ratio_witnesses':{'17':w17,'29':w29},'g29_cubic_resolvent':{'coefficients_high_pairs':R29,'reduction_prime':17,'i_mod_prime':4,'rabin_certificate':cR},'field_nonisomorphism_witnesses':pairs,'theorems':{'geometric_simplicity':'P46/Qbar is geometrically simple','geometric_endomorphism_algebra':'End^0_Qbar(P46)=Q(i)'},'classification':['DERIVED_GEOMETRIC_THEOREM','GEOMETRICALLY_SIMPLE','GEOMETRIC_ENDOMORPHISM_ALGEBRA_QI','CORRECTION_AWARE','NOT_NEW_AXIOM','NOT_FOUNDATION','P000_UNCHANGED']}
 print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if out['all_passed'] else 1)

if __name__=='__main__':main()
