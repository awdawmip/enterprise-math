"""Work/depth/storage tradeoffs for one fixed prefix-observable OR semantics.

The semantic object is already fixed: for H k-bit action masks, output every
inclusive prefix OR

    U_t = A_1 OR ... OR A_t,  t=1,...,H.

This module compares exact implementations of that same prefix trace.

### Sequential streaming scan

Maintain one current k-bit mask and emit each prefix as it is formed.

* word-level OR gates: H-1;
* bit work: k*(H-1);
* dependency depth from all inputs available at once: H-1;
* extra working masks beyond the output sink:1.

The H-1 gate count is globally minimum in a fan-in-two OR-only circuit that must
produce the final prefix, because the final prefix is the OR of H independent
inputs.  The chain attains that lower bound while exposing all intermediate
prefixes for free along the chain.

### Hillis-Steele parallel inclusive scan

For offsets 1,2,4,..., use synchronized rounds.  At offset s, positions s..H-1
OR the previous-round value from i-s into i.  With

    r=ceil(log2 H),

* depth: r;
* word-level OR gates: sum_j (H-2^j) = r*H-(2^r-1);
* bit work: k times that count;
* clean double-buffer working storage:2H k-bit masks.

It attains the unavoidable depth lower bound from the final H-input OR, while
paying extra work/storage.  No claim is made that Hillis-Steele minimizes work
among all depth-optimal prefix networks.

### Terminal-only balanced reduction

A balanced OR tree computes only the final effect using H-1 word gates and depth
ceil(log2 H).  It is a useful resource lower envelope but is **not semantically
valid** for the declared full-prefix output language.

Parallel-prefix networks and scan algorithms are standard prior CS.  The
Enterprise Math value is applying the resource comparison only after the prefix
semantic object has been fixed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def ceil_log2(value: int) -> int:
    number = _positive("value", value)
    if number == 1:
        return 0
    return (number - 1).bit_length()


def sequential_prefix_or(values: Sequence[int], bit_width: int) -> tuple[int, ...]:
    k = _positive("bit_width", bit_width)
    masks = tuple(values)
    if not masks:
        return ()
    limit = 1 << k
    if any(isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit for mask in masks):
        raise ValueError("mask outside declared bit width")
    current = 0
    outputs = []
    for mask in masks:
        current |= mask
        outputs.append(current)
    return tuple(outputs)


def sequential_word_or_gates(word_length: int) -> int:
    h = _positive("word_length", word_length)
    return h - 1


def sequential_bit_work(bit_width: int, word_length: int) -> int:
    k = _positive("bit_width", bit_width)
    return k * sequential_word_or_gates(word_length)


def sequential_dependency_depth(word_length: int) -> int:
    return sequential_word_or_gates(word_length)


def prefix_depth_lower_bound(word_length: int) -> int:
    """Any full prefix circuit must compute the final H-input OR."""
    return ceil_log2(_positive("word_length", word_length))


def prefix_work_lower_bound_word_gates(word_length: int) -> int:
    """Final H-input OR alone needs H-1 binary OR gates."""
    return sequential_word_or_gates(word_length)


def hillis_steele_round_count(word_length: int) -> int:
    return prefix_depth_lower_bound(word_length)


def hillis_steele_word_or_gates(word_length: int) -> int:
    h = _positive("word_length", word_length)
    rounds = hillis_steele_round_count(h)
    return rounds * h - ((1 << rounds) - 1)


def hillis_steele_bit_work(bit_width: int, word_length: int) -> int:
    k = _positive("bit_width", bit_width)
    return k * hillis_steele_word_or_gates(word_length)


def hillis_steele_prefix_or(values: Sequence[int], bit_width: int) -> tuple[int, ...]:
    k = _positive("bit_width", bit_width)
    masks = tuple(values)
    if not masks:
        return ()
    limit = 1 << k
    if any(isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit for mask in masks):
        raise ValueError("mask outside declared bit width")
    current = list(masks)
    offset = 1
    while offset < len(current):
        previous = tuple(current)
        current = [
            previous[index] if index < offset else previous[index] | previous[index - offset]
            for index in range(len(previous))
        ]
        offset <<= 1
    result = tuple(current)
    direct = sequential_prefix_or(masks, k)
    if result != direct:
        raise AssertionError("Hillis-Steele scan disagreed with exact sequential prefix trace")
    return result


def terminal_only_balanced_word_or_gates(word_length: int) -> int:
    return _positive("word_length", word_length) - 1


def terminal_only_balanced_depth(word_length: int) -> int:
    return ceil_log2(_positive("word_length", word_length))


@dataclass(frozen=True)
class PrefixScanResourcePoint:
    name: str
    word_or_gates: int
    bit_work: int
    parallel_depth: int
    extra_working_masks: int
    output_masks: int
    full_prefix_semantics: bool

    @property
    def total_live_masks_with_materialized_output(self) -> int:
        return self.extra_working_masks + self.output_masks


@dataclass(frozen=True)
class PrefixScanParetoReport:
    bit_width: int
    word_length: int
    work_lower_bound_word_gates: int
    depth_lower_bound: int
    sequential_streaming: PrefixScanResourcePoint
    hillis_steele_parallel: PrefixScanResourcePoint
    terminal_only_balanced: PrefixScanResourcePoint

    @property
    def hillis_steele_extra_word_work(self) -> int:
        return (
            self.hillis_steele_parallel.word_or_gates
            - self.sequential_streaming.word_or_gates
        )

    @property
    def hillis_steele_depth_saving(self) -> int:
        return (
            self.sequential_streaming.parallel_depth
            - self.hillis_steele_parallel.parallel_depth
        )


def prefix_scan_pareto_report(bit_width: int, word_length: int) -> PrefixScanParetoReport:
    k = _positive("bit_width", bit_width)
    h = _positive("word_length", word_length)
    sequential = PrefixScanResourcePoint(
        name="sequential-streaming-prefix-scan",
        word_or_gates=sequential_word_or_gates(h),
        bit_work=sequential_bit_work(k, h),
        parallel_depth=sequential_dependency_depth(h),
        extra_working_masks=1,
        output_masks=h,
        full_prefix_semantics=True,
    )
    parallel = PrefixScanResourcePoint(
        name="hillis-steele-parallel-prefix-scan",
        word_or_gates=hillis_steele_word_or_gates(h),
        bit_work=hillis_steele_bit_work(k, h),
        parallel_depth=hillis_steele_round_count(h),
        extra_working_masks=2 * h,
        output_masks=h,
        full_prefix_semantics=True,
    )
    terminal = PrefixScanResourcePoint(
        name="terminal-only-balanced-reduction",
        word_or_gates=terminal_only_balanced_word_or_gates(h),
        bit_work=k * terminal_only_balanced_word_or_gates(h),
        parallel_depth=terminal_only_balanced_depth(h),
        extra_working_masks=h,
        output_masks=1,
        full_prefix_semantics=False,
    )
    return PrefixScanParetoReport(
        bit_width=k,
        word_length=h,
        work_lower_bound_word_gates=prefix_work_lower_bound_word_gates(h),
        depth_lower_bound=prefix_depth_lower_bound(h),
        sequential_streaming=sequential,
        hillis_steele_parallel=parallel,
        terminal_only_balanced=terminal,
    )
