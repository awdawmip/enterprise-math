import unittest

from enterprise_math.witness_threshold_precision import (
    analyze_threshold_repair,
    project_truncated_cost,
    repaired_threshold_state,
    threshold_profile,
    threshold_signature_equivalent,
    truncated_witness_cost,
    truncation_chain_compatible,
)


class WitnessThresholdPrecisionTests(unittest.TestCase):
    def test_truncation_matches_threshold_profile(self) -> None:
        for cutoff in range(6):
            for left in (0, 1, 2, 5, 9, None):
                for right in (0, 1, 2, 5, 9, None):
                    self.assertEqual(
                        threshold_signature_equivalent(left, right, cutoff),
                        truncated_witness_cost(left, cutoff)
                        == truncated_witness_cost(right, cutoff),
                    )

    def test_infinity_and_large_cost_coalesce_at_finite_cutoff(self) -> None:
        self.assertEqual(truncated_witness_cost(None, 3), 4)
        self.assertEqual(truncated_witness_cost(99, 3), 4)
        self.assertEqual(threshold_profile(None, 3), (False, False, False, False))
        self.assertEqual(threshold_profile(99, 3), (False, False, False, False))

    def test_truncation_chain_projects_exactly(self) -> None:
        for cost in (0, 1, 2, 5, 9, None):
            for high in range(6):
                for low in range(high + 1):
                    self.assertTrue(truncation_chain_compatible(cost, low, high))
        self.assertEqual(project_truncated_cost(7, 2), 3)

    def test_repaired_state_keeps_base_and_only_needed_cost(self) -> None:
        self.assertEqual(repaired_threshold_state("same-rad", 1, 1), ("same-rad", 1))
        self.assertEqual(repaired_threshold_state("same-rad", 2, 1), ("same-rad", 2))
        self.assertEqual(repaired_threshold_state("same-rad", 9, 1), ("same-rad", 2))

    def test_finite_coarsest_repair(self) -> None:
        base = {
            "123": (1, 2, 3),
            "189": (1, 2, 3),
            "large": (1, 2, 3),
            "other": (1, 3, 4),
        }
        costs = {"123": 1, "189": 2, "large": 9, "other": 1}

        cutoff_1 = analyze_threshold_repair(base, costs, 1)
        self.assertEqual(cutoff_1["block_count"], 3)
        self.assertEqual(
            cutoff_1["repaired_states"]["189"],
            cutoff_1["repaired_states"]["large"],
        )

        cutoff_2 = analyze_threshold_repair(base, costs, 2)
        self.assertEqual(cutoff_2["block_count"], 4)
        self.assertNotEqual(
            cutoff_2["repaired_states"]["189"],
            cutoff_2["repaired_states"]["large"],
        )

    def test_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            truncated_witness_cost(-1, 2)
        with self.assertRaises(ValueError):
            analyze_threshold_repair({"a": 1}, {"b": 2}, 1)


if __name__ == "__main__":
    unittest.main()
