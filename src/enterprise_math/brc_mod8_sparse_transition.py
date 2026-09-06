"""Exact sparse BRC root transport over the odd-N mod-8 representative scan.

The exact scan quotient keeps multiplier residues {0,1,3,5,7} modulo 8. In
increasing order, adjacent retained multipliers differ only by 1 or 2. This
module therefore avoids materializing the statically removed intermediate root
states: one-step transitions reuse the existing consecutive predictor and
two-step transitions use a compiled lower dyadic predictor for
sqrt((m+2)/m).

No additional checked-in predictor payload is required. The two-step constants
are compiled once from adjacent one-step constants already supplied by the
canonical multiplier-transition table.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from .brc_multiplier_priority_jump import odd_n_multiplier_is_scan_irredundant
from .brc_multiplier_transition import initial_multiplier_root_state
from .brc_multiplier_transition_table import (
    MAX_MULTIPLIER,
    transition_constants_for_n_bits,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def compile_two_step_gamma_constants(
    fraction_bits: int,
    consecutive_gamma_constants: tuple[int, ...],
) -> tuple[int, ...]:
    """Compile lower dyadic predictors for ``sqrt((m+2)/m)-1``.

    Entry i of the input is the lower dyadic constant for the consecutive
    factor ``sqrt((i+2)/(i+1))-1`` at a common precision B. Multiplying the
    corresponding lower factors for m->m+1 and m+1->m+2 and truncating back to
    B bits remains a lower bound for the exact two-step factor.

    The returned entry i corresponds to multiplier m=i+1 and has length one
    less than the input sequence.
    """
    _require_positive("fraction_bits", fraction_bits)
    if len(consecutive_gamma_constants) < 2:
        return ()
    scale = 1 << fraction_bits
    return tuple(
        (((scale + left) * (scale + right)) >> fraction_bits) - scale
        for left, right in zip(
            consecutive_gamma_constants,
            consecutive_gamma_constants[1:],
        )
    )


@lru_cache(maxsize=None)
def _compiled_static_constants(
    n_bits: int,
) -> tuple[int, tuple[int, ...], tuple[int, ...], str]:
    B, one_step, mode = transition_constants_for_n_bits(n_bits)
    two_step = compile_two_step_gamma_constants(B, one_step)
    return B, one_step, two_step, mode


@dataclass(frozen=True)
class SparseMultiplierRootState:
    n: int
    multiplier: int
    root: int
    remainder: int
    step_from_previous: int
    correction_steps: int

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        if isinstance(self.root, bool) or not isinstance(self.root, int) or self.root < 0:
            raise ValueError("root must be a non-negative integer")
        if (
            isinstance(self.remainder, bool)
            or not isinstance(self.remainder, int)
            or self.remainder < 0
            or self.remainder > 2 * self.root
        ):
            raise ValueError("remainder escaped square-root BRC basin")
        if self.step_from_previous not in (0, 1, 2):
            raise ValueError("step_from_previous must be 0, 1, or 2")
        if (
            isinstance(self.correction_steps, bool)
            or not isinstance(self.correction_steps, int)
            or not 0 <= self.correction_steps <= 4
        ):
            raise ValueError("correction_steps must lie in 0..4")

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder

    @property
    def ceiling_root(self) -> int:
        return self.root if self.remainder == 0 else self.root + 1

    @property
    def ceiling_completion_gap(self) -> int:
        return 0 if self.remainder == 0 else 2 * self.root + 1 - self.remainder


def _advance_sparse(
    state: SparseMultiplierRootState,
    *,
    step: int,
    fraction_bits: int,
    gamma_constant: int,
    correction_bound: int,
) -> SparseMultiplierRootState:
    if step not in (1, 2):
        raise ValueError("sparse transition step must be 1 or 2")
    j = state.root
    d0 = (gamma_constant * j) >> fraction_bits
    candidate = j + d0

    # (m+step)N - candidate^2, using mN=j^2+R.
    gap = state.remainder + step * state.n - d0 * (2 * j + d0)
    if gap < 0:
        raise AssertionError("sparse dyadic lower predictor overshot target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        odd_width += 2
        corrections += 1
        if corrections > correction_bound:
            raise AssertionError("sparse transition correction theorem failed")

    next_state = SparseMultiplierRootState(
        n=state.n,
        multiplier=state.multiplier + step,
        root=candidate,
        remainder=gap,
        step_from_previous=step,
        correction_steps=corrections,
    )
    if next_state.target_value != next_state.multiplier * state.n:
        raise AssertionError("sparse multiplier transition reconstruction failed")
    return next_state


def odd_n_sparse_multiplier_root_sequence(
    n: int,
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[SparseMultiplierRootState, ...]:
    """Return exact increasing root states only on the mod-8 scan representatives.

    For ``max_multiplier=100`` this returns 62 states instead of 100.  The only
    N-dependent integer root is the initial m=1 root.  Retained-state gaps are
    1 or 2; one-step transitions have the existing two-correction bound and
    compiled two-step transitions have the proved four-correction bound.
    """
    _require_positive("n", n)
    _require_positive("max_multiplier", max_multiplier)
    if n % 2 == 0:
        raise ValueError("mod-8 sparse scan requires odd n")
    if max_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"static sparse transition currently requires max_multiplier <= {MAX_MULTIPLIER}")

    B, one_step, two_step, _ = _compiled_static_constants(n.bit_length())
    initial = initial_multiplier_root_state(n)
    state = SparseMultiplierRootState(
        n=n,
        multiplier=1,
        root=initial.root,
        remainder=initial.remainder,
        step_from_previous=0,
        correction_steps=0,
    )
    states = [state]

    for target in range(2, max_multiplier + 1):
        if not odd_n_multiplier_is_scan_irredundant(target):
            continue
        step = target - state.multiplier
        if step == 1:
            gamma = one_step[state.multiplier - 1]
            bound = 2
        elif step == 2:
            gamma = two_step[state.multiplier - 1]
            bound = 4
        else:
            raise AssertionError("mod-8 representative gaps must be 1 or 2")
        state = _advance_sparse(
            state,
            step=step,
            fraction_bits=B,
            gamma_constant=gamma,
            correction_bound=bound,
        )
        states.append(state)
    return tuple(states)


def sparse_transition_table_mode(n: int) -> str:
    _require_positive("n", n)
    return _compiled_static_constants(n.bit_length())[3]


__all__ = [
    "SparseMultiplierRootState",
    "compile_two_step_gamma_constants",
    "odd_n_sparse_multiplier_root_sequence",
    "sparse_transition_table_mode",
]
