#!/usr/bin/env python3
"""R103 exact integer reproducibility check; standard library only."""
from itertools import product
from fractions import Fraction
import json

S = (10, -5, 1)
B = (26, -11, 2)
C = (36, -16, 3)
T_VALUES = (1, 10, 11, 12, 25, 100)
P_VALUES = (11, 27, 28, 38, 39, 40, 45)
MAX_PORT = max(P_VALUES)


def port(a):
    return max(sum(max(t, 0) for t in a), sum(max(-t, 0) for t in a))


def is_canonical(a):
    return next((v > 0 for v in a if v != 0), False)


def expected_ties(t, p):
    if t < 11:
        return {S}
    if t == 11:
        return {S} | ({B} if p >= 28 else set()) | ({C} if p >= 39 else set())
    return {C} if p >= 39 else {S} | ({B} if p >= 28 else set())


def enumerate_lattice():
    rows = []
    for a in product(range(-MAX_PORT, MAX_PORT + 1), repeat=3):
        if not is_canonical(a):
            continue
        q = port(a)
        if q > MAX_PORT:
            continue
        x, y, z = a
        u, v, h = x + 3*y + 6*z, 3*x + 12*y + 30*z, 7*x + 39*y + 126*z
        m = max(abs(u), abs(v), abs(h))
        d = max(abs(v-u), abs(h-u), abs(h-v))
        rows.append((q, a, m, d))
    return rows


def main():
    rows = enumerate_lattice()
    assert len(rows) == 157020, len(rows)
    checks = []
    for t in T_VALUES:
        for p in P_VALUES:
            denominator = 2 * (t + 1)
            candidates = [(max(2*m, (t+1)*d), a) for q, a, m, d in rows if q <= p]
            best_numerator = min(n for n, a in candidates)
            actual = {a for n, a in candidates if n == best_numerator}
            expected_num = 12 if p >= 39 and t > 11 else t + 1
            assert best_numerator == expected_num, (t, p, best_numerator, expected_num)
            assert actual == expected_ties(t, p), (t, p, actual, expected_ties(t, p))
            checks.append({
                "T": t, "p": p,
                "optimal": f"{Fraction(best_numerator, denominator)}",
                "tie_count": len(actual),
            })
    summary = {
        "schema": "X6_R103_EXACT_INTEGER_AUTHOR_CHECK_V1",
        "status": "PASS",
        "unoriented_lattice_vectors_q_le_45": len(rows),
        "parameter_port_pairs": len(checks),
        "T_values": list(T_VALUES),
        "p_values": list(P_VALUES),
        "exact_arithmetic": "integer numerator 2(T+1)F; no floating point",
        "verification_scope": "Complete q<=45 lattice, 42 selected integral T/p pairs",
        "not_independent_review": True,
        "examples": [record for record in checks if record["p"] in (28, 39)],
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
