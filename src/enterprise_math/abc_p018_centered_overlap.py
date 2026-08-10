"""Exact small-radical compiler on the P018/P025 centered-prime overlap.

For an activated P025 (2,2) difference atom coming from odd primes
q=center-radius, p=center+radius, Stage 73 gives

    m(radius) >= T * rad(center).

If the same pair lies in the canonical P018 size range q>radius^2, then
``radius^2<center``.  With gcd(radius,center)=1 and n=radius*center,

    T*rad(n) <= radius,
    n^2 < center^3,
    T^2*rad(n)^2 < center.

Thus center<=X compiles the overlap to one integer n below X^(3/2) with radical
below X^(1/2)/T.  The subsequent de Bruijn counting theorem is external prior
art and is not implemented here.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_prime_square_centered_bridge import (
    PrimeSquareCenteredBridge,
    prime_square_centered_bridge,
)
from .abc_support import radical


@dataclass(frozen=True)
class CenteredOverlapSmallRadicalState:
    bridge: PrimeSquareCenteredBridge
    threshold: int
    center_radius_product: int
    product_radical: int
    exact_radius_bound_lhs: int
    product_square: int
    center_cube: int


def centered_overlap_small_radical_state(
    q: int, p: int, threshold: int
) -> CenteredOverlapSmallRadicalState:
    """Compile an activated Stage-73 pair inside the P018 size range."""
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    bridge = prime_square_centered_bridge(q, p)
    if not bridge.in_p018_size_range:
        raise ValueError("centered pair lies outside the P018 q>radius^2 range")
    if bridge.radius_residual < threshold * bridge.center_radical:
        raise ValueError("P025 prime-square atom does not cross the supplied threshold")

    A = bridge.radius
    B = bridge.center
    n = A * B
    rad_n = radical(n)
    if rad_n != radical(A) * radical(B):
        raise AssertionError("coprime centered coordinates lost radical multiplicativity")
    if threshold * rad_n > A:
        raise AssertionError("activated centered pair lost exact small-radical bound")
    if not A * A < B:
        # P018 has B-A>A^2, which is strictly stronger than A^2<B.
        raise AssertionError("P018 size range failed centered radius-square bound")
    if not n * n < B**3:
        raise AssertionError("center-radius product escaped B^(3/2) height")
    if not threshold**2 * rad_n**2 < B:
        raise AssertionError("centered small-radical square bound failed")

    return CenteredOverlapSmallRadicalState(
        bridge=bridge,
        threshold=threshold,
        center_radius_product=n,
        product_radical=rad_n,
        exact_radius_bound_lhs=threshold * rad_n,
        product_square=n * n,
        center_cube=B**3,
    )


def centered_height_power_profile() -> dict[str, tuple[int, int]]:
    """Return formal exponents for the theorem-native de Bruijn input.

    The exact compiler gives n < X^(3/2) and rad(n) < X^(1/2)/T when center<=X.
    Exponents are stored as rational pairs and do not constitute an asymptotic
    proof by themselves.
    """
    return {
        "product_height_power": (3, 2),
        "radical_height_power": (1, 2),
    }
