"""Exact finite-state analyzers for the R005-A sieve quotient specialization.

This module contains no primality oracle and no generic automata novelty claim.
The Prime Toolkit facade validates the supplied prime set through canonical
owner code, while these helpers implement the exact R005-A arithmetic/finite-
state specialization accepted for targeted toolkit ingestion.
"""

from __future__ import annotations

from math import gcd, prod
from typing import Hashable, Iterable, Sequence

Observation = Hashable
LANGUAGES = {"relation_resolved", "union_support"}
ACTIVATIONS = {"actual", "steady"}


def normalize_distinct_set(values: Iterable[int]) -> tuple[int, ...]:
    primes = tuple(sorted(int(value) for value in values))
    if not primes:
        raise ValueError("prime set must be nonempty")
    if len(set(primes)) != len(primes):
        raise ValueError("prime set must contain distinct values")
    if primes[0] < 2:
        raise ValueError("prime set values must be >= 2")
    return primes


def period_q(primes: Sequence[int]) -> int:
    return prod(primes)


def relation_preperiod(primes: Sequence[int]) -> int:
    p_max = max(primes)
    return p_max * p_max - p_max + 1


def union_preperiod(primes: Sequence[int]) -> int:
    ghost_max = -1
    for p in primes:
        smaller_product = prod(q for q in primes if q < p)
        r_p = max(m for m in range(1, p) if gcd(m, smaller_product) == 1)
        ghost_max = max(ghost_max, p * r_p)
    return ghost_max + 1


def relation_observation(
    n: int, primes: Sequence[int], activation: str = "actual"
) -> tuple[int, ...]:
    if activation == "actual":
        return tuple(p for p in primes if n >= p * p and n % p == 0)
    if activation == "steady":
        return tuple(p for p in primes if n % p == 0)
    raise ValueError(f"unknown activation: {activation}")


def union_observation(n: int, primes: Sequence[int], activation: str = "actual") -> bool:
    if activation == "actual":
        return any(n >= p * p and n % p == 0 for p in primes)
    if activation == "steady":
        return any(n % p == 0 for p in primes)
    raise ValueError(f"unknown activation: {activation}")


def _observation(n: int, primes: Sequence[int], language: str, activation: str) -> Observation:
    if language == "relation_resolved":
        return relation_observation(n, primes, activation)
    if language == "union_support":
        return union_observation(n, primes, activation)
    raise ValueError(f"unknown sieve language: {language}")


def preperiod(primes: Sequence[int], language: str, activation: str) -> int:
    if activation == "steady":
        return 0
    if activation != "actual":
        raise ValueError(f"unknown activation: {activation}")
    if language == "relation_resolved":
        return relation_preperiod(primes)
    if language == "union_support":
        return union_preperiod(primes)
    raise ValueError(f"unknown sieve language: {language}")


def canonical_machine(
    primes: Sequence[int], language: str, activation: str
) -> tuple[list[Observation], list[int], int, int]:
    if language not in LANGUAGES:
        raise ValueError(f"unknown sieve language: {language}")
    if activation not in ACTIVATIONS:
        raise ValueError(f"unknown activation: {activation}")
    mu = preperiod(primes, language, activation)
    q = period_q(primes)
    state_count = mu + q
    observations = [_observation(i, primes, language, activation) for i in range(state_count)]
    next_state = list(range(1, state_count)) + [mu]
    return observations, next_state, mu, q


def _refine_once(
    observations: Sequence[Observation], next_state: Sequence[int], classes: Sequence[int]
) -> tuple[list[int], int]:
    ids: dict[tuple[Observation, int], int] = {}
    refined: list[int] = []
    for state, value in enumerate(observations):
        key = (value, classes[next_state[state]])
        refined.append(ids.setdefault(key, len(ids)))
    return refined, len(ids)


def finite_horizon_class_count(
    primes: Sequence[int], language: str, activation: str, horizon: int
) -> int:
    if horizon < 0:
        raise ValueError("horizon must be >= 0")
    observations, next_state, _, _ = canonical_machine(primes, language, activation)
    ids: dict[Observation, int] = {}
    classes = [ids.setdefault(value, len(ids)) for value in observations]
    if horizon == 0:
        return len(ids)
    count = len(ids)
    for _ in range(horizon):
        classes, count = _refine_once(observations, next_state, classes)
    return count


def direct_window_class_count(
    primes: Sequence[int], language: str, activation: str, horizon: int
) -> int:
    if horizon < 0:
        raise ValueError("horizon must be >= 0")
    observations, next_state, _, _ = canonical_machine(primes, language, activation)
    signatures = set()
    for start in range(len(observations)):
        state = start
        signature = []
        for _ in range(horizon + 1):
            signature.append(observations[state])
            state = next_state[state]
        signatures.add(tuple(signature))
    return len(signatures)


def stabilization_horizon(primes: Sequence[int], language: str, activation: str) -> int:
    observations, next_state, _, _ = canonical_machine(primes, language, activation)
    target = len(observations)
    ids: dict[Observation, int] = {}
    classes = [ids.setdefault(value, len(ids)) for value in observations]
    if len(ids) == target:
        return 0
    for horizon in range(1, target + 1):
        classes, count = _refine_once(observations, next_state, classes)
        if count == target:
            return horizon
    raise AssertionError("finite-state sieve machine failed to reach its residual quotient")


def segment_class_count(
    primes: Sequence[int],
    language: str,
    activation: str,
    segment_length: int,
    transitions: int,
) -> int:
    if segment_length <= 0:
        raise ValueError("segment_length must be > 0")
    if transitions < 0:
        raise ValueError("transitions must be >= 0")
    equivalent_horizon = (transitions + 1) * segment_length - 1
    return direct_window_class_count(primes, language, activation, equivalent_horizon)


def actual_transient_summary(primes: Sequence[int]) -> dict[str, object]:
    q = period_q(primes)
    mu_relation = relation_preperiod(primes)
    mu_union = union_preperiod(primes)
    return {
        "primes": list(primes),
        "period_Q": q,
        "p_max": max(primes),
        "relation_resolved": {
            "preperiod": mu_relation,
            "residual_state_count": q + mu_relation,
        },
        "union_support": {
            "preperiod": mu_union,
            "residual_state_count": q + mu_union,
        },
    }


def finite_horizon_summary(
    primes: Sequence[int],
    horizon: int,
    *,
    language: str,
    activation: str,
    segment_length: int | None = None,
    transitions: int | None = None,
    state_limit: int = 100_000,
) -> dict[str, object]:
    if horizon < 0:
        raise ValueError("horizon must be >= 0")
    mu = preperiod(primes, language, activation)
    q = period_q(primes)
    full_state_count = mu + q
    if full_state_count > state_limit:
        raise ValueError(
            f"exact finite-state analyzer requires {full_state_count} states; "
            f"state_limit={state_limit}"
        )
    class_count = finite_horizon_class_count(primes, language, activation, horizon)
    h_star = stabilization_horizon(primes, language, activation)
    value: dict[str, object] = {
        "primes": list(primes),
        "language": language,
        "activation": activation,
        "period_Q": q,
        "preperiod": mu,
        "horizon": horizon,
        "class_count": class_count,
        "full_residual_state_count": full_state_count,
        "stabilization_horizon": h_star,
        "is_full_quotient": class_count == full_state_count,
    }
    if language == "relation_resolved" and activation == "steady":
        value["relation_steady_recovery_formula"] = max(primes) - 2
    if (segment_length is None) != (transitions is None):
        raise ValueError("segment_length and transitions must be supplied together")
    if segment_length is not None and transitions is not None:
        if segment_length <= 0:
            raise ValueError("segment_length must be > 0")
        if transitions < 0:
            raise ValueError("transitions must be >= 0")
        equivalent_horizon = (transitions + 1) * segment_length - 1
        value["segment"] = {
            "segment_length": segment_length,
            "transitions": transitions,
            "equivalent_horizon": equivalent_horizon,
            "class_count": finite_horizon_class_count(
                primes, language, activation, equivalent_horizon
            ),
            "transition_depth_to_full": (h_star + segment_length) // segment_length - 1,
        }
    return value
