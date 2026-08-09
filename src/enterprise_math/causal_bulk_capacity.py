"""Capacity bounds for finite structural state plus additive integer bulk channels.

Consider a dimension-uniform repeated-slot generator with:

* at most M structural continuation types;
* r integer bulk channels;
* additive bulk updates;
* for each channel j, every one-step increment lies in a fixed integer interval
  of width R_j, because it depends only on finite local symbol/type data.

After d steps channel j occupies at most d*R_j+1 integer values, hence the whole
causal state has at most

    M * product_j (d*R_j + 1)

possible states.  This gives a representation-independent polynomial-capacity
upper bound for the declared schema.  Exponential tasks such as binary copy
cannot be represented by any fixed M,r,R_j of this form.

An update such as `s <- 2*s + x` escapes the theorem because it is not bounded-
increment additive bulk transport: it scales the already accumulated bulk.
"""

from __future__ import annotations

from math import prod


def additive_bulk_state_bound(
    continuation_type_count: int,
    increment_widths: tuple[int, ...],
    depth: int,
) -> int:
    if (
        isinstance(continuation_type_count, bool)
        or not isinstance(continuation_type_count, int)
        or continuation_type_count <= 0
    ):
        raise ValueError("continuation_type_count must be a positive integer")
    if not isinstance(increment_widths, tuple):
        raise ValueError("increment_widths must be a tuple")
    if any(
        isinstance(width, bool) or not isinstance(width, int) or width < 0
        for width in increment_widths
    ):
        raise ValueError("increment widths must be non-negative integers")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    return continuation_type_count * prod(depth * width + 1 for width in increment_widths)


def additive_bulk_capacity_violation(
    required_classes: int,
    continuation_type_count: int,
    increment_widths: tuple[int, ...],
    depth: int,
) -> bool:
    if isinstance(required_classes, bool) or not isinstance(required_classes, int) or required_classes <= 0:
        raise ValueError("required_classes must be a positive integer")
    return required_classes > additive_bulk_state_bound(
        continuation_type_count,
        increment_widths,
        depth,
    )


def first_binary_copy_additive_bulk_violation(
    continuation_type_count: int,
    increment_widths: tuple[int, ...],
    maximum_half_length: int,
) -> int | None:
    """First d where 2^d midpoint copy classes exceed the additive-bulk bound."""
    if (
        isinstance(maximum_half_length, bool)
        or not isinstance(maximum_half_length, int)
        or maximum_half_length <= 0
    ):
        raise ValueError("maximum_half_length must be a positive integer")
    for depth in range(1, maximum_half_length + 1):
        if additive_bulk_capacity_violation(
            2**depth,
            continuation_type_count,
            increment_widths,
            depth,
        ):
            return depth
    return None


def nontrivial_bulk_channel_count(increment_widths: tuple[int, ...]) -> int:
    """Number of additive bulk channels whose reachable range can grow with depth."""
    if not isinstance(increment_widths, tuple):
        raise ValueError("increment_widths must be a tuple")
    if any(
        isinstance(width, bool) or not isinstance(width, int) or width < 0
        for width in increment_widths
    ):
        raise ValueError("increment widths must be non-negative integers")
    return sum(width > 0 for width in increment_widths)
