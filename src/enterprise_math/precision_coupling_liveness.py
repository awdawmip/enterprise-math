"""Typed liveness gates for demoting joint witness coupling to marginals."""

from __future__ import annotations

from itertools import product
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple

JointKey = Tuple[Hashable, ...]


def may_query_from_marginals(marginals: Sequence[FrozenSet[Hashable]], predicate: FrozenSet[JointKey]):
    """Return forced MAY answer from marginal supports, or None if coupling-sensitive."""
    if not marginals:
        return False
    universe = frozenset(product(*[tuple(S) for S in marginals]))
    P = universe.intersection(predicate)
    if not P:
        return False
    complement = universe - P
    for i, S in enumerate(marginals):
        projected = frozenset(y[i] for y in complement)
        if projected != S:
            return True
    return None


def additive_potential(coefficients: Mapping[JointKey, int], shape: Sequence[int]):
    """Return integer alpha,f_i if c(y)=alpha+sum f_i(y_i), else None."""
    base = tuple(0 for _ in shape)
    alpha = int(coefficients[base])
    fs = []
    for i, n in enumerate(shape):
        values = []
        for v in range(n):
            y = list(base)
            y[i] = v
            values.append(int(coefficients[tuple(y)]) - alpha)
        fs.append(tuple(values))
    for y in product(*[range(n) for n in shape]):
        if int(coefficients[y]) != alpha + sum(fs[i][y[i]] for i in range(len(shape))):
            return None
    return alpha, tuple(fs)


def count_query_from_marginals(
    coefficients: Mapping[JointKey, int],
    marginals: Sequence[Sequence[int]],
):
    shape = tuple(len(m) for m in marginals)
    potential = additive_potential(coefficients, shape)
    if potential is None:
        return None
    alpha, fs = potential
    total = sum(int(v) for v in marginals[0]) if marginals else 0
    return alpha * total + sum(
        fs[i][v] * int(marginals[i][v])
        for i in range(len(shape))
        for v in range(shape[i])
    )


def boolean_predicate_is_single_coordinate(predicate: FrozenSet[JointKey], shape: Sequence[int]) -> bool:
    coeffs = {y: int(y in predicate) for y in product(*[range(n) for n in shape])}
    potential = additive_potential(coeffs, shape)
    if potential is None:
        return False
    # For Boolean-valued additive tensors, at most one coordinate potential can vary.
    _, fs = potential
    return sum(len(set(f)) > 1 for f in fs) <= 1


def full_joint_count_coupling_dimension(shape: Sequence[int]) -> int:
    if not shape or any(n < 1 for n in shape):
        raise ValueError("shape entries must be positive")
    cells = 1
    for n in shape:
        cells *= n
    marginal_rank = sum(shape) - (len(shape) - 1)
    return cells - marginal_rank


def full_joint_count_padic_profile(shape: Sequence[int], K: int) -> Tuple[int, ...]:
    if K < 1:
        raise ValueError("K must be positive")
    return (K,) * full_joint_count_coupling_dimension(shape)


def label_union_query_from_marginals(
    label_joint_supports: Mapping[Hashable, FrozenSet[JointKey]],
    label_marginals: Mapping[Hashable, Sequence[FrozenSet[Hashable]]],
    predicate: FrozenSet[JointKey],
):
    """Return exact forced label union if every label's MAY query is marginal-determined."""
    present = set()
    for label, marginals in label_marginals.items():
        answer = may_query_from_marginals(marginals, predicate)
        if answer is None:
            return None
        if answer:
            present.add(label)
    return frozenset(present)
