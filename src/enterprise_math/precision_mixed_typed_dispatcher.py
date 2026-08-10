"""R004 mixed typed future-language dispatcher (finite, exact, fraction-free).

This module consumes already-compiled unary operation contexts. Generic finitary-to-unary
context compilation belongs upstream to A2/P023.

Typed obligations supported here:
- total unary contexts;
- partial unary contexts, with legality as part of semantics;
- quotient-relative relation channels aggregated in a declared commutative monoid.

Optional semiring helpers certify exact descent of relation composition after block-sum
stability has been established.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional, Sequence, Tuple

Partition = Tuple[int, ...]
TotalUnary = Tuple[int, ...]
PartialUnary = Tuple[Optional[int], ...]


def normalize_partition(labels: Sequence[Any]) -> Partition:
    mapping = {}
    out = []
    for label in labels:
        if label not in mapping:
            mapping[label] = len(mapping)
        out.append(mapping[label])
    return tuple(out)


def partition_blocks(partition: Sequence[Any]) -> Tuple[Tuple[int, ...], ...]:
    p = normalize_partition(partition)
    if not p:
        return ()
    blocks = [[] for _ in range(max(p) + 1)]
    for state, block in enumerate(p):
        blocks[block].append(state)
    return tuple(tuple(block) for block in blocks)


def block_count(partition: Sequence[Any]) -> int:
    return len(partition_blocks(partition))


def raw_common_refinement(*partitions: Sequence[Any]) -> Partition:
    if not partitions:
        return ()
    n = len(partitions[0])
    if any(len(p) != n for p in partitions):
        raise ValueError("all partitions must have the same carrier size")
    normalized = [normalize_partition(p) for p in partitions]
    return normalize_partition(tuple(tuple(p[x] for p in normalized) for x in range(n)))


@dataclass(frozen=True)
class RelationChannel:
    name: str
    weights: Tuple[Tuple[Any, ...], ...]
    zero: Any
    combine: Callable[[Any, Any], Any]


@dataclass(frozen=True)
class Semiring:
    zero: Any
    one: Any
    add: Callable[[Any, Any], Any]
    mul: Callable[[Any, Any], Any]


@dataclass(frozen=True)
class MixedCompileResult:
    partition: Partition
    history: Tuple[Partition, ...]
    descended_total_unary: Tuple[Tuple[int, ...], ...]
    descended_partial_unary: Tuple[Tuple[Optional[int], ...], ...]
    descended_relation_rows: Tuple[Tuple[Tuple[Any, ...], ...], ...]


def _aggregate(values, zero, combine):
    acc = zero
    for value in values:
        acc = combine(acc, value)
    return acc


def _validate_unary_carrier(n: int, total_ops, partial_ops) -> None:
    for f in total_ops:
        if len(f) != n or any(y < 0 or y >= n for y in f):
            raise ValueError("invalid total unary operation")
    for g in partial_ops:
        if len(g) != n:
            raise ValueError("invalid partial unary operation")
        if any(y is not None and (y < 0 or y >= n) for y in g):
            raise ValueError("invalid partial unary output")


def _validate_channel(n: int, channel: RelationChannel) -> None:
    if len(channel.weights) != n or any(len(row) != n for row in channel.weights):
        raise ValueError(f"relation channel {channel.name!r} has wrong carrier size")


def relation_signature(partition: Sequence[Any], channel: RelationChannel, state: int) -> Tuple[Any, ...]:
    p = normalize_partition(partition)
    blocks = partition_blocks(p)
    return tuple(
        _aggregate((channel.weights[state][target] for target in block), channel.zero, channel.combine)
        for block in blocks
    )


def refine_once(
    partition: Sequence[Any],
    total_unary_ops: Sequence[TotalUnary] = (),
    partial_unary_ops: Sequence[PartialUnary] = (),
    relation_channels: Sequence[RelationChannel] = (),
) -> Partition:
    p = normalize_partition(partition)
    n = len(p)
    _validate_unary_carrier(n, total_unary_ops, partial_unary_ops)
    for channel in relation_channels:
        _validate_channel(n, channel)

    signatures = []
    for x in range(n):
        total_sig = tuple(p[f[x]] for f in total_unary_ops)
        partial_sig = tuple(
            ("disabled",) if g[x] is None else ("enabled", p[g[x]])
            for g in partial_unary_ops
        )
        relation_sig = tuple(relation_signature(p, channel, x) for channel in relation_channels)
        signatures.append((p[x], total_sig, partial_sig, relation_sig))
    return normalize_partition(signatures)


def is_stable(
    partition: Sequence[Any],
    total_unary_ops: Sequence[TotalUnary] = (),
    partial_unary_ops: Sequence[PartialUnary] = (),
    relation_channels: Sequence[RelationChannel] = (),
) -> bool:
    p = normalize_partition(partition)
    return refine_once(p, total_unary_ops, partial_unary_ops, relation_channels) == p


def _descend_total(p: Partition, op: TotalUnary) -> Tuple[int, ...]:
    return tuple(p[op[block[0]]] for block in partition_blocks(p))


def _descend_partial(p: Partition, op: PartialUnary) -> Tuple[Optional[int], ...]:
    out = []
    for block in partition_blocks(p):
        value = op[block[0]]
        out.append(None if value is None else p[value])
    return tuple(out)


def _descend_relation(p: Partition, channel: RelationChannel) -> Tuple[Tuple[Any, ...], ...]:
    return tuple(relation_signature(p, channel, block[0]) for block in partition_blocks(p))


def compile_mixed_typed(
    initial_partition: Sequence[Any],
    total_unary_ops: Sequence[TotalUnary] = (),
    partial_unary_ops: Sequence[PartialUnary] = (),
    relation_channels: Sequence[RelationChannel] = (),
) -> MixedCompileResult:
    p = normalize_partition(initial_partition)
    history = [p]
    while True:
        q = refine_once(p, total_unary_ops, partial_unary_ops, relation_channels)
        if q == p:
            break
        if block_count(q) <= block_count(p):
            raise AssertionError("strict refinement must increase block count")
        history.append(q)
        p = q
        if len(history) - 1 > len(p):
            raise AssertionError("finite refinement bound violated")

    return MixedCompileResult(
        partition=p,
        history=tuple(history),
        descended_total_unary=tuple(_descend_total(p, f) for f in total_unary_ops),
        descended_partial_unary=tuple(_descend_partial(p, g) for g in partial_unary_ops),
        descended_relation_rows=tuple(_descend_relation(p, c) for c in relation_channels),
    )


def partial_totalization(op: PartialUnary) -> TotalUnary:
    """Adjoin one disabled state and totalize a unary partial operation.

    This is a quotient-compatibility device only; it does not claim that arbitrary
    algebraic identities of a partial algebra are preserved by one-point totalization.
    """
    n = len(op)
    bottom = n
    return tuple(bottom if y is None else y for y in op) + (bottom,)


def lifted_partition_with_bottom(partition: Sequence[Any]) -> Partition:
    p = normalize_partition(partition)
    bottom_label = (max(p) + 1) if p else 0
    return p + (bottom_label,)


def relation_is_block_sum_stable(partition: Sequence[Any], matrix, semiring: Semiring) -> bool:
    p = normalize_partition(partition)
    blocks = partition_blocks(p)
    n = len(p)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError("matrix has wrong carrier size")
    for source_block in blocks:
        representative = source_block[0]
        base = tuple(
            _aggregate((matrix[representative][y] for y in target_block), semiring.zero, semiring.add)
            for target_block in blocks
        )
        for x in source_block[1:]:
            row = tuple(
                _aggregate((matrix[x][y] for y in target_block), semiring.zero, semiring.add)
                for target_block in blocks
            )
            if row != base:
                return False
    return True


def quotient_matrix(partition: Sequence[Any], matrix, semiring: Semiring) -> Tuple[Tuple[Any, ...], ...]:
    p = normalize_partition(partition)
    if not relation_is_block_sum_stable(p, matrix, semiring):
        raise ValueError("matrix is not block-sum stable")
    blocks = partition_blocks(p)
    return tuple(
        tuple(
            _aggregate((matrix[source_block[0]][y] for y in target_block), semiring.zero, semiring.add)
            for target_block in blocks
        )
        for source_block in blocks
    )


def matrix_add(left, right, semiring: Semiring):
    if len(left) != len(right) or (left and len(left[0]) != len(right[0])):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(semiring.add(left[i][j], right[i][j]) for j in range(len(left[0])))
        for i in range(len(left))
    )


def matrix_mul(left, right, semiring: Semiring):
    if not left or not right:
        return ()
    if len(left[0]) != len(right):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(
            _aggregate(
                (semiring.mul(left[i][j], right[j][k]) for j in range(len(right))),
                semiring.zero,
                semiring.add,
            )
            for k in range(len(right[0]))
        )
        for i in range(len(left))
    )


def identity_matrix(n: int, semiring: Semiring):
    return tuple(
        tuple(semiring.one if i == j else semiring.zero for j in range(n))
        for i in range(n)
    )


def boolean_star(matrix):
    """Reflexive-transitive closure for a Boolean matrix."""
    reach = [list(map(bool, row)) for row in matrix]
    n = len(reach)
    if any(len(row) != n for row in reach):
        raise ValueError("Boolean star requires a square matrix")
    for i in range(n):
        reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return tuple(tuple(row) for row in reach)


def ping_pong_operations(n: int) -> Tuple[TotalUnary, TotalUnary, Partition]:
    """Sharp cross-activation family for every n >= 3."""
    if n < 3:
        raise ValueError("n must be at least 3")
    f = list(range(n))
    g = list(range(n))
    for k in range(1, n):
        if k % 2 == 1:
            f[k] = k - 1
        else:
            g[k] = k - 1
    initial = normalize_partition((0,) + (1,) * (n - 1))
    return tuple(f), tuple(g), initial
