"""Finite-support reference model for projective precision completion.

The mathematical mother result is topological: surjectivity of every finite
coordinate shadow makes the actual image dense in the full product, but need
not make it equal to the product.  This module supplies the canonical countable
counterexample for binary coordinates: finite-support profiles realize every
finite pattern while omitting all infinite-support completion points.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from itertools import product

Coordinate = Hashable
FiniteSupportProfile = frozenset[Coordinate]


def project_binary_profile(
    profile: FiniteSupportProfile,
    coordinates: Iterable[Coordinate],
) -> tuple[int, ...]:
    """Project one finite-support binary profile onto finitely many coordinates."""

    coords = tuple(coordinates)
    if len(coords) != len(set(coords)):
        raise ValueError("coordinates must be distinct")
    return tuple(int(coordinate in profile) for coordinate in coords)


def realize_finite_binary_pattern(
    pattern: Mapping[Coordinate, int],
) -> FiniteSupportProfile:
    """Return a finite-support profile realizing any finite binary pattern."""

    for value in pattern.values():
        if value not in (0, 1) or isinstance(value, bool):
            raise ValueError("binary pattern values must be integer 0 or 1")
    return frozenset(coordinate for coordinate, value in pattern.items() if value == 1)


def finite_shadow_is_surjective(coordinates: Iterable[Coordinate]) -> bool:
    """Executable audit that every pattern on a finite coordinate set is realized."""

    coords = tuple(coordinates)
    if len(coords) != len(set(coords)):
        raise ValueError("coordinates must be distinct")
    for values in product((0, 1), repeat=len(coords)):
        pattern = dict(zip(coords, values, strict=True))
        profile = realize_finite_binary_pattern(pattern)
        if project_binary_profile(profile, coords) != values:
            return False
    return True


def finite_support_profile_from_ones(ones: Iterable[Coordinate]) -> FiniteSupportProfile:
    """Canonical finite-support profile with the supplied coordinates equal to one."""

    return frozenset(ones)


def profiles_up_to_support_size(
    coordinates: Iterable[Coordinate], maximum_support: int
) -> tuple[FiniteSupportProfile, ...]:
    """Finite truncation of the countable finite-support profile space."""

    coords = tuple(coordinates)
    if len(coords) != len(set(coords)):
        raise ValueError("coordinates must be distinct")
    if maximum_support < 0:
        raise ValueError("maximum_support must be nonnegative")
    result: list[FiniteSupportProfile] = []
    for mask in range(1 << len(coords)):
        support = frozenset(
            coordinate
            for index, coordinate in enumerate(coords)
            if mask & (1 << index)
        )
        if len(support) <= maximum_support:
            result.append(support)
    return tuple(result)
