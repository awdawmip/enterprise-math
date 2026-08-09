"""Minimal repair for lower-band P017 root-shell identification.

The exact cofactor windows already separate least-prime shells.  Applying the
integer square root can merge the realized images of the p=2 and p=3 shells at
three small k values.  This module records the canonical one-bit repair used by
P017 L057 and the exact local split multiplicity behind its minimality.
"""

from __future__ import annotations

from math import isqrt

from .p017_actual_root_separation import lower_band_primes
from .quotient_window import square_basin_window
from .task_precision_refinement import minimal_repair_alphabet_size


TaggedState = tuple[int, int]


def p2_repair_threshold(k: int) -> int:
    """Largest cofactor compatible with any shell p>=3."""

    if k < 1:
        raise ValueError("k must be positive")
    return k * (k + 2) // 3


def p2_shell_bit(k: int, cofactor: int) -> int:
    """Return the canonical bit ``1[q > floor(k(k+2)/3)]``."""

    if k < 1:
        raise ValueError("k must be positive")
    if cofactor < 0:
        raise ValueError("cofactor must be nonnegative")
    return int(cofactor > p2_repair_threshold(k))


def lower_band_tagged_states(k: int) -> tuple[TaggedState, ...]:
    """Tagged exact cofactor states ``(least_prime, q)`` in the lower band."""

    states: list[TaggedState] = []
    for prime in lower_band_primes(k):
        window = square_basin_window(k, prime)
        if window is None:
            continue
        states.extend((prime, q) for q in range(window.lo, window.hi + 1))
    return tuple(states)


def repaired_root_state(k: int, cofactor: int) -> tuple[int, int]:
    return isqrt(cofactor), p2_shell_bit(k, cofactor)


def repaired_root_images(k: int) -> dict[int, frozenset[tuple[int, int]]]:
    """Actual repaired-root image of every lower-band prime shell."""

    result: dict[int, set[tuple[int, int]]] = {}
    for prime, cofactor in lower_band_tagged_states(k):
        result.setdefault(prime, set()).add(repaired_root_state(k, cofactor))
    return {prime: frozenset(images) for prime, images in result.items()}


def repaired_root_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[tuple[int, int]]], ...]:
    images = repaired_root_images(k)
    primes = tuple(images)
    overlaps: list[tuple[int, int, frozenset[tuple[int, int]]]] = []
    for i, left in enumerate(primes):
        for right in primes[i + 1 :]:
            common = images[left] & images[right]
            if common:
                overlaps.append((left, right, frozenset(common)))
    return tuple(overlaps)


def root_shell_split_multiplicities(k: int) -> dict[int, int]:
    """Number of shell labels realized in each unrepaired root fiber."""

    roots: dict[int, set[int]] = {}
    for prime, cofactor in lower_band_tagged_states(k):
        roots.setdefault(isqrt(cofactor), set()).add(prime)
    return {root: len(primes) for root, primes in roots.items()}


def minimal_root_shell_repair_alphabet_size(k: int) -> int:
    """Minimum repair alphabet needed while retaining the root coordinate."""

    states = lower_band_tagged_states(k)
    if not states:
        return 1
    coarse = {state: isqrt(state[1]) for state in states}
    target = {state: (isqrt(state[1]), state[0]) for state in states}
    return minimal_repair_alphabet_size(states, target, coarse)


def p2_bit_matches_shell(k: int) -> bool:
    """Finite executable check that the repair bit is exactly the p=2 flag."""

    if k < 4:
        raise ValueError("the theorem is stated for k>=4")
    return all(
        p2_shell_bit(k, cofactor) == int(prime == 2)
        for prime, cofactor in lower_band_tagged_states(k)
    )
