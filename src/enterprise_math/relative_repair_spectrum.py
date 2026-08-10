"""Relative repair spectrum between finite precision partitions.

For a refinement F of E, the canonical quotient projection

    X/F -> X/E

forgets which fine block inside an old coarse block was retained.  The fiber
sizes of that projection are therefore exactly the local minimum repair
alphabet sizes.  Applying the P011 collision-spectrum formulas to this
canonical projection gives a complete higher-order repair spectrum.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping
from math import comb
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
Label = Hashable
Partition = Mapping[State, Label]


def _states(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _validate(states: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(states):
        raise ValueError("partition must label every state exactly once")


def refines(domain: Iterable[State], finer: Partition, coarser: Partition) -> bool:
    """Whether equality in ``finer`` always implies equality in ``coarser``."""

    states = _states(domain)
    _validate(states, finer)
    _validate(states, coarser)
    coarse_by_fine: dict[Label, Label] = {}
    for state in states:
        fine = finer[state]
        coarse = coarser[state]
        previous = coarse_by_fine.get(fine)
        if previous is not None and previous != coarse:
            return False
        coarse_by_fine[fine] = coarse
    return True


def quotient_projection_split_sizes(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> tuple[int, ...]:
    """Return numbers of fine blocks contained in each reached coarse block.

    These are the fiber sizes of the canonical quotient projection ``X/F -> X/E``.
    The tuple is sorted only to make the executable representation label-invariant.
    """

    states = _states(domain)
    _validate(states, finer)
    _validate(states, coarser)
    if not refines(states, finer, coarser):
        raise ValueError("finer partition must refine coarser partition")

    fine_labels_by_coarse: dict[Label, set[Label]] = {}
    for state in states:
        fine_labels_by_coarse.setdefault(coarser[state], set()).add(finer[state])
    return tuple(sorted((len(labels) for labels in fine_labels_by_coarse.values()), reverse=True))


def maximum_repair_alphabet_size(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> int:
    """Worst local alphabet needed to recover ``finer`` from ``coarser``."""

    return max(quotient_projection_split_sizes(domain, finer, coarser))


def relative_repair_spectrum(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> tuple[int, ...]:
    """Return J_k of the canonical quotient projection for all nonzero orders.

    If ``s_B`` is the number of fine blocks inside coarse block ``B``, then

        R_k(E <- F) = sum_B binom(s_B, k).

    The first coordinate is the number of fine quotient classes.  Higher
    coordinates count k-tuples of fine classes that the coarse precision forgets
    into one coarse class.
    """

    split_sizes = quotient_projection_split_sizes(domain, finer, coarser)
    maximum = max(split_sizes)
    return tuple(
        sum(comb(size, order) for size in split_sizes)
        for order in range(1, maximum + 1)
    )


def reconstructed_split_size_distribution(spectrum: tuple[int, ...]) -> dict[int, int]:
    """Recover the number of coarse blocks of each split size by binomial inversion."""

    if not spectrum:
        raise ValueError("spectrum must be nonempty")
    values = (0,) + tuple(spectrum)
    maximum = len(spectrum)
    return {
        size: sum(
            ((-1) ** (order - size)) * comb(order, size) * values[order]
            for order in range(size, maximum + 1)
        )
        for size in range(1, maximum + 1)
    }


def actual_split_size_distribution(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> dict[int, int]:
    """Direct histogram used as a differential oracle for the inversion theorem."""

    sizes = quotient_projection_split_sizes(domain, finer, coarser)
    histogram = Counter(sizes)
    return {size: histogram.get(size, 0) for size in range(1, max(sizes) + 1)}


def relative_repair_polynomial_coefficients(
    domain: Iterable[State], finer: Partition, coarser: Partition
) -> tuple[int, ...]:
    """Coefficients of ``sum_B ((1+t)^s_B - 1)`` from degree zero upward.

    Degree zero is always zero; degree k is exactly the k-th relative repair
    spectrum coordinate.
    """

    return (0,) + relative_repair_spectrum(domain, finer, coarser)


def refinement_gain_spectrum(
    domain: Iterable[State], coarse: Partition, fine: Partition
) -> tuple[int, ...]:
    """State-level ambiguity removed by refining ``coarse`` to ``fine``.

    Here block sizes count original fine states rather than quotient classes.  If
    A_k(E)=sum_{B in X/E} binom(|B|,k), the returned coordinate is
    A_k(coarse)-A_k(fine).  It exactly counts k-element state sets that were
    previously co-observed but are separated by the finer precision.
    """

    states = _states(domain)
    _validate(states, coarse)
    _validate(states, fine)
    if not refines(states, fine, coarse):
        raise ValueError("fine partition must refine coarse partition")

    def block_sizes(partition: Partition) -> tuple[int, ...]:
        counts = Counter(partition[state] for state in states)
        return tuple(counts.values())

    coarse_sizes = block_sizes(coarse)
    fine_sizes = block_sizes(fine)
    maximum = max(coarse_sizes)
    gains = []
    for order in range(1, maximum + 1):
        before = sum(comb(size, order) for size in coarse_sizes)
        after = sum(comb(size, order) for size in fine_sizes)
        gain = before - after
        if gain < 0:
            raise AssertionError("refinement increased a binomial ambiguity coordinate")
        gains.append(gain)
    return tuple(gains)
