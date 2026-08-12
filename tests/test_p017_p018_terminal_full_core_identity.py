import unittest

from enterprise_math.p017_p018_terminal_core_compression import (
    terminal_core_signed_profile,
)
from enterprise_math.p017_p018_terminal_full_core_identity import (
    terminal_complete_core_candidates,
    terminal_full_core_column_identity,
)


class P017P018TerminalFullCoreIdentityTests(unittest.TestCase):
    def test_complete_core_candidate_counts_at_critical_scales(self):
        expected = {
            8_191: (56, 65),
            20_000: (2, 2),
            524_287: (9, 9),
        }
        for k, row in expected.items():
            data = terminal_complete_core_candidates(k)
            self.assertEqual(
                (
                    data["candidate_radical_count"],
                    data["complete_core_candidate_count"],
                ),
                row,
            )

    def test_row_free_column_sum_matches_direct_terminal_residual_on_small_scales(self):
        expected = {
            16: (1, ((15, 1),)),
            22: (0, ()),
            31: (2, ((15, 1), (21, 1))),
            46: (3, ((21, 2), (35, 1))),
        }
        for k, (residual, nonzero) in expected.items():
            columns = terminal_full_core_column_identity(k)
            direct = terminal_core_signed_profile(k)
            observed = tuple(
                (row["complete_core"], row["full_core_incidence"])
                for row in columns["nonzero_complete_core_rows"]
            )
            self.assertEqual(columns["terminal_residual_exact_column_sum"], residual)
            self.assertEqual(direct["residual_core_excess"], residual)
            self.assertEqual(observed, nonzero)

    def test_all_complete_core_candidates_stay_below_k(self):
        for k in (16, 22, 31, 46, 8_191, 20_000, 524_287):
            data = terminal_complete_core_candidates(k)
            self.assertTrue(
                all(1 <= core <= k - 1 for core in data["complete_core_candidates"])
            )


if __name__ == "__main__":
    unittest.main()
