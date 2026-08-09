"""Lower-band root images for exact windows and realized P017 shells.

L055 works first with the exact raw cofactor window

    W_p(k) = [floor(k^2/p)+1, floor(k(k+2)/p)].

A real least-prime shell is the admissible subset of that window whose
cofactors have no prime divisor below p.  Keeping the arithmetic envelope and
its p-rough realizability filter separate prevents exact interval states from
being mislabeled as actually realized shell states.
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


def primes_below(n: int) -> tuple[int, ...]:
    return tuple(p for p in range(2, n) if is_prime(p))


def lower_band_primes(k: int) -> tuple[int, ...]:
    """Primes satisfying the P017 lower-band condition ``p^2 < 2k``."""

    if k < 1:
        raise ValueError("k must be positive")
    limit = isqrt(2 * k - 1)
    return tuple(p for p in range(2, limit + 1) if is_prime(p))


def root_image_of_window(window: IntegerWindow | None) -> frozenset[int]:
    """Exact image of one closed integer window under floor square root."""

    if window is None:
        return frozenset()
    return frozenset(range(isqrt(window.lo), isqrt(window.hi) + 1))


def exact_window_root_image(k: int, prime: int) -> frozenset[int]:
    """Root image of the full exact cofactor window for ``prime``."""

    return root_image_of_window(square_basin_window(k, prime))


def exact_window_lower_band_root_images(k: int) -> dict[int, frozenset[int]]:
    return {p: exact_window_root_image(k, p) for p in lower_band_primes(k)}


def _overlaps(
    images: dict[int, frozenset[int]],
) -> tuple[tuple[int, int, frozenset[int]], ...]:
    primes = tuple(images)
    overlaps: list[tuple[int, int, frozenset[int]]] = []
    for i, p in enumerate(primes):
        for r in primes[i + 1 :]:
            common = images[p] & images[r]
            if common:
                overlaps.append((p, r, common))
    return tuple(overlaps)


def exact_window_lower_band_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[int]], ...]:
    """Cross-prime collisions between exact-window root images."""

    return _overlaps(exact_window_lower_band_root_images(k))


def exact_window_lower_band_root_images_disjoint(k: int) -> bool:
    return not exact_window_lower_band_overlaps(k)


def actual_shell_cofactors(k: int, prime: int) -> frozenset[int]:
    """Cofactors actually realized by the least-prime shell ``prime``.

    For ``n=prime*q`` inside the basin, ``spf(n)=prime`` iff no prime below
    ``prime`` divides ``q``.  Thus the true shell is obtained by filtering the
    exact quotient window with the p-roughness predicate.
    """

    window = square_basin_window(k, prime)
    if window is None:
        return frozenset()
    smaller_primes = primes_below(prime)
    return frozenset(
        q
        for q in range(window.lo, window.hi + 1)
        if all(q % smaller != 0 for smaller in smaller_primes)
    )


def actual_shell_root_image(k: int, prime: int) -> frozenset[int]:
    """Root image actually realized by the least-prime shell ``prime``."""

    return frozenset(isqrt(q) for q in actual_shell_cofactors(k, prime))


def actual_lower_band_root_images(k: int) -> dict[int, frozenset[int]]:
    return {p: actual_shell_root_image(k, p) for p in lower_band_primes(k)}


def actual_lower_band_overlaps(
    k: int,
) -> tuple[tuple[int, int, frozenset[int]], ...]:
    """Cross-prime collisions between actually realized shell root images."""

    return _overlaps(actual_lower_band_root_images(k))


def actual_lower_band_root_images_disjoint(k: int) -> bool:
    return not actual_lower_band_overlaps(k)
