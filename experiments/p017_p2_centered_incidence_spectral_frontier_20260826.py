#!/usr/bin/env python3
"""Exact exponent/regression checks for the P017 centered-incidence frontier.

No final P2 theorem is certified here.  The script checks the rational exponent
bookkeeping and finite incidence inequalities used in
`docs/P017_P2_CENTERED_INCIDENCE_SPECTRAL_FRONTIER_20260826.md`.
"""

from fractions import Fraction as Q
from math import isqrt


MU = Q(31, 36)   # M exponent in K
NU = Q(1, 4)     # N exponent in K
LEVEL = MU + NU  # 10/9
THETA_K = Q(4999, 5000)  # y = K^(2 theta)


def hit_count(k: int, modulus: int) -> int:
    return (k * k + 2 * k) // modulus - (k * k) // modulus


def odd_carry(k: int, modulus: int) -> int:
    return hit_count(k, modulus) - hit_count(k, 2 * modulus)


def divisor_count(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    p = 2
    out = 1
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out *= e + 1
        p += 1 if p == 2 else 2
    if x > 1:
        out *= 2
    return out


def check_exact_exponents() -> None:
    assert LEVEL == Q(10, 9)
    assert Q(1) - LEVEL / 2 == Q(4, 9)
    assert LEVEL / 2 == Q(5, 9)
    assert (Q(1) - LEVEL / 2) + LEVEL / 2 == 1

    gamma_min = 1 - THETA_K
    assert gamma_min == Q(1, 5000)

    # Energy-only Cauchy exponent: sqrt(K * K^(10/9)).
    energy_only = (Q(1) + LEVEL) / 2
    assert energy_only == Q(19, 18)
    assert LEVEL - energy_only == Q(1, 18)
    assert energy_only > 1 > THETA_K

    # Degree exponents for B at the current split.
    row_degree = 1 - MU
    col_degree = 1 - NU
    schur = (row_degree + col_degree) / 2
    assert row_degree == Q(5, 36)
    assert col_degree == Q(3, 4)
    assert schur == Q(4, 9)


def finite_incidence_regression(k_max: int = 120) -> None:
    """Check the exact row/column divisor-degree argument at small K.

    We use moderate dyadic boxes chosen from the asymptotic powers but enforce
    mn>K explicitly.  The regression checks the theorem's combinatorial map,
    not an asymptotic numerical spectral claim.
    """
    for k in range(8, k_max + 1):
        M = max(1, int(k ** float(MU)))
        N = max(1, int(k ** float(NU)))
        ms = [m for m in range(M + 1, 2 * M + 1) if m % 2 == 1]
        ns = [n for n in range(N + 1, 2 * N + 1) if n % 2 == 1]
        if not ms or not ns:
            continue

        # A local exact divisor-count maximum is enough for this finite check.
        tau_max = 1
        for r in range(1, (k + 1) * (k + 1)):
            tau_max = max(tau_max, divisor_count(r))

        row_bound = (2 * k / M + 1) * tau_max
        col_bound = (2 * k / N + 1) * tau_max

        row_degrees = {m: 0 for m in ms}
        col_degrees = {n: 0 for n in ns}

        for m in ms:
            for n in ns:
                q = m * n
                if q <= k:
                    continue
                b = odd_carry(k, q)
                assert b in (0, 1)
                if b:
                    row_degrees[m] += 1
                    col_degrees[n] += 1

        assert max(row_degrees.values(), default=0) <= row_bound + 1e-12
        assert max(col_degrees.values(), default=0) <= col_bound + 1e-12


def main() -> None:
    check_exact_exponents()
    finite_incidence_regression()
    print("P017 centered-incidence spectral frontier certificate: PASS")
    print("M exponent in K =", MU, "~=", float(MU))
    print("N exponent in K =", NU, "~=", float(NU))
    print("MN exponent =", LEVEL, "~=", float(LEVEL))
    print("critical operator exponent = 4/9 ~=", float(Q(4, 9)))
    print("coefficient norm exponent = 5/9 ~=", float(Q(5, 9)))
    print("minimum centered spectral gap for theta=4999/10000 = 1/5000 =", float(Q(1, 5000)))
    print("energy-only amplitude exponent = 19/18 ~=", float(Q(19, 18)))


if __name__ == "__main__":
    main()
