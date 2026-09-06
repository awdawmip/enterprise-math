#!/usr/bin/env python3
"""Exact finite checks for the prime-winding harmonic/gap frontier.

The script uses integers and ``Fraction`` only.  It verifies the exact finite
kernels behind the asymptotic argument; it is not a numerical proof of the PNT
and does not claim novelty for the classical Selberg identity.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial, isqrt
from typing import DefaultDict, Dict, Tuple

Monomial = Tuple[int, ...]
Polynomial = Dict[Monomial, int]


def factorization(n: int) -> dict[int, int]:
    assert n >= 1
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n: int) -> int:
    assert n >= 1
    factors = factorization(n)
    if any(e > 1 for e in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def divisors(n: int) -> list[int]:
    assert n >= 1
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


@lru_cache(maxsize=None)
def harmonic_history(r: int, n: int) -> Fraction:
    """Ordered r-history mass sum_{n1*...*nr<=n} 1/(n1*...*nr)."""
    assert r >= 0 and n >= 1
    if r == 0:
        return Fraction(1, 1)
    return sum(
        (harmonic_history(r - 1, n // a) / a for a in range(1, n + 1)),
        Fraction(0, 1),
    )


def poly_add(a: Polynomial, b: Polynomial, scale: int = 1) -> Polynomial:
    out: DefaultDict[Monomial, int] = defaultdict(int, a)
    for monomial, coefficient in b.items():
        out[monomial] += scale * coefficient
        if out[monomial] == 0:
            del out[monomial]
    return dict(out)


def poly_mul(a: Polynomial, b: Polynomial) -> Polynomial:
    out: DefaultDict[Monomial, int] = defaultdict(int)
    for left, c_left in a.items():
        for right, c_right in b.items():
            out[tuple(sorted(left + right))] += c_left * c_right
    return dict(out)


def poly_pow(a: Polynomial, exponent: int) -> Polynomial:
    assert exponent >= 0
    out: Polynomial = {(): 1}
    for _ in range(exponent):
        out = poly_mul(out, a)
    return out


def formal_log(n: int) -> Polynomial:
    """Formal prime-labelled logarithm sum_p v_p(n) X_p."""
    return {(p,): exponent for p, exponent in factorization(n).items()}


def formal_mangoldt(n: int) -> Polynomial:
    """Formal Lambda(n): X_p on a positive p-power and zero otherwise."""
    factors = factorization(n)
    if len(factors) != 1:
        return {}
    p = next(iter(factors))
    return {(p,): 1}


def primitive_poly(r: int, n: int) -> Polynomial:
    """Formal Möbius primitive Lambda_r = mu * log^r."""
    assert r >= 1 and n >= 1
    out: Polynomial = {}
    for d in divisors(n):
        out = poly_add(out, poly_pow(formal_log(n // d), r), mobius(d))
    return out


def check_mobius_harmonic_recoalescence(limit: int = 60, max_r: int = 4) -> None:
    for n in range(1, limit + 1):
        # Exact floor Möbius collapse.
        assert sum(mobius(d) * (n // d) for d in range(1, n + 1)) == 1

        # PHR-T01 for the first few history degrees.
        for r in range(1, max_r + 1):
            lhs = sum(
                (
                    Fraction(mobius(d), d) * harmonic_history(r, n // d)
                    for d in range(1, n + 1)
                ),
                Fraction(0, 1),
            )
            assert lhs == harmonic_history(r - 1, n), (n, r, lhs)


def check_hyperbola_identity(limit: int = 100) -> None:
    for n in range(1, limit + 1):
        m = isqrt(n)
        rhs = (
            2
            * sum(
                (harmonic_history(1, n // a) / a for a in range(1, m + 1)),
                Fraction(0, 1),
            )
            - harmonic_history(1, m) ** 2
        )
        assert harmonic_history(2, n) == rhs, n


def check_primitive_recurrence(limit: int = 100, max_r: int = 5) -> None:
    """Check Lambda_(r+1) = D Lambda_r + Lambda * Lambda_r formally."""
    for n in range(1, limit + 1):
        for r in range(1, max_r):
            lhs = primitive_poly(r + 1, n)
            rhs = poly_mul(primitive_poly(r, n), formal_log(n))

            convolution: Polynomial = {}
            for d in divisors(n):
                convolution = poly_add(
                    convolution,
                    poly_mul(formal_mangoldt(d), primitive_poly(r, n // d)),
                )
            rhs = poly_add(rhs, convolution)

            assert lhs == rhs, (n, r, lhs, rhs)
            assert all(coefficient >= 0 for coefficient in lhs.values()), (n, r, lhs)

    # Top squarefree shell: the commutative mixed coefficient is r!.
    prime_prefix = [2, 3, 5, 7, 11]
    for r in range(1, max_r + 1):
        primes = prime_prefix[:r]
        n = 1
        for p in primes:
            n *= p
        assert primitive_poly(r, n) == {tuple(primes): factorial(r)}, (r, n)


def sample_value(n: int) -> Fraction:
    """Deterministic rational test field for quotient identities."""
    numerator = ((37 * n * n + 11 * n + 7) % 97) - 48
    denominator = ((13 * n + 5) % 17) + 1
    return Fraction(numerator, denominator)


def q2(n: int) -> int:
    return n // 2


def q4(n: int) -> int:
    return n // 4


def defect2(n: int) -> Fraction:
    return sample_value(n) + sample_value(q2(n))


def defect4(n: int) -> Fraction:
    return sample_value(n) + sample_value(q4(n))


def check_quotient_odd_triangle(limit: int = 500) -> None:
    for n in range(0, limit + 1):
        assert q2(q2(n)) == q4(n)
        assert (
            2 * sample_value(n)
            == defect2(n) + defect4(n) - defect2(q2(n))
        )
        assert 4 * sample_value(n) ** 2 <= 3 * (
            defect2(n) ** 2 + defect4(n) ** 2 + defect2(q2(n)) ** 2
        )

    # PHR-T08, using that q2 has at most two preimages.
    for n_max in range(4, limit + 1):
        lhs = sum(
            (sample_value(n) ** 2 for n in range(4, n_max + 1)),
            Fraction(0, 1),
        )
        rhs = Fraction(9, 4) * sum(
            (defect2(n) ** 2 for n in range(2, n_max + 1)),
            Fraction(0, 1),
        ) + Fraction(3, 4) * sum(
            (defect4(n) ** 2 for n in range(4, n_max + 1)),
            Fraction(0, 1),
        )
        assert lhs <= rhs, n_max


def main() -> None:
    check_mobius_harmonic_recoalescence()
    check_hyperbola_identity()
    check_primitive_recurrence()
    check_quotient_odd_triangle()
    print("prime-winding harmonic recoalescence/gap checks: PASS")


if __name__ == "__main__":
    main()
