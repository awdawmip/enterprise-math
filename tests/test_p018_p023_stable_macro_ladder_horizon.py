import unittest

from enterprise_math.p018_p023_stable_macro_ladder import (
    stable_macro_ladder_tail_data,
)
from enterprise_math.p018_p023_stable_macro_ladder_horizon import (
    next_prime_log_lower_bound,
    stable_macro_ladder_horizon_matches_direct,
    stable_macro_ladder_required_horizon,
    stable_macro_ladder_tail_formula_matches_shell,
    stable_macro_ladder_tail_horizon,
)


class P018P023StableMacroLadderHorizonTests(unittest.TestCase):
    def test_tail_closed_form_matches_exact_shell_scan(self):
        for macro_budget in range(5):
            q, transition, constant = stable_macro_ladder_tail_data(macro_budget)
            for multiplier in range(1, 25):
                max_state = constant * multiplier
                self.assertTrue(
                    stable_macro_ladder_tail_formula_matches_shell(
                        max_state, macro_budget
                    ),
                    (macro_budget, q, transition, constant, max_state),
                )

    def test_shell_horizon_matches_direct_shortest_words_on_small_domains(self):
        for macro_budget in range(4):
            for max_state in range(1, 80):
                self.assertTrue(
                    stable_macro_ladder_horizon_matches_direct(
                        max_state, macro_budget
                    ),
                    (macro_budget, max_state),
                )

    def test_known_tail_formulas(self):
        # s=1: C=2, T=1, q=3 -> 1 + floor(log_3(N/2)).
        self.assertEqual(stable_macro_ladder_tail_horizon(2, 1), 1)
        self.assertEqual(stable_macro_ladder_tail_horizon(6, 1), 2)
        self.assertEqual(stable_macro_ladder_tail_horizon(18, 1), 3)
        self.assertEqual(stable_macro_ladder_tail_horizon(54, 1), 4)

        # s=2: C=12, T=3, q=5 -> 3 + floor(log_5(N/12)).
        self.assertEqual(stable_macro_ladder_tail_horizon(12, 2), 3)
        self.assertEqual(stable_macro_ladder_tail_horizon(60, 2), 4)
        self.assertEqual(stable_macro_ladder_tail_horizon(300, 2), 5)

        # s=3: C=60, T=4, q=7 -> 4 + floor(log_7(N/60)).
        self.assertEqual(stable_macro_ladder_tail_horizon(60, 3), 4)
        self.assertEqual(stable_macro_ladder_tail_horizon(420, 3), 5)
        self.assertEqual(stable_macro_ladder_tail_horizon(2940, 3), 6)

    def test_canonical_ladder_is_within_fixed_additive_gap_of_universal_lower_bound(self):
        for macro_budget in range(5):
            _q, transition, constant = stable_macro_ladder_tail_data(macro_budget)
            for multiplier in range(1, 40):
                max_state = constant * multiplier
                lower = next_prime_log_lower_bound(max_state, macro_budget)
                canonical = stable_macro_ladder_required_horizon(
                    max_state, macro_budget
                )
                self.assertLessEqual(lower, canonical)
                self.assertLessEqual(canonical, lower + transition)


if __name__ == "__main__":
    unittest.main()
