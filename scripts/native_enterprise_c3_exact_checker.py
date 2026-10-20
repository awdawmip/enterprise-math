#!/usr/bin/env python3
"""Independent exact checker for the native Enterprise C3 prime-allocation lane.

Checks only finite/exact statements used by the current free-research packet.
No external packages are required.
"""

from __future__ import annotations

import math
from collections import defaultdict


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def label(r: int, t: int, sigma: int) -> int:
    return shell_base(r) + t + sigma * r


def coord_from_n(n: int):
    if n < 1:
        raise ValueError
    r = max(1, int((math.sqrt(1 + 8 * n / 3) - 1) / 2))
    while 3 * r * (r + 1) // 2 < n:
        r += 1
    while r > 1 and 3 * (r - 1) * r // 2 >= n:
        r -= 1
    j = n - shell_base(r)
    sigma, t = divmod(j, r)
    if sigma == 0:
        addr = (r - t, t, 0)
    elif sigma == 1:
        addr = (0, r - t, t)
    elif sigma == 2:
        addr = (t, 0, r - t)
    else:
        raise AssertionError((n, r, j, sigma, t))
    return r, t, sigma, addr


def ray_label(u: int, v: int, sigma: int, m: int) -> int:
    r = (u + v) * m
    return shell_base(r) + (sigma * (u + v) + v) * m


def saturated_gate(u: int, v: int, q: int) -> bool:
    return all(
        any(ray_label(u, v, sigma, m) % q == 0 for sigma in range(3))
        for m in range(1, q)
    )


def gcd_primitive_pairs(max_sum: int):
    for s in range(1, max_sum + 1):
        for u in range(s + 1):
            v = s - u
            if math.gcd(u, v) == 1:
                yield u, v


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


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def omega(q: int) -> int:
    return 3 + 2 * legendre(-20, q) + legendre(-24, q)


def sieve(nmax: int) -> bytearray:
    p = bytearray(b"\x01") * (nmax + 1)
    p[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(nmax) + 1):
        if p[q]:
            start = q * q
            p[start:nmax + 1:q] = b"\x00" * (((nmax - start) // q) + 1)
    return p


def main() -> None:
    # Coordinate bijection / roundtrip.
    for n in range(1, 100001):
        r, t, sigma, addr = coord_from_n(n)
        assert label(r, t, sigma) == n
        assert min(addr) == 0 and sum(addr) == r
        if sigma == 0:
            assert addr == (r - t, t, 0) and addr[0] > 0
        elif sigma == 1:
            assert addr == (0, r - t, t) and addr[1] > 0
        else:
            assert addr == (t, 0, r - t) and addr[2] > 0

    expected = {
        3: {(0,1),(0,2),(1,0),(1,1),(2,0),(2,2)},
        5: {(1,1),(2,2),(3,3),(4,4)},
        7: {(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)},
    }
    for q in (3,5,7):
        got = {
            (u,v)
            for u in range(q)
            for v in range(q)
            if saturated_gate(u,v,q)
        }
        assert got == expected[q], (q, got)

    max_gate = []
    for u, v in gcd_primitive_pairs(100):
        if all(saturated_gate(u, v, q) for q in (3,5,7)):
            max_gate.append((u + v, u, v))
            assert (u - v) % 35 == 0
            assert math.gcd(u * v, 35) == 1
            assert (u * v * (u - v)) % 3 == 0
    assert max_gate[0] == (2,1,1)
    assert max_gate[1:3] == [(37,1,36),(37,36,1)]

    colors = defaultdict(list)
    for residue in range(1,120):
        if math.gcd(residue,120) != 1:
            continue
        q = residue
        while not (q > 5 and is_prime64(q)):
            q += 120
        colors[omega(q)].append(residue)
    assert colors[0] == [13,17,19,37,71,91,113,119]
    assert colors[2] == [11,31,53,59,73,77,79,97]
    assert colors[4] == [23,41,43,47,61,67,89,109]
    assert colors[6] == [1,7,29,49,83,101,103,107]

    # Exact C3 shell census r<=5000.
    rmax = 5000
    prime = sieve(3 * rmax * (rmax + 1) // 2)
    total = 0
    counts = []
    for r in range(1, rmax + 1):
        b = shell_base(r)
        c = 0
        for t in range(r):
            a0 = b + t
            if prime[a0] and prime[a0 + r] and prime[a0 + 2 * r]:
                c += 1
                assert r % 6 == 0 or min(a0, a0+r, a0+2*r) <= 3
                center = a0 + r
                for q in (5,7,11,13,17,19,23,29):
                    if r % q:
                        z = center * pow(r, -1, q) % q
                        assert z not in {q-1,0,1}
        if c:
            counts.append((c,r))
        total += c
    assert total == 3919
    counts.sort(reverse=True)
    assert counts[0] == (27,4620)

    print("COORDINATE_ROUNDTRIP=PASS n<=100000")
    print("SMALL_GATE_CLASSIFICATION=PASS")
    print("MAX_GATE_MINIMUM=(1,1), NEXT=(1,36)/(36,1)")
    print("MOD120_FOUR_COLOR=PASS 8+8+8+8")
    print("PROJECTIVE_FORBIDDEN_SLOPES=PASS")
    print("FULL_C3_FIBERS_R5000=3919")
    print("HOTTEST_SHELL=4620:27")


if __name__ == "__main__":
    main()
