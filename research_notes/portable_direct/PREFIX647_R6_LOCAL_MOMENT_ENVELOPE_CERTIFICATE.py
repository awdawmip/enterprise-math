#!/usr/bin/env python3
"""Exact rational implication certificate, PREFIX-647-R6.

Dependent on strict exact central-point inequalities in PREFIX-645.
Does not re-execute native 96-port dynamics or the 189-layer survivor witness.
"""
from fractions import Fraction as F
from pathlib import Path
from math import prod
import json

N = 189
h = F(1,2**25)
delta = 2*h
rising = lambda n,r: prod(n+i for i in range(r))
L = {r:2*N*rising(N,r) for r in (1,2,3)}
L1,L2,L3 = [L[r] for r in (1,2,3)]
# Strict central-point brackets from PREFIX-645:
mu0_max, var0_min, var0_max, third0_max = 109,336,337,-1209
m2_center_max = var0_max + mu0_max**2
mu_local_max, m2_local_max = 110,12219
assert m2_center_max == 12218
assert F(L1)*delta < mu_local_max-mu0_max
assert F(L2)*delta < m2_local_max-m2_center_max

# Mean value/pathwise product-difference bounds on the segment from
# (p0,z0) to a point in the rectangle.
Lvar_local = L2 + 2*mu_local_max*L1
Lthird_local = L3 + 3*(m2_local_max*L1+mu_local_max*L2)+6*mu_local_max**2*L1
assert L == {1:71442,2:13573980,3:2592630180}
assert Lvar_local == 29291220
assert Lthird_local == 14877582174
assert F(Lvar_local)*delta < 2
assert F(Lthird_local)*delta < 887
# m1<110, Var>334, kappa_3(Y)<-322 for all points in rectangle.
assert var0_min-2 == 334
assert third0_max+887 == -322
q=F(12)
upper_at_12 = -322*q*q -3*334*q + 110
slope_at_12 = -644*q -3*334
assert upper_at_12 < 0 and slope_at_12<0
# Comparison to previously published PREFIX-646: h0=2^-27.
assert h/F(1,2**27) == 4

f=lambda x: str(x)
result={
 "schema":"PREFIX647_R6_LOCAL_MOMENT_ENVELOPE_V1",
 "date":"2026-11-10",
 "frozen_scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "source_witness":"PREFIX-645 enterprise-math@f11c0345bf89321aba48d90671c244bdec25d416",
 "prior_radius":"1/134217728", "new_radius":f(h),"radius_enlargement_factor":4,
 "center":{"p":"1/6","z":"19/128"},
 "local_rectangular_parameter_delta_max":f(delta),
 "raw_moment_lipschitz":{str(k):v for k,v in L.items()},
 "m2_center_bound":"<12218","m2_local_bound":"<12219","mu_local_bound":"<110",
 "variance_local_lipschitz":Lvar_local,"third_cumulant_local_lipschitz":Lthird_local,
 "strict_inequalities":{
  "mu_perturbation":f(L1*delta),"m2_perturbation":f(L2*delta),
  "var_perturbation":f(Lvar_local*delta),"third_perturbation":f(Lthird_local*delta),
  "kappa3_Tq_over_q_upper_at_q12":f(upper_at_12),
  "upper_polynomial_derivative_at_q12":f(slope_at_12)
 },
 "uniform_bounds":{"mean":"<110","variance":">334","third_cumulant_Y":"<-322",
  "third_cumulant_Tq":"<0 for all real q>=12 where marked law exists"},
 "verification":"ALL_CHECKS_PASS",
 "validation_kind":"EXACT_RATIONAL_IMPLICATION_FROM_PREFIX645_POINT_WITNESS",
 "survivor_reexecution":False,"native_96port_reexecution":False,
 "admission":"AUTHOR_DERIVED/UNREVIEWED/NOT_ADMITTED"
}
Path(__file__).with_name('PREFIX647_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('ALL_CHECKS_PASS')
for k,v in result['strict_inequalities'].items(): print(k,v)
