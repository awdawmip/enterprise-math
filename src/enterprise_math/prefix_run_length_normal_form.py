"""Run-length exact normal form for prefix-observable commuting-idempotent words.

The full prefix trace of a word is a monotone sequence of cumulative OR masks.
Although trace length is the word length H, the mask can change at most k times
because each of the k generators is introduced at most once.

Compress the trace to phases

    ((g_1,r_1),...,(g_s,r_s)),

where g_i are distinct generators in first-appearance order, r_i>0 is the number
of consecutive prefix positions for which the cumulative mask remains at the
level reached after introducing g_i, and sum r_i=H.

This normal form is exact for full prefix-state observation:

* decoding reconstructs the cumulative-mask trace;
* a canonical representative word repeats each newly introduced generator for
  its phase duration;
* normalizing that representative returns the same phase form.

Composition is formulaic.  Start with the left phases and their seen-generator
set.  Scan right phases in order.  If right generator g was already seen on the
left, its entire duration causes no new cumulative mask and is added to the
current final phase.  Otherwise append a new phase (g,r).  This exactly matches
word concatenation and makes the prefix-run forms a monoid with the empty form as
identity.

For k=1 the monoid reduces to nonnegative word length under addition: all
nonempty words have the same terminal effect but retain their duration.

The form also explains the exact prefix-trace count.  With s phases, choose an
ordered s-tuple of distinct generators and a positive composition of H into s
parts, giving

    P(k,s) * C(H-1,s-1)

forms.

Run-length encoding, ordered set partitions/compositions and idempotent word
reductions are standard prior mathematics/CS.  The project value is the exact
finite-parameter presentation of an infinite prefix-observable operation law.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial
from typing import Sequence

from .prefix_observable_or_word_semantics import (
    prefix_mask_trace,
    prefix_trace_count_exact_length,
)


@dataclass(frozen=True)
class PrefixRun:
    generator: int
    run_length: int


PrefixRunNormalForm = tuple[PrefixRun, ...]


def _generator_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("generator_count must be a positive integer")
    return value


def _validate_form(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> PrefixRunNormalForm:
    k = _generator_count(generator_count)
    phases = tuple(form)
    seen = set()
    for phase in phases:
        if not isinstance(phase, PrefixRun):
            raise TypeError("prefix form entries must be PrefixRun values")
        generator = phase.generator
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("phase generator outside declared range")
        if generator in seen:
            raise ValueError("phase generators must be distinct first appearances")
        seen.add(generator)
        if isinstance(phase.run_length, bool) or not isinstance(phase.run_length, int) or phase.run_length < 1:
            raise ValueError("phase run length must be a positive integer")
    return phases


def normalize_prefix_word_to_runs(
    word: Sequence[int],
    generator_count: int,
) -> PrefixRunNormalForm:
    k = _generator_count(generator_count)
    seen = set()
    phases: list[PrefixRun] = []
    for generator in word:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("word contains generator outside declared range")
        if generator not in seen:
            seen.add(generator)
            phases.append(PrefixRun(generator=generator, run_length=1))
        else:
            if not phases:
                raise AssertionError("seen generator without active phase")
            last = phases[-1]
            phases[-1] = PrefixRun(
                generator=last.generator,
                run_length=last.run_length + 1,
            )
    return tuple(phases)


def prefix_run_word_length(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> int:
    phases = _validate_form(form, generator_count)
    return sum(phase.run_length for phase in phases)


def prefix_run_phase_count(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> int:
    return len(_validate_form(form, generator_count))


def decode_prefix_runs_to_trace(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> tuple[int, ...]:
    phases = _validate_form(form, generator_count)
    current = 0
    trace = []
    for phase in phases:
        current |= 1 << phase.generator
        trace.extend(current for _ in range(phase.run_length))
    return tuple(trace)


def canonical_word_from_prefix_runs(
    form: Sequence[PrefixRun],
    generator_count: int,
) -> tuple[int, ...]:
    phases = _validate_form(form, generator_count)
    return tuple(
        generator
        for phase in phases
        for generator in (phase.generator,) * phase.run_length
    )


def prefix_run_normal_form_matches_word(
    word: Sequence[int],
    generator_count: int,
) -> bool:
    form = normalize_prefix_word_to_runs(word, generator_count)
    decoded = decode_prefix_runs_to_trace(form, generator_count)
    direct = prefix_mask_trace(word, generator_count)
    if decoded != direct:
        raise AssertionError("prefix run normal form failed exact trace decoding")
    canonical = canonical_word_from_prefix_runs(form, generator_count)
    if normalize_prefix_word_to_runs(canonical, generator_count) != form:
        raise AssertionError("canonical prefix-run representative failed normalization round-trip")
    return True


def compose_prefix_run_forms(
    left: Sequence[PrefixRun],
    right: Sequence[PrefixRun],
    generator_count: int,
) -> PrefixRunNormalForm:
    k = _generator_count(generator_count)
    left_form = _validate_form(left, k)
    right_form = _validate_form(right, k)
    result = list(left_form)
    seen = {phase.generator for phase in left_form}

    for phase in right_form:
        if phase.generator in seen:
            if not result:
                raise AssertionError("overlapping right phase without active left result")
            last = result[-1]
            result[-1] = PrefixRun(
                generator=last.generator,
                run_length=last.run_length + phase.run_length,
            )
        else:
            seen.add(phase.generator)
            result.append(phase)
    return tuple(result)


def prefix_run_composition_matches_words(
    left_word: Sequence[int],
    right_word: Sequence[int],
    generator_count: int,
) -> bool:
    left = normalize_prefix_word_to_runs(left_word, generator_count)
    right = normalize_prefix_word_to_runs(right_word, generator_count)
    composed = compose_prefix_run_forms(left, right, generator_count)
    direct = normalize_prefix_word_to_runs(
        (*tuple(left_word), *tuple(right_word)),
        generator_count,
    )
    if composed != direct:
        raise AssertionError("prefix run composition disagreed with word concatenation")
    return True


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def prefix_run_form_count_with_phases(
    generator_count: int,
    word_length: int,
    phase_count: int,
) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if isinstance(phase_count, bool) or not isinstance(phase_count, int) or phase_count < 0:
        raise ValueError("phase_count must be nonnegative")
    if word_length == 0:
        return int(phase_count == 0)
    if not 1 <= phase_count <= min(k, word_length):
        return 0
    return (
        falling_factorial(k, phase_count)
        * comb(word_length - 1, phase_count - 1)
    )


def prefix_run_form_count_exact_length(
    generator_count: int,
    word_length: int,
) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    total = sum(
        prefix_run_form_count_with_phases(k, word_length, phases)
        for phases in range(1, min(k, word_length) + 1)
    )
    expected = prefix_trace_count_exact_length(k, word_length)
    if total != expected:
        raise AssertionError("prefix run count disagreed with prefix trace theorem")
    return total
