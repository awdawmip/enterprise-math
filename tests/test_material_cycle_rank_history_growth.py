import unittest

from enterprise_math.material_contact_network_cycle_kernel import contact_cycle_rank
from enterprise_math.material_cycle_rank_history_growth import (
    cycle_rank_history_growth_report,
    disjoint_balanced_cycle_minimum_history_count,
    disjoint_balanced_cycle_minimum_relation,
    disjoint_balanced_cycle_network,
)


class MaterialCycleRankHistoryGrowthTests(unittest.TestCase):
    def test_network_cycle_rank_matches_number_of_disjoint_balanced_cycles(self):
        for beta in range(1, 6):
            state = disjoint_balanced_cycle_network(beta)
            self.assertEqual(len(state.masses), 4 * beta)
            self.assertEqual(len(state.contacts), 4 * beta)
            self.assertEqual(contact_cycle_rank(state), beta)

    def test_history_class_count_is_exactly_two_s_plus_one_to_cycle_rank(self):
        for beta in range(1, 5):
            for denominator in range(1, 5):
                expected = (2 * denominator + 1) ** beta
                self.assertEqual(
                    disjoint_balanced_cycle_minimum_history_count(
                        beta, denominator
                    ),
                    expected,
                )
                # Keep actual relation materialization bounded for test runtime.
                if expected <= 1000:
                    self.assertEqual(
                        len(
                            disjoint_balanced_cycle_minimum_relation(
                                beta, denominator
                            )
                        ),
                        expected,
                    )

    def test_report_verifies_body_score_energy_invisibility_and_future_distinguishability(self):
        for beta, denominator in ((1, 4), (2, 2), (3, 1)):
            report = cycle_rank_history_growth_report(beta, denominator)
            self.assertEqual(report.cycle_rank, beta)
            self.assertEqual(report.history_class_count, (2 * denominator + 1) ** beta)
            self.assertEqual(
                report.minimum_total_impulse_numerator,
                4 * beta * denominator,
            )
            self.assertTrue(all(value == 0 for value in report.common_body_after_numerators))
            self.assertTrue(all(value == 0 for value in report.common_final_score_numerators))
            self.assertEqual(report.common_kinetic_after_numerator, 0)
            self.assertTrue(
                report.all_histories_future_distinguishable_under_reservoir_reload
            )

    def test_true_precision_refinement_embeds_old_product_histories_and_adds_new_classes(self):
        beta = 2
        coarse_s = 1
        fine_s = 3
        coarse = disjoint_balanced_cycle_minimum_relation(beta, coarse_s)
        fine = set(disjoint_balanced_cycle_minimum_relation(beta, fine_s))
        multiplier = fine_s // coarse_s
        embedded = {
            tuple(multiplier * value for value in history)
            for history in coarse
        }
        self.assertTrue(embedded.issubset(fine))
        self.assertEqual(len(coarse), 3**2)
        self.assertEqual(len(fine), 7**2)
        self.assertEqual(len(fine) - len(coarse), 40)

    def test_precision_and_cycle_rank_both_increase_hidden_material_state_count(self):
        self.assertLess(
            disjoint_balanced_cycle_minimum_history_count(1, 4),
            disjoint_balanced_cycle_minimum_history_count(2, 4),
        )
        self.assertLess(
            disjoint_balanced_cycle_minimum_history_count(2, 2),
            disjoint_balanced_cycle_minimum_history_count(2, 3),
        )

    def test_invalid_cycle_rank_or_denominator_is_rejected(self):
        with self.assertRaises(ValueError):
            disjoint_balanced_cycle_network(0)
        with self.assertRaises(ValueError):
            disjoint_balanced_cycle_minimum_relation(1, 0)
        with self.assertRaises(ValueError):
            cycle_rank_history_growth_report(0, 1)


if __name__ == "__main__":
    unittest.main()
