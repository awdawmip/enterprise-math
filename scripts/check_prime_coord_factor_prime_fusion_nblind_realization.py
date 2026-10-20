#!/usr/bin/env python3
"""PCF6 exact checker: public N-only ambient profile + external factor verifier.

The public_worker() interface consumes only the unfactored modulus H.
Hidden factors are used only by external_verify_pair(), which checks theorem
claims against a proof-side oracle and is never called by public_worker().
"""
from __future__ import annotations

from collections import Counter
from math import gcd, isqrt

T = (
    (0, 0, 0, -1),
    (1, 0, 0, -1),
    (0, 1, 0, -2),
    (0, 0, 1, -1),
)
I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))


def mat_mul(a, b):
    n, m, k = len(a), len(b[0]), len(b)
    return tuple(
        tuple(sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m))
        for i in range(n)
    )


def mat_pow(a, n):
    out = I4
    base = a
    while n:
        if n & 1:
            out = mat_mul(out, base)
        base = mat_mul(base, base)
        n >>= 1
    return out


def mat_sub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def det_bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def public_worker(H: int):
    """N-only profile. No factor argument, factor oracle, or adaptive branch."""
    if H <= 1 or gcd(H, 6) != 1:
        raise ValueError("public theorem-domain checker requires H>1 and gcd(H,6)=1")
    assert mat_pow(T, 12) == I4
    dets = tuple(det_bareiss(mat_sub(mat_pow(T, k), I4)) for k in range(1, 13))
    expected = tuple(
        0 if (k % 3 == 0 or k % 4 == 0) else (6 if k % 2 else 12)
        for k in range(1, 13)
    )
    assert tuple(abs(d) for d in dets) == expected
    gcd_profile = tuple(gcd(H, d) for d in dets)
    expected_gcd = tuple(H if d == 0 else 1 for d in expected)
    assert gcd_profile == expected_gcd
    return {"period": 12, "det_abs": expected, "gcd_profile": gcd_profile}


def is_prime(n: int) -> bool:
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


def roots_mod_prime(poly, p):
    return [x for x in range(p) if poly(x) % p == 0]


def crt_pair(a, p, b, q):
    return (a + p * (((b - a) * pow(p, -1, q)) % q)) % (p * q)


def external_verify_pair(p: int, q: int):
    """Proof-side verifier. p,q are deliberately confined to this compartment."""
    assert p != q and p > 3 and q > 3 and is_prime(p) and is_prime(q)
    assert p % 4 == 1 and q % 3 == 1
    H = p * q

    # Selector c is 0 mod p and 1 mod q.
    c = (p * pow(p, -1, q)) % H
    assert c % p == 0 and c % q == 1 and (c * c - c) % H == 0
    assert gcd(c, H) == p and gcd(c - 1, H) == q

    # A rank-2 mixed operator with charpoly X^2+cX+1 has trace -c.
    T2 = ((0, -1), (1, -c))
    trace = T2[0][0] + T2[1][1]
    assert (-trace) % H == c
    assert gcd((-trace) % H, H) == p

    fp = roots_mod_prime(lambda x: x * x + 1, p)
    gp = roots_mod_prime(lambda x: x * x + x + 1, p)
    fq = roots_mod_prime(lambda x: x * x + 1, q)
    gq = roots_mod_prime(lambda x: x * x + x + 1, q)
    assert len(fp) == 2 and len(gq) == 2

    mixed = sorted(crt_pair(a, p, b, q) for a in fp for b in gq)
    h_roots = sorted(x for x in mixed if (x * x + c * x + 1) % H == 0)
    assert h_roots == mixed and len(mixed) == 4

    full_count = (len(fp) + len(gp)) * (len(fq) + len(gq))
    predicted = 4 * (1 + int(p % 3 == 1)) * (1 + int(q % 4 == 1))
    assert full_count == predicted

    for x in mixed:
        assert (x * x + 1) % p == 0
        assert (x * x + x + 1) % q == 0
        assert pow(x, 6, p) == p - 1
        assert pow(x, 6, q) == 1
        assert gcd(H, pow(x, 6, H) + 1) == p
        assert gcd(H, (pow(x, 6, H) - 1) % H) == q

    public_worker(H)  # public compartment receives H only.
    return full_count


def main():
    # Integral Bezout identity: (X+1)(X^2+1)-X(X^2+X+1)=1.
    for x in range(-20, 21):
        assert (x + 1) * (x * x + 1) - x * (x * x + x + 1) == 1

    # Pressure guard H=91.
    p, q, H = 13, 7, 91
    c = (p * pow(p, -1, q)) % H
    assert c == 78
    mixed = [x for x in range(H) if (x * x + 1) % p == 0 and (x * x + x + 1) % q == 0]
    full = [x for x in range(H) if ((x * x + 1) * (x * x + x + 1)) % H == 0]
    hroots = [x for x in range(H) if (x * x + c * x + 1) % H == 0]
    assert mixed == [18, 44, 60, 86]
    assert hroots == mixed
    assert full == [9, 16, 18, 44, 60, 74, 81, 86]

    primes = [n for n in range(5, 300) if is_prime(n)]
    pairs = []
    classes = Counter()
    for p in primes:
        if p % 4 != 1:
            continue
        for q in primes:
            if q == p or q % 3 != 1:
                continue
            # Source T9-compatible branch only.
            if not ((p % 8 == 1 and q % 12 == 1) or (p % 8 == 5 and q % 12 == 7)):
                continue
            classes[external_verify_pair(p, q)] += 1
            pairs.append((p, q))
    assert len(pairs) == 412
    assert classes == Counter({4: 144, 8: 224, 16: 44})
    print(
        "PCF6_CHECK_PASS "
        f"source_pairs={len(pairs)} public_profiles={len(pairs)} selectors={len(pairs)} "
        f"root_classes=4:{classes[4]},8:{classes[8]},16:{classes[16]} "
        "pressure=PASS trace_split=PASS ambient_sync=PASS"
    )


if __name__ == "__main__":
    main()
