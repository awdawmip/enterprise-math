"""E001.8 task-relative future quotient for a collapsed contact fiber.

Fix one macro-contact factor ``d`` and restrict attention to the current contact
fiber ``r in {0,...,d-1}``, where the coarse gap is zero.  Let the future action
alphabet consist of non-negative *separating* primitive-gap increments.

After a word of actions with cumulative increment ``s``, contact persists iff

    r + s < d.

Hence two current details are future-equivalent for the Boolean contact/exit
language exactly when no cumulative increment reachable from the action alphabet
separates their remaining boundary capacities ``d-r``.

Because increments are non-negative, only reachable cumulative sums below ``d``
matter.  They induce the coarsest exact partition of the contact fiber for the
entire unbounded future word language:

    r ~ r'  iff  for every reachable s<d,
                 [r+s >= d] == [r'+s >= d].

If unit increment ``1`` is available, every detail is eventually distinguishable
and the exact bounded remainder is required.  If the action semigroup is coarser
(e.g. only increment 2), several adjacent details remain future-equivalent.

This is an E001 application/specialization of the A2/P023 future-compatible
quotient question.  It does not claim Myhill-Nerode/task-relative quotient
minimization as new mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterable


@dataclass(frozen=True)
class ContactFutureQuotient:
    """Coarsest contact-fiber partition for one separating-action alphabet."""

    collapse_factor: int
    increments: tuple[int, ...]
    reachable_subfactor_sums: tuple[int, ...]
    classes: tuple[tuple[int, ...], ...]


def _require_positive_factor(collapse_factor: int) -> None:
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")


def _normalize_increments(increments: Iterable[int]) -> tuple[int, ...]:
    normalized = sorted(set(increments))
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in normalized):
        raise ValueError("increments must be non-negative integers")
    return tuple(normalized)


def reachable_subfactor_sums(
    collapse_factor: int,
    increments: Iterable[int],
) -> tuple[int, ...]:
    """Return all cumulative action sums in ``[0,d-1]`` reachable by finite words."""
    _require_positive_factor(collapse_factor)
    actions = _normalize_increments(increments)
    positive = tuple(value for value in actions if 0 < value < collapse_factor)

    reachable = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for increment in positive:
            updated = current + increment
            if updated >= collapse_factor or updated in reachable:
                continue
            reachable.add(updated)
            frontier.append(updated)
    return tuple(sorted(reachable))


def contact_exit_signature(
    detail: int,
    collapse_factor: int,
    increments: Iterable[int],
) -> tuple[bool, ...]:
    """Boolean exit signature over every reachable subfactor cumulative increment."""
    _require_positive_factor(collapse_factor)
    if isinstance(detail, bool) or not isinstance(detail, int) or not 0 <= detail < collapse_factor:
        raise ValueError("detail must lie in the current contact fiber")
    sums = reachable_subfactor_sums(collapse_factor, increments)
    return tuple(detail + cumulative >= collapse_factor for cumulative in sums)


def contact_future_quotient(
    collapse_factor: int,
    increments: Iterable[int],
) -> ContactFutureQuotient:
    """Return the coarsest exact partition for all finite words over the action alphabet."""
    _require_positive_factor(collapse_factor)
    actions = _normalize_increments(increments)
    sums = reachable_subfactor_sums(collapse_factor, actions)

    by_signature: dict[tuple[bool, ...], list[int]] = {}
    for detail in range(collapse_factor):
        signature = tuple(
            detail + cumulative >= collapse_factor for cumulative in sums
        )
        by_signature.setdefault(signature, []).append(detail)

    classes = tuple(
        sorted(
            (tuple(details) for details in by_signature.values()),
            key=lambda block: block[0],
        )
    )
    flattened = tuple(detail for block in classes for detail in block)
    if flattened != tuple(range(collapse_factor)):
        raise AssertionError("future quotient failed to partition the contact fiber")
    return ContactFutureQuotient(
        collapse_factor=collapse_factor,
        increments=actions,
        reachable_subfactor_sums=sums,
        classes=classes,
    )


def future_class_for_detail(
    quotient: ContactFutureQuotient,
    detail: int,
) -> int:
    """Return the exact class index of one current contact-fiber detail."""
    if isinstance(detail, bool) or not isinstance(detail, int):
        raise ValueError("detail must be an integer")
    for index, block in enumerate(quotient.classes):
        if detail in block:
            return index
    raise ValueError("detail does not belong to the quotient contact fiber")
