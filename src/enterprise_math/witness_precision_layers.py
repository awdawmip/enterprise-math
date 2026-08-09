"""Layered lower bounds and non-degeneracy overhead for P025 witnesses.

The exact witness precision ``mu`` is the first L-infinity radius containing a
relation-adapted witness outside the Wronskian-degeneracy sublattice.  This
module separates three questions:

* ``lambda_abc``: what the arithmetic multiplicity demand already forces;
* ``rho``: when the additive witness lattice first contains any nonzero state;
* ``mu``: when a non-degenerate certificate first exists.

No new shortest-vector theory is claimed.  The purpose is to provide exact
counterexamples to unsafe state erasure between these task layers.
"""

from __future__ import annotations

from itertools import product

from .abc_support import abc_support_state
from .abc_witness_precision import (
    additive_relation_vector,
    minimal_witness_cost,
    witness_coordinates,
)
from .witness_precision_bracket import (
    abc_demand_floor,
    sparse_two_coordinate_upper_bound,
)


def minimal_additive_radius(
    a: int,
    b: int,
    c: int,
    *,
    max_bound: int = 32,
    state_cap: int = 2_000_000,
) -> int:
    """Return the first L-infinity radius containing a nonzero additive witness."""
    abc_support_state(a, b, c)
    if isinstance(max_bound, bool) or not isinstance(max_bound, int) or max_bound < 1:
        raise ValueError("max_bound must be a positive integer")
    if isinstance(state_cap, bool) or not isinstance(state_cap, int) or state_cap < 1:
        raise ValueError("state_cap must be a positive integer")

    coordinates = witness_coordinates(a, b, c)
    alpha = additive_relation_vector(a, b, c)
    examined = 0
    for radius in range(1, max_bound + 1):
        alphabet = range(-radius, radius + 1)
        for vector in product(alphabet, repeat=len(coordinates)):
            if max(abs(value) for value in vector) != radius:
                continue
            examined += 1
            if examined > state_cap:
                raise ValueError("state_cap exceeded before additive radius was found")
            if sum(coefficient * value for coefficient, value in zip(alpha, vector, strict=True)) == 0:
                return radius
    raise ValueError("no nonzero additive witness found within max_bound")


def witness_precision_layer_profile(
    a: int,
    b: int,
    c: int,
    *,
    max_bound: int = 32,
    state_cap: int = 2_000_000,
) -> dict[str, object]:
    """Return lambda_abc, rho, mu and U2 with exact layer gaps."""
    abc_support_state(a, b, c)
    demand = int(abc_demand_floor(a, b, c)["lambda_abc"])
    additive = minimal_additive_radius(
        a, b, c, max_bound=max_bound, state_cap=state_cap
    )
    upper = int(sparse_two_coordinate_upper_bound(a, b, c)["U2"])
    exact = minimal_witness_cost(
        a, b, c, max_bound=max(max_bound, upper), state_cap=state_cap
    )
    lower = max(demand, additive)
    if not (demand <= exact and additive <= exact <= upper):
        raise AssertionError("witness precision layers are inconsistent")
    return {
        "triple": (a, b, c),
        "lambda_abc": demand,
        "rho": additive,
        "combined_floor": lower,
        "mu": exact,
        "U2": upper,
        "demand_gap": exact - demand,
        "additive_gap": exact - additive,
        "nondegeneracy_overhead": exact - lower,
        "upper_gap": upper - exact,
    }


def exact_degeneracy_barrier_examples() -> tuple[dict[str, object], ...]:
    """Return fixed exact P025 counterexamples used by the regression suite."""
    return (
        witness_precision_layer_profile(1, 36, 37, max_bound=24),
        witness_precision_layer_profile(1, 53, 54, max_bound=27),
    )
