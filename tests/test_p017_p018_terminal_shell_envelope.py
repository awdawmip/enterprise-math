import ast
import inspect
import unittest

from enterprise_math import p017_p018_terminal_shell_envelope as envelope_module
from enterprise_math.p017_p018_terminal_shell_capacity import terminal_full_core_candidates
from enterprise_math.p017_p018_terminal_shell_envelope import (
    terminal_replacement_depth_envelope,
)
from enterprise_math.p017_p018_terminal_tail_windows import terminal_tail_window_profile


class P017P018TerminalShellEnvelopeTests(unittest.TestCase):
    def test_reference_depth_weighted_envelopes(self):
        expected = {
            8191: (233, 493, 5075),
            524_287: (40, 40, 146),
            2_147_483_647: (299_747, 3_779_055, 51_114_465),
        }
        for k, (radicals, full_cores, windows) in expected.items():
            data = terminal_replacement_depth_envelope(k)
            self.assertEqual(data["terminal_radical_candidate_bound"], radicals)
            self.assertEqual(data["terminal_full_core_candidate_bound"], full_cores)
            self.assertEqual(data["terminal_window_integer_mass_bound"], windows)
            self.assertTrue(data["bound_is_basin_row_independent"])

    def test_envelope_dominates_exact_shell_without_scanning_basin_rows(self):
        for k in (8191, 524_287):
            bound = terminal_replacement_depth_envelope(k)
            exact_shell = terminal_full_core_candidates(k)
            exact_windows = terminal_tail_window_profile(k)
            self.assertLessEqual(
                exact_shell["candidate_count"],
                bound["terminal_radical_candidate_bound"],
            )
            self.assertLessEqual(
                exact_shell["full_core_candidate_count"],
                bound["terminal_full_core_candidate_bound"],
            )
            self.assertLessEqual(
                exact_windows["total_window_integer_mass"],
                bound["terminal_window_integer_mass_bound"],
            )

    def test_large_critical_scale_bound_is_strictly_sublinear_numerically(self):
        k = 2_147_483_647
        data = terminal_replacement_depth_envelope(k)
        self.assertLess(data["terminal_window_integer_mass_bound"], k)
        self.assertLess(40 * data["terminal_window_integer_mass_bound"], k)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(envelope_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
