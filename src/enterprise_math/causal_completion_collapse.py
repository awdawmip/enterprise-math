"""Causally generated growth observables feeding the P008 root/collapse core.

A LEGO/causal construction may produce a sequence V(k) of integer observations
for complete structural levels k: configuration count, ball cardinality, shell
capacity, admissible-state count, etc.  P008 applies exactly when k -> V(k) is an
order embedding (strictly increasing on the integer chain).  Then

    R_V(n) = max{k : V(k) <= n}
    C_V(n) = V(R_V(n))

is the right-adjoint completion root and induced idempotent downward collapse.

If V has plateaus, capacity alone cannot recover level identity.  This is not a
numerical failure: those levels are observationally collapsed by V and must
remain identified or the observable must be refined.  In particular, the free
one-slot allocation count H_1(c)=1 cannot serve as a value-scale embedding even
though c itself remains a perfectly valid integer bulk value.
"""

from __future__ import annotations


def _validate_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in capacities
    ):
        raise ValueError("capacities must be non-negative integers")


def observable_is_monotone(capacities: tuple[int, ...]) -> bool:
    _validate_capacities(capacities)
    return all(left <= right for left, right in zip(capacities, capacities[1:]))


def observable_is_order_embedding(capacities: tuple[int, ...]) -> bool:
    """On a finite integer chain, order embedding is strict increase."""
    _validate_capacities(capacities)
    return all(left < right for left, right in zip(capacities, capacities[1:]))


def completion_root_index(capacities: tuple[int, ...], amount: int) -> int | None:
    """Largest represented structural level whose complete observation is <= amount."""
    _validate_capacities(capacities)
    if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
        raise ValueError("amount must be a non-negative integer")
    if not observable_is_monotone(capacities):
        raise ValueError("completion root requires a monotone represented growth law")
    result = None
    for index, capacity in enumerate(capacities):
        if capacity <= amount:
            result = index
        else:
            break
    return result


def completion_collapse(capacities: tuple[int, ...], amount: int) -> int | None:
    """P008-style projection to the largest represented complete capacity <= amount."""
    index = completion_root_index(capacities, amount)
    return None if index is None else capacities[index]


def exact_level_recovery(capacities: tuple[int, ...]) -> bool:
    """Whether R_V(V(k))=k for every represented level."""
    if not observable_is_order_embedding(capacities):
        return False
    return all(
        completion_root_index(capacities, capacity) == index
        for index, capacity in enumerate(capacities)
    )


def plateau_level_classes(capacities: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Levels identified by the same monotone structural observation."""
    _validate_capacities(capacities)
    if not observable_is_monotone(capacities):
        raise ValueError("plateau classes require a monotone observable")
    result = []
    current = [0]
    for index in range(1, len(capacities)):
        if capacities[index] == capacities[index - 1]:
            current.append(index)
        else:
            result.append(tuple(current))
            current = [index]
    result.append(tuple(current))
    return tuple(result)


def collapse_is_idempotent_on_represented_range(
    capacities: tuple[int, ...],
    maximum_amount: int,
) -> bool:
    _validate_capacities(capacities)
    if isinstance(maximum_amount, bool) or not isinstance(maximum_amount, int) or maximum_amount < 0:
        raise ValueError("maximum_amount must be a non-negative integer")
    for amount in range(maximum_amount + 1):
        first = completion_collapse(capacities, amount)
        if first is None:
            continue
        second = completion_collapse(capacities, first)
        if second != first:
            return False
    return True
