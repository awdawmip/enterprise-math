"""Exact storage/inference-depth presentations for a unary implication chain.

Consider the closure law

    x_0 -> x_1 -> ... -> x_n.

A translation-invariant jump presentation chooses lengths

    L subseteq {1,...,n}, 1 in L,

and stores every valid implication

    x_i -> x_(i+ell)

for each ell in L and i+ell<=n.

The exact storage is

    S_n(L) = sum_(ell in L) (n-ell+1).

Starting from x_0, the earliest round at which x_t can be derived is the minimum
number of jump lengths whose sum is t.  Thus if ``lambda_L(t)`` is the ordinary
unbounded coin-count function, the full synchronous closure depth is

    D_n(L) = max_(1<=t<=n) lambda_L(t).

This unifies:

* adjacent/Hasse basis L={1}: n rules, n rounds;
* full transitive table L={1,...,n}: n(n+1)/2 rules, one round;
* power-of-two jumps: O(n log n) rules, O(log n) rounds;
* geometric/radix jump families and arbitrary additive bases.

The storage weight ``n-ell+1`` makes long jump denominations cheaper because
there are fewer source positions on which they can occur.  Therefore binary
powers are a useful exact construction but are not generically Pareto-optimal.
The finite optimum is a weighted additive-basis/coin-system problem.

Implication closure, transitive reduction/closure, coin systems and shortcut
spanners are standard prior mathematics/CS.  The project value is the explicit
Stage131 semantic-basis versus execution-presentation resource law.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import log
from typing import Iterable, Sequence


Rule = tuple[int, int]


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def normalize_jump_lengths(chain_length: int, jump_lengths: Iterable[int]) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    lengths = tuple(sorted(set(jump_lengths)))
    if not lengths:
        raise ValueError("jump_lengths must be nonempty")
    if any(isinstance(length, bool) or not isinstance(length, int) for length in lengths):
        raise TypeError("jump lengths must be integers")
    if any(length <= 0 or length > n for length in lengths):
        raise ValueError("jump lengths must lie in 1..chain_length")
    if 1 not in lengths:
        raise ValueError("a complete chain presentation must include jump length1")
    return lengths


def chain_jump_rules(chain_length: int, jump_lengths: Iterable[int]) -> tuple[Rule, ...]:
    n = _positive_int(chain_length, name="chain_length")
    lengths = normalize_jump_lengths(n, jump_lengths)
    return tuple(
        (source, source + length)
        for length in lengths
        for source in range(0, n - length + 1)
    )


def chain_jump_rule_count(chain_length: int, jump_lengths: Iterable[int]) -> int:
    n = _positive_int(chain_length, name="chain_length")
    lengths = normalize_jump_lengths(n, jump_lengths)
    return sum(n - length + 1 for length in lengths)


def minimum_jump_rounds_by_distance(
    chain_length: int,
    jump_lengths: Iterable[int],
) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    lengths = normalize_jump_lengths(n, jump_lengths)
    best = [0] + [n + 1] * n
    for distance in range(1, n + 1):
        best[distance] = 1 + min(
            best[distance - length]
            for length in lengths
            if length <= distance
        )
    return tuple(best)


def chain_jump_closure_rounds(chain_length: int, jump_lengths: Iterable[int]) -> int:
    rounds = minimum_jump_rounds_by_distance(chain_length, jump_lengths)
    return max(rounds[1:])


def synchronous_chain_closure_sequence(
    chain_length: int,
    jump_lengths: Iterable[int],
) -> tuple[frozenset[int], ...]:
    """Known chain indices after each synchronous forward-chaining round."""
    n = _positive_int(chain_length, name="chain_length")
    rules = chain_jump_rules(n, jump_lengths)
    known = frozenset({0})
    stages = [known]
    while len(known) < n + 1:
        nxt = frozenset(
            set(known)
            | {
                target
                for source, target in rules
                if source in known
            }
        )
        if nxt == known:
            raise AssertionError("complete chain jump presentation failed to reach all states")
        stages.append(nxt)
        known = nxt
        if len(stages) - 1 > n:
            raise AssertionError("chain closure exceeded adjacent-basis depth bound")
    return tuple(stages)


def closure_sequence_matches_coin_rounds(
    chain_length: int,
    jump_lengths: Iterable[int],
) -> bool:
    n = _positive_int(chain_length, name="chain_length")
    rounds = minimum_jump_rounds_by_distance(n, jump_lengths)
    stages = synchronous_chain_closure_sequence(n, jump_lengths)
    for state in range(n + 1):
        first = next(index for index, known in enumerate(stages) if state in known)
        if first != rounds[state]:
            raise AssertionError("synchronous chain derivation disagreed with coin-count distance")
    return True


def adjacent_jump_lengths(chain_length: int) -> tuple[int, ...]:
    _positive_int(chain_length, name="chain_length")
    return (1,)


def full_transitive_jump_lengths(chain_length: int) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    return tuple(range(1, n + 1))


def binary_jump_lengths(chain_length: int) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    return tuple(1 << bit for bit in range(n.bit_length()) if (1 << bit) <= n)


def geometric_jump_lengths(chain_length: int, base: int) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    b = _positive_int(base, name="base")
    if b < 2:
        raise ValueError("geometric base must be at least two")
    values = []
    power = 1
    while power <= n:
        values.append(power)
        power *= b
    return tuple(values)


def binary_jump_rule_count_closed(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    m = n.bit_length() - 1
    # Sum_{d=1}^n bit_length(d).
    return (m + 1) * (n + 1) + 1 - (1 << (m + 1))


def binary_chain_closure_rounds_closed(chain_length: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    return (n + 1).bit_length() - 1


def geometric_jump_rule_count_closed(chain_length: int, base: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    lengths = geometric_jump_lengths(n, base)
    return len(lengths) * (n + 1) - sum(lengths)


def two_jump_lengths(chain_length: int, long_jump: int) -> tuple[int, ...]:
    n = _positive_int(chain_length, name="chain_length")
    q = _positive_int(long_jump, name="long_jump")
    if q < 2 or q > n:
        raise ValueError("long_jump must lie in 2..chain_length")
    return (1, q)


def two_jump_closure_rounds_closed(chain_length: int, long_jump: int) -> int:
    n = _positive_int(chain_length, name="chain_length")
    q = _positive_int(long_jump, name="long_jump")
    if q < 2 or q > n:
        raise ValueError("long_jump must lie in 2..chain_length")
    quotient, remainder = divmod(n, q)
    return quotient + max(q - 2, remainder)


@dataclass(frozen=True)
class ChainPresentationPoint:
    chain_length: int
    jump_lengths: tuple[int, ...]
    stored_rules: int
    full_closure_rounds: int

    @property
    def jump_type_count(self) -> int:
        return len(self.jump_lengths)


def chain_presentation_point(
    chain_length: int,
    jump_lengths: Iterable[int],
) -> ChainPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    lengths = normalize_jump_lengths(n, jump_lengths)
    return ChainPresentationPoint(
        chain_length=n,
        jump_lengths=lengths,
        stored_rules=chain_jump_rule_count(n, lengths),
        full_closure_rounds=chain_jump_closure_rounds(n, lengths),
    )


def canonical_chain_presentation_points(chain_length: int) -> dict[str, ChainPresentationPoint]:
    n = _positive_int(chain_length, name="chain_length")
    return {
        "adjacent": chain_presentation_point(n, adjacent_jump_lengths(n)),
        "binary": chain_presentation_point(n, binary_jump_lengths(n)),
        "full": chain_presentation_point(n, full_transitive_jump_lengths(n)),
    }


def point_dominates(left: ChainPresentationPoint, right: ChainPresentationPoint) -> bool:
    if left.chain_length != right.chain_length:
        raise ValueError("presentation points must belong to the same chain")
    return (
        left.stored_rules <= right.stored_rules
        and left.full_closure_rounds <= right.full_closure_rounds
        and (
            left.stored_rules < right.stored_rules
            or left.full_closure_rounds < right.full_closure_rounds
        )
    )


def enumerate_chain_jump_presentations(chain_length: int) -> tuple[ChainPresentationPoint, ...]:
    n = _positive_int(chain_length, name="chain_length")
    if n > 20:
        raise ValueError("exhaustive jump-set enumeration is limited to chain_length<=20")
    optional = tuple(range(2, n + 1))
    points = []
    for count in range(len(optional) + 1):
        for chosen in combinations(optional, count):
            points.append(chain_presentation_point(n, (1, *chosen)))
    return tuple(points)


def exact_chain_jump_pareto_frontier(chain_length: int) -> tuple[ChainPresentationPoint, ...]:
    points = enumerate_chain_jump_presentations(chain_length)
    return tuple(
        sorted(
            (
                point
                for point in points
                if not any(
                    point_dominates(other, point)
                    for other in points
                    if other != point
                )
            ),
            key=lambda point: (
                point.stored_rules,
                point.full_closure_rounds,
                point.jump_lengths,
            ),
        )
    )


def best_two_jump_presentation(chain_length: int) -> ChainPresentationPoint:
    n = _positive_int(chain_length, name="chain_length")
    if n == 1:
        return chain_presentation_point(n, (1,))
    candidates = tuple(
        chain_presentation_point(n, (1, jump))
        for jump in range(2, n + 1)
    )
    # First minimize closure depth, then storage.
    return min(
        candidates,
        key=lambda point: (point.full_closure_rounds, point.stored_rules),
    )
