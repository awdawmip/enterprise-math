"""Reflection split for deep single-digit Franel zeros.

The p^2 Jarvis--Verrill lift already proves, at a single-digit p-zero n with
mirror m=p-1-n,

    (-8)^n (F_m/p) = (F_n/p) - F'_n                 (mod p).

If n is deep, p^2|F_n, the first quotient on the right vanishes and therefore

    (-8)^n (F_m/p) = -F'_n                           (mod p).

This gives an exact dichotomy which is useful for the remaining Barlow
transport branches:

* if F'_n is nonzero mod p, the reflected zero m is simple;
* if F'_n is zero mod p, the reflected zero is deep as well.

Thus a deep/deep reflected pair is equivalent to a multiple root of the
single-digit Franel interpolation polynomial: F_n=F'_n=0 (mod p).  In
particular a deep forced midpoint, being self-reflected, is necessarily such a
multiple-root event.

The p^2 reflection formula and Straub formal derivative are provided by the
existing P022 reflection module.  This file only packages the deep-zero
consequence so higher-level escape arguments do not need to treat arbitrary
p-adic depth as an untyped branch.
"""

from __future__ import annotations

from .p022_barlow_franel_gessel_lucas_copy import (
    _fraction_mod,
    franel_formal_derivative,
)
from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_reflection_first_jet import zero_reflection_quotient_residue
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def digit_root_is_multiple(prime: int, index: int) -> bool:
    """Whether F_index=F'_index=0 modulo p in the single-digit range."""
    _require_odd_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    if triple_moment_factor(index) % prime:
        return False
    derivative = _fraction_mod(franel_formal_derivative(index), prime)
    return derivative == 0


def deep_zero_reflection_split(
    prime: int,
    index: int,
) -> tuple[str, int, int, int]:
    """Classify a deep zero by the exact depth of its reflected first quotient.

    Returns ``(branch,mirror,derivative,mirror_depth)``.  Branch is
    ``simple-mirror`` when F'_index is nonzero and ``deep-mirror`` when the
    derivative vanishes.
    """
    _require_odd_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    if p_adic_valuation(triple_moment_factor(index), prime) < 2:
        raise ValueError("index must be a deep Franel p-zero")

    mirror = prime - 1 - index
    u, v, derivative, scale = zero_reflection_quotient_residue(prime, index)
    if u != 0:
        raise AssertionError("a deep source zero must have zero first quotient")
    if scale * v % prime != (-derivative) % prime:
        raise AssertionError("deep reflection quotient law changed")

    mirror_depth = p_adic_valuation(triple_moment_factor(mirror), prime)
    if derivative:
        if v == 0 or mirror_depth != 1:
            raise AssertionError("transverse deep zero must reflect to a simple zero")
        return "simple-mirror", mirror, derivative, mirror_depth

    if v != 0 or mirror_depth < 2:
        raise AssertionError("multiple digit root must have a deep reflected zero")
    if not digit_root_is_multiple(prime, index):
        raise AssertionError("deep/deep branch must be the multiple-root locus")
    return "deep-mirror", mirror, derivative, mirror_depth


def deep_reflected_pair_iff_multiple_root(prime: int, index: int) -> bool:
    """For a deep digit zero, certify mirror deep iff F'_index=0 mod p."""
    branch, mirror, derivative, mirror_depth = deep_zero_reflection_split(prime, index)
    mirror_deep = mirror_depth >= 2
    multiple = derivative == 0
    if mirror_deep != multiple:
        raise AssertionError("deep reflected pair and multiple-root status must coincide")
    if (branch == "deep-mirror") != multiple:
        raise AssertionError("deep reflection branch label changed")
    _ = mirror
    return multiple


def deep_forced_midpoint_is_multiple_root(prime: int) -> bool:
    """A self-reflected forced midpoint can be deep only on the multiple-root locus."""
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("prime must lie in the forced-midpoint mod-8 sector")
    midpoint = half_index(prime)
    if p_adic_valuation(triple_moment_factor(midpoint), prime) < 2:
        raise ValueError("forced midpoint is not deep")
    branch, mirror, derivative, mirror_depth = deep_zero_reflection_split(prime, midpoint)
    if mirror != midpoint or branch != "deep-mirror" or derivative != 0 or mirror_depth < 2:
        raise AssertionError("a deep self-reflected midpoint must be a multiple digit root")
    return True
