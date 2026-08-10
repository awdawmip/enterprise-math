"""Exact completing schedule counts for perfect binary helper compilers.

A complete asynchronous helper firing word is exactly a linear extension of the
helper dependency poset.  For a perfect binary gate tree of height h with
n_h=2^h-1 internal gates, let L_h count linear extensions.  The root is last;
left/right subtree extensions can be interleaved arbitrarily:

    L_1 = 1
    L_h = binom(2*n_(h-1), n_(h-1)) * L_(h-1)^2.

For the pre-output helper forest of the k=2^d conjunction compiler (two
height-(d-1) trees), the same formula gives exactly L_d complete helper words.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

from .perfect_binary_progress_counts import perfect_binary_progress_count


@dataclass(frozen=True)
class PerfectBinaryScheduleCount:
    arity: int
    depth: int
    helper_count: int
    completing_schedule_count: int
    async_progress_state_count: int
    endpoint_class_count: int


def perfect_tree_gate_count(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be an integer >= 1")
    return (1 << height) - 1


def perfect_tree_linear_extensions(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be an integer >= 1")
    value = 1
    for h in range(2, height + 1):
        child_nodes = perfect_tree_gate_count(h - 1)
        value = comb(2 * child_nodes, child_nodes) * value * value
    return value


def perfect_binary_schedule_count(depth: int) -> PerfectBinaryScheduleCount:
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 2:
        raise ValueError("depth must be an integer >= 2")
    arity = 1 << depth
    helper_count = arity - 2
    schedule_count = perfect_tree_linear_extensions(depth)
    progress = perfect_binary_progress_count(depth)
    return PerfectBinaryScheduleCount(
        arity=arity,
        depth=depth,
        helper_count=helper_count,
        completing_schedule_count=schedule_count,
        async_progress_state_count=progress.asynchronous_preoutput_state_count,
        endpoint_class_count=1,
    )
