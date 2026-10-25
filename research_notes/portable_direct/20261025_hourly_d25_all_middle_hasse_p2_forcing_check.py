#!/usr/bin/env python3
"""Exact p^2 certificate for every previously mod-p-invisible middle Hasse cutoff port."""
from math import isqrt

def is_prime(n):
    return n >= 2 and all(n % d != 0 for d in range(2, isqrt(n) + 1))

def check(p, order_limit=None):
    assert is_prime(p) and p % 6 == 1
    m, mod = (p - 1) // 6, p * p
    N = p - 2 if order_limit is None else min(p - 2, order_limit)
    fac = 1
    for j in range(1, p):
        fac = fac * j % mod
    A = 2 * pow(fac, -2, mod) % mod
    c = [1] + [0] * N
    bases = []
    for shift, slope in ((m, 1), (2 * m, 2)):
        for j in range(p):
            h = j - shift
            if h == 0:
                continue
            A = A * h % mod
            u = slope * pow(h, -1, mod) % mod
            bases.append(u)
            for n in range(N, 0, -1):
                c[n] = (c[n] - u * c[n - 1]) % mod
    assert A % p == 2
    inverses = [pow(j, -1, mod) for j in range(1, p)]
    unit_powers = bases[:]
    for n in range(1, N + 1):
        direct_sum = sum(unit_powers) % mod
        two_n = pow(2, n, mod)
        h_all = sum(pow(j, n, mod) for j in inverses) % mod
        h_m = sum(pow(j, n + 1, mod) for j in inverses[:m]) % mod
        h_2m = sum(pow(j, n + 1, mod) for j in inverses[:2*m]) % mod
        harmonic_sum = ((1 + two_n) * h_all
                        - (-1)**n * n * p * (h_m + two_n * h_2m)) % mod
        predicted_forcing = 2 * harmonic_sum * pow(n, -1, mod) % mod
        actual_forcing = -A * c[n] % mod
        assert direct_sum == harmonic_sum and direct_sum % p == 0
        assert actual_forcing == predicted_forcing, (p, n, actual_forcing, predicted_forcing)
        unit_powers = [(x * u) % mod for x, u in zip(unit_powers, bases)]
    return N

def main():
    small = [p for p in range(7, 374) if p % 6 == 1 and is_prime(p)]
    total = 0
    for p in small:
        total += check(p)
    for p in (1327, 19963):
        total += check(p, order_limit=12)
    for p in (7, 13, 19, 31, 373):
        print(f"p={p}: PASS all middle Hasse forcing ranks k=3..{p}")
    print(f"PASS: {len(small)} full-range primes, 2 large-prime 12-order certificates, "
          f"{total} independently compared (p, Hasse-order) pairs")

if __name__ == "__main__":
    main()
