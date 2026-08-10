import unittest

from enterprise_math.p017_p018_terminal_core_compression import (
    terminal_core_signed_profile,
)
from enterprise_math.p017_p018_terminal_radical_capacity import (
    terminal_radical_capacity,
)


class P017P018TerminalRadicalCapacityTests(unittest.TestCase):
    def test_exact_candidate_capacity_checkpoints(self):
        expected = {
            8_191: (56, 143, 8_191),
            20_000: (2, 4, 260),
            524_287: (9, 19, 34_953),
        }
        for k, row in expected.items():
            data = terminal_radical_capacity(k)
            self.assertEqual(
                (
                    data["candidate_count"],
                    data["exact_radical_capacity_sum"],
                    data["previous_uniform_overlap_capacity"],
                ),
                row,
            )
            self.assertTrue(data["strictly_improves_uniform_overlap"])
            self.assertEqual(data["active_capacity_source"], "exact_radical_sum")
            self.assertEqual(
                data["combined_terminal_capacity"],
                data["exact_radical_capacity_sum"],
            )

    def test_every_candidate_capacity_is_cg12_integer_bound(self):
        for k in (8_191, 20_000, 524_287):
            data = terminal_radical_capacity(k)
            for row in data["radical_capacity_rows"]:
                radical = row["radical"]
                self.assertEqual(
                    row["signed_reuse_capacity"],
                    (k - 1) // radical + 1,
                )

    def test_observed_terminal_residual_is_below_exact_radical_sum(self):
        for k in (8_191, 20_000, 524_287):
            bound = terminal_radical_capacity(k)
            actual = terminal_core_signed_profile(k)
            self.assertLessEqual(
                actual["residual_core_excess"],
                bound["combined_terminal_capacity"],
            )


if __name__ == "__main__":
    unittest.main()
