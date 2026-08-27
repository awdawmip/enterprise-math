"""Double-horizon integer reduction for the P022 Franel boundary obstruction.

The existing P022 Bailey-tail theorem reduces, for a prime p=6M-1,

    p | F_(2M)

to vanishing modulo p of

    T_M = 3F2(-M,-M,-M; -3M,3M; 1).

This module records a second exact integerization of the same rational value.
Four terminating 3F2(1) transformations give

    T_M = E_M K_M,

where

    E_M = (2/3) M!(2M)!(2M-1)!(3M-1)! / (4M-1)!^2

and

    K_M = sum_(j=0)^(2M) (-1)^j
          C(2M,j) C(M+j,j) C(4M+j-1,j).

For prime p=6M-1>3, E_M is a p-adic unit, so T_M and K_M have the
same zero locus modulo p.  The last K_M summand is 0 modulo p and the
remaining alternating sign can be absorbed by the binomial complement
identity

    C(4M+j-1,j) = (-1)^j C(2M-1,j)  (mod p),

which yields the sign-free companion

    W_M = sum_(j=0)^(2M-1)
          C(2M,j) C(M+j,j) C(2M-1,j)

with K_M = W_M (mod p).

At the Driver-routed q=3r-1 twin boundary one has M=3m, r=2M=6m,
and q=6M-1=18m-1.  Hence the remaining boundary zero is equivalently
K_(3m)=0 (mod q), or W_(3m)=0 (mod q).

This is an exact reduction only.  It does not prove the required all-m
nonvanishing in the admissible twin-boundary classes.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

from .p022_barlow_franel_third_index_bailey_tail import (
    bailey_symmetric_binomial_denominator,
    bailey_symmetric_integer_sum,
)
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_positive_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _pochhammer(value: int, length: int) -> int:
    result = 1
    for step in range(length):
        result *= value + step
    return result


def _fraction_mod_prime(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    if denominator == 0:
        raise ValueError("fraction denominator is not a p-adic unit")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def symmetric_bailey_tail_value(truncation: int) -> Fraction:
    """Return T_M=3F2(-M,-M,-M;-3M,3M;1) exactly."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    total = Fraction(0, 1)
    for j in range(M + 1):
        total += Fraction(
            _pochhammer(-M, j) ** 3,
            _pochhammer(-3 * M, j)
            * _pochhammer(3 * M, j)
            * factorial(j),
        )
    return total


def double_horizon_integer_kernel(truncation: int) -> int:
    """Return K_M, the denominator-free 2M-horizon integer kernel."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    return sum(
        (-1) ** j
        * comb(2 * M, j)
        * comb(M + j, j)
        * comb(4 * M + j - 1, j)
        for j in range(2 * M + 1)
    )


def double_horizon_prefactor(truncation: int) -> Fraction:
    """Return the exact unit candidate E_M in T_M=E_M K_M."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    return Fraction(
        2
        * factorial(M)
        * factorial(2 * M)
        * factorial(2 * M - 1)
        * factorial(3 * M - 1),
        3 * factorial(4 * M - 1) ** 2,
    )


def double_horizon_exact_identity(
    truncation: int,
) -> tuple[Fraction, int, Fraction]:
    """Return (T_M,K_M,E_M K_M) and certify the exact transform identity."""
    tail = symmetric_bailey_tail_value(truncation)
    kernel = double_horizon_integer_kernel(truncation)
    transformed = double_horizon_prefactor(truncation) * kernel
    if tail != transformed:
        raise AssertionError("double-horizon terminating transform failed")
    return tail, kernel, transformed


def double_horizon_old_integer_ratio(truncation: int) -> Fraction:
    """Certify the exact relation between K_M and the earlier U_M kernel."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    kernel = double_horizon_integer_kernel(M)
    old_integer = bailey_symmetric_integer_sum(M)
    ratio = Fraction(
        comb(4 * M - 1, M),
        2 * comb(2 * M - 1, M),
    )
    if Fraction(kernel, 1) != ratio * old_integer:
        raise AssertionError("double-horizon and Bailey integer kernels disagree")

    # Cross-check against the already frozen denominator D_M T_M=U_M.
    denominator = bailey_symmetric_binomial_denominator(M)
    if symmetric_bailey_tail_value(M) * denominator != old_integer:
        raise AssertionError("existing Bailey integerization changed")
    return ratio


def sign_free_companion_kernel(truncation: int) -> int:
    """Return W_M, the positive-binomial companion used modulo p=6M-1."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    return sum(
        comb(2 * M, j)
        * comb(M + j, j)
        * comb(2 * M - 1, j)
        for j in range(2 * M)
    )


def double_horizon_modular_certificate(
    truncation: int,
) -> tuple[int, int, int, int]:
    """Return (p,K_M mod p,W_M mod p,U_M mod p) for prime p=6M-1."""
    _require_positive_integer("truncation", truncation)
    M = truncation
    prime = 6 * M - 1
    if prime <= 3 or not _is_prime(prime):
        raise ValueError("6*truncation-1 must be prime")

    _, kernel, _ = double_horizon_exact_identity(M)
    companion = sign_free_companion_kernel(M)
    old_integer = bailey_symmetric_integer_sum(M)

    prefactor_residue = _fraction_mod_prime(
        double_horizon_prefactor(M),
        prime,
    )
    if prefactor_residue == 0:
        raise AssertionError("double-horizon prefactor must be a p-adic unit")

    ratio_residue = _fraction_mod_prime(
        double_horizon_old_integer_ratio(M),
        prime,
    )
    if ratio_residue == 0:
        raise AssertionError("integer-kernel conversion must be a p-adic unit")

    kernel_residue = kernel % prime
    companion_residue = companion % prime
    old_residue = old_integer % prime
    if kernel_residue != companion_residue:
        raise AssertionError("sign-free companion congruence failed")
    if (kernel_residue == 0) != (old_residue == 0):
        raise AssertionError("double-horizon and old integer zero loci disagree")
    return prime, kernel_residue, companion_residue, old_residue


def twin_boundary_double_horizon_certificate(
    scale: int,
) -> tuple[int, int, int, int, int]:
    """Certify the q=18m-1 twin-boundary reduction to K_(3m) modulo q.

    The exact P022 twin-boundary hypotheses require 12m-1, 12m+1 and
    18m-1 to be prime.  The returned tuple is

        (q, r, F_r mod q, K_(3m) mod q, W_(3m) mod q).
    """
    _require_positive_integer("scale", scale)
    m = scale
    left_twin = 12 * m - 1
    right_twin = 12 * m + 1
    prime = 18 * m - 1
    if not (_is_prime(left_twin) and _is_prime(right_twin) and _is_prime(prime)):
        raise ValueError("scale must realize the P022 prime twin boundary")

    M = 3 * m
    rank = 2 * M
    _, kernel_residue, companion_residue, _ = double_horizon_modular_certificate(M)
    franel_residue = triple_moment_factor(rank) % prime
    if (franel_residue == 0) != (kernel_residue == 0):
        raise AssertionError("boundary Franel zero and double-horizon zero disagree")
    return prime, rank, franel_residue, kernel_residue, companion_residue
