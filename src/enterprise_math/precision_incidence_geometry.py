"""Finite precision incidence graph and integer repair geometry.

Two partitions of the same state set define a bipartite graph between their
blocks: an edge is present exactly when the two blocks have nonempty
intersection.  This one graph simultaneously records realized product classes,
minimum task-addition repair alphabets, higher repair spectra, and a directed
multiplicative repair factor.

The directed factor obeys a multiplicative triangle inequality.  Applying the
integer symbol-depth ``min{ell : factor <= base**ell}`` produces an integer
Lawvere-style directed distance; symmetrizing it yields a genuine metric on
partition equivalence relations (independent of block label names).
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping
from math import comb

State = Hashable
Partition = Mapping[State, Hashable]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    return domain


def _validate(states: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(states):
        raise ValueError("partition must label every domain state exactly once")


def same_partition(
    states: Iterable[State], first: Partition, second: Partition
) -> bool:
    """Whether two labelings induce the same equivalence relation."""

    domain = _domain(states)
    _validate(domain, first)
    _validate(domain, second)
    for left in domain:
        for right in domain:
            if (first[left] == first[right]) != (second[left] == second[right]):
                return False
    return True


def refines(states: Iterable[State], fine: Partition, coarse: Partition) -> bool:
    """Whether every fine block lies inside one coarse block."""

    domain = _domain(states)
    _validate(domain, fine)
    _validate(domain, coarse)
    owner: dict[Hashable, Hashable] = {}
    for state in domain:
        fine_label = fine[state]
        coarse_label = coarse[state]
        previous = owner.get(fine_label)
        if previous is not None and previous != coarse_label:
            return False
        owner[fine_label] = coarse_label
    return True


def block_count(states: Iterable[State], partition: Partition) -> int:
    domain = _domain(states)
    _validate(domain, partition)
    return len({partition[state] for state in domain})


def incidence_edges(
    states: Iterable[State], first: Partition, second: Partition
) -> frozenset[tuple[Hashable, Hashable]]:
    """Nonempty intersections of first- and second-partition blocks."""

    domain = _domain(states)
    _validate(domain, first)
    _validate(domain, second)
    return frozenset((first[state], second[state]) for state in domain)


def realized_product_class_count(
    states: Iterable[State], first: Partition, second: Partition
) -> int:
    """Number of blocks of the common refinement ``first ∩ second``."""

    return len(incidence_edges(states, first, second))


def formal_product_candidate_count(
    states: Iterable[State], first: Partition, second: Partition
) -> int:
    return block_count(states, first) * block_count(states, second)


def unrealized_product_tuple_defect(
    states: Iterable[State], first: Partition, second: Partition
) -> int:
    """Formal Cartesian class pairs that are not realized by any state."""

    return formal_product_candidate_count(states, first, second) - realized_product_class_count(
        states, first, second
    )


def incidence_degrees(
    states: Iterable[State], first: Partition, second: Partition
) -> dict[Hashable, int]:
    """Number of second blocks meeting each first block."""

    edges = incidence_edges(states, first, second)
    degrees: Counter[Hashable] = Counter(left for left, _ in edges)
    return dict(degrees)


def directed_repair_factor(
    states: Iterable[State], known: Partition, added: Partition
) -> int:
    """Minimum alphabet for upgrading ``known`` to the product task.

    This is the maximum number of ``added`` blocks meeting one ``known`` block.
    Equivalently it is the minimum repair alphabet for
    ``known -> (known, added)``.
    """

    return max(incidence_degrees(states, known, added).values())


def directed_repair_spectrum(
    states: Iterable[State], known: Partition, added: Partition
) -> tuple[int, ...]:
    """Binomial spectrum of local task-addition repair sizes."""

    degrees = incidence_degrees(states, known, added)
    edge_count = sum(degrees.values())
    return tuple(
        sum(comb(degree, order) for degree in degrees.values())
        for order in range(1, edge_count + 1)
    )


def common_refinement(
    states: Iterable[State], first: Partition, second: Partition
) -> dict[State, tuple[Hashable, Hashable]]:
    domain = _domain(states)
    _validate(domain, first)
    _validate(domain, second)
    return {state: (first[state], second[state]) for state in domain}


def integer_symbol_depth(value: int, base: int) -> int:
    """Return the least ``ell`` with ``value <= base**ell`` using integers only."""

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
    """Integer symbol-depth of the directed repair factor."""

    return integer_symbol_depth(directed_repair_factor(states, known, added), base)


def symmetric_repair_distance(
    states: Iterable[State], first: Partition, second: Partition, base: int = 2
) -> int:
    """Symmetric integer metric induced by the two directed repair depths."""

    return directed_repair_depth(states, first, second, base) + directed_repair_depth(
        states, second, first, base
    )


def multiplicative_triangle(
    states: Iterable[State], first: Partition, middle: Partition, last: Partition
) -> dict[str, int | bool]:
    """Return ``rho(first,last) <= rho(first,middle)*rho(middle,last)``."""

    left = directed_repair_factor(states, first, last)
    first_leg = directed_repair_factor(states, first, middle)
    second_leg = directed_repair_factor(states, middle, last)
    bound = first_leg * second_leg
    if left > bound:
        raise AssertionError("directed repair factor violated multiplicative triangle")
    return {
        "direct": left,
        "first_leg": first_leg,
        "second_leg": second_leg,
        "product_bound": bound,
        "holds": True,
    }


def additive_depth_triangle(
    states: Iterable[State],
    first: Partition,
    middle: Partition,
    last: Partition,
    base: int = 2,
) -> dict[str, int | bool]:
    """Return the integer directed triangle after applying symbol depth."""

    direct = directed_repair_depth(states, first, last, base)
    first_leg = directed_repair_depth(states, first, middle, base)
    second_leg = directed_repair_depth(states, middle, last, base)
    if direct > first_leg + second_leg:
        raise AssertionError("directed repair depth violated triangle inequality")
    return {
        "direct": direct,
        "first_leg": first_leg,
        "second_leg": second_leg,
        "sum_bound": first_leg + second_leg,
        "holds": True,
    }
