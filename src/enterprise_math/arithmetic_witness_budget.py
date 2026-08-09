"""Exact integer witness-budget layers for the P025 abc pressure test.

This module is a finite-state unpacking of the arithmetic-derivative/Wronskian
machinery used by Pasten.  It does not claim the derivative, Wronskian, abc
estimate, or triangle/norm inequalities as new mathematics.

For a primitive relation a+b=c and a relation-adapted non-degenerate derivation
psi, the module exposes the exact chain

    M <= |W^psi| <= B_abs <= B_norm,

where

* M = abc / rad(abc) is the multiplicity residual demand;
* |W^psi| is the actual arithmetic Wronskian witness;
* B_abs forgets sign cancellation between prime-coordinate contributions;
* B_norm forgets the coordinate distribution and retains only ||psi||_infinity.

The three successive non-negative gaps telescope exactly.  This is intended as
a precision/proof-state diagnostic, not as a stronger abc theorem.
"""

from __future__ import annotations

from collections.abc import Mapping

from .abc_support import abc_support_state, multiplicity_residual, prime_factorization


def _require_int_mapping(values: Mapping[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for prime, value in values.items():
        if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
            raise ValueError("derivation coordinates must use integer prime labels >= 2")
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("derivation coordinate values must be integers")
        result[prime] = value
    return result


def support_primes(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the sorted prime support of a primitive abc triple."""
    data = abc_support_state(a, b, c)
    return tuple(sorted(set().union(*(set(s) for s in data["supports"]))))


def arithmetic_derivative(n: int, values: Mapping[int, int]) -> int:
    """Evaluate Pasten's prime-coordinate arithmetic derivative exactly.

    For x_p = psi(xi_p),

        d^psi(n) = sum_{p|n} (n/p) v_p(n) x_p.

    Every summand is integral.  Coordinates absent from ``values`` are treated
    as zero.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    psi = _require_int_mapping(values)
    return sum((n // prime) * exponent * psi.get(prime, 0) for prime, exponent in prime_factorization(n))


def derivation_norm_on_abc(
    a: int, b: int, c: int, values: Mapping[int, int]
) -> int:
    """Return the L-infinity norm on the declared abc support.

    Nonzero coordinates outside supp(abc) are rejected, matching the
    support-restricted witness language used for T(a,b).
    """
    psi = _require_int_mapping(values)
    coordinates = support_primes(a, b, c)
    coordinate_set = set(coordinates)
    if any(value != 0 and prime not in coordinate_set for prime, value in psi.items()):
        raise ValueError("nonzero derivation coordinate lies outside supp(abc)")
    return max((abs(psi.get(prime, 0)) for prime in coordinates), default=0)


def is_relation_adapted(
    a: int, b: int, c: int, values: Mapping[int, int]
) -> bool:
    """Check d^psi(a)+d^psi(b)=d^psi(c) for the chosen abc relation."""
    abc_support_state(a, b, c)
    return (
        arithmetic_derivative(a, values)
        + arithmetic_derivative(b, values)
        == arithmetic_derivative(c, values)
    )


def arithmetic_wronskian(x: int, y: int, values: Mapping[int, int]) -> int:
    """Return W^psi(x,y)=x*d^psi(y)-y*d^psi(x)."""
    return x * arithmetic_derivative(y, values) - y * arithmetic_derivative(x, values)


def _pair_absolute_budget(x: int, y: int, values: Mapping[int, int]) -> int:
    """Triangle envelope obtained by forgetting signs in W^psi(x,y)."""
    psi = _require_int_mapping(values)
    terms: list[int] = []
    for prime, exponent in prime_factorization(y):
        terms.append(x * (y // prime) * exponent * psi.get(prime, 0))
    for prime, exponent in prime_factorization(x):
        terms.append(-y * (x // prime) * exponent * psi.get(prime, 0))
    return sum(abs(term) for term in terms)


def _pair_norm_base_weight(x: int, y: int) -> int:
    """Integer coefficient mass before multiplying by the global L-infinity norm."""
    weight = 0
    for prime, exponent in prime_factorization(y):
        weight += x * (y // prime) * exponent
    for prime, exponent in prime_factorization(x):
        weight += y * (x // prime) * exponent
    return weight


def pair_budget_profile(
    a: int,
    b: int,
    c: int,
    values: Mapping[int, int],
    pair: tuple[int, int],
) -> dict[str, int | tuple[int, int]]:
    """Return one orientation of the exact four-level witness-budget chain."""
    data = abc_support_state(a, b, c)
    psi = _require_int_mapping(values)
    if not is_relation_adapted(a, b, c, psi):
        raise ValueError("derivation is not adapted to the chosen relation a+b=c")

    x, y = pair
    if x not in (a, b, c) or y not in (a, b, c) or x == y:
        raise ValueError("pair must be an ordered pair of distinct abc entries")

    witness = arithmetic_wronskian(x, y, psi)
    if witness == 0:
        raise ValueError("arithmetic Wronskian is degenerate")
    witness_size = abs(witness)

    residual_demand = int(data["residual_product"])
    expected = a * b * c // int(data["radical_product"])
    if residual_demand != expected:
        raise AssertionError("radical/residual product disagrees with abc/rad(abc)")
    if witness_size % residual_demand != 0:
        raise AssertionError("relation-adapted Wronskian failed residual divisibility")

    absolute_budget = _pair_absolute_budget(x, y, psi)
    norm = derivation_norm_on_abc(a, b, c, psi)
    if norm == 0:
        raise ValueError("non-degenerate witness cannot have zero derivation norm")
    base_weight = _pair_norm_base_weight(x, y)
    norm_budget = norm * base_weight

    if not (residual_demand <= witness_size <= absolute_budget <= norm_budget):
        raise AssertionError("witness-budget chain is not monotone")

    absorption_gap = witness_size - residual_demand
    cancellation_gap = absolute_budget - witness_size
    norm_projection_gap = norm_budget - absolute_budget
    total_gap = norm_budget - residual_demand
    if total_gap != absorption_gap + cancellation_gap + norm_projection_gap:
        raise AssertionError("witness-budget shell gaps failed to telescope")

    return {
        "pair": pair,
        "residual_demand": residual_demand,
        "witness": witness,
        "witness_size": witness_size,
        "absorption_multiplier": witness_size // residual_demand,
        "absolute_budget": absolute_budget,
        "derivation_norm": norm,
        "norm_base_weight": base_weight,
        "norm_budget": norm_budget,
        "absorption_gap": absorption_gap,
        "cancellation_gap": cancellation_gap,
        "norm_projection_gap": norm_projection_gap,
        "total_gap": total_gap,
    }


def relation_budget_profile(
    a: int, b: int, c: int, values: Mapping[int, int]
) -> dict[str, object]:
    """Return all cyclic pair budgets for one adapted non-degenerate witness.

    Additivity makes the three cyclic Wronskians equal up to sign, so their
    absolute witness level is common while their coordinate/norm envelopes may
    differ.  The cheapest norm envelope is therefore a finite orientation
    observable of the same witness.
    """
    abc_support_state(a, b, c)
    psi = _require_int_mapping(values)
    profiles = tuple(
        pair_budget_profile(a, b, c, psi, pair)
        for pair in ((a, b), (b, c), (c, a))
    )
    witness_sizes = {int(profile["witness_size"]) for profile in profiles}
    if len(witness_sizes) != 1:
        raise AssertionError("adapted cyclic Wronskians must agree in absolute size")
    best = min(profiles, key=lambda profile: (int(profile["norm_budget"]), int(profile["absolute_budget"]), tuple(profile["pair"])))
    return {
        "triple": (a, b, c),
        "support": support_primes(a, b, c),
        "derivation_norm": derivation_norm_on_abc(a, b, c, psi),
        "profiles": profiles,
        "best_pair": best["pair"],
        "best_norm_budget": best["norm_budget"],
    }


def residual_derivative_divisibility(n: int, values: Mapping[int, int]) -> bool:
    """Check the elementary local absorber: m(n) divides d^psi(n)."""
    residual = multiplicity_residual(n)
    derivative = arithmetic_derivative(n, values)
    return derivative % residual == 0
