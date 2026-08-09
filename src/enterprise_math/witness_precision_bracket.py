"""Exact lower/upper brackets for P025 relation-conditioned witness precision.

This module combines two already-explicit P025 structures:

* arithmetic witness-budget demand from ``arithmetic_witness_budget``;
* the additive/degeneracy generator rows from ``abc_witness_precision``.

For a primitive abc triple with a non-degenerate witness family it produces

    lambda_abc <= mu <= U_2,

where ``lambda_abc`` is a triple-only arithmetic demand floor and ``U_2`` is an
explicit sparse two-coordinate witness bound read directly from nonzero Pluecker
minors of the generator rows.  The construction is finite integer arithmetic;
it is not an abc proof and does not claim the underlying lattice algebra as new.
"""

from __future__ import annotations

from math import gcd

from .abc_support import abc_support_state, multiplicity_residual, prime_factorization, radical
from .abc_witness_precision import (
    additive_relation_vector,
    is_nondegenerate_witness,
    minimal_witness_cost,
    witness_coordinates,
    wronskian_relation_vector,
)
from .core import integer_nth_root


def normalized_derivative_weight(n: int) -> int:
    """Return A(n)/m(n) = sum_(p|n) rad(n)/p * v_p(n)."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    r = radical(n)
    return sum((r // prime) * exponent for prime, exponent in prime_factorization(n))


def normalized_pair_capacity(x: int, y: int) -> int:
    """Return the residual-normalized coefficient mass K_(x,y).

    If H_(x,y) is the norm-budget coefficient mass from Supplement 05, then

        H_(x,y) = m(x) m(y) K_(x,y).
    """
    for name, value in (("x", x), ("y", y)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    return (
        radical(x) * normalized_derivative_weight(y)
        + radical(y) * normalized_derivative_weight(x)
    )


def target_demand_floor(a: int, b: int, c: int, target_index: int) -> int:
    """Return ceil(m(target)/K(complement)) for one target orientation."""
    abc_support_state(a, b, c)
    if target_index not in (0, 1, 2):
        raise ValueError("target_index must be 0, 1, or 2")
    values = (a, b, c)
    complement = tuple(index for index in range(3) if index != target_index)
    capacity = normalized_pair_capacity(values[complement[0]], values[complement[1]])
    if capacity <= 0:
        raise ValueError("complementary normalized capacity must be positive")
    demand = multiplicity_residual(values[target_index])
    return (demand + capacity - 1) // capacity


def abc_demand_floor(a: int, b: int, c: int) -> dict[str, object]:
    """Return the strongest orientation-combined arithmetic lower bound on mu."""
    abc_support_state(a, b, c)
    floors = tuple(target_demand_floor(a, b, c, index) for index in range(3))
    capacities = tuple(
        normalized_pair_capacity(*tuple((a, b, c)[j] for j in range(3) if j != index))
        for index in range(3)
    )
    residuals = tuple(multiplicity_residual(value) for value in (a, b, c))
    return {
        "triple": (a, b, c),
        "residuals": residuals,
        "target_capacities": capacities,
        "target_floors": floors,
        "lambda_abc": max(floors),
    }


def sparse_two_coordinate_candidates(a: int, b: int, c: int) -> tuple[dict[str, object], ...]:
    """Construct all non-degenerate two-coordinate witnesses from row minors.

    Let alpha be the primitive additive normal and beta the degeneracy normal.
    For coordinates i<j with omega_ij=alpha_i beta_j-alpha_j beta_i != 0,
    put g=gcd(|alpha_i|,|alpha_j|) and choose the primitive kernel vector

        x_i = alpha_j/g,  x_j = -alpha_i/g,

    with all other coordinates zero.  Then alpha*x=0 and beta*x is nonzero.
    """
    abc_support_state(a, b, c)
    coordinates = witness_coordinates(a, b, c)
    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    candidates: list[dict[str, object]] = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            minor = alpha[i] * beta[j] - alpha[j] * beta[i]
            if minor == 0:
                continue
            content = gcd(abs(alpha[i]), abs(alpha[j]))
            if content == 0:
                raise AssertionError("nonzero row minor cannot have both alpha entries zero")
            vector = [0] * len(coordinates)
            vector[i] = alpha[j] // content
            vector[j] = -alpha[i] // content
            witness = tuple(vector)
            if not is_nondegenerate_witness(a, b, c, witness):
                raise AssertionError("Pluecker-minor construction failed non-degeneracy")
            cost = max(abs(value) for value in witness)
            candidates.append(
                {
                    "indices": (i, j),
                    "primes": (coordinates[i], coordinates[j]),
                    "minor": minor,
                    "vector": witness,
                    "cost": cost,
                }
            )
    if not candidates:
        raise ValueError("no nonzero generator minor; witness family is degenerate")
    return tuple(candidates)


def sparse_two_coordinate_upper_bound(a: int, b: int, c: int) -> dict[str, object]:
    """Return the cheapest explicit two-coordinate non-degenerate witness."""
    candidates = sparse_two_coordinate_candidates(a, b, c)
    best = min(
        candidates,
        key=lambda item: (
            int(item["cost"]),
            tuple(item["primes"]),
            tuple(item["vector"]),
        ),
    )
    return {
        "U2": int(best["cost"]),
        "best_candidate": best,
        "candidate_count": len(candidates),
    }


def witness_precision_bracket(
    a: int,
    b: int,
    c: int,
    *,
    verify_exact: bool = False,
    max_bound: int = 32,
    state_cap: int = 2_000_000,
) -> dict[str, object]:
    """Return lambda_abc <= mu <= U2 and optionally verify the exact mu."""
    lower_data = abc_demand_floor(a, b, c)
    upper_data = sparse_two_coordinate_upper_bound(a, b, c)
    lower = int(lower_data["lambda_abc"])
    upper = int(upper_data["U2"])
    if lower > upper:
        raise AssertionError("arithmetic demand floor exceeds explicit witness upper bound")
    result: dict[str, object] = {
        **lower_data,
        **upper_data,
        "width": upper - lower,
        "certified_exact": lower == upper,
    }
    if verify_exact:
        exact = minimal_witness_cost(
            a, b, c, max_bound=max(max_bound, upper), state_cap=state_cap
        )
        if not (lower <= exact <= upper):
            raise AssertionError("exact witness precision escaped the certified bracket")
        result["mu"] = exact
        result["lower_gap"] = exact - lower
        result["upper_gap"] = upper - exact
    return result


def high_quality_witness_floor(
    a: int, b: int, c: int, u: int, v: int
) -> dict[str, object]:
    """Transport the P025 high-quality residual horizon to witness precision.

    If c^v > rad(abc)^u with u>v, the earlier P025 residual theorem gives

        m_max > R_(3u)(c^(u-v)(c-1)^u).

    Since every target residual obeys m_i <= K_i * mu, using K_max yields

        mu >= floor(root_horizon / K_max) + 1.

    The returned bound is conditional; ``high_quality`` records whether the
    premise actually holds.
    """
    abc_support_state(a, b, c)
    if isinstance(u, bool) or not isinstance(u, int) or u <= 0:
        raise ValueError("u must be a positive integer")
    if isinstance(v, bool) or not isinstance(v, int) or v <= 0 or v >= u:
        raise ValueError("require positive integers u>v")
    rad_abc = radical(a * b * c)
    high_quality = c**v > rad_abc**u
    threshold = c ** (u - v) * (c - 1) ** u
    root_horizon = integer_nth_root(threshold, 3 * u)
    capacities = tuple(int(value) for value in abc_demand_floor(a, b, c)["target_capacities"])
    max_capacity = max(capacities)
    floor = root_horizon // max_capacity + 1 if high_quality else 0
    return {
        "high_quality": high_quality,
        "u": u,
        "v": v,
        "root_horizon": root_horizon,
        "max_target_capacity": max_capacity,
        "witness_floor": floor,
    }
