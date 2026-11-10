#!/usr/bin/env python3
"""Exact rational implication checker for first integer q=9873 crossing.
Requires pinned PREFIX685 A(L),B(L) enclosures and PREFIX682/PREFIX684
bounds on F'_q across I, not a new 189-level recurrence replay.
"""
from fractions import Fraction as Q
import json

def proof():
    den=10**24
    al=Q(803334881118283114227,den)
    au=Q(803334881118283114228,den)
    bl=Q(7930886194096894324395803,den)
    bu=Q(7930886194096894324395804,den)
    q=9873
    fmin=q*al-bu
    fmax=q*au-bl
    assert fmin>0
    lower=fmin/(1800*q+150)
    upper=fmax/(1600*q+100)
    assert Q(247,10**13)<lower<upper<Q(278,10**13)
    assert 9872*au-bl<0
    return {
      "result":"ALL_CHECKS_PASS PREFIX686-R6",
      "dependencies":["PREFIX685-R6 A/B exact endpoint enclosures",
                      "PREFIX682-R6 uniform derivative signs on I",
                      "PREFIX684-R6 uniqueness of crossing on I"],
      "scientific_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
      "q":9873,
      "base_L":"2663/50000",
      "certified_root_bracket":"L + 247/10^13 < z_9873 < L + 278/10^13",
      "root_bracket_width":"31/10^13",
      "F_9873_L_enclosure":[str(fmin),str(fmax)],
      "delta_lower_exact":str(lower),
      "delta_upper_exact":str(upper),
      "q_9872_F_at_L_negative":True,
      "arithmetic":"exact Fraction strict rational comparisons",
      "prior_189_kernel_rerun":False,
      "status":"AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED"
    }
if __name__=="__main__":
    print(json.dumps(proof(),indent=2,ensure_ascii=False))
