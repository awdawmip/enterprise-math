"""Exact near-primorial radical capacity for the terminal even-J residual.

This bridge composes existing owner results without re-owning their mother
statements:

* ``near_primorial_radical_candidates(k)`` gives the exact squarefree J-prime
  radicals ``D < k`` that a terminal low-complete-core row can have when
  ``J = J_perp(k)`` is positive and even;
* P017 CG12 gives the alignment-free signed reuse ceiling

      m_D <= floor((k-1)/D) + 1;

* P017 CG13 sharpens that ceiling to the exact anchor-surviving signed divisor
  fiber ``X_D(k)``.  On this bridge the centered boundary-carry engine computes
  its exact cardinality, while the signed-token fiber exposes the finite points.

At terminal order ``m=J-1``, full-core compression says every residual row has
support size exactly J and complete transverse core ``C <= k-1``.  Therefore
its radical ``rad(C)`` belongs to the exact near-primorial candidate list.
Consequently

    R_terminal(k)
      <= | union_{D in R_J(k)} X_D(k) |
      <= sum_{D in R_J(k)} |X_D(k)|
      <= sum_{D in R_J(k)} (floor((k-1)/D) + 1).

The union step removes real cross-column duplicate signed points before any
support/core factorization is used.  It is still only a capacity bound; the
separate reduced-candidate exact oracle filters support and prime-power content
to recover the actual terminal residual on finite pressure-test scales.
"""

from __future__ import annotations

from .p017_p018_near_primorial_shell import near_primorial_radical_candidates
from .p017_p018_signed_boundary_carry import (
    anchor_surviving_divisor_boundary_carry,
)
from .p017_p018_terminal_overlap_capacity import terminal_overlap_capacity
from .p017_p018_token_remainder_repair import signed_token_fiber


def terminal_radical_capacity(k: int) -> dict[str, object]:
    """Return the nested terminal capacities from uniform packing to exact fiber union."""
    data = near_primorial_radical_candidates(k)
    candidates = tuple(int(value) for value in data["candidate_radicals"])
    rows: list[dict[str, object]] = []
    universal_total = 0
    raw_aligned_total = 0
    exact_anchor_total = 0
    anchor_union: set[int] = set()

    for radical in candidates:
        if radical <= 0 or radical >= k:
            raise AssertionError("terminal radical escaped 1 <= D < k")
        boundary = anchor_surviving_divisor_boundary_carry(k, radical)
        fiber = signed_token_fiber(k, radical)
        universal = int(boundary["cg12_universal_capacity"])
        raw_aligned = int(boundary["raw_signed_fiber_size"])
        exact_anchor = int(boundary["anchor_surviving_fiber_size"])
        signed_points = tuple(int(point) for point in fiber["signed_points"])
        if exact_anchor != len(signed_points):
            raise AssertionError("boundary-carry and signed-token exact fibers disagree")
        if not (0 <= exact_anchor <= raw_aligned <= universal):
            raise AssertionError("terminal radical capacity chain failed")
        rows.append(
            {
                "radical": radical,
                "cg12_universal_capacity": universal,
                "raw_aligned_capacity": raw_aligned,
                "exact_anchor_capacity": exact_anchor,
                "anchor_signed_points": signed_points,
            }
        )
        universal_total += universal
        raw_aligned_total += raw_aligned
        exact_anchor_total += exact_anchor
        anchor_union.update(signed_points)

    exact_anchor_union = len(anchor_union)
    if exact_anchor_union > exact_anchor_total:
        raise AssertionError("fiber union exceeded the sum of exact anchor capacities")

    old = terminal_overlap_capacity(k)
    old_capacity = int(old["terminal_residual_row_capacity"])
    combined = min(
        old_capacity,
        universal_total,
        raw_aligned_total,
        exact_anchor_total,
        exact_anchor_union,
    )
    if combined == exact_anchor_union:
        source = "exact_anchor_fiber_union"
    elif combined == exact_anchor_total:
        source = "exact_anchor_radical_sum"
    elif combined == raw_aligned_total:
        source = "raw_aligned_radical_sum"
    elif combined == universal_total:
        source = "universal_radical_sum"
    else:
        source = "uniform_overlap"

    return {
        "k": k,
        "transverse_primorial_depth": int(data["transverse_primorial_depth"]),
        "replacement_depth": int(data["replacement_depth"]),
        "candidate_radicals": candidates,
        "candidate_count": len(candidates),
        "radical_capacity_rows": tuple(rows),
        "universal_radical_capacity_sum": universal_total,
        "raw_aligned_radical_capacity_sum": raw_aligned_total,
        "exact_anchor_radical_capacity_sum": exact_anchor_total,
        "exact_anchor_fiber_union_capacity": exact_anchor_union,
        "exact_anchor_fiber_union_points": tuple(sorted(anchor_union)),
        "previous_uniform_overlap_capacity": old_capacity,
        "combined_terminal_capacity": combined,
        "active_capacity_source": source,
        "strictly_improves_uniform_overlap": combined < old_capacity,
    }
