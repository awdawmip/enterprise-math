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

The compact state is also closed under the declared online operation language:

* INSERT(label,value) may be processed from exposed levels + guard alone; values
  weaker than the guard can never become future extrema inside the remaining
  deletion budget, while stronger inserted levels are re-ranked explicitly;
* DELETE(label) consumes one unit of deletion horizon.  Removing an exposed
  label updates its known level; removing a non-exposed label does not require
  knowing whether it was a guard or hidden label.  Re-scanning exposed levels at
  horizon ``h-1`` either exposes the old guard again or promotes a known exposed
  level to guard before any deleted unique guard could matter.

Thus the per-state coarsest deletion signature is a future-compatible Markov
state for arbitrary insertions and at most ``h`` subsequent labeled deletions.
This is an E001/P023 specialization of finite future distinguishability; order
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


def _is_more_extreme(value: int, reference: int, maximize: bool) -> bool:
    return value > reference if maximize else value < reference


def _recompile_from_known_levels(
    maximize: bool,
    deletion_horizon: int,
    labels: tuple[int, ...],
    known_levels: tuple[ExtremumLevel, ...],
    fallback_guard_value: int,
) -> ExtremumFutureSignature:
    """Rebuild exposed/guard boundary from known levels plus one safe guard value."""
    grouped: dict[int, set[int]] = {}
    for level in known_levels:
        grouped.setdefault(level.value, set()).update(level.labels)

    exposed: list[ExtremumLevel] = []
    used = 0
    for value in sorted(grouped, reverse=maximize):
        level_labels = tuple(sorted(grouped[value]))
        if used + len(level_labels) <= deletion_horizon:
            exposed.append(ExtremumLevel(value=value, labels=level_labels))
            used += len(level_labels)
        else:
            return ExtremumFutureSignature(
                maximize=maximize,
                deletion_horizon=deletion_horizon,
                labels=labels,
                exposed_levels=tuple(exposed),
                guard_value=value,
            )

    return ExtremumFutureSignature(
        maximize=maximize,
        deletion_horizon=deletion_horizon,
        labels=labels,
        exposed_levels=tuple(exposed),
        guard_value=fallback_guard_value,
    )


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


def insert_extremum_value(
    signature: ExtremumFutureSignature,
    label: int,
    value: int,
) -> ExtremumFutureSignature:
    """Update the compact future state after inserting one new labeled value."""
    if isinstance(label, bool) or not isinstance(label, int):
        raise ValueError("label must be an integer")
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    if label in signature.labels:
        raise ValueError("inserted label must be new")
    labels = tuple(sorted(signature.labels + (label,)))

    if not _is_more_extreme(value, signature.guard_value, signature.maximize):
        # Equal/less-extreme values cannot become visible within the remaining
        # deletion horizon because the guard level is already undeletable.
        return ExtremumFutureSignature(
            maximize=signature.maximize,
            deletion_horizon=signature.deletion_horizon,
            labels=labels,
            exposed_levels=signature.exposed_levels,
            guard_value=signature.guard_value,
        )

    levels = list(signature.exposed_levels)
    for index, level in enumerate(levels):
        if level.value == value:
            levels[index] = ExtremumLevel(
                value=value,
                labels=tuple(sorted(level.labels + (label,))),
            )
            break
    else:
        levels.append(ExtremumLevel(value=value, labels=(label,)))
    return _recompile_from_known_levels(
        signature.maximize,
        signature.deletion_horizon,
        labels,
        tuple(levels),
        signature.guard_value,
    )


def delete_extremum_label(
    signature: ExtremumFutureSignature,
    label: int,
) -> ExtremumFutureSignature:
    """Consume one deletion and update the compact state without hidden values."""
    if isinstance(label, bool) or not isinstance(label, int):
        raise ValueError("label must be an integer")
    if label not in signature.labels:
        raise ValueError("deleted label must belong to the signature")
    if signature.deletion_horizon <= 0:
        raise ValueError("no deletion budget remains")

    labels = tuple(item for item in signature.labels if item != label)
    new_horizon = signature.deletion_horizon - 1
    levels = []
    for level in signature.exposed_levels:
        remaining = tuple(item for item in level.labels if item != label)
        if remaining:
            levels.append(ExtremumLevel(value=level.value, labels=remaining))

    return _recompile_from_known_levels(
        signature.maximize,
        new_horizon,
        labels,
        tuple(levels),
        signature.guard_value,
    )


def worst_case_labeled_candidate_count(deletion_horizon: int) -> int:
    """Maximum labels retained by the coarsest scalar signature: exactly h."""
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
    ):
        raise ValueError("deletion_horizon must be a non-negative integer")
    return deletion_horizon
