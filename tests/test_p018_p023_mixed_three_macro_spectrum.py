from enterprise_math.p018_p023_mixed_three_macro_spectrum import (
    formula_matches_direct,
    prime_eight_nine_ten_first_fail,
    prime_eight_nine_ten_hard_shell,
    two_five_mixed_cost,
)
from enterprise_math.p018_p023_pure_power_macro_spectrum import (
    pure_power_macro_shell,
)


def test_two_five_coupled_cost_basic_cases() -> None:
    assert two_five_mixed_cost(2, 0) == 2
    assert two_five_mixed_cost(3, 0) == 1
    assert two_five_mixed_cost(1, 1) == 1
    assert two_five_mixed_cost(4, 1) == 2
    assert two_five_mixed_cost(8, 1) == 4


def test_pointwise_formula_matches_independent_recursion() -> None:
    assert formula_matches_direct(2_000)


def test_prime_eight_nine_ten_shell_internal_phase_change() -> None:
    expected = {
        1: 2,
        2: 4,
        3: 12,
        4: 84,
        5: 588,
        6: 4_116,
        7: 28_812,
        8: 201_684,
        9: 1_171_875,
        10: 5_859_375,
    }
    for cost, shell in expected.items():
        assert prime_eight_nine_ten_hard_shell(cost) == shell


def test_mixed_code_first_fail_horizons_five_through_eight() -> None:
    assert prime_eight_nine_ten_first_fail(5) == 4_116
    assert prime_eight_nine_ten_first_fail(6) == 28_812
    assert prime_eight_nine_ten_first_fail(7) == 201_684
    assert prime_eight_nine_ten_first_fail(8) == 1_171_875


def test_budget_three_candidate_crossovers() -> None:
    # Pure transient {4,8,9} wins before the mixed code.
    for h in (3, 4):
        assert pure_power_macro_shell((4, 8, 9), h + 1) > prime_eight_nine_ten_first_fail(h)

    # The mixed code wins through the final transient horizon h=8.
    for h in (5, 6, 7, 8):
        assert prime_eight_nine_ten_first_fail(h) > pure_power_macro_shell((4, 8, 9), h + 1)
        assert prime_eight_nine_ten_first_fail(h) > pure_power_macro_shell((8, 9, 25), h + 1)

    # At h=9 the stable q=7 pure-power code finally overtakes the mixed code.
    assert pure_power_macro_shell((8, 9, 25), 10) > prime_eight_nine_ten_first_fail(9)
