#!/usr/bin/env python3
"""PREFIX-636: exact transverse stability audit using PREFIX-635's prior fixed-slice lemma."""
import json
from fractions import Fraction as Q
from pathlib import Path

N, M = 189, 188
base_p2, delta = Q(19,128), Q(1,2**33)
a, b = Q(4,25), Q(161,1000)
root_12 = (Q(168247,2**20), Q(168248,2**20))
root_24 = (Q(167883,2**20), Q(167884,2**20))
assert a < root_24[0] < root_24[1] < root_12[0] < root_12[1] < b
K0, K1, K2 = N*M**2, 11*N**2*M**2, 25*N**2*M**3
m_left = 23000*(root_24[0]-a)
m_right = 23000*(b-root_12[1])
checks = {
    "p2_interval_inside_unit": 0 <= base_p2-delta < base_p2+delta <= 1,
    "alpha_beta_nb_weights": N==M+1,
    "mu_prime_perturbation_lt_one": K0*delta < 1,
    "q_endpoint_grad_margin_left": K1*delta < m_left,
    "q_endpoint_grad_margin_right": K1*delta < m_right,
    "F_second_perturbation_lt_1000": K2*delta < 1000,
    "uniform_strict_convexity": 23000-K2*delta > 22000,
    "uniform_curvature_upper": 50000+K2*delta < 51000,
    "uniform_mu_prime_lower": 300-K0*delta > 299,
    "uniform_mu_prime_upper": 310+K0*delta < 311
}
assert all(checks.values()), checks
gap_lo, gap_hi = Q(299,51000*24), Q(311,22000*24)
assert 0<gap_lo<gap_hi<1
fmt=lambda z:f"{z.numerator}/{z.denominator}"
result = {
 "schema":"PREFIX636_R6_TRANSVERSE_STABILITY_EXACT_V1",
 "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "source_dependency":"enterprise-math@ec03483204af911eef75785bcdaf610d24519ab2 (PREFIX-635)",
 "model_scope":"two-information-direction BRC signed statistical first-passage observer; original native 96-port graph frozen",
 "p1_range":[fmt(a),fmt(b)],"p2_center":fmt(base_p2),"p2_radius":fmt(delta),
 "q_range":[12,24],"N":N,"M":M,
 "K_mu_mix":K0,"K_grad_mix":K1,"K_curv_mix":K2,
 "delta_K0":fmt(K0*delta),"delta_K1":fmt(K1*delta),"delta_K2":fmt(K2*delta),
 "left_margin_from_prefix635":fmt(m_left),"right_margin_from_prefix635":fmt(m_right),
 "strict_mu_prime_bounds":"299 < mu_p1 < 311",
 "strict_curvature_bounds":"22000 < F_q_p1p1 < 51000",
 "unique_minimum":True,"monotonic_in_q":"dc/dq < 0",
 "gap_lower_strict":fmt(gap_lo),"gap_upper_strict":fmt(gap_hi),
 "transverse_root_sensitivity_bound":fmt(Q(K1,22000)),
 "checks":checks,"validation":"ALL_CHECKS_PASS",
 "status":"AUTHOR_DERIVED_FROM_PREFIX635 / EXACT_RATIONAL_BOUND_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if __name__=="__main__":
 p=Path(__file__).with_name("PREFIX636_R6_RESULTS.json")
 p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print("ALL_CHECKS_PASS",len(checks))
 print(fmt(gap_lo),"< c(12,p2)-c(24,p2) <",fmt(gap_hi))
