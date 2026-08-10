"""Joint witness-coupling certificates and safe marginal erasures.

A joint target family is represented as one weighted relation from coarse source state to
the product target.  Marginals are pushforwards along projections.  The joint coupling is
the canonical fallback whenever coupled future predicates remain live.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple

JointKey = Tuple[Hashable, ...]


def joint_weight_table(
    witnesses: Iterable[Hashable],
    coarse_fn: Callable[[Hashable], Hashable],
    target_fns: Sequence[Callable[[Hashable], Hashable]],
    weight_fn: Callable[[Hashable], int] = lambda _x: 1,
) -> Dict[Hashable, Dict[JointKey, int]]:
    """Natural-number joint witness-count tensor by coarse source state."""
    out: Dict[Hashable, Dict[JointKey, int]] = defaultdict(lambda: defaultdict(int))
    for x in witnesses:
        y = tuple(f(x) for f in target_fns)
        out[coarse_fn(x)][y] += int(weight_fn(x))
    return {a: dict(table) for a, table in out.items()}


def pushforward_table(table: Mapping[JointKey, int], mapping: Callable[[JointKey], Hashable]) -> Dict[Hashable, int]:
    out: Dict[Hashable, int] = defaultdict(int)
    for y, weight in table.items():
        out[mapping(y)] += int(weight)
    return dict(out)


def marginal_count_table(table: Mapping[JointKey, int], coordinate: int) -> Dict[Hashable, int]:
    return pushforward_table(table, lambda y: y[coordinate])


def support(table: Mapping[JointKey, int]) -> FrozenSet[JointKey]:
    return frozenset(y for y, weight in table.items() if weight != 0)


def marginal_supports(joint_support: Iterable[JointKey]) -> Tuple[FrozenSet[Hashable], ...]:
    J = tuple(joint_support)
    if not J:
        return tuple()
    m = len(J[0])
    return tuple(frozenset(y[i] for y in J) for i in range(m))


def rectangular_hull(joint_support: Iterable[JointKey]) -> FrozenSet[JointKey]:
    marginals = marginal_supports(joint_support)
    if not marginals:
        return frozenset()
    return frozenset(product(*[tuple(S) for S in marginals]))


def coupling_obstruction(joint_support: Iterable[JointKey]) -> FrozenSet[JointKey]:
    J = frozenset(joint_support)
    return rectangular_hull(J) - J


def marginal_supports_uniquely_determine_joint(joint_support: Iterable[JointKey]) -> bool:
    """Exact Boolean criterion: at most one non-singleton marginal support."""
    marginals = marginal_supports(joint_support)
    return sum(len(S) > 1 for S in marginals) <= 1


def coupled_predicate_count(table: Mapping[JointKey, int], predicate: Callable[[JointKey], bool]) -> int:
    return sum(int(weight) for y, weight in table.items() if predicate(y))


def pushforward_functorial(
    table: Mapping[JointKey, int],
    first: Callable[[JointKey], Hashable],
    second: Callable[[Hashable], Hashable],
) -> bool:
    first_table = pushforward_table(table, first)
    lhs: Dict[Hashable, int] = defaultdict(int)
    for z, weight in first_table.items():
        lhs[second(z)] += weight
    rhs = pushforward_table(table, lambda y: second(first(y)))
    return dict(lhs) == rhs
