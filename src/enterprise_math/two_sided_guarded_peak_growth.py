"""Eventual affine growth for two-sided guard-only future precision.

For a genuinely two-sided finite integer action alphabet ``A`` and upper guard
``x<g``, the exact horizon-``h`` guard-only class count is one plus the number
of nonnegative cumulative translations reachable in at most ``h-1`` actions.
The finite counts can be irregular.  This module identifies the exact eventual
affine law and a finite certificate for where it starts.

First divide all actions by their positive gcd grain ``d``.  Let the normalized
alphabet be ``Abar`` and let

    P = max {a in Abar : a>0}

be its fastest positive action.  A word of at most ``n`` actions reaching
normalized translation ``q`` can be padded to exactly ``n`` slots with unused
zero actions.  Relative to the all-``P`` reference path its deficit is

    delta = n*P - q.

Each used action ``a`` contributes deficit ``P-a`` and each unused slot
contributes deficit ``P``.  Hence the positive deficit generators are

    D = {P} union {P-a : a in Abar, P-a>0}.

Because ``gcd(Abar)=1``, ``gcd(D)=1``.  Thus ``S_D=<D>`` is a numerical
semigroup.  Let ``gamma`` be its genus (number of positive gaps) and ``c`` its
conductor.

For all sufficiently large prefix horizons ``n`` every semigroup deficit
``delta<=nP`` has a representation using at most ``n`` slots.  Consequently

    |M_n intersect N_0| = n*P + 1 - gamma,

and therefore the guarded word-horizon class count is eventually

    K_h = (h-1)*P + 2 - gamma.             (h>=1)

This separates three exact resources:

* ``d`` controls the infinite state-cell width;
* ``P`` controls the eventual number of new classes per extra action horizon;
* ``gamma`` is the permanent finite class deficit relative to the full
  normalized interval.

A finite proof bound is obtained from any deficit generator ``R>P`` (one exists
because the original action alphabet contains a negative action).  For each
residue modulo ``R`` let ``w_r`` be the least semigroup value and ``ell_r`` the
least generator length among representations of that least value.  Every
semigroup value in that residue is ``w_r+kR`` and has a representation of length
at most ``ell_r+k``.  Therefore all deficits up to ``nP`` fit inside ``n`` slots
once

    n*(R-P) >= R*ell_r - w_r

for every residue, together with ``nP>=c-1``.  The implementation chooses the
best available ``R``.  Since the affine law is then proved for every later
horizon, a finite scan only up to that proof bound determines the exact minimal
affine onset.

Numerical semigroups, Apéry sets and shortest residue representatives are
standard prior mathematics.  This module is the P024 guarded-action
specialization and makes no generic novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import gcd
from typing import Iterable

from .action_language_precision import (
    numerical_semigroup_profile,
    relevant_semigroup_holes,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _normalize_two_sided_actions(
    actions: Iterable[int],
) -> tuple[int, tuple[int, ...]]:
    values = tuple(actions)
    if not values:
        raise ValueError("at least one action is required")
    for action in values:
        _require_int("action", action)
    values = tuple(sorted(set(values)))
    if not any(action > 0 for action in values):
        raise ValueError("two-sided action family requires a positive action")
    if not any(action < 0 for action in values):
        raise ValueError("two-sided action family requires a negative action")

    grain = 0
    for action in values:
        grain = gcd(grain, abs(action))
    if grain <= 0:
        raise AssertionError("two-sided action grain must be positive")
    normalized = tuple(action // grain for action in values)
    normalized_grain = 0
    for action in normalized:
        normalized_grain = gcd(normalized_grain, abs(action))
    if normalized_grain != 1:
        raise AssertionError("normalized action alphabet lost gcd-one form")
    return grain, normalized


def _ceil_div_nonnegative(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    if numerator <= 0:
        return 0
    return (numerator + denominator - 1) // denominator


def two_sided_deficit_generators(
    actions: Iterable[int],
) -> tuple[int, ...]:
    """Return the normalized positive deficit-semigroup generators ``D``."""
    _, normalized = _normalize_two_sided_actions(actions)
    fastest = max(action for action in normalized if action > 0)
    generators = {
        fastest,
        *(
            fastest - action
            for action in normalized
            if fastest - action > 0
        ),
    }
    result = tuple(sorted(generators))
    common = 0
    for generator in result:
        common = gcd(common, generator)
    if common != 1:
        raise AssertionError("normalized deficit generators must have gcd one")
    if not any(generator > fastest for generator in result):
        raise AssertionError("negative action must supply a deficit generator above P")
    return result


def _apery_value_lengths(
    generators: tuple[int, ...],
    modulus: int,
) -> tuple[tuple[int, int], ...]:
    """Least semigroup value and then least length in every residue mod ``modulus``."""
    if modulus not in generators:
        raise ValueError("repair modulus must be one of the deficit generators")
    if modulus <= 0:
        raise ValueError("repair modulus must be positive")

    infinity = 10**30
    best = [(infinity, infinity)] * modulus
    best[0] = (0, 0)
    queue: list[tuple[int, int, int]] = [(0, 0, 0)]

    while queue:
        value, length, residue = heappop(queue)
        if (value, length) != best[residue]:
            continue
        for generator in generators:
            candidate_value = value + generator
            candidate_length = length + 1
            target = candidate_value % modulus
            candidate = (candidate_value, candidate_length)
            if candidate < best[target]:
                best[target] = candidate
                heappush(
                    queue,
                    (candidate_value, candidate_length, target),
                )

    if any(value >= infinity for value, _ in best):
        raise AssertionError("gcd-one deficit semigroup did not reach every residue")
    return tuple(best)


def _reachable_nonnegative_counts(
    normalized_actions: tuple[int, ...],
    maximum_horizon: int,
) -> tuple[int, ...]:
    """Counts of distinct nonnegative translations reachable in <=n actions."""
    if maximum_horizon < 0:
        raise ValueError("maximum_horizon must be non-negative")
    reached = {0}
    frontier = {0}
    counts = [1]
    for _ in range(maximum_horizon):
        frontier = {
            total + action
            for total in frontier
            for action in normalized_actions
        }
        reached.update(frontier)
        counts.append(sum(total >= 0 for total in reached))
    return tuple(counts)


@dataclass(frozen=True)
class TwoSidedGuardPeakGrowthReport:
    action_grain: int
    normalized_actions: tuple[int, ...]
    normalized_fastest_positive: int
    deficit_generators: tuple[int, ...]
    deficit_conductor: int
    deficit_genus: int
    repair_modulus: int
    sufficient_prefix_horizon: int
    exact_prefix_affine_onset: int

    @property
    def sufficient_word_horizon(self) -> int:
        """Word horizon after which the affine class law is proved."""
        return self.sufficient_prefix_horizon + 1

    @property
    def exact_word_affine_onset(self) -> int:
        """Smallest word horizon from which the affine class law holds forever."""
        return self.exact_prefix_affine_onset + 1

    def nonnegative_reachable_count_formula(
        self,
        prefix_horizon: int,
    ) -> int:
        """Exact eventual ``|M_n∩N_0|`` formula, guarded by its proved onset."""
        _require_int("prefix_horizon", prefix_horizon)
        if prefix_horizon < self.exact_prefix_affine_onset:
            raise ValueError("prefix horizon is before the exact affine onset")
        return (
            prefix_horizon * self.normalized_fastest_positive
            + 1
            - self.deficit_genus
        )

    def guard_only_class_count_formula(
        self,
        word_horizon: int,
    ) -> int:
        """Exact eventual guard-only class count on ``Z``."""
        _require_int("word_horizon", word_horizon)
        if word_horizon < self.exact_word_affine_onset:
            raise ValueError("word horizon is before the exact affine onset")
        prefix_horizon = word_horizon - 1
        return self.nonnegative_reachable_count_formula(prefix_horizon) + 1


def two_sided_guard_peak_growth_report(
    actions: Iterable[int],
) -> TwoSidedGuardPeakGrowthReport:
    """Compile exact eventual class-growth data for a two-sided action alphabet."""
    grain, normalized = _normalize_two_sided_actions(actions)
    fastest = max(action for action in normalized if action > 0)
    deficits = two_sided_deficit_generators(normalized)

    semigroup = numerical_semigroup_profile(deficits)
    if semigroup.grain != 1:
        raise AssertionError("deficit semigroup must be numerical after normalization")
    conductor = semigroup.conductor
    if conductor == 0:
        genus = 0
    else:
        genus = len(relevant_semigroup_holes(conductor, deficits))

    conductor_horizon = (
        0
        if conductor <= 1
        else _ceil_div_nonnegative(conductor - 1, fastest)
    )

    repair_candidates: list[tuple[int, int]] = []
    for modulus in deficits:
        if modulus <= fastest:
            continue
        residue_data = _apery_value_lengths(deficits, modulus)
        residue_horizon = 0
        for value, length in residue_data:
            residue_horizon = max(
                residue_horizon,
                _ceil_div_nonnegative(
                    modulus * length - value,
                    modulus - fastest,
                ),
            )
        repair_candidates.append(
            (max(conductor_horizon, residue_horizon), modulus)
        )
    if not repair_candidates:
        raise AssertionError("negative action must provide one repair modulus above P")

    sufficient_horizon, repair_modulus = min(repair_candidates)

    counts = _reachable_nonnegative_counts(normalized, sufficient_horizon)
    expected = tuple(
        n * fastest + 1 - genus
        for n in range(sufficient_horizon + 1)
    )
    exact_onset = sufficient_horizon
    for candidate in range(sufficient_horizon + 1):
        if all(
            counts[n] == expected[n]
            for n in range(candidate, sufficient_horizon + 1)
        ):
            exact_onset = candidate
            break

    if counts[sufficient_horizon] != expected[sufficient_horizon]:
        raise AssertionError("finite repair bound failed at its certified horizon")

    return TwoSidedGuardPeakGrowthReport(
        action_grain=grain,
        normalized_actions=normalized,
        normalized_fastest_positive=fastest,
        deficit_generators=deficits,
        deficit_conductor=conductor,
        deficit_genus=genus,
        repair_modulus=repair_modulus,
        sufficient_prefix_horizon=sufficient_horizon,
        exact_prefix_affine_onset=exact_onset,
    )
