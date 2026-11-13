#!/usr/bin/env python3
"""Exact combinatorial constants for PREFIX-758's analytic first-kill theorem."""
from fractions import Fraction
from math import comb
import json

gmin=2*Fraction(1,2)**25
assert gmin == Fraction(1,2**24)
D=Fraction(4**25-1-3**25,4**25)
c1=Fraction(comb(50,25),2**75)
c2=51*c1
assert c1==Fraction(15801325804719,4722366482869645213696)
assert D*c1==Fraction(4444330742038655213871594105,1329227995784915872903807060280344576)
print(json.dumps({
    "schema":"PREFIX758_R6_FIRST_KILL_MOMENT_BOUND_V1",
    "result":"PASS",
    "scientific_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "arithmetic":"Python exact Fraction/integer",
    "scope":"closed-form combinatorial factors only; analytic inequalities separately proved",
    "min_first_death_mass":str(gmin),
    "D_p0_to_quarter":str(D),
    "moment1_universal_coefficient":str(c1),
    "moment2_universal_coefficient":str(c2),
    "example_mean_gap_lower_bound":str(D*c1)
},indent=2))
print("ALL_CHECKS_PASS PREFIX758-R6")
