import unittest

from enterprise_math.p017_p018_terminal_candidate_exact import (
    terminal_candidate_exact_profile,
)


class P017P018TerminalCandidateExactTests(unittest.TestCase):
    def test_reduced_candidate_checkpoints(self):
        expected = {
            8_191: (56, 72, 26, 24),
            20_000: (2, 1, 0, 0),
            524_287: (9, 13, 2, 2),
        }
        for k, row in expected.items():
            data = terminal_candidate_exact_profile(k)
            self.assertEqual(
                (
                    data["candidate_radical_count"],
                    data["candidate_signed_point_count"],
                    data["exact_j_support_candidate_count"],
                    data["terminal_residual_count"],
                ),
                row,
            )

    def test_k524287_two_residual_full_cores_are_exact(self):
        data = terminal_candidate_exact_profile(524_287)
        self.assertEqual(
            data["terminal_residual_cores"],
            (435_435, 465_465),
        )
        self.assertEqual(len(data["terminal_residual_points"]), 2)

    def test_terminal_residual_rows_have_declared_support_depth_and_low_core(self):
        for k in (8_191, 20_000, 524_287):
            data = terminal_candidate_exact_profile(k)
            j = data["transverse_primorial_depth"]
            residual_rows = [
                row for row in data["rows"] if row["terminal_low_core_residual"]
            ]
            self.assertEqual(len(residual_rows), data["terminal_residual_count"])
            for row in residual_rows:
                self.assertEqual(row["support_size"], j)
                self.assertLessEqual(row["complete_transverse_core"], k - 1)
                self.assertIn(
                    row["support_radical"],
                    row["candidate_radicals"],
                )


if __name__ == "__main__":
    unittest.main()
