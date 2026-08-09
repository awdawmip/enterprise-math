"""Finite task-partition refinement and exact repair multiplicity.

This module supplies the finite counting layer behind the generic P023 pair
repair.  A represented partition may be refined by a richer task.  The exact
repair cost is controlled locally: within each old coarse block, count how
many target blocks it splits into.  Repair symbols can be reused across
different coarse blocks, so the minimum global alphabet is the maximum local
split multiplicity rather than the total number of target classes.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
QueryName = TypeVar("QueryName", bound=Hashable)
Label = Hashable
Partition = Mapping[State, Label]
Query = Mapping[State, Label]


def _states(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _validate_partition(states: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(states):
        raise ValueError("partition must label every state exactly once")


def _canonical_ids(
    states: tuple[State, ...], signatures: Mapping[State, Label]
) -> dict[State, int]:
    ids: dict[Label, int] = {}
    result: dict[State, int] = {}
    for state in states:
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


def same_partition(
    domain: Iterable[State], left: Partition, right: Partition
) -> bool:
    """Whether two label maps induce the same equivalence relation."""

    states = _states(domain)
    _validate_partition(states, left)
    _validate_partition(states, right)
    return all(
        (left[x] == left[y]) == (right[x] == right[y])
        for x in states
        for y in states
    )


def refines(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> bool:
    """Whether every finer block lies inside one coarser block."""

    states = _states(domain)
    _validate_partition(states, finer)
    _validate_partition(states, coarser)
    seen: dict[Label, Label] = {}
    for state in states:
        fine = finer[state]
        coarse = coarser[state]
        previous = seen.get(fine)
        if previous is not None and previous != coarse:
            return False
        seen[fine] = coarse
    return True


def class_count(partition: Partition) -> int:
    return len(set(partition.values()))


def task_partition(
    domain: Iterable[State],
    queries: Mapping[QueryName, Query],
) -> dict[State, int]:
    """Kernel partition of the tuple of all declared query outputs.

    With no queries, every state lies in one class.
    """

    states = _states(domain)
    items = tuple(queries.items())
    for _, query in items:
        _validate_partition(states, query)
    if not items:
        return {state: 0 for state in states}
    signatures = {
        state: tuple(query[state] for _, query in items) for state in states
    }
    return _canonical_ids(states, signatures)


def realized_class_tuples(
    domain: Iterable[State], *partitions: Partition
) -> frozenset[tuple[Label, ...]]:
    """Actual tuples realized in the Cartesian product of quotient labels."""

    states = _states(domain)
    for partition in partitions:
        _validate_partition(states, partition)
    if not partitions:
        return frozenset({()})
    return frozenset(
        tuple(partition[state] for partition in partitions) for state in states
    )


def combined_partition(
    domain: Iterable[State], *partitions: Partition
) -> dict[State, int]:
    """Common refinement induced by retaining every supplied quotient label."""

    states = _states(domain)
    for partition in partitions:
        _validate_partition(states, partition)
    if not partitions:
        return {state: 0 for state in states}
    signatures = {
        state: tuple(partition[state] for partition in partitions)
        for state in states
    }
    return _canonical_ids(states, signatures)


def local_split_multiplicities(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> dict[Label, int]:
    """Number of target blocks realized inside each old coarse block."""

    states = _states(domain)
    _validate_partition(states, finer)
    _validate_partition(states, coarser)
    if not refines(states, finer, coarser):
        raise ValueError("finer partition must refine coarser partition")

    splits: dict[Label, set[Label]] = {}
    for state in states:
        splits.setdefault(coarser[state], set()).add(finer[state])
    return {coarse: len(fine_labels) for coarse, fine_labels in splits.items()}


def minimal_repair_alphabet_size(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> int:
    """Exact minimum number of repair symbols needed to upgrade the quotient."""

    multiplicities = local_split_multiplicities(domain, finer, coarser)
    return max(multiplicities.values())


def minimal_repair_code(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> dict[State, int]:
    """Construct a minimum-size repair code.

    Fine-block codes are assigned independently inside each old coarse block,
    so the same integer symbols are reused across unrelated coarse blocks.
    """

    states = _states(domain)
    _validate_partition(states, finer)
    _validate_partition(states, coarser)
    if not refines(states, finer, coarser):
        raise ValueError("finer partition must refine coarser partition")

    local_codes: dict[Label, dict[Label, int]] = {}
    repair: dict[State, int] = {}
    for state in states:
        coarse = coarser[state]
        fine = finer[state]
        codes = local_codes.setdefault(coarse, {})
        if fine not in codes:
            codes[fine] = len(codes)
        repair[state] = codes[fine]
    return repair


def repaired_partition(
    domain: Iterable[State], coarser: Partition, repair: Partition
) -> dict[State, int]:
    """Partition induced by retaining the old coarse label plus repair code."""

    return combined_partition(domain, coarser, repair)


def repair_chain_bound(
    domain: Iterable[State],
    finest: Partition,
    middle: Partition,
    coarsest: Partition,
) -> tuple[int, int, int]:
    """Return repair costs for a refinement chain and verify submultiplicativity.

    For ``finest <= middle <= coarsest`` in the refinement order, returns
    ``(R_coarse_middle, R_middle_fine, R_coarse_fine)`` and asserts

        R_coarse_fine <= R_coarse_middle * R_middle_fine.
    """

    states = _states(domain)
    if not refines(states, finest, middle):
        raise ValueError("finest must refine middle")
    if not refines(states, middle, coarsest):
        raise ValueError("middle must refine coarsest")

    first = minimal_repair_alphabet_size(states, middle, coarsest)
    second = minimal_repair_alphabet_size(states, finest, middle)
    direct = minimal_repair_alphabet_size(states, finest, coarsest)
    if direct > first * second:
        raise AssertionError("repair multiplicity must be submultiplicative")
    return first, second, direct
