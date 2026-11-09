#!/usr/bin/env python3
"""PREFIX-637 exact rational corollary certificate; relies on PREFIX-635/636 certified continuous envelopes.
Frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
No 189-layer rerun or original 96-port graph execution is claimed.
"""
import json
from fractions import Fraction as F
from pathlib import Path

CENTRE = dict(mu_lower=300,mu_upper=310,curvature_lower=23000,curvature_upper=50000)
STRIP = dict(mu_lower=299,mu_upper=311,curvature_lower=22000,curvature_upper=51000)
t24,t12=F(1,24),F(1,12)
dt=t12-t24
assert dt==F(1,24)

def curvature_bounds(e):
    assert 0 < e['mu_lower'] < e['mu_upper']
    assert 0 < e['curvature_lower'] < e['curvature_upper']
    lo=F(e['mu_lower']**2,e['curvature_upper'])
    hi=F(e['mu_upper']**2,e['curvature_lower'])
    assert 0<lo<hi
    return lo,hi

a,b=curvature_bounds(CENTRE)
c,d=curvature_bounds(STRIP)
checks={
    "t_interval": t24==F(1,24) and t12==F(1,12),
    "centre_curvature_lower":a==F(9,5),
    "centre_curvature_upper":b==F(961,230),
    "strip_curvature_lower":c==F(89401,51000),
    "strip_curvature_upper":d==F(96721,22000),
    "strip_simple_lower":c>F(7,4),
    "strip_simple_upper":d<F(22,5),
    "centre_envelope_sharper":a>c and b<d,
    "mean_gap_lower":c*dt==F(89401,1224000),
    "mean_gap_upper":d*dt==F(96721,528000),
    "centre_mean_gap_lower":a*dt==F(3,40),
    "centre_mean_gap_upper":b*dt==F(961,5520),
    "jensen_lower":c*dt**2/8==F(89401,235008000),
    "centre_jensen_lower":a*dt**2/8==F(1,2560),
    "jensen_strict_positive":c*dt**2/8>0,
    "curvature_strict_positive":STRIP['curvature_lower']>0,
    "p2_strip_radius_positive":F(1,2**33)>0,
    "p2_strip_inside_probability_domain":0<F(19,128)-F(1,2**33)<F(19,128)+F(1,2**33)<1
}
assert all(checks.values()),[key for key,value in checks.items() if not value]
result={
    "schema":"PREFIX637_R6_OPTIMAL_VALUE_CURVATURE_V1",
    "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "predecessor_commits":{"PREFIX635":"ec03483204af911eef75785bcdaf610d24519ab2","PREFIX636":"c70457fde1d39265b126976bd92126731c31c23e"},
    "p1_interval":["4/25","161/1000"],
    "p2_centre":"19/128",
    "p2_radius":"1/8589934592",
    "t_interval":["1/24","1/12"],
    "identity":"Phi_tt=-(mu_p(c,z))^2/G_pp(c,t,z)",
    "centre_curvature":[str(a),str(b)],
    "strip_curvature":[str(c),str(d)],
    "centre_mean_gap":[str(a*dt),str(b*dt)],
    "strip_mean_gap":[str(c*dt),str(d*dt)],
    "centre_midpoint_surplus_lower":str(a*dt**2/8),
    "strip_midpoint_surplus_lower":str(c*dt**2/8),
    "checks":len(checks),
    "validation":"ALL_CHECKS_PASS",
    "evidence_scope":"Exact rational consequences of PREFIX-635/636 continuous theorems; 189-level computation inherited, not repeated",
    "status":"AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED",
    "next_question":"Exact adaptive two-variable Bernstein certificate across [3/20,1/6] x [37/256,39/256]."
}
Path(__file__).with_name('PREFIX637_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',len(checks))
print('centre',a,b,'strip',c,d)
print('mean gap bounds',c*dt,d*dt)
print('Jensen lower',c*dt**2/8)
