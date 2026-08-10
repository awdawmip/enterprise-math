"""Exact near-primorial radical capacity for the terminal even-J residual.

This bridge composes two already-proved ingredients without re-owning either
mother theorem:

* ``near_primorial_radical_candidates(k)`` gives the exact squarefree J-prime
  radicals ``D < k`` that a terminal low-complete-core row can have when
  ``J = J_perp(k)`` is positive and even;
* P017 CG12 gives every odd transverse divisor label ``D`` the signed reuse
  capacity

      m_D <= floor((k-1)/D) + 1.

At terminal order ``m=J-1``, full-core compression says every residual row has
support size exactly J and complete transverse core ``C <= k-1``.  Therefore
its radical ``rad(C)`` belongs to the exact near-primorial candidate list.  The
residual rows partition by that radical, so summing the CG12 capacities gives

    R_terminal(k)
      <= sum_{D in R_J(k)} (floor((k-1)/D) + 1).

This is strictly sharper than the earlier uniform-overlap capacity whenever the
exact candidate shell is sparse enough.  It is a finite subterminal capacity
bound, not a Legendre proof.
"""

from __future__ import annotations

from .p017_p018_near_primorial_shell import near_primorial_radical_candidates
from .p017_p018_terminal_overlap_capacity import terminal_overlap_capacity


def terminal_radical_capacity(k: int) -> dict[str, object]:
    """Return the exact-candidate CG12 upper capacity for terminal residual rows."""
    data = near_primorial_radical_candidates(k)
    candidates = tuple(int(value) for value in data["candidate_radicals"])
    rows: list[dict[str, int]] = []
    total = 0

    for radical in candidates:
        if radical <= 0 or radical >= k:
            raise AssertionError("terminal radical escaped 1 <= D < k")
        capacity = (k - 1) // radical + 1
        rows.append({"radical": radical, "signed_reuse_capacity": capacity})
        total += capacity

    old = terminal_overlap_capacity(k)
    old_capacity = int(old["terminal_residual_row_capacity"])
    if total > old_capacity:
        # The exact-radical partition should never be advertised as an
        # improvement unless it is at least as strong as the previously proved
        # uniform-overlap packing bound.  For a future exotic input where the
        # two incomparable relaxations reverse, retain both bounds instead of
        # silently weakening the result.
        combined = old_capacity
        source = "uniform_overlap"
    else:
        combined = total
        source = "exact_radical_sum"

    return {
        "k": k,
        "transverse_primorial_depth": int(data["transverse_primorial_depth"]),
        "replacement_depth": int(data["replacement_depth"]),
        "candidate_radicals": candidates,
        "candidate_count": len(candidates),
        "radical_capacity_rows": tuple(rows),
        "exact_radical_capacity_sum": total,
        "previous_uniform_overlap_capacity": old_capacity,
        "combined_terminal_capacity": combined,
        "active_capacity_source": source,
        "strictly_improves_uniform_overlap": total < old_capacity,
    }
