#!/usr/bin/env python3
"""Exact finite checks for the rough-divisor Duhamel / quotient-cell BRC.

The checker verifies, with exact rational arithmetic:

1. the global Alladi average equals the rough-divisor Duhamel expansion;
2. the rough divisor polynomial equals the average rough-prefix phase;
3. the z=-1 and z=0 endpoint identities;
4. grouping by floor-quotient cells;
5. the equivalent rough-partial-sum convolution;
6. an arbitrary-reference split;
7. the exact Abel/innovation formula for the conditional defect;
8. the quotient-cell support light cone.

These are finite algebraic regression checks only, not evidence for RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def distinct_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append(n)
    return factors


def is_squarefree(n: int) -> bool:
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return False
        d = 3 if d == 2 else d + 2
    return True


def mobius_squarefree(n: int) -> int:
    if not is_squarefree(n):
        return 0
    return -1 if len(distinct_prime_factors(n)) % 2 else 1


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(a, b):
    length = max(len(a), len(b))
    output = [0] * length
    for index in range(length):
        output[index] = (
            (a[index] if index < len(a) else 0)
            + (b[index] if index < len(b) else 0)
        )
    return trim(output)


def poly_scale(poly, scalar):
    return trim([scalar * coefficient for coefficient in poly])


def poly_multiply(a, b):
    if not a or not b:
        return []
    output = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i + j] += x * y
    return trim(output)


def poly_subtract(a, b):
    return poly_add(a, poly_scale(b, -1))


def poly_evaluate(poly, point):
    total = 0
    power = 1
    for coefficient in poly:
        total += coefficient * power
        power *= point
    return total


def one_plus_z_power(exponent: int):
    return [comb(exponent, degree) for degree in range(exponent + 1)]


def global_alladi_polynomial(n: int, cutoff: int):
    """Coefficients in z for f(p)=p+1 on p<=cutoff."""
    ordered_primes = distinct_prime_factors(n)[::-1]
    coefficients = []
    for degree, prime in enumerate(ordered_primes):
        weight = prime + 1 if prime <= cutoff else 0
        coefficients.append((-1) ** (degree + 1) * weight)
    return trim(coefficients)


def suffix_alladi_polynomial(n: int, cutoff: int):
    ordered_small_primes = [
        prime
        for prime in distinct_prime_factors(n)[::-1]
        if prime <= cutoff
    ]
    return trim(
        [
            (-1) ** (degree + 1) * (prime + 1)
            for degree, prime in enumerate(ordered_small_primes)
        ]
    )


def rough_depth(n: int, cutoff: int) -> int:
    return sum(
        prime > cutoff for prime in distinct_prime_factors(n)
    )


def squarefree_rough_integers(limit: int, cutoff: int):
    output = []
    for integer in range(1, limit + 1):
        if not is_squarefree(integer):
            continue
        factors = distinct_prime_factors(integer)
        if all(prime > cutoff for prime in factors):
            output.append(integer)
    return output


def average_polynomial(polynomials, denominator: int):
    total = []
    for polynomial in polynomials:
        total = poly_add(total, polynomial)
    return [Fraction(coefficient, denominator) for coefficient in total]


def suffix_average(limit: int, cutoff: int):
    return average_polynomial(
        [
            suffix_alladi_polynomial(integer, cutoff)
            for integer in range(1, limit + 1)
        ],
        limit,
    )


def direct_global_average(limit: int, cutoff: int):
    return average_polynomial(
        [
            global_alladi_polynomial(integer, cutoff)
            for integer in range(1, limit + 1)
        ],
        limit,
    )


def rough_partial_polynomial(limit: int, cutoff: int):
    """sum mu(a)(1+z)^omega(a) over squarefree cutoff-rough a<=limit."""
    total = []
    for integer in squarefree_rough_integers(limit, cutoff):
        term = poly_scale(
            one_plus_z_power(len(distinct_prime_factors(integer))),
            mobius_squarefree(integer),
        )
        total = poly_add(total, term)
    return total


def rough_duhamel_average(limit: int, cutoff: int):
    total = []
    for divisor in squarefree_rough_integers(limit, cutoff):
        quotient = limit // divisor
        branch = poly_scale(
            one_plus_z_power(len(distinct_prime_factors(divisor))),
            mobius_squarefree(divisor) * Fraction(quotient, limit),
        )
        total = poly_add(
            total,
            poly_multiply(branch, suffix_average(quotient, cutoff)),
        )
    return total


def direct_rough_phase_average(limit: int, cutoff: int):
    total = []
    for integer in range(1, limit + 1):
        depth = rough_depth(integer, cutoff)
        phase = [0] * depth + [(-1) ** depth]
        total = poly_add(total, poly_scale(phase, Fraction(1, limit)))
    return total


def rough_phase_from_divisors(limit: int, cutoff: int):
    total = []
    for divisor in squarefree_rough_integers(limit, cutoff):
        quotient = limit // divisor
        term = poly_scale(
            one_plus_z_power(len(distinct_prime_factors(divisor))),
            mobius_squarefree(divisor) * Fraction(quotient, limit),
        )
        total = poly_add(total, term)
    return total


def quotient_cells(limit: int, cutoff: int):
    cells = {}
    for divisor in squarefree_rough_integers(limit, cutoff):
        quotient = limit // divisor
        term = poly_scale(
            one_plus_z_power(len(distinct_prime_factors(divisor))),
            mobius_squarefree(divisor),
        )
        cells[quotient] = poly_add(cells.get(quotient, []), term)
    return cells


def quotient_cell_average(limit: int, cutoff: int):
    total = []
    for quotient, cell_polynomial in quotient_cells(limit, cutoff).items():
        total = poly_add(
            total,
            poly_scale(
                poly_multiply(
                    cell_polynomial,
                    suffix_average(quotient, cutoff),
                ),
                Fraction(quotient, limit),
            ),
        )
    return total


def convolution_average(limit: int, cutoff: int):
    total = []
    for integer in range(1, limit + 1):
        total = poly_add(
            total,
            poly_scale(
                poly_multiply(
                    suffix_alladi_polynomial(integer, cutoff),
                    rough_partial_polynomial(limit // integer, cutoff),
                ),
                Fraction(1, limit),
            ),
        )
    return total


def reference_split(limit: int, cutoff: int, reference):
    rough_phase = []
    conditional_defect = []
    for divisor in squarefree_rough_integers(limit, cutoff):
        quotient = limit // divisor
        branch = poly_scale(
            one_plus_z_power(len(distinct_prime_factors(divisor))),
            mobius_squarefree(divisor) * Fraction(quotient, limit),
        )
        rough_phase = poly_add(rough_phase, branch)
        conditional_defect = poly_add(
            conditional_defect,
            poly_multiply(
                branch,
                poly_subtract(
                    suffix_average(quotient, cutoff),
                    reference,
                ),
            ),
        )
    reconstructed = poly_add(
        poly_multiply(reference, rough_phase),
        conditional_defect,
    )
    return reconstructed, rough_phase, conditional_defect


def innovation_defect(limit: int, cutoff: int, reference):
    """Abel form: X^-1 sum_U M_rough(floor(X/U))(A_U-reference)."""
    total = []
    for quotient in range(1, limit + 1):
        innovation = poly_subtract(
            suffix_alladi_polynomial(quotient, cutoff),
            reference,
        )
        total = poly_add(
            total,
            poly_scale(
                poly_multiply(
                    rough_partial_polynomial(limit // quotient, cutoff),
                    innovation,
                ),
                Fraction(1, limit),
            ),
        )
    return total


def smooth_count(limit: int, cutoff: int) -> int:
    return sum(
        all(
            prime <= cutoff
            for prime in distinct_prime_factors(integer)
        )
        for integer in range(1, limit + 1)
    )


def check_all() -> None:
    for limit in (20, 37, 60, 101):
        for cutoff in (2, 3, 5, 7):
            direct = direct_global_average(limit, cutoff)
            assert rough_duhamel_average(limit, cutoff) == direct
            assert quotient_cell_average(limit, cutoff) == direct
            assert convolution_average(limit, cutoff) == direct

            phase_direct = direct_rough_phase_average(limit, cutoff)
            phase_divisor = rough_phase_from_divisors(limit, cutoff)
            assert phase_direct == phase_divisor
            assert poly_evaluate(phase_direct, -1) == 1
            assert poly_evaluate(phase_direct, 0) == Fraction(
                smooth_count(limit, cutoff), limit
            )

            reference = [
                Fraction(-3, 7),
                Fraction(2, 5),
                Fraction(1, 11),
            ]
            reconstructed, _, conditional_defect = reference_split(
                limit,
                cutoff,
                reference,
            )
            assert reconstructed == direct
            assert innovation_defect(
                limit,
                cutoff,
                reference,
            ) == conditional_defect

            # Every nonconstant rough branch obeys the quotient-depth light cone.
            for divisor in squarefree_rough_integers(limit, cutoff):
                depth = len(distinct_prime_factors(divisor))
                if depth:
                    quotient = limit // divisor
                    assert quotient * cutoff**depth < limit

    print("all exact rough-divisor Duhamel BRC checks passed")


if __name__ == "__main__":
    check_all()
