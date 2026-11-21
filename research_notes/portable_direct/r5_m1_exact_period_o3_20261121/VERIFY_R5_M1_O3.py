#!/usr/bin/env python3
"""Exact, dependency-free primitive-root pole audit of frozen R5 at m=1.

Frozen 101 prices 214..314 and original 5 failure-event incidences.
The threshold-one case uses genuine union intersections (all selected loads zero).
No floating point, numerical root approximation, or collapsed union-cap error.
"""
from math import comb, lcm
import json

PRICES = tuple(range(214, 315))
EVENTS = (
    frozenset(range(214, 219)),
    frozenset((214, 216, 217, 218, 219, 220, 221)),
    frozenset((215, 216, 217, 218, 219, 220, 221)),
    frozenset(range(223, 291)),
    frozenset(range(296, 313)),
)
MAX_TAYLOR = 5


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def exact_monic_division(f, g):
    f = f[:]
    out = [0] * (len(f) - len(g) + 1)
    while len(f) >= len(g):
        coeff = f[-1]
        k = len(f) - len(g)
        out[k] = coeff
        for j, x in enumerate(g):
            f[k + j] -= coeff * x
        while f and f[-1] == 0:
            f.pop()
    assert not f
    return out


def cyclotomic(n, cache={}):
    if n not in cache:
        f = [-1] + [0] * (n - 1) + [1]
        for d in divisors(n):
            if d < n:
                f = exact_monic_division(f, cyclotomic(d))
        cache[n] = f
    return cache[n]


def reduce_primitive(v, d):
    f = v[:]
    ph = cyclotomic(d)
    degree = len(ph) - 1
    for k in range(len(f) - 1, degree - 1, -1):
        c = f[k]
        if c:
            for j, a in enumerate(ph):
                f[k - degree + j] -= c * a
    return f[:degree]


def product_jets(prices, d, order):
    """Product (1-(z(1+t))^p) mod z^d-1 and t^(order+1)."""
    cur = [[0] * d for _ in range(order + 1)]
    cur[0][0] = 1
    for p in sorted(prices):
        nxt = [row[:] for row in cur]
        shift = p % d
        for j in range(order + 1):
            for a in range(j + 1):
                scale = comb(p, a)
                for r, v in enumerate(cur[j - a]):
                    if v:
                        nxt[j][(r + shift) % d] -= scale * v
        cur = nxt
    return cur


def add(a, b, scale=1):
    return [[x + scale * y for x, y in zip(u, v)] for u, v in zip(a, b)]


def multiply(a, b, d, order):
    out = [[0] * d for _ in range(order + 1)]
    for i in range(order + 1):
        for j in range(order + 1 - i):
            for x, ax in enumerate(a[i]):
                if ax:
                    for y, by in enumerate(b[j]):
                        if by:
                            out[i + j][(x + y) % d] += ax * by
    return out


def direct_numerator_jets(d, order):
    """All 31 genuine intersections, without group simplification."""
    out = [[0] * d for _ in range(order + 1)]
    for mask in range(1, 32):
        U = set().union(*(EVENTS[i] for i in range(5) if mask & (1 << i)))
        out = add(out, product_jets(U, d, order), 1 if mask.bit_count() % 2 else -1)
    return out


def grouped_numerator_jets(d, order):
    """R=1-(1-R_A)(1-W3)(1-W4), supports disjoint by construction."""
    A = [[0] * d for _ in range(order + 1)]
    for mask in range(1, 8):
        U = set().union(*(EVENTS[i] for i in range(3) if mask & (1 << i)))
        A = add(A, product_jets(U, d, order), 1 if mask.bit_count() % 2 else -1)
    B = product_jets(EVENTS[3], d, order)
    C = product_jets(EVENTS[4], d, order)
    AB = multiply(A, B, d, order)
    AC = multiply(A, C, d, order)
    BC = multiply(B, C, d, order)
    ABC = multiply(AB, C, d, order)
    return add(add(add(add(add(add(A, B), C), AB, -1), AC, -1), BC, -1), ABC)


def verify():
    rows = []
    active = []
    for d in range(1, 26):
        k = sum(p % d == 0 for p in PRICES)
        if k < 5:
            continue
        direct = direct_numerator_jets(d, MAX_TAYLOR)
        grouped = grouped_numerator_jets(d, MAX_TAYLOR)
        assert direct == grouped, (d, "independent inclusion-exclusion failure")
        cyclotomic_jets = [reduce_primitive(c, d) for c in direct]
        nonzero = [j for j, c in enumerate(cyclotomic_jets) if any(c)]
        assert nonzero, (d, "increase exact derivative bound")
        nu = nonzero[0]
        pole = k - nu
        rows.append({"d": d, "k": k, "nu": nu, "pole": pole,
                     "leading_coefficient_cyclotomic_basis": cyclotomic_jets[nu]})
        if pole >= 5:
            active.append(d)
    # Five multiples for d>=26 would span 4d>=104, outside 214..314.
    assert all(sum(p % d == 0 for p in PRICES) <= 4 for d in range(26, 315))
    assert lcm(*[r["d"] for r in rows if r["pole"] >= 6]) == 12252240
    assert active == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]
    M = lcm(*active)
    assert M == 232792560
    assert next(r for r in rows if r["d"] == 19)["leading_coefficient_cyclotomic_basis"] == [6, 7, 10, 12, 13, 10, 11, 2, 0, -6, -8, -18, -14, -17, -14, -14, -10, -8]
    assert next(r for r in rows if r["d"] == 24)["nu"] == 1
    return {"schema": "R5_M1_EXACT_MINIMAL_PERIOD_O_N3_V1",
            "frozen_prices": [214, 314],
            "threshold": 1, "target_error": "O(N^3)",
            "verified_methods": ["31-mask direct genuine intersection",
                                 "A/E3/E4 disjoint factorization"],
            "cyclotomic_arithmetic": "exact integer Z[z]/Phi_d(z)",
            "rows": rows, "active_root_orders": active,
            "comparison_O_N4_min_period": 12252240,
            "min_period_O_N3": M,
            "result": "PASS", "independent_review": "NOT_REVIEWED"}


if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
