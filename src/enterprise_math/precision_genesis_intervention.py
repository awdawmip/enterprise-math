"""Finite response-table completion for R004 generative-identifiability tests.

For a finite family of rational stochastic response kernels, every possible
context can be assigned a response in advance using one finite uniform master
seed.  An adaptive policy may choose which context is visited from earlier
observations; the unused counterfactual entries remain latent, while every
visited conditional distribution is reproduced exactly.

This is a finite rational specialization of established functional
representation / structural-causal randomization ideas.  R004 uses it as a
negative boundary: finite interventions plus classical rational stochastic
kernels do not by themselves prove that randomness or distinguishability was
created online.
"""
from __future__ import annotations

from collections.abc import Sequence
from fractions import Fraction
from itertools import product
from math import lcm


def _probability_row(row: Sequence[Fraction]) -> tuple[Fraction, ...]:
    probabilities = tuple(row)
    if not probabilities:
        raise ValueError("probability row must be nonempty")
    if any(not isinstance(probability, Fraction) or probability < 0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative Fractions")
    if sum(probabilities, Fraction(0, 1)) != 1:
        raise ValueError("probability row must sum exactly to one")
    return probabilities


def local_uniform_response_table(row: Sequence[Fraction]) -> tuple[int, ...]:
    """Expand one rational distribution into a finite uniform outcome table."""
    probabilities = _probability_row(row)
    denominator = 1
    for probability in probabilities:
        denominator = lcm(denominator, probability.denominator)
    return tuple(
        outcome
        for outcome, probability in enumerate(probabilities)
        for _ in range(probability.numerator * (denominator // probability.denominator))
    )


def master_response_seeds(
    kernels: Sequence[Sequence[Fraction]],
) -> tuple[tuple[int, ...], ...]:
    """Return the finite uniform counterfactual response-table seed space.

    Entry ``seed[c]`` is the pre-sampled outcome for context ``c``.  Duplicate
    tuples are retained as distinct uniform seed atoms whenever denominator
    multiplicity requires them.
    """
    local_tables = tuple(local_uniform_response_table(row) for row in kernels)
    if not local_tables:
        raise ValueError("at least one context kernel is required")
    return tuple(product(*local_tables))


def marginal_counts(
    seeds: Sequence[tuple[int, ...]], context: int
) -> tuple[int, ...]:
    """Count uniform seed atoms by the pre-sampled outcome at one context."""
    if not seeds:
        raise ValueError("seed space must be nonempty")
    if isinstance(context, bool) or not isinstance(context, int) or context < 0:
        raise ValueError("context must be a non-negative integer")
    if context >= len(seeds[0]):
        raise ValueError("unknown context")
    if any(len(seed) != len(seeds[0]) for seed in seeds):
        raise ValueError("seed rows must have common context width")
    max_outcome = max(seed[context] for seed in seeds)
    return tuple(
        sum(seed[context] == outcome for seed in seeds)
        for outcome in range(max_outcome + 1)
    )


def adaptive_two_step_counts(
    seeds: Sequence[tuple[int, ...]],
    first_context: int,
    next_context_by_first_outcome: Sequence[int],
) -> dict[tuple[int, int], int]:
    """Evaluate one adaptive two-step policy on the pre-sampled master table."""
    if not seeds:
        raise ValueError("seed space must be nonempty")
    width = len(seeds[0])
    if isinstance(first_context, bool) or not isinstance(first_context, int) or not 0 <= first_context < width:
        raise ValueError("unknown first context")
    next_context = tuple(next_context_by_first_outcome)
    if not next_context:
        raise ValueError("adaptive policy must provide at least one next context")
    if any(
        isinstance(context, bool)
        or not isinstance(context, int)
        or not 0 <= context < width
        for context in next_context
    ):
        raise ValueError("unknown adaptive context")

    counts: dict[tuple[int, int], int] = {}
    for seed in seeds:
        first = seed[first_context]
        if first >= len(next_context):
            raise ValueError("policy lacks a context for a reachable first outcome")
        second = seed[next_context[first]]
        counts[(first, second)] = counts.get((first, second), 0) + 1
    return counts
