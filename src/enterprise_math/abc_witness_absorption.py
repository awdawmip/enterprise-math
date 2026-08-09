"""Absorption-aware witness diagnostics for the P025 abc pressure test.

This module refines the scalar witness-radius view from ``abc_witness_precision``.
For a Pasten-style relation-adapted arithmetic derivative, the arithmetic
Wronskian is an exact integer linear form on the additive witness lattice.  The
multiplicity residual product divides every non-zero Wronskian value, so each
witness has a second discrete cost: the positive integer absorption redundancy
``|W| / M``.

The lattice/determinantal-divisor facts used here are standard integer linear
algebra.  P025 uses them only as a finite-state pressure test; this module does
not prove the abc conjecture and does not claim the underlying Smith/Pluecker or
Pareto mathematics as new.
"""

from __future__ import annotations

from math import gcd

from .abc_support import abc_support_state, prime_factorization
from .abc_witness_precision import (
    additive_relation_vector,
    bounded_nondegenerate_witnesses,
    is_nondegenerate_witness,
    witness_coordinates,
)


def _require_vector_dimension(
    a: int, b: int, c: int, vector: tuple[int, ...]
) -> tuple[int, ...]:
    coordinates = witness_coordinates(a, b, c)
    if len(vector) != len(coordinates):
        raise ValueError("witness vector dimension does not match prime coordinates")
    return coordinates


def _valuation_map(n: int) -> dict[int, int]:
    return dict(prime_factorization(n))


def raw_wronskian_vector(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the canonically scaled integer row for ``W^psi(a,b)``.

    Unlike ``wronskian_relation_vector`` this row is *not* primitive-normalized:
    its arithmetic scale matters when the future language observes ``|W|``.
    """
    coordinates = witness_coordinates(a, b, c)
    va = _valuation_map(a)
    vb = _valuation_map(b)
    return tuple(
        (a * b * vb.get(prime, 0) // prime if prime in vb else 0)
        - (a * b * va.get(prime, 0) // prime if prime in va else 0)
        for prime in coordinates
    )


def arithmetic_derivative_value(
    a: int,
    b: int,
    c: int,
    n: int,
    vector: tuple[int, ...],
) -> int:
    """Evaluate Pasten's finite-support arithmetic derivative exactly."""
    coordinates = _require_vector_dimension(a, b, c, vector)
    values = dict(zip(coordinates, vector, strict=True))
    return sum(
        n * exponent // prime * values[prime]
        for prime, exponent in prime_factorization(n)
    )


def arithmetic_wronskian_value(
    a: int, b: int, c: int, vector: tuple[int, ...]
) -> int:
    """Evaluate ``a*d(b)-b*d(a)`` as an exact integer."""
    _require_vector_dimension(a, b, c, vector)
    direct = a * arithmetic_derivative_value(a, b, c, b, vector) - b * arithmetic_derivative_value(
        a, b, c, a, vector
    )
    row_value = sum(
        coefficient * entry
        for coefficient, entry in zip(raw_wronskian_vector(a, b, c), vector, strict=True)
    )
    if direct != row_value:
        raise AssertionError("Wronskian row disagrees with direct arithmetic derivative")
    return direct


def multiplicity_residual_product(a: int, b: int, c: int) -> int:
    """Return ``M=m(a)m(b)m(c)=abc/rad(abc)`` for a primitive abc triple."""
    data = abc_support_state(a, b, c)
    result = 1
    for residual in data["residuals"]:
        result *= int(residual)
    return result


def witness_absorption_redundancy(
    a: int, b: int, c: int, vector: tuple[int, ...]
) -> int:
    """Return the positive integer ``eta=|W|/M`` for a non-degenerate witness."""
    if not is_nondegenerate_witness(a, b, c, vector):
        raise ValueError("vector must be a non-degenerate additive witness")
    wronskian = abs(arithmetic_wronskian_value(a, b, c, vector))
    residual = multiplicity_residual_product(a, b, c)
    if wronskian == 0 or wronskian % residual != 0:
        raise AssertionError("multiplicity residual product must divide the Wronskian")
    return wronskian // residual


def _wedge_coordinates(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    if len(left) != len(right):
        raise ValueError("wedge vectors must have equal dimension")
    return tuple(
        left[i] * right[j] - left[j] * right[i]
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )


def _content(entries: tuple[int, ...]) -> int:
    value = 0
    for entry in entries:
        value = gcd(value, abs(entry))
    return value


def scaled_wronskian_signature(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the sign-normalized *scaled* exterior signature ``alpha wedge beta``.

    The primitive additive normal ``alpha`` fixes the witness lattice.  Keeping
    the full content of ``alpha wedge beta`` (rather than projectivizing it)
    retains the scale of the Wronskian functional on that lattice.  Global sign
    is irrelevant because the absorption observable uses ``|W|``.
    """
    alpha = additive_relation_vector(a, b, c)
    omega = _wedge_coordinates(alpha, raw_wronskian_vector(a, b, c))
    if not omega or all(entry == 0 for entry in omega):
        raise ValueError("Wronskian functional is degenerate on the additive lattice")
    first_nonzero = next(entry for entry in omega if entry != 0)
    if first_nonzero < 0:
        omega = tuple(-entry for entry in omega)
    return omega


def minimum_absorption_redundancy(a: int, b: int, c: int) -> int:
    """Return the exact minimum positive ``|W|/M`` over all additive witnesses.

    For primitive ``alpha``, the image of the integer functional ``beta`` on
    ``ker_Z(alpha)`` is ``d Z``, where ``d`` is the gcd/content of the 2x2 minors
    of ``[alpha; beta]``.  These minors are exactly ``alpha wedge beta``.
    """
    step = _content(scaled_wronskian_signature(a, b, c))
    residual = multiplicity_residual_product(a, b, c)
    if step == 0 or step % residual != 0:
        raise AssertionError("Wronskian image step must be a positive multiple of M")
    return step // residual


def _pareto_pairs(pairs: set[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    frontier = []
    for pair in pairs:
        if any(
            other[0] <= pair[0]
            and other[1] <= pair[1]
            and other != pair
            for other in pairs
        ):
            continue
        frontier.append(pair)
    return tuple(sorted(frontier))


def certified_absorption_pareto_frontier(
    a: int,
    b: int,
    c: int,
    *,
    max_bound: int = 32,
    state_cap: int = 2_000_000,
) -> tuple[tuple[int, int], ...]:
    """Return the exact Pareto frontier ``(||x||_inf, eta(x))`` when certified.

    Enumeration stops once a witness attains the mathematically exact minimum
    absorption redundancy.  At that radius, every witness outside the searched
    ball has larger norm and absorption redundancy at least that minimum, so it
    cannot add a new Pareto-minimal pair.
    """
    if isinstance(max_bound, bool) or not isinstance(max_bound, int) or max_bound < 1:
        raise ValueError("max_bound must be a positive integer")
    eta_floor = minimum_absorption_redundancy(a, b, c)
    seen: set[tuple[int, int]] = set()
    for bound in range(1, max_bound + 1):
        witnesses = bounded_nondegenerate_witnesses(
            a, b, c, bound, state_cap=state_cap
        )
        for vector in witnesses:
            norm = max(abs(entry) for entry in vector)
            eta = witness_absorption_redundancy(a, b, c, vector)
            seen.add((norm, eta))
        if any(eta == eta_floor for _norm, eta in seen):
            return _pareto_pairs(seen)
    raise ValueError("absorption-optimal witness not found within max_bound")


def absorption_tradeoff_examples() -> dict[str, object]:
    """Return exact small counterexamples to scalar witness-cost completeness."""
    first = (2, 3, 5)
    second = (5, 7, 12)
    first_frontier = certified_absorption_pareto_frontier(*first, max_bound=3)
    second_frontier = certified_absorption_pareto_frontier(*second, max_bound=3)
    if first_frontier != ((1, 2), (2, 1)):
        raise AssertionError("2+3=5 tradeoff frontier changed")
    if second_frontier != ((1, 6), (2, 2)):
        raise AssertionError("5+7=12 tradeoff frontier changed")
    return {
        "perfect_absorption_tradeoff": {
            "triple": first,
            "frontier": first_frontier,
            "minimum_absorption_redundancy": minimum_absorption_redundancy(*first),
        },
        "irreducible_absorption_overhead": {
            "triple": second,
            "frontier": second_frontier,
            "minimum_absorption_redundancy": minimum_absorption_redundancy(*second),
        },
    }


def mason_degree_slack(
    deg_a: int,
    deg_b: int,
    deg_c: int,
    radical_degree: int,
    wronskian_degree: int,
) -> dict[str, int]:
    """Decompose the degree margin in the classical Wronskian proof.

    If ``D=deg(a)+deg(b)+deg(c)-deg(rad(abc))`` satisfies
    ``D <= deg(W) <= deg(a)+deg(b)-1``, then exactly

    ``deg(rad(abc))-deg(c)-1 = (deg(W)-D) + (deg(a)+deg(b)-1-deg(W))``.

    The two non-negative terms are called absorption slack and capacity slack
    here only as P025 diagnostic language; the identity is elementary algebra.
    """
    values = (deg_a, deg_b, deg_c, radical_degree, wronskian_degree)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("all degrees must be non-negative integers")
    if deg_a + deg_b == 0:
        raise ValueError("Wronskian capacity requires deg(a)+deg(b)>=1")
    residual_degree = deg_a + deg_b + deg_c - radical_degree
    capacity = deg_a + deg_b - 1
    if residual_degree < 0:
        raise ValueError("residual degree must be non-negative")
    if not (residual_degree <= wronskian_degree <= capacity):
        raise ValueError("require residual_degree <= wronskian_degree <= capacity")
    absorption_slack = wronskian_degree - residual_degree
    capacity_slack = capacity - wronskian_degree
    theorem_margin = radical_degree - deg_c - 1
    if theorem_margin != absorption_slack + capacity_slack:
        raise AssertionError("Mason slack decomposition failed")
    return {
        "residual_degree": residual_degree,
        "wronskian_capacity": capacity,
        "absorption_slack": absorption_slack,
        "capacity_slack": capacity_slack,
        "theorem_margin": theorem_margin,
    }
