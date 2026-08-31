#!/usr/bin/env python3
"""Exact/regression checker for the inert-minus finite Clausen-Swisher bridge.

The all-prime congruence is NOT proved here.  This checker verifies:
1. the exact A14 companion-definition identity and its first-order recurrence;
2. the unique p-singular recurrence location n=(p-3)/2;
3. the exact source-valuation zoning for target primes;
4. bounded equivalence regression between C_p and the singular-boundary certificate.

Finite prime checks are regression/falsification only.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, gcd

TARGET_PRIMES = (17, 23, 41, 47, 71, 89)


def vp_int(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_fraction(x: Fraction, p: int) -> int:
    if x == 0:
        return 10**9
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def mod_fraction(x: Fraction, modulus: int) -> int:
    if gcd(x.denominator, modulus) != 1:
        raise AssertionError(
            f"denominator is not a unit modulo {modulus}: {x.denominator}"
        )
    return (
        (x.numerator % modulus)
        * pow(x.denominator % modulus, -1, modulus)
        % modulus
    )


def pochhammer(a: Fraction, k: int) -> Fraction:
    out = Fraction(1)
    for j in range(k):
        out *= a + j
    return out


def h(k: int) -> Fraction:
    return Fraction(comb(2 * k, k) ** 2 * comb(3 * k, k), 216**k)


def w_full(p: int) -> Fraction:
    return sum((6 * k + 1) * h(k) for k in range(p))


def w_tilde(p: int) -> Fraction:
    m = (2 * p - 1) // 3
    return sum((6 * k + 1) * h(k) for k in range(m + 1))


def e_swisher(p: int) -> Fraction:
    m = (2 * p - 1) // 3
    return sum(
        (-1) ** k
        * (6 * k + 1)
        * pochhammer(Fraction(1, 3), k) ** 3
        / factorial(k) ** 3
        for k in range(m + 1)
    )


def a14_companion(n: int) -> Fraction:
    """Sun A14(i) companion quotient, used only as an exact finite definition."""
    if n <= 0:
        raise ValueError("n must be positive")
    numerator = sum(
        (6 * k + 1)
        * comb(2 * k, k) ** 2
        * comb(3 * k, k)
        * 216 ** (n - 1 - k)
        for k in range(n)
    )
    denominator = n * (2 * n + 1) * comb(2 * n, n)
    return Fraction(numerator, denominator)


def fuss_catalan_2(n: int) -> int:
    value = Fraction(comb(3 * n, n), 2 * n + 1)
    assert value.denominator == 1
    return value.numerator


def recurrence_source(n: int) -> int:
    return (6 * n + 1) * comb(2 * n - 1, n) * fuss_catalan_2(n)


def check_exact_companion_identity(p: int) -> None:
    a = a14_companion(p)
    exact = (
        Fraction(p * (2 * p + 1) * comb(2 * p, p), 216 ** (p - 1)) * a
    )
    assert w_full(p) == exact


def check_exact_recurrence(limit: int = 18) -> None:
    # From S_{n+1}=216 S_n + A_n and the exact normalizing denominator:
    # (2n+3)a_{n+1}=108n a_n+R_n.
    for n in range(1, limit + 1):
        lhs = (2 * n + 3) * a14_companion(n + 1)
        rhs = 108 * n * a14_companion(n) + recurrence_source(n)
        assert lhs == rhs, (n, lhs - rhs)


def source_valuation_zones(p: int) -> None:
    assert p % 24 in (17, 23)
    s = (p - 3) // 2
    m = (2 * p - 1) // 3

    # Unique singular recurrence coefficient 2n+3=p.
    singular = [n for n in range(1, p) if (2 * n + 3) % p == 0]
    assert singular == [s]

    # Exact target-class source zoning.
    assert vp_int(recurrence_source(s), p) == 1
    assert vp_int(recurrence_source(s + 1), p) == 0
    for n in range(s + 2, m + 1):
        assert vp_int(recurrence_source(n), p) == 1, (p, n)
    for n in range(m + 1, p):
        assert vp_int(recurrence_source(n), p) >= 2, (p, n)


def backward_target(p: int) -> tuple[int, int]:
    """Return s and T_{s+1} modulo p^2.

    T_p is the exact A14 quotient target equivalent to W_p == -p (mod p^3):
      a_p == -216^(p-1) / ((2p+1) C(2p,p))  (mod p^2).
    For n=p-1,...,s+1, propagate this target backward through the unit
    recurrence coefficients.
    """
    p2 = p * p
    s = (p - 3) // 2
    unit = ((2 * p + 1) * comb(2 * p, p)) % p2
    assert gcd(unit, p) == 1
    t = (-pow(216, p - 1, p2) * pow(unit, -1, p2)) % p2

    for n in range(p - 1, s, -1):
        den = (108 * n) % p2
        assert gcd(den, p) == 1
        t = (
            ((2 * n + 3) * t - recurrence_source(n))
            * pow(den, -1, p2)
            % p2
        )
    return s, t


def singular_boundary_residual(p: int) -> Fraction:
    s, t = backward_target(p)
    return 108 * s * a14_companion(s) + recurrence_source(s) - p * t


def check_regression_equivalence(p: int) -> None:
    assert p % 24 in (17, 23)
    p3 = p**3

    # Frozen predecessor high-tail valuation.
    assert vp_fraction(w_full(p) - w_tilde(p), p) >= 3

    # Bounded target and bridge regression; not theorem evidence.
    assert mod_fraction(w_full(p) + p, p3) == 0
    assert mod_fraction(2 * w_tilde(p) - e_swisher(p), p3) == 0

    # New singular-boundary certificate regression.
    s = (p - 3) // 2
    assert gcd(a14_companion(s).denominator, p) == 1
    assert mod_fraction(singular_boundary_residual(p), p3) == 0


def main() -> int:
    check_exact_recurrence()
    for p in TARGET_PRIMES:
        check_exact_companion_identity(p)
        source_valuation_zones(p)
        check_regression_equivalence(p)

    print(
        "PASS: exact companion recurrence, unique singular boundary, valuation zones, "
        "and bounded target/bridge equivalence regression. "
        "No all-prime proof is claimed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
