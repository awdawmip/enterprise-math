"""Exact-integer explorer for R007 scale/collapse descent.

No floating-point root is used.  This module is research evidence, not a stable API.
"""

from __future__ import annotations

from math import comb, gcd
from typing import Callable


def floor_root(n: int, p: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    if p < 1:
        raise ValueError("p must be positive")
    if n < 2 or p == 1:
        return n
    lo, hi = 0, 1
    while hi**p <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def collapse(n: int, p: int) -> int:
    k = floor_root(n, p)
    return k**p


def q(n: int, r: int) -> int:
    if r < 1:
        raise ValueError("r must be positive")
    return n // r


def unsafe_witness(p: int, r: int, t: int = 1) -> tuple[int, int]:
    if p < 2 or r < 2 or t < 1:
        raise ValueError("require p,r >= 2 and t >= 1")
    y = (t * r + 1) ** p
    return y - 1, y


def coarse_future_defect(p: int, r: int, t: int = 1) -> int:
    x, y = unsafe_witness(p, r, t)
    return q(collapse(y, p), r) - q(collapse(x, p), r)


def defect_polynomial(p: int, r: int, t: int = 1) -> int:
    return sum(comb(p, i) * (t**i) * (r ** (i - 1)) for i in range(1, p))


def repair_bit(n: int, p: int, r: int) -> int:
    return int(q(collapse(n, p), r) == q(n, r))


def repair_future_from_bit(a: int, beta: int, p: int, r: int) -> int:
    if beta not in (0, 1):
        raise ValueError("beta must be 0 or 1")
    if beta:
        return a
    return q(collapse(a * r, p), r)


def fiber_repair_values(a: int, p: int, r: int) -> set[int]:
    return {q(collapse(n, p), r) for n in range(a * r, (a + 1) * r)}


def fiber_needs_repair(a: int, p: int, r: int) -> bool:
    left = a * r
    k = floor_root(left, p)
    if k**p == left:
        return False
    next_power = (k + 1) ** p
    return next_power < (a + 1) * r


def projection(m: int, e: int, d: int) -> int:
    if d < 1 or e < 1 or e % d:
        raise ValueError("require positive d|e")
    return m // (e // d)


def relative_lift(m: int, d: int, p: int) -> int:
    """F_d^H for H=C_p: d * C_p(floor(m/d))."""
    return d * collapse(m // d, p)


def root_induced_on_q(a: int, p: int, r: int) -> int:
    return floor_root(a // (r ** (p - 1)), p)


# --- Stage-2: safe-operation monoid and scale-natural residue tower ---------


def is_safe_on_fiber(F: Callable[[int], int], r: int, a: int) -> bool:
    """Finite exact check of q_r-safety on one fiber I_a."""
    values = {q(F(n), r) for n in range(a * r, (a + 1) * r)}
    return len(values) <= 1


def is_safe_on_prefix(F: Callable[[int], int], r: int, fibers: int = 100) -> bool:
    """Finite regression helper, not a proof oracle."""
    return all(is_safe_on_fiber(F, r, a) for a in range(fibers))


def translation_predicted_safe(t: int, r: int) -> bool:
    if t < 0 or r < 1:
        raise ValueError("require t>=0 and r>=1")
    return t % r == 0


def affine_predicted_safe(u: int, v: int, r: int) -> bool:
    """Exact classification for F(n)=u*n+v when r>=2 and u,v>=0."""
    if u < 0 or v < 0 or r < 2:
        raise ValueError("require u,v>=0 and r>=2")
    return u == 0 or (u == 1 and v % r == 0)


def power_map(n: int, p: int) -> int:
    if p < 1:
        raise ValueError("p must be positive")
    return n**p


def power_unsafe_witness(p: int, r: int, t: int = 1) -> tuple[int, int]:
    if p < 2 or r < 2 or t < 1:
        raise ValueError("require p,r>=2 and t>=1")
    return t * r, t * r + 1


def translation_scale_spectrum(steps: list[int], max_r: int | None = None) -> list[int]:
    """Admissible r for a finite translation language.

    If max_r is omitted and some step is nonzero, returns all positive divisors
    of gcd(steps).  If all steps are zero, max_r is required because every r is
    admissible.
    """
    if any(t < 0 for t in steps):
        raise ValueError("steps must be nonnegative")
    g = 0
    for t in steps:
        g = gcd(g, t)
    if g == 0:
        if max_r is None:
            raise ValueError("all-zero language has unbounded spectrum; provide max_r")
        return list(range(1, max_r + 1))
    return [r for r in range(1, g + 1) if g % r == 0]


def residue_zero(d: int, s: int) -> int:
    return 0


def residue_identity(d: int, s: int) -> int:
    return s


def residue_reflect(d: int, s: int) -> int:
    return d - 1 - s


def residue_divide(k: int) -> Callable[[int, int], int]:
    if k < 1:
        raise ValueError("k must be positive")
    return lambda d, s: s // k


def residue_upper_divide(k: int) -> Callable[[int, int], int]:
    if k < 1:
        raise ValueError("k must be positive")
    return lambda d, s: d - 1 - ((d - 1 - s) // k)


def residue_policy_coherent(
    rho: Callable[[int, int], int], d: int, ratio: int, u: int
) -> bool:
    """One exact naturality square in the divisibility residue tower."""
    if d < 1 or ratio < 1:
        raise ValueError("require positive d and ratio")
    e = d * ratio
    if not (0 <= u < e):
        raise ValueError("require 0<=u<d*ratio")
    fine = rho(e, u)
    coarse_input = u // ratio
    coarse = rho(d, coarse_input)
    if not (0 <= fine < e and 0 <= coarse < d):
        return False
    return fine // ratio == coarse


def natural_lift_with_residue(
    m: int,
    d: int,
    H: Callable[[int], int],
    rho: Callable[[int, int], int],
) -> int:
    """F_d(da+s)=d*H(a)+rho_d(s), for a scale-coherent rho."""
    if d < 1:
        raise ValueError("d must be positive")
    a, s = divmod(m, d)
    out_s = rho(d, s)
    if not 0 <= out_s < d:
        raise ValueError("residue policy must return a value in [0,d)")
    return d * H(a) + out_s


def check_natural_lift_square(
    m: int,
    d: int,
    ratio: int,
    H: Callable[[int], int],
    rho: Callable[[int, int], int],
) -> bool:
    e = d * ratio
    lhs = projection(natural_lift_with_residue(m, e, H, rho), e, d)
    rhs = natural_lift_with_residue(projection(m, e, d), d, H, rho)
    return lhs == rhs


# --- Stage-3: inverse-limit cuts and natural clamp retractions -------------


def rational_split_cut(d: int, num: int, den: int, side: str = "right") -> int:
    """Coordinate c_d of a rational split point alpha=num/den in [0,1].

    `right` uses floor(d*alpha) and is unavailable at alpha=1.
    `left` uses ceil(d*alpha)-1 and is unavailable at alpha=0.
    Away from exact rational grid boundaries the two coordinates coincide.
    """
    if d < 1 or den < 1 or not (0 <= num <= den):
        raise ValueError("require d,den>0 and 0<=num<=den")
    if side == "right":
        if num == den:
            raise ValueError("the right copy of endpoint 1 does not exist")
        return (d * num) // den
    if side == "left":
        if num == 0:
            raise ValueError("the left copy of endpoint 0 does not exist")
        return (d * num + den - 1) // den - 1
    raise ValueError("side must be 'left' or 'right'")


def split_cut_coherent(num: int, den: int, side: str, d: int, ratio: int) -> bool:
    if d < 1 or ratio < 1:
        raise ValueError("require d,ratio>0")
    return (
        rational_split_cut(d * ratio, num, den, side) // ratio
        == rational_split_cut(d, num, den, side)
    )


def residue_lower_clamp(cut: Callable[[int], int]) -> Callable[[int, int], int]:
    """rho_d(s)=min(s,c_d) for a coherent residue-tower cut c."""
    return lambda d, s: min(s, cut(d))


def residue_upper_clamp(cut: Callable[[int], int]) -> Callable[[int, int], int]:
    """rho_d(s)=max(s,c_d) for a coherent residue-tower cut c."""
    return lambda d, s: max(s, cut(d))


def residue_interval_clamp(
    lower: Callable[[int], int], upper: Callable[[int], int]
) -> Callable[[int, int], int]:
    """Coordinatewise clamp to a coherent split interval [lower,upper]."""
    def rho(d: int, s: int) -> int:
        lo, hi = lower(d), upper(d)
        if lo > hi:
            raise ValueError("lower cut must not exceed upper cut")
        return min(max(s, lo), hi)
    return rho


def residue_policy_idempotent_on_scale(
    rho: Callable[[int, int], int], d: int
) -> bool:
    return all(rho(d, rho(d, s)) == rho(d, s) for s in range(d))


def residue_policy_downward_on_scale(
    rho: Callable[[int, int], int], d: int
) -> bool:
    return all(rho(d, s) <= s for s in range(d))


def self_check() -> dict[str, int]:
    witness_cases = 0
    fiber_cases = 0
    naturality_cases = 0
    erasure_cases = 0
    root_safe_cases = 0
    safe_monoid_cases = 0
    residue_cases = 0
    scale_spectrum_cases = 0
    split_clamp_cases = 0

    for p in range(2, 7):
        for r in range(2, 20):
            for t in range(1, 20):
                x, y = unsafe_witness(p, r, t)
                assert q(x, r) == q(y, r)
                assert q(collapse(x, p), r) != q(collapse(y, p), r)
                assert coarse_future_defect(p, r, t) == defect_polynomial(p, r, t)
                witness_cases += 1

                z = (t * r) ** p
                a = z // r
                repaired = {
                    (q(n, r), q(collapse(n, p), r))
                    for n in range(z, z + r)
                }
                assert len(repaired) == 1
                assert len(range(z, z + r)) == r
                erasure_cases += 1

    for p in range(2, 6):
        for r in range(2, 50):
            for a in range(0, 500):
                values = fiber_repair_values(a, p, r)
                assert len(values) <= 2
                assert (len(values) == 2) == fiber_needs_repair(a, p, r)
                for n in range(a * r, (a + 1) * r):
                    beta = repair_bit(n, p, r)
                    assert repair_future_from_bit(a, beta, p, r) == q(collapse(n, p), r)
                fiber_cases += 1

    for p in range(2, 6):
        for d in range(1, 10):
            for ratio in range(1, 10):
                e = d * ratio
                for m in range(0, 1000, 17):
                    lhs = projection(relative_lift(m, e, p), e, d)
                    rhs = relative_lift(projection(m, e, d), d, p)
                    assert lhs == rhs
                    assert relative_lift(relative_lift(m, d, p), d, p) == relative_lift(m, d, p)
                    assert relative_lift(m, d, p) <= m
                    naturality_cases += 1

    for p in range(1, 6):
        for r in range(2, 20):
            for n in range(0, 2000, 13):
                lhs = q(floor_root(n, p), r)
                rhs = root_induced_on_q(q(n, r), p, r)
                assert lhs == rhs
                root_safe_cases += 1

    for r in range(2, 15):
        for u in range(0, 5):
            for v in range(0, 3 * r + 1):
                predicted = affine_predicted_safe(u, v, r)
                observed = is_safe_on_prefix(lambda n, u=u, v=v: u * n + v, r, 40)
                assert predicted == observed
                safe_monoid_cases += 1
        for t in range(0, 3 * r + 1):
            assert translation_predicted_safe(t, r) == is_safe_on_prefix(
                lambda n, t=t: n + t, r, 40
            )
            safe_monoid_cases += 1
        for p in range(2, 6):
            x, y = power_unsafe_witness(p, r)
            assert q(x, r) == q(y, r)
            assert q(power_map(x, p), r) != q(power_map(y, p), r)
            safe_monoid_cases += 1

    policies = [
        residue_zero,
        residue_identity,
        residue_reflect,
        residue_divide(2),
        residue_divide(3),
        residue_upper_divide(2),
        residue_upper_divide(3),
    ]
    Hs = [lambda a: a, lambda a: a // 2, lambda a: floor_root(a, 2)]
    for rho in policies:
        for d in range(1, 10):
            for ratio in range(1, 8):
                e = d * ratio
                for u in range(e):
                    assert residue_policy_coherent(rho, d, ratio, u)
                    residue_cases += 1
                for H in Hs:
                    for m in range(0, 400, 17):
                        assert check_natural_lift_square(m, d, ratio, H, rho)
                        residue_cases += 1

    translation_languages = [[6, 10], [12, 18, 30], [7], [0, 24, 36]]
    for steps in translation_languages:
        spectrum = translation_scale_spectrum(steps)
        g = 0
        for t in steps:
            g = gcd(g, t)
        assert spectrum == [r for r in range(1, g + 1) if g % r == 0]
        for r in range(1, max(2, g + 2)):
            observed = all(translation_predicted_safe(t, r) for t in steps)
            assert observed == (g % r == 0)
            scale_spectrum_cases += 1

    # Rational representatives exercise both copies of split rational boundaries.
    split_points = [
        (0, 1, "right"),
        (1, 1, "left"),
        (1, 2, "left"),
        (1, 2, "right"),
        (2, 3, "left"),
        (2, 3, "right"),
        (1, 7, "left"),
        (1, 7, "right"),
    ]
    for num, den, side in split_points:
        cut = lambda d, num=num, den=den, side=side: rational_split_cut(d, num, den, side)
        lower = residue_lower_clamp(cut)
        upper = residue_upper_clamp(cut)
        for d in range(1, 15):
            assert 0 <= cut(d) < d
            assert residue_policy_idempotent_on_scale(lower, d)
            assert residue_policy_idempotent_on_scale(upper, d)
            assert residue_policy_downward_on_scale(lower, d)
            for ratio in range(1, 10):
                assert split_cut_coherent(num, den, side, d, ratio)
                e = d * ratio
                for u in range(e):
                    assert residue_policy_coherent(lower, d, ratio, u)
                    assert residue_policy_coherent(upper, d, ratio, u)
                    split_clamp_cases += 2
                for p in range(2, 5):
                    H = lambda a, p=p: collapse(a, p)
                    for m in range(0, 300, 29):
                        assert check_natural_lift_square(m, d, ratio, H, lower)
                        out = natural_lift_with_residue(m, d, H, lower)
                        assert out <= m
                        out2 = natural_lift_with_residue(out, d, H, lower)
                        assert out2 == out
                        split_clamp_cases += 1

    lo_cut = lambda d: rational_split_cut(d, 1, 3, "right")
    hi_cut = lambda d: rational_split_cut(d, 2, 3, "left")
    corridor = residue_interval_clamp(lo_cut, hi_cut)
    for d in range(1, 15):
        assert residue_policy_idempotent_on_scale(corridor, d)
        for ratio in range(1, 10):
            for u in range(d * ratio):
                assert residue_policy_coherent(corridor, d, ratio, u)
                split_clamp_cases += 1

    return {
        "witness_cases": witness_cases,
        "fiber_cases": fiber_cases,
        "naturality_cases": naturality_cases,
        "erasure_cases": erasure_cases,
        "root_safe_cases": root_safe_cases,
        "safe_monoid_cases": safe_monoid_cases,
        "residue_cases": residue_cases,
        "scale_spectrum_cases": scale_spectrum_cases,
        "split_clamp_cases": split_clamp_cases,
    }


if __name__ == "__main__":
    print(self_check())
