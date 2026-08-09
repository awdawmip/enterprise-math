"""Future-minimal state count for a finite cyclic material force word.

An internal material oscillator may expose n clock phases, but a declared future
force observable need not distinguish all n phases.  Let

    w = (w_0,...,w_{n-1})

be the force/output samples attached to the cyclic transition ``i -> i+1 mod n``.
Two phase states are future-equivalent exactly when every future clock step emits
the same output, i.e. when their infinite periodic output words agree.

For a finite cyclic word this quotient has a closed form: the stable class count
is the primitive period ``t`` of w, the least positive divisor of n satisfying

    w_i = w_{i+t mod n}  for every i.

Thus an n-phase internal clock is only *capacity*.  The declared material output
can collapse it to t future-relevant phase classes.  A constant word needs one
state; a primitive word needs all n.

This is an E001 specialization of the canonical P023 future-compatible quotient.
The generic minimization theorem remains A2/P023-owned.  This module supplies the
closed cyclic-word formula and cross-checks it against ``stable_family_partition``.
"""

from __future__ import annotations

from dataclasses import dataclass

from .operation_quotient import class_count, stable_family_partition


def _word(samples: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    word = tuple(samples)
    if not word:
        raise ValueError("cyclic material word must be nonempty")
    for sample in word:
        if isinstance(sample, bool) or not isinstance(sample, int):
            raise ValueError("material word samples must be integers")
    return word


def divisors(n: int) -> tuple[int, ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def cyclic_word_primitive_period(samples: tuple[int, ...] | list[int]) -> int:
    """Return the least period dividing the finite cyclic material word length."""
    word = _word(samples)
    n = len(word)
    for period in divisors(n):
        if all(word[i] == word[(i + period) % n] for i in range(n)):
            return period
    raise AssertionError("word length itself must be a valid period")


@dataclass(frozen=True)
class CyclicMaterialPhaseQuotient:
    samples: tuple[int, ...]
    clock_phase_count: int
    primitive_output_period: int
    stable_future_class_count: int
    stable_partition: tuple[int, ...]
    compression_factor_numerator: int
    compression_factor_denominator: int


def cyclic_material_phase_quotient(
    samples: tuple[int, ...] | list[int],
) -> CyclicMaterialPhaseQuotient:
    """Compute the closed-form and P023 future quotient for one cyclic force word."""
    word = _word(samples)
    n = len(word)
    period = cyclic_word_primitive_period(word)
    domain = tuple(range(n))
    step = {phase: (phase + 1) % n for phase in domain}
    observation = {phase: word[phase] for phase in domain}
    stable = stable_family_partition(domain, {"STEP": step}, observation)
    count = class_count(stable)
    if count != period:
        raise AssertionError("P023 cyclic phase quotient disagrees with primitive word period")

    # Canonicalize by first occurrence so the tuple is deterministic even if the
    # mother implementation changes its internal class labels.
    labels: dict[int, int] = {}
    canonical: list[int] = []
    for phase in domain:
        raw = stable[phase]
        if raw not in labels:
            labels[raw] = len(labels)
        canonical.append(labels[raw])
    if any(canonical[i] != canonical[i % period] for i in domain):
        raise AssertionError("stable cyclic partition does not repeat with primitive period")
    return CyclicMaterialPhaseQuotient(
        samples=word,
        clock_phase_count=n,
        primitive_output_period=period,
        stable_future_class_count=count,
        stable_partition=tuple(canonical),
        compression_factor_numerator=n,
        compression_factor_denominator=period,
    )
