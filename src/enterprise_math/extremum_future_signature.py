"""Coarsest finite future signature for one labeled extremum under deletions.

Fix a finite labeled integer family ``v[label]`` and a future language that may
delete at most ``h`` labels, then observes only the remaining maximum (or
minimum).  Group labels by distinct extremum levels ``S_1,S_2,...`` in extremal
order.  Let ``J`` be the largest index whose cumulative level size is at most
``h``.

The complete future-deletion signature is represented exactly by:

* for levels ``1..J``: the level value and the complete label set;
* for level ``J+1``: only its value (the guard value);
* all lower levels: discarded.

Why the guard labels are unnecessary: after deleting all earlier exposed levels,
the remaining deletion budget is strictly smaller than the guard-level
multiplicity, so at least one guard label must survive.  Conversely, every
exposed level's labels are necessary in general because a future deletion can
remove that whole level and expose the next value.

Thus this is the coarsest exact state for the declared scalar extremum-output
language, not merely the uniform ``h+1`` order-statistic upper bound.  The result
is an E001/P023 specialization of finite future distinguishability; order
statistics themselves are established mathematics.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ExtremumLevel:
    value: int
    labels: tuple[int, ...]


@dataclass(frozen=True)
class ExtremumFutureSignature:
    maximize: bool
    deletion_horizon: int
    labels: tuple[int, ...]
    exposed_levels: tuple[ExtremumLevel, ...]
    guard_value: int


def _validate_values(
    values: Mapping[int, int],
    deletion_horizon: int,
) -> dict[int, int]:
    items = dict(values)
    if not items:
        raise ValueError("at least one labeled value is required")
    for label, value in items.items():
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError("labels must be integers")
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("extremum values must be integers")
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
    ):
        raise ValueError("deletion_horizon must be a non-negative integer")
    if deletion_horizon >= len(items):
        raise ValueError("deletion_horizon must leave at least one label")
    return items


def compile_extremum_future_signature(
    values: Mapping[int, int],
    deletion_horizon: int,
    maximize: bool = True,
) -> ExtremumFutureSignature:
    """Compile the exact deletion-future signature of max/min output."""
    items = _validate_values(values, deletion_horizon)
    grouped: dict[int, list[int]] = {}
    for label, value in items.items():
        grouped.setdefault(value, []).append(label)

    exposed: list[ExtremumLevel] = []
    used = 0
    guard_value: int | None = None
    for value in sorted(grouped, reverse=maximize):
        labels = tuple(sorted(grouped[value]))
        if used + len(labels) <= deletion_horizon:
            exposed.append(ExtremumLevel(value=value, labels=labels))
            used += len(labels)
        else:
            guard_value = value
            break

    if guard_value is None:
        raise AssertionError("finite deletion horizon failed to leave a guard level")
    return ExtremumFutureSignature(
        maximize=maximize,
        deletion_horizon=deletion_horizon,
        labels=tuple(sorted(items)),
        exposed_levels=tuple(exposed),
        guard_value=guard_value,
    )


def extremum_after_deletions(
    signature: ExtremumFutureSignature,
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> int:
    """Evaluate the exact remaining extremum using only the compact signature."""
    removed = frozenset(removed_labels)
    if not removed.issubset(signature.labels):
        raise ValueError("removed labels must belong to the certified family")
    if len(removed) > signature.deletion_horizon:
        raise ValueError("removal set exceeds deletion horizon")

    for level in signature.exposed_levels:
        if not set(level.labels).issubset(removed):
            return level.value
    return signature.guard_value


def worst_case_labeled_candidate_count(deletion_horizon: int) -> int:
    """Maximum labels retained by the coarsest scalar signature: exactly h."""
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
    ):
        raise ValueError("deletion_horizon must be a non-negative integer")
    return deletion_horizon
