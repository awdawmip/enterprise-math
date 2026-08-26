"""Finite A2 precision-incidence calculus.

The module treats a finite precision state as a partition/equivalence relation on
one finite state set.  It compiles exact task-addition repair, higher-order
repair spectra, incidence geometry, and higher-order joint task structure.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping, Sequence
from math import comb
from typing import TypeAlias

State = Hashable
Partition: TypeAlias = Mapping[State, Hashable]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    return domain


def _validate(domain: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(domain):
        raise ValueError("partition must label every state exactly once")


def same_partition(states: Iterable[State], first: Partition, second: Partition) -> bool:
    domain = _domain(states)
    _validate(domain, first)
    _validate(domain, second)
    return all(
        (first[x] == first[y]) == (second[x] == second[y])
        for x in domain
        for y in domain
    )


def refines(states: Iterable[State], fine: Partition, coarse: Partition) -> bool:
    """Whether equality at ``fine`` implies equality at ``coarse``."""
    domain = _domain(states)
    _validate(domain, fine)
    _validate(domain, coarse)
    owner: dict[Hashable, Hashable] = {}
    for state in domain:
        fine_label = fine[state]
        coarse_label = coarse[state]
        if fine_label in owner and owner[fine_label] != coarse_label:
            return False
        owner[fine_label] = coarse_label
    return True


def block_count(states: Iterable[State], partition: Partition) -> int:
    domain = _domain(states)
    _validate(domain, partition)
    return len({partition[state] for state in domain})


def common_refinement(
    states: Iterable[State], partitions: Sequence[Partition]
) -> dict[State, tuple[Hashable, ...]]:
    domain = _domain(states)
    for partition in partitions:
        _validate(domain, partition)
    return {
        state: tuple(partition[state] for partition in partitions)
        for state in domain
    }


def realized_joint_tuples(
    states: Iterable[State], partitions: Sequence[Partition]
) -> frozenset[tuple[Hashable, ...]]:
    joint = common_refinement(states, partitions)
    return frozenset(joint.values())


def realized_joint_class_count(
    states: Iterable[State], partitions: Sequence[Partition]
) -> int:
    return len(realized_joint_tuples(states, partitions))


def formal_joint_candidate_count(
    states: Iterable[State], partitions: Sequence[Partition]
) -> int:
    domain = _domain(states)
    product = 1
    for partition in partitions:
        product *= block_count(domain, partition)
    return product


def incidence_edges(
    states: Iterable[State], first: Partition, second: Partition
) -> frozenset[tuple[Hashable, Hashable]]:
    domain = _domain(states)
    _validate(domain, first)
    _validate(domain, second)
    return frozenset((first[state], second[state]) for state in domain)


def incidence_degrees(
    states: Iterable[State], known: Partition, added: Partition
) -> dict[Hashable, int]:
    edges = incidence_edges(states, known, added)
    degrees: Counter[Hashable] = Counter(left for left, _ in edges)
    return dict(degrees)


def directed_repair_factor(
    states: Iterable[State], known: Partition, added: Partition
) -> int:
    """Minimum alphabet for upgrading ``known`` to ``known ∩ added``."""
    return max(incidence_degrees(states, known, added).values())


def directed_repair_spectrum(
    states: Iterable[State], known: Partition, added: Partition
) -> tuple[int, ...]:
    """Binomial spectrum of local repair multiplicities.

    Entry k-1 is ``sum_B binom(deg(B), k)``.  The spectrum stops at the
    maximum local repair size; trailing zero orders are omitted.
    """
    degrees = tuple(incidence_degrees(states, known, added).values())
    maximum = max(degrees)
    return tuple(
        sum(comb(degree, order) for degree in degrees)
        for order in range(1, maximum + 1)
    )


def repair_size_distribution(
    states: Iterable[State], known: Partition, added: Partition
) -> dict[int, int]:
    return dict(Counter(incidence_degrees(states, known, added).values()))


def reconstruct_repair_distribution(
    spectrum: Sequence[int],
) -> dict[int, int]:
    values = tuple(spectrum)
    if not values:
        raise ValueError("spectrum must be nonempty")
    maximum = len(values)
    padded = (0,) + values
    distribution = {
        size: sum(
            (-1) ** (order - size) * comb(order, size) * padded[order]
            for order in range(size, maximum + 1)
        )
        for size in range(1, maximum + 1)
    }
    return {size: count for size, count in distribution.items() if count}


def active_repair_support_count(
    states: Iterable[State], known: Partition, added: Partition
) -> int:
    """Number of known blocks that genuinely split when the task is added."""
    return sum(
        degree > 1 for degree in incidence_degrees(states, known, added).values()
    )


def binary_split_identity(
    states: Iterable[State], known: Partition, added: Partition
) -> dict[str, int | bool]:
    """Exact S20 identity when every local split has size one or two.

    In that case the number of active split blocks equals the second repair
    spectrum coefficient and the increase in joint class count.
    """
    domain = _domain(states)
    degrees = incidence_degrees(domain, known, added)
    if any(degree not in (1, 2) for degree in degrees.values()):
        raise ValueError("binary_split_identity requires all local degrees in {1,2}")
    active = sum(degree == 2 for degree in degrees.values())
    pair_mass = sum(comb(degree, 2) for degree in degrees.values())
    coarse_count = block_count(domain, known)
    fine_count = realized_joint_class_count(domain, [known, added])
    gain = fine_count - coarse_count
    if not (active == pair_mass == gain):
        raise AssertionError("binary split identity failed")
    return {
        "active_support": active,
        "second_repair_mass": pair_mass,
        "class_count_gain": gain,
        "holds": True,
    }


def integer_symbol_depth(value: int, base: int = 2) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    if base < 2:
        raise ValueError("base must be at least two")
    depth = 0
    capacity = 1
    while capacity < value:
        capacity *= base
        depth += 1
    return depth


def directed_repair_depth(
    states: Iterable[State], known: Partition, added: Partition, base: int = 2
) -> int:
    return integer_symbol_depth(directed_repair_factor(states, known, added), base)


def symmetric_repair_distance(
    states: Iterable[State], first: Partition, second: Partition, base: int = 2
) -> int:
    return directed_repair_depth(states, first, second, base) + directed_repair_depth(
        states, second, first, base
    )


def multiplicative_triangle(
    states: Iterable[State], first: Partition, middle: Partition, last: Partition
) -> bool:
    return directed_repair_factor(states, first, last) <= (
        directed_repair_factor(states, first, middle)
        * directed_repair_factor(states, middle, last)
    )


def additive_depth_triangle(
    states: Iterable[State],
    first: Partition,
    middle: Partition,
    last: Partition,
    base: int = 2,
) -> bool:
    return directed_repair_depth(states, first, last, base) <= (
        directed_repair_depth(states, first, middle, base)
        + directed_repair_depth(states, middle, last, base)
    )


def extension_sets(
    states: Iterable[State],
    known_partitions: Sequence[Partition],
    added_partition: Partition,
) -> dict[tuple[Hashable, ...], frozenset[Hashable]]:
    domain = _domain(states)
    _validate(domain, added_partition)
    for partition in known_partitions:
        _validate(domain, partition)
    extensions: dict[tuple[Hashable, ...], set[Hashable]] = {}
    for state in domain:
        prefix = tuple(partition[state] for partition in known_partitions)
        extensions.setdefault(prefix, set()).add(added_partition[state])
    return {prefix: frozenset(values) for prefix, values in extensions.items()}


def conditional_repair_factor(
    states: Iterable[State],
    known_partitions: Sequence[Partition],
    added_partition: Partition,
) -> int:
    return max(
        len(values)
        for values in extension_sets(states, known_partitions, added_partition).values()
    )


def conditional_repair_spectrum(
    states: Iterable[State],
    known_partitions: Sequence[Partition],
    added_partition: Partition,
) -> tuple[int, ...]:
    degrees = tuple(
        len(values)
        for values in extension_sets(states, known_partitions, added_partition).values()
    )
    maximum = max(degrees)
    return tuple(
        sum(comb(degree, order) for degree in degrees)
        for order in range(1, maximum + 1)
    )


def context_refinement_monotone(
    states: Iterable[State],
    less_context: Sequence[Partition],
    more_context: Sequence[Partition],
    added_partition: Partition,
) -> bool:
    """More retained context cannot increase the repair for one added task."""
    domain = _domain(states)
    less_joint = common_refinement(domain, less_context)
    more_joint = common_refinement(domain, more_context)
    if not refines(domain, more_joint, less_joint):
        raise ValueError("more_context must refine less_context")
    return conditional_repair_factor(domain, more_context, added_partition) <= (
        conditional_repair_factor(domain, less_context, added_partition)
    )


def pairwise_intersection_counts(
    states: Iterable[State], partitions: Sequence[Partition]
) -> dict[tuple[int, int], dict[tuple[Hashable, Hashable], int]]:
    domain = _domain(states)
    result: dict[tuple[int, int], dict[tuple[Hashable, Hashable], int]] = {}
    for i in range(len(partitions)):
        for j in range(i + 1, len(partitions)):
            _validate(domain, partitions[i])
            _validate(domain, partitions[j])
            counts = Counter(
                (partitions[i][state], partitions[j][state]) for state in domain
            )
            result[(i, j)] = dict(counts)
    return result
