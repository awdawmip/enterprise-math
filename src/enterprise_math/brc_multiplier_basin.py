"""Exact multiplier-induced square-root BRC basin calculus.

This module is a typed subtool of the canonical BRC family. It studies the
integer map ``n -> multiplier * n`` under square-root collapse while retaining
root index, exact remainder, target-basin support, and unit-weight branch
multiplicity.

All arithmetic is integer-only. Positive Weighted-BRC is used only for
multiplicity bookkeeping; Boolean support and provenance are not identified.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .brc_weighted import CWMState
from .core import integer_nth_root


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def is_square(value: int) -> bool:
    """Return whether a non-negative integer is a perfect square."""
    _require_natural("value", value)
    root = integer_nth_root(value, 2)
    return root * root == value


def squarefree_decomposition(multiplier: int) -> tuple[int, int]:
    """Return the canonical pair ``(a,d)`` with multiplier ``= a**2 * d``.

    ``d`` is squarefree. The implementation is an exact reference routine and
    intentionally uses trial division rather than claiming a fast factorizer.
    """
    _require_positive("multiplier", multiplier)
    remaining = multiplier
    square_part = 1
    kernel = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            square_part *= prime ** (exponent // 2)
            if exponent % 2:
                kernel *= prime
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        kernel *= remaining
    if square_part * square_part * kernel != multiplier:
        raise AssertionError("squarefree decomposition failed reconstruction")
    return square_part, kernel


@dataclass(frozen=True)
class BRCCostState:
    """Exact downward and next-square edit costs after multiplication."""

    n: int
    multiplier: int
    target_value: int
    target_root: int
    subtraction_cost: int
    addition_cost: int

    @property
    def target_basin_width(self) -> int:
        return 2 * self.target_root + 1


@dataclass(frozen=True)
class TargetMultiplicity:
    """One target root together with its exact source interval and multiplicity."""

    target_root: int
    source_n_min: int
    source_n_max: int
    count: int

    @property
    def cwm(self) -> CWMState:
        return CWMState(self.count, Fraction(self.count, 1), Fraction(1, 1))


@dataclass(frozen=True)
class MultiplierBasinProfile:
    source_root: int
    multiplier: int
    source_n_min: int
    source_n_max: int
    branches: tuple[TargetMultiplicity, ...]

    @property
    def source_count(self) -> int:
        return self.source_n_max - self.source_n_min + 1

    @property
    def target_support(self) -> tuple[int, ...]:
        return tuple(branch.target_root for branch in self.branches)

    @property
    def support_size(self) -> int:
        return len(self.branches)

    @property
    def consecutive_support(self) -> bool:
        support = self.target_support
        return all(right == left + 1 for left, right in zip(support, support[1:]))

    @property
    def total_multiplicity(self) -> int:
        return sum(branch.count for branch in self.branches)


@dataclass(frozen=True)
class SquareMultiplierLaw:
    source_root: int
    square_root_multiplier: int
    source_count: int
    support_size: int
    dense_regime: bool
    quotient: int | None
    remainder: int | None
    branches: tuple[TargetMultiplicity, ...]


@dataclass(frozen=True)
class NonSquareStableSupportLaw:
    source_root: int
    multiplier: int
    floor_sqrt_multiplier: int
    start_root: int
    next_square_floor: int
    beatty_step: int
    endpoint_defect: int
    endpoint_resonance: bool
    support_size: int


@dataclass(frozen=True)
class SquarefreeCompositionState:
    """Exact ``m=a^2 d`` decomposition of one multiplied BRC state."""

    n: int
    multiplier: int
    square_part: int
    squarefree_kernel: int
    kernel_root: int
    kernel_remainder: int
    refinement_phase: int
    target_root: int
    target_remainder: int


def point_cost_state(n: int, multiplier: int) -> BRCCostState:
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    target = multiplier * n
    root = integer_nth_root(target, 2)
    subtraction = target - root * root
    addition = (root + 1) * (root + 1) - target
    state = BRCCostState(
        n=n,
        multiplier=multiplier,
        target_value=target,
        target_root=root,
        subtraction_cost=subtraction,
        addition_cost=addition,
    )
    if state.subtraction_cost + state.addition_cost != state.target_basin_width:
        raise AssertionError("BRC add/sub complement identity failed")
    return state


def multiplier_basin_profile(source_root: int, multiplier: int) -> MultiplierBasinProfile:
    """Push one complete square-root basin through ``n -> multiplier*n`` exactly."""
    _require_natural("source_root", source_root)
    _require_positive("multiplier", multiplier)
    source_min = source_root * source_root
    source_max = (source_root + 1) * (source_root + 1) - 1
    target_min = integer_nth_root(multiplier * source_min, 2)
    target_max = integer_nth_root(multiplier * source_max, 2)
    branches: list[TargetMultiplicity] = []
    for target_root in range(target_min, target_max + 1):
        lower = max(source_min, _ceil_div(target_root * target_root, multiplier))
        upper = min(
            source_max,
            (((target_root + 1) * (target_root + 1) - 1) // multiplier),
        )
        if lower <= upper:
            branches.append(
                TargetMultiplicity(
                    target_root=target_root,
                    source_n_min=lower,
                    source_n_max=upper,
                    count=upper - lower + 1,
                )
            )
    profile = MultiplierBasinProfile(
        source_root=source_root,
        multiplier=multiplier,
        source_n_min=source_min,
        source_n_max=source_max,
        branches=tuple(branches),
    )
    if profile.total_multiplicity != profile.source_count:
        raise AssertionError("target multiplicities do not partition the source basin")
    return profile


def square_multiplier_law(source_root: int, square_root_multiplier: int) -> SquareMultiplierLaw:
    """Exact law for multiplier ``square_root_multiplier**2``.

    Let ``N=2*k+1`` be the source basin size and ``s`` the square-root
    multiplier. The support size is exactly ``min(s,N)``.

    If ``s<=N`` the support is the consecutive block ``sk,...,s(k+1)-1``.
    Writing ``N=q*s+a`` with ``0<=a<s``, every target multiplicity is ``q`` or
    ``q+1`` and exactly ``a`` targets receive ``q+1`` source states.

    If ``s>N`` the map is injective on the N source integers, so every occupied
    target has multiplicity one (with gaps allowed).
    """
    _require_natural("source_root", source_root)
    _require_positive("square_root_multiplier", square_root_multiplier)
    k = source_root
    s = square_root_multiplier
    source_count = 2 * k + 1

    if s <= source_count:
        q, a = divmod(source_count, s)
        thresholds = [
            _ceil_div(2 * s * k * t + t * t, s * s)
            for t in range(s + 1)
        ]
        branches = tuple(
            TargetMultiplicity(
                target_root=s * k + t,
                source_n_min=k * k + thresholds[t],
                source_n_max=k * k + thresholds[t + 1] - 1,
                count=thresholds[t + 1] - thresholds[t],
            )
            for t in range(s)
        )
        counts = tuple(branch.count for branch in branches)
        if any(count not in (q, q + 1) for count in counts):
            raise AssertionError("square multiplier balance law failed")
        if sum(count == q + 1 for count in counts) != a:
            raise AssertionError("square multiplier excess-bin count failed")
        return SquareMultiplierLaw(
            source_root=k,
            square_root_multiplier=s,
            source_count=source_count,
            support_size=s,
            dense_regime=True,
            quotient=q,
            remainder=a,
            branches=branches,
        )

    source_min = k * k
    roots = tuple(
        integer_nth_root(s * s * n, 2)
        for n in range(source_min, (k + 1) * (k + 1))
    )
    if any(right <= left for left, right in zip(roots, roots[1:])):
        raise AssertionError("square multiplier sparse-regime injectivity failed")
    branches = tuple(
        TargetMultiplicity(root, n, n, 1)
        for root, n in zip(roots, range(source_min, (k + 1) * (k + 1)))
    )
    return SquareMultiplierLaw(
        source_root=k,
        square_root_multiplier=s,
        source_count=source_count,
        support_size=source_count,
        dense_regime=False,
        quotient=None,
        remainder=None,
        branches=branches,
    )


def nonsquare_stable_support_law(source_root: int, multiplier: int) -> NonSquareStableSupportLaw:
    """Exact Beatty/Pell support law in the no-skip regime ``m<=4*k**2``.

    For non-square ``m``, set ``q=k+1`` and
    ``T=floor(q*sqrt(m))``, ``D=m*q**2-T**2``. Then the final target root is
    ``T-1`` exactly when ``D<m`` and otherwise ``T``. The support size is

    ``floor((k+1)sqrt(m))-floor(k sqrt(m))+1-1[D<m]``.

    The Beatty increment is one of the two adjacent integers around sqrt(m).
    """
    _require_positive("source_root", source_root)
    _require_positive("multiplier", multiplier)
    k = source_root
    m = multiplier
    root_m = integer_nth_root(m, 2)
    if root_m * root_m == m:
        raise ValueError("multiplier must be non-square")
    if m > 4 * k * k:
        raise ValueError("stable no-skip certificate requires multiplier <= 4*k**2")

    start_root = integer_nth_root(m * k * k, 2)
    q = k + 1
    next_floor = integer_nth_root(m * q * q, 2)
    defect = m * q * q - next_floor * next_floor
    resonance = defect < m
    beatty_step = next_floor - start_root
    if beatty_step not in (root_m, root_m + 1):
        raise AssertionError("Beatty increment escaped the two-value law")
    support_size = beatty_step + 1 - int(resonance)

    profile = multiplier_basin_profile(k, m)
    if not profile.consecutive_support:
        raise AssertionError("stable no-skip condition failed to give consecutive support")
    if profile.support_size != support_size:
        raise AssertionError("Beatty/Pell support formula disagrees with exact basin profile")

    return NonSquareStableSupportLaw(
        source_root=k,
        multiplier=m,
        floor_sqrt_multiplier=root_m,
        start_root=start_root,
        next_square_floor=next_floor,
        beatty_step=beatty_step,
        endpoint_defect=defect,
        endpoint_resonance=resonance,
        support_size=support_size,
    )


def endpoint_resonance_defect(q: int, multiplier: int) -> tuple[int, bool]:
    """Return ``D=m*q^2-floor(q*sqrt(m))^2`` and the event ``0<D<m``.

    For non-square m this event is exactly the generalized-Pell near-square
    condition used by :func:`nonsquare_stable_support_law` once the stable
    no-skip regime is reached.
    """
    _require_positive("q", q)
    _require_positive("multiplier", multiplier)
    t = integer_nth_root(multiplier * q * q, 2)
    defect = multiplier * q * q - t * t
    return defect, 0 < defect < multiplier


def squarefree_composition_state(n: int, multiplier: int) -> SquarefreeCompositionState:
    """Factor the multiplier action into squarefree core plus finite square phase.

    Write ``m=a^2 d`` with squarefree d and first compute
    ``d*n = y^2 + rho``. Then the final BRC root/remainder are

    ``J = a*y + u``
    ``R = a^2*rho - 2*a*y*u - u^2``

    with the finite refinement phase ``0<=u<a``. Thus ``(y,rho)`` is sufficient
    for exact composition, while y alone is generally not.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    a, d = squarefree_decomposition(multiplier)
    kernel_value = d * n
    y = integer_nth_root(kernel_value, 2)
    rho = kernel_value - y * y
    target_root = integer_nth_root(multiplier * n, 2)
    phase = target_root - a * y
    if not 0 <= phase < a:
        raise AssertionError("square refinement phase escaped 0..a-1")
    target_remainder = a * a * rho - 2 * a * y * phase - phase * phase
    if target_remainder != multiplier * n - target_root * target_root:
        raise AssertionError("squarefree composition remainder identity failed")
    if not 0 <= target_remainder <= 2 * target_root:
        raise AssertionError("composed remainder escaped target BRC basin")
    return SquarefreeCompositionState(
        n=n,
        multiplier=multiplier,
        square_part=a,
        squarefree_kernel=d,
        kernel_root=y,
        kernel_remainder=rho,
        refinement_phase=phase,
        target_root=target_root,
        target_remainder=target_remainder,
    )


__all__ = [
    "BRCCostState",
    "TargetMultiplicity",
    "MultiplierBasinProfile",
    "SquareMultiplierLaw",
    "NonSquareStableSupportLaw",
    "SquarefreeCompositionState",
    "is_square",
    "squarefree_decomposition",
    "point_cost_state",
    "multiplier_basin_profile",
    "square_multiplier_law",
    "nonsquare_stable_support_law",
    "endpoint_resonance_defect",
    "squarefree_composition_state",
]
