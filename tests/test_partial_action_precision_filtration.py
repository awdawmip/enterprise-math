import unittest
from math import comb

from enterprise_math.partial_action_precision_filtration import (
    countdown_collision_ambiguity,
    countdown_collision_precision_gain,
    countdown_future_fiber_shape,
    countdown_pair_ambiguity,
    countdown_pair_precision_gain,
    countdown_precision_filtration,
    countdown_total_pair_gain,
)


class PartialActionPrecisionFiltrationTests(unittest.TestCase):
    def test_fiber_shape_is_one_tail_plus_h_singletons(self):
        for maximum_state in range(1, 12):
            for horizon in range(maximum_state + 4):
                capped = min(horizon, maximum_state)
                expected = (
                    maximum_state - capped + 1,
                ) + (1,) * capped
                self.assertEqual(
                    countdown_future_fiber_shape(
                        maximum_state, horizon
                    ),
                    expected,
                )
                self.assertEqual(sum(expected), maximum_state + 1)

    def test_all_higher_collision_ambiguity_lives_in_unresolved_tail(self):
        for maximum_state in range(1, 11):
            for horizon in range(maximum_state + 2):
                capped = min(horizon, maximum_state)
                tail = maximum_state - capped + 1
                for order in range(2, maximum_state + 3):
                    expected = comb(tail, order) if tail >= order else 0
                    self.assertEqual(
                        countdown_collision_ambiguity(
                            maximum_state, horizon, order
                        ),
                        expected,
                    )

    def test_pair_ambiguity_has_closed_binomial_form(self):
        for maximum_state in range(1, 20):
            for horizon in range(maximum_state + 1):
                tail = maximum_state - horizon + 1
                self.assertEqual(
                    countdown_pair_ambiguity(
                        maximum_state, horizon
                    ),
                    comb(tail, 2),
                )

    def test_each_future_step_removes_exactly_n_minus_h_pairs(self):
        for maximum_state in range(1, 20):
            for horizon in range(maximum_state):
                self.assertEqual(
                    countdown_pair_precision_gain(
                        maximum_state, horizon
                    ),
                    maximum_state - horizon,
                )
            self.assertEqual(
                countdown_pair_precision_gain(
                    maximum_state, maximum_state
                ),
                0,
            )

    def test_pair_gains_telescope_to_entire_initial_ambiguity(self):
        for maximum_state in range(1, 30):
            self.assertEqual(
                countdown_total_pair_gain(maximum_state),
                comb(maximum_state + 1, 2),
            )
            self.assertEqual(
                countdown_total_pair_gain(maximum_state),
                countdown_pair_ambiguity(maximum_state, 0),
            )
            self.assertEqual(
                countdown_pair_ambiguity(
                    maximum_state, maximum_state
                ),
                0,
            )

    def test_general_collision_gain_is_lower_order_tail_binomial(self):
        # C(t,k)-C(t-1,k)=C(t-1,k-1).
        for maximum_state in range(2, 14):
            for horizon in range(maximum_state):
                tail_after = maximum_state - horizon
                for order in range(2, maximum_state + 2):
                    expected = (
                        comb(tail_after, order - 1)
                        if tail_after >= order - 1
                        else 0
                    )
                    self.assertEqual(
                        countdown_collision_precision_gain(
                            maximum_state, horizon, order
                        ),
                        expected,
                    )

    def test_filtration_stage_count_increases_one_while_pair_gain_decreases(self):
        for maximum_state in range(2, 15):
            stages = countdown_precision_filtration(maximum_state)
            self.assertEqual(len(stages), maximum_state + 1)
            self.assertEqual(
                tuple(stage.class_count for stage in stages),
                tuple(range(1, maximum_state + 2)),
            )
            self.assertEqual(
                tuple(stage.next_pair_gain for stage in stages),
                tuple(range(maximum_state, -1, -1)),
            )
            self.assertEqual(stages[-1].pair_ambiguity, 0)
            self.assertEqual(
                stages[-1].fiber_shape,
                (1,) * (maximum_state + 1),
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            countdown_future_fiber_shape(0, 0)
        with self.assertRaises(ValueError):
            countdown_future_fiber_shape(3, -1)
        with self.assertRaises(ValueError):
            countdown_collision_ambiguity(3, 0, 1)
        with self.assertRaises(TypeError):
            countdown_collision_ambiguity(3, 0, True)


if __name__ == "__main__":
    unittest.main()
