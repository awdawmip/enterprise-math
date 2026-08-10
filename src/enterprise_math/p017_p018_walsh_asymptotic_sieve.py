"""Orientation-Walsh as an exact dimension-one asymptotic-sieve candidate.

Instead of expanding the full endpoint detector at once, split the upper-prime
Walsh weight into a positive lower-side divisor amplifier followed by an upper
small-prime sieve.

For an anchor-surviving odd radius r put

    a(r) = 2^{c_-(r)}
         = product_{p transverse}(1 + 1_{p|M-r}),

and for a squarefree transverse d define

    A_d = sum_{r surviving, d|M+r} a(r).

Expand a(r) over squarefree lower divisors e.  A common prime cannot divide d
and e because it would divide both M-r and M+r while being transverse to M, so
only (d,e)=1 occurs.  Anchor survival is imposed by Mobius over the effective
odd anchor product A, and odd parity contributes the factor 2.  Replacing each
one-class interval count by its continuous CRT density gives the exact
factorized main model

    X = (k-1)/2 * phi(A)/A * product_p(1+1/p),

where p runs over transverse odd primes <=k, and

    X_d = X g(d),
    g(d)=product_{p|d} 1/(p+1).

The actual finite A_d is therefore written exactly as

    A_d = X g(d) + R_d

by definition of the centered/interval remainder R_d.

The key local-density cancellation is

    X * product_p (1-g(p))
      = (k-1)/2 * phi(A)/A,

because (1+1/p)(1-1/(p+1))=1 prime by prime.  Thus the lower divisor amplifier
exactly compensates the logarithmic density loss of the upper prime sieve at the
formal main-term level.  This is the density-level explanation of the
orientation-Walsh mean-one phenomenon.

Classical asymptotic-sieve theory shows that a factorized dimension-one density
law alone does not break the parity problem; an additional bilinear hypothesis
is required.  In the present sequence that missing bilinear object involves

    a(mn) ~ tau_sf(2M-mn)

inside the thin physical strip |mn-M|<k, and after divisor expansion leads to
congruences mn=2M (mod d), hence Kloosterman-fraction / dual-Titchmarsh structure.
This module records the exact local-density layer only.  It does not assert that
the required bilinear axiom has been proved.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod

from .legendre import primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports
from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _transverse_primes(k: int) -> tuple[int, ...]:
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def _factor_squarefree_transverse(d: int, primes: tuple[int, ...]) -> tuple[int, ...]:
    if isinstance(d, bool) or not isinstance(d, int) or d < 1:
        raise ValueError("d must be a positive integer")
    remaining = d
    factors: list[int] = []
    for prime in primes:
        if remaining % prime == 0:
            remaining //= prime
            factors.append(prime)
            if remaining % prime == 0:
                raise ValueError("d must be squarefree")
    if remaining != 1:
        raise ValueError("d must use only declared transverse primes")
    return tuple(factors)


def walsh_continuous_main(k: int) -> dict[str, object]:
    """Return X and the exact prime-by-prime cancellation of X*V."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    K = k - 1
    anchors = effective_odd_anchor_primes(k)
    trans = _transverse_primes(k)

    anchor_density = prod((Fraction(p - 1, p) for p in anchors), start=Fraction(1, 1))
    amplifier_density = prod((Fraction(p + 1, p) for p in trans), start=Fraction(1, 1))
    X = Fraction(K, 2) * anchor_density * amplifier_density
    sieve_V = prod((Fraction(p, p + 1) for p in trans), start=Fraction(1, 1))
    sifted_main = X * sieve_V
    expected_sifted = Fraction(K, 2) * anchor_density
    if sifted_main != expected_sifted:
        raise AssertionError("Walsh amplifier/sieve local factors did not cancel exactly")
    return {
        "k": k,
        "K": K,
        "effective_odd_anchors": anchors,
        "transverse_primes": trans,
        "anchor_density": anchor_density,
        "lower_amplifier_density": amplifier_density,
        "continuous_total_main_X": X,
        "upper_sieve_product_V": sieve_V,
        "continuous_sifted_main": sifted_main,
        "anchor_surviving_continuous_radius_main": expected_sifted,
        "local_density_cancellation": True,
    }


def walsh_sieve_density(k: int, d: int) -> Fraction:
    """Return g(d)=product_{p|d}1/(p+1)."""
    trans = _transverse_primes(k)
    factors = _factor_squarefree_transverse(d, trans)
    return prod((Fraction(1, p + 1) for p in factors), start=Fraction(1, 1))


def actual_lower_amplifier_mass(k: int, d: int = 1) -> dict[str, object]:
    """Evaluate finite A_d and the exact remainder from the continuous main model."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    trans = _transverse_primes(k)
    _factor_squarefree_transverse(d, trans)
    M = k * (k + 1)
    actual = 0
    surviving = 0
    rows: list[dict[str, object]] = []
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        surviving += 1
        lower_support, _upper_support = mirror_transverse_supports(k, radius)
        amplifier = 2 ** len(lower_support)
        selected = (M + radius) % d == 0
        if selected:
            actual += amplifier
        rows.append(
            {
                "radius": radius,
                "lower_support_size": len(lower_support),
                "lower_amplifier": amplifier,
                "selected_by_upper_modulus": selected,
            }
        )

    main_data = walsh_continuous_main(k)
    g = walsh_sieve_density(k, d)
    main = main_data["continuous_total_main_X"] * g
    remainder = Fraction(actual, 1) - main
    return {
        "k": k,
        "d": d,
        "surviving_radius_count": surviving,
        "actual_A_d": actual,
        "g_d": g,
        "continuous_main_X_g_d": main,
        "finite_remainder_R_d": remainder,
        "rows": tuple(rows),
    }
