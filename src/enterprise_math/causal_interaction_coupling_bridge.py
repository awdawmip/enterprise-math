"""Bridge between local LEGO response interaction and causal signature coupling.

A nonlinear/cross response does not automatically create new causal information.
It creates additional signature distinction exactly when it fails to descend
through the currently available marginal signature map.

This module implements the finite fiber-constant criterion from the causal
signature viewpoint.  No numeric norm, probability, or interaction tensor is
required.
"""

from __future__ import annotations

from typing import Hashable


State = Hashable
Marginal = Hashable
Response = Hashable


def response_descends_through_marginals(
    state_to_marginal: dict[State, Marginal],
    response: dict[State, Response],
) -> bool:
    """Whether response is constant on every marginal-signature fiber."""
    if not isinstance(state_to_marginal, dict) or not state_to_marginal:
        raise ValueError("state_to_marginal must be a non-empty dict")
    if set(response) != set(state_to_marginal):
        raise ValueError("response must be defined on exactly the same states")
    seen: dict[Marginal, Response] = {}
    for state, marginal in state_to_marginal.items():
        value = response[state]
        if marginal in seen and seen[marginal] != value:
            return False
        seen[marginal] = value
    return True


def response_split_excess(
    state_to_marginal: dict[State, Marginal],
    response: dict[State, Response],
) -> int:
    """How many extra classes appear after adjoining one joint response."""
    if set(response) != set(state_to_marginal):
        raise ValueError("response must be defined on exactly the same states")
    marginal_classes = set(state_to_marginal.values())
    refined_classes = {
        (state_to_marginal[state], response[state])
        for state in state_to_marginal
    }
    return len(refined_classes) - len(marginal_classes)


def induced_response_map(
    state_to_marginal: dict[State, Marginal],
    response: dict[State, Response],
) -> dict[Marginal, Response]:
    """Return the unique coarse response when descent is valid."""
    if not response_descends_through_marginals(state_to_marginal, response):
        raise ValueError("response does not descend through marginal signatures")
    result: dict[Marginal, Response] = {}
    for state, marginal in state_to_marginal.items():
        result[marginal] = response[state]
    return result


def binary_lego_interaction(
    response00: int,
    response10: int,
    response01: int,
    response11: int,
) -> int:
    """Exact two-unit inclusion-exclusion interaction coefficient."""
    values = (response00, response10, response01, response11)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("responses must be integers")
    return response11 - response10 - response01 + response00
