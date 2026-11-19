#!/usr/bin/env python3
"""Independent exact census of frozen WBRC-T56 test fixture, not original module execution."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
import json

# Original source: test_brc_newton_fiber_quotient_foundation.py:23-33
# theta=1/2, multiplicity=2:
# A1,A2 -> (1,1); B1,B2 -> (1,0); C -> (1/2,0); D -> (1/2,1)
FIBERS = ((0, 1), (2, 3), (4,), (5,))

def check(condition, label):
    if not condition:
        raise ArithmeticError("Unit155 exact check failed: " + label)

def full(x):
    return tuple(sum(x[j] for j in fiber) for fiber in FIBERS)

def edge(x):
    return full(x)[:2]

def transfer(x, anchor, moved, amount):
    y = list(map(Fraction, x))
    y[anchor] -= amount
    y[moved] += amount
    return tuple(y)

def census(values):
    signatures, edge_signatures = Counter(), Counter()
    total = 0
    for state in product(values, repeat=6):
        total += 1
        f, e = full(state), edge(state)
        check(f[:2] == e, "edge projection")
        signatures[f] += 1
        edge_signatures[e] += 1
    return {"states": total, "full_signatures": len(signatures),
            "edge_signatures": len(edge_signatures),
            "full_equal_ordered_pairs": sum(n*n for n in signatures.values()),
            "edge_equal_ordered_pairs": sum(n*n for n in edge_signatures.values())}

def main():
    positive = census((0, 1, 2))
    signed = census((-1, 0, 1))
    expected = {"states": 729, "full_signatures": 225, "edge_signatures": 25,
                "full_equal_ordered_pairs": 3249, "edge_equal_ordered_pairs": 29241}
    check(positive == expected and signed == expected, "census")
    transfer_checks = 0
    for x in product((-1, 0, 1), repeat=6):
        for anchor, moved in ((0, 1), (2, 3)):
            y = transfer(x, anchor, moved, Fraction(2, 3))
            check(full(x) == full(y) and edge(x) == edge(y), "fractional transfer")
            transfer_checks += 1
    check(transfer_checks == 1458, "transfer count")
    check(full((1,-1,0,0,0,0)) == (0,0,0,0), "signed cancellation")
    check(full((0,0,0,0,1,0)) == (0,0,1,0), "full C observation")
    check(edge((0,0,0,0,1,0)) == edge((0,)*6), "edge-only hidden C")
    check(full((1,0,0,0,0,0)) == full((0,1,0,0,0,0)), "label coalescence")
    check(all(full(x) != (0,0,0,0) or x == (0,)*6
              for x in product((0,1,2), repeat=6)), "positive zero reflection")
    return {
        "schema":"X6_UNIT155_EXACT_CENSUS_V1",
        "frozen_ref":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "frozen_implementation_blob":"f9db29609e74b8f2a7202a1f626a138eb716fa29",
        "frozen_test_blob":"2fc8a1dcee7710d3f3f2654a1cd9e19d51ea9cc1",
        "fibers":[list(x) for x in FIBERS],
        "full_Q_rank":4, "full_Q_kernel_dimension":2,
        "edge_Q_rank":2, "edge_Q_kernel_dimension":4,
        "positive_census":positive, "signed_census":signed,
        "exact_fractional_fiber_transfer_checks":transfer_checks,
        "tests_passed":True, "historical_module_executed":False,
        "original_R063_benchmark_executed":False
    }

if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, separators=(",", ":"), ensure_ascii=False))
