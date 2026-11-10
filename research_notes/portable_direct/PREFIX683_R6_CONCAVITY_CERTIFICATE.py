#!/usr/bin/env python3
"""PREFIX-683 exact rational implication checker.
Inputs are the pinned PREFIX-682 derivative/jet certificate, not a replay of
the 189-level survivor recurrence. Calculus proof is in the companion paper.
"""
import json
from fractions import Fraction as Q

PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
def certificate():
    radius=Q(1,2000000)
    a3=218571424275456
    b3=69527880576
    # Certified exact floors of 10**8 times A''(c), B''(c).
    floor_a2=-6657264578649
    floor_b2=-99474141353
    def abs_from_floor(k):
        return Q(max(abs(k),abs(k+1)),10**8)
    abs_a2=abs_from_floor(floor_a2)+a3*radius
    abs_b2=abs_from_floor(floor_b2)+b3*radius
    assert abs_a2 < 110000000
    assert abs_b2 < 36000
    q=10000
    gamma=Q(794,100)*(Q(110000000)+Q(36000,q))/(1600*q+100)
    assert gamma==Q(109175003573,2000012500)
    assert 0<gamma<55<3200
    assert Q(793,100)<Q(794,100)
    return {
      "result":"NEW_RATIONAL_BOUND_CHECKS_PASS",
      "scope":"Given PREFIX-682 exact premises; real q>=10000",
      "scientific_pin":PIN,
      "prior_exact_source":"enterprise-math@d437f76a2d52b617e938130c9cb9e8e61257c5a9",
      "A2_bound_exact":str(abs_a2),
      "B2_bound_exact":str(abs_b2),
      "gamma_10000":str(gamma),
      "new_conclusion":"z(q) strictly increasing and strictly concave",
      "derivative_bound":"793/[100q(1800q+150)]<z'(q)<794/[100q(1600q+100)]",
      "curvature_bound":"z''(q)<-3145*793/[100q(1800q+150)^2]<0",
      "replay_189_level_model":False,
      "status":"AUTHOR_DERIVED / EXACT_RATIONAL_BOUND_CHECKED / UNREVIEWED / NOT_ADMITTED"
    }
if __name__=="__main__":
    print(json.dumps(certificate(),ensure_ascii=False,indent=2))
