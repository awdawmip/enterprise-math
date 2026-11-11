#!/usr/bin/env python3
"""PREFIX-690 exact Fraction implication checker; frozen BRC input:
f42f2906d77f24085c123f3ccfe9667d41caa96d.
Upstream 189-level recurrence and third-derivative certificates are inherited.
"""
from fractions import Fraction as Q
from json import dumps

SCIENCE_PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
L=Q('0.0528706'); R=Q('0.0530659')
fl=Q(2028625,10**9)       # F_12(L)>=fl, exact floor from PREFIX688
fr=Q(-7369716,10**9)      # F_24(R)<fr, exact floor from PREFIX688
al0,al1=Q('0.656'),Q('0.657')  # strict A(L) bounds from PREFIX689
ar0,ar1=Q('0.329'),Q('0.330')  # strict A(R) bounds from PREFIX689
assert 0<al0<al1 and 0<ar0<ar1 and fl>0 and fr<0

qlo=12-fl/al1
qhi=24-fr/ar1
assert qlo==Q(63055771,5256000)
assert qhi==Q(660614143,27500000)
assert qlo<Q('11.997')<12<24<Q('24.022')<qhi
assert (R-L)>0

def margins(q):
    # Coarse lower/upper bounds; strict at end qlo,qhi due to A<amax.
    left=fl+(q-12)*(al1 if q<=12 else al0)
    right=fr+(q-24)*(ar0 if q<=24 else ar1)
    return left,right

cert={}
for q in (qlo,Q('11.997'),Q(12),Q(13),Q(18),Q(20),
          Q(24),Q('24.022'),qhi):
    lower,upper=margins(q)
    assert lower>=0 and upper<=0,(q,lower,upper)
    if q not in (qlo,qhi):assert lower>0 and upper<0
    cert[str(q)]=[str(lower),str(upper)]

p18,n18=margins(Q(18))
assert p18==Q(31504229,8000000)
assert n18==-Q(495342429,250000000)

# For every 12<q<24, F_q(z12)=(q-12)A(z12)>0,
# F_q(z24)=(q-24)A(z24)<0. Both A windows have A>0.
assert L<Q('0.0528708')<Q('0.0530655')<R

print(dumps({
  'result':'ALL_CHECKS_PASS PREFIX690-R6',
  'science_pin':SCIENCE_PIN,
  'proof_dependencies':['PREFIX688_R6_RESULTS.json','PREFIX689_R6_PARAMETER_COLLAR_CERTIFICATE.py'],
  'coverage':'exact rational consequences of inherited endpoint and window bounds',
  'certified_q_interval':[str(qlo),str(qhi)],
  'fixed_spatial_interval':[str(L),str(R)],
  'exact_q_width':str(qhi-qlo),
  'endpoint_signed_margin_witnesses':cert,
  'q18_left_F_strict_gt':str(p18),
  'q18_right_F_strict_lt':str(n18),
  'polynomial_root_parity':'Analytic proof in manuscript: odd number of odd-multiplicity roots per q',
  'ordered_root_interpolation':'Analytic proof in manuscript: root between z12 and z24 for every 12<q<24',
  'model_recurrence':'Not rerun; exact predecessor certificates inherited',
  'status':'AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
},indent=2))
