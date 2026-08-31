#!/usr/bin/env python3
"""Native Enterprise C3 shell/AP/recoalescence experiment.

Experimental/free-research utility. Uses only the standard library.

The tri-sector shell r has 3r labels. Its C3 orbit at side-offset t is
    B_r+t, B_r+t+r, B_r+t+2r,
where B_r = 3r(r-1)/2+1.
"""

from __future__ import annotations
import argparse
import math
import statistics


def sieve(nmax: int) -> bytearray:
    p = bytearray(b"\x01") * (nmax + 1)
    if nmax >= 0:
        p[0] = 0
    if nmax >= 1:
        p[1] = 0
    for q in range(2, math.isqrt(nmax) + 1):
        if p[q]:
            start = q * q
            p[start:nmax + 1:q] = b"\x00" * (((nmax - start) // q) + 1)
    return p


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def orbit_labels(r: int, t: int) -> tuple[int, int, int]:
    b = shell_base(r) + t
    return b, b + r, b + 2 * r


def midpoint_labels(r: int) -> tuple[int, int, int]:
    if r % 2:
        raise ValueError("midpoint requires even r")
    return orbit_labels(r, r // 2)


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def resonance_factor(r: int) -> float:
    z = 1.0
    for p in factor_distinct(r):
        if p > 3:
            z *= (p - 1) / (p - 3)
    return z


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def omega(p: int) -> int:
    if p <= 5:
        raise ValueError
    return 3 + 2 * legendre(-20, p) + legendre(-24, p)


def is_prime64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
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


def run(rmax: int, kmax: int) -> None:
    # Exact C3-orbit AP check.
    for r in range(1, min(rmax, 500) + 1):
        for t in range(r):
            a, b, c = orbit_labels(r, t)
            assert b - a == r and c - b == r

    prime = sieve(3 * rmax * (rmax + 1) // 2)
    rows = []
    bad_full = []
    midpoint_bad = []
    for r in range(1, rmax + 1):
        b = shell_base(r)
        cnt = 0
        for t in range(r):
            if prime[b + t] and prime[b + t + r] and prime[b + t + 2 * r]:
                cnt += 1
                if min(b + t, b + t + r, b + t + 2 * r) > 3 and r % 6:
                    bad_full.append((r, t))
        if r % 2 == 0:
            a, c0, z = midpoint_labels(r)
            if prime[a] and prime[c0] and prime[z] and r % 210:
                midpoint_bad.append(r)
        if r >= 30 and r % 6 == 0:
            scale = r / (math.log(1.5 * r * r) ** 3)
            rows.append((r, cnt, resonance_factor(r), cnt / scale))
    assert not bad_full
    assert not midpoint_bad

    # q mod 120 four-color root profile.
    color = {0: [], 2: [], 4: [], 6: []}
    for a in range(1, 120):
        if math.gcd(a, 120) != 1:
            continue
        q = None
        x = a
        while x < 10000:
            if x > 5 and is_prime64(x):
                q = x
                break
            x += 120
        assert q is not None
        color[omega(q)].append(a)
    assert all(len(v) == 8 for v in color.values())

    xs = [x[2] for x in rows]
    ys = [x[3] for x in rows]
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    corr = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(
        sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)
    )
    top = sorted(rows, key=lambda x: (x[1], x[0]), reverse=True)[:10]

    # Midpoint after the exact r=210k recoalescence.
    tri = 0
    first = []
    for k in range(1, kmax + 1):
        r = 210 * k
        a, b, c = midpoint_labels(r)
        assert a % 210 == b % 210 == c % 210 == 1
        if is_prime64(a) and is_prime64(b) and is_prime64(c):
            tri += 1
            if len(first) < 12:
                first.append(k)

    print(f"RMAX={rmax}")
    print(f"SHELL_RESONANCE_CORR={corr:.12f}")
    print("TOP_SHELLS=" + repr([(r, c) for r, c, _, _ in top]))
    print("ROOT_COLORS_MOD120=" + repr(color))
    print(f"KMAX={kmax}")
    print(f"MIDPOINT_TRIPLE_EVENTS={tri}")
    print("FIRST_K=" + repr(first))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--r-max", type=int, default=5000)
    ap.add_argument("--k-max", type=int, default=200000)
    args = ap.parse_args()
    run(args.r_max, args.k_max)
