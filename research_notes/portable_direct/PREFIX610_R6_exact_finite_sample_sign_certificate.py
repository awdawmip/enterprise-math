#!/usr/bin/env python3
"""PREFIX610: exact signed-coin reduction of the native BRC tagged endpoints."""
import io, json
from contextlib import redirect_stdout
from pathlib import Path
import sympy as S
with redirect_stdout(io.StringIO()):
 import PREFIX609_R6_multi_fiber_fisher_certificate as prev
assert prev.SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
C,P,h,groups=prev.C,prev.P,prev.h,prev.output_groups
pi=S.Rational(1,48)
entries=0; sums=0
for j in range(3):
 mass=S.Rational(1,12) if j==0 else S.Rational(1,24)
 for l in range(12):
  signmass={+1:S.Integer(0),-1:S.Integer(0),0:S.Integer(0)}
  for q in groups[l]:
   for yes in (True,False):
    if yes:
     a=S.cancel(pi*sum(C[j][i][q] for i in range(48)))
     d=S.cancel(sum(h[l][i]*C[j][i][q] for i in range(48) if h[l][i]))
    else:
     a=S.cancel(pi*sum(P[i][q]-C[j][i][q] for i in range(48)))
     d=S.cancel(sum(h[l][i]*(P[i][q]-C[j][i][q]) for i in range(48) if h[l][i]))
    if a==0:
     assert d==0
     continue
    r=S.cancel(d-48*a)
    z=S.cancel(d+48*a)
    s=+1 if r==0 else -1 if z==0 else 0
    assert (s!=0 or d==0), (j,l,q,yes,a,d)
    signmass[s]+=a
    entries+=1
  assert S.cancel(signmass[1]-mass/2)==0
  assert S.cancel(signmass[-1]-mass/2)==0
  assert S.cancel(sum(signmass.values())-S.Rational(1,12))==0
  assert S.cancel(signmass[0]-(S.Rational(1,12)-mass))==0
  sums+=4
result={'status':'ALL_CHECKS_PASS','science_pin':prev.SCIENCE_PIN,'original_native_blob':prev.blob,
 'sympy_version':S.__version__,
 'full_joint_likelihood':'For each active fiber l, sign S_l in {+1,-1,0}; Pr(S_l=+1)=m_j/2*(1+48 theta_l), Pr(S_l=-1)=m_j/2*(1-48 theta_l). Uninformative complementary atoms do not depend on theta_l.',
 'informative_mass_per_active_fiber':{'slot0':'1/12','slot1':'1/24','slot2':'1/24'},
 'conditional_sign_success_prob':'(1+48*theta_l)/2',
 'fisher_full_cube':{'slot0':'diag_l(192/(1-2304*theta_l**2))','slot1':'diag_l(96/(1-2304*theta_l**2))','slot2':'diag_l(96/(1-2304*theta_l**2))'},
 'M_l_distribution':'Binomial(N,m_j) marginally; joint group counts multinomial',
 'exact_conditional_variance_given_M_l_positive':'(1-2304*theta_l**2)/(2304*M_l)',
 'Pr_M_l_zero':'(1-m_j)**N',
 'global_unbiased_score_estimator_covariance':'(diag_l(1/c_j)-theta*theta^T)/N',
 'nonzero_observation_atoms_checked':entries,'symbolic_mass_equalities_checked':sums,
 'directions_checked':12,'tags_checked':3,
 'status_level':'AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX610_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'atoms':entries,'mass_checks':sums,'fisher':result['fisher_full_cube']},indent=2))
