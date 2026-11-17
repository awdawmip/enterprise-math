#!/usr/bin/env python3
"""R749STF exact rational conditioning and one-bit repair certificate.
R749STB collision existence/fourth gap is a pinned dependency, not rechecked.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

WEIGHTS=(1,1,2,3,6)
N=125
coeff=[0]*(N+1)
coeff[0]=1
for wt in WEIGHTS:
    for k in range(wt,N+1):
        coeff[k]+=coeff[k-wt]
C=[0]*(N+1);T=[0]*(N+1)
for n in range(1,N+1):
    C[n]=C[n-1]+coeff[n-1]
    T[n]=T[n-1]+C[n-1]
assert [C[n] for n in (73,77,79,83,91,95)]==[707343,906087,1020943,1285543,1978664,2422568]
assert [T[n] for n in (73,77,79,83,91,95)]==[8931013,12046216,13914446,18379893,30933812,39491884]

record={
 'unit':'R749STF','classification':'AUTHOR_EXACT_NOT_REVIEWED',
 'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'precise_dependency':{
  'R749STB':'PR #2616 / d2a4436f4ed42aba25a54f9b7015e4c4a776c944: analytic collision curve, admissible errors, fourth gap >1/100000',
  'this_checker_reverifies_STB':False},
 'model':{'weights':list(WEIGHTS),'q_candidates':[73,77],'observations_for_ambiguity':3,'next_observation_index':3},
 'new_proved_consequences':{
  'two_states_per_prefix_in_restricted_sheet':True,
  'minimum_repair_cardinality':2,
  'zero_bit_fourth_read_minimax_error_strictly_greater_than':'1/200000',
  'one_bit_exact_all_future_reconstruction':True,
  'one_bit_fourth_read_error_bound':'103*eta',
  'eta_range':'0<=eta<=1/100000000',
  'one_bit_all_future_error_bound':'66000*eta'},
 'q_certificates':{}
}
for q in (73,77):
    c0,c1=C[q],C[q+6];t0,t1=T[q],T[q+6]
    lower=(t1*c0-t0*c1)-2*(t1-t0)-2*(c1-c0)
    denmax=(c0+2)*(c1+2)
    assert t1>t0 and c1>c0 and lower>denmax
    gamma=F(lower,denmax)
    Kd=2*(c0+c1+4)
    M0=F(t0+2,c0-2)
    Ke=F(c0+2,1)+(M0+F(1,4))*Kd
    n=q+18
    Mn=F(T[n]+2,C[n]-2)
    A3=F(n**3,C[n]-2)*(Ke+Mn*Kd)/q**3
    assert A3 < (98 if q==73 else 103)
    U=F(225000,1)*F(73,72)**5*(Ke/F(q**2)+F(2*Kd,q))/q**3
    assert U<66000
    record['q_certificates'][str(q)]={
      'C_q':c0,'C_q_plus_6':c1,'T_q':t0,'T_q_plus_6':t1,
      'true_normalized_two_read_gap_lower':str(gamma),
      'gap_numerator_lower':lower,'denominator_upper':denmax,
      'strict_margin':lower-denmax,'Kd':str(Kd),'Ke':str(Ke),
      'fourth_Lipschitz_factor_A3':str(A3),
      'fourth_Lipschitz_bound_103_verified':True,
      'all_future_global_factor_upper':str(U),
      'all_future_bound_66000_verified':True}
s=json.dumps(record,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
p=Path(__file__).with_name('R749STF_BINARY_REPAIR_RESULTS.json')
p.write_text(s,encoding='utf-8')
print('PASS R749STF: exact two-class conditioning, fourth <103*eta, all future <66000*eta')
for q,v in record['q_certificates'].items():
    print(q,'gamma',v['true_normalized_two_read_gap_lower'],
          'A3 approx',float(F(v['fourth_Lipschitz_factor_A3'])),
          'U approx',float(F(v['all_future_global_factor_upper'])))
print('results_sha256',hashlib.sha256(s.encode()).hexdigest())
