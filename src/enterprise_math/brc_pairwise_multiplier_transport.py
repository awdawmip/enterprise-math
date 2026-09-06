"""Exact pairwise BRC multiplier root/remainder transport.

For fixed positive N, an exact source state

    m*N = J_m**2 + R_m,  0 <= R_m <= 2*J_m

can be transported directly to any target multiplier t without materializing a
new integer square root.  A lower dyadic predictor for sqrt(t/m) gives a root
candidate below the exact target root, followed by a bounded number of ordinary
odd-width BRC basin crossings.

This is a strict extension of the existing multiplier transition / priority
tools.  It is finite integer transport, not a new factoring theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import isqrt
from typing import Protocol

from .brc_multiplier_priority_jump import prioritized_odd_multiplier_order
from .brc_multiplier_transition import initial_multiplier_root_state
from .brc_multiplier_transition_table import (
    MAX_MULTIPLIER,
    fraction_bits_for_n_bits,
)


class MultiplierStateLike(Protocol):
    n: int
    multiplier: int
    root: int
    remainder: int


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_sqrt_ratio(target_multiplier: int, source_multiplier: int) -> int:
    """Return ceil(sqrt(target/source)) exactly using integer comparisons."""
    _require_positive("target_multiplier", target_multiplier)
    _require_positive("source_multiplier", source_multiplier)
    value = isqrt(target_multiplier // source_multiplier)
    if value * value * source_multiplier < target_multiplier:
        value += 1
    return max(1, value)


def pairwise_correction_bound(source_multiplier: int, target_multiplier: int) -> int:
    """A uniform proof bound for the number of upward BRC basin corrections.

    For equal multipliers the bound is zero. Otherwise, if
    beta=sqrt(target/source), the lower predictor misses the exact target root
    by strictly less than beta+3/2. Hence at most ceil(beta)+1 integer basin
    crossings are needed. For target<source this is at most two; for
    source,target<=100 the global bound is eleven.
    """
    _require_positive("source_multiplier", source_multiplier)
    _require_positive("target_multiplier", target_multiplier)
    if source_multiplier == target_multiplier:
        return 0
    return _ceil_sqrt_ratio(target_multiplier, source_multiplier) + 1


@lru_cache(maxsize=None)
def pairwise_scale_constant(
    n_bits: int,
    source_multiplier: int,
    target_multiplier: int,
) -> tuple[int, int]:
    """Return ``(B,A)`` with A=floor(2**B*sqrt(target/source)) exactly."""
    _require_positive("n_bits", n_bits)
    _require_positive("source_multiplier", source_multiplier)
    _require_positive("target_multiplier", target_multiplier)
    if source_multiplier > MAX_MULTIPLIER or target_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"multipliers must be <= {MAX_MULTIPLIER}")
    B = fraction_bits_for_n_bits(n_bits)
    A = isqrt((target_multiplier << (2 * B)) // source_multiplier)
    return B, A


@dataclass(frozen=True)
class PairwiseMultiplierRootState:
    n: int
    multiplier: int
    root: int
    remainder: int
    source_multiplier: int
    correction_steps: int

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        _require_positive("source_multiplier", self.source_multiplier)
        if isinstance(self.root, bool) or not isinstance(self.root, int) or self.root < 0:
            raise ValueError("root must be a non-negative integer")
        if (
            isinstance(self.remainder, bool)
            or not isinstance(self.remainder, int)
            or self.remainder < 0
            or self.remainder > 2 * self.root
        ):
            raise ValueError("remainder escaped the square-root BRC basin")
        if (
            isinstance(self.correction_steps, bool)
            or not isinstance(self.correction_steps, int)
            or self.correction_steps < 0
        ):
            raise ValueError("correction_steps must be non-negative")

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder

    @property
    def ceiling_root(self) -> int:
        return self.root if self.remainder == 0 else self.root + 1

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


def transport_multiplier_root_state(
    source: MultiplierStateLike,
    target_multiplier: int,
) -> PairwiseMultiplierRootState:
    """Transport an exact BRC multiplier state directly from m to t.

    The candidate is a lower bound, so correction is one-sided: repeated
    subtraction of the next odd square-basin width.  No integer root of t*N is
    materialized.
    """
    _require_positive("target_multiplier", target_multiplier)
    if target_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"target_multiplier must be <= {MAX_MULTIPLIER}")

    n = source.n
    m = source.multiplier
    j = source.root
    r = source.remainder

    _require_positive("n", n)
    _require_positive("source multiplier", m)
    if m > MAX_MULTIPLIER:
        raise ValueError(f"source multiplier must be <= {MAX_MULTIPLIER}")
    if j * j + r != m * n:
        raise ValueError("source state does not reconstruct source_multiplier*n")
    if not 0 <= r <= 2 * j:
        raise ValueError("source remainder escaped its BRC basin")

    if target_multiplier == m:
        return PairwiseMultiplierRootState(
            n=n,
            multiplier=m,
            root=j,
            remainder=r,
            source_multiplier=m,
            correction_steps=0,
        )

    B, scale_constant = pairwise_scale_constant(
        n.bit_length(),
        m,
        target_multiplier,
    )
    candidate = (scale_constant * j) >> B
    d = candidate - j

    # t*N-candidate^2 from m*N=j^2+r.  The formula is valid for d<0 too.
    gap = r + (target_multiplier - m) * n - d * (2 * j + d)
    if gap < 0:
        raise AssertionError("pairwise lower predictor overshot the exact target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    bound = pairwise_correction_bound(m, target_multiplier)
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > bound:
            raise AssertionError("pairwise BRC correction bound failed")
        odd_width += 2

    state = PairwiseMultiplierRootState(
        n=n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        source_multiplier=m,
        correction_steps=corrections,
    )
    if state.target_value != target_multiplier * n:
        raise AssertionError("pairwise multiplier transport failed exact reconstruction")
    return state


def pairwise_multiplier_order_states(
    n: int,
    order: tuple[int, ...],
) -> tuple[PairwiseMultiplierRootState, ...]:
    """Transport one N through an arbitrary multiplier order starting at m=1.

    The initial square root of N is materialized exactly once. Every later state
    is transported from the immediately previous state in the declared order.
    """
    _require_positive("n", n)
    if not order or order[0] != 1:
        raise ValueError("order must be nonempty and start at multiplier 1")
    if len(set(order)) != len(order):
        raise ValueError("order multipliers must be unique")
    if any(m <= 0 or m > MAX_MULTIPLIER for m in order):
        raise ValueError(f"order multipliers must lie in 1..{MAX_MULTIPLIER}")

    base = initial_multiplier_root_state(n)
    current = PairwiseMultiplierRootState(
        n=n,
        multiplier=1,
        root=base.root,
        remainder=base.remainder,
        source_multiplier=1,
        correction_steps=0,
    )
    states = [current]
    for target in order[1:]:
        current = transport_multiplier_root_state(current, target)
        states.append(current)
    return tuple(states)


def pairwise_prioritized_odd_multiplier_states(
    n: int,
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[PairwiseMultiplierRootState, ...]:
    """Follow the current exact odd-N representative priority order pairwise."""
    _require_positive("n", n)
    if n % 2 == 0:
        raise ValueError("prioritized odd multiplier scan requires odd n")
    _require_positive("max_multiplier", max_multiplier)
    if max_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"max_multiplier must be <= {MAX_MULTIPLIER}")
    order = prioritized_odd_multiplier_order(max_multiplier)
    return pairwise_multiplier_order_states(n, order)


__all__ = [
    "PairwiseMultiplierRootState",
    "pairwise_correction_bound",
    "pairwise_scale_constant",
    "transport_multiplier_root_state",
    "pairwise_multiplier_order_states",
    "pairwise_prioritized_odd_multiplier_states",
]
