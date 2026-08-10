import unittest

from enterprise_math.integer_observation_profinite_fiber import (
    apply_observation,
    finite_modular_family_fiber_false_positive,
    observation_kernel_is_profinite_closed,
    observation_kernel_is_profinite_open,
    observation_kernel_is_saturated,
    profinite_fiber_precision_report,
)


class IntegerObservationProfiniteFiberTests(unittest.TestCase):
    def test_nonzero_observation_has_closed_nonopen_exact_kernel(self):
        observation = ((2, 0),)
        report = profinite_fiber_precision_report(observation)
        self.assertTrue(report.saturated_kernel)
        self.assertTrue(report.profinitely_closed)
        self.assertFalse(report.profinitely_open)
        self.assertEqual(report.observation_rational_rank, 1)
        self.assertEqual(report.exact_hidden_free_rank, 1)
        self.assertTrue(observation_kernel_is_saturated(observation))
        self.assertTrue(observation_kernel_is_profinite_closed(observation))
        self.assertFalse(observation_kernel_is_profinite_open(observation))

    def test_zero_observation_kernel_is_whole_state_space_and_open(self):
        observation = (
            (0, 0),
            (0, 0),
        )
        report = profinite_fiber_precision_report(observation)
        self.assertTrue(report.profinitely_open)
        self.assertEqual(report.observation_rational_rank, 0)
        self.assertEqual(report.exact_hidden_free_rank, 2)
        with self.assertRaises(ValueError):
            finite_modular_family_fiber_false_positive(observation, (2, 3))

    def test_every_finite_modular_family_has_exact_state_equality_false_positive(self):
        observations = (
            ((1,),),
            ((2,),),
            ((1, 0),),
            ((2, 4), (0, 6)),
        )
        families = (
            (2,),
            (4, 6),
            (3, 5, 8),
        )
        for observation in observations:
            for family in families:
                witness = finite_modular_family_fiber_false_positive(
                    observation,
                    family,
                )
                self.assertTrue(witness.exact_outputs_differ)
                for modulus in family:
                    self.assertTrue(all(
                        (left - right) % modulus == 0
                        for left, right in zip(
                            witness.left_exact_output,
                            witness.right_exact_output,
                            strict=True,
                        )
                    ))

    def test_identity_observation_witness_is_lcm_state_difference(self):
        observation = (
            (1, 0),
            (0, 1),
        )
        witness = finite_modular_family_fiber_false_positive(
            observation,
            (4, 6),
        )
        self.assertEqual(witness.lcm_ceiling, 12)
        self.assertEqual(witness.witness_coordinate, 0)
        self.assertEqual(witness.left_state, (0, 0))
        self.assertEqual(witness.right_state, (12, 0))
        self.assertEqual(witness.left_exact_output, (0, 0))
        self.assertEqual(witness.right_exact_output, (12, 0))

    def test_nonunimodular_observation_coordinate_torsion_does_not_make_kernel_open(self):
        observation = ((6,),)
        report = profinite_fiber_precision_report(observation)
        self.assertEqual(report.observation_rational_rank, 1)
        self.assertEqual(report.exact_hidden_free_rank, 0)
        self.assertFalse(report.profinitely_open)
        witness = finite_modular_family_fiber_false_positive(observation, (2, 3))
        self.assertEqual(witness.right_state, (6,))
        self.assertEqual(apply_observation(observation, witness.right_state), (36,))
        self.assertTrue(witness.exact_outputs_differ)

    def test_validation(self):
        with self.assertRaises(ValueError):
            profinite_fiber_precision_report(())
        with self.assertRaises(ValueError):
            apply_observation(((1, 0),), (1,))
        with self.assertRaises(ValueError):
            finite_modular_family_fiber_false_positive(((1,),), ())
        with self.assertRaises(ValueError):
            finite_modular_family_fiber_false_positive(((1,),), (0,))


if __name__ == "__main__":
    unittest.main()
