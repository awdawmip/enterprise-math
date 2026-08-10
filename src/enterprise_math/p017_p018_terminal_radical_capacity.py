"""Exact near-primorial radical capacity for the terminal even-J residual.

This bridge composes existing owner results without re-owning their mother
statements:

* ``near_primorial_radical_candidates(k)`` gives the exact squarefree J-prime
  radicals ``D < k`` that a terminal low-complete-core row can have when
  ``J = J_perp(k)`` is positive and even;
* P017 CG12 gives the alignment-free signed reuse ceiling

      m_D <= floor((k-1)/D) + 1;

* P017 CG13 sharpens that ceiling to the exact anchor-surviving signed divisor
  fiber.  On this bridge the already-existing centered boundary-carry engine
  computes that exact fiber as ``F_surv(D)`` by one mod-2D class plus anchor
  Möbius filtering.

At terminal order ``m=J-1``, full-core compression says every residual row has
support size exactly J and complete transverse core ``C <= k-1``.  Therefore
its radical ``rad(C)`` belongs to the exact near-primorial candidate list.  The
residual rows partition by that radical.  Consequently

    R_terminal(k)
      <= sum_{D in R_J(k)} F_surv(D)
      <= sum_{D in R_J(k)} (floor((k-1)/D) + 1).

The exact-anchor sum can be much smaller than both the older uniform-overlap
packing bound and the alignment-free radical sum.  This is a finite subterminal
capacity theorem, not a Legendre proof.
"""

from __future__ import annotations

from .p017_p018_near_primorial_shell import near_primorial_radical_candidates
from .p017_p018_signed_boundary_carry import (
    anchor_surviving_divisor_boundary_carry,
)
from .p017_p018_terminal_overlap_capacity import terminal_overlap_capacity


def terminal_radical_capacity(k: int) -> dict[str, object]:
    """Return exact terminal radical-column capacities after alignment/anchor filtering."""
    data = near_primorial_radical_candidates(k)
    candidates = tuple(int(value) for value in data["candidate_radicals"])
    rows: list[dict[str, int]] = []
    universal_total = 0
    raw_aligned_total = 0
    exact_anchor_total = 0

    for radical in candidates:
        if radical <= 0 or radical >= k:
            raise AssertionError("terminal radical escaped 1 <= D < k")
        boundary = anchor_surviving_divisor_boundary_carry(k, radical)
        universal = int(boundary["cg12_universal_capacity"])
        raw_aligned = int(boundary["raw_signed_fiber_size"])
        exact_anchor = int(boundary["anchor_surviving_fiber_size"])
        if not (0 <= exact_anchor <= raw_aligned <= universal):
            raise AssertionError("terminal radical capacity chain failed")
        rows.append(
            {
                "radical": radical,
                "cg12_universal_capacity": universal,
                "raw_aligned_capacity": raw_aligned,
                "exact_anchor_capacity": exact_anchor,
            }
        )
        universal_total += universal
        raw_aligned_total += raw_aligned
        exact_anchor_total += exact_anchor

    old = terminal_overlap_capacity(k)
    old_capacity = int(old["terminal_residual_row_capacity"])
    combined = min(old_capacity, universal_total, raw_aligned_total, exact_anchor_total)
    if combined == exact_anchor_total:
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
        "previous_uniform_overlap_capacity": old_capacity,
        "combined_terminal_capacity": combined,
        "active_capacity_source": source,
        "strictly_improves_uniform_overlap": combined < old_capacity,
    }
