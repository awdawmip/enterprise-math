"""Finite causal counting weights derived from collapse multiplicity.

No probability measure is assumed. Fine states are explicit unit states. For a
finite collapse F:X->Y, the weight of a coarse event A is simply the number of
fine unit states whose image lies in A:

    mu_F(A) = |F^{-1}(A)|.

Postcomposition pushes these integer counts forward by addition. Conventional
finite probabilities can be rendered later as exact count pairs (n,N); no float
or true division is needed by the causal core.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, gcd
from typing import Hashable


State = Hashable


@dataclass(frozen=True)
class ExactCountRatio:
    """Exact nonnegative ratio stored without division."""

    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        if (
            isinstance(self.numerator, bool)
            or not isinstance(self.numerator, int)
            or self.numerator < 0
        ):
            raise ValueError("numerator must be a non-negative integer")
        if (
            isinstance(self.denominator, bool)
            or not isinstance(self.denominator, int)
            or self.denominator <= 0
        ):
            raise ValueError("denominator must be a positive integer")

    def reduced(self) -> "ExactCountRatio":
        divisor = gcd(self.numerator, self.denominator)
        return ExactCountRatio(
            self.numerator // divisor,
            self.denominator // divisor,
        )

    def compare(self, other: "ExactCountRatio") -> int:
        """Return -1, 0, 1 by fraction-free cross multiplication."""
        if not isinstance(other, ExactCountRatio):
            raise ValueError("other must be an ExactCountRatio")
        left = self.numerator * other.denominator
        right = other.numerator * self.denominator
        return -1 if left < right else (1 if left > right else 0)


def fiber_multiplicities(mapping: dict[State, State]) -> dict[State, int]:
    """Count fine unit states per reachable coarse state."""
    if not isinstance(mapping, dict):
        raise ValueError("mapping must be a dict")
    counts: dict[State, int] = {}
    for fine_state, coarse_state in mapping.items():
        try:
            hash(fine_state)
            hash(coarse_state)
        except TypeError as error:
            raise ValueError("states must be hashable") from error
        counts[coarse_state] = counts.get(coarse_state, 0) + 1
    return counts


def event_count(mapping: dict[State, State], coarse_event: frozenset[State]) -> int:
    """mu_F(A)=|F^{-1}(A)| for a finite coarse event A."""
    if not isinstance(coarse_event, frozenset):
        raise ValueError("coarse_event must be a frozenset")
    counts = fiber_multiplicities(mapping)
    return sum(counts.get(state, 0) for state in coarse_event)


def event_count_ratio(
    mapping: dict[State, State], coarse_event: frozenset[State]
) -> ExactCountRatio:
    """Exact normalized shadow `(mu_F(A), |X|)` without division."""
    if not mapping:
        raise ValueError("probability-style count ratio needs a non-empty fine state set")
    return ExactCountRatio(event_count(mapping, coarse_event), len(mapping))


def collision_count(mapping: dict[State, State], order: int) -> int:
    """Number J_k of k-subsets of fine histories collapsed to one coarse state."""
    if isinstance(order, bool) or not isinstance(order, int) or order <= 0:
        raise ValueError("order must be a positive integer")
    counts = fiber_multiplicities(mapping)
    return sum(comb(count, order) for count in counts.values() if count >= order)


def collision_count_ratio(
    mapping: dict[State, State], order: int
) -> ExactCountRatio:
    """Exact pair `(J_k, C(N,k))` for a uniform k-subset collision shadow.

    The returned object is still combinatorial. Calling it a probability needs
    the additional sampling convention that every k-subset of fine histories is
    given equal unit sampling weight.
    """
    if isinstance(order, bool) or not isinstance(order, int) or order <= 0:
        raise ValueError("order must be a positive integer")
    total = len(mapping)
    if order > total:
        raise ValueError("order cannot exceed the number of fine states")
    return ExactCountRatio(collision_count(mapping, order), comb(total, order))


def pushforward_multiplicities(
    fine_counts: dict[State, int],
    post_map: dict[State, State],
) -> dict[State, int]:
    """Push integer coarse weights through one deterministic postcomposition."""
    if not isinstance(fine_counts, dict) or not isinstance(post_map, dict):
        raise ValueError("fine_counts and post_map must be dicts")
    result: dict[State, int] = {}
    for state, count in fine_counts.items():
        if (
            isinstance(count, bool)
            or not isinstance(count, int)
            or count <= 0
        ):
            raise ValueError("multiplicities must be positive integers")
        if state not in post_map:
            raise ValueError("post_map must define every reachable intermediate state")
        target = post_map[state]
        result[target] = result.get(target, 0) + count
    return result


def compose_mapping(
    first: dict[State, State],
    second: dict[State, State],
) -> dict[State, State]:
    """Compose finite deterministic maps, requiring second on im(first)."""
    if not isinstance(first, dict) or not isinstance(second, dict):
        raise ValueError("maps must be dicts")
    result = {}
    for state, middle in first.items():
        if middle not in second:
            raise ValueError("second map must define every reachable middle state")
        result[state] = second[middle]
    return result


def conditional_count_ratio(
    fine_states: frozenset[State],
    event: frozenset[State],
    condition: frozenset[State],
) -> ExactCountRatio:
    """Exact finite conditional-count pair |A∩B| / |B| without division.

    This is a counting object only. A probabilistic interpretation requires an
    additional modeling choice that all fine states in the condition are sampled
    with equal unit weight.
    """
    if not all(isinstance(value, frozenset) for value in (fine_states, event, condition)):
        raise ValueError("fine_states, event, and condition must be frozensets")
    conditioned = fine_states & condition
    if not conditioned:
        raise ValueError("condition must contain at least one fine state")
    numerator = len(conditioned & event)
    return ExactCountRatio(numerator, len(conditioned))
