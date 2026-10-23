#!/usr/bin/env python3
"""Exact BRC Hall predecessor counterexample verifier; stdlib only."""
from fractions import Fraction
import json

W = (1, 1, 4)
DEN = sum(W)
EDGES = ((0, 1), (0, 2), (1, 2))
DEG = tuple(sum(i in e for e in EDGES) for i in range(3))

def occupancy_formula(n):
    if n == 0:
        return Fraction(0)
    return sum(Fraction((W[i] + W[j]) ** n - W[i] ** n - W[j] ** n, DEN ** n)
               for i, j in EDGES)

def occupancy_independent_mask(n):
    states = {0: Fraction(1)}
    for _ in range(n):
        nxt = {}
        for mask, mass in states.items():
            for i, w in enumerate(W):
                newmask = mask | (1 << i)
                nxt[newmask] = nxt.get(newmask, Fraction(0)) + mass * Fraction(w, DEN)
        states = nxt
    return sum(mass for mask, mass in states.items()
               if mask.bit_count() == 2 and
               tuple(i for i in range(3) if mask & (1 << i)) in EDGES)

def hall_margins_scaled(n):
    demands = [DEG[i] * (DEN - W[i]) * W[i] ** n for i in range(3)]
    capacities = [(DEN - W[i] - W[j]) * (W[i] + W[j]) ** n for i, j in EDGES]
    margins = [
        sum(capacities[eidx] for eidx, (i, j) in enumerate(EDGES)
            if mask & ((1 << i) | (1 << j)))
        - sum(demands[i] for i in range(3) if mask & (1 << i))
        for mask in range(1, 8)
    ]
    return demands, capacities, margins

def F(n):
    return 5 ** n + 2 ** (n + 1) - 2 * 4 ** n - 10

def verify():
    for n in range(0, 11):
        assert occupancy_formula(n) == occupancy_independent_mask(n)
    assert occupancy_formula(2) == Fraction(1, 2)
    assert occupancy_formula(3) == Fraction(7, 12)
    assert occupancy_formula(4) == Fraction(125, 216)
    assert occupancy_formula(3) - occupancy_formula(2) == Fraction(1, 12)
    assert occupancy_formula(4) - occupancy_formula(3) == -Fraction(1, 216)
    d3, c3, h3 = hall_margins_scaled(3)
    d4, c4, h4 = hall_margins_scaled(4)
    assert d3 == [10, 10, 256] and c3 == [32, 125, 125]
    assert h3 == [147, 147, 262, -6, 16, 16, 6]
    assert d4 == [10, 10, 1024] and c4 == [64, 625, 625]
    assert h4 == [679, 679, 1294, 226, 280, 280, 270]
    for n in range(3, 81):
        assert F(n) > 0
        assert F(n + 1) - 4 * F(n) == 5 ** n - 4 * 2 ** n + 30
        assert occupancy_formula(n + 1) - occupancy_formula(n) == Fraction(-F(n), 3 * 6 ** n)
        assert min(hall_margins_scaled(n + 1)[2]) > 0
    return {
        "schema": "EM_BRC_HALL_PREDECESSOR_EXACT_EVIDENCE_V1",
        "model": {"weights": list(W), "denominator": DEN,
                  "good_edges": [list(e) for e in EDGES], "one_action": True},
        "delta": {str(n): str(occupancy_formula(n)) for n in range(2, 5)},
        "delta_3_to_4": "-1/216",
        "hall_3": {"denominator": 6 ** 4, "demands": d3,
                   "capacities": c3, "margins_mask_1_to_7": h3},
        "hall_4": {"denominator": 6 ** 5, "demands": d4,
                   "capacities": c4, "margins_mask_1_to_7": h4},
        "independent_mask_crosscheck_n": [0, 10],
        "exponential_identity_exact_check_n": [3, 80],
        "arithmetic": "exact integer and Fraction",
        "review": "AUTHOR_SIDE_ONLY_NOT_ADMITTED"
    }

if __name__ == "__main__":
    print(json.dumps(verify(), sort_keys=True, indent=2, ensure_ascii=False))
