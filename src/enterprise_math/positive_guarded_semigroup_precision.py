"""Positive guarded translations reduce to a compiled P024 semigroup orbit.

This layer specializes ``guarded_translation_precision`` to a strictly positive
integer action alphabet ``A``.  For a nonempty word, positivity makes every
prefix sum strictly increase, so if ``p`` is the total before the last action
``a`` then

    H = p,
    T = p + a.

For ordered-threshold boundaries ``B`` and common upper guard ``x<g``, that
profile contributes the cuts

    g-p

and

    (b-a)-p   whenever b-a < g.

Define the one-step compiled base cut set

    D = {g} union {b-a : b in B, a in A, b-a < g}.

If ``M_h`` is canonical P024 cumulative positive-translation reachability in at
most ``h`` actions, then for every horizon ``h>=1`` the entire guarded cut set is
exactly

    C_h^guard = B union (D - M_(h-1)).

Thus the state-dependent guard does not require a new state-partition mother
algorithm in this positive specialization.  It compiles once into ``D`` and
then reuses the existing one-sided translation boundary orbit with a one-step
horizon shift.

At infinite horizon, write ``S=<A>`` for the additive numerical semigroup.  The
guarded future cuts are

    C_inf^guard = B union (D - S).

Let ``gcd(A)=d`` and let ``c`` be the conductor of the gcd-normalized numerical
semigroup.  For every residue class modulo ``d`` represented by ``D``, choose
the largest compiled base cut ``anchor`` in that residue.  Then every integer
cut in the same residue at or below

    anchor - d*c

belongs to ``D-S``.  Hence the canonical P024 conductor still bounds the entire
irregular tail depth after guard compilation; the guard changes the finite
boundary layer and represented residue anchors, not the eventual semigroup
periodicity.

Numerical-semigroup/Apéry/conductor mathematics is standard prior art.  The
project result is the exact reduction of this state-dependent guarded action
language back to the canonical P024 positive-semigroup boundary calculus.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .action_language_precision import (
    numerical_semigroup_profile,
    reachable_translations,
)
from .guarded_translation_precision import guarded_reachable_boundary_cuts


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _positive_actions(actions: Iterable[int]) -> tuple[int, ...]:
    values = tuple(actions)
    if not values:
        raise ValueError("at least one action is required")
    for action in values:
        _require_int("action", action)
        if action <= 0:
            raise ValueError("actions must be strictly positive")
    return tuple(sorted(set(values)))


def _boundaries(boundaries: Iterable[int]) -> tuple[int, ...]:
    values = tuple(boundaries)
    for boundary in values:
        _require_int("boundary", boundary)
    return tuple(sorted(set(values)))


def positive_guarded_base_cuts(
    boundaries: Iterable[int],
    actions: Iterable[int],
    guard: int,
) -> tuple[int, ...]:
    """Return ``D={g} union {b-a : b-a<g}`` for the positive guarded language."""
    cuts = _boundaries(boundaries)
    values = _positive_actions(actions)
    _require_int("guard", guard)
    compiled = {guard}
    for action in values:
        for boundary in cuts:
            shifted = boundary - action
            if shifted < guard:
                compiled.add(shifted)
    return tuple(sorted(compiled))


def positive_guarded_boundary_cuts_closed_form(
    boundaries: Iterable[int],
    actions: Iterable[int],
    guard: int,
    horizon: int,
) -> tuple[int, ...]:
    """Exact ``B union (D-M_(h-1))`` formula for positive guarded cuts."""
    cuts = _boundaries(boundaries)
    values = _positive_actions(actions)
    _require_int("guard", guard)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    if horizon == 0:
        return cuts

    bases = positive_guarded_base_cuts(cuts, values, guard)
    prefix_totals = reachable_translations(values, horizon - 1)
    result = set(cuts)
    result.update(
        base - prefix
        for base in bases
        for prefix in prefix_totals
    )
    return tuple(sorted(result))


def positive_semigroup_contains(total: int, actions: Iterable[int]) -> bool:
    """Exact membership in ``<actions>`` via canonical normalized Apéry data."""
    _require_int("total", total)
    values = _positive_actions(actions)
    if total < 0:
        return False
    profile = numerical_semigroup_profile(values)
    if total % profile.grain != 0:
        return False
    normalized = total // profile.grain
    multiplicity = min(profile.normalized_generators)
    return normalized >= profile.apery_set[normalized % multiplicity]


def positive_guarded_infinite_cut_membership(
    cut: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    guard: int,
) -> bool:
    """Whether ``cut`` belongs to the exact infinite guarded cut set ``B union (D-S)``."""
    _require_int("cut", cut)
    cuts = _boundaries(boundaries)
    values = _positive_actions(actions)
    _require_int("guard", guard)
    if cut in cuts:
        return True
    bases = positive_guarded_base_cuts(cuts, values, guard)
    return any(
        positive_semigroup_contains(base - cut, values)
        for base in bases
    )


@dataclass(frozen=True)
class GuardedSemigroupTailResidue:
    residue: int
    anchor: int
    complete_below: int


@dataclass(frozen=True)
class PositiveGuardedSemigroupTail:
    grain: int
    normalized_conductor: int
    physical_irregular_depth: int
    compiled_base_cuts: tuple[int, ...]
    residues: tuple[GuardedSemigroupTailResidue, ...]


def positive_guarded_semigroup_tail(
    boundaries: Iterable[int],
    actions: Iterable[int],
    guard: int,
) -> PositiveGuardedSemigroupTail:
    """Return the exact conductor-controlled eventual residue lattice behind ``D``."""
    cuts = _boundaries(boundaries)
    values = _positive_actions(actions)
    _require_int("guard", guard)
    bases = positive_guarded_base_cuts(cuts, values, guard)
    semigroup = numerical_semigroup_profile(values)

    anchors: dict[int, int] = {}
    for base in bases:
        residue = base % semigroup.grain
        anchors[residue] = max(anchors.get(residue, base), base)

    residues = tuple(
        GuardedSemigroupTailResidue(
            residue=residue,
            anchor=anchor,
            complete_below=anchor - semigroup.physical_irregular_depth,
        )
        for residue, anchor in sorted(anchors.items())
    )
    return PositiveGuardedSemigroupTail(
        grain=semigroup.grain,
        normalized_conductor=semigroup.conductor,
        physical_irregular_depth=semigroup.physical_irregular_depth,
        compiled_base_cuts=bases,
        residues=residues,
    )


def positive_guarded_closed_form_agrees_with_profile_compiler(
    boundaries: Iterable[int],
    actions: Iterable[int],
    guard: int,
    horizon: int,
) -> bool:
    """Executable theorem check against the general guarded-profile compiler."""
    values = _positive_actions(actions)
    return positive_guarded_boundary_cuts_closed_form(
        boundaries, values, guard, horizon
    ) == guarded_reachable_boundary_cuts(
        boundaries, values, guard, horizon
    )
