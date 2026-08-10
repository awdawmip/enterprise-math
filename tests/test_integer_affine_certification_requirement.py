import unittest

from enterprise_math.integer_affine_certification_requirement import (
    affine_certification_requirement,
    experiment_profile_satisfies_requirement,
    join_certification_requirements,
    joint_affine_certification_requirement,
    least_joint_finite_all_target_modulus,
)
from enterprise_math.integer_affine_experiment_precision_profile import (
    all_primes_precision_profile,
    finite_family_precision_profile,
    power_ladder_precision_profile,
)


class IntegerAffineCertificationRequirementTests(unittest.TestCase):
    def test_single_task_requirement_matches_free_flag_and_prime_depths(self):
        requirement = affine_certification_requirement(
            (
                (12,),
                (0,),
            )
        )
        self.assertTrue(requirement.free_separation_required)
        self.assertEqual(requirement.prime_depths, ((2, 2), (3, 1)))
        self.assertEqual(requirement.torsion_exponent, 12)

    def test_joint_requirement_is_coordinatewise_max_not_sum(self):
        first = affine_certification_requirement(((4,),))
        second = affine_certification_requirement(((8,),))
        third = affine_certification_requirement(((9,),))
        joined = join_certification_requirements((first, second, third))
        self.assertFalse(joined.free_separation_required)
        self.assertEqual(joined.prime_depths, ((2, 3), (3, 2)))
        self.assertEqual(joined.torsion_exponent, 72)
        self.assertEqual(
            least_joint_finite_all_target_modulus(
                (((4,),), ((8,),), ((9,),))
            ),
            72,
        )

    def test_one_free_task_makes_joint_finite_all_target_certificate_impossible(self):
        matrices = (
            ((4,),),
            ((1,), (0,)),
        )
        requirement = joint_affine_certification_requirement(matrices)
        self.assertTrue(requirement.free_separation_required)
        self.assertEqual(requirement.prime_depths, ((2, 2),))
        self.assertIsNone(least_joint_finite_all_target_modulus(matrices))

    def test_experiment_profile_dominates_requirement_coordinatewise(self):
        requirement = affine_certification_requirement(
            (
                (12,),
                (0,),
            )
        )
        all_primes = all_primes_precision_profile()
        ladder_six = power_ladder_precision_profile(6)
        finite_twelve = finite_family_precision_profile((12,))

        self.assertFalse(experiment_profile_satisfies_requirement(all_primes, requirement))
        self.assertTrue(experiment_profile_satisfies_requirement(ladder_six, requirement))
        # Finite mod12 has enough p-depth but lacks the free-separation resource.
        self.assertFalse(experiment_profile_satisfies_requirement(finite_twelve, requirement))

    def test_full_rank_joint_requirement_is_satisfied_by_lcm_modulus(self):
        matrices = (
            ((4,),),
            ((6,),),
        )
        requirement = joint_affine_certification_requirement(matrices)
        self.assertFalse(requirement.free_separation_required)
        self.assertEqual(requirement.prime_depths, ((2, 2), (3, 1)))
        self.assertEqual(requirement.torsion_exponent, 12)
        profile = finite_family_precision_profile((3, 4))
        self.assertTrue(experiment_profile_satisfies_requirement(profile, requirement))
        self.assertEqual(least_joint_finite_all_target_modulus(matrices), 12)

    def test_validation(self):
        with self.assertRaises(ValueError):
            join_certification_requirements(())
        with self.assertRaises(ValueError):
            joint_affine_certification_requirement(())
        with self.assertRaises(ValueError):
            least_joint_finite_all_target_modulus(())


if __name__ == "__main__":
    unittest.main()
