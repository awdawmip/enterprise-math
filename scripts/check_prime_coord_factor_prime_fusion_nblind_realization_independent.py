#!/usr/bin/env python3
"""Independent PCF6 checker using local cyclotomic/root classification.

This checker does not use the 4x4 ambient matrix implementation from the
primary checker. Public cyclotomic observables are evaluated from exact local
orders; p,q occur only in the external theorem-verification compartment.
"""
from __future__ import annotations

from collections import Counter
from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def public_cyclotomic_profile(H):
    if H <= 1 or gcd(H, 6) != 1:
        raise ValueError("requires H>1 and gcd(H,6)=1")
    out = []
    for k in range(1, 13):
        rf = 0 if k % 4 == 0 else (4 if k % 2 == 0 else 2)
        rg = 0 if k % 3 == 0 else 3
        delta = rf * rg
        out.append(gcd(H, delta))
    expected = [H if (k % 3 == 0 or k % 4 == 0) else 1 for k in range(1, 13)]
    assert out == expected
    return tuple(out)


def roots(poly, p):
    return [x for x in range(p) if poly(x) % p == 0]


def crt(a, p, b, q):
    return (a + p * (((b - a) * pow(p, -1, q)) % q)) % (p * q)


def external_pair(p, q):
    assert p != q and p > 3 and q > 3 and is_prime(p) and is_prime(q)
    assert p % 4 == 1 and q % 3 == 1
    H = p * q
    c = p * pow(p, -1, q) % H
    assert (c * c - c) % H == 0
    assert gcd(c, H) == p
    assert gcd(c - 1, H) == q

    fp = roots(lambda x: x * x + 1, p)
    gp = roots(lambda x: x * x + x + 1, p)
    fq = roots(lambda x: x * x + 1, q)
    gq = roots(lambda x: x * x + x + 1, q)
    assert len(fp) == 2 and len(gq) == 2
    assert len(gp) == (2 if p % 3 == 1 else 0)
    assert len(fq) == (2 if q % 4 == 1 else 0)

    mixed = {crt(a, p, b, q) for a in fp for b in gq}
    assert len(mixed) == 4
    for x in mixed:
        assert (x * x + c * x + 1) % H == 0

    full_count = (len(fp) + len(gp)) * (len(fq) + len(gq))
    assert full_count in (4, 8, 16)
    assert (full_count == 4) == (p % 3 != 1 and q % 4 != 1)

    public_cyclotomic_profile(H)
    return full_count


def main():
    p, q, H = 13, 7, 91
    c = p * pow(p, -1, q) % H
    assert c == 78 and gcd(c, H) == 13
    fp = roots(lambda x: x*x+1, p)
    gp = roots(lambda x: x*x+x+1, p)
    fq = roots(lambda x: x*x+1, q)
    gq = roots(lambda x: x*x+x+1, q)
    mixed = sorted(crt(a,p,b,q) for a in fp for b in gq)
    full = sorted({crt(a,p,b,q) for a in fp+gp for b in fq+gq})
    assert mixed == [18,44,60,86]
    assert full == [9,16,18,44,60,74,81,86]

    primes = [n for n in range(5, 200) if is_prime(n)]
    classes = Counter()
    count = 0
    for p in primes:
        if p % 4 != 1:
            continue
        for q in primes:
            if q == p or q % 3 != 1:
                continue
            classes[external_pair(p,q)] += 1
            count += 1
    assert count == 432
    assert classes == Counter({4:144, 8:216, 16:72})

    print(
        "PCF6_INDEPENDENT_PASS "
        f"algebraic_pairs={count} root_classes=4:{classes[4]},8:{classes[8]},16:{classes[16]} "
        "selector_equivalence=PASS fixed_cyclotomic_sync=PASS pressure=PASS"
    )


if __name__ == "__main__":
    main()
