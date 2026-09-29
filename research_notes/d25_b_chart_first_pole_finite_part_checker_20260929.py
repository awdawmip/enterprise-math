#!/usr/bin/env python3
"""Dependency-free regression for the D25 upper-B first-pole finite part.

Regression only. The proof is in d25_b_chart_first_pole_finite_part_20260929.md.
"""

from math import isqrt

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

def inv(a: int, mod: int) -> int:
    return pow(a % mod, -1, mod)

def q(num: int, den: int, mod: int) -> int:
    return (num % mod) * inv(den, mod) % mod

def harmonic(n: int, p: int) -> int:
    return sum(inv(k, p) for k in range(1, n + 1)) % p

def q_endpoint_mod_p2(p: int) -> int:
    m = (p - 1) // 6
    J = 2 * m - 1
    mod = p * p
    Q = -1 % mod
    for j in range(J):
        Q = Q * ((6 * j + 5) % mod) % mod
        Q = Q * inv(4 * (3 * j + 2), mod) % mod
    return Q

def B_mod_p(p: int) -> int:
    m = (p - 1) // 6
    N = 2 * m - 2
    b = q(5, 32, p)
    total = 0
    for j in range(N + 1):
        total = (total + b) % p
        if j < N:
            num = (j + 1) * (2 * j + 5) * (3 * j + 4) * (6 * j + 11)
            den = 4 * (j + 3) * (2 * j + 3) * (3 * j + 5) * (3 * j + 7)
            b = b * (num % p) % p * inv(den, p) % p
    return total

def check_prime(p: int):
    m = (p - 1) // 6
    mod2 = p * p
    QJ = q_endpoint_mod_p2(p)

    delta_num = (QJ + q(8, 3, mod2)) % mod2
    assert delta_num % p == 0
    delta = (delta_num // p) % p

    A = q(
        -(2 * p - 3) * (2 * p + 1),
        2 * (p - 2) * (p - 1) * (p + 2),
        mod2,
    )
    pbJ = A * QJ % mod2
    assert pbJ % p == (-1) % p

    beta_num = (pbJ + 1) % mod2
    assert beta_num % p == 0
    beta = (beta_num // p) % p

    beta_from_delta = (q(3, 8, p) * delta - q(7, 3, p)) % p
    assert beta == beta_from_delta

    H3 = harmonic(3 * m, p)
    H2 = harmonic(2 * m, p)
    beta_h = (-q(1, 2, p) * H3 + q(1, 3, p) * H2 - q(5, 2, p)) % p
    assert beta == beta_h

    C = q(
        (p - 1) * (2 * p + 3) * (2 * p + 7),
        4 * (p + 1) * (p + 3) * (p + 5) * (2 * p + 1),
        mod2,
    )
    b_next = pbJ * C % mod2
    assert b_next % p == q(7, 20, p)

    gamma_num = (b_next - q(7, 20, mod2)) % mod2
    assert gamma_num % p == 0
    gamma = (gamma_num // p) % p
    gamma_rhs = (-q(94, 75, p) - q(7, 20, p) * beta) % p
    assert gamma == gamma_rhs

    B = B_mod_p(p)
    target = (H3 - q(2, 3, p) * H2 + q(10, 3, p)) % p
    finite_part_target = (-2 * beta - q(5, 3, p)) % p
    assert target == finite_part_target
    assert B == target

    undivided = (p * B + 2 * pbJ + 2 + q(5 * p, 3, mod2)) % mod2
    assert undivided == 0

def main():
    primes = [p for p in range(7, 10000) if p % 6 == 1 and is_prime(p)]
    failures = []
    for p in primes:
        try:
            check_prime(p)
        except Exception as exc:
            failures.append((p, repr(exc)))
            break
    print({
        "prime_count": len(primes),
        "range": "p < 10000, p == 1 (mod 6)",
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "evidence_role": "finite regression/falsification only",
    })
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
