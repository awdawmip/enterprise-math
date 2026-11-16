#!/usr/bin/env python3
"""Exact Helly S12 positive chart -> provenance-labelled signed X6 BRC lift.

Chart producer: scripts/tool_discovery_helly_radon_certificate_calculus.py
Git blob 6118b3bd04010e05355586d353c9cf0ec38b1070.
Independent checker for its fixed finite chart constraints, not entire producer.
"""
from itertools import combinations, product
from math import comb
import hashlib
import json

def calculate():
    chart_constraints = (
        (frozenset(range(2, 8)), frozenset(range(1, 7))),
        (frozenset(range(5, 10)), frozenset(range(0, 5))),
        (frozenset(range(4, 9)), frozenset(range(3, 10))),
    )
    a_values = tuple(sorted(set.intersection(*(set(c[0]) for c in chart_constraints))))
    b_values = tuple(sorted(set.intersection(*(set(c[1]) for c in chart_constraints))))
    if a_values != (5, 6, 7) or b_values != (3, 4):
        raise AssertionError("producer chart changed")
    anchor = (10, -2, 3, 0, 1, 7)
    paths = {}
    labelled = []
    for i, j in combinations(range(6), 2):
        for si, sj in product((-1, 1), repeat=2):
            for a, b in product(a_values, b_values):
                disp = [0] * 6
                disp[i], disp[j] = si*a, sj*b
                disp = tuple(disp)
                end = tuple(x + v for x, v in zip(anchor, disp))
                w = comb(a+b, a)
                record = (i, j, si, sj, a, b)
                if disp in paths:
                    raise AssertionError("strict positive support should be injective")
                paths[disp] = {"end":end, "n_brc":w, "provenance":record,
                               "g":sum(v*v for v in disp)}
                labelled.append(w)
    by_root = [{"a":a, "b":b, "g":a*a+b*b, "n_brc":comb(a+b,a)}
               for a,b in product(a_values,b_values)]
    if len(paths) != 360 or sum(labelled) != 55560:
        raise AssertionError("signed-lift totals disagree")
    if not all(sum(abs(v) for v in d) == p["provenance"][4] +
               p["provenance"][5] for d,p in paths.items()):
        raise AssertionError("native step length mismatch")
    if not all(sum(v*v for v in d) == p["g"] for d,p in paths.items()):
        raise AssertionError("native square-norm mismatch")
    d1 = (5,3,0,0,0,0)
    d2 = (5,0,3,0,0,0)
    if d1 == d2 or d1 not in paths or d2 not in paths:
        raise AssertionError("same-chart/different-native-lift witness fails")
    origin = (0,0,0,0,0,0)
    if tuple(origin[t]+d1[t] for t in range(6)) == tuple(
        anchor[t]+d1[t] for t in range(6)):
        raise AssertionError("anchor witness fails")
    result = {
        "schema":"X6_HELLY_S12_SIGNED_BRC_UNIT54_CERTIFICATE_V1",
        "producer_blob_sha1":"6118b3bd04010e05355586d353c9cf0ec38b1070",
        "anchor":list(anchor), "a_values":list(a_values), "b_values":list(b_values),
        "selected_ordered_pair_count":15, "polarity_choices_per_pair":4,
        "positive_chart_points":len(by_root),
        "native_signed_labelled_lifts":len(labelled),
        "unique_native_displacements":len(paths),
        "positive_chart_total_n_brc":sum(v["n_brc"] for v in by_root),
        "signed_union_total_n_brc":sum(labelled),
        "by_root":by_root, "two_different_lifts_of_same_chart":[list(d1),list(d2)],
        "provenance_preserved":True,
    }
    serialized = json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["certificate_sha256"] = hashlib.sha256(serialized).hexdigest()
    return result

if __name__ == "__main__":
    outcome=calculate()
    print(json.dumps(outcome,indent=2,sort_keys=True,ensure_ascii=False))
    print("PASS_X6_HELLY_S12_SIGNED_BRC_LIFT_UNIT54")
