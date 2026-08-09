"""Minimal repair for lower-band P017 realized root-shell identification.

The raw cofactor windows are arithmetic envelopes.  A true least-prime shell
also satisfies the p-roughness/admissibility condition.  This module computes
repair multiplicity on those actually realized shell states.

The uniform threshold bit

    beta_k(q) = 1[q > floor(k(k+2)/3)]

is always the p=2 shell indicator for k>=4.  It is therefore informative at
many k values, but it is task-necessary as a root-shell repair only when an
actual root fiber contains both p=2 and p=3 shell states: exactly k=5 and k=8.
"""

from __future__ import annotations

from math import isqrt

from .factor_precision import first_factor_shell
from .p017_actual_root_separation import lower_band_primes
from .task_precision_refinement import minimal_repair_alphabet_size


TaggedState = tuple[int, int]


def p2_repair_threshold(k: int) -> int:
    """Largest raw cofactor compatible with any shell p>=3."""

    if k < 1:
        raise ValueError("k must be positive")
    return k * (k + 2) // 3


def p2_shell_bit(k: int, cofactor: int) -> int:
    """Return the uniform p=2 indicator ``1[q > floor(k(k+2)/3)]``."""

    if k < 1:
        raise ValueError("k must be positive")
    if cofactor < 0:
        raise ValueError("cofactor must be nonnegative")
    return int(cofactor > p2_repair_threshold(k))


def lower_band_tagged_states(k: int) -> tuple[TaggedState, ...]:
    """Actually realized tagged states ``(least_prime, q)`` in the lower band."""

    states: list[TaggedState] = []
    for prime in lower_band_primes(k):
        states.extend((prime, n // prime) for n in first_factor_shell(k, prime))
    return tuple(states)


def uniform_repaired_root_state(k: int, cofactor: int) -> tuple[int, int]:
    """Root plus the uniform p=2 feature bit."""

    return isqrt(cofactor), p2_shell_bit(k, cofactor)


def minimal_repair_symbol(k: int, cofactor: int) -> int:
    """A minimum-alphabet root-shell repair for the realized lower band.

    Actual root-shell ambiguity occurs only at k=5 and k=8.  Elsewhere a
    constant repair symbol is sufficient and is strictly smaller than carrying
    the otherwise informative p=2 feature.
    """

    if k < 4:
        raise ValueError("the theorem is stated for k>=4")
    if cofactor < 0:
        raise ValueError("cofactor must be nonnegative")
    if k in {5, 8}:
        return p2_shell_bit(k, cofactor)
    return 0


def minimally_repaired_root_state(k: int, cofactor: int) -> tuple[int, int]:
    return isqrt(cofactor), minimal_repair_symbol(k, cofactor)


def _images(
    k: int, state_fn,
) -> dict[int, frozenset[tuple[int, int]]]:
    result: dict[int, set[tuple[int, int]]] = {}
    for prime, cofactor in lower_band_tagged_states(k):
        result.setdefault(prime, set()).add(state_fn(k, cofactor))
    return {prime: frozenset(images) for prime, images in result.items()}


def uniform_repaired_root_images(k: int) -> dict[int, frozenset[tuple[int, int]]]:
    return _images(k, uniform_repaired_root_state)


def minimally_repaired_root_images(k: int) -> dict[int, frozenset[tuple[int, int]]]:
    return _images(k, minimally_repaired_root_state)


def _overlaps(
    images: dict[int, frozenset[tuple[int, int]]],
) -> tuple[tuple[int, int, frozenset[tuple[int, int]]], ...]:
    primes = tuple(images)
    overlaps: list[tuple[int, int, frozenset[tuple[int, int]]]] = []
    for i, left in enumerate(primes):
        for right in primes[i + 1 :]:
            common = images[left] & images[right]
            if common:
                overlaps.append((left, right, frozenset(common)))
    return tuple(overlaps)


def uniform_repaired_root_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[tuple[int, int]]], ...]:
    return _overlaps(uniform_repaired_root_images(k))


def minimally_repaired_root_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[tuple[int, int]]], ...]:
    return _overlaps(minimally_repaired_root_images(k))


def root_shell_split_multiplicities(k: int) -> dict[int, int]:
    """Number of realized shell labels inside each unrepaired root fiber."""

    roots: dict[int, set[int]] = {}
    for prime, cofactor in lower_band_tagged_states(k):
        roots.setdefault(isqrt(cofactor), set()).add(prime)
    return {root: len(primes) for root, primes in roots.items()}


def minimal_root_shell_repair_alphabet_size(k: int) -> int:
    """Exact minimum repair alphabet while retaining the root coordinate."""

    states = lower_band_tagged_states(k)
    if not states:
        return 1
    coarse = {state: isqrt(state[1]) for state in states}
    target = {state: (isqrt(state[1]), state[0]) for state in states}
    return minimal_repair_alphabet_size(states, target, coarse)


def p2_bit_matches_shell(k: int) -> bool:
    """Whether the uniform threshold bit equals the p=2 flag on actual states."""

    if k < 4:
        raise ValueError("the theorem is stated for k>=4")
    return all(
        p2_shell_bit(k, cofactor) == int(prime == 2)
        for prime, cofactor in lower_band_tagged_states(k)
    )
