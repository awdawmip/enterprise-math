import unittest

from enterprise_math.material_cycle_history_p023 import (
    AGGREGATE,
    BODY_ONLY,
    CONTACT_LOCAL,
    balanced_cycle_p023_history_report,
)


class MaterialCycleHistoryP023Tests(unittest.TestCase):
    def test_body_only_language_collapses_every_hidden_cycle_history(self):
        for denominator in range(1, 10):
            report = balanced_cycle_p023_history_report(
                denominator, BODY_ONLY
            )
            self.assertEqual(report.hidden_history_count, 2 * denominator + 1)
            self.assertEqual(report.stable_pre_history_class_count, 1)
            self.assertEqual(report.stable_post_history_class_count, 1)
            self.assertEqual(report.stable_total_class_count, 1)
            self.assertTrue(report.all_hidden_histories_merge)
            self.assertFalse(report.all_hidden_histories_future_distinguished)

    def test_aggregate_impulse_language_still_cannot_see_contact_local_history(self):
        for denominator in range(1, 10):
            report = balanced_cycle_p023_history_report(
                denominator, AGGREGATE
            )
            self.assertEqual(report.stable_pre_history_class_count, 1)
            self.assertEqual(report.stable_post_history_class_count, 1)
            # PRE and POST aggregate protocol stages remain distinct current
            # observations, but hidden t is still safely erased.
            self.assertEqual(report.stable_total_class_count, 2)
            self.assertTrue(report.all_hidden_histories_merge)

    def test_contact_local_future_language_recovers_every_hidden_history_in_one_reload(self):
        for denominator in range(1, 12):
            report = balanced_cycle_p023_history_report(
                denominator, CONTACT_LOCAL
            )
            expected = 2 * denominator + 1
            self.assertEqual(report.hidden_history_count, expected)
            self.assertEqual(report.stable_pre_history_class_count, expected)
            self.assertEqual(report.stable_post_history_class_count, expected)
            self.assertTrue(report.all_hidden_histories_future_distinguished)
            self.assertFalse(report.all_hidden_histories_merge)

    def test_same_current_body_observation_splits_only_after_contact_local_future_is_declared(self):
        body = balanced_cycle_p023_history_report(3, BODY_ONLY)
        local = balanced_cycle_p023_history_report(3, CONTACT_LOCAL)
        pre_states = [state for state in local.domain if state[0] == "PRE"]
        self.assertEqual(
            {body.initial_observation[state] for state in pre_states},
            {("BODY_ZERO",)},
        )
        self.assertEqual(
            len({body.stable_partition[state] for state in pre_states}),
            1,
        )
        self.assertEqual(
            len({local.stable_partition[state] for state in pre_states}),
            7,
        )

    def test_precision_growth_is_language_relative_not_automatic_state_growth(self):
        body_counts = []
        local_counts = []
        for denominator in (1, 2, 4, 8):
            body_counts.append(
                balanced_cycle_p023_history_report(
                    denominator, BODY_ONLY
                ).stable_pre_history_class_count
            )
            local_counts.append(
                balanced_cycle_p023_history_report(
                    denominator, CONTACT_LOCAL
                ).stable_pre_history_class_count
            )
        self.assertEqual(body_counts, [1, 1, 1, 1])
        self.assertEqual(local_counts, [3, 5, 9, 17])

    def test_invalid_language_or_denominator_is_rejected(self):
        with self.assertRaises(ValueError):
            balanced_cycle_p023_history_report(0, BODY_ONLY)
        with self.assertRaises(ValueError):
            balanced_cycle_p023_history_report(1, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
