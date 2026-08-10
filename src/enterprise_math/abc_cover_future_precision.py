"""Future-query-relative precision compiler for odd-prime cover transport.

Supplement 89 reduces qualitative odd-cover transport to two natural bits:

    R = ancestor support resonance,
    S = quotient squarefree.

But different future queries require different states and observation trees:

* binary non-attenuation: R or not S, with symmetric short-circuit trees;
* ternary class: S must be known; if not S the answer is immediately amplified,
  while R is needed only on the squarefree branch;
* exact multiplier: the sufficient natural state is (R,d) with d=m(Q).

This module separates semantic output, sufficient observation state, and
adaptive observation order.  It is an executable pressure test of task-relative
precision, not a generic decision-theory framework.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_odd_cover_transport_gap import (
    OddCoverTransportGapState,
    odd_cover_transport_gap_state,
)


@dataclass(frozen=True)
class ObservationTrace:
    future_query: str
    observation_order: str
    observed_fields: tuple[str, ...]
    result: bool | str | Fraction
    short_circuited: bool


@dataclass(frozen=True)
class CoverFuturePrecisionState:
    support_resonance: bool
    quotient_squarefree: bool
    quotient_residual: int
    binary_nonattenuating: bool
    ternary_transport_class: str
    exact_multiplier: Fraction


def binary_nonattenuating_from_bits(
    support_resonance: bool, quotient_squarefree: bool
) -> bool:
    """Return Lambda>=1 from the Stage-89 qualitative bits."""
    return support_resonance or not quotient_squarefree


def ternary_transport_class_from_bits(
    support_resonance: bool, quotient_squarefree: bool
) -> str:
    """Return attenuated/resonant/amplified from the two natural bits."""
    if not quotient_squarefree:
        return "amplified"
    return "resonant" if support_resonance else "attenuated"


def exact_multiplier_from_resonance_residual(
    support_resonance: bool, quotient_residual: int, cover_prime: int
) -> Fraction:
    """Return the exact odd-cover multiplier from (R,d)."""
    if isinstance(quotient_residual, bool) or not isinstance(quotient_residual, int) or quotient_residual < 1:
        raise ValueError("quotient_residual must be a positive integer")
    if isinstance(cover_prime, bool) or not isinstance(cover_prime, int) or cover_prime < 3:
        raise ValueError("cover_prime must be at least three")
    if support_resonance:
        return Fraction(quotient_residual, 1)
    return Fraction(quotient_residual, cover_prime)


def cover_future_precision_state(
    q: int,
    p: int,
    lower_exponent: int,
    cover_prime: int,
    mode: str,
) -> CoverFuturePrecisionState:
    """Compile the three future languages for one exact odd-prime cover."""
    gap = odd_cover_transport_gap_state(
        q, p, lower_exponent, cover_prime, mode
    )
    binary = binary_nonattenuating_from_bits(
        gap.support_resonance, gap.quotient_squarefree
    )
    ternary = ternary_transport_class_from_bits(
        gap.support_resonance, gap.quotient_squarefree
    )
    exact = exact_multiplier_from_resonance_residual(
        gap.support_resonance, gap.quotient_residual, cover_prime
    )
    if binary != (gap.inheritance_multiplier >= 1):
        raise AssertionError("binary future quotient disagreed with exact multiplier")
    if ternary != gap.transport_class:
        raise AssertionError("ternary future quotient disagreed with exact transport class")
    if exact != gap.inheritance_multiplier:
        raise AssertionError("exact natural state lost multiplier")
    return CoverFuturePrecisionState(
        support_resonance=gap.support_resonance,
        quotient_squarefree=gap.quotient_squarefree,
        quotient_residual=gap.quotient_residual,
        binary_nonattenuating=binary,
        ternary_transport_class=ternary,
        exact_multiplier=exact,
    )


def binary_observation_trace(
    state: CoverFuturePrecisionState, order: str
) -> ObservationTrace:
    """Return an exact short-circuit trace for the binary future query."""
    if order == "resonance_first":
        if state.support_resonance:
            return ObservationTrace(
                "nonattenuating",
                order,
                ("support_resonance",),
                True,
                True,
            )
        return ObservationTrace(
            "nonattenuating",
            order,
            ("support_resonance", "quotient_squarefree"),
            not state.quotient_squarefree,
            False,
        )
    if order == "squarefree_first":
        if not state.quotient_squarefree:
            return ObservationTrace(
                "nonattenuating",
                order,
                ("quotient_squarefree",),
                True,
                True,
            )
        return ObservationTrace(
            "nonattenuating",
            order,
            ("quotient_squarefree", "support_resonance"),
            state.support_resonance,
            False,
        )
    raise ValueError("order must be 'resonance_first' or 'squarefree_first'")


def ternary_observation_trace(
    state: CoverFuturePrecisionState, order: str
) -> ObservationTrace:
    """Return an exact observation trace for the three-state future query."""
    if order == "squarefree_first":
        if not state.quotient_squarefree:
            return ObservationTrace(
                "transport_class",
                order,
                ("quotient_squarefree",),
                "amplified",
                True,
            )
        return ObservationTrace(
            "transport_class",
            order,
            ("quotient_squarefree", "support_resonance"),
            "resonant" if state.support_resonance else "attenuated",
            False,
        )
    if order == "resonance_first":
        # R alone never distinguishes resonant/amplified or attenuated/amplified.
        return ObservationTrace(
            "transport_class",
            order,
            ("support_resonance", "quotient_squarefree"),
            ternary_transport_class_from_bits(
                state.support_resonance, state.quotient_squarefree
            ),
            False,
        )
    raise ValueError("order must be 'resonance_first' or 'squarefree_first'")


def exact_observation_trace(state: CoverFuturePrecisionState) -> ObservationTrace:
    """The exact multiplier requires resonance plus the numerical quotient residual."""
    return ObservationTrace(
        "exact_multiplier",
        "resonance_and_residual",
        ("support_resonance", "quotient_residual"),
        state.exact_multiplier,
        False,
    )
