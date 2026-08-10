import unittest
from fractions import Fraction

from enterprise_math.abc_activation_area_operation_family import (
    future_area_for_family_action,
    operation_family_area_signature,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class ActivationAreaOperationFamilyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.current = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1),
                Fraction(11),
            ),
        )
        self.candidates = (
            Fraction(1, 10),
            Fraction(3, 5),
            Fraction(5),
            Fraction(20),
        )

    def test_ordered_threshold_actions_form_response_staircase(self) -> None:
        signature = operation_family_area_signature(self.current, self.candidates)
        self.assertEqual(signature.current_area, 9)
        self.assertEqual(signature.threshold_crossing_depths, (1, 2, 2, None))
        self.assertEqual(signature.threshold_area_increments, (3, 2, 2, 0))
        self.assertEqual(signature.threshold_future_areas, (12, 11, 11, 9))
        self.assertTrue(signature.crossing_staircase_verified)
        self.assertTrue(signature.future_reconstruction_verified)

    def test_family_signature_predicts_every_declared_one_step_area(self) -> None:
        signature = operation_family_area_signature(self.current, self.candidates)
        for index, expected in enumerate((12, 11, 11, 9)):
            self.assertEqual(
                future_area_for_family_action(signature, "threshold", index),
                expected,
            )
        self.assertEqual(
            future_area_for_family_action(signature, "orbit"),
            signature.orbit_future_area,
        )
        self.assertEqual(
            signature.orbit_future_area,
            signature.current_area + signature.orbit_new_rank,
        )

    def test_threshold_response_space_is_compressed_by_order(self) -> None:
        signature = operation_family_area_signature(self.current, self.candidates)
        # h=3 and a=4: weakly increasing depth vectors from 5 ordered states.
        self.assertEqual(signature.monotone_threshold_response_state_count, 70)
        self.assertEqual(signature.unconstrained_threshold_response_tuple_count, 5**4)
        self.assertLess(
            signature.monotone_threshold_response_state_count,
            signature.unconstrained_threshold_response_tuple_count,
        )

    def test_response_signature_contains_area_staircase_and_orbit_rank(self) -> None:
        signature = operation_family_area_signature(self.current, self.candidates)
        self.assertEqual(
            signature.response_signature,
            (
                9,
                (1, 2, 2, None),
                signature.orbit_new_rank,
            ),
        )

    def test_candidate_thresholds_must_be_ordered_new_actions(self) -> None:
        with self.assertRaises(ValueError):
            operation_family_area_signature(
                self.current,
                (Fraction(3, 5), Fraction(1, 10)),
            )
        with self.assertRaises(ValueError):
            operation_family_area_signature(
                self.current,
                (Fraction(1, 2), Fraction(3, 5)),
            )

    def test_action_lookup_contract(self) -> None:
        signature = operation_family_area_signature(self.current, self.candidates)
        with self.assertRaises(ValueError):
            future_area_for_family_action(signature, "threshold")
        with self.assertRaises(ValueError):
            future_area_for_family_action(signature, "threshold", 99)
        with self.assertRaises(ValueError):
            future_area_for_family_action(signature, "orbit", 0)
        with self.assertRaises(ValueError):
            future_area_for_family_action(signature, "unknown")


if __name__ == "__main__":
    unittest.main()
