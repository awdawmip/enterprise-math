import itertools
import unittest

from enterprise_math.integer_observation_fiber_local_global import (
    bounded_state_box_certificate_holds,
    bounded_state_box_certificate_modulus,
    exact_observation_equal,
    fiber_local_global_requirement,
    modular_observation_equal,
    observation_needs_unbounded_precision,
    power_ladder_uniformly_certifies_exact_fiber,
)


class IntegerObservationFiberLocalGlobalTests(unittest.TestCase):
    def test_nonzero_observation_needs_unbounded_free_separation_only(self):
        observation = ((6, 0),)
        requirement = fiber_local_global_requirement(observation)
        self.assertEqual(requirement.observation_rational_rank, 1)
        self.assertTrue(requirement.unbounded_free_separation_required)
        self.assertEqual(requirement.torsion_prime_depths_required, ())
        self.assertTrue(observation_needs_unbounded_precision(observation))
        self.assertTrue(power_ladder_uniformly_certifies_exact_fiber(observation, 2))
        self.assertTrue(power_ladder_uniformly_certifies_exact_fiber(observation, 7))
        self.assertFalse(power_ladder_uniformly_certifies_exact_fiber(observation, 1))

    def test_zero_observation_needs_no_precision_resource(self):
        observation = ((0, 0),)
        requirement = fiber_local_global_requirement(observation)
        self.assertEqual(requirement.observation_rational_rank, 0)
        self.assertFalse(requirement.unbounded_free_separation_required)
        self.assertTrue(power_ladder_uniformly_certifies_exact_fiber(observation, 1))

    def test_bounded_state_box_modulus_is_strictly_above_output_difference_bound(self):
        observation = (
            (2, -3),
            (1, 1),
        )
        bound = 4
        # max row L1=5; output-difference bound=2*4*5=40.
        self.assertEqual(bounded_state_box_certificate_modulus(observation, bound), 41)

    def test_bounded_box_certificate_matches_exact_equality_exhaustively(self):
        observation = (
            (2, -1),
            (0, 3),
        )
        bound = 2
        states = tuple(itertools.product(range(-bound, bound + 1), repeat=2))
        modulus = bounded_state_box_certificate_modulus(observation, bound)
        for left in states:
            for right in states:
                self.assertEqual(
                    exact_observation_equal(observation, left, right),
                    modular_observation_equal(observation, left, right, modulus),
                    (left, right, modulus),
                )
                self.assertEqual(
                    bounded_state_box_certificate_holds(
                        observation,
                        left,
                        right,
                        bound,
                    ),
                    exact_observation_equal(observation, left, right),
                )

    def test_too_coarse_modulus_can_merge_exactly_distinct_bounded_states(self):
        observation = ((1,),)
        left = (0,)
        right = (2,)
        self.assertFalse(exact_observation_equal(observation, left, right))
        self.assertTrue(modular_observation_equal(observation, left, right, 2))
        self.assertEqual(bounded_state_box_certificate_modulus(observation, 2), 5)
        self.assertFalse(modular_observation_equal(observation, left, right, 5))

    def test_validation(self):
        with self.assertRaises(ValueError):
            bounded_state_box_certificate_modulus(((1,),), -1)
        with self.assertRaises(ValueError):
            bounded_state_box_certificate_holds(((1,),), (2,), (0,), 1)
        with self.assertRaises(ValueError):
            modular_observation_equal(((1,),), (0,), (1,), 0)
        with self.assertRaises(TypeError):
            power_ladder_uniformly_certifies_exact_fiber(((1,),), True)


if __name__ == "__main__":
    unittest.main()
