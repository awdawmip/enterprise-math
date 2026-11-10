#!/usr/bin/env python3
"""Exact rational 7->3 bridge dual-envelope verification.

The seven exact dual minima/norms are imported as literals from R5 PR #1986;
the terminal dual table is from PR #1990. This program checks the NEW affine
minimax theorem. It does not rerun 30-column/polygon predecessor certificates.
"""
from fractions import Fraction as F

DATA = {
    "00": (F(570031933801575355927,3025154085489542635200), F(2003,2025)),
    "33": (F(9386098186912477,52340117054042400), F(335783,32400)),
    "43": (F(5506094603075,179341701138288), F(281443,43200)),
    "45": (F(95758167010,1245428480127), F(26371,6000)),
    "65": (F(239395417525,4981713920508), F(509,416)),
    "66": (F(16939155808730941927,3025154085489542635200), F(1017037,324000)),
    "ell": (F(1196977087625,89670850569144), F(13493,9936)),
}
smin = F(7933,36000)
smax = smin + F(67,162)*(F(13,40)-F(1,10))
gamma = {"00":smin, "33":1-2*smax,"43":F(0),"45":F(0),
         "65":F(0),"66":smin,"ell":F(0)}

def radius(label,t):
    beta,eta = DATA[label]
    return ((1-t)*beta+t*gamma[label])/eta

A = radius("66",F(0))
B = radius("66",F(1))
C = radius("43",F(0))
tc = (C-A)/(B-A+C)
peak = (1-tc)*C

assert smin==F(7933,36000)
assert smax==F(3761,12000)
assert gamma["33"]==F(2239,6000)
assert A==F(254087337130964128905,142439520168704998753514)
assert B==F(71397,1017037)
assert C==F(550609460307500,116839042577461087)
assert F(0)<tc<F(1) and A<C<B
assert tc==F(27506071400619459894935030258545,
             686822379881831688569552660816119)
assert peak==F(3107058982823291144749787115000,
               686822379881831688569552660816119)
# Each ratio is affine in t. On both subintervals [0,tc] and [tc,1],
# check every individual ratio at both endpoints against the active line.
for t in (F(0),tc,F(1)):
    floor = min(radius("66",t),radius("43",t))
    assert all(radius(k,t)>=floor for k in DATA)
    assert min(radius(k,t) for k in DATA)==floor
# All terminal v values are bounded by gamma (s(v) increases in v).
assert smin>0 and 1-2*smax>0
for t in (F(0),F(1,100),F(1,25),tc,F(1,10),F(1,2),F(9,10)):
    r=min(radius(k,t) for k in DATA)
    assert r>0 and r>=(1-t)*A
    if t>0:
        assert r>(1-t)*A
print("FROZEN_GLOBAL a01383f825ef9d43b4b754254303298c64041568")
print("FROZEN_EM 86149263e38c22292c9def1e0f69092efa1be77e")
print("CITED_INPUTS PR1976+PR1986+PR1990")
print("TERMINAL_S_MIN",smin,"S_MAX",smax,"GAMMA33",gamma["33"])
print("R_66_T0",A,"R_66_T1",B,"R_43_T0",C)
print("EXACT_SWITCH",tc,"APPROX",float(tc))
print("MAX_CERTIFIED_RADIUS",peak,"APPROX",float(peak))
print("PEAK_OVER_OLD_POLYGON_RADIUS",peak/A,"APPROX",float(peak/A))
print("LATE_TAPER_IMPROVEMENT",C/A,"APPROX",float(C/A))
print("BREAKPOINT_BINDING",tuple(k for k in DATA if radius(k,tc)==peak))
print("PASS_EXACT_TWO_LINE_SEVEN_CERTIFICATE_ENVELOPE")
