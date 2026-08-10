import pytest

from enterprise_math.p022_barlow_franel_companion_last_hit import (
    companion_branch_zero_is_unique,
    rank_from_universal_companion,
    twin_terminal_offset_mod3_obstruction,
    universal_companion_casoratian,
)


def test_H_K_casoratian_is_exact() -> None:
    expected = (
        -2,
        16,
        -10368,
        51840000,
        -995742720000,
    )
    assert tuple(universal_companion_casoratian(d) for d in range(5)) == expected


def test_selected_branch_is_unique_at_real_zero_offsets() -> None:
    # q=29 uses H and has left offsets 2 and 0(midpoint); q=41 uses K and
    # has left offsets 10 and 13.  The opposite companion is a q-unit.
    assert companion_branch_zero_is_unique(29, 2)
    assert companion_branch_zero_is_unique(41, 10)
    assert companion_branch_zero_is_unique(41, 13)


def test_last_companion_hit_recovers_rank_of_apparition() -> None:
    assert rank_from_universal_companion(29) == 12
    assert rank_from_universal_companion(41) == 7
    assert rank_from_universal_companion(59) == 17
    assert rank_from_universal_companion(73) == 6
    assert rank_from_universal_companion(157) == 16


def test_twin_terminal_offsets_divisible_by_three_are_prime_impossible() -> None:
    assert twin_terminal_offset_mod3_obstruction(6, 41) == 1
    assert twin_terminal_offset_mod3_obstruction(9, 61) == 2

    # d=3 would give q=4r+3, which is divisible by three for twin-center r.
    with pytest.raises(ValueError):
        twin_terminal_offset_mod3_obstruction(3, 21)
