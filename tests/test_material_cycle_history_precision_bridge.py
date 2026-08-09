import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from enterprise_math.material_cycle_history_precision_bridge import (
    balanced_four_cycle_circulation,
    balanced_four_cycle_history_precision_report,
    balanced_four_cycle_minimum_relation,
    balanced_four_cycle_state,
    new_hidden_history_classes_under_refinement,
)


def compositions4(total: int):
    for a in range(total + 1):
        for b in range(total - a + 1):
            for c in range(total - a - b + 1):
                d = total - a - b - c
                yield (a, b, c, d)


class MaterialCycleHistoryPrecisionBridgeTests(unittest.TestCase):
    def test_balanced_cycle_kernel_has_zero_sum_primitive_circulation(self):
        self.assertEqual(
            balanced_four_cycle_circulation(),
            (1, -1, 1, -1),
        )
        self.assertEqual(sum(balanced_four_cycle_circulation()), 0)

    def test_denominator_one_has_exact_three_way_hidden_minimum_history(self):
        report = balanced_four_cycle_history_precision_report(1)
        self.assertEqual(report.minimum_total_impulse_numerator, 4)
        self.assertEqual(report.history_class_count, 3)
        self.assertEqual(
            report.impulse_relation,
            ((0, 2, 0, 2), (1, 1, 1, 1), (2, 0, 2, 0)),
        )
        self.assertEqual(report.common_body_after_numerators, (0, 0, 0, 0))
        self.assertEqual(report.common_final_score_numerators, (0, 0, 0, 0))
        self.assertEqual(report.common_kinetic_after_numerator, 0)
        # A body-only state cannot tell whether contact 0 accumulated 0, 1 or 2.
        self.assertEqual(
            {vector[0] for vector in report.impulse_relation},
            {0, 1, 2},
        )

    def test_history_fiber_grows_exactly_as_two_s_plus_one(self):
        for denominator in range(1, 20):
            report = balanced_four_cycle_history_precision_report(denominator)
            self.assertEqual(report.history_class_count, 2 * denominator + 1)
            self.assertEqual(len(report.impulse_relation), 2 * denominator + 1)
            self.assertTrue(
                all(sum(vector) == 4 * denominator for vector in report.impulse_relation)
            )

    def test_true_refinement_embeds_old_histories_and_adds_intermediate_classes(self):
        coarse = balanced_four_cycle_minimum_relation(2)
        fine = balanced_four_cycle_minimum_relation(6)
        scaled_coarse = {
            tuple(3 * value for value in vector)
            for vector in coarse
        }
        self.assertTrue(scaled_coarse.issubset(set(fine)))
        self.assertEqual(len(fine) - len(coarse), 8)
        self.assertEqual(new_hidden_history_classes_under_refinement(2, 6), 8)

    def test_bounded_oracle_confirms_exact_minimum_total_relation(self):
        state = balanced_four_cycle_state()
        for denominator in range(1, 4):
            scaled = ContactNetworkMomentum1D(
                masses=state.masses,
                momenta=tuple(denominator * value for value in state.momenta),
                contacts=state.contacts,
            )
            target_total = 4 * denominator
            feasible_minimum = []
            for vector in compositions4(target_total):
                step = apply_contact_impulse_vector(scaled, vector)
                if all(score >= 0 for score in step.relative_scores_after):
                    feasible_minimum.append(vector)
            self.assertEqual(
                set(feasible_minimum),
                set(balanced_four_cycle_minimum_relation(denominator)),
            )
            # Any smaller total is impossible by the summed-score lower bound;
            # bounded brute force confirms the first few precision cells.
            for smaller_total in range(target_total):
                self.assertFalse(
                    any(
                        all(
                            score >= 0
                            for score in apply_contact_impulse_vector(
                                scaled, vector
                            ).relative_scores_after
                        )
                        for vector in compositions4(smaller_total)
                    )
                )

    def test_cycle_related_histories_keep_body_score_total_and_energy_identical(self):
        report = balanced_four_cycle_history_precision_report(5)
        left = report.impulse_relation[0]
        right = report.impulse_relation[-1]
        self.assertNotEqual(left, right)
        self.assertEqual(sum(left), sum(right))
        self.assertEqual(report.common_body_after_numerators, (0, 0, 0, 0))
        self.assertEqual(report.common_final_score_numerators, (0, 0, 0, 0))
        self.assertEqual(report.common_kinetic_after_numerator, 0)
        self.assertNotEqual(left[0], right[0])
        self.assertNotEqual(left[1], right[1])

    def test_nondivisibility_is_not_called_refinement(self):
        with self.assertRaises(ValueError):
            new_hidden_history_classes_under_refinement(2, 3)
        with self.assertRaises(ValueError):
            balanced_four_cycle_history_precision_report(0)


if __name__ == "__main__":
    unittest.main()
