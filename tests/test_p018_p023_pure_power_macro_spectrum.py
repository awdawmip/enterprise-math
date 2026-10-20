from enterprise_math.p018_p023_pure_power_macro_spectrum import (
    predicted_budget_three_threshold,
    pure_power_budget_optimizer,
    pure_power_macro_shell,
    pure_power_macro_spectrum,
    spectrum_matches_direct,
)


def test_known_marginal_spectra() -> None:
    assert pure_power_macro_spectrum((4, 9), 6) == (2, 3, 4, 4, 4, 4)
    assert pure_power_macro_spectrum((8, 9), 7) == (2, 2, 3, 5, 5, 5, 5)
    assert pure_power_macro_spectrum((4, 8, 9), 7) == (2, 3, 5, 5, 5, 5, 5)
    assert pure_power_macro_spectrum((8, 9, 25), 8) == (2, 2, 3, 5, 7, 7, 7, 7)


def test_spectral_shell_matches_independent_shortest_word() -> None:
    for macros in ((4, 9), (8, 9), (4, 8, 9), (8, 9, 25)):
        for cost in range(1, 8):
            assert spectrum_matches_direct(macros, cost)


def test_budget_three_transient_stable_crossing() -> None:
    expected = {
        3: (150, (4, 8, 9)),
        4: (750, (4, 8, 9)),
        5: (3750, (4, 8, 9)),
        6: (20580, (8, 9, 25)),
        7: (144060, (8, 9, 25)),
    }
    for horizon, want in expected.items():
        assert predicted_budget_three_threshold(horizon) == want


def test_budget_three_candidates_dominate_each_other_at_expected_crossing() -> None:
    for h in range(3, 6):
        assert pure_power_macro_shell((4, 8, 9), h + 1) >= pure_power_macro_shell((8, 9, 25), h + 1)
    for h in range(6, 10):
        assert pure_power_macro_shell((8, 9, 25), h + 1) >= pure_power_macro_shell((4, 8, 9), h + 1)
