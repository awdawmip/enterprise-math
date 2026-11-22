#!/usr/bin/env python3
"""Exact rational verification of all eight p19 q9 valuation-one H012 witnesses."""
import json
from fractions import Fraction
from pathlib import Path

base = Path(__file__).resolve().parent
cert = json.loads((base / "T6_P19_Q9_ONEPOWER_H013_AUTHOR_CERT_20261122_2300.json").read_text())
assert cert["H012_survivor_count"] == len(cert["witnesses"]) == 8
assert sum(x["H012_support_disjoint"] for x in cert["splits"]) == 8
assert all(x["H013_support_disjoint"] == 0 for x in cert["splits"])
def smooth19(n):
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        while n % prime == 0:
            n //= prime
    return n == 1
def moment(ds, k):
    return sum((Fraction(d - 1, d) ** k for d in ds), Fraction(0))
gaps = []
for w in cert["witnesses"]:
    A, B = w["A"], w["B"]
    assert set(A).isdisjoint(B)
    assert all(d > 19 and d % 19 == 0 and smooth19(d // 19) for d in A + B)
    assert all(sum(d - 1 for d in ds) <= 2331 for ds in (A, B))
    def qsum(ds):
        return sum((d // 19) // 19 for d in ds)
    assert (qsum(A), qsum(B)) == tuple(w["split"])
    for k in (0, 1, 2):
        assert moment(A, k) == moment(B, k), (k, w)
    gap = moment(A, 3) - moment(B, 3)
    assert gap != 0 and str(gap) == w["H3"], (gap, w["H3"])
    gaps.append(abs(gap))
assert min(gaps) == Fraction(1, 2710237824)
print("PASS: 8 full-denominator exact rational H012 aliases; no H013; sharp |H3|=1/2710237824.")
