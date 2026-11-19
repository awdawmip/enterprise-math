#!/usr/bin/env python3
"""Independent exact integer checker for frozen R061 derived-minzero observer gauge, Unit151.
Does not run historical code or the original R063 benchmark.
"""
import itertools
import json
from fractions import Fraction

S = range(-3,4)
V = list(itertools.product(S, repeat=3))

def can(z):
    m=min(z)
    return tuple(t-m for t in z)

def g(z):
    return sum(t*t for t in can(z))

def add(x,y):
    return tuple(a+b for a,b in zip(x,y))

def neg(x):
    return tuple(-a for a in x)

def require(cond, label):
    if not cond:
        raise RuntimeError(label)

pos = 0
pair_tests=0
rev_min=None
rev_max=None
for z in V:
    cz = can(z)
    gz = g(z)
    gn = g(neg(z))
    require(all(x>=0 for x in cz) and min(cz)==0,"bad_minzero")
    require(gz == sum(x*x for x in cz),"bad_gauge")
    require(gz == 0 if z[0]==z[1]==z[2] else gz>0,"bad_zero_kernel")
    require(gn <= 2*gz and gz <= 2*gn,"bad_reversal_bound")
    require(can(neg(z)) == can(neg(cz)),"bad_reverse_quotient")
    if gz:
        pos += 1
        rat=Fraction(gn,gz)
        rev_min = rat if rev_min is None or rat < rev_min else rev_min
        rev_max = rat if rev_max is None or rat > rev_max else rev_max

for x in V:
    cx=can(x)
    gx=g(x)
    for y in V:
        cy=can(y)
        gy=g(y)
        sumxy=add(x,y)
        cxy=can(sumxy)
        require(cxy == can(add(cx,cy)), "quotient_add")
        gxy=g(sumxy)
        # Exact integer comparison: sqrt(gxy) <= sqrt(gx)+sqrt(gy)
        if gxy>gx+gy:
            require((gxy-gx-gy)**2 <= 4*gx*gy,"triangle_failure")
        pair_tests+=1

require(rev_min==Fraction(1,2) and rev_max==Fraction(2,1),"sharp_ratio_not_seen")
require(g((3,4,0))==25 and g((-3,-4,0))==17,"historic_witness")
require(g((0,0,1))==1 and g((0,0,-1))==2,"upper_sharp")
require(g((0,1,1))==2 and g((0,-1,-1))==1,"lower_sharp")
result={
 "schema":"ENTERPRISE_MATH_X6_UNIT151_HISTORICAL_GAUGE_FINITE_CERT_V1",
 "status":"FINITE_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED",
 "domain":"[-3,3]^3 integer triples and all ordered pairs",
 "vector_count":len(V),"nonzero_quotient_vector_count":pos,
 "ordered_pair_count":pair_tests,
 "min_reversal_squared_ratio":str(rev_min),
 "max_reversal_squared_ratio":str(rev_max),
 "example_historic":{"vector":[3,4,0],"gauge_square":25,"reversed_gauge_square":17},
 "upper_sharp_witness":{"vector":[0,0,1],"squared_ratio":"2"},
 "lower_sharp_witness":{"vector":[0,1,1],"squared_ratio":"1/2"},
 "native_benchmark_executed":False,
 "historical_script_executed":False
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(',',':')))
