import unittest

from enterprise_math.integer_affine_experiment_precision_profile import (
    INFINITE_DEPTH,
    all_primes_precision_profile,
    experiment_precision_completeness_report,
    experiment_profile_uniformly_complete,
    finite_family_precision_profile,
    power_ladder_precision_profile,
)


class IntegerAffineExperimentPrecisionProfileTests(unittest.TestCase):
    def test_finite_family_needs_full_row_rank_and_lcm_torsion_depth(self):
        full_rank = (
            (2, 0),
            (0, 6),
        )
        rank_deficient = (
            (2,),
            (0,),
        )

        complete_family = finite_family_precision_profile((2, 3))
        self.assertTrue(experiment_profile_uniformly_complete(full_rank, complete_family))
        self.assertFalse(experiment_profile_uniformly_complete(rank_deficient, complete_family))

        too_shallow = finite_family_precision_profile((2,))
        self.assertFalse(experiment_profile_uniformly_complete(full_rank, too_shallow))

    def test_all_primes_is_complete_exactly_at_squarefree_torsion_depth(self):
        profile = all_primes_precision_profile()
        self.assertTrue(profile.free_integer_separating)
        self.assertEqual(profile.depth_at(2), 1)
        self.assertEqual(profile.depth_at(101), 1)

        self.assertTrue(experiment_profile_uniformly_complete(((6,),), profile))
        self.assertFalse(experiment_profile_uniformly_complete(((12,),), profile))

        # Free cokernel is also separated because the family contains infinitely
        # many distinct prime divisors in its supernatural lcm.
        self.assertTrue(
            experiment_profile_uniformly_complete(
                ((1,), (0,)),
                profile,
            )
        )

    def test_power_ladder_gives_infinite_depth_only_on_base_prime_support(self):
        profile = power_ladder_precision_profile(6)
        self.assertTrue(profile.free_integer_separating)
        self.assertEqual(profile.depth_at(2), INFINITE_DEPTH)
        self.assertEqual(profile.depth_at(3), INFINITE_DEPTH)
        self.assertEqual(profile.depth_at(5), 0)

        self.assertTrue(experiment_profile_uniformly_complete(((12,),), profile))
        self.assertTrue(
            experiment_profile_uniformly_complete(
                ((12,), (0,)),
                profile,
            )
        )

        missing_three = power_ladder_precision_profile(2)
        self.assertFalse(experiment_profile_uniformly_complete(((12,),), missing_three))

    def test_torsion_free_free_cokernel_requires_only_free_separation_resource(self):
        matrix = (
            (1,),
            (0,),
        )
        finite = finite_family_precision_profile((2, 3, 5, 7))
        primes = all_primes_precision_profile()
        binary_ladder = power_ladder_precision_profile(2)
        self.assertFalse(experiment_profile_uniformly_complete(matrix, finite))
        self.assertTrue(experiment_profile_uniformly_complete(matrix, primes))
        self.assertTrue(experiment_profile_uniformly_complete(matrix, binary_ladder))

    def test_report_exposes_exact_resource_deficit(self):
        matrix = (
            (12,),
            (0,),
        )
        profile = all_primes_precision_profile()
        report = experiment_precision_completeness_report(matrix, profile)
        self.assertEqual(report.free_cokernel_rank, 1)
        self.assertEqual(report.torsion_exponent, 12)
        self.assertEqual(report.required_prime_depths, ((2, 2), (3, 1)))
        self.assertFalse(report.complete)
        # Free resource is present; the sole deficit is p=2 depth 1 versus 2.
        self.assertTrue(report.profile.free_integer_separating)
        self.assertEqual(report.profile.depth_at(2), 1)

    def test_surjective_map_is_complete_under_even_trivial_finite_profile(self):
        matrix = (
            (1, 0),
            (0, 1),
        )
        profile = finite_family_precision_profile((1,))
        self.assertTrue(experiment_profile_uniformly_complete(matrix, profile))

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_family_precision_profile(())
        with self.assertRaises(ValueError):
            finite_family_precision_profile((0,))
        with self.assertRaises(TypeError):
            finite_family_precision_profile((True,))
        with self.assertRaises(ValueError):
            power_ladder_precision_profile(0)
        with self.assertRaises(TypeError):
            power_ladder_precision_profile(True)


if __name__ == "__main__":
    unittest.main()
