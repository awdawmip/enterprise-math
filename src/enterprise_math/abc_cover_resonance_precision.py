"""Finite ratio precision of odd-prime cover support resonance.

For an odd cover prime r and lower exponent m, resonance is the ratio equation

    x^m =  1 mod r   (difference),
    x^m = -1 mod r   (sum),

inside F_r^*.  If g=gcd(m,r-1), the difference equation has exactly g roots.
The sum equation has g roots iff (r-1)/g is even, and no roots otherwise.

This module records the exact class count, unit-ratio density, and an elementary
height-window incidence envelope.  It also exposes the saturation boundary:
difference resonance fills all unit ratios when r-1 divides m, while sum
resonance never fills the entire unit-ratio space.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .legendre import is_prime


@dataclass(frozen=True)
class CoverResonancePrecisionState:
    lower_exponent: int
    cover_prime: int
    mode: str
    group_order: int
    exponent_group_gcd: int
    solvable: bool
    resonance_class_count: int
    unit_ratio_density: Fraction
    precision_saturated: bool


def cover_resonance_precision_state(
    lower_exponent: int, cover_prime: int, mode: str
) -> CoverResonancePrecisionState:
    """Return the exact number of resonant ratio classes modulo an odd prime."""
    if isinstance(lower_exponent, bool) or not isinstance(lower_exponent, int) or lower_exponent < 2:
        raise ValueError("lower_exponent must be an integer >=2")
    if isinstance(cover_prime, bool) or not isinstance(cover_prime, int) or cover_prime < 3 or cover_prime % 2 == 0 or not is_prime(cover_prime):
        raise ValueError("cover_prime must be an odd prime")
    if mode not in {"difference", "sum"}:
        raise ValueError("mode must be 'sum' or 'difference'")

    N = cover_prime - 1
    g = gcd(lower_exponent, N)
    if mode == "difference":
        solvable = True
        count = g
    else:
        solvable = (N // g) % 2 == 0
        count = g if solvable else 0

    density = Fraction(count, N)
    saturated = count == N
    if mode == "sum" and saturated:
        raise AssertionError("sum resonance cannot fill all unit ratios")
    if mode == "difference" and saturated != (lower_exponent % N == 0):
        raise AssertionError("difference saturation must be exactly r-1 dividing m")

    return CoverResonancePrecisionState(
        lower_exponent=lower_exponent,
        cover_prime=cover_prime,
        mode=mode,
        group_order=N,
        exponent_group_gcd=g,
        solvable=solvable,
        resonance_class_count=count,
        unit_ratio_density=density,
        precision_saturated=saturated,
    )


def ratio_resonates_mod_cover_prime(
    p: int,
    q: int,
    state: CoverResonancePrecisionState,
) -> bool:
    """Decide the root-of-unity resonance equation for one unit ratio."""
    r = state.cover_prime
    if p % r == 0 or q % r == 0:
        return False
    x = (p % r) * pow(q % r, -1, r) % r
    value = pow(x, state.lower_exponent, r)
    if state.mode == "difference":
        return value == 1
    return value == r - 1


def resonance_height_incidence_upper_bound(
    lower_exponent: int,
    cover_prime: int,
    mode: str,
    height: int,
) -> int:
    """Bound ordered integer pairs <=height lying in resonant unit-ratio classes."""
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be a positive integer")
    state = cover_resonance_precision_state(lower_exponent, cover_prime, mode)
    if not state.solvable:
        return 0
    r = cover_prime
    unit_q_count = height - height // r
    per_nonzero_residue = (height + r - 1) // r
    raw = state.resonance_class_count * unit_q_count * per_nonzero_residue
    return min(height * height, raw)
