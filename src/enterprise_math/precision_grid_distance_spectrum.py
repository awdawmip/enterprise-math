"""Exact L1 pair-distance spectra for finite product grids.

For one path with ``n`` vertices, the number of ordered coordinate pairs at
distance ``s`` is ``n`` for ``s=0`` and ``2(n-s)`` for ``1<=s<n``.  Cartesian
products multiply these generating polynomials, so finite integer convolution
gives the full ordered L1-distance spectrum of any rectangular grid.

R004 uses the spectrum to count exactly how many state pairs enter the zero
record-overlap region of its threshold-record toy.  The graph/distance counting
is established finite combinatorics; the record interpretation remains a
physical hypothesis.
"""
from __future__ import annotations

from fractions import Fraction
from collections.abc import Sequence


def _side_lengths(side_lengths: Sequence[int]) -> tuple[int, ...]:
    sides = tuple(side_lengths)
    if not sides:
        raise ValueError("at least one grid axis is required")
    if any(
        isinstance(side, bool) or not isinstance(side, int) or side <= 0
        for side in sides
    ):
        raise ValueError("grid side lengths must be positive integers")
    return sides


def axis_ordered_distance_spectrum(size: int) -> tuple[int, ...]:
    sides = _side_lengths((size,))
    n = sides[0]
    return tuple([n, *(2 * (n - distance) for distance in range(1, n))])


def _convolve(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return tuple(output)


def grid_ordered_distance_spectrum(
    side_lengths: Sequence[int],
) -> tuple[int, ...]:
    sides = _side_lengths(side_lengths)
    spectrum = (1,)
    for side in sides:
        spectrum = _convolve(spectrum, axis_ordered_distance_spectrum(side))
    return spectrum


def grid_vertex_count(side_lengths: Sequence[int]) -> int:
    sides = _side_lengths(side_lengths)
    count = 1
    for side in sides:
        count *= side
    return count


def grid_unordered_pair_count(side_lengths: Sequence[int]) -> int:
    vertices = grid_vertex_count(side_lengths)
    return vertices * (vertices - 1) // 2


def grid_unordered_distance_spectrum(
    side_lengths: Sequence[int],
) -> tuple[int, ...]:
    """Return unordered distinct-pair counts, with coefficient zero set to 0."""
    ordered = grid_ordered_distance_spectrum(side_lengths)
    output = [0]
    for count in ordered[1:]:
        if count % 2:
            raise AssertionError("positive-distance ordered pairs must reverse in pairs")
        output.append(count // 2)
    if sum(output) != grid_unordered_pair_count(side_lengths):
        raise AssertionError("distance spectrum must partition unordered pairs")
    return tuple(output)


def grid_zero_overlap_pair_count(
    side_lengths: Sequence[int], record_resolution: int
) -> int:
    if (
        isinstance(record_resolution, bool)
        or not isinstance(record_resolution, int)
        or record_resolution <= 0
    ):
        raise ValueError("record_resolution must be a positive integer")
    spectrum = grid_unordered_distance_spectrum(side_lengths)
    if record_resolution >= len(spectrum):
        return 0
    return sum(spectrum[record_resolution:])


def grid_zero_overlap_pair_fraction(
    side_lengths: Sequence[int], record_resolution: int
) -> Fraction:
    total = grid_unordered_pair_count(side_lengths)
    if total == 0:
        return Fraction(0, 1)
    return Fraction(
        grid_zero_overlap_pair_count(side_lengths, record_resolution), total
    )


def uniform_cube_zero_overlap_fraction(
    side: int, dimension: int, record_resolution: int
) -> Fraction:
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension <= 0:
        raise ValueError("dimension must be a positive integer")
    return grid_zero_overlap_pair_fraction(
        (side,) * dimension, record_resolution
    )
