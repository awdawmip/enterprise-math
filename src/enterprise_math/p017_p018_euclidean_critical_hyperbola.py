"""Critical q*d hyperbola joining Euclidean Poisson precision to P017 reuse.

After tent-Poisson completion and frequency-conductor descent, a primitive
conductor q paired with an opposite-side divisor channel d has natural scale

    H_q = q*d/k.

This creates an exact structural split.

LOW / reusable region: q*d <= k.
--------------------------------
Here H_q<=1.  Since the tent transform satisfies

    |W_hat(x)| <= 1/(pi^2*x^2)  for |x|>=1,

the entire nonzero-frequency contribution, after the Poisson prefactor 1/H_q,
is bounded by

    H_q/3 = q*d/(3k).

The zero-frequency main is 1/H_q=k/(q*d), so the relative oscillatory error is
at most H_q^2/3.  No Kloosterman cancellation is required in this region.

HIGH / single-use region: q*d > k.
---------------------------------
In a physical surviving mirror radius r, q lies on one side and d on the other:

    q | M+r,
    d | M-r.

The mirror support disjointness gives gcd(q,d)=1 for transverse channels.  Hence
r is determined by one CRT class

    r=-M (mod q),
    r= M (mod d)

modulo q*d.  Since the physical interval has 1<=r<k<q*d, this cross-orientation
(q,d) token occurs at most once in the entire basin.

Thus the same critical surface q*d=k separates a reusable density regime from a
globally single-use boundary regime.  This does NOT imply that the high region
is small: one radius may carry many high cross-tokens.  The intended compiler is
therefore hybrid -- estimate the low region in column/Poisson coordinates and
repack the high region by its unique physical radius instead of taking tokenwise
absolute values.

This module records the exact structural split only; it does not prove the
row-repacked high contribution is small or prove Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, pi


def low_hyperbola_poisson_bounds(k: int, q: int, d: int) -> dict[str, object]:
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 1 for value in (k, q, d)):
        raise ValueError("k,q,d must be positive integers")
    H = Fraction(q * d, k)
    if H > 1:
        raise ValueError("low-hyperbola theorem requires q*d<=k")
    main = Fraction(k, q * d)
    oscillation_ceiling = Fraction(q * d, 3 * k)
    relative_ceiling = Fraction(q * q * d * d, 3 * k * k)
    return {
        "k": k,
        "q": q,
        "d": d,
        "frequency_scale_H_q": H,
        "zero_frequency_main": main,
        "nonzero_frequency_absolute_ceiling": oscillation_ceiling,
        "relative_oscillation_ceiling": relative_ceiling,
        "deterministic_main_dominated": True,
    }


def cross_orientation_reuse_capacity(k: int, center: int, q: int, d: int) -> dict[str, object]:
    """Return the elementary CRT capacity for q|M+r and d|M-r in 1<=r<k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(center, bool) or not isinstance(center, int) or center < 1:
        raise ValueError("center must be positive")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 1 for value in (q, d)):
        raise ValueError("q,d must be positive integers")
    if gcd(q, d) != 1:
        raise ValueError("cross-orientation CRT capacity requires gcd(q,d)=1")
    modulus = q * d
    # CRT residue constructed without requiring primality/squarefreeness.
    residue = ((-center) + q * (((2 * center) * pow(q, -1, d)) % d)) % modulus
    hits = tuple(r for r in range(1, k) if r % modulus == residue)
    direct = tuple(r for r in range(1, k) if (center + r) % q == 0 and (center - r) % d == 0)
    if hits != direct:
        raise AssertionError("cross-orientation CRT residue missed direct channels")
    capacity_ceiling = (k - 1) // modulus + 1
    if len(hits) > capacity_ceiling:
        raise AssertionError("cross-orientation reuse exceeded interval-class capacity")
    single_use = modulus > k - 1
    if single_use and len(hits) > 1:
        raise AssertionError("high cross-token reused inside the basin")
    return {
        "k": k,
        "center": center,
        "q": q,
        "d": d,
        "cross_modulus": modulus,
        "crt_radius_residue": residue,
        "physical_hits": hits,
        "reuse_capacity_ceiling": capacity_ceiling,
        "globally_single_use": single_use,
    }


def critical_hyperbola_classification(k: int, center: int, q: int, d: int) -> dict[str, object]:
    """Classify one q,d pair as low reusable or high single-use when coprime."""
    if gcd(q, d) != 1:
        raise ValueError("q,d must be coprime")
    product_value = q * d
    if product_value <= k:
        low = low_hyperbola_poisson_bounds(k, q, d)
        return {
            "region": "LOW_REUSABLE_MAIN_DOMINATED",
            "product_qd": product_value,
            "low_poisson": low,
            "high_capacity": None,
        }
    high = cross_orientation_reuse_capacity(k, center, q, d)
    if not bool(high["globally_single_use"]):
        raise AssertionError("qd>k failed single-use classification")
    return {
        "region": "HIGH_SINGLE_USE_BOUNDARY",
        "product_qd": product_value,
        "low_poisson": None,
        "high_capacity": high,
    }
