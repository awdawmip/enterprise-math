#!/usr/bin/env python3
"""Deterministic checks for the native Enterprise C3 shell-residue basin.

Standard library only.  The deep U(210) scan is enabled with --k-max 50000.
"""

from __future__ import annotations

import argparse
import math
import statistics


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def center(r: int, t: int) -> int:
    return shell_base(r) + t + r


def shell_residue(r: int, t: int) -> int:
    return center(r, t) % r


def phi(n: int) -> int:
    out, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            out -= out // p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out -= out // x
    return out


def is_prime64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_upto(n: int) -> list[int]:
    mark = bytearray(b"\x01") * (n + 1)
    mark[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if mark[p]:
            mark[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if mark[i]]


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    z = pow(a, (q - 1) // 2, q)
    return -1 if z == q - 1 else 1


def omega_u(q: int, u: int) -> int:
    if u % q == 0:
        return 3
    return 3 + 2 * legendre(1 - 6*u, q) + legendre(-6*u, q)


def unit_fiber(r: int, u: int) -> tuple[int, int, int]:
    if r % 2:
        raise ValueError("U210 scan uses even shells")
    t = (u - r // 2 - 1) % r
    c = center(r, t)
    assert c % r == u % r
    return c - r, c, c + r


def finite_score(u: int, qmax: int) -> float:
    log_s = 0.0
    for q in primes_upto(qmax):
        if q <= 7:
            continue
        w = omega_u(q, u)
        log_s += math.log((1 - w/q) / ((1 - 1/q) ** 3))
    return math.exp(log_s)


def pearson(xs: list[float], ys: list[float]) -> float:
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    den = math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))
    return num / den


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k-max", type=int, default=10000)
    ap.add_argument("--q-max", type=int, default=5000)
    args = ap.parse_args()

    # Exact shell-residue / totient / identity checks.
    for r in range(1, 2001):
        residues = [shell_residue(r, t) for t in range(r)]
        assert sorted(residues) == list(range(r))
        primitive = sum(math.gcd(shell_residue(r, t), r) == 1 for t in range(r))
        assert primitive == phi(r)
        id_t = next(t for t in range(r) if shell_residue(r, t) == 1 % r)
        if r > 1 and r % 2:
            assert id_t == 0
        if r % 2 == 0:
            assert id_t == r // 2
            c = center(r, id_t)
            assert (c-r) % r == c % r == (c+r) % r == 1 % r

    units = [u for u in range(1, 210) if math.gcd(u, 210) == 1]
    assert len(units) == 48

    counts = {u: 0 for u in units}
    for k in range(2, args.k_max + 1):
        r = 210 * k
        for u in units:
            if all(is_prime64(x) for x in unit_fiber(r, u)):
                counts[u] += 1

    scores = {u: finite_score(u, args.q_max) for u in units}
    corr = pearson([math.log(scores[u]) for u in units], [counts[u] for u in units])
    rank = sorted(units, key=lambda u: counts[u], reverse=True)
    score_rank = sorted(units, key=lambda u: scores[u], reverse=True)

    print("SHELL_RESIDUE_BIJECTION=PASS r<=2000")
    print("PRIMITIVE_FIBER_COUNT=phi(r) PASS r<=2000")
    print("IDENTITY_PARITY_AXIS_BISECTOR=PASS")
    print(f"K_MAX={args.k_max} Q_MAX={args.q_max}")
    print("COUNT_RANK_TOP10=" + ",".join(f"{u}:{counts[u]}" for u in rank[:10]))
    print("LOCAL_SCORE_TOP10=" + ",".join(f"{u}:{scores[u]:.9f}" for u in score_rank[:10]))
    print(f"LOG_SCORE_COUNT_CORRELATION={corr:.12f}")

    if args.k_max == 50000 and args.q_max == 5000:
        expected = [131, 103, 101, 1]
        assert rank[:4] == expected, rank[:4]
        assert [counts[u] for u in expected] == [395, 309, 271, 258]
        assert abs(corr - 0.9569418125338793) < 1e-12
        print("DEEP_FROZEN_CENSUS=PASS")


if __name__ == "__main__":
    main()
