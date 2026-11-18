#!/usr/bin/env python3
"""R762EY exact q9 mod27/mod81 normalized terminal period certificates."""
import hashlib
import json
Q = 9
BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
CASES=((3,162,14),(4,486,16))  # precision, period, first index
ORDER=127
LAST=max(N+ORDER-1+T for h,T,N in CASES)
F=lambda n:max(0,n//3-2)
MOD=3**(F(LAST)+max(h for h,T,N in CASES))

def ix(x,y,z):return (x*Q+y)*Q+z
SHIFT=[tuple(ix((x-dx)%Q,(y-dy)%Q,(z-dz)%Q) for x in range(Q) for y in range(Q) for z in range(Q)) for dx,dy,dz in BRANCHES]

def compute():
 v=[0]*(Q**3);v[0]=1
 raw={3:{},4:{}}
 for n in range(LAST+1):
  assert sum(v)%MOD==pow(6,n,MOD),('mass',n)
  if n>=13:
   e=3**F(n)
   assert all(z%e==0 for z in v),('integrality',n)
   for h in (3,4):raw[h][n]=bytes((z//e)%(3**h) for z in v)
  if n<LAST:v=[sum(v[p[i]] for p in SHIFT)%MOD for i in range(Q**3)]
 output={'schema':'R762EY_EXACT_INTEGER_CERT_V1','q':Q,'coordinate_order':'(x*9+y)*9+z', 'last_power':LAST,'fixed_modulus_exponent':F(LAST)+4,'recurrence_order':ORDER,'mass_checks':LAST+1,'normalization_integrality_coefficient_checks':(LAST-12)*Q**3,'status':'PASS','cases':[]}
 for h,T,N in CASES:
  s=raw[h]
  for n in range(N,N+ORDER):assert s[n]==s[n+T],('initial_window',h,n)
  minprev=T//3
  pre_old=N-1
  differences={}
  w0=next(n for n in range(N,N+T) if s[n]!=s[n+minprev])
  for label,u,w in [('exclude_previous_period',w0,w0+minprev),('preperiod_sharp',pre_old,pre_old+T)]:
   ix0=next((i for i,(a,b) in enumerate(zip(s[u],s[w])) if a!=b),None)
   assert ix0 is not None,(h,label)
   differences[label]={'n':u,'compare_n':w,'index':ix0,'residue_n':s[u][ix0],'residue_compare':s[w][ix0]}
  output['cases'].append({'h':h,'modulus':3**h,'candidate_period':T,'candidate_preperiod':N,'window_start':N,'window_end':N+ORDER-1,'period_vector_equalities':ORDER,'period_coefficient_equalities':ORDER*Q**3,'witnesses':differences,'window_concat_sha256':hashlib.sha256(b''.join(s[n] for n in range(N,N+ORDER))).hexdigest(),'window_pairs_concat_sha256':hashlib.sha256(b''.join(s[n]+s[n+T] for n in range(N,N+ORDER))).hexdigest()})
 return output
if __name__=='__main__':print(json.dumps(compute(),indent=2,sort_keys=True))
