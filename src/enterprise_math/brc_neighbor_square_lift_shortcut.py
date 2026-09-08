"""Exact N-dependent multiplier probes from local square divisors.

Unit-distance parent law
========================
If

    N = a^2*t + epsilon,   epsilon in {+1,-1},

set ``m = 2*a - epsilon``.  Then identically

    m*N = a^2*(m*t + 1) - (a-epsilon)^2.

General local-distance law
==========================
More generally, for positive distance d,

    N = a^2*t + epsilon*d,
    m = 2*a - epsilon*d,

one has

    m*N = a^2*(m*t + 1) - (a-epsilon*d)^2.

Thus squarehood of ``m*t+1`` gives an exact fixed-gap multiplier-Fermat/BRC
witness.  The useful opportunistic specialization uses power-of-two square
divisors of nearby N±d values.

A bounded local distance window can itself be compressed.  Suppose a power of
two ``a0=2^k`` satisfies

    2*(a0/2) + D <= H < 2*a0 + D,
    2*D < a0^2.

Then no lower power-of-two square level can induce a multiplier above horizon H,
and modulo ``a0^2`` there is at most one signed distance ``1<=d<=D`` for which
``a0^2 | N±d``.  If that unique low-bit distance is absent, no higher square
level can reintroduce one.  Therefore all beyond-H power-of-two candidates in
the whole radius-D neighborhood are located with one low-bit mask and, on a
hit, one v2 computation; no scan over d is required.

These are specializations of classical multiplier-Fermat/difference-of-squares,
not new factorization principles.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .brc_square_gap_cascade import passes_square_residue_cascade


def _require_odd_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1 or n % 2 == 0:
        raise ValueError("n must be an odd integer greater than one")


def valuation_two(value: int) -> tuple[int, int]:
    """Return ``(v2(value), odd_part)`` for a positive integer."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    exponent = 0
    odd = value
    while odd % 2 == 0:
        odd //= 2
        exponent += 1
    return exponent, odd


@dataclass(frozen=True, slots=True)
class NeighborSquareLiftProbe:
    """Exact unit-distance N±1 shortcut result."""

    n: int
    epsilon: int
    square_root_divisor: int
    quotient: int
    multiplier: int
    square_test_value: int
    passed_residue_filter: bool
    square_root: int | None
    proper_factor: int | None

    @property
    def square_hit(self) -> bool:
        return self.square_root is not None

    @property
    def factor_hit(self) -> bool:
        return self.proper_factor is not None

    @property
    def fixed_gap_root(self) -> int:
        return abs(self.square_root_divisor - self.epsilon)


@dataclass(frozen=True, slots=True)
class NeighborDistanceSquareLiftProbe:
    """Exact local-distance N±d shortcut result."""

    n: int
    distance: int
    epsilon: int
    square_root_divisor: int
    quotient: int
    multiplier: int
    square_test_value: int
    passed_residue_filter: bool
    square_root: int | None
    proper_factor: int | None

    @property
    def square_hit(self) -> bool:
        return self.square_root is not None

    @property
    def factor_hit(self) -> bool:
        return self.proper_factor is not None

    @property
    def fixed_gap_root(self) -> int:
        return abs(self.square_root_divisor - self.epsilon * self.distance)


def neighbor_distance_square_parameters(
    n: int,
    square_root_divisor: int,
    distance: int,
    epsilon: int,
) -> tuple[int, int, int]:
    """Return ``(t,m,z)`` for the exact local-distance identity.

    Requires ``a^2 | n-epsilon*d`` and positive ``m=2a-epsilon*d``.  The
    returned values satisfy

        n = a^2*t + epsilon*d,
        m = 2*a - epsilon*d,
        z = m*t + 1,
        m*n = a^2*z - (a-epsilon*d)^2.
    """
    _require_odd_n(n)
    if epsilon not in (-1, 1):
        raise ValueError("epsilon must be +1 or -1")
    if isinstance(distance, bool) or not isinstance(distance, int) or distance <= 0:
        raise ValueError("distance must be a positive integer")
    if (
        isinstance(square_root_divisor, bool)
        or not isinstance(square_root_divisor, int)
        or square_root_divisor < 2
    ):
        raise ValueError("square_root_divisor must be an integer >= 2")

    a = square_root_divisor
    shifted = n - epsilon * distance
    square = a * a
    if shifted <= 0 or shifted % square:
        raise ValueError("a^2 must divide n-epsilon*distance")

    t = shifted // square
    m = 2 * a - epsilon * distance
    if m <= 0:
        raise ValueError("induced multiplier must be positive")
    z = m * t + 1
    if m * n != square * z - (a - epsilon * distance) ** 2:
        raise AssertionError("neighbor-distance identity reconstruction failed")
    return t, m, z


def neighbor_square_parameters(
    n: int,
    square_root_divisor: int,
    epsilon: int,
) -> tuple[int, int, int]:
    """Backward-compatible unit-distance ``(t,m,z)`` helper."""
    return neighbor_distance_square_parameters(
        n, square_root_divisor, 1, epsilon
    )


def probe_neighbor_distance_square_lift(
    n: int,
    square_root_divisor: int,
    distance: int,
    epsilon: int,
    *,
    residue_profile: str = "BALANCED",
) -> NeighborDistanceSquareLiftProbe:
    """Run one exact local-distance fixed-gap square-completion probe."""
    t, m, z = neighbor_distance_square_parameters(
        n, square_root_divisor, distance, epsilon
    )
    passed = passes_square_residue_cascade(z, residue_profile)
    if not passed:
        return NeighborDistanceSquareLiftProbe(
            n,
            distance,
            epsilon,
            square_root_divisor,
            t,
            m,
            z,
            False,
            None,
            None,
        )

    root = isqrt(z)
    if root * root != z:
        return NeighborDistanceSquareLiftProbe(
            n,
            distance,
            epsilon,
            square_root_divisor,
            t,
            m,
            z,
            True,
            None,
            None,
        )

    a = square_root_divisor
    center = a * root
    gap_root = abs(a - epsilon * distance)
    left = center - gap_root
    right = center + gap_root
    if left * right != m * n:
        raise AssertionError("difference-of-squares witness failed")

    factor = gcd(left, n)
    if not 1 < factor < n:
        factor = gcd(right, n)
    proper = factor if 1 < factor < n else None
    return NeighborDistanceSquareLiftProbe(
        n,
        distance,
        epsilon,
        a,
        t,
        m,
        z,
        True,
        root,
        proper,
    )


def probe_neighbor_square_lift(
    n: int,
    square_root_divisor: int,
    epsilon: int,
    *,
    residue_profile: str = "BALANCED",
) -> NeighborSquareLiftProbe:
    """Run the backward-compatible N±1 shortcut."""
    probe = probe_neighbor_distance_square_lift(
        n,
        square_root_divisor,
        1,
        epsilon,
        residue_profile=residue_profile,
    )
    return NeighborSquareLiftProbe(
        probe.n,
        probe.epsilon,
        probe.square_root_divisor,
        probe.quotient,
        probe.multiplier,
        probe.square_test_value,
        probe.passed_residue_filter,
        probe.square_root,
        probe.proper_factor,
    )


def power2_neighbor_square_candidates(
    n: int,
    *,
    min_multiplier: int = 1,
    all_levels: bool = False,
) -> tuple[tuple[int, int, int], ...]:
    """Return cheap N±1 power-of-two candidates as ``(epsilon,a,m)``."""
    _require_odd_n(n)
    if min_multiplier <= 0:
        raise ValueError("min_multiplier must be positive")
    out: list[tuple[int, int, int]] = []
    for epsilon in (1, -1):
        shifted = n - epsilon
        if shifted <= 0:
            continue
        exponent, _ = valuation_two(shifted)
        max_k = exponent // 2
        if max_k < 1:
            continue
        levels = range(1, max_k + 1) if all_levels else (max_k,)
        for k in levels:
            a = 1 << k
            m = 2 * a - epsilon
            if m >= min_multiplier:
                out.append((epsilon, a, m))
    out.sort(key=lambda item: item[2])
    return tuple(out)


def try_power2_neighbor_square_shortcuts(
    n: int,
    *,
    ordinary_horizon: int = 100,
    all_levels: bool = False,
    residue_profile: str = "BALANCED",
) -> tuple[NeighborSquareLiftProbe, ...]:
    """Probe only N±1 multipliers beyond the ordinary horizon."""
    if ordinary_horizon <= 0:
        raise ValueError("ordinary_horizon must be positive")
    return tuple(
        probe_neighbor_square_lift(
            n, a, epsilon, residue_profile=residue_profile
        )
        for epsilon, a, _ in power2_neighbor_square_candidates(
            n,
            min_multiplier=ordinary_horizon + 1,
            all_levels=all_levels,
        )
    )


def compressed_neighbor_distance_start_level(
    ordinary_horizon: int,
    max_distance: int,
) -> int | None:
    """Return the first power-of-two root level with exact distance compression.

    For ``a=2^k`` the conditions are

        2*(a/2)+D <= H < 2*a+D,
        2*D < a^2.

    The first inequality proves every lower power-of-two level has multiplier at
    most H even in its most favorable signed distance.  The second makes the
    signed residue ``N ≡ ±d (mod a^2)``, ``1<=d<=D``, unique.

    ``None`` means this exact one-residue compression does not cover the entire
    requested (H,D) regime; callers should use another strategy rather than
    silently dropping possible lower-level candidates.
    """
    if ordinary_horizon <= 0 or max_distance <= 0:
        raise ValueError("ordinary_horizon/max_distance must be positive")
    limit = (ordinary_horizon + max_distance).bit_length() + 3
    for k in range(1, limit + 1):
        a = 1 << k
        previous_a = a >> 1
        if (
            2 * previous_a + max_distance <= ordinary_horizon
            and ordinary_horizon < 2 * a + max_distance
            and 2 * max_distance < a * a
        ):
            return k
    return None


def compressed_power2_neighbor_distance_candidates(
    n: int,
    *,
    ordinary_horizon: int = 100,
    max_distance: int = 64,
    all_levels: bool = False,
) -> tuple[tuple[int, int, int, int], ...]:
    """Locate all/maximum power-of-two candidates in a whole local window.

    Returns tuples ``(distance, epsilon, a, m)``.  Under the certified start
    condition, **all** beyond-horizon power-of-two candidates for
    ``1<=distance<=max_distance`` share one unique signed distance determined by
    a single low-bit mask at the start modulus.  If that distance is outside the
    window, the exact result is empty and no larger square level can revive it.

    With ``all_levels=True`` every beyond-horizon square level on that unique
    signed neighbor is returned.  The default keeps only the largest level as a
    lowest-overhead opportunistic probe.
    """
    _require_odd_n(n)
    if max_distance >= n:
        raise ValueError("max_distance must be smaller than n")
    k0 = compressed_neighbor_distance_start_level(
        ordinary_horizon, max_distance
    )
    if k0 is None:
        return ()

    a0 = 1 << k0
    modulus = a0 * a0
    residue = n & (modulus - 1)
    if residue <= modulus - residue:
        distance = residue
        epsilon = 1
    else:
        distance = modulus - residue
        epsilon = -1

    # n is odd while modulus is even, so distance=0 cannot occur.
    if distance <= 0 or distance > max_distance:
        return ()

    shifted = n - epsilon * distance
    exponent, _ = valuation_two(shifted)
    max_k = exponent // 2
    if max_k < k0:
        raise AssertionError("unique distance failed its start-level divisibility")

    levels = range(k0, max_k + 1) if all_levels else (max_k,)
    out: list[tuple[int, int, int, int]] = []
    for k in levels:
        a = 1 << k
        multiplier = 2 * a - epsilon * distance
        if multiplier > ordinary_horizon:
            out.append((distance, epsilon, a, multiplier))
    return tuple(out)


def try_compressed_power2_neighbor_distance_shortcuts(
    n: int,
    *,
    ordinary_horizon: int = 100,
    max_distance: int = 64,
    all_levels: bool = False,
    residue_profile: str = "BALANCED",
) -> tuple[NeighborDistanceSquareLiftProbe, ...]:
    """Probe a whole radius-D neighborhood without scanning its distances."""
    return tuple(
        probe_neighbor_distance_square_lift(
            n,
            a,
            distance,
            epsilon,
            residue_profile=residue_profile,
        )
        for distance, epsilon, a, _ in compressed_power2_neighbor_distance_candidates(
            n,
            ordinary_horizon=ordinary_horizon,
            max_distance=max_distance,
            all_levels=all_levels,
        )
    )


__all__ = [
    "NeighborSquareLiftProbe",
    "NeighborDistanceSquareLiftProbe",
    "valuation_two",
    "neighbor_square_parameters",
    "neighbor_distance_square_parameters",
    "probe_neighbor_square_lift",
    "probe_neighbor_distance_square_lift",
    "power2_neighbor_square_candidates",
    "try_power2_neighbor_square_shortcuts",
    "compressed_neighbor_distance_start_level",
    "compressed_power2_neighbor_distance_candidates",
    "try_compressed_power2_neighbor_distance_shortcuts",
]
