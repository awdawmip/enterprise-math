"""Higher-order repair spectrum of a finite precision projection.

Let ``fine`` refine ``coarse`` on one finite state set.  The canonical quotient
projection from fine classes to coarse classes has a fiber over each coarse
class whose size is exactly the number of fine classes inside that block.  This
is the local minimum repair alphabet of P023-S9.

Applying the P011 collision spectrum to this quotient projection yields a full
higher-order repair spectrum for the precision upgrade ``coarse -> fine``.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping
from math import comb

State = Hashable
Partition = Mapping[State, Hashable]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    result = tuple(states)
    if not result:
        raise ValueError("state domain must be nonempty")
    if len(result) != len(set(result)):
        raise ValueError("state domain must contain distinct states")
    return result


def _validate_partition(states: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(states):
        raise ValueError("partition must label every domain state exactly once")


def refines(states: Iterable[State], fine: Partition, coarse: Partition) -> bool:
    """Whether equality at ``fine`` implies equality at ``coarse``."""

    domain = _domain(states)
    _validate_partition(domain, fine)
    _validate_partition(domain, coarse)
    seen: dict[Hashable, Hashable] = {}
    for state in domain:
        f = fine[state]
        c = coarse[state]
        previous = seen.get(f)
        if previous is not None and previous != c:
            return False
        seen[f] = c
    return True


def fine_classes_by_coarse_block(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> dict[Hashable, frozenset[Hashable]]:
    """Fibers of the canonical quotient projection ``X/fine -> X/coarse``."""

    domain = _domain(states)
    if not refines(domain, fine, coarse):
        raise ValueError("fine partition must refine coarse partition")
    groups: dict[Hashable, set[Hashable]] = {}
    for state in domain:
        groups.setdefault(coarse[state], set()).add(fine[state])
    return {block: frozenset(classes) for block, classes in groups.items()}


def local_repair_sizes(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> dict[Hashable, int]:
    """Local minimum repair alphabet in every coarse block."""

    return {
        block: len(classes)
        for block, classes in fine_classes_by_coarse_block(states, fine, coarse).items()
    }


def minimum_repair_alphabet_size(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> int:
    return max(local_repair_sizes(states, fine, coarse).values())


def repair_spectrum(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> tuple[int, ...]:
    """P011 collision spectrum of the quotient projection ``X/fine -> X/coarse``.

    ``J_1`` equals the number of fine classes.  Higher entries count subsets of
    fine classes that must share one coarse output block.
    """

    sizes = local_repair_sizes(states, fine, coarse)
    fine_class_count = sum(sizes.values())
    return tuple(
        sum(comb(size, order) for size in sizes.values())
        for order in range(1, fine_class_count + 1)
    )


def repair_size_distribution(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> dict[int, int]:
    """Count coarse blocks by their local minimum repair alphabet size."""

    sizes = local_repair_sizes(states, fine, coarse)
    fine_class_count = sum(sizes.values())
    counts = Counter(sizes.values())
    return {
        size: counts.get(size, 0)
        for size in range(1, fine_class_count + 1)
    }


def reconstruct_repair_distribution_from_spectrum(
    spectrum: tuple[int, ...] | list[int],
) -> dict[int, int]:
    """Recover local repair-size multiplicities by P011 binomial inversion."""

    values = tuple(spectrum)
    if not values:
        raise ValueError("spectrum must be nonempty")
    fine_class_count = values[0]
    if not isinstance(fine_class_count, int) or fine_class_count < 1:
        raise ValueError("J_1 must be the positive number of fine classes")
    if len(values) != fine_class_count:
        raise ValueError("spectrum must contain J_1 through J_number_of_fine_classes")
    padded = (0,) + values
    return {
        size: sum(
            (-1) ** (order - size) * comb(order, size) * padded[order]
            for order in range(size, fine_class_count + 1)
        )
        for size in range(1, fine_class_count + 1)
    }


def repair_gain_spectrum(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> tuple[int, ...]:
    """Subsets of fine classes that are separated by retaining fine precision.

    The coarse projection spectrum counts subsets of fine classes merged by the
    forgetting map.  The identity projection on ``X/fine`` has spectrum
    ``(number_of_fine_classes, 0, ..., 0)``.  Thus orders >=2 are exactly the
    higher-order ambiguities removed by upgrading from coarse to fine.
    """

    spectrum = repair_spectrum(states, fine, coarse)
    return (0,) + spectrum[1:]


def chain_projection_profiles(
    states: Iterable[State],
    finest: Partition,
    middle: Partition,
    coarsest: Partition,
) -> dict[str, object]:
    """Exact local composition data for ``X/finest -> X/middle -> X/coarsest``."""

    domain = _domain(states)
    if not refines(domain, finest, middle):
        raise ValueError("finest must refine middle")
    if not refines(domain, middle, coarsest):
        raise ValueError("middle must refine coarsest")

    fine_in_middle = fine_classes_by_coarse_block(domain, finest, middle)
    middle_in_coarse = fine_classes_by_coarse_block(domain, middle, coarsest)
    fine_in_coarse = fine_classes_by_coarse_block(domain, finest, coarsest)

    middle_owner: dict[Hashable, Hashable] = {}
    for state in domain:
        middle_owner[middle[state]] = coarsest[state]

    reconstructed: dict[Hashable, int] = {}
    for coarse_block, middle_blocks in middle_in_coarse.items():
        reconstructed[coarse_block] = sum(
            len(fine_in_middle[middle_block])
            for middle_block in middle_blocks
        )

    direct = {block: len(classes) for block, classes in fine_in_coarse.items()}
    if reconstructed != direct:
        raise AssertionError("quotient projection fiber sizes failed exact composition")

    first_max = max(len(classes) for classes in fine_in_middle.values())
    second_max = max(len(classes) for classes in middle_in_coarse.values())
    direct_max = max(direct.values())
    if direct_max > first_max * second_max:
        raise AssertionError("direct repair exceeded staged product bound")

    return {
        "finest_to_middle": {
            block: len(classes) for block, classes in fine_in_middle.items()
        },
        "middle_to_coarsest": {
            block: len(classes) for block, classes in middle_in_coarse.items()
        },
        "finest_to_coarsest": direct,
        "first_max": first_max,
        "second_max": second_max,
        "direct_max": direct_max,
        "product_bound": first_max * second_max,
    }
