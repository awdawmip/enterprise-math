#!/usr/bin/env python3
"""R254 exact proof certificate for the 63-mask scalar observer at s=2/5.
Frozen scientific definition pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
All calculations use integer/Fraction arithmetic, no numerical approximation.
"""
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
import json, hashlib

W=(144,576,1440,4320,17280,86400,518400)
SCIENCE_PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
S=Q(2,5)

def setup():
 s=S; t=(1691*s-2615)/(2615*s-3539)
 a=[Q(1,5),Q(1,4),Q(3,10),Q(9,20),s,Q(2,3),t]
 b=[Q(13,60)]+[Q(5,18)*abs(Q(1,2)-a[i]) for i in range(1,7)]
 pi=[b[i]/(1-a[i]) for i in range(7)]
 assert sum(pi)==1
 z=sum(b[i]/(1-a[i])**2 for i in range(7))
 rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
 assert sum(rho)==1
 P=[[a[i]*(i==j)+(1-a[i])*pi[j] for j in range(7)] for i in range(7)]
 return a,b,pi,rho,P

def indices(m): return [0]+[j+1 for j in range(6) if m>>j&1]

def mul_linear(f,c):
 g=[Q(0)]*(len(f)+1)
 for i,x in enumerate(f):g[i]-=c*x;g[i+1]+=x
 return g

def characteristic(a,b,idx):
 prod=[Q(1)]
 for i in idx: prod=mul_linear(prod,a[i])
 for i in idx:
  g=[Q(1)]
  for j in idx:
   if j!=i:g=mul_linear(g,a[j])
  for j,x in enumerate(g):prod[j]-=b[i]*x
 assert prod[-1]==1
 return prod

def factors(n):
 out={};p=2
 while p*p<=n:
  if n%p==0:
   v=0
   while n%p==0:n//=p;v+=1
   out[p]=v
  p+=1
 if n>1:out[n]=1
 return out

def moments(a,pi,rho,idx,weight,top_k):
 v=[Q(1)]*len(idx)
 for k in range(top_k+1):
  yield weight*sum(rho[i]*v[j] for j,i in enumerate(idx))
  z=sum(pi[i]*v[j] for j,i in enumerate(idx))
  v=[a[i]*v[j]+(1-a[i])*z for j,i in enumerate(idx)]

def certificate():
 a,b,pi,rho,P=setup()
 L=lcm(*(x.denominator for row in P for x in row))
 J=lcm(*((W[m.bit_count()]*rho[i]).denominator for m in range(63) for i in indices(m)))
 T=2**3*3**3*5*277
 K=2**3*3**3*5**3*277
 assert (L,J,T,K)==(552847680,2055053,299160,7479000)
 char_coeffs={};slope={};coef_checks=0
 for m in range(63):
  ix=indices(m);d=len(ix)
  c=characteristic(a,b,ix)
  scaled=[]
  for j in range(d+1):
   f=c[j]*T**(d-j)
   assert f.denominator==1,(m,j,f)
   scaled.append(int(f))
  char_coeffs[m]=scaled
  for j in range(1,d+1):
   for p,v in factors(c[d-j].denominator).items():
    slope[p]=max(slope.get(p,0),(v+j-1)//j)
   coef_checks+=1
 assert slope=={2:3,3:3,5:1,277:1},slope
 base_count=0
 vals={};witness_mod={2:3,3:17,5:2,277:32,7:2,11:40,13:1,2053:0}
 for m in range(63):
  d=len(indices(m));ix=indices(m)
  hs=list(moments(a,pi,rho,ix,W[m.bit_count()],max(3+d-1,66)))
  vals[m]=hs
  for k in range(3,3+d):
   q=Q(J*T**k,K)*hs[k]
   assert q.denominator==1,(m,k,q)
   base_count+=1
 assert base_count==249
 receipts=[]
 for p,m in witness_mod.items():
  d=len(indices(m));c=char_coeffs[m]
  residues=[x%p for x in c]
  init=[int(Q(J*T**k,K)*vals[m][k])%p for k in range(3,3+d)]
  assert all(v!=0 for v in init),(p,m,init)
  if p!=13:
   assert residues[:-2]==[0]*(d-1),(p,m,residues)
   u=(-residues[-2])%p
   assert u!=0,(p,m,u)
   mode='eventual_geometric'
  else:
   u=2
   assert (sum(residues[j]*pow(u,j,p) for j in range(d+1))%p)==0
   assert init==[(init[0]*pow(u,j,p))%p for j in range(d)]
   mode='eigenmode_geometric'
  receipts.append({'prime':p,'mask':m,'degree':d,
    'scaled_characteristic_mod_p':residues,
    'q_k_mod_p_for_k_3_to_d_plus_2':init,'recurrence_unit':u,'proof_mode':mode})
 samples=[]
 for k in (0,1,2,3,4,5,8,16,32,64):
  observed=lcm(*(vals[m][k].denominator for m in range(63)))
  expected=J*T**k//K if k>=3 else None
  if expected is not None:assert observed==expected,(k,observed,expected)
  samples.append({'k':k,'exact_common_denominator_bits':observed.bit_length(),
    'old_full_matrix_bound_bits':(J*L**k).bit_length(),
    'spectral_scaled_bound_bits':(J*T**k).bit_length(),
    'sharp_formula_match':expected is None or observed==expected})
 result={'schema':'EM_R254_SHARP_63_LABELLED_DENOMINATOR_V1',
  'frozen_science_pin':SCIENCE_PIN,'parameter':'2/5','mask_count':63,
  'domain':'all integer k>=3',
  'theorem':'lcm_m denom(h_m,k)=J*T^k/K, with J=2055053, T=299160, K=7479000',
  'full_matrix_lcm':L,'spectral_minimum_integer_scaling':T,
  'initial_mass_denominator':J,'sharp_divisor':K,
  'T_factors':{str(p):e for p,e in factors(T).items()},
  'scaled_characteristic_coefficients_checked':coef_checks,
  'finite_integrality_bases_checked':base_count,
  'required_prime_witnesses':receipts,'exact_output_spot_checks':samples,
  'scope':'positive scalar observer only; fixed rational parameter 2/5; no native signed port preservation',
  'proof_status':'AUTHOR_PROVED_EXACT_COMPUTATION_NOT_REVIEWED','pass':True}
 return result

if __name__=='__main__':
 result=certificate()
 raw=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
 out=Path(__file__).with_name('R254_verification.json')
 out.write_text(raw,encoding='utf-8')
 print('PASS: char coefficients',result['scaled_characteristic_coefficients_checked'],
       'integrality bases',result['finite_integrality_bases_checked'],
       'modular witnesses',len(result['required_prime_witnesses']))
 print('SHA256',hashlib.sha256(raw.encode()).hexdigest())
 print('samples',[(x['k'],x['exact_common_denominator_bits']) for x in result['exact_output_spot_checks']])
