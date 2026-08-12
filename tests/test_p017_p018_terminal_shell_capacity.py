import ast
import inspect
import unittest

from enterprise_math import p017_p018_terminal_shell_capacity as shell_module
from enterprise_math.p017_p018_terminal_core_compression import terminal_core_signed_profile
from enterprise_math.p017_p018_terminal_shell_capacity import (
    terminal_full_core_candidates,
    terminal_power_depth_ceiling,
    terminal_shell_divisor_capacity,
    terminal_shell_exact_incidence,
)


class P017P018TerminalShellCapacityTests(unittest.TestCase):
    def test_reference_shell_sizes_and_divisor_capacities(self):
        expected = {
            31: (2, 2, 0, 3),
            8191: (56, 65, 1, 121),
            524_287: (9, 9, 0, 13),
        }
        for k, (radicals, blocks, power_depth, capacity) in expected.items():
            data = terminal_shell_divisor_capacity(k)
            self.assertEqual(data["candidate_count"], radicals)
            self.assertEqual(data["full_core_candidate_count"], blocks)
            self.assertEqual(data["maximum_extra_prime_multiplicity"], power_depth)
            self.assertLessEqual(
                data["maximum_extra_prime_multiplicity"],
                data["power_depth_ceiling"],
            )
            self.assertEqual(data["terminal_residual_divisor_capacity"], capacity)

    def test_analytic_power_depth_ceiling_matches_reference_scales(self):
        expected = {
            8191: (3, 1, False),
            524_287: (3, 0, True),
            2_147_483_647: (3, 2, False),
        }
        for k, (least_prime, depth, squarefree) in expected.items():
            data = terminal_power_depth_ceiling(k)
            self.assertEqual(data["smallest_transverse_prime"], least_prime)
            self.assertEqual(data["power_depth_ceiling"], depth)
            self.assertEqual(data["terminal_shell_forced_squarefree"], squarefree)
            self.assertLessEqual(data["largest_minimum_power_product"], k - 1)
            self.assertGreater(data["first_forbidden_power_product"], k - 1)

    def test_524287_terminal_shell_is_forced_squarefree(self):
        data = terminal_full_core_candidates(524_287)
        self.assertTrue(data["terminal_shell_squarefree"])
        self.assertTrue(data["terminal_shell_forced_squarefree"])
        self.assertEqual(
            data["full_core_candidates"],
            (255_255, 285_285, 345_345, 373_065, 435_435, 440_895, 451_605, 465_465, 504_735),
        )

    def test_small_exact_full_core_column_sum_equals_terminal_residual(self):
        exact = terminal_shell_exact_incidence(31, verify_direct=True)
        direct = terminal_core_signed_profile(31)
        self.assertEqual(exact["terminal_residual_exact_incidence"], direct["residual_core_excess"])
        self.assertEqual(exact["terminal_residual_exact_incidence"], 2)
        self.assertTrue(exact["terminal_residual_identity"])

    def test_divisor_shell_capacity_dominates_observed_residual_rows(self):
        for k in (31, 8191):
            bound = terminal_shell_divisor_capacity(k)
            actual = terminal_core_signed_profile(k)
            self.assertLessEqual(
                actual["residual_core_excess"],
                bound["terminal_residual_divisor_capacity"],
            )

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(shell_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
