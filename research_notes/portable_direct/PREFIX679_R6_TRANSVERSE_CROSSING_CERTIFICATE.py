#!/usr/bin/env python3
"""PREFIX-679-R6: exact rational implication check; frozen BRC model.
Requires predecessor PREFIX-677/678 center jets and curvature budgets.
This does not re-execute the 189-layer frozen recurrence.
"""
from fractions import Fraction as Q
import json

b = Q(53, 1000)
rho = Q(1, 330000000)
A2 = Q(281945567232)
B2 = Q(133031808)
# Exact certified predecessor center bounds:
# 11/25<A(b)<441/1000; 789/100<B(b)<79/10;
# -1681<A'(b)<-1680; 128<B'(b)<129;
# R(b)>332788/25; q0(b) in (17.948788665,17.948788666).
DA = Q(1681)*rho + A2*rho*rho/2
DB = Q(129)*rho + B2*rho*rho/2
Am = Q(11,25)-DA
Ap = Q(441,1000)+DA
Bm = Q(789,100)-DB
Bp = Q(79,10)+DB
A_prime_abs = Q(1681)+A2*rho
B_prime_abs = Q(129)+B2*rho
L = B2*Ap + A2*Bp
Rlower = Q(332788,25)-L*rho
Rupper = B_prime_abs*Ap + Bp*A_prime_abs
slope_lower = Rlower/Ap**2
slope_upper = Rupper/Am**2
checks = [
 Am > Q(439,1000), Ap < Q(442,1000),
 Bm > 0, Bp > 0, Rlower > 6500,
 slope_lower > 33000, slope_upper < 104000,
]
q_c_lo=Q(17948788665,10**9)
q_c_hi=Q(17948788666,10**9)
q_lo=Q(1794869,100000)
q_hi=Q(1794888,100000)
checks += [
 q_c_hi - 33000*rho < q_lo,
 q_hi < q_c_lo + 33000*rho,
 q_lo < q_hi, b-rho>0, b+rho<Q(1,2),
]
Dmin = Q(12)*Q(439,1000)*33000
Dmax = Q(24)*Q(442,1000)*104000
checks += [Dmin==173844, Dmax==1103232]
qwidth=q_hi-q_lo
checks += [qwidth==Q(19,100000), qwidth/Q(104000)>0,
           qwidth/Q(33000)<2*rho]
assert all(checks), [i for i,x in enumerate(checks,1) if not x]
results = {
 'label':'PREFIX-679-R6',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'source':'PREFIX-677/678 exact center jets and global second derivative budgets',
 'verification':'EXACT_FRACTION_IMPLICATION_ONLY',
 'check_count':len(checks),
 'center':'53/1000',
 'radius':'1/330000000',
 'q_range':['1794869/100000','1794888/100000'],
 'slope_bounds':'33000 < q0_prime(z) < 104000',
 'inverse_slope_bounds':'1/104000 < z_prime(q) < 1/33000',
 'transversality':'173844*abs(z-zq) < abs(D_q(z)) < 1103232*abs(z-zq) for z != zq',
 'residual_to_root':'abs(z-zq) < abs(D_q(z))/173844 for z != zq',
 'root_band_min_separation':str(qwidth/Q(104000)),
 'root_band_max_separation':str(qwidth/Q(33000)),
 'Rupper_numerator':str(Rupper.numerator),
 'Rupper_denominator':str(Rupper.denominator),
 'slope_upper_numerator':str(slope_upper.numerator),
 'slope_upper_denominator':str(slope_upper.denominator),
 'checks':'PASS',
 'review':'AUTHOR_ONLY_UNREVIEWED_NOT_ADMITTED'
}
print('ALL_CHECKS_PASS',len(checks))
print(json.dumps(results,indent=2,ensure_ascii=False))
