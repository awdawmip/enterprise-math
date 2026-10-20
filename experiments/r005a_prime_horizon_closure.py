from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd, prod
from typing import Callable, Hashable, Iterable, Sequence

from enterprise_math.prime_toolkit import PrimeToolResult, bounded_prime_enumeration

Observation = Hashable


def canonical_prime_prefix(limit: int) -> tuple[int, ...]:
    result = bounded_prime_enumeration(limit)
    if not isinstance(result, PrimeToolResult):
        raise AssertionError("prime toolkit did not return PrimeToolResult")
    if result.exactness != "exact":
        raise AssertionError("bounded prime enumeration must remain exact")
    if "CLASSICAL_BASELINE" not in result.source_status:
        raise AssertionError("prime enumeration provenance must remain classical baseline")
    return tuple(int(p) for p in result.value)


def relation_observation(n: int, primes: Sequence[int]) -> tuple[int, ...]:
    return tuple(p for p in primes if n >= p * p and n % p == 0)


def union_observation(n: int, primes: Sequence[int]) -> bool:
    return any(n >= p * p and n % p == 0 for p in primes)


def steady_relation_observation(n: int, primes: Sequence[int]) -> tuple[int, ...]:
    return tuple(p for p in primes if n % p == 0)


def steady_union_observation(n: int, primes: Sequence[int]) -> bool:
    return any(n % p == 0 for p in primes)


def relation_preperiod_formula(primes: Sequence[int]) -> int:
    p = max(primes)
    return p * p - p + 1


def union_preperiod_formula(primes: Sequence[int]) -> int:
    ghost_max = -1
    for p in primes:
        smaller_product = prod(q for q in primes if q < p)
        r = max(m for m in range(1, p) if gcd(m, smaller_product) == 1)
        ghost_max = max(ghost_max, p * r)
    return ghost_max + 1


def exact_preperiod_by_period_check(
    primes: Sequence[int], observation: Callable[[int, Sequence[int]], Observation]
) -> int:
    period = prod(primes)
    pmax = max(primes)
    last_mismatch = -1
    for n in range(pmax * pmax + period + 1):
        if observation(n, primes) != observation(n + period, primes):
            last_mismatch = n
    return last_mismatch + 1


def canonical_machine(
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    preperiod: int,
) -> tuple[list[Observation], list[int]]:
    period = prod(primes)
    state_count = preperiod + period
    obs = [observation(i, primes) for i in range(state_count)]
    nxt = list(range(1, state_count)) + [preperiod]
    return obs, nxt


def finite_horizon_class_counts(
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    preperiod: int,
    max_horizon: int,
) -> list[int]:
    obs, nxt = canonical_machine(primes, observation, preperiod)
    ids: dict[Observation, int] = {}
    classes = [ids.setdefault(value, len(ids)) for value in obs]
    counts = [len(ids)]
    for _ in range(max_horizon):
        ids2: dict[tuple[Observation, int], int] = {}
        new_classes = []
        for state, value in enumerate(obs):
            key = (value, classes[nxt[state]])
            new_classes.append(ids2.setdefault(key, len(ids2)))
        classes = new_classes
        counts.append(len(ids2))
    return counts


def stabilization_horizon(
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    preperiod: int,
) -> int:
    target = preperiod + prod(primes)
    obs, nxt = canonical_machine(primes, observation, preperiod)
    ids: dict[Observation, int] = {}
    classes = [ids.setdefault(value, len(ids)) for value in obs]
    if len(ids) == target:
        return 0
    for horizon in range(1, target + 1):
        ids2: dict[tuple[Observation, int], int] = {}
        new_classes = []
        for state, value in enumerate(obs):
            key = (value, classes[nxt[state]])
            new_classes.append(ids2.setdefault(key, len(ids2)))
        classes = new_classes
        if len(ids2) == target:
            return horizon
    raise AssertionError("canonical ultimately-periodic machine did not minimize")


def steady_stabilization_horizon(
    primes: Sequence[int], observation: Callable[[int, Sequence[int]], Observation]
) -> int:
    period = prod(primes)
    obs = [observation(i, primes) for i in range(period)]
    nxt = [(i + 1) % period for i in range(period)]
    ids: dict[Observation, int] = {}
    classes = [ids.setdefault(value, len(ids)) for value in obs]
    if len(ids) == period:
        return 0
    for horizon in range(1, period):
        ids2: dict[tuple[Observation, int], int] = {}
        new_classes = []
        for state, value in enumerate(obs):
            key = (value, classes[nxt[state]])
            new_classes.append(ids2.setdefault(key, len(ids2)))
        classes = new_classes
        if len(ids2) == period:
            return horizon
    raise AssertionError("steady word unexpectedly lacked least period Q")


def direct_window_class_count(
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    preperiod: int,
    horizon: int,
) -> int:
    period = prod(primes)
    return len(
        {
            tuple(observation(start + t, primes) for t in range(horizon + 1))
            for start in range(preperiod + period)
        }
    )


def segment_signature(
    start: int,
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    segment_length: int,
    transitions: int,
) -> tuple[tuple[Observation, ...], ...]:
    return tuple(
        tuple(
            observation(start + k * segment_length + j, primes)
            for j in range(segment_length)
        )
        for k in range(transitions + 1)
    )


def segment_class_count(
    primes: Sequence[int],
    observation: Callable[[int, Sequence[int]], Observation],
    preperiod: int,
    segment_length: int,
    transitions: int,
) -> int:
    period = prod(primes)
    return len(
        {
            segment_signature(start, primes, observation, segment_length, transitions)
            for start in range(preperiod + period)
        }
    )


@dataclass(frozen=True)
class PrattNormalized:
    n: int
    witness: int
    children: tuple[int, ...]
    valuations: tuple[tuple[int, int], ...]
    division_cost: int
    modular_exponentiation_cost: int


def _valuation_by_repeated_division(value: int, q: int) -> tuple[int, int]:
    exponent = 0
    while value % q == 0:
        value //= q
        exponent += 1
    return exponent, value


def normalize_pratt(n: int, witness: int, children: Iterable[int]) -> PrattNormalized:
    support = tuple(sorted(set(children)))
    residual = n - 1
    valuations: list[tuple[int, int]] = []
    divisions = 0
    for q in support:
        if residual % q != 0:
            raise ValueError("supplied child does not divide n-1")
        exponent, residual = _valuation_by_repeated_division(residual, q)
        divisions += exponent
        valuations.append((q, exponent))
    if residual != 1:
        raise ValueError("Pratt support does not fully cover n-1")
    return PrattNormalized(
        n=n,
        witness=witness % n,
        children=support,
        valuations=tuple(valuations),
        division_cost=divisions,
        modular_exponentiation_cost=1 + len(support),
    )


def verify_pratt_local(state: PrattNormalized) -> bool:
    n = state.n
    a = state.witness
    if pow(a, n - 1, n) != 1:
        return False
    return all(pow(a, (n - 1) // q, n) != 1 for q in state.children)


@dataclass(frozen=True)
class PocklingtonNormalized:
    n: int
    witnesses: tuple[tuple[int, int], ...]
    valuations: tuple[tuple[int, int], ...]
    factored_part: int
    division_cost: int


def normalize_pocklington(
    n: int, witnesses: Iterable[tuple[int, int]]
) -> PocklingtonNormalized:
    witness_map = dict(witnesses)
    support = tuple(sorted(witness_map))
    residual = n - 1
    valuations: list[tuple[int, int]] = []
    factored_part = 1
    divisions = 0
    for q in support:
        if residual % q != 0:
            raise ValueError("supplied child does not divide n-1")
        exponent, residual = _valuation_by_repeated_division(residual, q)
        divisions += exponent
        valuations.append((q, exponent))
        factored_part *= q**exponent
    return PocklingtonNormalized(
        n=n,
        witnesses=tuple((q, witness_map[q] % n) for q in support),
        valuations=tuple(valuations),
        factored_part=factored_part,
        division_cost=divisions,
    )


def verify_pocklington_local(state: PocklingtonNormalized) -> bool:
    n = state.n
    if state.factored_part * state.factored_part <= n:
        return False
    for q, a in state.witnesses:
        if pow(a, n - 1, n) != 1:
            return False
        if gcd(pow(a, (n - 1) // q, n) - 1, n) != 1:
            return False
    return True


@dataclass(frozen=True)
class ECPPToyRelation:
    n: int
    child_q: int
    curve_token: str | None
    point_token: str | None
    order_multiplier: int | None


def ecpp_toy_legality(state: ECPPToyRelation) -> bool:
    # Verifier-language toy only, not an ECPP implementation.
    return (
        state.curve_token is not None
        and state.point_token is not None
        and state.order_multiplier is not None
        and state.child_q > 1
    )


def run_regressions() -> None:
    primes = canonical_prime_prefix(11)
    assert primes == (2, 3, 5, 7, 11)

    # Exhaustive transient preperiod oracle on every nonempty subset.
    for r in range(1, len(primes) + 1):
        for subset in combinations(primes, r):
            assert exact_preperiod_by_period_check(
                subset, relation_observation
            ) == relation_preperiod_formula(subset)
            assert exact_preperiod_by_period_check(
                subset, union_observation
            ) == union_preperiod_formula(subset)

    # Prime-prefix Boolean transient is p_max+1, unlike relation-resolved.
    for k in range(1, len(primes) + 1):
        prefix = primes[:k]
        pmax = prefix[-1]
        assert union_preperiod_formula(prefix) == pmax + 1
        assert relation_preperiod_formula(prefix) == pmax * pmax - pmax + 1

    # Single-prime finite-horizon law C_p(H)=min(H+2,p^2+1).
    for p in primes:
        P = (p,)
        mu = relation_preperiod_formula(P)
        for H in range(0, p * p + 2):
            assert direct_window_class_count(P, relation_observation, mu, H) == min(
                H + 2, p * p + 1
            )
        assert stabilization_horizon(P, relation_observation, mu) == p * p - 1

    # Steady relation-resolved recovery is exactly p_max-2.
    for k in range(1, len(primes) + 1):
        prefix = primes[:k]
        assert steady_stabilization_horizon(
            prefix, steady_relation_observation
        ) == max(prefix) - 2

    # Boolean wheel phase-separation radius regressions.
    assert canonical_prime_prefix(13) == (2, 3, 5, 7, 11, 13)
    expected_union_steady = {
        (2, 3): 3,
        (2, 3, 5): 13,
        (2, 3, 5, 7): 37,
        (2, 3, 5, 7, 11): 65,
        (2, 3, 5, 7, 11, 13): 137,
    }
    for prefix, expected in expected_union_steady.items():
        assert steady_stabilization_horizon(
            prefix, steady_union_observation
        ) == expected

    # Partition-refinement recurrence equals direct exhaustive windows.
    P = (2, 3, 5, 7)
    for observation, mu in (
        (relation_observation, relation_preperiod_formula(P)),
        (union_observation, union_preperiod_formula(P)),
    ):
        counts = finite_horizon_class_counts(P, observation, mu, 40)
        for H in range(0, 41):
            assert counts[H] == direct_window_class_count(P, observation, mu, H)

    # Segment composition: D transitions of B-long observations equal one
    # contiguous horizon of (D+1)B symbols.
    mu = union_preperiod_formula(P)
    for B in (1, 2, 4, 8, 16):
        for D in range(0, 5):
            assert segment_class_count(P, union_observation, mu, B, D) == (
                direct_window_class_count(
                    P, union_observation, mu, (D + 1) * B - 1
                )
            )

    # Pratt verifier-profile normalization.
    p1 = normalize_pratt(97, 5, [3, 2, 2])
    p2 = normalize_pratt(97, 5, [2, 3])
    assert p1 == p2
    assert p1.valuations == ((2, 5), (3, 1))
    assert p1.division_cost == 6
    assert verify_pratt_local(p1)

    # Pocklington valuation serialization can be reconstructed under the profile.
    pock = normalize_pocklington(97, [(2, 5), (3, 2)])
    assert pock.valuations == ((2, 5), (3, 1))
    assert pock.factored_part == 96
    assert verify_pocklington_local(pock)

    # ECPP attack: child identity alone is not enough for parent-local group actions.
    full = ECPPToyRelation(101, 5, "curve-A", "point-P", 20)
    bare_child = ECPPToyRelation(101, 5, None, None, None)
    assert ecpp_toy_legality(full)
    assert not ecpp_toy_legality(bare_child)


if __name__ == "__main__":
    run_regressions()
    print("R005-A closure regressions passed")
