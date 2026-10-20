import ast
import inspect
import unittest

from enterprise_math import p017_p018_terminal_tail_windows as tail_module
from enterprise_math.p017_p018_terminal_core_compression import terminal_core_signed_profile
from enterprise_math.p017_p018_terminal_tail_windows import terminal_tail_window_profile


class P017P018TerminalTailWindowsTests(unittest.TestCase):
    def test_reference_window_masses_and_exact_terminal_tail_counts(self):
        expected = {
            31: (7, 6, 1, 2),
            8191: (245, 216, 29, 24),
            524_287: (25, 22, 3, 2),
        }
        for k, (integer_mass, bulk, carry, prime_tails) in expected.items():
            data = terminal_tail_window_profile(k)
            self.assertEqual(data["total_window_integer_mass"], integer_mass)
            self.assertEqual(data["total_window_bulk_mass"], bulk)
            self.assertEqual(data["total_window_carry_mass"], carry)
            self.assertEqual(integer_mass, bulk + carry)
            self.assertEqual(data["terminal_prime_tail_count"], prime_tails)
            self.assertTrue(data["tail_windows_pairwise_disjoint"])
            self.assertTrue(data["prime_tails_globally_distinct"])

    def test_every_window_is_one_quotient_response_bulk_plus_binary_carry(self):
        for k in (31, 8191, 524_287):
            data = terminal_tail_window_profile(k)
            for row in data["window_rows"]:
                self.assertIn(row["window_carry"], (0, 1))
                self.assertEqual(
                    row["window_size"],
                    row["window_bulk"] + row["window_carry"],
                )

    def test_prime_tail_window_count_equals_terminal_core_residual(self):
        for k in (31, 8191):
            tails = terminal_tail_window_profile(k)
            direct = terminal_core_signed_profile(k)
            self.assertEqual(
                tails["terminal_prime_tail_count"],
                direct["residual_core_excess"],
            )
            self.assertEqual(
                tuple(tails["terminal_signed_points"]),
                tuple(
                    sorted(int(row["signed_point"]) for row in direct["residual_rows"])
                ),
            )

    def test_524287_only_two_terminal_prime_tail_resources_survive(self):
        data = terminal_tail_window_profile(524_287)
        self.assertEqual(data["terminal_prime_tails"], (590_543, 631_271))
        self.assertEqual(data["terminal_signed_points"], (-105_229, 285_161))

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(tail_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
