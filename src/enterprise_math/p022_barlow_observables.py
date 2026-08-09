"""Finite shell observables used to compare Barlow precision languages.

These helpers deliberately expose several different summaries of the same
rooted shell.  They are not treated as a linear precision scale: explicit P022
counterexamples show cardinality and total path multiplicity are incomparable,
while richer spectra refine some but not all coordinate-sensitive languages.
"""

from __future__ import annotations

from collections import Counter

from .p022_barlow_coordination import barlow_shell_vertex_count_from_extreme_imbalances
from .p022_barlow_growth import barlow_shell_total_geodesic_paths_closed
from .p022_barlow_stacking import (
    BarlowPoint,
    StackingPattern,
    barlow_geodesic_path_count,
    barlow_shell,
    stacking_prefix_imbalance,
)

MultiplicitySpectrum = tuple[tuple[int, int], ...]
LayerMultiplicitySpectrum = tuple[tuple[int, MultiplicitySpectrum], ...]


def shell_cardinality(radius: int, pattern: StackingPattern) -> int:
    """Whole-shell vertex count using the exact quadratic drift formula."""
    return barlow_shell_vertex_count_from_extreme_imbalances(
        radius,
        stacking_prefix_imbalance(pattern, radius),
        stacking_prefix_imbalance(pattern, -radius),
    )


def shell_total_geodesic_count(radius: int, pattern: StackingPattern) -> int:
    """Whole-shell total number of shortest paths."""
    return barlow_shell_total_geodesic_paths_closed(radius, pattern)


def shell_multiplicity_spectrum(
    radius: int, pattern: StackingPattern
) -> MultiplicitySpectrum:
    """Histogram ``(shortest_path_count, endpoint_count)`` over one shell."""
    counts: Counter[int] = Counter()
    for point in barlow_shell(radius, pattern):
        counts[barlow_geodesic_path_count(point, pattern)] += 1
    return tuple(sorted(counts.items()))


def layer_resolved_multiplicity_spectrum(
    radius: int, pattern: StackingPattern
) -> LayerMultiplicitySpectrum:
    """Multiplicity spectrum on every horizontal target layer separately."""
    shell = barlow_shell(radius, pattern)
    output = []
    for layer in range(-radius, radius + 1):
        counts: Counter[int] = Counter()
        for point in shell:
            if point[2] == layer:
                counts[barlow_geodesic_path_count(point, pattern)] += 1
        output.append((layer, tuple(sorted(counts.items()))))
    return tuple(output)


def rooted_shell_path_count_function(
    radius: int, pattern: StackingPattern
) -> tuple[tuple[BarlowPoint, int], ...]:
    """Coordinate-labelled shortest-path count function on one rooted shell."""
    return tuple(
        sorted(
            (
                (point, barlow_geodesic_path_count(point, pattern))
                for point in barlow_shell(radius, pattern)
            ),
            key=lambda item: item[0],
        )
    )


def spectrum_recovers_cardinality(spectrum: MultiplicitySpectrum) -> int:
    return sum(endpoint_count for _, endpoint_count in spectrum)


def spectrum_recovers_total_geodesic_count(spectrum: MultiplicitySpectrum) -> int:
    return sum(
        multiplicity * endpoint_count
        for multiplicity, endpoint_count in spectrum
    )


def layer_spectrum_forgets_to_global(
    layer_spectrum: LayerMultiplicitySpectrum,
) -> MultiplicitySpectrum:
    counts: Counter[int] = Counter()
    for _, spectrum in layer_spectrum:
        for multiplicity, endpoint_count in spectrum:
            counts[multiplicity] += endpoint_count
    return tuple(sorted(counts.items()))
