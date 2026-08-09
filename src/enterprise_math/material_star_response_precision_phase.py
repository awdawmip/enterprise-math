"""Exact denominator-residue phase for the E001 branching-star response.

This generation is a precision-lattice extension of
``material_star_response_spectrum``.  It does not re-own the arbitrary-closing
integer star theorem.  Instead, for a positive closing quantum ``q`` and a
declared common impulse denominator ``s``, it consumes that theorem at the
scaled closing demand

    Q = q*s.

For ``k>=2`` identical leaves, the scaled integer constraints are

    -Q + A + a_i >= 0,       A = sum_i a_i.

The upstream star-spectrum theorem applied to ``Q`` gives the minimum relation.
Writing

    Q = (k+1)*t + r,         0 <= r <= k,

its exact parameters become

    A* = k*t + r,
    a_i = t + x_i,
    x_i >= 0,
    sum_i x_i = r.

The extra observation of this generation is what these scaled parameters mean
across precision denominators.  Substitution gives

    final_score_numerator_i = x_i.

Thus ``r=(q*s) mod (k+1)`` is exactly the total unavoidable outward-score mass
at minimum delivered impulse, while the minimum-response witness ambiguity is
the upstream weak-composition relation for distributing that residue.

A minimum response fixed by every leaf permutation exists exactly in the two
residue phases

    r = 0    or    r = k,

or equivalently

    (k+1) | q*s    or    (k+1) | (q*s+1).

At ``r=0`` the minimum is unique and all contact scores vanish.  At ``r=k`` a
symmetric minimum exists with one scaled outward-score unit on each contact,
though nonsymmetric minimizers also remain.  For ``1<=r<=k-1`` the minimum
relation has no permutation-fixed member.

The residue phase has exact denominator period

    (k+1) / gcd(q,k+1).

Finally, denominator magnitude is not the precision order.  True rational
lattice refinement is divisibility ``s | s'``.  Any coarse numerator vector
remains representable after multiplying by ``s'/s``, so the minimum physical
impulse cannot increase along this partial order.  A numerically larger
non-multiple denominator may increase the optimum; for ``k=3,q=1``, the minimum
moves from ``3/4`` at ``s=4`` to ``4/5`` at ``s=5``.  This is an E001 backflow
example for the existing Enterprise Math scale-lattice viewpoint, not a new
generic divisibility theorem.

No fractional canonical momentum state, continuum force, restitution law or
physical uniqueness is introduced.  Refined impulse numerators remain a
representation-layer pressure test until the world state is refined compatibly.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_star_response_spectrum import (
    star_minimum_relation_cardinality,
    star_minimum_relation_parameters,
    star_minimum_symmetric_integer_total,
    star_minimum_total_has_symmetric_integer_selector,
    star_minimum_total_impulse,
    star_minimum_total_integer_relation,
    star_score_vector,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_leaf_count(leaf_count: int) -> None:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")


def _scaled_closing(closing_quantum: int, denominator: int) -> int:
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    return closing_quantum * denominator


def star_scaled_closing_phase(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, int]:
    """Return ``(t,r)`` from ``q*s=(k+1)t+r`` via the upstream spectrum."""
    _require_leaf_count(leaf_count)
    scaled = _scaled_closing(closing_quantum, denominator)
    _, baseline, excess = star_minimum_relation_parameters(leaf_count, scaled)
    quotient, residue = divmod(scaled, leaf_count + 1)
    if (baseline, excess) != (quotient, residue):
        raise AssertionError("scaled star spectrum disagrees with Euclidean phase")
    return quotient, residue


def star_refinement_phase_period(leaf_count: int, closing_quantum: int) -> int:
    """Return the exact denominator period of ``q*s mod (k+1)``."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    return (leaf_count + 1) // gcd(closing_quantum, leaf_count + 1)


def star_minimum_total_numerator_at_precision(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> int:
    """Return the least total impulse numerator on the denominator-``s`` lattice."""
    _require_leaf_count(leaf_count)
    scaled = _scaled_closing(closing_quantum, denominator)
    return star_minimum_total_impulse(leaf_count, scaled)


def star_general_final_score_numerators(
    impulse_numerators: tuple[int, ...] | list[int],
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...]:
    """Return denominator-scaled final contact scores for closing quantum ``q``."""
    scaled = _scaled_closing(closing_quantum, denominator)
    return star_score_vector(tuple(impulse_numerators), scaled)


def star_minimum_response_relation_at_precision(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Return every minimum-total numerator vector at one precision denominator."""
    _require_leaf_count(leaf_count)
    scaled = _scaled_closing(closing_quantum, denominator)
    relation = star_minimum_total_integer_relation(leaf_count, scaled)
    quotient, residue = star_scaled_closing_phase(
        leaf_count, closing_quantum, denominator
    )
    if len(relation) != star_minimum_relation_cardinality(leaf_count, scaled):
        raise AssertionError("scaled minimum relation lost upstream cardinality")
    for vector in relation:
        residual_distribution = tuple(value - quotient for value in vector)
        if any(value < 0 for value in residual_distribution):
            raise AssertionError("scaled minimum response fell below baseline")
        if sum(residual_distribution) != residue:
            raise AssertionError("scaled minimum response lost residue mass")
        if star_general_final_score_numerators(
            vector, closing_quantum, denominator
        ) != residual_distribution:
            raise AssertionError("star residue no longer equals final score witness")
    return relation


def star_symmetric_minimum_numerators(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...] | None:
    """Return the permutation-fixed minimum response when one exists."""
    _require_leaf_count(leaf_count)
    scaled = _scaled_closing(closing_quantum, denominator)
    if not star_minimum_total_has_symmetric_integer_selector(leaf_count, scaled):
        return None
    total = star_minimum_total_impulse(leaf_count, scaled)
    if total % leaf_count != 0:
        raise AssertionError("upstream symmetric-selector criterion lost divisibility")
    return (total // leaf_count,) * leaf_count


def star_least_symmetric_feasible_numerators(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[int, ...]:
    """Return the least feasible vector fixed by every leaf permutation."""
    _require_leaf_count(leaf_count)
    scaled = _scaled_closing(closing_quantum, denominator)
    symmetric_total = star_minimum_symmetric_integer_total(leaf_count, scaled)
    if symmetric_total % leaf_count != 0:
        raise AssertionError("upstream symmetric integer total lost equal coordinates")
    result = (symmetric_total // leaf_count,) * leaf_count
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
        if star_symmetric_minimum_numerators(
            leaf_count, closing_quantum, denominator
        ) is not None:
            return denominator
    raise AssertionError("zero-residue phase must occur by the exact period")


def star_true_refinement_cost_drop_cross_numerator(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
    fine_denominator: int,
) -> int:
    """Return ``A_s*s' - A_s'*s`` for a true divisibility refinement ``s|s'``."""
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
    """Return the exact residue/symmetry/minimum-response precision phase."""
    quotient, residue = star_scaled_closing_phase(
        leaf_count, closing_quantum, denominator
    )
    scaled = closing_quantum * denominator
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

    modular_gate = scaled % (leaf_count + 1) == 0 or (scaled + 1) % (leaf_count + 1) == 0
    if (symmetric_minimum is not None) != modular_gate:
        raise AssertionError("upstream symmetric selector lost modular phase criterion")

    return StarResponseRefinementPhase(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        scaled_closing=scaled,
        quotient_level=quotient,
        residue=residue,
        minimum_total_numerator=minimum_total,
        minimum_response_count=star_minimum_relation_cardinality(leaf_count, scaled),
        symmetric_minimum_numerators=symmetric_minimum,
        least_symmetric_feasible_numerators=least_symmetric,
        symmetric_overresponse_numerator=overresponse,
        residue_period=star_refinement_phase_period(leaf_count, closing_quantum),
    )
