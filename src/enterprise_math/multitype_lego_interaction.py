"""Exact multi-type LEGO interaction basis on finite continuation inventories.

For type-count vectors n=(n_1,...,n_r), any bounded integer response table has
an exact product-binomial expansion

    phi(n) = sum_{k<=n} a_k prod_i C(n_i,k_i).

The coefficient a_k is the irreducible effect of selecting exactly k_i units of
continuation type i after all lower subconfigurations have been removed by
finite inclusion-exclusion.  No derivatives, real polynomial completion, or
Taylor remainder are used.

For one type this reduces exactly to the P011 repeated-unit binomial interaction
basis.  Coefficients with total order |k|>=2 are genuine multi-witness
interaction terms.  An additive type-inventory response has no such terms.
"""

from __future__ import annotations

from itertools import product
from math import comb

CountVector = tuple[int, ...]


def _require_vector(vector: CountVector, dimension: int | None = None) -> int:
    if not isinstance(vector, tuple) or not vector:
        raise ValueError("count vectors must be non-empty tuples")
    if dimension is not None and len(vector) != dimension:
        raise ValueError("count-vector dimension mismatch")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in vector):
        raise ValueError("count-vector entries must be non-negative integers")
    return len(vector)


def _subvectors(vector: CountVector):
    return product(*(range(value + 1) for value in vector))


def multitype_interaction_coefficient(
    response: dict[CountVector, int],
    order: CountVector,
) -> int:
    """Exact product-binomial finite-difference coefficient a_order."""
    dimension = _require_vector(order)
    result = 0
    for state in _subvectors(order):
        state = tuple(state)
        if state not in response:
            raise ValueError("response table must contain every subvector of order")
        value = response[state]
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("response values must be integers")
        parity = sum(o - s for o, s in zip(order, state))
        weight = 1
        for o, s in zip(order, state):
            weight *= comb(o, s)
        result += (-1 if parity % 2 else 1) * weight * value
    return result


def multitype_interaction_spectrum(
    response: dict[CountVector, int],
    maxima: CountVector,
) -> dict[CountVector, int]:
    """Return all a_k on the rectangular box 0<=k_i<=maxima_i."""
    dimension = _require_vector(maxima)
    coefficients: dict[CountVector, int] = {}
    for order in product(*(range(value + 1) for value in maxima)):
        order = tuple(order)
        _require_vector(order, dimension)
        coefficients[order] = multitype_interaction_coefficient(response, order)
    return coefficients


def reconstruct_multitype_response(
    coefficients: dict[CountVector, int],
    state: CountVector,
) -> int:
    """Exact phi(state)=sum_{k<=state} a_k prod_i C(state_i,k_i)."""
    dimension = _require_vector(state)
    result = 0
    for order in _subvectors(state):
        order = tuple(order)
        if order not in coefficients:
            raise ValueError("coefficient table must contain every subvector of state")
        coefficient = coefficients[order]
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise ValueError("interaction coefficients must be integers")
        weight = 1
        for n, k in zip(state, order):
            weight *= comb(n, k)
        result += coefficient * weight
    return result


def interaction_order(order: CountVector) -> int:
    _require_vector(order)
    return sum(order)


def higher_interaction_support(
    coefficients: dict[CountVector, int],
    minimum_order: int = 2,
) -> dict[CountVector, int]:
    if isinstance(minimum_order, bool) or not isinstance(minimum_order, int) or minimum_order < 0:
        raise ValueError("minimum_order must be a non-negative integer")
    return {
        order: coefficient
        for order, coefficient in coefficients.items()
        if interaction_order(order) >= minimum_order and coefficient != 0
    }


def additive_inventory_response_table(
    maxima: CountVector,
    unit_responses: tuple[int, ...],
    base: int = 0,
) -> dict[CountVector, int]:
    """Build phi(n)=base+sum_i n_i r_i for tests/reference."""
    dimension = _require_vector(maxima)
    if not isinstance(unit_responses, tuple) or len(unit_responses) != dimension:
        raise ValueError("unit_responses must match count-vector dimension")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in unit_responses):
        raise ValueError("unit responses must be integers")
    if isinstance(base, bool) or not isinstance(base, int):
        raise ValueError("base must be an integer")
    return {
        tuple(state): base + sum(n * r for n, r in zip(state, unit_responses))
        for state in product(*(range(value + 1) for value in maxima))
    }
