"""Bivariate mechanism polynomial for two-sided Barlow event repair.

The ordinary repair polynomial records only total repair dimension ``r=E+B``.
Here ``E`` is the zero-departure/orientation count and ``B`` the diagonal-split
side-label count.  Distinct mechanisms can have the same total r and therefore
the same microscopic fiber size ``2^r``.

The bivariate polynomial

    M_N(x,y) = sum_h x^E(h) y^B(h)

retains this semantic distinction while its diagonal specialization
``M_N(z,z)`` is exactly the ordinary repair polynomial.
"""

from __future__ import annotations

from collections import defaultdict

from .p022_barlow_excursion_repair import total_orientation_repair_bit_load
from .p022_barlow_repair_polynomial import (
    chamber_successors,
    repair_polynomial_coefficients,
)
from .p022_barlow_two_sided_repair import total_diagonal_split_bit_load

MechanismTerm = tuple[int, int, int]  # (orientation_bits, split_bits, history_count)
MechanismPolynomial = tuple[MechanismTerm, ...]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def transition_mechanism(
    previous: tuple[int, int], current: tuple[int, int]
) -> tuple[int, int]:
    """Return one-step ``(zero_departures, diagonal_split)`` event counts."""
    if current not in chamber_successors(previous):
        raise ValueError("current is not a legal chamber successor")
    orientation = int(previous[0] == 0) + int(previous[1] == 0)
    split = int(previous[0] == previous[1] and current[0] != current[1])
    return orientation, split


def mechanism_polynomial_terms(length: int) -> MechanismPolynomial:
    """Exact bivariate repair distribution by weighted chamber recursion."""
    _require_natural("length", length)
    # state -> {(E,B): quotient-history count}
    states: dict[tuple[int, int], dict[tuple[int, int], int]] = {
        (0, 0): {(0, 0): 1}
    }
    for _ in range(length):
        next_states: dict[
            tuple[int, int], dict[tuple[int, int], int]
        ] = defaultdict(dict)
        for state, terms in states.items():
            for successor in chamber_successors(state):
                add_e, add_b = transition_mechanism(state, successor)
                target = next_states[successor]
                for (orientation, split), count in terms.items():
                    key = orientation + add_e, split + add_b
                    target[key] = target.get(key, 0) + count
        states = dict(next_states)

    total: dict[tuple[int, int], int] = {}
    for terms in states.values():
        for key, count in terms.items():
            total[key] = total.get(key, 0) + count
    return tuple(
        (orientation, split, count)
        for (orientation, split), count in sorted(total.items())
    )


def evaluate_mechanism_polynomial(
    terms: MechanismPolynomial, orientation_weight: int, split_weight: int
) -> int:
    """Evaluate ``sum a_(E,B) x^E y^B`` at integer weights."""
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in (orientation_weight, split_weight)
    ):
        raise ValueError("weights must be integers")
    return sum(
        count
        * (orientation_weight**orientation)
        * (split_weight**split)
        for orientation, split, count in terms
    )


def diagonal_repair_coefficients(length: int) -> tuple[int, ...]:
    """Aggregate bivariate terms by ``r=E+B``."""
    terms = mechanism_polynomial_terms(length)
    totals: dict[int, int] = {}
    for orientation, split, count in terms:
        repair = orientation + split
        totals[repair] = totals.get(repair, 0) + count
    if not totals:
        return (1,)
    degree = max(totals)
    coefficients = tuple(totals.get(power, 0) for power in range(degree + 1))
    expected = repair_polynomial_coefficients(length)
    if coefficients != expected:
        raise AssertionError("bivariate diagonal must equal repair polynomial")
    return coefficients


def microscopic_orientation_load_from_mechanism(length: int) -> int:
    """Exact total orientation bits after microscopic fiber weighting.

    At ``x=y=2``, multiplying ``partial_x`` by x=2 yields

        sum E a_(E,B) 2^(E+B).
    """
    terms = mechanism_polynomial_terms(length)
    return sum(
        orientation * count * (2 ** (orientation + split))
        for orientation, split, count in terms
    )


def microscopic_split_load_from_mechanism(length: int) -> int:
    """Exact total diagonal side-label bits after microscopic weighting."""
    terms = mechanism_polynomial_terms(length)
    return sum(
        split * count * (2 ** (orientation + split))
        for orientation, split, count in terms
    )


def mechanism_load_identities(length: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Cross-check both partial derivatives against independent event counts."""
    _require_natural("length", length)
    orientation = microscopic_orientation_load_from_mechanism(length)
    # One-sided total is repeated against every word on the other side, for
    # each of two labelled sides.
    expected_orientation = (
        (2 ** (length + 1)) * total_orientation_repair_bit_load(length)
    )
    split = microscopic_split_load_from_mechanism(length)
    expected_split = total_diagonal_split_bit_load(length)
    if orientation != expected_orientation:
        raise AssertionError("orientation mechanism load mismatch")
    if split != expected_split:
        raise AssertionError("split mechanism load mismatch")
    return (orientation, expected_orientation), (split, expected_split)


def mechanism_aliases_at_total_repair(length: int) -> tuple[
    tuple[int, tuple[tuple[int, int, int], ...]], ...
]:
    """Repair dimensions realized by more than one ``(E,B)`` mechanism type."""
    grouped: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for orientation, split, count in mechanism_polynomial_terms(length):
        grouped[orientation + split].append((orientation, split, count))
    return tuple(
        (repair, tuple(values))
        for repair, values in sorted(grouped.items())
        if len(values) > 1
    )


def first_mechanism_alias() -> tuple[int, int, tuple[tuple[int, int, int], ...]]:
    """Smallest horizon/repair dimension where total r loses mechanism type."""
    length = 3
    aliases = dict(mechanism_aliases_at_total_repair(length))
    values = aliases.get(4)
    if values is None:
        raise AssertionError("length-three repair-four alias must exist")
    return length, 4, values
