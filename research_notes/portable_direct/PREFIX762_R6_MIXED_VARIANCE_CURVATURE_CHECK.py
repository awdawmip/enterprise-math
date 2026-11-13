#!/usr/bin/env python3
"""PREFIX-762 exact-rational mixed-variance curvature witness from PREFIX-760."""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, json

SOURCE_SHA256 = "1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76"
PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

def exact_pair(record):
    v = Q(int(record["exact_delta_variance_numerator"]),
          int(record["exact_delta_variance_denominator"]))
    w = Q(int(record["exact_delta_Vq2_numerator"]),
          int(record["exact_delta_Vq2_denominator"]))
    return v, w

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, default=Path(__file__).with_name("PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json"))
    args = p.parse_args()
    raw = args.source.read_bytes()
    assert len(raw) == 24743
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    source = json.loads(raw)
    assert source["scientific_input_commit"] == PIN
    a = {}
    for z in ("0", "1/4", "1/2"):
        var, v2 = exact_pair(source["variance_comparisons"][z])
        mean = 2*var - v2/2
        a[z] = (var, mean)
    assert a["0"][0] > 367
    assert a["1/4"][0] < -159
    assert -4 < a["1/2"][0] < -3
    assert 111 < a["0"][1] < 112
    assert a["0"][1] > a["1/4"][1] > a["1/2"][1] > 0
    b1v = a["1/4"][0] - a["0"][0]
    b2v = a["1/2"][0] - a["1/4"][0]
    b1m = a["1/4"][1] - a["0"][1]
    b2m = a["1/2"][1] - a["1/4"][1]
    assert b1v < -526 and b2v > 155
    assert -112 < b1m < 0 and b2m < 0
    assert 4*b1v-2*b1m < 0 and 4*b2v-2*b2m > 0
    for title,v,m in [("R_minus",b1v,b1m),("R_plus",b2v,b2m)]:
        print(title,"mixed_Var", format(float(v),".15g"),
              "mixed_mu",format(float(m),".15g"),
              "mixed_V2",format(float(4*v-2*m),".15g"))
    print("ALL_CHECKS_PASS PREFIX762")

if __name__=="__main__":
    main()
