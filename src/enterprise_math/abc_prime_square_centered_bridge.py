"""Centered-prime bridge for the cutoff-five (2,2) difference atom.

Let p>q be distinct odd primes and set

    center = (p+q)/2,
    radius = (p-q)/2.

Then q=center-radius and p=center+radius.  The P025 difference-of-prime-squares
relation is

    q^2 + 4*center*radius = p^2.

Because center and radius are coprime and have opposite parity,

    m(4*center*radius) = 4*m(center)*m(radius).

The complement capacities are both two, so the b-oriented projective term is
exactly

    rho = m(radius) / rad(center).

The same centered coordinates underlie P018, where the quadratic shell state is
``center^2-radius^2=p*q``.  P025 instead reads the dual quadratic coordinate
``(center+radius)^2-(center-radius)^2=4*center*radius``.  Shared coordinates do
not imply that the P025 radius is the *minimal* P018 centered-prime radius.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import multiplicity_residual, prime_factorization, radical
from .centered_prime_radius import centered_prime_pair, centered_shell_data


@dataclass(frozen=True)
class PrimeSquareCenteredBridge:
    left_prime: int
    right_prime: int
    center: int
    radius: int
    abc: tuple[int, int, int]
    p018_product_shell: int
    p025_difference_shell: int
    projective_atom_value: Fraction
    radius_residual: int
    center_radical: int
    in_p018_size_range: bool


def _require_odd_prime(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 3:
        raise ValueError(f"{name} must be an odd prime")
    if prime_factorization(value) != ((value, 1),):
        raise ValueError(f"{name} must be prime")


def prime_square_centered_bridge(q: int, p: int) -> PrimeSquareCenteredBridge:
    """Return the exact P018/P025 centered-coordinate bridge for odd primes p>q."""
    _require_odd_prime("q", q)
    _require_odd_prime("p", p)
    if p <= q:
        raise ValueError("require p>q")
    center = (p + q) // 2
    radius = (p - q) // 2
    if center - radius != q or center + radius != p:
        raise AssertionError("center/radius reconstruction failed")
    if gcd(center, radius) != 1:
        raise AssertionError("distinct odd prime centered coordinates must be coprime")
    if center % 2 == radius % 2:
        raise AssertionError("center and radius must have opposite parity")
    if centered_prime_pair(center, radius) != (q, p):
        raise AssertionError("P018 centered-prime coordinate recognition failed")

    product_shell = center * center - radius * radius
    if product_shell != p * q:
        raise AssertionError("P018 product shell identity failed")
    difference_shell = 4 * center * radius
    if difference_shell != p * p - q * q:
        raise AssertionError("P025 difference shell identity failed")

    # P025 abc orientation: q^2 + (p^2-q^2) = p^2.
    triple = (q * q, difference_shell, p * p)
    state = projective_capacity_condition_state(*triple)
    b_oriented = state.cyclic_weighted_defects[1]
    closed = Fraction(multiplicity_residual(radius), radical(center))
    if b_oriented != closed:
        raise AssertionError("prime-square centered projective formula failed")

    return PrimeSquareCenteredBridge(
        left_prime=q,
        right_prime=p,
        center=center,
        radius=radius,
        abc=triple,
        p018_product_shell=product_shell,
        p025_difference_shell=difference_shell,
        projective_atom_value=closed,
        radius_residual=multiplicity_residual(radius),
        center_radical=radical(center),
        in_p018_size_range=q > radius * radius,
    )


def p018_centered_shell_bridge(q: int, p: int) -> dict[str, object]:
    """Return P018 centered-shell data when its explicit size hypothesis holds."""
    bridge = prime_square_centered_bridge(q, p)
    if not bridge.in_p018_size_range:
        raise ValueError("centered prime pair lies outside P018 left-prime>radius^2 range")
    data = centered_shell_data(bridge.center, bridge.radius)
    if data["shell"] != [bridge.p018_product_shell]:
        raise AssertionError("P018 shell disagreed with centered bridge product")
    return {
        "bridge": bridge,
        "p018_shell_data": data,
    }


def prime_square_difference_threshold_holds(q: int, p: int, threshold: int) -> bool:
    """Decide the P025 difference-shell projective threshold in centered coordinates."""
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    bridge = prime_square_centered_bridge(q, p)
    return bridge.radius_residual >= threshold * bridge.center_radical
