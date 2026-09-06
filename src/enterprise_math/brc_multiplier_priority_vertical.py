"""Priority scheduling over BRC multiplier x vertical-factor search.

This module composes two already-established surfaces:

* monotone admissible multiplier root/remainder transport;
* the vertical quadratic-residue wheel.

The horizontal BRC states are computed once in the safe monotone order, then
reindexed and consumed in an experimental static priority order before the
expensive vertical search.  Reordering changes latency only; the full
multiplier x vertical rectangle is unchanged.

The module also exposes a proved remainder-aware arbitrary multiplier jump as
a diagnostic exact interface.  In the current Python reference implementation
that jump is not the default performance path because its large-integer
rational division is slower than direct ``math.isqrt`` for the tested priority
prefixes.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import isqrt
from typing import Iterable

from .brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    admissible_multipliers,
    admissible_root_state_sequence,
    heuristic_priority_multipliers,
)
from .brc_multiplier_transition_table import (
    MAX_MULTIPLIER,
    fraction_bits_for_n_bits,
)
from .brc_multiplier_vertical_wheel import (
    first_vertical_factor_witness,
    vertical_state_from_multiplier_state,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ArbitraryMultiplierJump:
    n: int
    source_multiplier: int
    target_multiplier: int
    source_root: int
    source_remainder: int
    fraction_bits: int
    predicted_root: int
    correction_steps: int
    target_root: int
    target_remainder: int

    def reconstruct(self) -> int:
        return self.target_root * self.target_root + self.target_remainder


@dataclass(frozen=True)
class PriorityVerticalFactorWitness:
    factor: int
    multiplier: int
    vertical_offset: int
    priority_rank: int
    horizontal_state_count: int


@lru_cache(maxsize=None)
def _beta_constant(source_multiplier: int, target_multiplier: int, fraction_bits: int) -> int:
    """floor(2**B * sqrt(target/source)) by integer arithmetic only."""
    return isqrt(
        (target_multiplier << (2 * fraction_bits)) // source_multiplier
    )


def remainder_aware_multiplier_jump(
    state: AdmissibleMultiplierRootState,
    target_multiplier: int,
) -> ArbitraryMultiplierJump:
    """Jump exactly between arbitrary multipliers 1..100 with <=1 correction.

    Write ``a*n = J^2 + R`` and ``sqrt(a*n)=J+delta``.  The retained BRC
    remainder gives the lower approximation

        L = J + R/(2J+1),

    and the exact identity

        sqrt(a*n)-L = delta*(1-delta)/(2J+1).

    For ``a,b<=100`` let beta=sqrt(b/a).  Using two more dyadic precision bits
    than the consecutive-transition table and a lower dyadic beta coefficient
    gives a predicted root q0 with

        floor(sqrt(b*n)) - q0 in {0,1}.

    One odd-width BRC basin correction therefore suffices.

    This is an exact structural interface, not the default Python fast path.
    """
    _require_positive("target_multiplier", target_multiplier)
    if not 1 <= state.multiplier <= MAX_MULTIPLIER:
        raise ValueError(f"source multiplier must be <= {MAX_MULTIPLIER}")
    if target_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"target_multiplier must be <= {MAX_MULTIPLIER}")

    source = state.multiplier
    j = state.root
    r = state.remainder
    if target_multiplier == source:
        return ArbitraryMultiplierJump(
            n=state.n,
            source_multiplier=source,
            target_multiplier=target_multiplier,
            source_root=j,
            source_remainder=r,
            fraction_bits=fraction_bits_for_n_bits(state.n.bit_length()) + 2,
            predicted_root=j,
            correction_steps=0,
            target_root=j,
            target_remainder=r,
        )

    B = fraction_bits_for_n_bits(state.n.bit_length()) + 2
    C = _beta_constant(source, target_multiplier, B)
    scale = 1 << B
    denominator = 2 * j + 1

    # floor(C/2^B * (J + R/(2J+1))) without Fraction/float state.
    product = C * j
    base = product >> B
    dyadic_remainder = product - (base << B)
    extra = (
        dyadic_remainder * denominator + C * r
    ) // (scale * denominator)
    predicted = base + extra

    d = predicted - j
    gap = r + (target_multiplier - source) * state.n - d * (2 * j + d)
    if gap < 0:
        raise AssertionError("remainder-aware lower predictor overshot target root")

    corrections = 0
    width = 2 * predicted + 1
    target_root = predicted
    if gap >= width:
        gap -= width
        target_root += 1
        corrections = 1

    if gap >= 2 * target_root + 1:
        raise AssertionError("one-correction arbitrary multiplier theorem failed")

    result = ArbitraryMultiplierJump(
        n=state.n,
        source_multiplier=source,
        target_multiplier=target_multiplier,
        source_root=j,
        source_remainder=r,
        fraction_bits=B,
        predicted_root=predicted,
        correction_steps=corrections,
        target_root=target_root,
        target_remainder=gap,
    )
    if result.reconstruct() != target_multiplier * state.n:
        raise AssertionError("arbitrary multiplier jump failed reconstruction")
    if not 0 <= gap <= 2 * target_root:
        raise AssertionError("arbitrary multiplier jump escaped target basin")
    return result


def priority_ordered_multiplier_states(
    n: int,
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[AdmissibleMultiplierRootState, ...]:
    """Compute horizontal states once, then return them in heuristic priority order."""
    _require_positive("n", n)
    states = admissible_root_state_sequence(n, max_multiplier)
    by_multiplier = {state.multiplier: state for state in states}
    order = heuristic_priority_multipliers(max_multiplier)
    if set(order) != set(by_multiplier):
        raise AssertionError("priority order does not match admissible multiplier support")
    return tuple(by_multiplier[m] for m in order)


def ordered_vertical_factor_witness_from_states(
    states: tuple[AdmissibleMultiplierRootState, ...],
    t_limit: int,
    multipliers: Iterable[int],
    *,
    first_modulus: int | None = None,
) -> PriorityVerticalFactorWitness | None:
    """Search one already-materialized horizontal state family in a declared order."""
    _require_positive("t_limit", t_limit)
    if not states:
        return None
    n = states[0].n
    if any(state.n != n for state in states):
        raise ValueError("all horizontal states must belong to one n")
    order = tuple(multipliers)
    if not order:
        return None
    if len(set(order)) != len(order):
        raise ValueError("multipliers must be unique")
    by_multiplier = {state.multiplier: state for state in states}
    if any(m not in by_multiplier for m in order):
        raise ValueError("ordered multiplier is absent from horizontal state family")

    for rank, multiplier in enumerate(order, 1):
        vertical = vertical_state_from_multiplier_state(by_multiplier[multiplier])
        witness = first_vertical_factor_witness(
            vertical,
            t_limit,
            first_modulus=first_modulus,
        )
        if witness is None:
            continue
        factor, t = witness
        return PriorityVerticalFactorWitness(
            factor=factor,
            multiplier=multiplier,
            vertical_offset=t,
            priority_rank=rank,
            horizontal_state_count=len(states),
        )
    return None


def ordered_vertical_factor_witness(
    n: int,
    t_limit: int,
    multipliers: Iterable[int],
    *,
    max_multiplier: int = MAX_MULTIPLIER,
    first_modulus: int | None = None,
) -> PriorityVerticalFactorWitness | None:
    """Build the monotone horizontal family once, then reorder only vertical work."""
    _require_positive("n", n)
    _require_positive("t_limit", t_limit)
    order = tuple(multipliers)
    if not order:
        return None
    if len(set(order)) != len(order):
        raise ValueError("multipliers must be unique")
    allowed = set(admissible_multipliers(max_multiplier))
    if any(m not in allowed for m in order):
        raise ValueError("all multipliers must belong to the admissible odd-N set")
    states = admissible_root_state_sequence(n, max_multiplier)
    return ordered_vertical_factor_witness_from_states(
        states,
        t_limit,
        order,
        first_modulus=first_modulus,
    )


def first_priority_vertical_factor_witness(
    n: int,
    t_limit: int,
    *,
    max_multiplier: int = MAX_MULTIPLIER,
    first_modulus: int | None = None,
) -> PriorityVerticalFactorWitness | None:
    """Search the full admissible rectangle in the current static priority order."""
    return ordered_vertical_factor_witness(
        n,
        t_limit,
        heuristic_priority_multipliers(max_multiplier),
        max_multiplier=max_multiplier,
        first_modulus=first_modulus,
    )


def first_ascending_vertical_factor_witness(
    n: int,
    t_limit: int,
    *,
    max_multiplier: int = MAX_MULTIPLIER,
    first_modulus: int | None = None,
) -> PriorityVerticalFactorWitness | None:
    """Reference latency baseline using increasing admissible multipliers."""
    return ordered_vertical_factor_witness(
        n,
        t_limit,
        admissible_multipliers(max_multiplier),
        max_multiplier=max_multiplier,
        first_modulus=first_modulus,
    )


__all__ = [
    "ArbitraryMultiplierJump",
    "PriorityVerticalFactorWitness",
    "remainder_aware_multiplier_jump",
    "priority_ordered_multiplier_states",
    "ordered_vertical_factor_witness_from_states",
    "ordered_vertical_factor_witness",
    "first_priority_vertical_factor_witness",
    "first_ascending_vertical_factor_witness",
]
