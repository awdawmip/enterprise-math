"""Negative boundary for local affine/root observations in P017.

PR #150 already shows that one fixed residual affine cell remains locally
admissible through every finite odd-prime wheel.  The newer mirror-product bridge
adds several quotient-root observations.  CG17 shows that those observations do
not remove the local multiplicity problem by themselves.

For one fixed ordered divisor cell (a,b), the three-state observation

    ( R_2((M-r)/a), R_2((M+r)/b), R_3((M^2-r^2)/(ab)) )

has at most 2*2*2=8 possible values over the whole bounded parity-compatible
cell.  Yet the explicit family a=3,b=5,k=30n+16 contains n distinct bounded
parity/divisibility lifts.  Therefore some observation fiber contains at least
ceil(n/8) radii, which is unbounded.

This is deliberately a pre-anchor/pre-primality boundary: it proves that root
geometry cannot replace the anchor and simultaneous-prime arithmetic filters.
It does not claim that all family lifts are exact residual full-core cells.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_cell(k: int, lower_divisor: int, upper_divisor: int) -> None:
    for name, value in (("k", k), ("lower_divisor", lower_divisor), ("upper_divisor", upper_divisor)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if k < 4:
        raise ValueError("k must be at least 4")
    if lower_divisor <= 1 or upper_divisor <= 1:
        raise ValueError("cell divisors must exceed one")
    if lower_divisor % 2 == 0 or upper_divisor % 2 == 0:
        raise ValueError("cell divisors must be odd")
    if lower_divisor * upper_divisor >= k:
        raise ValueError("require lower_divisor*upper_divisor < k")


def affine_parity_lifts(k: int, lower_divisor: int, upper_divisor: int) -> tuple[int, ...]:
    """Return odd bounded radii realizing both declared divisibilities."""
    _require_cell(k, lower_divisor, upper_divisor)
    center = k * (k + 1)
    return tuple(
        radius
        for radius in range(1, k, 2)
        if (center - radius) % lower_divisor == 0
        and (center + radius) % upper_divisor == 0
    )


def affine_root_observation(
    k: int,
    lower_divisor: int,
    upper_divisor: int,
    radius: int,
) -> tuple[int, int, int]:
    """Return the local two-tail square roots plus cubic joint-product root."""
    _require_cell(k, lower_divisor, upper_divisor)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    center = k * (k + 1)
    lower_state = center - radius
    upper_state = center + radius
    if lower_state % lower_divisor or upper_state % upper_divisor:
        raise ValueError("radius does not realize the declared affine cell")

    lower_tail = lower_state // lower_divisor
    upper_tail = upper_state // upper_divisor
    joint_tail = lower_tail * upper_tail
    return (
        integer_nth_root(lower_tail, 2),
        integer_nth_root(upper_tail, 2),
        integer_nth_root(joint_tail, 3),
    )


def affine_root_observation_partition(
    k: int,
    lower_divisor: int,
    upper_divisor: int,
) -> dict[str, object]:
    """CG17: one fixed affine cell has at most eight local root observations.

    The first two coordinates each meet at most two adjacent square-root basins:
    as r ranges across one parent square basin, floor((M-r)/a) and
    floor((M+r)/b) are fixed-divisor quotient images, the same two-basin fact
    formalized in canonical P018 APQ.

    For the cubic joint coordinate put S=ab and Q_r=(M^2-r^2)/S.  Since S<k,

        Q_r > (M-1)^2/(k-1) > k^3,

    so every cubic root is at least k.  If two cubic roots differed by at least
    two, their quotient values would differ by at least

        (t+2)^3-(t+1)^3 > 3k^2,

    while |Q_r-Q_s|=|r^2-s^2|/S<k^2/S<=k^2, contradiction.  Hence the cubic
    coordinate also takes at most two adjacent values.
    """
    lifts = affine_parity_lifts(k, lower_divisor, upper_divisor)
    buckets: dict[tuple[int, int, int], list[int]] = {}
    for radius in lifts:
        observation = affine_root_observation(k, lower_divisor, upper_divisor, radius)
        buckets.setdefault(observation, []).append(radius)

    lower_roots = {key[0] for key in buckets}
    upper_roots = {key[1] for key in buckets}
    cubic_roots = {key[2] for key in buckets}
    if len(lower_roots) > 2:
        raise AssertionError("fixed lower-divisor quotient image used more than two square roots")
    if len(upper_roots) > 2:
        raise AssertionError("fixed upper-divisor quotient image used more than two square roots")
    if len(cubic_roots) > 2:
        raise AssertionError("fixed-product cubic image used more than two root states")
    if len(buckets) > 8:
        raise AssertionError("three-coordinate local root observation exceeded 2*2*2 states")

    max_fiber = max((len(radii) for radii in buckets.values()), default=0)
    lower_bound = (len(lifts) + 7) // 8
    if max_fiber < lower_bound:
        raise AssertionError("pigeonhole observation-fiber lower bound failed")

    return {
        "k": k,
        "lower_divisor": lower_divisor,
        "upper_divisor": upper_divisor,
        "lifts": lifts,
        "lift_count": len(lifts),
        "observations": {key: tuple(value) for key, value in buckets.items()},
        "observation_count": len(buckets),
        "lower_root_count": len(lower_roots),
        "upper_root_count": len(upper_roots),
        "cubic_root_count": len(cubic_roots),
        "max_fiber": max_fiber,
        "pigeonhole_fiber_lower_bound": lower_bound,
    }


def unbounded_affine_root_fiber_family(scale: int) -> dict[str, object]:
    """Explicit CG17 family with n lifts and an observation fiber >=ceil(n/8).

    Put n=scale>=1 and

        k=30n+16,  a=3,  b=5.

    Then M=k(k+1)=2 mod 30.  The two divisibilities plus odd parity reduce to
    the single radius class

        r=23 mod 30.

    The bounded lifts are exactly

        r_t=23+30t,  0<=t<n,

    so there are n of them.  CG17 partitions these n lifts into at most eight
    local root-observation states; one fiber therefore has size at least
    ceil(n/8), proving unbounded radius repair for this local observation
    language before anchor/primality filtering.
    """
    if isinstance(scale, bool) or not isinstance(scale, int) or scale < 1:
        raise ValueError("scale must be a positive integer")
    n = scale
    k = 30 * n + 16
    data = affine_root_observation_partition(k, 3, 5)
    expected = tuple(23 + 30 * t for t in range(n))
    if data["lifts"] != expected:
        raise AssertionError("explicit (3,5) affine family lost its radius progression")
    if int(data["lift_count"]) != n:
        raise AssertionError("explicit affine family lift count is not n")
    if int(data["max_fiber"]) < (n + 7) // 8:
        raise AssertionError("explicit affine family did not realize the unbounded pigeonhole fiber")
    return {
        **data,
        "scale": n,
        "expected_lift_count": n,
    }
