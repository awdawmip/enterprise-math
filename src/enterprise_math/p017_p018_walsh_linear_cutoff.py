"""Cutoff-adaptive linear orientation-Walsh prime minorant.

Fix an anchor-surviving mirror radius r around M=k(k+1) and an integer cutoff
2<=z<k.  Split each transverse support into a low band p<=z and a high band
z<p<=k.  For the upper target define

    A_{z,+}(r)=prod_{p<=z}(1+1_{p|M-r}-1_{p|M+r}).

By mirror support disjointness this is zero if the upper side has a low prime,
and otherwise equals 2^(# lower low-band primes).  Let c_{z,+} be the number of
distinct upper support primes in (z,k].  If the upper side is composite and has
no low prime, its least prime factor lies in (z,k], so c_{z,+}>=1.  Therefore

    H_{z,+}(r)=A_{z,+}(r) (1-c_{z,+}(r))

is positive exactly on upper primes and is nonpositive on every upper composite.
The lower orientation is symmetric.  Hence a positive total H_{z,+}+H_{z,-}
is a sufficient Legendre certificate for every declared cutoff z.

On a complete product of transverse prime coordinates the low-band Walsh factors
all have mean one.  High-band first-order hits are independent coordinates with
mean 1/p.  Thus the exact local-model mean of one orientation is

    1 - L_z(k),
    L_z(k)=sum_{z<p<=k, p transverse} 1/p.

For power cutoffs z=k^alpha, classical prime harmonic asymptotics give
L_z(k)->log(1/alpha); in particular the fourth-root/P3 cutoff z~sqrt(k) has
limit margin 1-log 2>0.  This is a local-model statement only; the finite
physical-window boundary discrepancy remains the analytic obstruction.

At the half cutoff C=floor((k-1)/2), every half-rough composite has exactly one
high support prime, so the minorant becomes nonnegative and exact.  The separate
half-cutoff bridge identifies its incidence-optimal version with the existing
incidence-optimal Walsh compiler and terminal Buchstab deletion staircase.
"""

from __future__ import annotations

from fractions import Fraction

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def _split(support: list[int] | tuple[int, ...], cutoff: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    normalized = tuple(int(p) for p in support)
    return tuple(p for p in normalized if p <= cutoff), tuple(p for p in normalized if p > cutoff)


def cutoff_walsh_orientation_point(
    k: int,
    radius: int,
    cutoff: int,
    orientation: str,
) -> dict[str, object]:
    """Evaluate H_{z,+} or H_{z,-} on one surviving mirror radius."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (2 <= cutoff < k):
        raise ValueError("cutoff must satisfy 2<=cutoff<k")
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be 'upper' or 'lower'")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    lower_low, lower_high = _split(lower_support_raw, cutoff)
    upper_low, upper_high = _split(upper_support_raw, cutoff)

    if orientation == "upper":
        target_state = upper_state
        target_low, target_high = upper_low, upper_high
        opposite_low = lower_low
    else:
        target_state = lower_state
        target_low, target_high = lower_low, lower_high
        opposite_low = upper_low

    amplifier = 0 if target_low else 2 ** len(opposite_low)
    high_count = len(target_high) if not target_low else 0
    weight = amplifier * (1 - high_count) if amplifier else 0
    target_prime = is_prime(target_state)
    if target_prime and (target_low or target_high):
        raise AssertionError("prime target retained a transverse support prime")
    if not target_prime and not target_low and high_count < 1:
        raise AssertionError("cutoff-rough composite has no high support prime")
    if (weight > 0) != target_prime:
        raise AssertionError("linear cutoff Walsh weight lost exact positive-prime semantics")
    if not target_prime and weight > 0:
        raise AssertionError("composite target received positive minorant weight")

    return {
        "k": k,
        "radius": radius,
        "cutoff": cutoff,
        "orientation": orientation,
        "target_state": target_state,
        "target_low_support": target_low,
        "target_high_support": target_high,
        "opposite_low_support": opposite_low,
        "low_band_walsh_amplifier": amplifier,
        "high_band_support_count": high_count,
        "linear_cutoff_weight": weight,
        "target_prime": target_prime,
        "positive_iff_target_prime": True,
    }


def cutoff_local_harmonic(k: int, cutoff: int) -> dict[str, object]:
    """Return L_z and the exact complete-coordinate local-model mean 1-L_z."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (2 <= cutoff < k):
        raise ValueError("cutoff must satisfy 2<=cutoff<k")
    M = k * (k + 1)
    high_primes: set[int] = set()
    # The mirror support oracle is not needed here; trial primality is bounded by k.
    for value in range(cutoff + 1, k + 1):
        if value % 2 == 0 or M % value == 0:
            continue
        divisor = 3
        prime = value >= 3
        while divisor * divisor <= value:
            if value % divisor == 0:
                prime = False
                break
            divisor += 2
        if prime:
            high_primes.add(value)
    harmonic = sum((Fraction(1, p) for p in sorted(high_primes)), start=Fraction(0, 1))
    return {
        "k": k,
        "cutoff": cutoff,
        "high_transverse_primes": tuple(sorted(high_primes)),
        "high_band_harmonic_mass": harmonic,
        "one_orientation_complete_coordinate_mean": Fraction(1, 1) - harmonic,
        "positive_local_model_margin": harmonic < 1,
    }


def cutoff_walsh_profile(k: int, cutoff: int) -> dict[str, object]:
    """Aggregate the symmetric cutoff minorant over all anchor-surviving radii."""
    rows: list[dict[str, object]] = []
    total = 0
    prime_exists = False
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        upper = cutoff_walsh_orientation_point(k, radius, cutoff, "upper")
        lower = cutoff_walsh_orientation_point(k, radius, cutoff, "lower")
        pair_weight = int(upper["linear_cutoff_weight"]) + int(lower["linear_cutoff_weight"])
        total += pair_weight
        pair_prime = bool(upper["target_prime"] or lower["target_prime"])
        prime_exists = prime_exists or pair_prime
        rows.append({"radius": radius, "pair_weight": pair_weight, "pair_prime": pair_prime})
    if total > 0 and not prime_exists:
        raise AssertionError("positive cutoff Walsh total fired without a basin prime")

    half = cutoff == reusable_floor_product_cutoff(k)
    if half and k >= 10:
        # At the half cutoff every composite contribution is exactly zero.
        if any(int(row["pair_weight"]) < 0 for row in rows):
            raise AssertionError("half-cutoff terminal compiler retained a negative composite weight")
        if (total > 0) != prime_exists:
            raise AssertionError("half-cutoff terminal compiler lost exact positivity")

    return {
        **cutoff_local_harmonic(k, cutoff),
        "surviving_radius_count": len(rows),
        "symmetric_linear_cutoff_weight": total,
        "prime_exists": prime_exists,
        "positive_total_is_prime_certificate": total <= 0 or prime_exists,
        "half_cutoff_terminal_exact": half and k >= 10,
        "rows": tuple(rows),
    }
