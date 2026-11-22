"""Exact terminal residual as a finite sum of complete-core columns.

Assume positive even ``J=J_perp(k)`` and terminal odd order ``m=J-1``.
Terminal full-core compression proves that a signed row carries residual defect
if and only if

* its transverse support has exactly J primes; and
* its complete transverse small-prime core C satisfies ``C<=k-1``.

The near-primorial shell theorem independently gives the exact finite list of
possible squarefree radicals ``D=rad(C)<k`` with J transverse primes.  For one
such radical, every possible low complete core is obtained by raising only the
already-selected prime exponents while keeping the product below k.

Let ``C_J(k)`` be the resulting finite set of complete-core labels.  Complete
core is a function of the state, so these columns are disjoint.  With
``I_full(C)`` denoting the exact all-support/exact-valuation Möbius incidence,
we therefore have the exact identity

    R_terminal(k) = sum_{C in C_J(k)} I_full(C).

This is a row-free representation of the terminal residual.  It does not by
itself supply a uniform analytic bound for the finite column sum and therefore
does not prove Legendre's conjecture.
"""

from __future__ import annotations

from .p017_p018_full_core_incidence import full_core_incidence_mobius
from .p017_p018_near_primorial_shell import near_primorial_radical_candidates


def _complete_core_lifts_below_k(
    k: int,
    radical: int,
    support: tuple[int, ...],
) -> tuple[int, ...]:
    """Return all C<k with rad(C)=radical and the declared support."""
    if radical >= k or radical < 1:
        raise ValueError("radical must satisfy 1<=D<k")
    if not support:
        raise ValueError("support must be nonempty")

    values: list[int] = []

    def extend(index: int, current: int) -> None:
        if index == len(support):
            values.append(current)
            return
        prime = int(support[index])
        value = current
        while value < k:
            extend(index + 1, value)
            if value > (k - 1) // prime:
                break
            value *= prime

    extend(0, radical)
    result = tuple(sorted(set(values)))
    if not result or result[0] != radical:
        raise AssertionError("complete-core lift set lost its squarefree radical")
    for value in result:
        remaining = value
        seen: list[int] = []
        for prime in support:
            if remaining % prime:
                raise AssertionError("complete-core lift lost a support prime")
            seen.append(prime)
            while remaining % prime == 0:
                remaining //= prime
        if remaining != 1 or tuple(seen) != support:
            raise AssertionError("complete-core lift introduced an outside prime")
    return result


def terminal_complete_core_candidates(k: int) -> dict[str, object]:
    """Enumerate the exact finite low complete-core label set C_J(k)."""
    radicals = near_primorial_radical_candidates(k)
    j = int(radicals["transverse_primorial_depth"])
    if j <= 0 or radicals["J_parity"] != "EVEN":
        raise ValueError("terminal full-core identity requires positive even J_perp(k)")

    rows: list[dict[str, object]] = []
    all_cores: list[int] = []
    for radical_row in radicals["candidate_rows"]:
        radical = int(radical_row["radical"])
        support = tuple(int(p) for p in radical_row["radical_primes"])
        if len(support) != j:
            raise AssertionError("terminal radical candidate has the wrong support depth")
        lifts = _complete_core_lifts_below_k(k, radical, support)
        rows.append(
            {
                "radical": radical,
                "support": support,
                "complete_core_lifts": lifts,
                "complete_core_lift_count": len(lifts),
            }
        )
        all_cores.extend(lifts)

    cores = tuple(sorted(all_cores))
    if len(set(cores)) != len(cores):
        raise AssertionError("distinct terminal radicals produced the same complete core")

    return {
        "k": k,
        "transverse_primorial_depth": j,
        "replacement_depth": int(radicals["replacement_depth"]),
        "candidate_radical_count": int(radicals["candidate_count"]),
        "complete_core_candidate_count": len(cores),
        "complete_core_candidates": cores,
        "radical_rows": tuple(rows),
    }


def terminal_full_core_column_identity(
    k: int,
    *,
    verify_each_column_direct: bool = False,
) -> dict[str, object]:
    """Evaluate the row-free exact terminal residual column sum."""
    candidates = terminal_complete_core_candidates(k)
    rows: list[dict[str, object]] = []
    total = 0

    for core in candidates["complete_core_candidates"]:
        data = full_core_incidence_mobius(
            k,
            int(core),
            verify_direct=verify_each_column_direct,
        )
        incidence = int(data["full_core_incidence"])
        total += incidence
        if incidence:
            rows.append(
                {
                    "complete_core": int(core),
                    "full_core_incidence": incidence,
                    "support_primes": tuple(int(p) for p in data["support_primes"]),
                }
            )

    return {
        **candidates,
        "nonzero_complete_core_rows": tuple(rows),
        "nonzero_complete_core_count": len(rows),
        "terminal_residual_exact_column_sum": total,
    }
