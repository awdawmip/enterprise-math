"""Half-cutoff semantic bridge for the incidence-optimal orientation-Walsh detector.

Fix k>=10, M=k(k+1), K=k-1 and

    C = floor((k-1)/2).

On an anchor-surviving mirror radius let L,U be the transverse prime supports of
M-r and M+r, and split them at C.  If the upper side has a prime <=C then the
low-band upper sieve kills that side.  If it has no prime <=C, then an upper
composite has exactly one distinct prime p with C<p<=k: its least prime factor
p lies in that band and the cofactor q is a prime >k; a third factor >C would
exceed the square-basin ceiling for k>=10.  Thus

    upper prime  <=>  U_low is empty and |U_high|=0,
    upper composite half-rough <=> U_low is empty and M+r=p*q,
                                      C<p<=k<q.

Let h_*(S) be the existing incidence-optimal Walsh support weight, the number
of squarefree support divisors <=C.  Since a divisor <=C cannot use a support
prime >C,

    h_*(L)=h_*(L_low).

Therefore

    H_+(r)=h_*(L_low) 1_{U_low=empty} (1-|U_high|)

is nonnegative and positive exactly when M+r is prime.  On a prime side it is
exactly the existing incidence-optimal prime weight.  The lower orientation is
symmetric.

The composite deletions form a sparse bipartite matching geometry.  Every high
p>C has period 2p>K and therefore labels at most one radius in each orientation
(left degree <=2).  The large tail q>k is globally nonreused: if the same odd q
divided two signed basin states, it would divide their nonzero even difference
of magnitude <2q, impossible.  Hence right degree <=1.  If one p occurs in both
orientations, the two q tails are the adjacent odd candidates from the terminal
Buchstab staircase and differ by 2.

This gives the incidence-optimal Walsh compiler a terminal Buchstab meaning:
low-band amplified half-rough mass minus a weighted sparse matching of single-
use p*q deletions.  The theorem is an exact representation bridge, not an
estimate of the matching weight and not a Legendre proof.
"""

from __future__ import annotations

from collections import defaultdict

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
    high_prime = None
    large_tail_prime = None
    if half_rough and not target_prime:
        if len(target_high) != 1:
            raise AssertionError("half-rough composite did not have exactly one high support prime")
        high_prime = int(target_high[0])
        if target_state % high_prime:
            raise AssertionError("declared high support prime does not divide target")
        large_tail_prime = target_state // high_prime
        if large_tail_prime <= k or not is_prime(large_tail_prime):
            raise AssertionError("half-rough composite did not factor as p*q with q>k prime")
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
        "terminal_high_prime": high_prime,
        "terminal_large_tail_prime": large_tail_prime,
        "half_cutoff_terminal_weight": weight,
        "high_prime_deletion_single_use": (not target_high) or 2 * target_high[0] > k - 1,
        "exact_prime_detector": True,
    }


def half_cutoff_bridge_profile(k: int) -> dict[str, object]:
    """Aggregate both orientations and expose the weighted terminal matching identity."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")

    rows: list[dict[str, object]] = []
    low_band_mass = 0
    deletion_mass = 0
    prime_weight = 0
    deletion_edges: list[dict[str, object]] = []
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
                    deletion_edges.append(
                        {
                            "orientation": orientation,
                            "radius": radius,
                            "p": int(row["terminal_high_prime"]),
                            "q": int(row["terminal_large_tail_prime"]),
                            "target_state": int(row["target_state"]),
                            "opposite_amplifier_weight": amp,
                        }
                    )
                prime_weight += int(row["half_cutoff_terminal_weight"])

    if low_band_mass - deletion_mass != prime_weight:
        raise AssertionError("weighted half-cutoff Buchstab identity failed")

    # Left degree <=2: one p can occur at most once in each orientation.
    left_orientation_labels = [(str(edge["orientation"]), int(edge["p"])) for edge in deletion_edges]
    if len(left_orientation_labels) != len(set(left_orientation_labels)):
        raise AssertionError("a high-prime deletion label was reused within one orientation")
    left_rows: dict[int, list[dict[str, object]]] = defaultdict(list)
    for edge in deletion_edges:
        left_rows[int(edge["p"])].append(edge)
    if any(len(edges) > 2 for edges in left_rows.values()):
        raise AssertionError("terminal high-prime matching left degree exceeded two")
    for edges in left_rows.values():
        if len(edges) == 2:
            q_values = sorted(int(edge["q"]) for edge in edges)
            if q_values[1] - q_values[0] != 2:
                raise AssertionError("double-orientation high-prime deletion did not produce twin q tails")

    # Right degree <=1: a q>k cannot divide two distinct odd basin states.
    q_values = [int(edge["q"]) for edge in deletion_edges]
    if len(q_values) != len(set(q_values)):
        raise AssertionError("large terminal tail prime was reused across deletion edges")

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
        "deletion_edges": tuple(deletion_edges),
        "left_high_prime_degree_ceiling": 2,
        "right_large_tail_degree_ceiling": 1,
        "terminal_deletion_graph_is_sparse_matching": True,
        "rows": tuple(rows),
    }
