#!/usr/bin/env python3
"""PREFIX-671: exact rational implication checker for fixed-witness BRC pruning.

Frozen observer: f42f2906d77f24085c123f3ccfe9667d41caa96d
Dependencies (source assumptions, not independently rerun here):
  PREFIX-659: at Q=(0,19/128), -451 < V_12,z < -449 and
              11344 < V_24,z < 11347.
  PREFIX-660: V_12,zz < -12800000; V_24,zz < -51500000
              everywhere on I=[607/4096,609/4096], and each
              q in [12,24] has a unique interior edge maximum.
  PREFIX-670: M(q)-V_q(p,z) >= L(q)*p+C(q)*p**2+...
              on [0,1/64] x I, with L(q)>=76650.
All mathematical comparisons below are exact rational operations.
"""
from fractions import Fraction as F
import json

P12, P24 = F(12), F(24)
D12, D24 = F(451), F(11347)
CURV12, CURV24 = F(12800000), F(51500000)
a0, a1 = D12/P12, D24/P24
b0, b1 = CURV12/P12, CURV24/P24
w0, w1 = a0*a0/b0, a1*a1/b1
D = D24*D24/(2*CURV24)
cut = F(1,61317)
linear = F(76650)*cut
margin = linear-D
checks = 0

def check(x, reason):
    global checks
    assert x, reason
    checks += 1

def ratio(t):
    a = (1-t)*a0+t*a1
    b = (1-t)*b0+t*b1
    return a*a/b

def weighted_bound(t):
    return (1-t)*w0+t*w1

check(w0 < w1, '24 slot dominates curvature-normalized slope bound')
check(D == F(128754409,103000000), 'exact universal witness-gap bound')
check(margin == F(38634449,2105217000000), 'strict exclusion margin')
check(margin > 0, 'nonzero uniform pruning')
check(F(76650,61318) < D, '61317 is largest integer-denominator cutoff from p-linear budget')
check(F(76650,61317) > D, '61317 cutoff works')
check(F(1,64)>cut, 'nonempty excluded strip')
check(F(1)-F(64,61317)==F(61253,61317), 'area fraction')
check(F(607,4096) <= F(19,128) <= F(609,4096), 'Q inside I')
check(F(12800000)>0 and F(51500000)>0, 'positive curvature budgets')
# The universal statement follows from a one-line exact Cauchy identity
# shown in the proof. The following tests check its algebra on test fractions,
# and do not replace that symbolic identity as the universal proof.
for t in [F(0),F(1,7),F(1,4),F(1,2),F(3,4),F(6,7),F(1)]:
    b = (1-t)*b0+t*b1
    diff = weighted_bound(t)-ratio(t)
    rhs = t*(1-t)*(a0*b1-a1*b0)**2/(b0*b1*b)
    check(diff == rhs, 'exact rational weighted Cauchy identity')
    check(diff >= 0, 'weighted Cauchy positivity')
    q = 12+12*t
    check(q*ratio(t)/2 <= D, 'uniform gap upper comparison at test rational')

result = {
    'schema':'EM_PREFIX671_R6_FIXED_WITNESS_PRUNING_V1',
    'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'dependencies':['PREFIX-659','PREFIX-660','PREFIX-670'],
    'observer':'189-layer two-direction first-stop BRC statistical observer',
    'slot_interval':['12','24'],
    'probability_interval':['607/4096','609/4096'],
    'fixed_witness':['0','19/128'],
    'universal_edge_gap_strict_upper':str(D.numerator)+'/'+str(D.denominator),
    'cutoff_p_inclusive':str(cut.numerator)+'/'+str(cut.denominator),
    'strict_uniform_advantage_lower':str(margin.numerator)+'/'+str(margin.denominator),
    'excluded_area_fraction':str(F(61253,61317).numerator)+'/'+str(F(61253,61317).denominator),
    'checks':checks,
    'proof_scope':'exact rational implication of predecessor author certificates; universal proof is the quadratic-envelope and weighted Cauchy identity',
    'review':'UNREVIEWED_NOT_ADMITTED'
}
print('ALL_CHECKS_PASS',checks)
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
