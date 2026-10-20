"""Exact terminal-residual audit on the reduced near-primorial candidate fibers.

The theorem-level reduction is already available on the bridge:

* positive even ``J=J_perp(k)`` and terminal order ``m=J-1`` imply every low
  residual row has exactly J transverse support primes and complete core
  ``C<=k-1``;
* its squarefree radical belongs to the exact finite list returned by
  ``near_primorial_radical_candidates(k)``;
* P017 CG13 / the signed-token fiber layer gives the exact anchor-surviving
  signed points attached to each candidate radical.

Therefore the whole signed basin need not be scanned to audit the terminal
residual.  It is enough to take the union of those exact candidate fibers and
inspect complete support/core only on that reduced point set.

This module is an executable finite oracle for the reduced problem.  It does
not replace the row-free Möbius formula in ``p017_p018_full_core_incidence`` and
it is not a Legendre proof.
"""

from __future__ import annotations

from math import prod

from .cutoff_pairing import transverse_prime_support
from .legendre import anchor_product
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core
from .p017_p018_near_primorial_shell import near_primorial_radical_candidates
from .p017_p018_token_remainder_repair import signed_token_fiber


def terminal_candidate_exact_profile(k: int) -> dict[str, object]:
    """Audit the exact terminal residual using only reduced candidate fibers."""
    candidates = near_primorial_radical_candidates(k)
    j = int(candidates["transverse_primorial_depth"])
    if j <= 0 or candidates["J_parity"] != "EVEN":
        raise ValueError("terminal candidate exact profile requires positive even J_perp(k)")

    radical_rows = tuple(candidates["candidate_rows"])
    radical_set = {int(row["radical"]) for row in radical_rows}
    point_sources: dict[int, set[int]] = {}
    for row in radical_rows:
        radical = int(row["radical"])
        fiber = signed_token_fiber(k, radical)
        for point in fiber["signed_points"]:
            point_sources.setdefault(int(point), set()).add(radical)

    center = k * (k + 1)
    anchor = anchor_product(k)
    rows: list[dict[str, object]] = []
    exact_j_support_count = 0
    residual_count = 0
    residual_cores: list[int] = []
    residual_points: list[int] = []

    for point in sorted(point_sources):
        state = center - point
        support = tuple(transverse_prime_support(state, k, anchor))
        core = complete_transverse_core(state, support)
        radical = prod(support) if support else 1
        exact_j = len(support) == j
        terminal_residual = exact_j and core <= k - 1

        if terminal_residual and radical not in radical_set:
            raise AssertionError("terminal residual radical escaped the exact near-primorial candidate list")
        if terminal_residual and radical not in point_sources[point]:
            raise AssertionError("terminal residual point was not carried by its own radical fiber")

        exact_j_support_count += int(exact_j)
        residual_count += int(terminal_residual)
        if terminal_residual:
            residual_cores.append(core)
            residual_points.append(point)

        rows.append(
            {
                "signed_point": point,
                "state": state,
                "candidate_radicals": tuple(sorted(point_sources[point])),
                "support": support,
                "support_size": len(support),
                "support_radical": radical,
                "complete_transverse_core": core,
                "exact_terminal_support_size": exact_j,
                "terminal_low_core_residual": terminal_residual,
            }
        )

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "replacement_depth": int(candidates["replacement_depth"]),
        "candidate_radical_count": len(radical_rows),
        "candidate_signed_point_count": len(rows),
        "exact_j_support_candidate_count": exact_j_support_count,
        "terminal_residual_count": residual_count,
        "terminal_residual_points": tuple(residual_points),
        "terminal_residual_cores": tuple(residual_cores),
        "rows": tuple(rows),
    }
