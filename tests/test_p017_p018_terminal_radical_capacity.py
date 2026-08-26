import unittest

from enterprise_math.p017_p018_terminal_core_compression import (
    terminal_core_signed_profile,
)
from enterprise_math.p017_p018_terminal_radical_capacity import (
    terminal_radical_capacity,
)


class P017P018TerminalRadicalCapacityTests(unittest.TestCase):
    def test_exact_candidate_capacity_checkpoints(self):
        # (candidate_count, universal radical sum, raw aligned sum,
        #  exact anchor sum, exact anchor union, previous uniform-overlap bound)
        expected = {
            8_191: (56, 143, 108, 108, 72, 8_191),
            20_000: (2, 4, 2, 1, 1, 260),
            524_287: (9, 19, 13, 13, 13, 34_953),
        }
        for k, row in expected.items():
            data = terminal_radical_capacity(k)
            self.assertEqual(
                (
                    data["candidate_count"],
                    data["universal_radical_capacity_sum"],
                    data["raw_aligned_radical_capacity_sum"],
                    data["exact_anchor_radical_capacity_sum"],
                    data["exact_anchor_fiber_union_capacity"],
                    data["previous_uniform_overlap_capacity"],
                ),
                row,
            )
            self.assertTrue(data["strictly_improves_uniform_overlap"])
            self.assertEqual(data["active_capacity_source"], "exact_anchor_fiber_union")
            self.assertEqual(
                data["combined_terminal_capacity"],
                data["exact_anchor_fiber_union_capacity"],
            )

    def test_every_candidate_capacity_forms_the_exact_chain(self):
        for k in (8_191, 20_000, 524_287):
            data = terminal_radical_capacity(k)
            for row in data["radical_capacity_rows"]:
                radical = row["radical"]
                self.assertEqual(
                    row["cg12_universal_capacity"],
                    (k - 1) // radical + 1,
                )
                self.assertEqual(
                    row["exact_anchor_capacity"],
                    len(row["anchor_signed_points"]),
                )
                self.assertLessEqual(
                    row["exact_anchor_capacity"],
                    row["raw_aligned_capacity"],
                )
                self.assertLessEqual(
                    row["raw_aligned_capacity"],
                    row["cg12_universal_capacity"],
                )

    def test_k8191_union_removes_cross_radical_duplicate_points(self):
        data = terminal_radical_capacity(8_191)
        self.assertEqual(data["exact_anchor_radical_capacity_sum"], 108)
        self.assertEqual(data["exact_anchor_fiber_union_capacity"], 72)
        self.assertLess(
            data["exact_anchor_fiber_union_capacity"],
            data["exact_anchor_radical_capacity_sum"],
        )

    def test_k20000_anchor_filter_removes_second_candidate_column(self):
        data = terminal_radical_capacity(20_000)
        rows = {row["radical"]: row for row in data["radical_capacity_rows"]}
        self.assertEqual(rows[17_017]["exact_anchor_capacity"], 1)
        self.assertEqual(rows[19_019]["raw_aligned_capacity"], 1)
        self.assertEqual(rows[19_019]["exact_anchor_capacity"], 0)

    def test_observed_terminal_residual_checkpoint_counts(self):
        expected = {
            8_191: 24,
            20_000: 0,
            524_287: 2,
        }
        for k, residual in expected.items():
            bound = terminal_radical_capacity(k)
            actual = terminal_core_signed_profile(k)
            self.assertEqual(actual["residual_core_excess"], residual)
            self.assertLessEqual(
                residual,
                bound["combined_terminal_capacity"],
            )


if __name__ == "__main__":
    unittest.main()
