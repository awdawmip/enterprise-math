"""Exact N-dependent multiplier probe from square divisors of N±1.

If

    N = a^2*t + epsilon,   epsilon in {+1,-1},

set m = 2*a - epsilon.  Then identically

    m*N = a^2*(m*t + 1) - (a-epsilon)^2.

Hence a square

    c^2 = m*t + 1

produces the exact difference-of-squares witness

    m*N = (a*c)^2 - (a-epsilon)^2.

The useful opportunistic case is a power-of-two square divisor of N±1.  Its
availability is read from v2(N±1) with shifts only.  When the resulting m lies
beyond the normal bounded multiplier horizon, this gives one cheap N-dependent
probe that would otherwise never be tried.  Misses are passed through the
existing zero-false-negative square-gap residue cascade before any isqrt.

This is a specialization of multiplier-Fermat/BRC square completion, not a new
factorization principle.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .brc_square_gap_cascade import passes_square_residue_cascade


def _require_odd_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1 or n % 2 == 0:
        raise ValueError("n must be an odd integer greater than one")


def valuation_two(value: int) -> tuple[int, int]:
    """Return (v2(value), odd_part) for a positive integer."""
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


def neighbor_square_parameters(
    n: int,
    square_root_divisor: int,
    epsilon: int,
) -> tuple[int, int, int]:
    """Return (t,m,z) for the exact neighbor-square identity.

    Requires ``a^2 | n-epsilon``.  The returned values satisfy

        n = a^2*t + epsilon,
        m = 2*a - epsilon,
        z = m*t + 1,
        m*n = a^2*z - (a-epsilon)^2.
    """
    _require_odd_n(n)
    if epsilon not in (-1, 1):
        raise ValueError("epsilon must be +1 or -1")
    if (
        isinstance(square_root_divisor, bool)
        or not isinstance(square_root_divisor, int)
        or square_root_divisor < 2
    ):
        raise ValueError("square_root_divisor must be an integer >= 2")
    a = square_root_divisor
    square = a * a
    shifted = n - epsilon
    if shifted <= 0 or shifted % square:
        raise ValueError("a^2 must divide n-epsilon")
    t = shifted // square
    m = 2 * a - epsilon
    z = m * t + 1
    if m * n != square * z - (a - epsilon) ** 2:
        raise AssertionError("neighbor-square identity reconstruction failed")
    return t, m, z


def probe_neighbor_square_lift(
    n: int,
    square_root_divisor: int,
    epsilon: int,
    *,
    residue_profile: str = "BALANCED",
) -> NeighborSquareLiftProbe:
    """Run one exact fixed-gap square-completion probe.

    The staged quadratic-residue filter has zero false negatives.  Therefore a
    filter rejection proves that ``z`` is not square; ``isqrt`` is paid only on
    survivors.  If a square witness is found, both difference-of-squares sides
    are gcd-tested against n.
    """
    t, m, z = neighbor_square_parameters(n, square_root_divisor, epsilon)
    passed = passes_square_residue_cascade(z, residue_profile)
    if not passed:
        return NeighborSquareLiftProbe(
            n, epsilon, square_root_divisor, t, m, z, False, None, None
        )

    root = isqrt(z)
    if root * root != z:
        return NeighborSquareLiftProbe(
            n, epsilon, square_root_divisor, t, m, z, True, None, None
        )

    a = square_root_divisor
    center = a * root
    gap_root = abs(a - epsilon)
    left = center - gap_root
    right = center + gap_root
    if left * right != m * n:
        raise AssertionError("difference-of-squares witness failed")

    factor = gcd(left, n)
    if not 1 < factor < n:
        factor = gcd(right, n)
    proper = factor if 1 < factor < n else None
    return NeighborSquareLiftProbe(
        n, epsilon, a, t, m, z, True, root, proper
    )


def power2_neighbor_square_candidates(
    n: int,
    *,
    min_multiplier: int = 1,
    all_levels: bool = False,
) -> tuple[tuple[int, int, int], ...]:
    """Return cheap power-of-two square-divisor probes as (epsilon,a,m).

    For each epsilon, v2(n-epsilon) determines every a=2^k for which
    ``a^2 | n-epsilon``.  ``all_levels=False`` retains only the largest such a
    on each side; this is the lowest-overhead beyond-horizon mode.
    """
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
    """Probe only N-dependent multipliers beyond the ordinary horizon.

    The trigger itself is almost free: it uses v2(n±1).  This function is
    intentionally opportunistic.  It does not replace the ordinary complete
    multiplier scan and a miss changes no mathematical coverage.
    """
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


__all__ = [
    "NeighborSquareLiftProbe",
    "valuation_two",
    "neighbor_square_parameters",
    "probe_neighbor_square_lift",
    "power2_neighbor_square_candidates",
    "try_power2_neighbor_square_shortcuts",
]
