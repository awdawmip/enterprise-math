#!/usr/bin/env python3
"""PREFIX-649: exact rational implication certificate for BRC observer's
sampling-slot skewness/kurtosis flow; does not replay the native 96-port graph.
All assertions use integers and fractions, with no floating approximations.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
h = Q(1, 2**29)
delta = 2*h
L1, L2, K3, K4 = 71442, 13573980, 14877582174, 9592604213472
KW = 29291220
# Published PREFIX-645 certified center intervals (lower, upper), exact 6dp containers.
central = {
    "mu": (Q(54327837,500000), Q(4346227,40000)),
    "variance": (Q(42102733,125000), Q(67364373,200000)),
    "cumulant3": (Q(-1209500201,1000000), Q(-6047501,5000)),
    "cumulant4": (Q(25187126503,500000), Q(50374253007,1000000)),
}
# Inherited PREFIX-646/647 raw moment perturbation and PREFIX-648 C4 modulus.
mu_lo, mu_hi = central["mu"][0]-L1*delta, central["mu"][1]+L1*delta
w_lo, w_hi = central["variance"][0]-KW*delta, central["variance"][1]+KW*delta
c_lo, c_hi = central["cumulant3"][0]-K3*delta, central["cumulant3"][1]+K3*delta
d_lo, d_hi = central["cumulant4"][0]-K4*delta, central["cumulant4"][1]+K4*delta
assert Q(108)<mu_lo and mu_hi<Q(110)
assert Q(335)<w_lo and w_hi<Q(338)
assert Q(-1266)<c_lo and c_hi<Q(-1153)
assert Q(14638)<d_lo and d_hi<Q(86111)
assert delta <= Q(1,2**28) and K4*delta < 35736

# For t=1/q: V(T_q)=q^2*(b-a*t) and standardized shape:
# gamma1(t)=(c-3*b*t+a*t*t)/(b-a*t)^(3/2),
# gamma2(t)=(d-6*c*t+7*b*t*t-a*t**3)/(b-a*t)^2.
# Their derivatives, after multiplication by positive denominators:
# -2*(b-a*t)^(5/2)*gamma1'(t)
#    =6*b*b-3*a*c-a*b*t+a*a*t*t;
# (b-a*t)^3*gamma2'(t)
#    =2*a*d-6*b*c+(14*b*b-6*a*c)*t-3*a*b*t*t+a*a*t**3.
# Strict signs follow from a>0,b>0,c<0,d>0, 0<t<b/a.
assert Q(110,12) < 335  # a*t<b for q>=12

# Conservative uniform derivative lower bounds on t in [1/24,1/12].
t_min, t_max = Q(1,24), Q(1,12)
min_minus_2_gamma1_numerator = 6*335**2 + 3*108*1153 - 110*338*t_max
assert min_minus_2_gamma1_numerator > 0
# sqrt(b)<19 since b<338<361; (b-a*t)^(5/2)<338^2*19.
gamma1_slot_gap_lower = min_minus_2_gamma1_numerator / (2*338**2*19) * (t_max-t_min)
assert gamma1_slot_gap_lower > Q(1,100)

# gamma2'(t)>0; discard individually positive terms -6*a*c*t and a^2*t^3.
# 14*b^2-3*a*b*t >0 throughout the slot interval.
positive_t_coefficient = 14*335**2 - 3*110*338*t_max
assert positive_t_coefficient > 0
min_gamma2_numerator = 2*108*14638 + 6*335*1153 + t_min*positive_t_coefficient
gamma2_slot_gap_lower = min_gamma2_numerator / 338**3 * (t_max-t_min)
assert gamma2_slot_gap_lower > Q(1,200)

# All estimates are exact rational certificates; the derivative identities
# follow by elementary differentiation of the two displayed quotient forms.
results = {
 "schema": "PREFIX649_R6_STANDARDIZED_SHAPE_FLOW_V1",
 "date": "2026-11-10", "frozen_scientific_pin": PIN,
 "research_status": "AUTHOR_PROVED_EXACT_RATIONAL_IMPLICATION_UNREVIEWED_NOT_ADMITTED",
 "source_commits": {
  "center": "f11c0345bf89321aba48d90671c244bdec25d416",
  "moment_modulus": "d64c99d8e6ea82f6c1d803df9f93b91e70eaf7b0",
  "local_third": "0dcaaf8c51a6cd38c8bc0d9183f916246e1e377c",
  "local_fourth": "6b53f51abe70ac29a591fa9fcd29c1308f6c98e2"},
 "parameter_center": {"p":"1/6", "z":"19/128"},
 "coordinate_halfwidth":str(h), "max_parameter_L1_distance":str(delta),
 "certified_bounds": {"mu":["108","110"],"variance":["335","338"],"cumulant3":["-1266","-1153"],"cumulant4":["14638","86111"]},
 "exact_inherited_intervals": {name:[str(lo),str(hi)] for name,(lo,hi) in {
    "mu":(mu_lo,mu_hi),"variance":(w_lo,w_hi),"cumulant3":(c_lo,c_hi),"cumulant4":(d_lo,d_hi)}.items()},
 "gamma1_direction":"strictly_increasing_in_real_q_ge_12 (negative)",
 "gamma2_direction":"strictly_decreasing_in_real_q_ge_12 (positive)",
 "q12_q24_guarantees": {
    "skewness_gamma1_24_minus_gamma1_12":">1/100",
    "excess_kurtosis_gamma2_12_minus_gamma2_24":">1/200"},
 "certified_gap_lower": {"skewness":str(gamma1_slot_gap_lower), "excess_kurtosis":str(gamma2_slot_gap_lower)},
 "checks":"ALL_CHECKS_PASS", "native_96port_reexecution": False,
 "189_survivor_layers_reexecution":False, "independent_review":False
}
p = Path(__file__).with_name("PREFIX649_R6_RESULTS.json")
p.write_text(json.dumps(results,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS")
print("skew gap certified >",gamma1_slot_gap_lower)
print("kurtosis gap certified >",gamma2_slot_gap_lower)
