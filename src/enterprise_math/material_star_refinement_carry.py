"""Carry and witness bifurcation under true branching-star precision refinement.

This E001 generation consumes the denominator phase from
``material_star_response_precision_phase``.  Let ``s`` be a coarse denominator
and refine to ``s'=m*s`` with integer multiplier ``m>=1``.  If the coarse phase
is

    q*s = (k+1)*t + r,

then refining the unresolved residue has its own exact Euclidean carry

    m*r = (k+1)*c + r'.

Consequently the fine phase is

    q*m*s = (k+1)*(m*t+c) + r',

and the minimum impulse numerators satisfy the exact carry law

    A*_(m*s) = m*A*_s - c.

After normalization by the fine denominator, the physical minimum-cost drop is
therefore exactly

    A*_s/s - A*_(m*s)/(m*s) = c/(m*s).

So a true divisibility refinement changes the minimum cost only when scaled
coarse residue crosses a ``k+1`` boundary.  If ``r>0``, the first strict cost
drop multiplier is

    ceil((k+1)/r).

If ``r=0``, no later divisibility refinement can lower this star optimum: the
zero-residue gate is stable under multiplication.

The more important future-safety boundary occurs *before* a carry.  When
``c=0``, every coarse minimum response remains a fine minimum after multiplying
all its numerators by ``m``.  But for ``m>1`` and ``r>0`` the fine minimum
relation is strictly larger: its residual compositions sum to ``m*r`` and
include newly representable per-contact allocations that were absent from the
coarse lattice.  Thus minimum total impulse may be unchanged while the minimum
response witness language has already refined.

When ``c>0``, scaled coarse minima remain feasible but cease to be fine minima;
they over-deliver by exactly ``c`` fine numerator units.  The finer lattice has
crossed a genuine optimization boundary.

There is also a sharp symmetry-before-cost gate.  If ``0<r<k`` and ``r`` divides
``k``, multiplier

    m_sym = k/r

has ``c=0`` and fine residue ``r'=k``.  A permutation-fixed minimum response
therefore appears while the normalized minimum cost is still exactly unchanged.
For the reference ``k=3,q=1,s=1`` sequence:

* ``m=1``: cost ``1``, 3 minima, no symmetric minimum;
* ``m=2``: cost ``1``, 6 minima, still no symmetric minimum;
* ``m=3``: cost ``1``, 10 minima, a symmetric minimum appears;
* ``m=4``: one carry occurs, cost drops to ``3/4``, and the minimum becomes the
  unique zero-residue response.

This is an E001 specialization of ordinary Euclidean carry/divisibility facts.
The project-side point is the separation of coarse cost stability from witness
refinement: a quotient that observes only minimum total impulse can remain
constant while future contact-local actions already distinguish newly available
minimum witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_star_response_precision_phase import (
    star_general_final_score_numerators,
    star_minimum_response_relation_at_precision,
    star_minimum_total_numerator_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
    star_true_refinement_cost_drop_cross_numerator,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def star_refinement_residue_carry(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> tuple[int, int]:
    """Return ``(carry c, fine residue r')`` from ``m*r=(k+1)c+r'``."""
    _require_positive("refinement_multiplier", refinement_multiplier)
    coarse = star_response_refinement_phase(
        leaf_count, closing_quantum, coarse_denominator
    )
    return divmod(refinement_multiplier * coarse.residue, leaf_count + 1)


def star_first_strict_cost_drop_multiplier(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
) -> int | None:
    """Return the first multiplier that makes a divisibility refinement lower cost."""
    coarse = star_response_refinement_phase(
        leaf_count, closing_quantum, coarse_denominator
    )
    if coarse.residue == 0:
        return None
    return _ceil_div(leaf_count + 1, coarse.residue)


def star_symmetry_before_cost_drop_multiplier(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
) -> int | None:
    """Return the no-carry multiplier reaching residue ``k``, when it exists."""
    coarse = star_response_refinement_phase(
        leaf_count, closing_quantum, coarse_denominator
    )
    residue = coarse.residue
    if residue == 0 or leaf_count % residue != 0:
        return None
    multiplier = leaf_count // residue
    carry, fine_residue = star_refinement_residue_carry(
        leaf_count,
        closing_quantum,
        coarse_denominator,
        multiplier,
    )
    if carry != 0 or fine_residue != leaf_count:
        raise AssertionError("symmetry-before-cost multiplier lost exact residue gate")
    return multiplier


def star_scaled_coarse_minimum_relation(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> tuple[tuple[int, ...], ...]:
    """Scale every coarse minimum witness into the fine denominator lattice."""
    _require_positive("refinement_multiplier", refinement_multiplier)
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, coarse_denominator
    )
    return tuple(
        tuple(refinement_multiplier * value for value in vector)
        for vector in relation
    )


@dataclass(frozen=True)
class StarRefinementCarryReport:
    leaf_count: int
    closing_quantum: int
    coarse_denominator: int
    refinement_multiplier: int
    fine_denominator: int
    coarse_residue: int
    carry: int
    fine_residue: int
    coarse_minimum_total_numerator: int
    fine_minimum_total_numerator: int
    coarse_minimum_response_count: int
    fine_minimum_response_count: int
    scaled_coarse_minima_remain_fine_minima: bool
    new_minimum_witnesses_without_cost_drop: bool
    fine_symmetric_minimum_exists: bool
    cross_multiplied_cost_drop: int

    @property
    def strict_cost_drop(self) -> bool:
        return self.carry > 0


def star_refinement_carry_report(
    leaf_count: int,
    closing_quantum: int,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> StarRefinementCarryReport:
    """Return exact cost/witness changes under ``s -> m*s`` refinement."""
    _require_positive("refinement_multiplier", refinement_multiplier)
    fine_denominator = coarse_denominator * refinement_multiplier
    coarse = star_response_refinement_phase(
        leaf_count, closing_quantum, coarse_denominator
    )
    fine = star_response_refinement_phase(
        leaf_count, closing_quantum, fine_denominator
    )
    carry, fine_residue = star_refinement_residue_carry(
        leaf_count,
        closing_quantum,
        coarse_denominator,
        refinement_multiplier,
    )
    if fine.residue != fine_residue:
        raise AssertionError("fine phase residue disagrees with refinement carry")
    if fine.quotient_level != refinement_multiplier * coarse.quotient_level + carry:
        raise AssertionError("fine quotient level lost residue-carry identity")

    coarse_total = coarse.minimum_total_numerator
    fine_total = fine.minimum_total_numerator
    if fine_total != refinement_multiplier * coarse_total - carry:
        raise AssertionError("minimum impulse lost exact refinement carry law")

    cross_drop = star_true_refinement_cost_drop_cross_numerator(
        leaf_count,
        closing_quantum,
        coarse_denominator,
        fine_denominator,
    )
    if cross_drop != coarse_denominator * carry:
        raise AssertionError("cross-multiplied cost drop disagrees with residue carry")

    scaled_relation = star_scaled_coarse_minimum_relation(
        leaf_count,
        closing_quantum,
        coarse_denominator,
        refinement_multiplier,
    )
    for vector in scaled_relation:
        if any(
            score < 0
            for score in star_general_final_score_numerators(
                vector, closing_quantum, fine_denominator
            )
        ):
            raise AssertionError("scaled coarse minimum stopped being fine-feasible")

    fine_relation = set(
        star_minimum_response_relation_at_precision(
            leaf_count, closing_quantum, fine_denominator
        )
    )
    scaled_set = set(scaled_relation)
    remain_minimum = carry == 0
    if remain_minimum != scaled_set.issubset(fine_relation):
        raise AssertionError("scaled coarse minimum relation lost carry/minimum boundary")

    new_witnesses = (
        carry == 0
        and refinement_multiplier > 1
        and coarse.residue > 0
        and len(fine_relation) > len(scaled_set)
    )
    if carry == 0 and refinement_multiplier > 1 and coarse.residue > 0 and not new_witnesses:
        raise AssertionError("no-carry refinement failed to enrich minimum witness relation")

    return StarRefinementCarryReport(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        coarse_denominator=coarse_denominator,
        refinement_multiplier=refinement_multiplier,
        fine_denominator=fine_denominator,
        coarse_residue=coarse.residue,
        carry=carry,
        fine_residue=fine.residue,
        coarse_minimum_total_numerator=coarse_total,
        fine_minimum_total_numerator=fine_total,
        coarse_minimum_response_count=coarse.minimum_response_count,
        fine_minimum_response_count=fine.minimum_response_count,
        scaled_coarse_minima_remain_fine_minima=remain_minimum,
        new_minimum_witnesses_without_cost_drop=new_witnesses,
        fine_symmetric_minimum_exists=(
            star_symmetric_minimum_numerators(
                leaf_count, closing_quantum, fine_denominator
            )
            is not None
        ),
        cross_multiplied_cost_drop=cross_drop,
    )
