"""Bit-level work/depth accounting for the idempotent-mask normal form.

A length-H word over k commuting idempotent generators normalizes by OR-reducing
H one-hot k-bit masks.  A balanced tree uses H-1 word-level OR gates; treating a
k-bit OR as k independent bit operations gives

    normalization bit work = k*(H-1),
    normalization depth = ceil(log2 H).

Applying the resulting effect mask to one k-bit state costs one more word-level
OR, i.e. k bit operations at depth1.  Total bit work is therefore k*H and total
depth ceil(log2 H)+1 for nonempty words.

This makes explicit what the formulaic representation buys: it replaces an
exponential Cayley/action table by a small circuit schema, at the price of
runtime work that remains linear in word length while parallel depth is
logarithmic.
"""

from __future__ import annotations

from dataclasses import dataclass

from .semantic_word_normalizer import parallel_normalization_depth


@dataclass(frozen=True)
class FormulaicWorkDepthReport:
    generator_count: int
    word_length: int
    normalization_word_or_gates: int
    normalization_bit_work: int
    normalization_depth: int
    state_apply_bit_work: int
    total_bit_work: int
    total_depth: int


def formulaic_or_work_depth(generator_count: int, word_length: int) -> FormulaicWorkDepthReport:
    if isinstance(generator_count, bool) or not isinstance(generator_count, int) or generator_count < 1:
        raise ValueError("generator_count must be positive")
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 1:
        raise ValueError("word_length must be positive")
    gates = word_length - 1
    normalization_work = generator_count * gates
    apply_work = generator_count
    depth = parallel_normalization_depth(word_length)
    return FormulaicWorkDepthReport(
        generator_count=generator_count,
        word_length=word_length,
        normalization_word_or_gates=gates,
        normalization_bit_work=normalization_work,
        normalization_depth=depth,
        state_apply_bit_work=apply_work,
        total_bit_work=normalization_work + apply_work,
        total_depth=depth + 1,
    )
