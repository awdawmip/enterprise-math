"""Exact-integer explorer for R007 scale/collapse descent.

No floating-point root is used.  This module is research evidence, not a stable API.
"""

from __future__ import annotations

from math import comb


def floor_root(n: int, p: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    if p < 1:
        raise ValueError("p must be positive")
    if n < 2 or p == 1:
        return n
    lo, hi = 0, 1
    while hi**p <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def collapse(n: int, p: int) -> int:
    k = floor_root(n, p)
    return k**p


def q(n: int, r: int) -> int:
    if r < 1:
        raise ValueError("r must be positive")
    return n // r


def unsafe_witness(p: int, r: int, t: int = 1) -> tuple[int, int]:
    if p < 2 or r < 2 or t < 1:
        raise ValueError("require p,r >= 2 and t >= 1")
    y = (t * r + 1) ** p
    return y - 1, y


def coarse_future_defect(p: int, r: int, t: int = 1) -> int:
    x, y = unsafe_witness(p, r, t)
    return q(collapse(y, p), r) - q(collapse(x, p), r)


def defect_polynomial(p: int, r: int, t: int = 1) -> int:
    return sum(comb(p, i) * (t**i) * (r ** (i - 1)) for i in range(1, p))


def repair_bit(n: int, p: int, r: int) -> int:
    return int(q(collapse(n, p), r) == q(n, r))


def repair_future_from_bit(a: int, beta: int, p: int, r: int) -> int:
    if beta not in (0, 1):
        raise ValueError("beta must be 0 or 1")
    if beta:
        return a
    return q(collapse(a * r, p), r)


def fiber_repair_values(a: int, p: int, r: int) -> set[int]:
    return {q(collapse(n, p), r) for n in range(a * r, (a + 1) * r)}


def fiber_needs_repair(a: int, p: int, r: int) -> bool:
    left = a * r
    k = floor_root(left, p)
    if k**p == left:
        return False
    next_power = (k + 1) ** p
    return next_power < (a + 1) * r


def projection(m: int, e: int, d: int) -> int:
    if e % d:
        raise ValueError("d must divide e")
    return m // (e // d)


def relative_lift(m: int, d: int, p: int) -> int:
    """F_d^H for H=C_p: d * C_p(floor(m/d))."""
    return d * collapse(m // d, p)


def root_induced_on_q(a: int, p: int, r: int) -> int:
    return floor_root(a // (r ** (p - 1)), p)


def self_check() -> dict[str, int]:
    witness_cases = 0
    fiber_cases = 0
    naturality_cases = 0
    erasure_cases = 0
    root_safe_cases = 0

    for p in range(2, 7):
        for r in range(2, 20):
            for t in range(1, 20):
                x, y = unsafe_witness(p, r, t)
                assert q(x, r) == q(y, r)
                assert q(collapse(x, p), r) != q(collapse(y, p), r)
                assert coarse_future_defect(p, r, t) == defect_polynomial(p, r, t)
                witness_cases += 1

                z = (t * r) ** p
                a = z // r
                repaired = {
                    (q(n, r), q(collapse(n, p), r))
                    for n in range(z, z + r)
                }
                assert len(repaired) == 1
                assert len(range(z, z + r)) == r
                erasure_cases += 1

    for p in range(2, 6):
        for r in range(2, 50):
            for a in range(0, 500):
                values = fiber_repair_values(a, p, r)
                assert len(values) <= 2
                assert (len(values) == 2) == fiber_needs_repair(a, p, r)
                for n in range(a * r, (a + 1) * r):
                    beta = repair_bit(n, p, r)
                    assert repair_future_from_bit(a, beta, p, r) == q(collapse(n, p), r)
                fiber_cases += 1

    for p in range(2, 6):
        for d in range(1, 10):
            for ratio in range(1, 10):
                e = d * ratio
                for m in range(0, 1000, 17):
                    lhs = projection(relative_lift(m, e, p), e, d)
                    rhs = relative_lift(projection(m, e, d), d, p)
                    assert lhs == rhs
                    assert relative_lift(relative_lift(m, d, p), d, p) == relative_lift(m, d, p)
                    assert relative_lift(m, d, p) <= m
                    naturality_cases += 1

    for p in range(1, 6):
        for r in range(2, 20):
            for n in range(0, 2000, 13):
                lhs = q(floor_root(n, p), r)
                rhs = root_induced_on_q(q(n, r), p, r)
                assert lhs == rhs
                root_safe_cases += 1

    return {
        "witness_cases": witness_cases,
        "fiber_cases": fiber_cases,
        "naturality_cases": naturality_cases,
        "erasure_cases": erasure_cases,
        "root_safe_cases": root_safe_cases,
    }


if __name__ == "__main__":
    print(self_check())
