"""Two-dimensional BRC multiplier/vertical square-gap wheel.

Horizontal multiplier states come from the retained BRC (J,R) transport.
For one fixed multiplier, let

    x_0 = ceil(sqrt(m*N)),
    D_0 = x_0**2 - m*N.

The vertical Fermat coordinate is

    x_t = x_0 + t,
    D_t = D_0 + t*(2*x_0+t).

A square hit must satisfy D_t being a quadratic residue modulo every chosen
modulus.  For a first modulus M, this condition is periodic in t modulo M, so
we build one exact offset wheel and enumerate only its support.  A second
modulus is then applied before D_t is materialized as a large integer.

The residue sieve and vertical Fermat recurrence are classical.  The BRC
application here is the typed composition with horizontally transported
root/remainder state and lazy exact materialization after the observer filters.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .brc_multiplier_factor_scan import AdmissibleMultiplierRootState
from .brc_square_gap_prefilter import square_residue_table
from .brc_square_gap_table_46189 import (
    MODULUS as SECOND_MODULUS,
    SQUARE_RESIDUE_TABLE as SECOND_TABLE,
)

SHORT_WHEEL_MODULUS = 1008
LONG_WHEEL_MODULUS = 20160
ADAPTIVE_WHEEL_THRESHOLD = 150_000


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _table_contains(table: bytes, modulus: int, value: int) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


@dataclass(frozen=True)
class VerticalBRCState:
    n: int
    multiplier: int
    base_x: int
    base_gap: int

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        _require_natural("base_x", self.base_x)
        _require_natural("base_gap", self.base_gap)
        if self.base_x * self.base_x - self.multiplier * self.n != self.base_gap:
            raise ValueError("vertical base state failed exact reconstruction")
        if self.base_x > 0 and (self.base_x - 1) * (self.base_x - 1) >= self.multiplier * self.n:
            raise ValueError("base_x must be the ceiling square-root coordinate")


@dataclass(frozen=True)
class VerticalResidueWheel:
    modulus: int
    offsets: tuple[int, ...]

    def __post_init__(self) -> None:
        _require_positive("modulus", self.modulus)
        if any(not 0 <= value < self.modulus for value in self.offsets):
            raise ValueError("wheel offsets must lie in one residue period")
        if tuple(sorted(set(self.offsets))) != self.offsets:
            raise ValueError("wheel offsets must be unique and sorted")

    @property
    def support_size(self) -> int:
        return len(self.offsets)

    @property
    def support_fraction(self) -> tuple[int, int]:
        return self.support_size, self.modulus


@dataclass(frozen=True)
class VerticalSquareCandidate:
    t: int
    x: int
    gap: int

    def __post_init__(self) -> None:
        _require_natural("t", self.t)
        _require_natural("x", self.x)
        _require_natural("gap", self.gap)


def vertical_state_from_multiplier_state(
    state: AdmissibleMultiplierRootState,
) -> VerticalBRCState:
    if state.remainder == 0:
        x = state.root
        gap = 0
    else:
        x = state.root + 1
        gap = 2 * state.root + 1 - state.remainder
    return VerticalBRCState(
        n=state.n,
        multiplier=state.multiplier,
        base_x=x,
        base_gap=gap,
    )


def vertical_gap_at(state: VerticalBRCState, t: int) -> int:
    """Exact D_t without iterating through earlier vertical positions."""
    _require_natural("t", t)
    return state.base_gap + t * (2 * state.base_x + t)


def vertical_next_gap(x: int, gap: int) -> tuple[int, int]:
    """Classical exact vertical update D_{t+1}=D_t+2*x_t+1."""
    _require_natural("x", x)
    _require_natural("gap", gap)
    return x + 1, gap + 2 * x + 1


def vertical_residue_wheel(
    state: VerticalBRCState, modulus: int
) -> VerticalResidueWheel:
    """Build the exact first-stage t-residue wheel for one multiplier state.

    The predicate is periodic because x_{t+M} == x_t (mod M).  Hence every
    exact square hit must have t mod M in the returned support.
    """
    _require_positive("modulus", modulus)
    table = square_residue_table(modulus)
    target_residue = (state.multiplier * state.n) % modulus
    x0 = state.base_x % modulus
    offsets = tuple(
        t
        for t in range(modulus)
        if _table_contains(
            table,
            modulus,
            ((x0 + t) * (x0 + t) - target_residue) % modulus,
        )
    )
    return VerticalResidueWheel(modulus=modulus, offsets=offsets)


def adaptive_first_wheel_modulus(t_limit: int) -> int:
    """Finite-benchmark policy, not a mathematical theorem."""
    _require_positive("t_limit", t_limit)
    return SHORT_WHEEL_MODULUS if t_limit < ADAPTIVE_WHEEL_THRESHOLD else LONG_WHEEL_MODULUS


def vertical_square_candidates(
    state: VerticalBRCState,
    t_limit: int,
    *,
    first_modulus: int | None = None,
) -> tuple[VerticalSquareCandidate, ...]:
    """Return candidates passing both residue stages, materializing D_t lazily.

    Rejected offsets never require an exact large-integer D_t construction.
    Every exact square D_t is retained because both residue tests are necessary
    conditions for squarehood.
    """
    _require_positive("t_limit", t_limit)
    modulus = adaptive_first_wheel_modulus(t_limit) if first_modulus is None else first_modulus
    wheel = vertical_residue_wheel(state, modulus)
    target_second = (state.multiplier * state.n) % SECOND_MODULUS
    x0_second = state.base_x % SECOND_MODULUS
    candidates: list[VerticalSquareCandidate] = []

    for base in range(0, t_limit, modulus):
        for offset in wheel.offsets:
            t = base + offset
            if t >= t_limit:
                break
            x_second = (x0_second + t) % SECOND_MODULUS
            second_gap = (x_second * x_second - target_second) % SECOND_MODULUS
            if not _table_contains(SECOND_TABLE, SECOND_MODULUS, second_gap):
                continue
            gap = vertical_gap_at(state, t)
            candidates.append(
                VerticalSquareCandidate(t=t, x=state.base_x + t, gap=gap)
            )
    return tuple(candidates)


def first_vertical_factor_witness(
    state: VerticalBRCState,
    t_limit: int,
    *,
    first_modulus: int | None = None,
) -> tuple[int, int] | None:
    """Return (factor,t) on the classical vertical difference-of-squares surface."""
    for candidate in vertical_square_candidates(
        state, t_limit, first_modulus=first_modulus
    ):
        root = isqrt(candidate.gap)
        if root * root != candidate.gap:
            continue
        for term in (candidate.x - root, candidate.x + root):
            factor = gcd(term, state.n)
            if 1 < factor < state.n:
                return factor, candidate.t
    return None


__all__ = [
    "SHORT_WHEEL_MODULUS",
    "LONG_WHEEL_MODULUS",
    "ADAPTIVE_WHEEL_THRESHOLD",
    "VerticalBRCState",
    "VerticalResidueWheel",
    "VerticalSquareCandidate",
    "vertical_state_from_multiplier_state",
    "vertical_gap_at",
    "vertical_next_gap",
    "vertical_residue_wheel",
    "adaptive_first_wheel_modulus",
    "vertical_square_candidates",
    "first_vertical_factor_witness",
]
