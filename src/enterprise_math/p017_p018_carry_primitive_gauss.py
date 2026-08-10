"""Exact Gauss selection for primitive odd carry Fourier modes.

This supplement sharpens the elementary Gauss bound in
p017_p018_carry_fourier_conductor.py.

Let E be positive odd, Q=2E, and for odd Fourier frequency r define

    G_E(h,r)=(1/Q) sum_(K mod Q)
               exp(2*pi*i [h(K+1)^2-rK]/Q).

Then:

1. if h is even, `G_E(h,r)=0`;
2. if h is odd and g=gcd(h,E) does not divide r, `G_E(h,r)=0`;
3. if h is odd and g|r,

       |G_E(h,r)| = sqrt(g/E).

An elementary proof comes directly from the squared sum.  For the unnormalized
S, write d=K-L.  The L-sum survives exactly when E|hd.  Put E=gE', h=gh', and
d=E't, t mod 2g.  The remaining phase sum is

    sum_(t mod 2g)
      exp(2*pi*i * (g-r)t/(2g)).

For odd h,r the mod-2 factor kills even h.  For odd h, the displayed root sum is
2g exactly when g|r (then r/g is odd) and is zero otherwise.  Hence
`|S|^2=4Eg` in the surviving case and normalization by Q=2E gives the formula.

In particular, if r is odd and gcd(r,E)=1, only odd h coprime to E survive and
every nonzero internal Gauss quantum has magnitude exactly E^(-1/2).  Combining
this with the finite sawtooth coefficients gives the clean primitive bound

    |hat eta_E(r)| <= (1+log E)/sqrt(E).

For an odd squarefree global modulus P, the conductor-triangle theorem says a
primitive global frequency gcd(P,r)=1 receives only the top modulus P.  Thus for
primitive odd r,

    |hat C_P(r)| <= (1+log P)/sqrt(P).

This is a conductor-level square-root estimate for individual modes.  It is not
by itself a pointwise bound on the full Mobius carry field: summing absolute
values over all primitive/nonprimitive frequencies would lose far too much.
Further progress must exploit conductor cancellation, special-phase structure,
or quotient-channel transport rather than an L1 Fourier estimate.
"""

from __future__ import annotations

from math import gcd, log, sqrt

from .p017_p018_carry_fourier_conductor import (
    mobius_carry_field_fourier_coefficient,
    normalized_carry_fourier_coefficient,
    normalized_quadratic_gauss_sum,
)


def exact_odd_frequency_gauss_magnitude(
    modulus: int,
    h: int,
    frequency: int,
) -> dict[str, object]:
    """Verify the exact zero/square-root law for odd external frequency."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    if isinstance(frequency, bool) or not isinstance(frequency, int) or frequency % 2 == 0:
        raise ValueError("frequency must be odd")
    E = modulus
    r = frequency % (2 * E)
    if r % 2 == 0:
        raise AssertionError("odd frequency normalized to even residue")
    g = gcd(h, E)
    if h % 2 == 0 or r % g != 0:
        expected = 0.0
        reason = "PARITY_ZERO" if h % 2 == 0 else "GCD_SELECTION_ZERO"
    else:
        expected = sqrt(g / E)
        reason = "SURVIVING_SQUARE_ROOT_QUANTUM"

    value = normalized_quadratic_gauss_sum(E, h, r)
    if abs(abs(value) - expected) > 1e-9:
        raise AssertionError("odd-frequency Gauss sum violated exact selection law")
    return {
        "modulus": E,
        "h": h,
        "frequency": r,
        "gcd_h_modulus": g,
        "selection_reason": reason,
        "expected_magnitude": expected,
        "actual_magnitude": abs(value),
        "selection_law_verified": True,
    }


def primitive_odd_carry_bound(modulus: int, frequency: int) -> dict[str, object]:
    """Verify |hat eta_E(r)| <= (1+log E)/sqrt(E) for primitive odd r."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1 or modulus % 2 == 0:
        raise ValueError("modulus must be an odd integer >1")
    if isinstance(frequency, bool) or not isinstance(frequency, int) or frequency % 2 == 0:
        raise ValueError("frequency must be odd")
    E = modulus
    r = frequency % (2 * E)
    if gcd(r, E) != 1:
        raise ValueError("frequency must be primitive with respect to E")
    coefficient = normalized_carry_fourier_coefficient(E, r)
    bound = (1.0 + log(E)) / sqrt(E)
    if abs(coefficient) > bound + 1e-10:
        raise AssertionError("primitive odd carry coefficient exceeded harmonic Gauss bound")
    return {
        "modulus": E,
        "frequency": r,
        "coefficient": coefficient,
        "coefficient_magnitude": abs(coefficient),
        "primitive_odd_bound": bound,
        "primitive_odd_bound_verified": True,
    }


def primitive_global_odd_carry_bound(primorial: int, frequency: int) -> dict[str, object]:
    """Verify a primitive global odd mode is top-modulus-only and square-root bounded."""
    if isinstance(primorial, bool) or not isinstance(primorial, int) or primorial <= 1 or primorial % 2 == 0:
        raise ValueError("primorial must be an odd integer >1")
    if isinstance(frequency, bool) or not isinstance(frequency, int) or frequency % 2 == 0:
        raise ValueError("frequency must be odd")
    P = primorial
    r = frequency % (2 * P)
    if gcd(r, P) != 1:
        raise ValueError("global frequency must be primitive with respect to P")
    global_data = mobius_carry_field_fourier_coefficient(P, r)
    if not bool(global_data["primitive_frequency"]):
        raise AssertionError("primitive global frequency was not recognized")
    bound = (1.0 + log(P)) / sqrt(P)
    magnitude = abs(global_data["direct_global_coefficient"])
    if magnitude > bound + 1e-10:
        raise AssertionError("primitive global carry mode exceeded top-modulus bound")
    return {
        **global_data,
        "primitive_odd_bound": bound,
        "primitive_odd_magnitude": magnitude,
        "top_modulus_square_root_bound_verified": True,
    }
