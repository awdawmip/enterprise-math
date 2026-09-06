"""Odd-N BRC multiplier scan with safe parity pruning and strong square-gap cascade.

This module composes:
- the proved BRC multiplier root/remainder transport;
- the classical obstruction m == 2 (mod 4) for differences of two squares;
- checked-in quadratic-residue filters modulo 20160 and 46189.

The default scan is deterministic and zero-false-negative relative to the
immediate multiplier-Fermat square-gap witness surface. An optional static
priority order is exposed as an experimental heuristic only; it never changes
which multipliers are admissible.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt

from .brc_multiplier_transition import initial_multiplier_root_state
from .brc_multiplier_transition_table import (
    MAX_MULTIPLIER,
    transition_constants_for_n_bits,
)
from .brc_multiplier_transition_jump2_table import jump2_constant_for_n_bits
from .brc_square_gap_prefilter import square_residue_table
from .brc_square_gap_table_46189 import (
    MODULUS as CASCADE_SECOND_MODULUS,
    SQUARE_RESIDUE_TABLE as CASCADE_SECOND_TABLE,
)

CASCADE_FIRST_MODULUS = 20160
STRONG_CASCADE_MODULI = (CASCADE_FIRST_MODULUS, CASCADE_SECOND_MODULUS)
STRONG_CASCADE_UNIFORM_PASS_FRACTION = Fraction(108, 46189)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _table_contains(table: bytes, modulus: int, value: int) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


def strong_cascade_passes_squarehood(value: int) -> bool:
    """Zero-false-negative necessary test for non-negative integer squarehood."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a non-negative integer")
    first = square_residue_table(CASCADE_FIRST_MODULUS)
    return _table_contains(first, CASCADE_FIRST_MODULUS, value) and _table_contains(
        CASCADE_SECOND_TABLE, CASCADE_SECOND_MODULUS, value
    )


def strong_cascade_square_root(value: int) -> int | None:
    """Return exact sqrt(value) after the two-table cascade, else None."""
    if not strong_cascade_passes_squarehood(value):
        return None
    root = isqrt(value)
    return root if root * root == value else None


def odd_multiplier_admissible(multiplier: int) -> bool:
    """Whether m*N can be a difference of squares for odd N."""
    _require_positive("multiplier", multiplier)
    return multiplier % 4 != 2


def admissible_multipliers(max_multiplier: int = MAX_MULTIPLIER) -> tuple[int, ...]:
    _require_positive("max_multiplier", max_multiplier)
    if max_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"max_multiplier must be <= {MAX_MULTIPLIER}")
    return tuple(m for m in range(1, max_multiplier + 1) if odd_multiplier_admissible(m))


@dataclass(frozen=True)
class AdmissibleMultiplierRootState:
    n: int
    multiplier: int
    root: int
    remainder: int
    correction_steps: int

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


def _advance(
    state: AdmissibleMultiplierRootState,
    target_multiplier: int,
    fraction_bits: int,
    gamma_constant: int,
    correction_bound: int,
) -> AdmissibleMultiplierRootState:
    step = target_multiplier - state.multiplier
    if step not in (1, 2):
        raise ValueError("admissible scan supports only monotone jumps of one or two")
    j = state.root
    d0 = (gamma_constant * j) >> fraction_bits
    candidate = j + d0
    gap = state.remainder + step * state.n - d0 * (2 * j + d0)
    if gap < 0:
        raise AssertionError("dyadic predictor overshot target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > correction_bound:
            raise AssertionError("admissible multiplier correction bound failed")
        odd_width += 2

    result = AdmissibleMultiplierRootState(
        n=state.n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        correction_steps=corrections,
    )
    if candidate * candidate + gap != target_multiplier * state.n:
        raise AssertionError("admissible BRC transport failed reconstruction")
    if not 0 <= gap <= 2 * candidate:
        raise AssertionError("admissible BRC transport escaped target basin")
    return result


def admissible_root_state_sequence(
    n: int, max_multiplier: int = MAX_MULTIPLIER
) -> tuple[AdmissibleMultiplierRootState, ...]:
    """Exact odd-N admissible multiplier states through max_multiplier.

    Multipliers 2 mod 4 are omitted with no loss for a difference-of-squares
    witness. Consecutive steps reuse the existing <=2 correction theorem.
    Jumps over an impossible multiplier use sqrt((m+2)/m) predictors and need
    at most three exact odd-width basin corrections.
    """
    _require_positive("n", n)
    if n % 2 == 0:
        raise ValueError("admissible odd-factor bridge requires odd n")
    path = admissible_multipliers(max_multiplier)
    base = initial_multiplier_root_state(n)
    state = AdmissibleMultiplierRootState(n, 1, base.root, base.remainder, 0)
    states = [state]
    B, consecutive_constants, _ = transition_constants_for_n_bits(n.bit_length())

    for target in path[1:]:
        step = target - state.multiplier
        if step == 1:
            constant = consecutive_constants[state.multiplier - 1]
            state = _advance(state, target, B, constant, 2)
        else:
            B2, constant, _ = jump2_constant_for_n_bits(
                n.bit_length(), state.multiplier
            )
            if B2 != B:
                raise AssertionError("predictor precision mismatch")
            state = _advance(state, target, B, constant, 3)
        states.append(state)
    return tuple(states)


def strong_cascade_candidates(
    n: int, max_multiplier: int = MAX_MULTIPLIER
) -> tuple[AdmissibleMultiplierRootState, ...]:
    return tuple(
        state
        for state in admissible_root_state_sequence(n, max_multiplier)
        if strong_cascade_passes_squarehood(state.ceiling_completion_gap)
    )


def first_immediate_factor_witness(
    n: int, max_multiplier: int = MAX_MULTIPLIER
) -> tuple[int, int] | None:
    """Return (factor,multiplier) on the classical immediate square-gap surface."""
    _require_positive("n", n)
    if n % 2 == 0:
        return (2, 1) if n > 2 else None
    for state in strong_cascade_candidates(n, max_multiplier):
        b = strong_cascade_square_root(state.ceiling_completion_gap)
        if b is None:
            continue
        x = state.root if state.remainder == 0 else state.root + 1
        for term in (x - b, x + b):
            factor = gcd(term, n)
            if 1 < factor < n:
                return factor, state.multiplier
    return None


def nontrivial_same_parity_factor_pairs(multiplier: int) -> tuple[tuple[int, int], ...]:
    _require_positive("multiplier", multiplier)
    pairs: list[tuple[int, int]] = []
    for v in range(1, isqrt(multiplier) + 1):
        if multiplier % v:
            continue
        u = multiplier // v
        if u > v and (u - v) % 2 == 0:
            pairs.append((u, v))
    return tuple(pairs)


def multiplier_priority_score(multiplier: int) -> Fraction:
    """Experimental ratio-coverage score nu(m)^4/m."""
    nu = len(nontrivial_same_parity_factor_pairs(multiplier))
    return Fraction(nu**4, multiplier)


def heuristic_priority_multipliers(
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[int, ...]:
    """Return m=1 first, then admissible m by decreasing experimental score."""
    path = admissible_multipliers(max_multiplier)
    tail = [m for m in path if m != 1]
    tail.sort(key=lambda m: (-multiplier_priority_score(m), m))
    return (1, *tail)


__all__ = [
    "CASCADE_FIRST_MODULUS",
    "CASCADE_SECOND_MODULUS",
    "STRONG_CASCADE_MODULI",
    "STRONG_CASCADE_UNIFORM_PASS_FRACTION",
    "AdmissibleMultiplierRootState",
    "strong_cascade_passes_squarehood",
    "strong_cascade_square_root",
    "odd_multiplier_admissible",
    "admissible_multipliers",
    "admissible_root_state_sequence",
    "strong_cascade_candidates",
    "first_immediate_factor_witness",
    "nontrivial_same_parity_factor_pairs",
    "multiplier_priority_score",
    "heuristic_priority_multipliers",
]
