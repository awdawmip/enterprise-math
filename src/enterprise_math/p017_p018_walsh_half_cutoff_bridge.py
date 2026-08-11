"""Half-cutoff semantic bridge for the incidence-optimal orientation-Walsh detector.

Fix k>=10, M=k(k+1), K=k-1 and

    C = floor((k-1)/2).

On an anchor-surviving mirror radius let L,U be the transverse prime supports of
M-r and M+r, and split them at C.  If the upper side has a prime <=C then the
low-band upper sieve kills that side.  If it has no prime <=C, then an upper
composite has exactly one distinct prime p with C<p<=k: its least prime factor
p lies in that band and the cofactor is >k; a third factor >C would exceed the
square-basin ceiling for k>=10.  Thus

    upper prime  <=>  U_low is empty and |U_high|=0,
    upper composite half-rough <=> U_low is empty and |U_high|=1.

Let h_*(S) be the existing incidence-optimal Walsh support weight, the number
of squarefree support divisors <=C.  Since a divisor <=C cannot use a support
prime >C,

    h_*(L)=h_*(L_low).

Therefore

    H_+(r)=h_*(L_low) 1_{U_low=empty} (1-|U_high|)

is nonnegative and positive exactly when M+r is prime.  On a prime side it is
exactly the existing incidence-optimal prime weight.  The lower orientation is
symmetric.

This gives the incidence-optimal Walsh compiler a terminal Buchstab meaning:
low-band amplified half-rough mass minus a matching family of single-use high-
prime composite deletions.  Every p>C has period 2p>K, so one orientation has
at most one physical radius for that p.  The theorem is an exact representation
bridge, not an estimate of the weighted deletion mass and not a Legendre proof.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_walsh_incidence_optimal import (
    incidence_optimal_prime_weight,
    incidence_optimal_weight,
)
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def _split_support(k: int, support: list[int] | tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    cutoff = reusable_floor_product_cutoff(k)
    normalized = tuple(int(p) for p in support)
    return (
        tuple(p for p in normalized if p <= cutoff),
        tuple(p for p in normalized if p > cutoff),
    )


def half_cutoff_orientation_weight(k: int, radius: int, orientation: str) -> dict[str, object]:
    """Return one incidence-optimal half-cutoff prime-side weight."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be 'upper' or 'lower'")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    lower_low, lower_high = _split_support(k, lower_support_raw)
    upper_low, upper_high = _split_support(k, upper_support_raw)

    if orientation == "upper":
        target_state = upper_state
        target_low, target_high = upper_low, upper_high
        opposite_low = lower_low
    else:
        target_state = lower_state
        target_low, target_high = lower_low, lower_high
        opposite_low = upper_low

    half_rough = not target_low
    target_prime = is_prime(target_state)
    if half_rough and not target_prime and len(target_high) != 1:
        raise AssertionError("half-rough composite did not have exactly one high support prime")
    if target_prime and (target_low or target_high):
        raise AssertionError("prime target retained a transverse support prime")

    amplifier = incidence_optimal_weight(k, opposite_low) if half_rough else 0
    high_count = len(target_high) if half_rough else 0
    weight = amplifier * (1 - high_count) if half_rough else 0
    if weight < 0:
        raise AssertionError("half-cutoff terminal weight became negative")
    if (weight > 0) != target_prime:
        raise AssertionError("half-cutoff bridge lost exact prime positivity")

    if target_prime:
        canonical = incidence_optimal_prime_weight(k, target_state)
        if int(canonical["incidence_optimal_prime_weight"]) != weight:
            raise AssertionError("half-cutoff prime weight disagrees with incidence-optimal compiler")

    cutoff = reusable_floor_product_cutoff(k)
    if any(p <= cutoff for p in target_high) or any(p > cutoff for p in target_low):
        raise AssertionError("support split crossed the half cutoff")
    if target_high and 2 * target_high[0] <= k - 1:
        raise AssertionError("high-prime deletion is not single-use in the radius window")

    return {
        "k": k,
        "radius": radius,
        "orientation": orientation,
        "reusable_floor_product_cutoff": cutoff,
        "target_state": target_state,
        "target_low_support": target_low,
        "target_high_support": target_high,
        "opposite_low_support": opposite_low,
        "half_rough": half_rough,
        "target_prime": target_prime,
        "low_band_incidence_optimal_amplifier": amplifier,
        "terminal_high_prime_hit_count": high_count,
        "half_cutoff_terminal_weight": weight,
        "high_prime_deletion_single_use": (not target_high) or 2 * target_high[0] > k - 1,
        "exact_prime_detector": True,
    }


def half_cutoff_bridge_profile(k: int) -> dict[str, object]:
    """Aggregate both orientations and expose the weighted terminal deletion identity."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    rows: list[dict[str, object]] = []
    low_band_mass = 0
    deletion_mass = 0
    prime_weight = 0
    deletion_labels: list[tuple[str, int, int]] = []
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        for orientation in ("upper", "lower"):
            row = half_cutoff_orientation_weight(k, radius, orientation)
            rows.append(row)
            if bool(row["half_rough"]):
                amp = int(row["low_band_incidence_optimal_amplifier"])
                low_band_mass += amp
                if int(row["terminal_high_prime_hit_count"]) == 1:
                    deletion_mass += amp
                    p = int(row["target_high_support"][0])
                    deletion_labels.append((orientation, p, radius))
                prime_weight += int(row["half_cutoff_terminal_weight"])

    if low_band_mass - deletion_mass != prime_weight:
        raise AssertionError("weighted half-cutoff Buchstab identity failed")
    # Each high prime can hit at most one radius in a fixed orientation because 2p>K.
    labels = [(orientation, p) for orientation, p, _r in deletion_labels]
    if len(labels) != len(set(labels)):
        raise AssertionError("a high-prime deletion label was reused within one orientation")

    prime_exists = prime_weight > 0
    return {
        "k": k,
        "reusable_floor_product_cutoff": reusable_floor_product_cutoff(k),
        "low_band_amplified_half_rough_mass": low_band_mass,
        "single_use_high_prime_deletion_mass": deletion_mass,
        "incidence_optimal_weighted_prime_signal": prime_weight,
        "weighted_terminal_identity": True,
        "prime_exists": prime_exists,
        "positive_iff_prime_exists": prime_exists == any(bool(row["target_prime"]) for row in rows),
        "deletion_labels": tuple(deletion_labels),
        "rows": tuple(rows),
    }
