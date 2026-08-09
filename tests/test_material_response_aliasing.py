import unittest

from enterprise_math.material_response_aliasing import (
    guaranteed_injective_budget,
    kinematic_response_partition,
    material_response_alias_report,
)


class MaterialResponseAliasingTests(unittest.TestCase):
    def test_pairwise_remainder_identity_on_small_domain(self):
        for amplitude in range(1, 20):
            for lower in range(amplitude + 1):
                for upper in range(lower, amplitude + 1):
                    for budget in range(0, 25):
                        report = material_response_alias_report(
                            lower, upper, budget, amplitude
                        )
                        self.assertEqual(
                            report.returned_budget_gap,
                            report.expected_gap_from_remainder,
                        )
                        self.assertEqual(
                            report.aliased,
                            report.lower_returned_budget == report.upper_returned_budget,
                        )

    def test_exact_alias_condition_and_permanent_pair_threshold(self):
        amplitude = 5
        lower = 2
        upper = 3
        # B=2 distinguishes, B=3 aliases again, B=4 distinguishes: low-budget
        # observability is not monotone because the lower-product remainder moves.
        reports = [
            material_response_alias_report(lower, upper, budget, amplitude)
            for budget in (1, 2, 3, 4, 5)
        ]
        self.assertEqual(
            [report.aliased for report in reports],
            [True, False, True, False, False],
        )
        self.assertTrue(all(report.permanent_separation_threshold == 5 for report in reports))
        for budget in range(5, 30):
            self.assertFalse(
                material_response_alias_report(lower, upper, budget, amplitude).aliased
            )

    def test_finite_material_class_count_can_refine_collapse_then_refine(self):
        responses = (2, 3, 5)
        counts = [
            kinematic_response_partition(responses, budget, 5).class_count
            for budget in (1, 2, 3, 4)
        ]
        self.assertEqual(counts, [2, 3, 2, 3])

    def test_minimum_gap_threshold_guarantees_global_injectivity(self):
        for amplitude in range(2, 20):
            responses = tuple(sorted({0, amplitude // 3, (2 * amplitude) // 3, amplitude}))
            threshold = guaranteed_injective_budget(responses, amplitude)
            if len(responses) <= 1:
                self.assertIsNone(threshold)
                continue
            self.assertIsNotNone(threshold)
            for budget in range(threshold, threshold + 10):
                partition = kinematic_response_partition(
                    responses, budget, amplitude
                )
                self.assertTrue(partition.injective)
                self.assertEqual(partition.class_count, len(set(responses)))

    def test_zero_budget_collapses_every_material_response_class(self):
        partition = kinematic_response_partition((0, 1, 3, 7, 10), 0, 10)
        self.assertEqual(partition.class_count, 1)
        self.assertEqual(partition.classes[0].returned_budget, 0)
        self.assertEqual(partition.merged_material_classes, 4)
        self.assertFalse(partition.injective)

    def test_duplicate_material_samples_do_not_create_fake_classes(self):
        partition = kinematic_response_partition((0, 2, 2, 5), 10, 5)
        self.assertEqual(partition.material_responses, (0, 2, 5))
        self.assertTrue(partition.injective)
        self.assertEqual(partition.class_count, 3)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            material_response_alias_report(3, 2, 1, 5)
        with self.assertRaises(ValueError):
            material_response_alias_report(0, 6, 1, 5)
        with self.assertRaises(ValueError):
            kinematic_response_partition((), 1, 5)
        with self.assertRaises(ValueError):
            kinematic_response_partition((0, 1), -1, 5)
        with self.assertRaises(ValueError):
            guaranteed_injective_budget((0, 6), 5)


if __name__ == "__main__":
    unittest.main()
