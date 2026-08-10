from fractions import Fraction

from enterprise_math.abc_quadratic_rank_energy import (
    rank_energy_state,
    stage107_arithmetic_observable_collision,
)


def test_area_collision_is_split_by_quadratic_energy() -> None:
    data = stage107_arithmetic_observable_collision()
    flat = data["flat"]
    jump = data["jump"]
    assert flat.ranks == (1, 1)
    assert jump.ranks == (0, 2)
    assert flat.activation_area == jump.activation_area == 2
    assert flat.quadratic_rank_energy == 2
    assert jump.quadratic_rank_energy == 4


def test_energy_uses_same_incidence_state_but_stronger_observable() -> None:
    state = rank_energy_state(
        (Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)),
        (Fraction(3, 4), Fraction(3, 2), Fraction(3, 1)),
    )
    assert state.ranks == (1, 2, 3)
    assert state.activation_area == 6
    assert state.quadratic_rank_energy == 14
