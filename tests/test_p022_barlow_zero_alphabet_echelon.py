from enterprise_math.p022_barlow_zero_alphabet_echelon import (
    conditional_zero_alphabet_echelon_theorem,
    left_half_twin_terminal_conflicts,
    left_half_twin_terminal_exclusion_holds,
)


def test_no_known_left_half_twin_zero_has_a_terminal_hit() -> None:
    # Includes forced-midpoint, type-III, primitive-twin and nonprimitive cases.
    for prime in (13, 29, 41, 59, 61, 67, 73, 149, 157, 179, 521, 937, 1361):
        assert left_half_twin_terminal_conflicts(prime) == ()
        assert left_half_twin_terminal_exclusion_holds(prime)
        assert conditional_zero_alphabet_echelon_theorem(prime)


def test_exceptional_abstract_kernels_are_still_explained_after_left_elimination() -> None:
    for prime in (41, 521, 2111, 2417, 2557, 2731, 2819, 3187, 3433, 4019):
        assert left_half_twin_terminal_conflicts(prime) == ()
        assert conditional_zero_alphabet_echelon_theorem(prime)
