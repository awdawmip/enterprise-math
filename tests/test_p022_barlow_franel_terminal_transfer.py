from fractions import Fraction

from enterprise_math.p022_barlow_franel_terminal_transfer import (
    primitive_terminal_transfer_residue,
    primitive_terminal_zero_iff_transfer_zero,
    terminal_transfer,
    terminal_transfer_fixed_gcd,
    terminal_transfer_matches_gap_continuant,
)


def test_first_direct_terminal_transfers() -> None:
    assert tuple(terminal_transfer(r) for r in range(3, 9)) == (
        Fraction(9, 2),
        Fraction(6784, 225),
        Fraction(424475, 1764),
        Fraction(2989066, 1575),
        Fraction(147689675, 9801),
        Fraction(243269610643456, 2029052025),
    )


def test_direct_transfer_is_same_fixed_obstruction_as_gap_continuant() -> None:
    for rank in range(3, 16):
        assert terminal_transfer_matches_gap_continuant(rank)


def test_primitive_terminal_transfer_on_twin_examples() -> None:
    # All these primitive twin rows have nonzero first-reentry terminal value.
    for rank, prime in ((6, 13), (6, 73), (9, 937), (15, 179), (21, 3019), (30, 1361)):
        actual, predicted = primitive_terminal_transfer_residue(rank, prime)
        assert actual == predicted
        assert actual != 0
        assert not primitive_terminal_zero_iff_transfer_zero(rank, prime)


def test_fixed_transfer_common_part_is_small_on_initial_triple_ranks() -> None:
    expected = {
        3: 1,
        6: 2,
        9: 4,
        12: 80,
        15: 1,
        18: 4,
        21: 1,
        24: 16,
        27: 1,
        30: 4,
    }
    assert {rank: terminal_transfer_fixed_gcd(rank) for rank in expected} == expected
