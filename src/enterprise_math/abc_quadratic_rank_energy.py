"""Quadratic threshold-rank energy for P025 precision pressure tests.

For ordered thresholds T and monotone node values v_j, let

    r_j = # {T_k : v_j >= T_k}.

Stage 107 studies the nonlinear observable

    E = sum_j r_j^2.

It deliberately uses the same incidence geometry as activation area while
changing only the future observable.  This separates observable refinement from
operation-word refinement.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .abc_signed_exponent_transport import dyadic_difference_pressure_tower
from .abc_two_step_history import activation_area, node_rank


@dataclass(frozen=True)
class RankEnergyState:
    thresholds: tuple[Fraction, ...]
    values: tuple[Fraction, ...]
    ranks: tuple[int, ...]
    activation_area: int
    quadratic_rank_energy: int


def _validate(thresholds: Sequence[Fraction], values: Sequence[Fraction]) -> None:
    if not values:
        raise ValueError("values must be non-empty")
    if any(not isinstance(value, Fraction) for value in (*thresholds, *values)):
        raise ValueError("thresholds and values must be Fractions")
    if any(value <= 0 for value in thresholds):
        raise ValueError("thresholds must be positive")
    if any(thresholds[i] >= thresholds[i + 1] for i in range(len(thresholds) - 1)):
        raise ValueError("thresholds must be strictly increasing")
    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("values must be nondecreasing")


def rank_energy_state(
    thresholds: Sequence[Fraction], values: Sequence[Fraction]
) -> RankEnergyState:
    """Return rank vector, area, and quadratic rank energy."""
    _validate(thresholds, values)
    thresholds_tuple = tuple(thresholds)
    values_tuple = tuple(values)
    ranks = tuple(node_rank(thresholds_tuple, value) for value in values_tuple)
    area = activation_area(thresholds_tuple, values_tuple)
    if area != sum(ranks):
        raise AssertionError("activation area is not the sum of column ranks")
    return RankEnergyState(
        thresholds=thresholds_tuple,
        values=values_tuple,
        ranks=ranks,
        activation_area=area,
        quadratic_rank_energy=sum(rank * rank for rank in ranks),
    )


def stage107_arithmetic_observable_collision() -> dict[str, RankEnergyState]:
    """Exact P025 states merged by area but separated by quadratic energy.

    Thresholds are (1/2,1).  The dyadic orbits `(3,5,2)` and `(7,17,2)`
    through one doubling have rank vectors (1,1) and (0,2), respectively.
    Both have area two, but energies two and four.
    """
    thresholds = (Fraction(1, 2), Fraction(1, 1))
    flat_pressures = dyadic_difference_pressure_tower(3, 5, 2, 1).pressures
    jump_pressures = dyadic_difference_pressure_tower(7, 17, 2, 1).pressures
    flat = rank_energy_state(thresholds, flat_pressures)
    jump = rank_energy_state(thresholds, jump_pressures)
    if flat.activation_area != jump.activation_area:
        raise AssertionError("fixtures should collide on activation area")
    if flat.ranks == jump.ranks:
        raise AssertionError("fixtures should have distinct rank geometry")
    if flat.quadratic_rank_energy == jump.quadratic_rank_energy:
        raise AssertionError("fixtures should be separated by quadratic energy")
    return {"flat": flat, "jump": jump}
