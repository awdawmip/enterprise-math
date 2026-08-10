import unittest

from enterprise_math.partial_action_precision_genesis import (
    constant_observation,
    countdown_domain,
    countdown_literal_signature,
    countdown_partial_partition_sequence,
    countdown_predictive_class_count,
    countdown_predictive_key,
    countdown_word_defined,
    countdown_wrong_total_partition_sequence,
    partial_countdown_action,
    precision_genesis_report,
    totalized_identity_countdown_action,
)


class PartialActionPrecisionGenesisTests(unittest.TestCase):
    def test_countdown_word_defined_iff_length_does_not_exceed_state(self):
        for state in range(10):
            for repetitions in range(12):
                self.assertEqual(
                    countdown_word_defined(state, repetitions),
                    repetitions <= state,
                )

    def test_horizon_equivalence_key_is_exact_minimum(self):
        maximum_state = 8
        for horizon in range(11):
            for state in countdown_domain(maximum_state):
                self.assertEqual(
                    countdown_predictive_key(
                        state, maximum_state, horizon
                    ),
                    min(state, horizon),
                )

    def test_partial_partition_sequence_grows_one_class_per_horizon_until_discrete(self):
        for maximum_state in range(1, 10):
            stages = countdown_partial_partition_sequence(maximum_state)
            counts = tuple(len(set(stage.values())) for stage in stages)
            self.assertEqual(
                counts,
                tuple(range(1, maximum_state + 2)),
            )
            terminal = stages[-1]
            self.assertEqual(len(set(terminal.values())), maximum_state + 1)

    def test_closed_class_count_matches_partition_compiler(self):
        for maximum_state in range(1, 10):
            stages = countdown_partial_partition_sequence(maximum_state)
            for horizon, stage in enumerate(stages):
                self.assertEqual(
                    len(set(stage.values())),
                    countdown_predictive_class_count(
                        maximum_state, horizon
                    ),
                )
            for horizon in range(maximum_state, maximum_state + 5):
                self.assertEqual(
                    countdown_predictive_class_count(
                        maximum_state, horizon
                    ),
                    maximum_state + 1,
                )

    def test_literal_signatures_match_min_state_horizon_partition(self):
        maximum_state = 7
        states = countdown_domain(maximum_state)
        for horizon in range(0, maximum_state + 2):
            signatures = {
                state: countdown_literal_signature(
                    state, maximum_state, horizon
                )
                for state in states
            }
            for left in states:
                for right in states:
                    self.assertEqual(
                        signatures[left] == signatures[right],
                        countdown_predictive_key(
                            left, maximum_state, horizon
                        )
                        == countdown_predictive_key(
                            right, maximum_state, horizon
                        ),
                    )

    def test_constant_current_observation_has_one_class_before_future_actions(self):
        for maximum_state in range(1, 10):
            observation = constant_observation(maximum_state)
            self.assertEqual(set(observation.values()), {0})
            self.assertEqual(
                countdown_predictive_class_count(maximum_state, 0),
                1,
            )

    def test_disabled_as_identity_total_comparator_never_generates_precision(self):
        for maximum_state in range(1, 10):
            stages = countdown_wrong_total_partition_sequence(maximum_state)
            self.assertEqual(len(stages), 1)
            self.assertEqual(set(stages[0].values()), {0})
            total = totalized_identity_countdown_action(maximum_state)
            self.assertEqual(total[0], 0)
            self.assertEqual(set(total), set(countdown_domain(maximum_state)))

    def test_partial_action_has_exact_one_missing_domain_state(self):
        for maximum_state in range(1, 10):
            action = partial_countdown_action(maximum_state)
            self.assertNotIn(0, action)
            self.assertEqual(
                set(action),
                set(range(1, maximum_state + 1)),
            )
            self.assertTrue(
                all(action[state] == state - 1 for state in action)
            )

    def test_report_quantifies_generated_predictive_precision(self):
        for maximum_state in range(1, 12):
            report = precision_genesis_report(maximum_state)
            self.assertEqual(report.current_class_count, 1)
            self.assertEqual(
                report.terminal_class_count,
                maximum_state + 1,
            )
            self.assertEqual(
                report.generated_predictive_classes,
                maximum_state,
            )
            self.assertEqual(
                report.stage_class_counts,
                tuple(range(1, maximum_state + 2)),
            )
            self.assertEqual(report.wrong_total_stage_count, 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            countdown_domain(0)
        with self.assertRaises(TypeError):
            countdown_domain(True)
        with self.assertRaises(ValueError):
            countdown_predictive_key(5, 3, 1)
        with self.assertRaises(ValueError):
            countdown_predictive_key(0, 3, -1)
        with self.assertRaises(ValueError):
            countdown_word_defined(-1, 0)
        with self.assertRaises(TypeError):
            countdown_word_defined(1, True)


if __name__ == "__main__":
    unittest.main()
