import unittest
from fractions import Fraction

from enterprise_math.precision_genesis_operation_envelope import (
    genesis_class_count,
    genesis_collision_ambiguity,
    genesis_operation_trajectory,
    genesis_pair_ambiguity,
    genesis_partial_operation_valley_horizon,
    genesis_partial_safe_probability,
    genesis_partial_safe_probability_closed,
    genesis_predictive_shape,
    genesis_shape_is_fixed_class_operation_maximum,
    genesis_tail_size,
    genesis_total_operation_valley_horizon,
    genesis_total_safe_probability,
    genesis_total_safe_probability_closed,
)
from enterprise_math.operation_freedom_majorization import (
    operation_freedom_range,
)


class PrecisionGenesisOperationEnvelopeTests(unittest.TestCase):
    def test_every_genesis_shape_is_fixed_class_operation_maximum(self):
        checked = 0
        for state_count in range(2, 30):
            for horizon in range(state_count):
                self.assertTrue(
                    genesis_shape_is_fixed_class_operation_maximum(
                        state_count, horizon
                    )
                )
                report = operation_freedom_range(
                    state_count,
                    genesis_class_count(state_count, horizon),
                )
                self.assertEqual(
                    genesis_predictive_shape(state_count, horizon),
                    report.imbalanced_shape,
                )
                checked += 1
        self.assertGreater(checked, 400)

    def test_closed_probabilities_match_majorization_counts(self):
        for state_count in range(2, 40):
            for horizon in range(state_count):
                self.assertEqual(
                    genesis_total_safe_probability(
                        state_count, horizon
                    ),
                    genesis_total_safe_probability_closed(
                        state_count, horizon
                    ),
                )
                self.assertEqual(
                    genesis_partial_safe_probability(
                        state_count, horizon
                    ),
                    genesis_partial_safe_probability_closed(
                        state_count, horizon
                    ),
                )

    def test_class_count_rises_while_pair_ambiguity_falls(self):
        for state_count in range(2, 30):
            trajectory = genesis_operation_trajectory(state_count)
            self.assertEqual(
                tuple(stage.class_count for stage in trajectory),
                tuple(range(1, state_count + 1)),
            )
            self.assertEqual(
                tuple(stage.tail_size for stage in trajectory),
                tuple(range(state_count, 0, -1)),
            )
            pair_values = tuple(
                stage.pair_ambiguity for stage in trajectory
            )
            self.assertEqual(pair_values[-1], 0)
            self.assertTrue(
                all(
                    left > right
                    for left, right in zip(
                        pair_values[:-1], pair_values[1:]
                    )
                )
            )

    def test_all_collision_orders_are_tail_binomials(self):
        from math import comb

        for state_count in range(2, 16):
            for horizon in range(state_count):
                tail = state_count - horizon
                for order in range(2, state_count + 2):
                    expected = (
                        comb(tail, order) if tail >= order else 0
                    )
                    self.assertEqual(
                        genesis_collision_ambiguity(
                            state_count, horizon, order
                        ),
                        expected,
                    )

    def test_total_operation_freedom_reconnects_at_both_filtration_endpoints(self):
        for state_count in range(3, 40):
            self.assertEqual(
                genesis_total_safe_probability(state_count, 0),
                Fraction(1, 1),
            )
            self.assertEqual(
                genesis_total_safe_probability(
                    state_count, state_count - 1
                ),
                Fraction(1, 1),
            )
            valley = genesis_total_operation_valley_horizon(
                state_count
            )
            self.assertGreater(valley, 0)
            self.assertLess(valley, state_count - 1)
            valley_probability = genesis_total_safe_probability(
                state_count, valley
            )
            self.assertLess(valley_probability, 1)

    def test_partial_operation_freedom_has_only_discrete_full_freedom_endpoint(self):
        for state_count in range(3, 40):
            self.assertLess(
                genesis_partial_safe_probability(state_count, 0),
                1,
            )
            self.assertEqual(
                genesis_partial_safe_probability(
                    state_count, state_count - 1
                ),
                Fraction(1, 1),
            )
            valley = genesis_partial_operation_valley_horizon(
                state_count
            )
            self.assertGreater(valley, 0)
            self.assertLess(valley, state_count - 1)

    def test_precision_monotonicity_does_not_imply_operation_freedom_monotonicity(self):
        for state_count in range(4, 25):
            trajectory = genesis_operation_trajectory(state_count)
            total_probabilities = tuple(
                stage.total_safe_probability for stage in trajectory
            )
            valley = min(
                range(state_count),
                key=lambda horizon: (
                    total_probabilities[horizon], horizon
                ),
            )
            self.assertTrue(
                all(
                    total_probabilities[index + 1]
                    <= total_probabilities[index]
                    for index in range(valley)
                )
            )
            self.assertTrue(
                all(
                    total_probabilities[index + 1]
                    >= total_probabilities[index]
                    for index in range(valley, state_count - 1)
                )
            )
            self.assertEqual(
                tuple(stage.class_count for stage in trajectory),
                tuple(range(1, state_count + 1)),
            )

    def test_pair_ambiguity_is_exactly_determined_by_tail_size(self):
        from math import comb

        for state_count in range(2, 30):
            for horizon in range(state_count):
                tail = genesis_tail_size(state_count, horizon)
                self.assertEqual(
                    genesis_pair_ambiguity(
                        state_count, horizon
                    ),
                    comb(tail, 2),
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            genesis_predictive_shape(1, 0)
        with self.assertRaises(ValueError):
            genesis_predictive_shape(3, 3)
        with self.assertRaises(ValueError):
            genesis_collision_ambiguity(3, 0, 1)
        with self.assertRaises(TypeError):
            genesis_total_safe_probability(True, 0)
        with self.assertRaises(ValueError):
            genesis_total_operation_valley_horizon(2)


if __name__ == "__main__":
    unittest.main()
