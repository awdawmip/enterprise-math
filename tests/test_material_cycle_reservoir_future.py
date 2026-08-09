import unittest

from enterprise_math.material_cycle_history_precision_bridge import (
    balanced_four_cycle_minimum_relation,
)
from enterprise_math.material_cycle_reservoir_future import (
    all_balanced_cycle_histories_future_distinguishable,
    balanced_cycle_history_shift,
    balanced_cycle_reservoir_after_history,
    balanced_cycle_reservoir_future_report,
)


class MaterialCycleReservoirFutureTests(unittest.TestCase):
    def test_denominator_one_three_hidden_histories_get_three_distinct_next_responses(self):
        relation = balanced_four_cycle_minimum_relation(1)
        futures = [
            balanced_cycle_reservoir_future_report(1, history)
            for history in relation
        ]
        self.assertEqual(len(relation), 3)
        self.assertEqual(
            {report.next_unique_response for report in futures},
            set(relation),
        )
        self.assertTrue(all_balanced_cycle_histories_future_distinguishable(1))

    def test_reservoir_complement_is_exact_opposite_cycle_shift(self):
        for denominator in range(1, 12):
            for history in balanced_four_cycle_minimum_relation(denominator):
                shift = balanced_cycle_history_shift(denominator, history)
                remaining = balanced_cycle_reservoir_after_history(
                    denominator, history
                )
                report = balanced_cycle_reservoir_future_report(
                    denominator, history
                )
                self.assertEqual(report.first_shift, shift)
                self.assertEqual(report.next_shift, -shift)
                self.assertEqual(report.next_unique_response, remaining)
                self.assertEqual(sum(remaining), 4 * denominator)
                self.assertEqual(
                    remaining,
                    (
                        denominator - shift,
                        denominator + shift,
                        denominator - shift,
                        denominator + shift,
                    ),
                )

    def test_precision_growth_of_hidden_histories_is_preserved_as_future_distinguishability(self):
        for denominator in range(1, 20):
            relation = balanced_four_cycle_minimum_relation(denominator)
            self.assertEqual(len(relation), 2 * denominator + 1)
            self.assertTrue(
                all_balanced_cycle_histories_future_distinguishable(denominator)
            )
            futures = {
                balanced_cycle_reservoir_future_report(
                    denominator, history
                ).next_unique_response
                for history in relation
            }
            self.assertEqual(len(futures), 2 * denominator + 1)

    def test_body_identical_histories_can_have_different_unique_material_futures(self):
        denominator = 3
        left = (0, 6, 0, 6)
        center = (3, 3, 3, 3)
        right = (6, 0, 6, 0)
        reports = [
            balanced_cycle_reservoir_future_report(denominator, history)
            for history in (left, center, right)
        ]
        self.assertEqual(
            [report.next_unique_response for report in reports],
            [right, center, left],
        )
        self.assertEqual(
            {report.total_remaining_capacity for report in reports},
            {12},
        )
        # Aggregate reservoir total is also insufficient: it is identical.
        self.assertEqual(len({report.remaining_capacity for report in reports}), 3)

    def test_two_cycles_exactly_deplete_the_declared_reservoir(self):
        for denominator in range(1, 8):
            initial_capacity = (2 * denominator,) * 4
            for history in balanced_four_cycle_minimum_relation(denominator):
                second = balanced_cycle_reservoir_future_report(
                    denominator, history
                ).next_unique_response
                remaining_after_two = tuple(
                    capacity - first - next_value
                    for capacity, first, next_value in zip(
                        initial_capacity, history, second
                    )
                )
                self.assertEqual(remaining_after_two, (0, 0, 0, 0))

    def test_nonminimum_history_is_rejected(self):
        with self.assertRaises(ValueError):
            balanced_cycle_reservoir_future_report(2, (2, 2, 2, 3))
        with self.assertRaises(ValueError):
            balanced_cycle_reservoir_after_history(0, (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
