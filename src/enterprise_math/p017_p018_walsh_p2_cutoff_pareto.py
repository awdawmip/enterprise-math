"""Exact P2-to-half cutoff Pareto for the linear orientation-Walsh detector.

Let M=k(k+1), K=k-1 and let

    z2=floor((k^2+2k)^(1/3))

be the exact product-certified P2 cutoff.  For every integer cutoff

    z2 <= z <= C=floor((k-1)/2),

a target side that has no transverse prime <=z is either prime or a semiprime

    p*q,       z<p<=k<q.

Indeed z>=z2 makes every z-rough basin state have Omega<=2, and a composite
state above k^2 has one factor <=k and the other >k.  Hence its visible target
support in (z,k] has size exactly one.

For one orientation let L_z be the opposite transverse support <=z and let U_z
be the target support <=z.  Use the existing incidence-optimal support weight
on L_z,

    h_z(L)=#{squarefree d|rad(L): d<=C}.

Then

    H_z = h_z(L_z) * 1_{U_z empty} * (1-c_high)

is nonnegative and positive exactly when the target side is prime.  Thus the
whole interval z2<=z<=C is an **exact linear-Walsh zone**; below z2 higher
factor-depth composites can make c_high>=2 and the same linear weight becomes
only a minorant.

The terminal composite deletions form p*q edges.  The large tail q>k is globally
nonreused.  The high factor p>z has P017 signed reuse capacity

    m_p <= floor(K/p)+1 <= floor(K/(z+1))+1.

Therefore cutoff depth trades directly against deletion reuse width.  At the
minimal P2 cutoff the universal width is O(k^(1/3)); at the half cutoff it is at
most two.

There is also an exact monotone refinement flow.  On a basin prime target, its
weight is the count of opposite-support squarefree divisors <=C whose prime
factors have already entered the cutoff.  Raising z can only add such divisors,
so the weighted prime signal is monotone nondecreasing.  If the cutoff crosses
an opposite-side prime ell, the pointwise increment is exactly

    Delta_ell h_C(S)=#{d|rad(S_old): d<=C/ell}.

Thus each precision refinement adds a child divisor budget floor(C/ell).  At the
same time terminal edges whose high factor has crossed into the low band vanish,
and the universal reuse-width ceiling decreases.  Deeper precision therefore
improves semantic signal and reuse depth simultaneously, at the cost of a
larger low-band incidence language.  This is a P017/P018 proof-depth/reuse-width
Pareto theorem, not an estimate of the weighted edge mass and not a Legendre
proof.
"""

from __future__ import annotations

from collections import defaultdict

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff
from .p017_p018_walsh_incidence_optimal import incidence_optimal_weight
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def p2_cutoff(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")
    return int(almost_prime_cutoff(k, 2)["cutoff"])


def exact_linear_cutoff_zone(k: int) -> tuple[int, int]:
    """Return [z2,C], the exact linear-Walsh cutoff interval."""
    z2 = p2_cutoff(k)
    C = reusable_floor_product_cutoff(k)
    if z2 > C:
        raise ValueError("k is below the stable P2-to-half cutoff zone")
    return z2, C


def cutoff_reuse_width_ceiling(k: int, cutoff: int) -> int:
    """Return floor((k-1)/(z+1))+1, the universal high-p signed reuse ceiling."""
    z2, C = exact_linear_cutoff_zone(k)
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (z2 <= cutoff <= C):
        raise ValueError("cutoff must lie in the exact linear-Walsh zone")
    return (k - 1) // (cutoff + 1) + 1


def _low_support(support: list[int] | tuple[int, ...], cutoff: int) -> tuple[int, ...]:
    return tuple(int(p) for p in support if int(p) <= cutoff)


def divisor_budget_weight(support: tuple[int, ...], budget: int) -> int:
    """Return #{squarefree support divisors <=budget}."""
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a nonnegative integer")
    values = [1]
    for prime in tuple(sorted(int(p) for p in support)):
        if prime < 3:
            raise ValueError("support entries must be odd primes")
        values += [value * prime for value in values if value <= budget // prime]
    return len(values) if budget >= 1 else 0


def cutoff_refinement_quantum(
    k: int,
    old_visible_support: tuple[int, ...],
    new_prime: int,
) -> dict[str, object]:
    """Return h_C(S union {ell})-h_C(S)=h_floor(C/ell)(S)."""
    _z2, C = exact_linear_cutoff_zone(k)
    support = tuple(sorted(int(p) for p in old_visible_support))
    ell = int(new_prime)
    if ell in support:
        raise ValueError("new_prime must not already be visible")
    old_weight = divisor_budget_weight(support, C)
    new_weight = divisor_budget_weight(tuple(sorted(support + (ell,))), C)
    child_budget = C // ell
    child_weight = divisor_budget_weight(support, child_budget)
    if new_weight - old_weight != child_weight:
        raise AssertionError("cutoff refinement quantum failed divisor-budget recursion")
    return {
        "k": k,
        "half_cutoff_budget": C,
        "old_visible_support": support,
        "new_prime": ell,
        "child_divisor_budget": child_budget,
        "old_weight": old_weight,
        "new_weight": new_weight,
        "refinement_increment": child_weight,
        "positive_refinement_quantum": child_weight >= 0,
        "divisor_budget_recursion": True,
    }


def p2_zone_orientation_weight(k: int, radius: int, cutoff: int, orientation: str) -> dict[str, object]:
    """Evaluate one exact linear-Walsh orientation inside z2<=z<=C."""
    z2, C = exact_linear_cutoff_zone(k)
    if not (z2 <= cutoff <= C):
        raise ValueError("cutoff must lie in the exact linear-Walsh zone")
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be 'upper' or 'lower'")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    lower_support = tuple(int(p) for p in lower_support_raw)
    upper_support = tuple(int(p) for p in upper_support_raw)
    lower_low = _low_support(lower_support, cutoff)
    upper_low = _low_support(upper_support, cutoff)

    if orientation == "upper":
        target_state = upper_state
        target_support = upper_support
        target_low = upper_low
        opposite_low = lower_low
    else:
        target_state = lower_state
        target_support = lower_support
        target_low = lower_low
        opposite_low = upper_low

    target_prime = is_prime(target_state)
    target_high = tuple(p for p in target_support if p > cutoff)
    rough = not target_low
    high_p = None
    tail_q = None
    if rough and not target_prime:
        if len(target_high) != 1:
            raise AssertionError("P2-zone rough composite did not have one visible medium factor")
        high_p = int(target_high[0])
        if target_state % high_p:
            raise AssertionError("visible medium factor does not divide target state")
        tail_q = target_state // high_p
        if tail_q <= k or not is_prime(tail_q):
            raise AssertionError("P2-zone rough composite is not p*q with q>k prime")
    if target_prime and target_support:
        raise AssertionError("prime target retained a transverse support")

    amplifier = incidence_optimal_weight(k, opposite_low) if rough else 0
    high_count = len(target_high) if rough else 0
    weight = amplifier * (1 - high_count) if rough else 0
    if weight < 0:
        raise AssertionError("exact P2-zone linear detector became negative")
    if (weight > 0) != target_prime:
        raise AssertionError("P2-zone linear detector lost prime positivity")

    capacity = None if high_p is None else (k - 1) // high_p + 1
    ceiling = cutoff_reuse_width_ceiling(k, cutoff)
    if capacity is not None and capacity > ceiling:
        raise AssertionError("actual high-p capacity exceeded cutoff Pareto ceiling")

    return {
        "k": k,
        "radius": radius,
        "orientation": orientation,
        "p2_cutoff": z2,
        "cutoff": cutoff,
        "half_cutoff": C,
        "target_state": target_state,
        "target_prime": target_prime,
        "target_low_support": target_low,
        "target_high_support": target_high,
        "opposite_low_support": opposite_low,
        "opposite_incidence_optimal_amplifier": amplifier,
        "terminal_high_prime": high_p,
        "terminal_large_tail_prime": tail_q,
        "high_prime_signed_reuse_capacity": capacity,
        "cutoff_reuse_width_ceiling": ceiling,
        "linear_weight": weight,
        "exact_nonnegative_prime_detector": True,
    }


def p2_cutoff_pareto_profile(k: int, cutoff: int) -> dict[str, object]:
    """Aggregate the exact detector and verify p/q reuse bounds at one cutoff."""
    z2, C = exact_linear_cutoff_zone(k)
    if not (z2 <= cutoff <= C):
        raise ValueError("cutoff must lie in the exact linear-Walsh zone")

    rows: list[dict[str, object]] = []
    weighted_prime_signal = 0
    edges: list[dict[str, object]] = []
    p_degree: dict[int, int] = defaultdict(int)
    q_seen: set[int] = set()
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        for orientation in ("upper", "lower"):
            row = p2_zone_orientation_weight(k, radius, cutoff, orientation)
            rows.append(row)
            weighted_prime_signal += int(row["linear_weight"])
            if row["terminal_high_prime"] is None:
                continue
            p = int(row["terminal_high_prime"])
            q = int(row["terminal_large_tail_prime"])
            p_degree[p] += 1
            if q in q_seen:
                raise AssertionError("large P2 tail prime was reused across signed states")
            q_seen.add(q)
            edges.append(
                {
                    "orientation": orientation,
                    "radius": radius,
                    "p": p,
                    "q": q,
                    "opposite_amplifier_weight": int(row["opposite_incidence_optimal_amplifier"]),
                }
            )

    width = cutoff_reuse_width_ceiling(k, cutoff)
    if any(degree > width for degree in p_degree.values()):
        raise AssertionError("physical deletion graph exceeded the P2 cutoff reuse width")
    prime_exists = any(bool(row["target_prime"]) for row in rows)
    if (weighted_prime_signal > 0) != prime_exists:
        raise AssertionError("P2 cutoff aggregate lost exact prime-existence equivalence")

    return {
        "k": k,
        "p2_cutoff": z2,
        "cutoff": cutoff,
        "half_cutoff": C,
        "cutoff_reuse_width_ceiling": width,
        "weighted_prime_signal": weighted_prime_signal,
        "prime_exists": prime_exists,
        "positive_iff_prime_exists": (weighted_prime_signal > 0) == prime_exists,
        "terminal_edges": tuple(edges),
        "high_prime_degrees": tuple(sorted(p_degree.items())),
        "large_tail_right_degree_ceiling": 1,
        "proof_depth_reuse_width_pareto": True,
        "rows": tuple(rows),
    }


def compare_cutoff_refinement(k: int, shallow_cutoff: int, deep_cutoff: int) -> dict[str, object]:
    """Verify monotone semantic signal / shrinking deletion graph under z refinement."""
    z2, C = exact_linear_cutoff_zone(k)
    if not (z2 <= shallow_cutoff <= deep_cutoff <= C):
        raise ValueError("cutoffs must satisfy z2<=shallow<=deep<=C")
    shallow = p2_cutoff_pareto_profile(k, shallow_cutoff)
    deep = p2_cutoff_pareto_profile(k, deep_cutoff)
    if int(deep["weighted_prime_signal"]) < int(shallow["weighted_prime_signal"]):
        raise AssertionError("deeper cutoff decreased the weighted prime signal")
    if int(deep["cutoff_reuse_width_ceiling"]) > int(shallow["cutoff_reuse_width_ceiling"]):
        raise AssertionError("deeper cutoff increased the reuse-width ceiling")

    shallow_edges = {
        (str(edge["orientation"]), int(edge["radius"]), int(edge["p"]), int(edge["q"]))
        for edge in shallow["terminal_edges"]
    }
    deep_edges = {
        (str(edge["orientation"]), int(edge["radius"]), int(edge["p"]), int(edge["q"]))
        for edge in deep["terminal_edges"]
    }
    if not deep_edges.issubset(shallow_edges):
        raise AssertionError("deeper cutoff created a new terminal deletion edge")

    return {
        "k": k,
        "shallow_cutoff": shallow_cutoff,
        "deep_cutoff": deep_cutoff,
        "shallow_weighted_prime_signal": int(shallow["weighted_prime_signal"]),
        "deep_weighted_prime_signal": int(deep["weighted_prime_signal"]),
        "prime_signal_nondecreasing": True,
        "shallow_reuse_width_ceiling": int(shallow["cutoff_reuse_width_ceiling"]),
        "deep_reuse_width_ceiling": int(deep["cutoff_reuse_width_ceiling"]),
        "reuse_width_nonincreasing": True,
        "terminal_deletion_edges_shrink_monotonically": True,
        "cutoff_refinement_is_semantically_monotone": True,
    }
