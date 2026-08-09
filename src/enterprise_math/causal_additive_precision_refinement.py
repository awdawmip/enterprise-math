"""Closed-form minimum future-safe refinement of a fixed block quotient.

Start with current observation q_d(n)=floor(n/d) and declared nonnegative
additive future generators U={u_i}.  Let

    g = gcd(d, u_1, ..., u_r).

Write the old basin remainder as r=g*a+s with 0<=s<g.  Every future sum is a
multiple of g, and q_d(n+future) depends on the old quotient q_d(n) and `a`, but
not on `s`.  Distinct values of a are distinguishable by some future word because
the normalized generators U/g generate the full residue group modulo D=d/g.

Therefore the exact future continuation partition inside every d-basin has
exactly D=d/g classes, represented by `a=floor((n mod d)/g)`.  The combined state
(q_d,a) is in bijection with the finer block quotient q_g(n).  Thus q_g is the
coarsest exact future refinement, not merely within block quotients but among all
deterministic state refinements that preserve the declared q_d observation.

Full remainder is required only when g=1; no detail is required when g=d.
"""

from __future__ import annotations

from collections import deque
from math import gcd


def _validate(block_capacity: int, generators: tuple[int, ...]) -> None:
    if isinstance(block_capacity, bool) or not isinstance(block_capacity, int) or block_capacity <= 0:
        raise ValueError("block_capacity must be a positive integer")
    if not isinstance(generators, tuple):
        raise ValueError("generators must be a tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in generators
    ):
        raise ValueError("generators must be non-negative integers")


def minimal_refinement_scale(
    block_capacity: int,
    generators: tuple[int, ...],
) -> int:
    _validate(block_capacity, generators)
    result = block_capacity
    for value in generators:
        result = gcd(result, value)
    return result


def continuation_type_count(
    block_capacity: int,
    generators: tuple[int, ...],
) -> int:
    g = minimal_refinement_scale(block_capacity, generators)
    return block_capacity // g


def continuation_type(
    units: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> int:
    if isinstance(units, bool) or not isinstance(units, int) or units < 0:
        raise ValueError("units must be non-negative integer")
    g = minimal_refinement_scale(block_capacity, generators)
    remainder = units % block_capacity
    return remainder // g


def coarse_quotient(units: int, block_capacity: int) -> int:
    if isinstance(units, bool) or not isinstance(units, int) or units < 0:
        raise ValueError("units must be non-negative integer")
    if isinstance(block_capacity, bool) or not isinstance(block_capacity, int) or block_capacity <= 0:
        raise ValueError("block_capacity must be positive")
    return units // block_capacity


def minimal_future_state(
    units: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> tuple[int, int]:
    return (
        coarse_quotient(units, block_capacity),
        continuation_type(units, block_capacity, generators),
    )


def refined_quotient(
    units: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> int:
    g = minimal_refinement_scale(block_capacity, generators)
    return coarse_quotient(units, g)


def minimal_state_matches_refined_quotient(
    units: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> bool:
    g = minimal_refinement_scale(block_capacity, generators)
    d_over_g = block_capacity // g
    quotient, tau = minimal_future_state(units, block_capacity, generators)
    return refined_quotient(units, block_capacity, generators) == d_over_g * quotient + tau


def _normalized_residue_witness(
    modulus: int,
    normalized_generators: tuple[int, ...],
    target_residue: int,
) -> int:
    """Nonnegative generated normalized sum with requested residue modulo modulus."""
    if modulus == 1:
        return 0
    generators = tuple(value % modulus for value in normalized_generators if value % modulus != 0)
    if not generators:
        raise ValueError("normalized generators do not generate a nontrivial residue group")
    queue = deque([0])
    witness = {0: 0}
    while queue:
        residue = queue.popleft()
        current_sum = witness[residue]
        for generator in generators:
            next_residue = (residue + generator) % modulus
            if next_residue in witness:
                continue
            witness[next_residue] = current_sum + generator
            queue.append(next_residue)
    target = target_residue % modulus
    if target not in witness:
        raise ValueError("declared generators do not reach requested residue")
    return witness[target]


def distinguishing_future_sum(
    left_type: int,
    right_type: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> int | None:
    """Construct one future sum separating two distinct continuation types.

    The returned sum is a nonnegative combination modulo D of normalized
    generators.  For equal types no future can distinguish them, so returns None.
    """
    g = minimal_refinement_scale(block_capacity, generators)
    D = block_capacity // g
    if any(
        isinstance(value, bool) or not isinstance(value, int) or not (0 <= value < D)
        for value in (left_type, right_type)
    ):
        raise ValueError("types must lie in the continuation range")
    if left_type == right_type:
        return None
    positive = tuple(value for value in generators if value > 0)
    if not positive:
        raise ValueError("distinct types cannot occur without positive generators")
    normalized = tuple(value // g for value in positive)
    # Aim to place the larger type exactly on a D-boundary; the smaller then lies
    # strictly below it.  Swap if needed.
    high = max(left_type, right_type)
    normalized_sum = _normalized_residue_witness(
        D,
        normalized,
        (-high) % D,
    )
    return g * normalized_sum


def future_quotient_after_sum(
    initial_type: int,
    future_sum: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> int:
    """Coarse q_d increment starting from basin quotient zero and given type."""
    g = minimal_refinement_scale(block_capacity, generators)
    representative = g * initial_type
    return (representative + future_sum) // block_capacity


def types_are_future_distinguishable(
    left_type: int,
    right_type: int,
    block_capacity: int,
    generators: tuple[int, ...],
) -> bool:
    if left_type == right_type:
        return False
    future_sum = distinguishing_future_sum(
        left_type,
        right_type,
        block_capacity,
        generators,
    )
    if future_sum is None:
        return False
    return future_quotient_after_sum(
        left_type, future_sum, block_capacity, generators
    ) != future_quotient_after_sum(
        right_type, future_sum, block_capacity, generators
    )
