"""Representation-independent continuation-state capacity bounds.

A fixed number of integer registers is not itself a low-complexity guarantee: an
unbounded integer can encode an arbitrarily long history.  The invariant object
is the number C of future-distinguishable continuation classes required by the
declared causal task.

Any exact encoding of C classes must use at least C distinct code states.  If a
single nonnegative integer is used, the smallest possible maximum code value is
C-1 (achieved by 0,...,C-1).  Thus coding a large continuation quotient into one
integer does not erase its causal state capacity.
"""

from __future__ import annotations


def minimum_nonnegative_code_ceiling(class_count: int) -> int:
    """Smallest possible max code for an injective N0 encoding of C classes."""
    if isinstance(class_count, bool) or not isinstance(class_count, int) or class_count <= 0:
        raise ValueError("class_count must be a positive integer")
    return class_count - 1


def exact_encoding_has_enough_states(class_count: int, available_state_count: int) -> bool:
    if isinstance(class_count, bool) or not isinstance(class_count, int) or class_count <= 0:
        raise ValueError("class_count must be a positive integer")
    if (
        isinstance(available_state_count, bool)
        or not isinstance(available_state_count, int)
        or available_state_count < 0
    ):
        raise ValueError("available_state_count must be a non-negative integer")
    return available_state_count >= class_count


def nonnegative_register_capacity(maximum_code: int) -> int:
    """Number of states available in one register restricted to 0..maximum_code."""
    if isinstance(maximum_code, bool) or not isinstance(maximum_code, int) or maximum_code < 0:
        raise ValueError("maximum_code must be a non-negative integer")
    return maximum_code + 1


def minimum_register_ceiling_profile(class_counts: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(class_counts, tuple) or not class_counts:
        raise ValueError("class_counts must be a non-empty tuple")
    return tuple(minimum_nonnegative_code_ceiling(count) for count in class_counts)
