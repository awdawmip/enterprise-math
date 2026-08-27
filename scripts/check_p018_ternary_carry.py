#!/usr/bin/env python3
"""Finite exact regression for the P018 quotient-root ternary carry formula.

Regression only: the general theorem is proved in Lean.
"""
from __future__ import annotations

from math import isqrt


def iroot(k: int, n: int) -> int:
    assert k >= 1 and n >= 0
    if k == 1:
        return n
    if n < 2:
        return n
    lo, hi = 0, 1
    while hi**k <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def check(s: int, n: int) -> tuple[bool, dict[str, int]]:
    r = s + 1
    H = iroot(s + 2, (s + 1) * n - 1)
    X = (H + 1) ** r
    Y = H**r
    D = n // X
    q = H // r
    A = max(q * X, (q + 1) * Y)
    B = (q + 1) * X
    tau = 0 if n < A else (1 if n < B else 2)
    states = {iroot(r, n // d) for d in range(1, n + 1)}
    lhs = len(states) + 1
    binary = D + H + (1 if (D + 1) * Y <= n else 0)
    ternary = H + q + tau
    return lhs == binary == ternary, {
        "s": s, "n": n, "H": H, "D": D, "q": q,
        "tau": tau, "lhs": lhs, "binary": binary, "ternary": ternary,
    }


def main() -> None:
    cases = 0
    for s in range(0, 8):
        for n in range(1, 2500):
            ok, row = check(s, n)
            cases += 1
            if not ok:
                raise SystemExit(f"FAIL {row}")
    print(f"PASS cases={cases} s=0..7 n=1..2499")


if __name__ == "__main__":
    main()
