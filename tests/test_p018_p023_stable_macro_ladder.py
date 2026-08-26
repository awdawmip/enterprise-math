import unittest

from enterprise_math.p018_p023_stable_macro_ladder import (
    direct_shortest_ladder_word_length,
    stable_macro_ladder,
    stable_macro_ladder_cheap_slots,
    stable_macro_ladder_shell,
    stable_macro_ladder_shell_matches_direct,
    stable_macro_ladder_tail_data,
)


class P018P023StableMacroLadderTests(unittest.TestCase):
    def test_first_canonical_ladders(self):
        expected = {
            0: (2, (), (), (2, 0, 1)),
            1: (3, (4,), (2,), (3, 1, 2)),
            2: (5, (8, 9), (2, 2, 3), (5, 3, 12)),
            3: (7, (8, 9, 25), (2, 2, 3, 5), (7, 4, 60)),
            4: (11, (16, 27, 25, 49), (2, 2, 2, 3, 3, 5, 7), (11, 7, 2520)),
        }
        for macro_budget, (q, macros, cheap, tail) in expected.items():
            self.assertEqual(stable_macro_ladder(macro_budget), (q, macros))
            self.assertEqual(
                stable_macro_ladder_cheap_slots(macro_budget), cheap
            )
            self.assertEqual(stable_macro_ladder_tail_data(macro_budget), tail)

    def test_closed_shell_matches_independent_shortest_word_search(self):
        for macro_budget in range(4):
            for cost in range(1, 7):
                self.assertTrue(
                    stable_macro_ladder_shell_matches_direct(macro_budget, cost),
                    (macro_budget, cost),
                )

    def test_tail_recurrence_uses_next_prime(self):
        for macro_budget in range(5):
            q, transition, _constant = stable_macro_ladder_tail_data(macro_budget)
            for cost in range(max(transition, 1), max(transition, 1) + 5):
                self.assertEqual(
                    stable_macro_ladder_shell(macro_budget, cost + 1),
                    q * stable_macro_ladder_shell(macro_budget, cost),
                )

    def test_each_predicted_shell_is_an_exact_cost_witness(self):
        for macro_budget in range(4):
            for cost in range(1, 7):
                boundary = stable_macro_ladder_shell(macro_budget, cost)
                self.assertEqual(
                    direct_shortest_ladder_word_length(boundary, macro_budget),
                    cost,
                )

    def test_shell_is_strictly_increasing(self):
        for macro_budget in range(5):
            shells = [
                stable_macro_ladder_shell(macro_budget, cost)
                for cost in range(0, 9)
            ]
            self.assertEqual(shells[0], 1)
            self.assertTrue(all(a < b for a, b in zip(shells, shells[1:])))


if __name__ == "__main__":
    unittest.main()
