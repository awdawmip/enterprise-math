"""Exact consecutive-multiplier BRC root/remainder transport.

For fixed positive N, write

    m*N = J_m**2 + R_m,   0 <= R_m <= 2*J_m.

After the initial m=1 root, this module advances m->m+1 without another root
evaluation. A dyadic predictor for gamma_m=sqrt((m+1)/m)-1 places the next root
at a lower candidate that needs at most two exact odd-width BRC corrections.

The checked-in predictor table is static through 4096-bit N. Larger N use the
same proved recurrence with a cached exact predictor construction.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import integer_nth_root
from .brc_multiplier_transition_table import (
    MAX_MULTIPLIER,
    RAW_PAYLOAD_BYTES,
    transition_constants_for_n_bits,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class MultiplierRootState:
    n: int
    multiplier: int
    root: int
    remainder: int
    correction_steps: int = 0

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        if isinstance(self.root, bool) or not isinstance(self.root, int) or self.root < 0:
            raise ValueError("root must be a non-negative integer")
        if (
            isinstance(self.remainder, bool)
            or not isinstance(self.remainder, int)
            or self.remainder < 0
        ):
            raise ValueError("remainder must be a non-negative integer")
        if self.remainder > 2 * self.root:
            raise ValueError("remainder escaped the square-root BRC basin")
        if (
            isinstance(self.correction_steps, bool)
            or not isinstance(self.correction_steps, int)
            or not 0 <= self.correction_steps <= 2
        ):
            raise ValueError("correction_steps must lie in 0..2")

    @property
    def collapsed_value(self) -> int:
        return self.root * self.root

    @property
    def target_value(self) -> int:
        return self.collapsed_value + self.remainder

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


def initial_multiplier_root_state(n: int) -> MultiplierRootState:
    """Materialize the only N-dependent multiplier root required by a scan."""
    _require_positive("n", n)
    root = integer_nth_root(n, 2)
    return MultiplierRootState(
        n=n,
        multiplier=1,
        root=root,
        remainder=n - root * root,
        correction_steps=0,
    )


def _next_with_constant(
    state: MultiplierRootState,
    *,
    fraction_bits: int,
    gamma_constant: int,
) -> MultiplierRootState:
    if state.multiplier >= MAX_MULTIPLIER:
        raise ValueError(f"transition table stops at multiplier {MAX_MULTIPLIER}")

    j = state.root
    r = state.remainder
    d0 = (gamma_constant * j) >> fraction_bits
    candidate = j + d0

    # (m+1)N-candidate^2 from mN=j^2+r, without squaring candidate.
    gap = r + state.n - d0 * (2 * j + d0)
    if gap < 0:
        raise AssertionError("dyadic lower predictor overshot the next BRC root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 2:
            raise AssertionError("two-correction transition theorem failed")
        odd_width += 2

    next_state = MultiplierRootState(
        n=state.n,
        multiplier=state.multiplier + 1,
        root=candidate,
        remainder=gap,
        correction_steps=corrections,
    )
    if next_state.target_value != (state.multiplier + 1) * state.n:
        raise AssertionError("BRC multiplier transition failed exact reconstruction")
    return next_state


def next_multiplier_root_state(state: MultiplierRootState) -> MultiplierRootState:
    B, constants, _ = transition_constants_for_n_bits(state.n.bit_length())
    return _next_with_constant(
        state,
        fraction_bits=B,
        gamma_constant=constants[state.multiplier - 1],
    )


def multiplier_root_state_sequence(
    n: int, max_multiplier: int = MAX_MULTIPLIER
) -> tuple[MultiplierRootState, ...]:
    """Exact m=1..M sequence; only the initial state materializes sqrt(N)."""
    _require_positive("n", n)
    _require_positive("max_multiplier", max_multiplier)
    if max_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"max_multiplier must be <= {MAX_MULTIPLIER}")

    B, constants, _ = transition_constants_for_n_bits(n.bit_length())
    state = initial_multiplier_root_state(n)
    states = [state]
    for m in range(1, max_multiplier):
        state = _next_with_constant(
            state,
            fraction_bits=B,
            gamma_constant=constants[m - 1],
        )
        states.append(state)
    return tuple(states)


def transition_table_mode(n: int) -> str:
    _require_positive("n", n)
    return transition_constants_for_n_bits(n.bit_length())[2]


def transition_correction_histogram(
    n: int, max_multiplier: int = MAX_MULTIPLIER
) -> tuple[int, int, int]:
    counts = [0, 0, 0]
    for state in multiplier_root_state_sequence(n, max_multiplier)[1:]:
        counts[state.correction_steps] += 1
    return tuple(counts)


def static_transition_payload_bytes() -> int:
    return RAW_PAYLOAD_BYTES


__all__ = [
    "MultiplierRootState",
    "initial_multiplier_root_state",
    "next_multiplier_root_state",
    "multiplier_root_state_sequence",
    "transition_table_mode",
    "transition_correction_histogram",
    "static_transition_payload_bytes",
]
