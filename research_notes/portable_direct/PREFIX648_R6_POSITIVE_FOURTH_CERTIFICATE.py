#!/usr/bin/env python3
"""PREFIX-648 exact rational fourth-cumulant sign certificate.

Conditional on PREFIX-645's exact center and PREFIX-646/647's established
moment coupling and third-cumulant rectangle; no original 96-port run.
"""
from fractions import Fraction as Q
from math import prod
from pathlib import Path
import json

N = 189
radius = Q(1, 2**29)
delta = 2 * radius
L = {r: 2 * N * prod(N+i for i in range(r)) for r in range(1,5)}
L1,L2,L3,L4 = (L[r] for r in range(1,5))
assert L == {1:71442,2:13573980,3:2592630180,4:497784994560}
# Strict center witnesses: mu<109, Var<337, kappa3<-1209, kappa4>50374.
center_mu_max, center_var_max, center_k3_max, center_k4_min = 109,337,-1209,50374
center_m2_max = center_var_max + center_mu_max**2
center_m3_max = center_k3_max + 3*center_mu_max*center_var_max + center_mu_max**3
assert center_m2_max == 12218 and center_m3_max == 1404019
M1,M2,M3 = 110,12219,1404029
assert L1*delta < M1-center_mu_max
assert L2*delta < M2-center_m2_max
assert L3*delta < M3-center_m3_max
# kappa4=m4-4m1*m3-3m2^2+12m1^2*m2-6m1^4.
# Telescope products over the segment; local M1/M2/M3 hold throughout.
Lk4 = (L4 + 4*(M1*L3+M3*L1)+6*M2*L2
       +12*(M1**2*L2+2*M1*M2*L1)+24*M1**3*L1)
assert Lk4 == 9592604213472
fourth_perturb = Lk4*delta
fourth_lower_exact = Q(center_k4_min)-fourth_perturb
assert fourth_perturb < 35736
assert fourth_lower_exact > 14638
# The whole rectangle is contained in PREFIX-647's negative-third region.
def fourth_lower(q):
    q=Q(q)
    return 14638*q**4 + 6*322*q**3 +7*334*q**2 -110*q
def third_upper(q):
    q=Q(q)
    return -322*q**3 -3*334*q**2 +110*q
assert all(fourth_lower(q)>0 and third_upper(q)<0 for q in (12,24))
# Divided-by-q fourth lower bound increases for all real q>=12.
assert 14638*12**3+1932*12**2+2338*12-110>0
assert 3*14638*12**2+2*1932*12+2338>0
assert -322*12**2-1002*12+110<0
assert -644*12-1002<0

result = {
 "schema":"PREFIX648_R6_FOURTH_CUMULANT_SIGN_RECTANGLE_V1",
 "date":"2026-11-10",
 "frozen_scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "source_center":"PREFIX-645 @ f11c0345bf89321aba48d90671c244bdec25d416",
 "source_moment_lipschitz":"PREFIX-646 @ d64c99d8e6ea82f6c1d803df9f93b91e70eaf7b0",
 "source_third_rectangle":"PREFIX-647 @ 0dcaaf8c51a6cd38c8bc0d9183f916246e1e377c",
 "parameter_center":{"p":"1/6","z":"19/128"},
 "coordinate_radius":str(radius),
 "L_raw_moment":{str(i):L[i] for i in range(1,5)},
 "moment_local_upper":{"m1":M1,"m2":M2,"m3":M3},
 "fourth_cumulant_Lipschitz":Lk4,
 "max_L1_parameter_distance":str(delta),
 "fourth_cumulant_perturbation_upper":str(fourth_perturb),
 "fourth_cumulant_lower_fraction":str(fourth_lower_exact),
 "uniform_strict_fourth_bound":"kappa4(Y)>14638",
 "uniform_third_bound":"kappa3(Y)<-322 (from PREFIX-647)",
 "uniform_action_cumulant_sign":"kappa3(Tq)<0 and kappa4(Tq)>0 for valid real q>=12",
 "action_kappa4_lower_integer":{"12":int(fourth_lower(12)),"24":int(fourth_lower(24))},
 "testing":"ALL_CHECKS_PASS, exact Python Fraction",
 "verification_scope":"author-verified rational implications conditioned on PREFIX-645/646/647 exact prior witnesses",
 "reconstructed_189_survivor_layers":False,"reran_native_96port":False,
 "review":"UNREVIEWED/NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX648_R6_RESULTS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS")
print("fourth_lower_exact =", fourth_lower_exact)
print("fourth_perturbation =", fourth_perturb)
print("q12_lower =", fourth_lower(12), "q24_lower =", fourth_lower(24))
