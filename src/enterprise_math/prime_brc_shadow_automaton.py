"""Minimal four-state Prime-BRC automaton on a large-q shadow edge.

For a double-hit edge a*q<M<(a+1)*q with q>k, define the cumulative scaled
support at E>=1 by

    S_E = (1[E|a], 1[E|a+1]).

The complete carry coordinate is the invertible sum/detail transform

    kappa_{Eq}=b_-+b_+,
    chi_{Eq}=b_--b_+.

The four directional support patterns are all realizable at the interface, so
an exact encoder needs at least four states.  (kappa,chi) realizes exactly four
and is therefore cardinality-minimal.  Multiplicative refinement is path-flat:
S_{E1*...*Em} depends only on the product.  Since consecutive multipliers are
coprime, after E>1 the double-hit state can never reappear.
"""

from __future__ import annotations

from math import gcd

from .legendre import square_carry
from .prime_brc_phase import square_midpoint_defect
from .prime_brc_shadow_staircase import cross_denominator_edge


SUPPORT_TO_CARRY = {
    (0, 0): (0, 0),
    (1, 0): (1, 1),
    (0, 1): (1, -1),
    (1, 1): (2, 0),
}
CARRY_TO_SUPPORT = {value: key for key, value in SUPPORT_TO_CARRY.items()}


def support_to_carry(lower_bit: int, upper_bit: int) -> tuple[int, int]:
    key = (lower_bit, upper_bit)
    if key not in SUPPORT_TO_CARRY:
        raise ValueError("directional bits must lie in {0,1}^2")
    return SUPPORT_TO_CARRY[key]


def carry_to_support(kappa: int, chi: int) -> tuple[int, int]:
    key = (kappa, chi)
    if key not in CARRY_TO_SUPPORT:
        raise ValueError("(kappa,chi) is not one of the four exact carry states")
    return CARRY_TO_SUPPORT[key]


def shadow_refinement_state(k: int, p: int, cumulative_scale: int) -> dict[str, object]:
    """Return exact support/carry state at modulus E*q on one shadow edge."""
    if cumulative_scale < 1:
        raise ValueError("cumulative_scale must be positive")
    edge = cross_denominator_edge(k, p)
    if edge["edge"] != 1:
        raise ValueError("p must support a shadow edge")
    a = p
    q = int(edge["q"])
    E = cumulative_scale
    support = (int(a % E == 0), int((a + 1) % E == 0))
    kappa = square_carry(k, E * q)
    chi = square_midpoint_defect(k, E * q)
    if (kappa, chi) != support_to_carry(*support):
        raise AssertionError("scaled (kappa,chi) failed exact support encoding")
    if E > 1 and support == (1, 1):
        raise AssertionError("coprime adjacent multipliers resurrected double support")
    return {
        "k": k,
        "p": p,
        "q": q,
        "scale": E,
        "support": support,
        "kappa": kappa,
        "chi": chi,
    }


def shadow_refinement_path(k: int, p: int, factors: tuple[int, ...]) -> dict[str, object]:
    """Replay a scale-factor path and verify path-flat no-resurrection transitions."""
    if not factors:
        raise ValueError("at least one scale factor is required")
    cumulative = 1
    records = [shadow_refinement_state(k, p, 1)]
    previous_support = (1, 1)
    for factor in factors:
        if factor < 2:
            raise ValueError("scale factors must be >=2")
        cumulative *= factor
        state = shadow_refinement_state(k, p, cumulative)
        support = tuple(state["support"])
        # Refinement can only delete side support; it cannot create a side that
        # was already absent at a divisor scale.
        if support[0] > previous_support[0] or support[1] > previous_support[1]:
            raise AssertionError("shadow refinement resurrected deleted support")
        records.append(state)
        previous_support = support
    direct = shadow_refinement_state(k, p, cumulative)
    if records[-1]["support"] != direct["support"]:
        raise AssertionError("shadow refinement failed product path flattening")
    return {
        "factors": factors,
        "cumulative_scale": cumulative,
        "records": tuple(records),
        "final_support": direct["support"],
    }


def minimal_state_certificate() -> dict[str, object]:
    """Cardinality-minimality certificate for directional boundary support.

    Four distinct support patterns must remain distinguishable if future
    observables can ask lower-hit and upper-hit separately.  Any exact complete
    encoder therefore needs >=4 labels.  The (kappa,chi) image has exactly four.
    This is the finite cardinality/no-resurrection sense of minimality.
    """
    supports = tuple(SUPPORT_TO_CARRY)
    codes = tuple(SUPPORT_TO_CARRY.values())
    if len(set(supports)) != 4 or len(set(codes)) != 4:
        raise AssertionError("four-state support/carry bijection failed")
    return {
        "support_patterns": supports,
        "carry_codes": codes,
        "required_state_count": 4,
        "realized_state_count": 4,
        "minimum_bits": 2,
        "status": "CARDINALITY_MINIMAL_EXACT_DIRECTIONAL_SUPPORT_ENCODER",
    }
