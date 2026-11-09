#!/usr/bin/env python3
"""PREFIX-646 integer/rational proof-implication certificate.

Uses exact strict PREFIX-645 point brackets. Does not rerun the native
96-port dynamics or the original 189-layer survivor computation.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

N=189
h=Q(1,2**27)
delta=2*h

def rising(a,r):
    v=1
    for j in range(r): v *= a+j
    return v

# Gamma stopping-time cap M=max(Gamma(N,1),Gamma(N,1)).
# E M**r <= 2 rising(N,r).
moment_cap={r:2*rising(N,r) for r in (1,2,3)}
lip={r:N*moment_cap[r] for r in (1,2,3)}
mean_cap=199 # E M <= N+sqrt(N/2)<199 since N=189<200
m2_cap=moment_cap[2]
w_lip=lip[2]+2*mean_cap*lip[1]
c3_lip=lip[3]+3*(m2_cap*lip[1]+mean_cap*lip[2])+6*mean_cap**2*lip[1]

assert N<200
assert lip=={1:71442,2:13573980,3:2592630180}
assert m2_cap==71820
assert w_lip==42007896
assert c3_lip==43064237412
assert lip[1]*delta < 1
assert w_lip*delta < 1
assert c3_lip*delta < 642

# PREFIX-645 EXACT point witness: mu<109, W>336, C3<-1209.
# On the full closed rectangle: mu<110, W>335, C3<-567.
# q>=12: kappa_3(T_q)/q < -567 q**2 -1005*q+110.
assert -567*12**2-1005*12+110 <0
assert -1134*12-1005 <0

result={
 "schema":"PREFIX646_R6_CUMULANT_STABILITY_V1",
 "date":"2026-11-10",
 "frozen_scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "source_witness":"PREFIX-645 f11c0345bf89321aba48d90671c244bdec25d416",
 "center":{"p":"1/6","z":"19/128"},
 "rectangular_half_width":str(h),
 "L1_delta_max":str(delta),
 "gamma_shape_cap":N,
 "raw_moment_caps":{str(r):str(v) for r,v in moment_cap.items()},
 "raw_moment_lipschitz":{str(r):str(v) for r,v in lip.items()},
 "variance_lipschitz":w_lip,
 "third_cumulant_lipschitz":c3_lip,
 "strict_margin_checks":{"mean":str(lip[1]*delta),"variance":str(w_lip*delta),"third_cumulant":str(c3_lip*delta)},
 "certified_uniform_bounds":{"E_Y":"<110","Var_Y":">335","kappa3_Y":"<-567","kappa3_Tq":"<0 for all q>=12"},
 "checks":"ALL_CHECKS_PASS",
 "native_96port_reexecution":False,
 "survivor_reexecution":False,
 "status":"AUTHOR_PROVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX646_R6_RESULTS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS; max L1 delta",delta,"C3 margin",c3_lip*delta)
