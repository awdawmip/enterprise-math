#!/usr/bin/env python3
"""X6 Unit69: sharp two-candidate signed-depth repair from min-zero + exact G and T."""
import json
from collections import Counter, defaultdict
from itertools import product
from math import factorial, isqrt, prod

PIN = "59538f585d037d09ef687b28715c4bc1a3f9fe03"
N = 10

def must(ok, why):
    if not ok:
        raise ValueError(why)

def can3(z):
    h = min(z)
    return tuple(v - h for v in z)

def gt(z):
    return sum(v*v for v in z), sum(abs(v) for v in z)

def nb(z):
    t = sum(abs(v) for v in z)
    return factorial(t)//prod(factorial(abs(v)) for v in z)

def candidates(r, g, t):
    must(len(r)==3 and all(type(v)==int and v>=0 for v in r)
         and min(r)==0 and type(g)==int and g>=0 and type(t)==int and t>=0,
         "invalid typed observer")
    R, Q = sum(r), sum(v*v for v in r)
    D = R*R + 3*(g-Q)
    if D < 0 or isqrt(D)**2 != D:
        return ()
    root = isqrt(D)
    hs = {a//3 for a in (-R-root, -R+root) if a % 3 == 0}
    return tuple(sorted(h for h in hs if sum(abs(v+h) for v in r)==t))

def run():
    fibers = defaultdict(list)
    for z in product(range(-N, N+1), repeat=3):
        r, (g,t) = can3(z), gt(z)
        h = min(z)
        cc = candidates(r,g,t)
        must(len(cc)<=2 and h in cc, "candidate recovery failed")
        must(tuple(v+h for v in r)==z, "raw coordinate repair failed")
        fibers[(r,g,t)].append(z)
    sizes = Counter(len(v) for v in fibers.values())
    must(max(sizes)<=2, "three-valued fiber")
    two = [v for v in fibers.values() if len(v)==2]
    unequal = [v for v in two if len({nb(z) for z in v})==2]
    x,y = (0,-3,-3), (4,1,1)
    must((can3(x),gt(x))==(can3(y),gt(y)), "old witness no longer collides")
    must((nb(x),nb(y))==(20,30), "old BRC counts changed")
    must(set(candidates(can3(x),*gt(x)))=={-3,1}, "sharp branch selector failed")
    result = {
        "schema":"EM_X6_UNIT69_TWO_CANDIDATE_SIGNED_DEPTH_V1",
        "science_pin":PIN,
        "model":"selected signed Z3 embedded into X6 with other three coordinates zero",
        "box":"[-10,10]^3",
        "points_tested":(2*N+1)**3,
        "distinct_observer_G_T_fibers":len(fibers),
        "fiber_size_histogram":{str(k):v for k,v in sorted(sizes.items())},
        "double_fibers":len(two),
        "double_fibers_with_distinct_N_BRC":len(unequal),
        "failures":0,
        "exact_depth_formula":"h=(-R +/- sqrt(R^2+3*(G-Q)))/3, R=sum(r), Q=sum(r_i^2)",
        "repair":"choose one of at most two feasible integer h after T filter; 1 selector bit sufficient, and necessary in worst case",
        "sharp_witness":{"r":[3,0,0],"G":18,"T":6,
                         "candidate_depths":list(candidates(can3(x),*gt(x))),
                         "N_BRC":[nb(x),nb(y)]},
        "status":"AUTHOR_EXACT_SCOPED_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED"
    }
    return result

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
