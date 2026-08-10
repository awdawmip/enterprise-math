"""Exact one-step static counterfactual coupling certificates.

For one visible state and a finite declared action family, prescribing the
output marginal p_a for every action is equivalent to prescribing marginals of
one joint response table.  A static latent atom is simply one deterministic
response tuple (y_a)_a, and a latent mixture is a coupling of the action
marginals.

This module gives an exact rational common-quantile construction.  If action a
has s_a positive outputs, the union of all marginal cumulative breakpoints has
at most

    1 + sum_a (s_a - 1)

intervals.  Each interval determines one response table, yielding a coupling
with at most that many atoms.  Every coupling needs at least max_a s_a atoms
because projection onto action a must cover every positive marginal output.

Thus independent product sampling is an existence construction, not a minimal
latent-capacity theorem.  Coupling/transportation-polytope mathematics is prior
art; the Enterprise Math use is the FQ-007 resource compression boundary.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping
from fractions import Fraction

Action = Hashable
Outcome = Hashable
ResponseTable = tuple[tuple[Action, Outcome], ...]
Marginal = dict[Outcome, Fraction]
Coupling = dict[ResponseTable, Fraction]


def _fraction(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError("coupling weights must be int or Fraction")
    return Fraction(value)


def _validate_marginals(
    marginals: Mapping[Action, Mapping[Outcome, int | Fraction]],
) -> tuple[tuple[Action, ...], dict[Action, Marginal]]:
    if not marginals:
        raise ValueError("at least one action marginal is required")
    actions = tuple(sorted(marginals, key=repr))
    normalized: dict[Action, Marginal] = {}
    for action in actions:
        raw = marginals[action]
        if not raw:
            raise ValueError("every action marginal must have positive support")
        row: Marginal = {}
        for outcome, raw_weight in raw.items():
            weight = _fraction(raw_weight)
            if weight < 0:
                raise ValueError("marginal weights must be nonnegative")
            if weight:
                row[outcome] = weight
        if not row:
            raise ValueError("every action marginal must have positive support")
        if sum(row.values(), Fraction(0)) != 1:
            raise ValueError("every action marginal must sum exactly to one")
        normalized[action] = row
    return actions, normalized


def _ordered_cumulative_row(row: Marginal) -> tuple[tuple[Outcome, Fraction], ...]:
    cumulative = Fraction(0)
    result: list[tuple[Outcome, Fraction]] = []
    for outcome in sorted(row, key=repr):
        cumulative += row[outcome]
        result.append((outcome, cumulative))
    if cumulative != 1:
        raise AssertionError("validated marginal must end at one")
    return tuple(result)


def response_at_quantile(
    cumulative_row: tuple[tuple[Outcome, Fraction], ...], point: Fraction
) -> Outcome:
    """Return the unique marginal outcome whose cumulative interval contains point."""
    if not cumulative_row:
        raise ValueError("cumulative marginal row must be nonempty")
    if point < 0 or point >= 1:
        raise ValueError("quantile point must lie in [0,1)")
    for outcome, upper in cumulative_row:
        if point < upper:
            return outcome
    raise AssertionError("normalized cumulative row must cover [0,1)")


def coupling_marginals(coupling: Mapping[ResponseTable, int | Fraction]) -> dict[Action, Marginal]:
    """Project a static deterministic-response-table mixture to action marginals."""
    if not coupling:
        raise ValueError("coupling must be nonempty")
    total = Fraction(0)
    action_order: tuple[Action, ...] | None = None
    projected: dict[Action, defaultdict[Outcome, Fraction]] = {}

    for raw_table, raw_weight in coupling.items():
        table = tuple(raw_table)
        weight = _fraction(raw_weight)
        if weight < 0:
            raise ValueError("coupling weights must be nonnegative")
        if not table:
            raise ValueError("response tables must be nonempty")
        actions = tuple(action for action, _ in table)
        if len(set(actions)) != len(actions):
            raise ValueError("response table action labels must be unique")
        if action_order is None:
            action_order = actions
            projected = {action: defaultdict(Fraction) for action in actions}
        elif actions != action_order:
            raise ValueError("all response tables must use one common ordered action family")
        total += weight
        if weight:
            for action, outcome in table:
                projected[action][outcome] += weight

    if total != 1:
        raise ValueError("coupling weights must sum exactly to one")
    assert action_order is not None
    return {
        action: {outcome: weight for outcome, weight in projected[action].items() if weight}
        for action in action_order
    }


def common_quantile_coupling(
    marginals: Mapping[Action, Mapping[Outcome, int | Fraction]],
) -> Coupling:
    """Construct an exact rational coupling from the union of CDF breakpoints.

    Outcome order is deterministic via ``repr`` and has no mathematical claim;
    any fixed order gives a valid coupling and the same universal support bound.
    """
    actions, normalized = _validate_marginals(marginals)
    cumulative = {
        action: _ordered_cumulative_row(normalized[action]) for action in actions
    }

    breakpoints = {Fraction(0), Fraction(1)}
    for action in actions:
        for _, upper in cumulative[action][:-1]:
            breakpoints.add(upper)
    ordered = tuple(sorted(breakpoints))

    result: defaultdict[ResponseTable, Fraction] = defaultdict(Fraction)
    for left, right in zip(ordered, ordered[1:], strict=True):
        if right <= left:
            raise AssertionError("distinct sorted breakpoints must define positive intervals")
        point = (left + right) / 2
        table: ResponseTable = tuple(
            (action, response_at_quantile(cumulative[action], point))
            for action in actions
        )
        result[table] += right - left

    coupling = {table: weight for table, weight in result.items() if weight}
    if coupling_marginals(coupling) != normalized:
        raise AssertionError("common-quantile coupling must reproduce every marginal")
    lower, upper = coupling_support_bounds(normalized)
    if not (lower <= len(coupling) <= upper):
        raise AssertionError("constructed coupling must obey the universal support bounds")
    return coupling


def coupling_certificate_holds(
    marginals: Mapping[Action, Mapping[Outcome, int | Fraction]],
    coupling: Mapping[ResponseTable, int | Fraction],
) -> bool:
    """Verify exact equality between declared marginals and a coupling certificate."""
    _, normalized = _validate_marginals(marginals)
    return coupling_marginals(coupling) == normalized


def coupling_support_bounds(
    marginals: Mapping[Action, Mapping[Outcome, int | Fraction]],
) -> tuple[int, int]:
    """Universal min-support lower bound and constructive quantile upper bound.

    These bounds do not claim that either is sharp for every marginal family.
    """
    actions, normalized = _validate_marginals(marginals)
    supports = tuple(len(normalized[action]) for action in actions)
    lower = max(supports)
    upper = 1 + sum(size - 1 for size in supports)
    return lower, upper


def identical_marginal_diagonal_rank(
    marginals: Mapping[Action, Mapping[Outcome, int | Fraction]],
) -> int | None:
    """Return the exact rank when all action marginals are literally identical.

    In that case one shared outcome latent variable gives a diagonal coupling
    with support equal to the common marginal support.  The projection lower
    bound proves optimality.  Returns ``None`` when marginals differ.
    """
    actions, normalized = _validate_marginals(marginals)
    first = normalized[actions[0]]
    if any(normalized[action] != first for action in actions[1:]):
        return None
    return len(first)
