"""Exact work/depth bounds for formulaic OR future-law execution.

Consider the commuting-idempotent k-bit action family from the parent generation.
A length-H word contributes H k-bit masks.

### Reusable normal-form output

To materialize the exact word effect, each output coordinate is the OR of H
independent input bits.  In a fan-in-two OR-only circuit:

* depth >= ceil(log2 H), because depth d reaches at most 2^d inputs;
* work >= H-1 gates per output coordinate.

Different output coordinates use disjoint input-variable sets.  An OR-only gate
mixing coordinates would introduce an irreversible wrong dependency, so the
lower bounds add across coordinates:

    normalization work >= k*(H-1).

Balanced coordinatewise OR trees attain both bounds.

### One-shot state execution

If the normalized effect does not need to be exposed/reused and the task only
asks for the updated state, coordinate i is the OR of H action-mask bits **and**
the current state bit: H+1 inputs.

Thus exact fan-in-two OR-only lower bounds are

    one-shot work >= k*H,
    one-shot depth >= ceil(log2(H+1)),

and a fused balanced tree attains both simultaneously.

The staged implementation from the parent (normalize, then apply) has the same
one-shot work kH but depth ceil(log2 H)+1.  It is therefore depth-optimal only at
horizons where that equals ceil(log2(H+1)); otherwise materializing the
intermediate normal form creates a pipeline-depth tax.

The normal form remains valuable when it must be retained or reused across
multiple states.  The theorem therefore separates one-shot execution from
reusable operation compilation rather than declaring one universally superior.

Circuit lower bounds for OR trees are standard prior CS.  The project value is
the exact future-interface interpretation of intermediate-state materialization.
"""

from __future__ import annotations

from dataclasses import dataclass


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def ceil_log2(value: int) -> int:
    number = _positive("value", value)
    if number == 1:
        return 0
    return (number - 1).bit_length()


def reusable_normal_form_work_lower_bound(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return k * (h - 1)


def reusable_normal_form_depth_lower_bound(word_length: int) -> int:
    h = _positive("word_length", word_length)
    return ceil_log2(h)


def one_shot_execution_work_lower_bound(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return k * h


def one_shot_execution_depth_lower_bound(word_length: int) -> int:
    h = _positive("word_length", word_length)
    return ceil_log2(h + 1)


def staged_normalize_then_apply_depth(word_length: int) -> int:
    h = _positive("word_length", word_length)
    return reusable_normal_form_depth_lower_bound(h) + 1


def staged_normalize_then_apply_work(generator_count: int, word_length: int) -> int:
    return one_shot_execution_work_lower_bound(generator_count, word_length)


def intermediate_materialization_depth_tax(word_length: int) -> int:
    h = _positive("word_length", word_length)
    return (
        staged_normalize_then_apply_depth(h)
        - one_shot_execution_depth_lower_bound(h)
    )


def staged_depth_is_one_shot_optimal(word_length: int) -> bool:
    return intermediate_materialization_depth_tax(word_length) == 0


def fused_one_shot_coordinate(
    state_bit: int,
    action_bits: tuple[int, ...],
) -> int:
    if state_bit not in (0, 1):
        raise ValueError("state_bit must be 0/1")
    if not action_bits:
        raise ValueError("at least one action bit is required")
    if any(bit not in (0, 1) for bit in action_bits):
        raise ValueError("action bits must be 0/1")
    result = state_bit
    for bit in action_bits:
        result |= bit
    return result


def fused_one_shot_mask(
    state_mask: int,
    action_masks: tuple[int, ...],
    generator_count: int,
) -> int:
    k = _positive("generator_count", generator_count)
    limit = 1 << k
    if isinstance(state_mask, bool) or not isinstance(state_mask, int) or not 0 <= state_mask < limit:
        raise ValueError("state_mask outside k-bit state space")
    if not action_masks:
        raise ValueError("at least one action mask is required")
    result = state_mask
    for mask in action_masks:
        if isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit:
            raise ValueError("action mask outside k-bit effect space")
        result |= mask
    return result


@dataclass(frozen=True)
class ORExecutionLowerBoundReport:
    generator_count: int
    word_length: int
    reusable_normal_form_work: int
    reusable_normal_form_depth: int
    staged_one_shot_work: int
    staged_one_shot_depth: int
    fused_one_shot_work: int
    fused_one_shot_depth: int
    materialization_depth_tax: int

    @property
    def fused_hits_work_lower_bound(self) -> bool:
        return self.fused_one_shot_work == one_shot_execution_work_lower_bound(
            self.generator_count,
            self.word_length,
        )

    @property
    def fused_hits_depth_lower_bound(self) -> bool:
        return self.fused_one_shot_depth == one_shot_execution_depth_lower_bound(
            self.word_length,
        )


def or_execution_lower_bound_report(
    generator_count: int,
    word_length: int,
) -> ORExecutionLowerBoundReport:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return ORExecutionLowerBoundReport(
        generator_count=k,
        word_length=h,
        reusable_normal_form_work=reusable_normal_form_work_lower_bound(k, h),
        reusable_normal_form_depth=reusable_normal_form_depth_lower_bound(h),
        staged_one_shot_work=staged_normalize_then_apply_work(k, h),
        staged_one_shot_depth=staged_normalize_then_apply_depth(h),
        fused_one_shot_work=one_shot_execution_work_lower_bound(k, h),
        fused_one_shot_depth=one_shot_execution_depth_lower_bound(h),
        materialization_depth_tax=intermediate_materialization_depth_tax(h),
    )
