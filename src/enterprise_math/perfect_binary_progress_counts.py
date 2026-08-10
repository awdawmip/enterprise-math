"""Exact ideal counts for asynchronous progress of perfect binary compilers.

For a perfect binary gate subtree of height h (2^h raw leaves, root gate
included), let F_h be the number of order ideals of its internal-gate poset.
Then

    F_1 = 2,
    F_h = F_(h-1)^2 + 1.

For the full k=2^d conjunction compiler before output z fires, the helper poset
is the disjoint union of two height-(d-1) subtrees, so the asynchronous helper
state count is F_(d-1)^2.  Its width is k/2, while synchronous pre-output
execution has only d states.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PerfectBinaryProgressCount:
    arity: int
    depth: int
    helper_count: int
    helper_poset_width: int
    synchronous_preoutput_state_count: int
    asynchronous_preoutput_state_count: int


def perfect_gate_ideal_count(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be an integer >= 1")
    value = 2
    for _ in range(2, height + 1):
        value = value * value + 1
    return value


def perfect_binary_progress_count(depth: int) -> PerfectBinaryProgressCount:
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 2:
        raise ValueError("depth must be an integer >= 2")
    arity = 1 << depth
    subtree_ideals = perfect_gate_ideal_count(depth - 1)
    async_count = subtree_ideals * subtree_ideals
    return PerfectBinaryProgressCount(
        arity=arity,
        depth=depth,
        helper_count=arity - 2,
        helper_poset_width=arity // 2,
        synchronous_preoutput_state_count=depth,
        asynchronous_preoutput_state_count=async_count,
    )
