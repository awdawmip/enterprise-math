"""Exact residue phase diagram for refined symmetric-star contact response.

This E001 generation continues the branching-star response relation from
``material_star_response_precision``.  It keeps the same equal-mass star but
allows an arbitrary positive integer closing quantum ``q`` and a declared
common impulse denominator ``s``.

There are ``k>=2`` identical leaves.  In denominator-scaled impulse numerators
``a_i>=0`` the contact constraints are

    -q*s + A + a_i >= 0,       A = sum_i a_i.

Write the scaled closing demand as

    q*s = (k+1)*t + r,         0 <= r <= k.

Then the exact minimum total numerator is

    A* = k*t + r = q*s - t,

and every minimum response is uniquely of the form

    a_i = t + x_i,
    x_i >= 0,
    sum_i x_i = r.

Most importantly, substituting this minimum response back into the contact
scores gives

    final_score_numerator_i = x_i.

Thus the Euclidean residue ``r=(q*s) mod (k+1)`` is not bookkeeping noise: at
minimum total response it is exactly the total unavoidable outward-score mass,
and the response witness ambiguity is exactly the set of weak compositions of
that residue among the contact channels.

The full leaf-permutation group has a fixed minimum response exactly in the two
residue phases

    r = 0    or    r = k,

equivalently

    (k+1) | q*s    or    (k+1) | (q*s + 1).

At ``r=0`` the minimum is unique and every contact is comoving.  At ``r=k`` a
symmetric minimum exists with one unit of scaled outward score on every
contact, although nonsymmetric minimizers also exist.  For ``1<=r<=k-1`` no
deterministic leaf-permutation-equivariant selector can choose a minimum
response without extra symmetry-breaking state.

The least symmetric feasible response has equal numerator
``ceil(q*s/(k+1))`` on every contact.  Relative to the unrestricted minimum its
extra total numerator is exactly ``k-r`` when ``r>0`` and zero when ``r=0``.

The residue phase is periodic in the denominator with exact period

    (k+1) / gcd(q,k+1).

Finally, denominator magnitude is not the refinement order.  A true lattice
refinement is divisibility ``s | s'``: every coarse response remains
representable after multiplying its numerators by ``s'/s``, so the exact
minimum physical impulse cannot increase along that partial order.  Merely
replacing ``s`` by a larger non-multiple can increase the optimum (for example
``k=3,q=1`` from ``s=4`` to ``s=5``).  This is an E001 specialization of the
project's existing scale-lattice viewpoint, not a new generic divisibility
lattice theorem.

No continuum force, fractional canonical momentum state, restitution law, or
physical uniqueness is introduced here.  Rationally refined impulse vectors
remain a representation-layer pressure test until a compatible world state is
declared.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, gcd


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_leaf_count(leaf_count: int) -> None:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")


def _weak_compositions(total: int, length: int) -> tuple[tuple[int, ...], ...]:
    if length == 1:
        return ((total,),)
    result: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for tail in _weak_compositions(total - first, length - 1):
            result.append((first,) + tail)
    return tuple(result)


def star_scaled_closing_phase(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, int]:
    """Return ``(t,r)`` from ``q*s=(k+1)t+r``."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    return divmod(closing_quantum * denominator, leaf_count + 1)


def star_refinement_phase_period(leaf_count: int, closing_quantum: int) -> int:
    """Return the exact denominator period of the residue phase."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    return (leaf_count + 1) // gcd(closing_quantum, leaf_count + 1)


def star_minimum_total_numerator_at_precision(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> int:
    """Return the least total impulse numerator on the denominator-``s`` lattice."""
    t, _ = star_scaled_closing_phase(leaf_count, closing_quantum, denominator)
    return closing_quantum * denominator - t


def star_general_final_score_numerators(
    impulse_numerators: tuple[int, ...] | list[int],
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...]:
    """Return denominator-scaled final contact scores for closing quantum ``q``."""
    values = tuple(impulse_numerators)
    _require_leaf_count(len(values))
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("impulse numerators must be non-negative integers")
    total = sum(values)
    scaled_closing = closing_quantum * denominator
    return tuple(-scaled_closing + total + value for value in values)


def star_minimum_response_relation_at_precision(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Return every minimum-total numerator vector at one precision denominator."""
    t, residue = star_scaled_closing_phase(leaf_count, closing_quantum, denominator)
    relation = tuple(
        tuple(t + value for value in composition)
        for composition in _weak_compositions(residue, leaf_count)
    )
    expected_total = star_minimum_total_numerator_at_precision(
        leaf_count, closing_quantum, denominator
    )
    if any(sum(vector) != expected_total for vector in relation):
        raise AssertionError("star minimum relation lost exact total numerator")
    for vector in relation:
        residual = tuple(value - t for value in vector)
        if star_general_final_score_numerators(
            vector, closing_quantum, denominator
        ) != residual:
            raise AssertionError("star residue no longer equals final score witness")
    return relation


def star_symmetric_minimum_numerators(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...] | None:
    """Return the permutation-fixed minimum response when one exists."""
    t, residue = star_scaled_closing_phase(leaf_count, closing_quantum, denominator)
    if residue == 0:
        return (t,) * leaf_count
    if residue == leaf_count:
        return (t + 1,) * leaf_count
    return None


def star_least_symmetric_feasible_numerators(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...]:
    """Return the least feasible vector fixed by every leaf permutation."""
    t, residue = star_scaled_closing_phase(leaf_count, closing_quantum, denominator)
    coordinate = t if residue == 0 else t + 1
    result = (coordinate,) * leaf_count
    if any(
        score < 0
        for score in star_general_final_score_numerators(
            result, closing_quantum, denominator
        )
    ):
        raise AssertionError("least symmetric response is not feasible")
    return result


def star_first_symmetric_minimum_denominator(
    leaf_count: int,
    closing_quantum: int,
) -> int:
    """Return the first denominator whose minimum relation has a symmetric fixed point."""
    period = star_refinement_phase_period(leaf_count, closing_quantum)
    for denominator in range(1, period + 1):
        _, residue = star_scaled_closing_phase(
            leaf_count, closing_quantum, denominator
        )
        if residue in (0, leaf_count):
            return denominator
    raise AssertionError("zero-residue phase must occur by the exact period")


def star_true_refinement_cost_drop_cross_numerator(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
    fine_denominator: int,
) -> int:
    """Return the non-negative cross-multiplied cost drop for ``s | s'``.

    Physical minimum totals are ``A_s/s`` and ``A_s'/s'``.  The returned
    integer is ``A_s*s' - A_s'*s``.
    """
    _require_positive("coarse_denominator", coarse_denominator)
    _require_positive("fine_denominator", fine_denominator)
    if fine_denominator % coarse_denominator != 0:
        raise ValueError("fine_denominator must be a divisibility refinement")
    coarse_total = star_minimum_total_numerator_at_precision(
        leaf_count, closing_quantum, coarse_denominator
    )
    fine_total = star_minimum_total_numerator_at_precision(
        leaf_count, closing_quantum, fine_denominator
    )
    drop = coarse_total * fine_denominator - fine_total * coarse_denominator
    if drop < 0:
        raise AssertionError("true denominator refinement increased minimum impulse")
    return drop


@dataclass(frozen=True)
class StarResponseRefinementPhase:
    leaf_count: int
    closing_quantum: int
    denominator: int
    scaled_closing: int
    quotient_level: int
    residue: int
    minimum_total_numerator: int
    minimum_response_count: int
    symmetric_minimum_numerators: tuple[int, ...] | None
    least_symmetric_feasible_numerators: tuple[int, ...]
    symmetric_overresponse_numerator: int
    residue_period: int

    @property
    def zero_excess_gate(self) -> bool:
        return self.residue == 0

    @property
    def one_excess_gate(self) -> bool:
        return self.residue == self.leaf_count

    @property
    def symmetry_minimum_compatible(self) -> bool:
        return self.symmetric_minimum_numerators is not None


def star_response_refinement_phase(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> StarResponseRefinementPhase:
    """Return the exact residue/symmetry/minimum-response phase."""
    t, residue = star_scaled_closing_phase(
        leaf_count, closing_quantum, denominator
    )
    minimum_total = star_minimum_total_numerator_at_precision(
        leaf_count, closing_quantum, denominator
    )
    symmetric_minimum = star_symmetric_minimum_numerators(
        leaf_count, closing_quantum, denominator
    )
    least_symmetric = star_least_symmetric_feasible_numerators(
        leaf_count, closing_quantum, denominator
    )
    overresponse = sum(least_symmetric) - minimum_total
    expected_overresponse = 0 if residue == 0 else leaf_count - residue
    if overresponse != expected_overresponse:
        raise AssertionError("symmetric overresponse lost residue formula")

    response_count = comb(residue + leaf_count - 1, leaf_count - 1)
    return StarResponseRefinementPhase(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        scaled_closing=closing_quantum * denominator,
        quotient_level=t,
        residue=residue,
        minimum_total_numerator=minimum_total,
        minimum_response_count=response_count,
        symmetric_minimum_numerators=symmetric_minimum,
        least_symmetric_feasible_numerators=least_symmetric,
        symmetric_overresponse_numerator=overresponse,
        residue_period=star_refinement_phase_period(leaf_count, closing_quantum),
    )
