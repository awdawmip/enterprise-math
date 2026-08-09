"""Higher-channel signed-permutation quotient and exact path-lift repair.

For d labelled signed channels with microscopic increments in {−1,+1}^d,
observe only the hyperoctahedral/B_d orbit representative

    q(x) = sort(abs(x_1),...,abs(x_d)).

For one coarse transition p->q, every labelled lift of p has the same number
m(p,q) of microscopic sign steps landing in orbit q.  The multiplicity is the
coefficient of the finite commutative polynomial

    product_i (z_|p_i-1| + z_(p_i+1)).

At p_i=0 the two signs both land at magnitude one, so that factor is 2*z_1.
A complete coarse path has microscopic fiber size equal to the product of its
transition multiplicities.

Rank two is special: all local factors are powers of two, recovering the old
binary E+B repair.  Rank three already has factor 3, so the general repair
coordinate is mixed-radix/integer rather than intrinsically binary.
"""

from __future__ import annotations

from collections import defaultdict
from math import prod

ChamberState = tuple[int, ...]
ChamberPath = tuple[ChamberState, ...]


def _require_dimension(dimension: int) -> None:
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension <= 0:
        raise ValueError("dimension must be a positive integer")


def _require_chamber_state(state: ChamberState) -> None:
    if not isinstance(state, tuple) or not state:
        raise ValueError("state must be a nonempty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in state
    ):
        raise ValueError("chamber entries must be non-negative integers")
    if tuple(sorted(state)) != state:
        raise ValueError("chamber state must be nondecreasing")


def canonical_bd_chamber(state: tuple[int, ...]) -> ChamberState:
    """Canonical B_d signed-permutation orbit representative."""
    if not isinstance(state, tuple) or not state:
        raise ValueError("state must be a nonempty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("state entries must be integers")
    return tuple(sorted(abs(value) for value in state))


def transition_multiplicity(previous: ChamberState, current: ChamberState) -> int:
    """Exact microscopic sign-step count for one chamber transition.

    The implementation evaluates the coefficient of

        product_i (z_|p_i-1| + z_(p_i+1))

    by a finite multiset dynamic program.  A polynomial monomial is represented
    by its sorted tuple of output magnitudes.  Repeated destinations accumulate
    their integer coefficients automatically.
    """
    _require_chamber_state(previous)
    _require_chamber_state(current)
    if len(previous) != len(current):
        raise ValueError("transition states must have equal dimension")

    terms: dict[tuple[int, ...], int] = {(): 1}
    for value in previous:
        destinations = (abs(value - 1), value + 1)
        next_terms: dict[tuple[int, ...], int] = defaultdict(int)
        for partial, coefficient in terms.items():
            for destination in destinations:
                monomial = tuple(sorted(partial + (destination,)))
                next_terms[monomial] += coefficient
        terms = dict(next_terms)
    return terms.get(current, 0)


def transition_spectrum(previous: ChamberState) -> tuple[tuple[ChamberState, int], ...]:
    """All reachable next chamber states and exact lift multiplicities."""
    _require_chamber_state(previous)
    terms: dict[tuple[int, ...], int] = {(): 1}
    for value in previous:
        destinations = (abs(value - 1), value + 1)
        next_terms: dict[tuple[int, ...], int] = defaultdict(int)
        for partial, coefficient in terms.items():
            for destination in destinations:
                monomial = tuple(sorted(partial + (destination,)))
                next_terms[monomial] += coefficient
        terms = dict(next_terms)
    return tuple(sorted(terms.items()))


def path_lift_factors(path: ChamberPath) -> tuple[int, ...]:
    """Local mixed-radix factors of a chamber path starting at the origin."""
    if not isinstance(path, tuple):
        raise ValueError("path must be a tuple")
    if not path:
        return ()
    for state in path:
        _require_chamber_state(state)
    dimension = len(path[0])
    _require_dimension(dimension)
    if any(len(state) != dimension for state in path):
        raise ValueError("all path states must have the same dimension")

    previous = (0,) * dimension
    factors = []
    for current in path:
        multiplicity = transition_multiplicity(previous, current)
        if multiplicity <= 0:
            raise ValueError("path contains a non-realizable chamber transition")
        factors.append(multiplicity)
        previous = current
    return tuple(factors)


def path_lift_count(path: ChamberPath) -> int:
    """Exact number of labelled microscopic sign paths lifting one coarse path."""
    return prod(path_lift_factors(path), start=1)


def is_power_of_two(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    return value & (value - 1) == 0


def path_is_binary_repair(path: ChamberPath) -> bool:
    """Whether every local repair radix is a power of two."""
    return all(is_power_of_two(factor) for factor in path_lift_factors(path))


def first_rank_three_nonbinary_transition() -> tuple[ChamberState, ChamberState, int]:
    """Minimal clean rank-three factor-3 example."""
    previous = (1, 1, 1)
    current = (0, 0, 2)
    multiplicity = transition_multiplicity(previous, current)
    if multiplicity != 3:
        raise AssertionError("rank-three equal-cluster split must have multiplicity three")
    return previous, current, multiplicity
