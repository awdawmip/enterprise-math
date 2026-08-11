"""Reuse tradeoff for materialized OR normal forms versus fused one-shot execution.

For a k-bit commuting-idempotent word of length H, one reusable semantic effect
mask costs k*(H-1) OR gates to normalize.  Applying it to q states costs k*q
additional OR gates, for

    W_materialize = k*(H-1+q).

If the normal form is not materialized and each state independently fuses its
state bit into the H action inputs, work is

    W_fused = k*H*q.

The exact work saving from materialization is

    k*(q-1)*(H-1).

For q=1 there is no work saving and fused one-shot execution can have one less
parallel layer.  For q>1, materialization amortizes normalization across uses.
This exposes reuse count as a separate representation-resource coordinate.
"""

from __future__ import annotations

from dataclasses import dataclass

from .or_circuit_execution_lower_bound import (
    one_shot_execution_depth_lower_bound,
    reusable_normal_form_depth_lower_bound,
)


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def materialized_reuse_work(generator_count: int, word_length: int, reuse_count: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    q = _positive("reuse_count", reuse_count)
    return k * (h - 1 + q)


def independent_fused_work(generator_count: int, word_length: int, reuse_count: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    q = _positive("reuse_count", reuse_count)
    return k * h * q


def materialization_work_saving(generator_count: int, word_length: int, reuse_count: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    q = _positive("reuse_count", reuse_count)
    return k * (q - 1) * (h - 1)


def parallel_materialized_reuse_depth(word_length: int) -> int:
    """Normalize once, then apply to all reused states in one parallel round."""
    h = _positive("word_length", word_length)
    return reusable_normal_form_depth_lower_bound(h) + 1


def parallel_independent_fused_depth(word_length: int) -> int:
    """Assume q independent fused state executions can run in parallel."""
    h = _positive("word_length", word_length)
    return one_shot_execution_depth_lower_bound(h)


@dataclass(frozen=True)
class ORNormalFormReuseReport:
    generator_count: int
    word_length: int
    reuse_count: int
    materialized_work: int
    fused_work: int
    work_saving: int
    materialized_parallel_depth: int
    fused_parallel_depth: int

    @property
    def materialization_saves_work(self) -> bool:
        return self.work_saving > 0

    @property
    def materialization_depth_tax(self) -> int:
        return self.materialized_parallel_depth - self.fused_parallel_depth


def or_normal_form_reuse_report(
    generator_count: int,
    word_length: int,
    reuse_count: int,
) -> ORNormalFormReuseReport:
    return ORNormalFormReuseReport(
        generator_count=_positive("generator_count", generator_count),
        word_length=_positive("word_length", word_length),
        reuse_count=_positive("reuse_count", reuse_count),
        materialized_work=materialized_reuse_work(generator_count, word_length, reuse_count),
        fused_work=independent_fused_work(generator_count, word_length, reuse_count),
        work_saving=materialization_work_saving(generator_count, word_length, reuse_count),
        materialized_parallel_depth=parallel_materialized_reuse_depth(word_length),
        fused_parallel_depth=parallel_independent_fused_depth(word_length),
    )
