"""Local repair width versus global active-support complexity.

For a finite refinement F of a coarser partition E, each E-block contains some
number s_B of F-blocks.  P023's minimum local repair alphabet is max s_B, while
the global repair spectrum sums binomial functions of the same local split
sizes.  This module separates those two notions and records the exact collapse
that occurs for binary refinements.
"""

from __future__ import annotations

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


def _validate(domain: tuple[State, ...], partition: Partition) -> None:
    if set(partition) != set(domain):
        raise ValueError("partition must cover the state domain exactly")


def local_split_sizes(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> dict[Hashable, int]:
    """Number of fine blocks meeting each coarse block, requiring fine<=coarse."""

    domain = _domain(states)
    _validate(domain, fine)
    _validate(domain, coarse)

    coarse_to_fine: dict[Hashable, set[Hashable]] = {}
    fine_to_coarse: dict[Hashable, Hashable] = {}
    for state in domain:
        f = fine[state]
        c = coarse[state]
        previous = fine_to_coarse.setdefault(f, c)
        if previous != c:
            raise ValueError("fine partition does not refine coarse partition")
        coarse_to_fine.setdefault(c, set()).add(f)
    return {coarse_label: len(fine_labels) for coarse_label, fine_labels in coarse_to_fine.items()}


def repair_support_summary(
    states: Iterable[State], fine: Partition, coarse: Partition
) -> dict[str, object]:
    """Return local width, active support, class gain and repair spectrum."""

    domain = _domain(states)
    sizes = local_split_sizes(domain, fine, coarse)
    values = tuple(sizes.values())
    maximum = max(values)
    active_support = sum(size > 1 for size in values)
    coarse_classes = len(values)
    fine_classes = sum(values)
    class_gain = fine_classes - coarse_classes

    spectrum = tuple(
        sum(comb(size, order) for size in values)
        for order in range(1, maximum + 1)
    )
    pair_ambiguity = spectrum[1] if maximum >= 2 else 0

    if active_support > class_gain:
        raise AssertionError("each active coarse block must create at least one extra fine class")
    if class_gain > (maximum - 1) * active_support:
        raise AssertionError("class gain exceeded local-width support bound")
    if active_support > pair_ambiguity:
        raise AssertionError("pair repair spectrum must dominate active support")
    if pair_ambiguity > comb(maximum, 2) * active_support:
        raise AssertionError("pair repair spectrum exceeded width-support bound")

    binary = maximum <= 2
    if binary and not (
        active_support == class_gain == pair_ambiguity
    ):
        raise AssertionError("binary refinement failed exact support/gain/J2 identity")

    return {
        "local_split_sizes": sizes,
        "maximum_local_repair_alphabet": maximum,
        "active_repair_support": active_support,
        "coarse_class_count": coarse_classes,
        "fine_class_count": fine_classes,
        "class_gain": class_gain,
        "repair_spectrum": spectrum,
        "pair_repair_ambiguity": pair_ambiguity,
        "binary_refinement": binary,
    }
