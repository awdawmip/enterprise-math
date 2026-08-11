"""Fixed-k long-horizon information limits for prefix semantic quotients.

Let a length-H literal word be iid uniform on k generator labels and let H grow
with k fixed.

Eventually all k generators are seen with probability tending to1.  Hence the
terminal-set semantic state converges to the deterministic full set and

    H_terminal -> 0.

By symmetry, conditional on all generators appearing, their first-appearance
order is uniform on k! permutations.  The missing-generator probability tends to
zero, so

    H_discovery -> log2(k!).

After i distinct generators have been discovered, each new action is already
seen with probability q_i=i/k and is a new generator with probability
p_i=(k-i)/k.  The duration of discovery phase i (for i<k) therefore converges to
a positive geometric waiting time

    P(R_i=r)=q_i^(r-1) p_i.

The coupon-collector waiting times are independent across phases, and the next
new generator identity is uniform among unseen labels independently of the wait.
The final phase duration is determined by H and the preceding waits.  Therefore
full-timing semantic entropy converges to

    log2(k!) + sum_{i=1}^{k-1} H(Geom(p_i)).

For a positive geometric variable with success p and q=1-p,

    H(Geom(p)) = -log2 p - (q/p) log2 q.

Thus timing entropy has a finite fixed-k limit even though the **number** of
possible timing classes at exact H grows polynomially like k H^(k-1).
Meanwhile literal entropy is H log2 k, so asymptotically almost all additional
literal information lies in stutter-action provenance:

    H_literal - H_timing = H log2 k - O_k(1).

This is a sharp workload-vs-worst-case semantic complexity separation.

Coupon collector waiting times and geometric entropy are standard probability /
information theory.  The Enterprise Math value is the exact Stage131 semantic-
information asymptotic and its contrast with class-count growth.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, log2

from .prefix_semantic_information_decomposition import (
    discovery_semantic_entropy_bits,
    literal_word_entropy_bits,
    terminal_semantic_entropy_bits,
    timing_semantic_entropy_bits,
)


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def positive_geometric_entropy_bits(success_probability: float) -> float:
    p = float(success_probability)
    if not 0.0 < p <= 1.0:
        raise ValueError("success_probability must lie in (0,1]")
    if p == 1.0:
        return 0.0
    q = 1.0 - p
    return -log2(p) - (q / p) * log2(q)


def discovery_entropy_limit_bits(generator_count: int) -> float:
    k = _positive("generator_count", generator_count)
    return log2(factorial(k))


def duration_entropy_limit_bits(generator_count: int) -> float:
    k = _positive("generator_count", generator_count)
    return sum(
        positive_geometric_entropy_bits((k - seen) / k)
        for seen in range(1, k)
    )


def timing_entropy_limit_bits(generator_count: int) -> float:
    k = _positive("generator_count", generator_count)
    return discovery_entropy_limit_bits(k) + duration_entropy_limit_bits(k)


def missing_any_generator_union_bound(generator_count: int, word_length: int) -> float:
    """Simple union bound k*((k-1)/k)^H, capped at1."""
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    if k == 1:
        return 0.0
    return min(1.0, k * (((k - 1) / k) ** h))


def timing_entropy_gap_to_limit_bits(generator_count: int, word_length: int) -> float:
    return (
        timing_entropy_limit_bits(generator_count)
        - timing_semantic_entropy_bits(generator_count, word_length)
    )


def discovery_entropy_gap_to_limit_bits(generator_count: int, word_length: int) -> float:
    return (
        discovery_entropy_limit_bits(generator_count)
        - discovery_semantic_entropy_bits(generator_count, word_length)
    )


def stutter_provenance_asymptotic_residual_bits(
    generator_count: int,
    word_length: int,
) -> float:
    """Difference between actual stutter-provenance loss and H log k - limit.

    This tends to zero with H because timing entropy tends to its finite limit.
    """
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    actual = literal_word_entropy_bits(k, h) - timing_semantic_entropy_bits(k, h)
    asymptotic = h * log2(k) - timing_entropy_limit_bits(k)
    return actual - asymptotic


@dataclass(frozen=True)
class PrefixInformationAsymptoticReport:
    generator_count: int
    word_length: int
    terminal_entropy_bits: float
    discovery_entropy_bits: float
    timing_entropy_bits: float
    literal_entropy_bits: float
    discovery_limit_bits: float
    duration_limit_bits: float
    timing_limit_bits: float
    missing_generator_union_bound: float

    @property
    def timing_gap_to_limit_bits(self) -> float:
        return self.timing_limit_bits - self.timing_entropy_bits

    @property
    def discovery_gap_to_limit_bits(self) -> float:
        return self.discovery_limit_bits - self.discovery_entropy_bits

    @property
    def stutter_provenance_bits(self) -> float:
        return self.literal_entropy_bits - self.timing_entropy_bits


def prefix_information_asymptotic_report(
    generator_count: int,
    word_length: int,
) -> PrefixInformationAsymptoticReport:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return PrefixInformationAsymptoticReport(
        generator_count=k,
        word_length=h,
        terminal_entropy_bits=terminal_semantic_entropy_bits(k, h),
        discovery_entropy_bits=discovery_semantic_entropy_bits(k, h),
        timing_entropy_bits=timing_semantic_entropy_bits(k, h),
        literal_entropy_bits=literal_word_entropy_bits(k, h),
        discovery_limit_bits=discovery_entropy_limit_bits(k),
        duration_limit_bits=duration_entropy_limit_bits(k),
        timing_limit_bits=timing_entropy_limit_bits(k),
        missing_generator_union_bound=missing_any_generator_union_bound(k, h),
    )
