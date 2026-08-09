"""Exact block-ideal decomposition for primitive unit relations ``1+b=c``.

For one block n, the raw arithmetic derivative is an integer linear form with
image ``A(n) Z``, where

    A(n) = gcd_{p|n} n*v_p(n)/p = m(n)*h(n).

In the relation ``1+b=c``, additivity is simply ``d(b)=d(c)`` and the
Wronskian equals ``d(b)``.  Hence the positive Wronskian image generator is the
intersection generator ``lcm(A(b),A(c))``.  The floor-access problem then
splits into independent minimum-norm preimage problems inside the two blocks.

Ideal intersection, lcm, and Bezout preimage optimization are standard integer
algebra.  This module is a P025 certificate-precision specialization.
"""

from __future__ import annotations

from math import gcd, lcm

from .abc_absorption_block import block_raw_additive_content
from .abc_absorption_formula import minimum_absorption_redundancy_support_formula
from .abc_absorption_two_variable import minimum_linf_diophantine_solution
from .abc_support import multiplicity_residual, prime_factorization


def raw_block_derivative_coefficients(n: int) -> tuple[tuple[int, int], ...]:
    """Return the coefficients ``n*v_p(n)/p`` of the raw block derivative."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        raise ValueError("n must be an integer > 1")
    return tuple((p, n * exponent // p) for p, exponent in prime_factorization(n))


def raw_block_derivative_image_generator(n: int) -> int:
    """Return the positive generator ``A(n)`` of all raw derivative values."""
    return block_raw_additive_content(n)


def unit_relation_absorption_floor(b: int, c: int) -> dict[str, int]:
    """Return the exact Wronskian image generator and ``eta_min`` for ``1+b=c``."""
    if isinstance(b, bool) or not isinstance(b, int) or b <= 1:
        raise ValueError("b must be an integer > 1")
    if isinstance(c, bool) or not isinstance(c, int) or c != b + 1:
        raise ValueError("require c=b+1")
    if gcd(b, c) != 1:
        raise AssertionError("consecutive positive integers must be coprime")
    A_b = raw_block_derivative_image_generator(b)
    A_c = raw_block_derivative_image_generator(c)
    D = lcm(A_b, A_c)
    M = multiplicity_residual(b) * multiplicity_residual(c)
    if D % M != 0:
        raise AssertionError("unit-relation Wronskian image generator must contain residual product")
    eta = D // M
    support_eta = minimum_absorption_redundancy_support_formula(1, b, c)
    if eta != support_eta:
        raise AssertionError("unit ideal-intersection formula disagrees with support formula")
    return {
        "block_generator_b": A_b,
        "block_generator_c": A_c,
        "wronskian_image_generator": D,
        "multiplicity_residual_product": M,
        "eta_min": eta,
        "target_multiple_b": D // A_b,
        "target_multiple_c": D // A_c,
    }


def minimum_block_derivative_access_radius(n: int, target: int) -> dict[str, object]:
    """Solve a block preimage exactly when its prime support has size <=2.

    The general higher-support problem is an ordinary affine-lattice minimum
    problem and is deliberately not hidden behind brute force here.
    """
    if isinstance(target, bool) or not isinstance(target, int):
        raise ValueError("target must be an integer")
    coefficients = raw_block_derivative_coefficients(n)
    generator = raw_block_derivative_image_generator(n)
    if target % generator != 0:
        raise ValueError("target is outside the block derivative image")
    if len(coefficients) == 1:
        coefficient = coefficients[0][1]
        coordinate = target // coefficient
        return {
            "primes": (coefficients[0][0],),
            "coordinates": (coordinate,),
            "radius": abs(coordinate),
        }
    if len(coefficients) == 2:
        (p, A), (q, B) = coefficients
        solution = minimum_linf_diophantine_solution(A, B, target)
        return {
            "primes": (p, q),
            "coordinates": (solution.u, solution.v),
            "radius": solution.radius,
        }
    raise ValueError("exact block access helper currently supports one or two prime coordinates")


def unit_relation_absorption_access(b: int, c: int) -> dict[str, object]:
    """Return exact ``nu`` when both non-unit blocks have support size <=2."""
    floor = unit_relation_absorption_floor(b, c)
    D = int(floor["wronskian_image_generator"])
    left = minimum_block_derivative_access_radius(b, D)
    right = minimum_block_derivative_access_radius(c, D)
    nu = max(int(left["radius"]), int(right["radius"]))
    return {
        **floor,
        "block_witness_b": left,
        "block_witness_c": right,
        "nu": nu,
    }


def mersenne_prime_unit_relation_access(exponent: int) -> dict[str, int | tuple[int, int]]:
    """Closed calibration for ``1+(2^m-1)=2^m`` when the Mersenne term is prime.

    The non-power block is prime and has derivative image generator 1.  The
    power block has generator ``m*2^(m-1)``.  Their lcm is therefore the latter,
    ``eta_min=m``, and the prime block must carry coordinate
    ``m*2^(m-1)``.  With only two prime coordinates total, this is also the
    first nondegenerate witness radius by the rank-one theorem.
    """
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 2:
        raise ValueError("exponent must be an integer >= 2")
    q = 2**exponent - 1
    if prime_factorization(q) != ((q, 1),):
        raise ValueError("2^exponent-1 must be prime")
    H = exponent * 2 ** (exponent - 1)
    floor = unit_relation_absorption_floor(q, 2**exponent)
    if floor["wronskian_image_generator"] != H or floor["eta_min"] != exponent:
        raise AssertionError("Mersenne unit-relation floor formula failed")
    access = unit_relation_absorption_access(q, 2**exponent)
    if access["nu"] != H:
        raise AssertionError("Mersenne unit-relation access formula failed")
    return {
        "exponent": exponent,
        "mersenne_prime": q,
        "eta_min": exponent,
        "mu": H,
        "nu": H,
        "floor_witness_q_2": (H, 1),
    }
