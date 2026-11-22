"""Irreducible symmetric boundary core of P017 orientation-Walsh precision.

Let a normalized one-sided prime amplifier have incidence expansion

    h(S)=sum_{T subseteq S} alpha(T),       alpha(empty)=1.

The normalized symmetric mirror detector is

    G(L,U)=1/2 [h(L) 1_{U empty}+h(U) 1_{L empty}].

For a selected root pattern whose lower-oriented selected set is A and whose
upper-oriented selected set is B (A and B disjoint), the exact coefficient is

    c(A,B)
      =1/2 [alpha(A)(-1)^|B| + alpha(B)(-1)^|A|].

Let C_k=floor((k-1)/2) be the exact reusable-floor cutoff.  Symmetricization does
not weaken the low-product floor equations: summing c(A,V\A) over all
orientations of a selected union V gives the same Mobius transform beta(V) as
the one-sided detector.  Consequently every normalized boundary-only symmetric
detector is still forced to satisfy

    alpha(T)=1                  whenever rad(T)<=C_k.

This creates an irreducible symmetric root core.  If both A and B are in the
reusable-floor down-set, then

    c(A,B)=1/2[(-1)^|B|+(-1)^|A|].

Hence

* if |A|+|B| is odd, the coefficient is exactly zero;
* if |A|+|B| is even, its magnitude is exactly one and no allowed tail compiler
  can change it.

In particular every forced nonzero symmetric root pattern satisfies

    rad(A)<=C_k, rad(B)<=C_k,

so its total selected conductor obeys

    rad(A union B)=rad(A)rad(B)<=C_k^2.

Thus C_k^2 is the **forced symmetric conductor horizon**.  Root patterns above
that product are not required by floor precision; any coefficients retained
there by hard Walsh belong to a compilable boundary tail.  This theorem does
not assert that all such tail coefficients can be eliminated simultaneously
under positivity; it isolates the exact irreducible core that no normalized
boundary-only symmetric detector can remove.

This is a finite precision/lower-bound theorem, not a Legendre proof.
"""

from __future__ import annotations

from math import prod

from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def _support(value: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in value))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct entries")
    if any(p < 3 or p % 2 == 0 for p in normalized):
        raise ValueError("support entries must be odd integers >=3")
    return normalized


def forced_low_incidence(k: int, support: tuple[int, ...]) -> int | None:
    """Return forced alpha=1 on reusable supports, else None for the free tail."""
    normalized = _support(support)
    return 1 if prod(normalized, start=1) <= reusable_floor_product_cutoff(k) else None


def symmetric_root_coefficient_from_incidence(
    lower_alpha: int,
    upper_alpha: int,
    lower_size: int,
    upper_size: int,
) -> float:
    """Return normalized coefficient c(A,B) from two incidence coefficients."""
    return 0.5 * (
        lower_alpha * ((-1) ** upper_size)
        + upper_alpha * ((-1) ** lower_size)
    )


def forced_symmetric_root_pattern(
    k: int,
    lower_selected: tuple[int, ...],
    upper_selected: tuple[int, ...],
) -> dict[str, object]:
    """Classify whether a root-pattern coefficient is irreducibly forced by floor precision."""
    lower = _support(lower_selected)
    upper = _support(upper_selected)
    if set(lower).intersection(upper):
        raise ValueError("lower and upper selected supports must be disjoint")
    cutoff = reusable_floor_product_cutoff(k)
    lower_rad = prod(lower, start=1)
    upper_rad = prod(upper, start=1)
    lower_forced = lower_rad <= cutoff
    upper_forced = upper_rad <= cutoff
    forced = lower_forced and upper_forced
    total_degree = len(lower) + len(upper)
    if forced:
        coefficient = symmetric_root_coefficient_from_incidence(1, 1, len(lower), len(upper))
        expected_magnitude = 1.0 if total_degree % 2 == 0 else 0.0
        if abs(coefficient) != expected_magnitude:
            raise AssertionError("forced symmetric parity coefficient failed")
    else:
        coefficient = None
        expected_magnitude = None
    total_conductor = lower_rad * upper_rad
    if forced and total_conductor > cutoff * cutoff:
        raise AssertionError("forced symmetric root escaped C_k^2 conductor horizon")
    return {
        "k": k,
        "lower_selected": lower,
        "upper_selected": upper,
        "lower_radical": lower_rad,
        "upper_radical": upper_rad,
        "reusable_floor_product_cutoff": cutoff,
        "forced_symmetric_conductor_horizon": cutoff * cutoff,
        "total_selected_conductor": total_conductor,
        "lower_incidence_forced": lower_forced,
        "upper_incidence_forced": upper_forced,
        "coefficient_forced": forced,
        "forced_symmetric_coefficient": coefficient,
        "forced_coefficient_magnitude": expected_magnitude,
        "total_selected_degree": total_degree,
        "even_degree_forced_nonzero": forced and total_degree % 2 == 0,
        "odd_degree_forced_zero": forced and total_degree % 2 == 1,
    }


def forced_partition_count(k: int, selected_support: tuple[int, ...]) -> dict[str, object]:
    """Count irreducible nonzero orientation roots for one selected union V."""
    selected = _support(selected_support)
    n = len(selected)
    cutoff = reusable_floor_product_cutoff(k)
    forced_nonzero = 0
    forced_zero = 0
    free_patterns = 0
    for mask in range(1 << n):
        lower = tuple(selected[i] for i in range(n) if mask & (1 << i))
        upper = tuple(selected[i] for i in range(n) if not (mask & (1 << i)))
        row = forced_symmetric_root_pattern(k, lower, upper)
        if bool(row["coefficient_forced"]):
            if bool(row["even_degree_forced_nonzero"]):
                forced_nonzero += 1
            else:
                forced_zero += 1
        else:
            free_patterns += 1
    if n % 2 == 1 and forced_nonzero != 0:
        raise AssertionError("odd selected degree retained an irreducible symmetric coefficient")
    if prod(selected, start=1) > cutoff * cutoff and forced_nonzero != 0:
        raise AssertionError("conductor above C_k^2 retained a forced nonzero root")
    return {
        "k": k,
        "selected_support": selected,
        "selected_conductor": prod(selected, start=1),
        "selected_degree": n,
        "forced_symmetric_conductor_horizon": cutoff * cutoff,
        "forced_nonzero_root_patterns": forced_nonzero,
        "forced_zero_root_patterns": forced_zero,
        "free_tail_root_patterns": free_patterns,
        "total_root_patterns": 1 << n,
    }
