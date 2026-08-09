"""Continuation-capacity bounds for fixed finite-range integer grade laws.

Suppose a finite alphabet of size A is scored by a fixed q-window integer grade
whose local values lie in [g_min,g_max].  After a prefix of length d>=q-1, an
exact raw future state is `(accumulated_grade,last_q_minus_1_symbols)`.

There are at most A^(q-1) suffix memories.  The completed-window count is
`d-q+1`; because each window grade lies in a fixed integer interval of width R,
the accumulated grade lies in an integer interval containing at most
`(d-q+1)*R+1` values.  Hence the number of future-distinguishable states required
by any such representation is bounded above by

    A^(q-1) * ((d-q+1)*R + 1).

Therefore a task whose exact continuation-class count exceeds this bound cannot
be represented by that fixed-local-grade schema.  The bound is deliberately
integer and representation-facing; no entropy or logarithm is needed.
"""

from __future__ import annotations


def fixed_local_grade_state_bound(
    alphabet_size: int,
    window: int,
    depth: int,
    local_grade_min: int,
    local_grade_max: int,
) -> int:
    if isinstance(alphabet_size, bool) or not isinstance(alphabet_size, int) or alphabet_size <= 0:
        raise ValueError("alphabet_size must be a positive integer")
    if isinstance(window, bool) or not isinstance(window, int) or window <= 0:
        raise ValueError("window must be a positive integer")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in (local_grade_min, local_grade_max)
    ):
        raise ValueError("local grade bounds must be integers")
    if local_grade_min > local_grade_max:
        raise ValueError("local_grade_min cannot exceed local_grade_max")

    if depth < window - 1:
        # No completed q-window yet; the raw prefix itself is at most A^depth.
        return alphabet_size**depth

    suffix_states = alphabet_size ** (window - 1)
    completed_windows = depth - window + 1
    grade_width = local_grade_max - local_grade_min
    grade_states = completed_windows * grade_width + 1
    return suffix_states * grade_states


def capacity_violation(
    required_classes: int,
    alphabet_size: int,
    window: int,
    depth: int,
    local_grade_min: int,
    local_grade_max: int,
) -> bool:
    if isinstance(required_classes, bool) or not isinstance(required_classes, int) or required_classes <= 0:
        raise ValueError("required_classes must be a positive integer")
    return required_classes > fixed_local_grade_state_bound(
        alphabet_size,
        window,
        depth,
        local_grade_min,
        local_grade_max,
    )


def first_binary_copy_violation(
    window: int,
    local_grade_min: int,
    local_grade_max: int,
    maximum_half_length: int,
) -> int | None:
    """First midpoint n where copy-language capacity 2^n beats the local-grade bound."""
    if (
        isinstance(maximum_half_length, bool)
        or not isinstance(maximum_half_length, int)
        or maximum_half_length <= 0
    ):
        raise ValueError("maximum_half_length must be a positive integer")
    for half in range(1, maximum_half_length + 1):
        if capacity_violation(
            2**half,
            2,
            window,
            half,
            local_grade_min,
            local_grade_max,
        ):
            return half
    return None
