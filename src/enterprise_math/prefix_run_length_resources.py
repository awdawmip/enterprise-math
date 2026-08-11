"""Growth/storage laws for the prefix run-length normal form.

For fixed generator count k and exact word length H, prefix-observable semantic
classes are

    N(k,H)=sum_{s=1}^{min(k,H)} P(k,s) C(H-1,s-1).

For H>=k this is a polynomial in H of degree k-1.  The s=k term has leading
coefficient

    k!/(k-1)! = k,

so N(k,H) ~ k*H^(k-1) for fixed k.

This sits strictly between literal syntax and terminal effects:

    literal words: k^H,
    prefix semantics: Theta(H^(k-1)) for fixed k,
    terminal effects: 2^k-1 once H>=k.

A concrete prefix run form with s<=k phases can be stored explicitly using:

* s generator IDs, each ceil(log2 k) bits in a simple fixed-width scheme;
* s positive run lengths, each ceil(log2(H+1)) bits.

This is an easy O(k log H) upper bound for fixed k, versus kH bits to materialize
all H cumulative k-bit prefix masks.

For a fixed phase count s, the exact number of forms is

    P(k,s) C(H-1,s-1),

so the information lower bound is the ceiling of its binary logarithm.  This can
be approached by ranking the ordered distinct generator tuple and the positive
composition (cut positions) separately.

Composition of two normal forms scans at most k right phases and keeps at most k
output phases; high-level structural work is therefore O(k), independent of the
literal word lengths, with integer run-length additions carrying O(log H) bit
cost.  Decoding the full prefix trace still requires H outputs.  This separates
compact compositional state from materialized observable history.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial

from .prefix_observable_or_word_semantics import prefix_trace_count_exact_length


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def ceil_log2_integer(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    if value == 1:
        return 0
    return (value - 1).bit_length()


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def prefix_semantic_class_count(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    return prefix_trace_count_exact_length(k, word_length)


def literal_word_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    return 1 if word_length == 0 else k**word_length


def terminal_effect_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(comb(k, s) for s in range(1, min(k, word_length) + 1))


def fixed_phase_form_count(generator_count: int, word_length: int, phase_count: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    if isinstance(phase_count, bool) or not isinstance(phase_count, int) or not 1 <= phase_count <= min(k, h):
        raise ValueError("phase_count must lie in 1..min(k,H)")
    return falling_factorial(k, phase_count) * comb(h - 1, phase_count - 1)


def fixed_phase_information_lower_bound_bits(
    generator_count: int,
    word_length: int,
    phase_count: int,
) -> int:
    return ceil_log2_integer(
        fixed_phase_form_count(generator_count, word_length, phase_count)
    )


def total_prefix_information_lower_bound_bits(generator_count: int, word_length: int) -> int:
    return ceil_log2_integer(prefix_semantic_class_count(generator_count, word_length))


def simple_rle_storage_upper_bound_bits(
    generator_count: int,
    word_length: int,
    phase_count: int,
) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    if isinstance(phase_count, bool) or not isinstance(phase_count, int) or not 0 <= phase_count <= min(k, h):
        raise ValueError("phase_count must lie in 0..min(k,H)")
    if h == 0:
        return 0
    generator_bits = ceil_log2_integer(k)
    run_bits = ceil_log2_integer(h + 1)
    return phase_count * (generator_bits + run_bits)


def full_materialized_prefix_trace_bits(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    return k * word_length


def leading_polynomial_coefficient(generator_count: int) -> int:
    """Leading coefficient of N_prefix(k,H) as polynomial in H for fixed k."""
    return _positive("generator_count", generator_count)


def max_normal_form_phases(generator_count: int) -> int:
    return _positive("generator_count", generator_count)


def composition_phase_work_upper_bound(generator_count: int) -> int:
    """One high-level visit per possible right phase."""
    return _positive("generator_count", generator_count)


@dataclass(frozen=True)
class PrefixRunResourceReport:
    generator_count: int
    word_length: int
    literal_words: int
    prefix_semantic_classes: int
    terminal_effects: int
    total_information_lower_bound_bits: int
    materialized_trace_bits: int
    maximum_phases: int
    worst_case_simple_rle_bits: int
    composition_phase_work_upper_bound: int

    @property
    def materialized_to_rle_bit_ratio(self) -> float:
        if self.worst_case_simple_rle_bits == 0:
            return 1.0
        return self.materialized_trace_bits / self.worst_case_simple_rle_bits


def prefix_run_resource_report(generator_count: int, word_length: int) -> PrefixRunResourceReport:
    k = _positive("generator_count", generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    h = word_length
    phases = min(k, h)
    return PrefixRunResourceReport(
        generator_count=k,
        word_length=h,
        literal_words=literal_word_count_exact_length(k, h),
        prefix_semantic_classes=prefix_semantic_class_count(k, h),
        terminal_effects=terminal_effect_count_exact_length(k, h),
        total_information_lower_bound_bits=total_prefix_information_lower_bound_bits(k, h),
        materialized_trace_bits=full_materialized_prefix_trace_bits(k, h),
        maximum_phases=phases,
        worst_case_simple_rle_bits=simple_rle_storage_upper_bound_bits(k, h, phases),
        composition_phase_work_upper_bound=composition_phase_work_upper_bound(k),
    )
