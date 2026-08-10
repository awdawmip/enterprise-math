import itertools
import unittest

from enterprise_math.material_contact_lifted_reservoir import (
    lifted_contact_reservoir_state,
)
from enterprise_math.material_contact_predictive_reservoir import (
    all_truncated_remainder_signatures,
    apply_named_unit_action_to_lifted_state,
    apply_named_unit_action_to_predictive_state,
    apply_named_word_to_lifted_state,
    apply_named_word_to_predictive_state,
    fixed_body_horizon_remainder_class_count,
    one_contact_horizon_remainder_class_count,
    predictive_contact_reservoir_state,
    predictive_projection_commutes_with_named_word,
    shortest_named_remainder_separator,
    truncated_carry_signature,
)


PATH_B = (
    (-1, 0),
    (1, -1),
    (0, 1),
)

TRIANGLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)


def words(contact_count, maximum_length):
    result = [()]
    for length in range(1, maximum_length + 1):
        result.extend(
            itertools.product(range(contact_count), repeat=length)
        )
    return tuple(result)


class MaterialContactPredictiveReservoirTests(unittest.TestCase):
    def test_one_step_projection_descends_exactly(self):
        for graph in (PATH_B, TRIANGLE_B):
            contact_count = len(graph[0])
            for amplitude in (1, 2, 5):
                for raw in itertools.product(
                    range(0, 9),
                    repeat=contact_count,
                ):
                    lifted = lifted_contact_reservoir_state(
                        graph,
                        raw,
                        amplitude,
                    )
                    predictive = predictive_contact_reservoir_state(
                        graph,
                        raw,
                        amplitude,
                    )
                    for contact in range(contact_count):
                        full_after = apply_named_unit_action_to_lifted_state(
                            graph,
                            lifted,
                            contact,
                        )
                        predictive_after = apply_named_unit_action_to_predictive_state(
                            graph,
                            predictive,
                            contact,
                        )
                        self.assertEqual(
                            predictive_after,
                            predictive_contact_reservoir_state(
                                graph,
                                full_after.raw_numerators,
                                amplitude,
                            ),
                        )

    def test_projection_commutes_with_arbitrary_short_named_words(self):
        examples = (
            (PATH_B, (6, 13), 10),
            (PATH_B, (0, 0), 3),
            (TRIANGLE_B, (6, 0, 0), 10),
            (TRIANGLE_B, (16, 10, 10), 10),
            (TRIANGLE_B, (2, 5, 8), 3),
        )
        for graph, raw, amplitude in examples:
            for word in words(len(graph[0]), 4):
                self.assertTrue(
                    predictive_projection_commutes_with_named_word(
                        graph,
                        raw,
                        amplitude,
                        word,
                    )
                )

    def test_cycle_allocation_is_erased_when_body_and_remainder_match(self):
        amplitude = 10
        left_raw = (6, 0, 0)
        right_raw = (16, 10, 10)

        left_full = lifted_contact_reservoir_state(
            TRIANGLE_B,
            left_raw,
            amplitude,
        )
        right_full = lifted_contact_reservoir_state(
            TRIANGLE_B,
            right_raw,
            amplitude,
        )
        self.assertNotEqual(
            left_full.delivered_impulse_quanta,
            right_full.delivered_impulse_quanta,
        )
        self.assertEqual(left_full.body_delta, right_full.body_delta)
        self.assertEqual(
            left_full.contact_remainders,
            right_full.contact_remainders,
        )

        left_predictive = predictive_contact_reservoir_state(
            TRIANGLE_B,
            left_raw,
            amplitude,
        )
        right_predictive = predictive_contact_reservoir_state(
            TRIANGLE_B,
            right_raw,
            amplitude,
        )
        self.assertEqual(left_predictive, right_predictive)

        for word in words(3, 4):
            left_after = apply_named_word_to_predictive_state(
                TRIANGLE_B,
                left_predictive,
                word,
            )
            right_after = apply_named_word_to_predictive_state(
                TRIANGLE_B,
                right_predictive,
                word,
            )
            self.assertEqual(left_after, right_after)

    def test_different_remainders_same_body_are_future_distinguishable(self):
        amplitude = 10
        left_raw = (6, 0)
        right_raw = (0, 0)
        left = predictive_contact_reservoir_state(
            PATH_B,
            left_raw,
            amplitude,
        )
        right = predictive_contact_reservoir_state(
            PATH_B,
            right_raw,
            amplitude,
        )
        self.assertEqual(left.body_delta, right.body_delta)
        self.assertNotEqual(left.contact_remainders, right.contact_remainders)

        separator = shortest_named_remainder_separator(
            left.contact_remainders,
            right.contact_remainders,
            amplitude,
        )
        self.assertEqual(separator, (0, 0, 0, 0))
        self.assertLessEqual(len(separator), amplitude - 1)

        left_after = apply_named_word_to_predictive_state(
            PATH_B,
            left,
            separator,
        )
        right_after = apply_named_word_to_predictive_state(
            PATH_B,
            right,
            separator,
        )
        self.assertNotEqual(left_after.body_delta, right_after.body_delta)

    def test_shortest_separator_bound_for_every_remainder_pair(self):
        for amplitude in range(2, 13):
            for left in range(amplitude):
                for right in range(amplitude):
                    separator = shortest_named_remainder_separator(
                        (left,),
                        (right,),
                        amplitude,
                    )
                    if left == right:
                        self.assertIsNone(separator)
                    else:
                        self.assertIsNotNone(separator)
                        assert separator is not None
                        self.assertLessEqual(len(separator), amplitude - 1)

    def test_one_contact_horizon_class_count_is_exact(self):
        for amplitude in range(1, 10):
            for horizon in range(0, amplitude + 3):
                signatures = {
                    truncated_carry_signature(
                        (remainder,),
                        amplitude,
                        horizon,
                    )
                    for remainder in range(amplitude)
                }
                self.assertEqual(
                    len(signatures),
                    one_contact_horizon_remainder_class_count(
                        amplitude,
                        horizon,
                    ),
                )
                self.assertEqual(
                    len(signatures),
                    min(amplitude, horizon + 1),
                )

    def test_multi_contact_horizon_class_count_is_exact_product(self):
        for amplitude in (1, 2, 3, 5):
            for contact_count in (1, 2, 3):
                for horizon in range(0, amplitude + 1):
                    signatures = all_truncated_remainder_signatures(
                        contact_count,
                        amplitude,
                        horizon,
                    )
                    self.assertEqual(
                        len(signatures),
                        fixed_body_horizon_remainder_class_count(
                            contact_count,
                            amplitude,
                            horizon,
                        ),
                    )
                    self.assertEqual(
                        len(signatures),
                        min(amplitude, horizon + 1) ** contact_count,
                    )

    def test_horizon_a_minus_one_recovers_exact_remainder_vector(self):
        amplitude = 7
        horizon = amplitude - 1
        signatures = {}
        for remainders in itertools.product(
            range(amplitude),
            repeat=2,
        ):
            signature = truncated_carry_signature(
                remainders,
                amplitude,
                horizon,
            )
            self.assertNotIn(signature, signatures)
            signatures[signature] = remainders
        self.assertEqual(len(signatures), amplitude ** 2)

    def test_exact_future_equivalence_is_body_plus_remainder_not_full_lifted_state(self):
        amplitude = 10
        # Same body + same remainder, different cycle allocation: future-equivalent.
        first = predictive_contact_reservoir_state(
            TRIANGLE_B,
            (6, 0, 0),
            amplitude,
        )
        second = predictive_contact_reservoir_state(
            TRIANGLE_B,
            (16, 10, 10),
            amplitude,
        )
        self.assertEqual(first, second)

        # Same body + different remainder: not future-equivalent.
        third = predictive_contact_reservoir_state(
            TRIANGLE_B,
            (0, 0, 0),
            amplitude,
        )
        self.assertEqual(first.body_delta, third.body_delta)
        self.assertNotEqual(first.contact_remainders, third.contact_remainders)
        self.assertIsNotNone(
            shortest_named_remainder_separator(
                first.contact_remainders,
                third.contact_remainders,
                amplitude,
            )
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            shortest_named_remainder_separator((0,), (0, 1), 10)
        with self.assertRaises(ValueError):
            shortest_named_remainder_separator((10,), (0,), 10)
        with self.assertRaises(ValueError):
            one_contact_horizon_remainder_class_count(0, 1)
        with self.assertRaises(ValueError):
            fixed_body_horizon_remainder_class_count(0, 10, 2)
        with self.assertRaises(ValueError):
            truncated_carry_signature((0,), 10, -1)
        with self.assertRaises(TypeError):
            predictive_contact_reservoir_state(PATH_B, (0, 0), True)


if __name__ == "__main__":
    unittest.main()
