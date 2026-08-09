"""Actual lower-band root images for the P017 square basin.

Unlike the two-point candidate pair used by L052, this module keeps the exact
cofactor window before applying the square-root coordinate. It is the
executable companion to L055.
"""

from __future__ import annotations

from math import isqrt

from .quotient_window import IntegerWindow, square_basin_window


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def lower_band_primes(k: int) -> tuple[int, ...]:
    """Primes satisfying the P017 lower-band condition ``p^2 < 2k``."""

    if k < 1:
        raise ValueError("k must be positive")
    limit = isqrt(2 * k - 1)
    return tuple(p for p in range(2, limit + 1) if is_prime(p))


def actual_root_image_of_window(window: IntegerWindow | None) -> frozenset[int]:
    """Exact image of an integer interval under floor square root."""

    if window is None:
        return frozenset()
    return frozenset(range(isqrt(window.lo), isqrt(window.hi) + 1))


def actual_root_image(k: int, prime: int) -> frozenset[int]:
    """Actual square-root image of the exact P017 quotient window for ``prime``."""

    return actual_root_image_of_window(square_basin_window(k, prime))


def actual_lower_band_root_images(k: int) -> dict[int, frozenset[int]]:
    return {p: actual_root_image(k, p) for p in lower_band_primes(k)}


def actual_lower_band_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[int]], ...]:
    images = actual_lower_band_root_images(k)
    primes = tuple(images)
    overlaps: list[tuple[int, int, frozenset[int]]] = []
    for i, p in enumerate(primes):
        for r in primes[i + 1 :]:
            common = images[p] & images[r]
            if common:
                overlaps.append((p, r, common))
    return tuple(overlaps)


def actual_lower_band_root_images_disjoint(k: int) -> bool:
    return not actual_lower_band_overlaps(k)
