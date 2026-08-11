"""Nearest-remainder tent descent for nontrivial orientation-Walsh conductors.

Let f be any zero-mean m-periodic function and put

    T_R(f)=sum_(|x|<R) (1-|x|/R) f(x).

If m>R>m/2 and t=m-R, the m-periodized centered tent satisfies pointwise

    G_R(x)=1-t/R+(t/R) G_t(x).

The constant part disappears against sum_(x mod m)f(x)=0, so

    T_R(f)=(t/R)T_t(f).

Apply this after the existing Euclidean selected-modulus descent.  For a
nontrivial odd squarefree conductor m transverse to M=k(k+1), write

    r=k mod m,      0<r<m.

The parent selected Walsh tent column is

    B_m(k)=(r/k) B_m^+(r),

where the child root center is the forward pronic residue r(r+1) mod m.  If
r<=m/2 this is already the nearest-remainder child.  If r>m/2, put t=m-r.  The
tent complement identity gives

    B_m(k)=(t/k) B_m^-(t),

and

    r(r+1) = (-t)(1-t) = t(t-1)       (mod m).

Thus every nontrivial selected conductor has an exact nearest-remainder state

    delta=min(r,m-r) < m/2

plus one binary pronic orientation bit:

    FORWARD  : center delta(delta+1),  r<=m/2;
    BACKWARD : center delta(delta-1),  r>m/2.

No translation of the root function is introduced.  The only repair needed to
make the nearest-remainder collapse future-safe is this forward/backward center
orientation.

For the actual incidence-optimal symmetric reusable core m<=C=floor((k-1)/2),
the previous quotient argument already gives r<k/3; hence delta<k/3 as well,
and m>2*delta.  Every root class at the nearest child is therefore deeply
single-use.

This is an exact Euclidean/BRC precision theorem.  It does not bound the sum over
conductors and does not prove Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff
from .p017_p018_walsh_remainder_descent import selected_modulus_tent_contribution


def _squarefree_odd_factors(modulus: int) -> tuple[int, ...]:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1 or modulus % 2 == 0:
        raise ValueError("modulus must be an odd integer >1")
    remaining = modulus
    factors: list[int] = []
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors.append(p)
            if remaining % p == 0:
                raise ValueError("modulus must be squarefree")
        p += 2
    if remaining > 1:
        factors.append(remaining)
    product = 1
    for p in factors:
        product *= p
    if product != modulus:
        raise AssertionError("squarefree factorization failed")
    return tuple(factors)


def signed_root_value(center: int, x: int, modulus: int) -> int:
    """Return the product of +/- root signs for a fixed center modulo m."""
    factors = _squarefree_odd_factors(modulus)
    if gcd(center, modulus) != 1:
        raise ValueError("center must be transverse to modulus")
    sign = 1
    for p in factors:
        if (center - x) % p == 0:
            continue
        if (center + x) % p == 0:
            sign = -sign
            continue
        return 0
    return sign


def generalized_selected_tent(center: int, radius: int, modulus: int) -> Fraction:
    """Return the exact centered tent sum for an arbitrary transverse root center."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 1:
        raise ValueError("radius must be a positive integer")
    _squarefree_odd_factors(modulus)
    if gcd(center, modulus) != 1:
        raise ValueError("center must be transverse to modulus")
    total = Fraction(0, 1)
    for x in range(-radius + 1, radius):
        value = signed_root_value(center, x, modulus)
        if value:
            total += value * Fraction(radius - abs(x), radius)
    return total


def periodic_root_mean(center: int, modulus: int) -> int:
    """Return one-period root-sign sum and certify it is zero for m>1."""
    total = sum(signed_root_value(center, x, modulus) for x in range(modulus))
    if total != 0:
        raise AssertionError("nontrivial signed root function retained nonzero period mean")
    return total


def tent_complement_identity(center: int, modulus: int, radius: int) -> dict[str, object]:
    """Verify T_R=(t/R)T_t for m>R>m/2 and a fixed zero-mean root phase."""
    if not (modulus > radius and 2 * radius > modulus):
        raise ValueError("require m>R>m/2")
    if gcd(center, modulus) != 1:
        raise ValueError("center must be transverse to modulus")
    periodic_root_mean(center, modulus)
    t = modulus - radius
    large = generalized_selected_tent(center, radius, modulus)
    small = generalized_selected_tent(center, t, modulus)
    reconstructed = Fraction(t, radius) * small
    if large != reconstructed:
        raise AssertionError("zero-mean tent complement identity failed")
    return {
        "center": center,
        "modulus_m": modulus,
        "large_radius_R": radius,
        "complement_radius_t": t,
        "large_tent": large,
        "small_tent": small,
        "reconstructed_large_tent": reconstructed,
        "zero_mean_constant_term_cancelled": True,
        "tent_complement_identity": True,
    }


def nearest_remainder_selected_descent(k: int, modulus: int) -> dict[str, object]:
    """Collapse B_m(k) to delta=min(r,m-r) with a forward/backward pronic bit."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    _squarefree_odd_factors(modulus)
    parent_center = k * (k + 1)
    if gcd(parent_center, modulus) != 1:
        raise ValueError("modulus must be transverse to k(k+1)")
    r = k % modulus
    if r == 0:
        raise AssertionError("transverse modulus divided k")

    parent = selected_modulus_tent_contribution(k, modulus)
    forward_center = r * (r + 1)
    forward = generalized_selected_tent(forward_center, r, modulus)
    if parent != Fraction(r, k) * forward:
        raise AssertionError("ordinary Euclidean selected descent failed in generalized tent coordinates")

    if 2 * r <= modulus:
        delta = r
        orientation = "FORWARD"
        child_center = delta * (delta + 1)
        child = forward
    else:
        delta = modulus - r
        orientation = "BACKWARD"
        child_center = delta * (delta - 1)
        if (child_center - forward_center) % modulus:
            raise AssertionError("forward child center did not become backward pronic modulo m")
        complement = tent_complement_identity(forward_center, modulus, r)
        child = generalized_selected_tent(child_center, delta, modulus)
        if child != complement["small_tent"]:
            raise AssertionError("backward-pronic child changed the root phase")

    reconstructed = Fraction(delta, k) * child
    if parent != reconstructed:
        raise AssertionError("nearest-remainder selected descent failed")
    if not 2 * delta <= modulus:
        raise AssertionError("nearest remainder escaped half-modulus radius")

    C = reusable_floor_product_cutoff(k)
    reusable_core = modulus <= C
    if reusable_core:
        if not 3 * delta < k:
            raise AssertionError("reusable symmetric-core nearest child escaped one-third parent scale")
        if not modulus > 2 * delta:
            # Equality can only occur for even modulus, excluded here.
            raise AssertionError("reusable-core conductor is not deeply single-use at nearest child")

    return {
        "k": k,
        "parent_center": parent_center,
        "modulus_m": modulus,
        "ordinary_remainder_r": r,
        "nearest_remainder_delta": delta,
        "pronic_orientation": orientation,
        "child_center": child_center,
        "parent_selected_tent": parent,
        "child_selected_tent": child,
        "transport_weight_delta_over_k": Fraction(delta, k),
        "reconstructed_parent": reconstructed,
        "nearest_remainder_at_most_half_modulus": 2 * delta <= modulus,
        "reusable_symmetric_core": reusable_core,
        "reusable_core_child_below_one_third": (not reusable_core) or 3 * delta < k,
        "reusable_core_conductor_exceeds_twice_child": (not reusable_core) or modulus > 2 * delta,
        "nearest_remainder_descent_exact": True,
    }
