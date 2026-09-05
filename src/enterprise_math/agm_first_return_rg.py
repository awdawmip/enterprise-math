"""Gauss-Legendre AGM domain facade over binary BRC first-return calculus.

This module does not define the binary return machinery itself; that reusable layer
lives in ``brc_binary_first_return``.  Here the activity variable is the AGM shape
s=(a-b)/(a+b), and finite first-return depth N supplies the rational approximation

    F_N(s) = sum_{n<=N} f_n s^(2n),
    T_N(s) = F_N(s)/(2-F_N(s)).

At completed depth, the research theorem identifies F with twice chord loss and
T with the exact AGM shape update.  The facade exposes finite rational operations,
proved error envelopes, and the standard-orbit adaptive depth/resource formulas.

Status: research-harvest domain operator.  It is not Foundation and does not by
itself identify the endogenous completion constant with classical pi.
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil

from .brc_binary_first_return import first_return_polynomial


def _as_fraction(value: Fraction | int) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def _require_shape(shape: Fraction) -> None:
    if shape < 0 or shape > Fraction(1, 4):
        raise ValueError("this facade certifies the standard AGM shape range 0<=s<=1/4")


def _require_positive_depth(depth: int) -> None:
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")


def finite_return_mass(shape: Fraction | int, depth: int) -> Fraction:
    """Return F_N(s) on the certified AGM shape range."""
    s = _as_fraction(shape)
    _require_shape(s)
    _require_positive_depth(depth)
    return first_return_polynomial(s, depth)


def finite_shape_update(shape: Fraction | int, depth: int) -> Fraction:
    """Return the explicit finite first-return shape map T_N=F_N/(2-F_N)."""
    f = finite_return_mass(shape, depth)
    return f / (2 - f)


def one_shell_shape_update(shape: Fraction | int) -> Fraction:
    """Minimal nontrivial return-depth map T_1=s^2/(4-s^2)."""
    s = _as_fraction(shape)
    _require_shape(s)
    return s * s / (4 - s * s)


def finite_geometric_channel(
    total_scale: Fraction | int,
    shape: Fraction | int,
    depth: int,
) -> Fraction:
    """Return the finite lower-channel approximation H*(1-F_N)/2."""
    h = _as_fraction(total_scale)
    if h <= 0:
        raise ValueError("total_scale must be positive")
    f = finite_return_mass(shape, depth)
    return h * (1 - f) / 2


def quadratic_universality_bounds(shape: Fraction | int) -> tuple[Fraction, Fraction]:
    """Return the proved depth-independent bounds for every N>=1.

    For 0<=s<=1/4,

        s^2/4 <= T_N(s) < (256/961) s^2 < (4/15) s^2.
    """
    s = _as_fraction(shape)
    _require_shape(s)
    return s * s / 4, Fraction(256, 961) * s * s


def shape_truncation_error_bound(shape: Fraction | int, depth: int) -> Fraction:
    """Return the proved upper envelope (512/961)*s^(2N+2)."""
    s = _as_fraction(shape)
    _require_shape(s)
    _require_positive_depth(depth)
    return Fraction(512, 961) * s ** (2 * depth + 2)


def standard_shape_dyadic_exponent(outer_step: int) -> int:
    """p such that the accepted standard-orbit bound gives s_n < 2^-p."""
    if isinstance(outer_step, bool) or not isinstance(outer_step, int) or outer_step < 0:
        raise ValueError("outer_step must be a nonnegative integer")
    return 3 * (1 << outer_step) - 2


def required_return_depth(target_bits: int, outer_step: int) -> int:
    """Sufficient N for one-step inner error below 2^-target_bits.

    Uses the accepted standard-orbit shape bound and the strict constant
    512/961<1.  At least one return shell is retained so the quadratic class is
    never collapsed to the zero-depth degenerate map.
    """
    if isinstance(target_bits, bool) or not isinstance(target_bits, int) or target_bits < 1:
        raise ValueError("target_bits must be a positive integer")
    exponent = standard_shape_dyadic_exponent(outer_step)
    return max(1, ceil(target_bits / (2 * exponent)) - 1)


def s4_predictive_state_cost(depth: int) -> int:
    """Scalar K4/S4 predictive-state count 12*(2N+1)=24N+12."""
    _require_positive_depth(depth)
    return 24 * depth + 12
