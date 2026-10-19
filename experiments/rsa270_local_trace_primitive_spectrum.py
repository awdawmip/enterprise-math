#!/usr/bin/env python3
"""
Verify that the packed local BRC trace has exactly the primitive odd character
support at conductor l^e.

Researcher-ID: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
import cmath
import math


def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root_prime_power(l, e):
    m = l ** e
    phi = (l - 1) * l ** (e - 1)
    pf = prime_factors(phi)
    for g in range(2, m):
        if math.gcd(g, m) == 1 and all(pow(g, phi // q, m) != 1 for q in pf):
            return g
    raise AssertionError("primitive root not found")


def ramanujan_prime_power(l, e, k):
    m = l ** e
    n = l ** (e - 1)
    k %= m
    if k == 0:
        return (l - 1) * n
    if k % n == 0:
        return -n
    return 0


def support_case(l, e, B=10):
    m = l ** e
    n = l ** (e - 1)
    phi = (l - 1) * n
    gen = primitive_root_prime_power(l, e)
    base = 1

    def G(x):
        return sum(
            (B ** j) * ramanujan_prime_power(l, e, x - (base + j * n))
            for j in range(l)
        )

    def H(x):
        return G(x) - G((-x) % m)

    units = []
    dlog = {}
    x = 1
    for a in range(phi):
        units.append(x)
        dlog[x] = a
        x = (x * gen) % m
    assert len(units) == phi

    z = cmath.exp(2j * math.pi / phi)
    transforms = []
    for k in range(phi):
        val = sum(H(x) * (z ** (-k * dlog[x])) for x in units)
        transforms.append(val)

    scale = max(abs(v) for v in transforms)
    observed = {
        k for k, v in enumerate(transforms)
        if abs(v) > max(1.0, scale) * 1e-9
    }

    # Character chi_k(generator)=z^k.
    # chi_k is odd iff k odd.
    # It is nontrivial on the reduction kernel iff l does not divide k.
    predicted = {k for k in range(phi) if k % 2 == 1 and k % l != 0}

    assert observed == predicted, (l, e, observed ^ predicted)

    expected_count = ((l - 1) ** 2 * l ** (e - 2)) // 2
    assert len(observed) == expected_count
    return expected_count


def main():
    rows = []
    for l in (3, 5, 7, 11):
        for e in (2, 3):
            count = support_case(l, e)
            rows.append((l, e, count))
            print(f"l={l} e={e}: support={count} PASS")
    assert len(rows) == 8
    print("ALL PASS")


if __name__ == "__main__":
    main()
