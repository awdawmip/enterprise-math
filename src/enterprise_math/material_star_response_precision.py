"""Symmetry/precision obstruction for a branching E001 contact star.

This module isolates the sharp degree-three-and-higher boundary exposed by the
Z-contact least-action probe.  It is a finite response-language specialization,
not a new theorem about permutation groups or convex optimization.

Consider one center body and ``k>=2`` identical leaf bodies, all masses one,
center momentum one, leaf momenta zero, with every declared contact normal
pointing from center to leaf.  Then

    r = (-1,...,-1),
    K_ii = 2,
    K_ij = 1  (i!=j).

For a non-negative integer impulse vector ``j`` with total ``S=sum(j)``, the
final contact scores are

    r'_i = -1 + S + j_i.

Therefore the minimum total integer impulse is exactly one, and the full set of
minimum-total responses is the permutation orbit of the unit vectors.  There is
no distinguished member without adding a symmetry-breaking policy.

A deterministic response that is equivariant under every permutation of the
identical leaves must be fixed by that permutation group, hence all impulse
coordinates must be equal.  The zero vector is infeasible, so the smallest
symmetric integer response is ``(1,...,1)`` with total impulse ``k``.  Thus on
the coarse integer impulse lattice the following three requirements cannot all
hold:

1. deterministic single-valued response;
2. exact leaf-permutation symmetry;
3. minimum total delivered impulse.

A set-valued response relation containing all ``k`` unit minimizers preserves
both minimum total and symmetry.

The obstruction is precision-dependent.  On a refined impulse lattice with
common denominator ``s``, write the physical impulse as integer numerator
``a_i/s``.  Multiplying the contact inequality by ``s`` gives

    -s + sum(a) + a_i >= 0.

A symmetric minimum-total response has all ``a_i=c`` and total
``k*c/s = 1``.  Hence ``s=k*c``; the smallest possible denominator is exactly
``k``.  At denominator ``k`` the symmetric vector ``(1/k,...,1/k)`` is feasible
and has total one.  This is only a lattice-representation statement: a world
that actually delivers such fractional contact impulses must also declare a
compatible finer momentum state.  This module does not silently insert that
finer state into the canonical integer-momentum world.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
)


def _require_leaf_count(leaf_count: int) -> None:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")


def symmetric_star_state(leaf_count: int) -> ContactNetworkMomentum1D:
    """Return the canonical equal-mass symmetric closing star."""
    _require_leaf_count(leaf_count)
    return ContactNetworkMomentum1D(
        masses=(1,) * (leaf_count + 1),
        momenta=(1,) + (0,) * leaf_count,
        contacts=tuple(
            ContactChannel1D(0, leaf, 1)
            for leaf in range(1, leaf_count + 1)
        ),
    )


def star_final_score_numerators(
    impulse_numerators: tuple[int, ...] | list[int],
    denominator: int = 1,
) -> tuple[int, ...]:
    """Return denominator-scaled final scores for the symmetric star."""
    values = tuple(impulse_numerators)
    _require_leaf_count(len(values))
    if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("denominator must be a positive integer")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("impulse numerators must be non-negative integers")
    total = sum(values)
    return tuple(-denominator + total + value for value in values)


def star_impulse_numerators_are_feasible(
    impulse_numerators: tuple[int, ...] | list[int],
    denominator: int = 1,
) -> bool:
    return all(
        score >= 0
        for score in star_final_score_numerators(impulse_numerators, denominator)
    )


def star_minimum_total_integer_response_relation(
    leaf_count: int,
) -> tuple[tuple[int, ...], ...]:
    """Return every minimum-total response on the coarse integer impulse lattice."""
    _require_leaf_count(leaf_count)
    return tuple(
        tuple(1 if index == selected else 0 for index in range(leaf_count))
        for selected in range(leaf_count)
    )


def star_minimum_symmetric_integer_response(leaf_count: int) -> tuple[int, ...]:
    """Return the least feasible response fixed by all leaf permutations."""
    _require_leaf_count(leaf_count)
    return (1,) * leaf_count


def star_minimum_symmetric_refinement_denominator(leaf_count: int) -> int:
    """Return the least denominator allowing symmetric total-one impulse."""
    _require_leaf_count(leaf_count)
    return leaf_count


def star_refined_symmetric_minimum_response(
    leaf_count: int,
) -> tuple[int, tuple[int, ...]]:
    """Return ``(denominator, numerators)`` for the first symmetric total-one response."""
    denominator = star_minimum_symmetric_refinement_denominator(leaf_count)
    numerators = (1,) * leaf_count
    if sum(numerators) != denominator:
        raise AssertionError("refined symmetric response lost total-one normalization")
    if not star_impulse_numerators_are_feasible(numerators, denominator):
        raise AssertionError("refined symmetric response is not feasible")
    return denominator, numerators


@dataclass(frozen=True)
class StarResponsePrecisionReport:
    leaf_count: int
    initial_scores: tuple[int, ...]
    coupling_gram: tuple[tuple[int, ...], ...]
    minimum_total_impulse: int
    minimum_relation: tuple[tuple[int, ...], ...]
    minimum_symmetric_integer_response: tuple[int, ...]
    symmetric_integer_total: int
    first_symmetric_minimum_denominator: int
    refined_symmetric_numerators: tuple[int, ...]

    @property
    def coarse_symmetry_overresponse_factor(self) -> int:
        return self.symmetric_integer_total // self.minimum_total_impulse


def star_response_precision_report(leaf_count: int) -> StarResponsePrecisionReport:
    """Return the exact integer-vs-refined symmetry tradeoff for one star."""
    state = symmetric_star_state(leaf_count)
    scores = contact_relative_scores(state)
    gram = contact_coupling_gram(state)
    expected_gram = tuple(
        tuple(2 if row == col else 1 for col in range(leaf_count))
        for row in range(leaf_count)
    )
    if scores != (-1,) * leaf_count or gram != expected_gram:
        raise AssertionError("canonical symmetric star lost its exact r/K form")

    relation = star_minimum_total_integer_response_relation(leaf_count)
    if not all(star_impulse_numerators_are_feasible(vector) for vector in relation):
        raise AssertionError("minimum response relation contains infeasible vector")
    if any(sum(vector) != 1 for vector in relation):
        raise AssertionError("minimum response relation lost total-one property")

    symmetric = star_minimum_symmetric_integer_response(leaf_count)
    denominator, numerators = star_refined_symmetric_minimum_response(leaf_count)
    return StarResponsePrecisionReport(
        leaf_count=leaf_count,
        initial_scores=scores,
        coupling_gram=gram,
        minimum_total_impulse=1,
        minimum_relation=relation,
        minimum_symmetric_integer_response=symmetric,
        symmetric_integer_total=sum(symmetric),
        first_symmetric_minimum_denominator=denominator,
        refined_symmetric_numerators=numerators,
    )
