#!/usr/bin/env python3
"""R244: rational two-Perron-mode uniform relative-error certificate.

Dependency: R243 exact all-parameter spectral tier bound.
Only exact fractions and integer arithmetic are used for PASS.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json

R0 = Q(990628, 1000000)
GAMMA = Q(977, 1000)
DELTA = Q(973, 1000)
C_G = Q(1681, 8400)
C_0 = Q(8424836672439, 1042768025600)
CASES = ((100, 372), (1000, 505))

def bound(n):
    assert n >= 2
    k = n-1
    qg = GAMMA/R0
    qd = DELTA/R0
    assert 0 < qd < qg < 1
    assert 0 < C_G < C_0 - 1
    return C_G*qg**k + (C_0-1-C_G)*qd**k

def digest(x):
    return sha256((str(x.numerator)+"/"+str(x.denominator)).encode()).hexdigest()

def main():
    rows = []
    for d, n in CASES:
        value, previous = bound(n), bound(n-1)
        upper_margin = Q(1,d)-value
        predecessor_margin = previous-Q(1,d)
        assert upper_margin > 0 and predecessor_margin >= 0
        rows.append({
            "target":f"1/{d}",
            "smallest_n_for_R244_explicit_bound":n,
            "n_certified":upper_margin>0,
            "n_minus_1_not_certified_by_this_bound":predecessor_margin>=0,
            "positive_margin_sha256":digest(upper_margin),
            "predecessor_nonnegative_margin_sha256":digest(predecessor_margin),
            "margin_numerator_bits":upper_margin.numerator.bit_length(),
            "margin_denominator_bits":upper_margin.denominator.bit_length(),
            "diagnostic_bound_decimal":format(float(value),'.16g')
        })
    print(json.dumps({
        "schema":"EM_R244_TWO_MODE_UNIFORM_TAIL_V1",
        "status":"PASS",
        "arithmetic":"exact Python fractions and integer comparisons",
        "domain":"39/100<s<41/100",
        "frozen_scientific_pin":"awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        "dependency_R243":"ef38804fff510da663a49202e4cac8060f2082c8",
        "root_lower":str(R0),
        "gamma":str(GAMMA),
        "delta":str(DELTA),
        "cG":str(C_G),
        "c0":str(C_0),
        "coefficient_delta":str(C_0-1-C_G),
        "cases":rows,
        "interpretation":"smallest integer horizons certified by the explicit R244 bound; not claimed optimal for actual two-mode model",
        "review":"NOT_REVIEWED",
        "native_BRC":"NOT_EXECUTED"
    },sort_keys=True,indent=2))

if __name__=="__main__":
    main()
