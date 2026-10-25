#!/usr/bin/env python3
"""Exact author-side checks for original W_p forward/reverse reciprocal pairing.

Not a native CM/divided-power experiment or formal independent review.
"""
from math import isqrt


def primes_1mod6(limit):
    for p in range(7, limit):
        if p % 6 != 1:
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def certify(p):
    assert p >= 7 and p % 6 == 1
    m = (p - 1) // 6
    fac = [1] * p
    for i in range(1, p):
        fac[i] = fac[i - 1] * i % p
    invfac = [1] * p
    invfac[-1] = pow(fac[-1], -1, p)
    for i in range(p - 1, 0, -1):
        invfac[i - 1] = invfac[i] * i % p

    source_prefactor = fac[2*m] * fac[3*m] * fac[4*m] % p
    source_prefactor = source_prefactor * (-1 if m % 2 else 1) * pow(9, -1, p) % p

    def source_tail(n):
        assert 4*m < n <= 6*m
        return ((source_prefactor * (6*n + 1) *
                 fac[n-1-2*m] * fac[n-1-3*m] * fac[n-1-4*m] *
                 invfac[n]**3 * pow(2, -n, p)) % p)

    A = 1
    reverse = 5
    total_tail = total_mirror = 0
    for k in range(2*m):
        e = source_tail(6*m-k)
        assert e == reverse, (p, k, "reverse kernel")
        delta = (2*k+1)*(3*k+1)*(3*k+2) % p
        phi = 2*(6*k+5)*pow(delta, -1, p) % p
        assert e*A % p == phi, (p, k, "cross-band product")
        mirror = phi * pow(A, -1, p) % p
        assert mirror == e
        total_tail = (total_tail + e) % p
        total_mirror = (total_mirror + mirror) % p
        if k == 0:
            assert e == 5
        if k == m:
            assert e*A % p == 16 % p, (p, "exceptional a_m/p")
        if k == 2*m-1:
            assert e*A % p == 3*pow(5, -1, p) % p, (p, "edge")
        if k+1 < 2*m:
            j = k+1
            reverse = (reverse*2*j**3*(6*j+5)*18 *
                       pow((6*j-1)*(3*j+2)*(2*j+1)*(3*j+1), -1, p)) % p
            A = A*delta*pow(36*j**3, -1, p) % p
    assert total_tail == total_mirror
    return total_tail


def main():
    tested = list(primes_1mod6(1000)) + [1327, 19963]
    for p in tested:
        ans = certify(p)
        if p in (7, 13, 19, 373, 1327, 19963):
            print(f"p={p}: reciprocal-mirror-tail={ans} mod {p}")
    print(f"PASS: {len(tested)} primes; complete reverse/source/forward pairing, "
          "exceptional rank and tail sum")


if __name__ == "__main__":
    main()
