import unittest

from enterprise_math.integer_affine_padic_image_spectrum import (
    INFINITE,
    affine_padic_target_height,
    finite_padic_image_spectrum,
    reachable_vs_deep_image_obstruction_indistinguishable_through,
)


class IntegerAffinePadicImageSpectrumTests(unittest.TestCase):
    def test_scalar_target_heights(self):
        self.assertEqual(
            affine_padic_target_height(((4,),), (2,), 2),
            1,
        )
        self.assertEqual(
            affine_padic_target_height(((8,),), (4,), 2),
            2,
        )
        self.assertEqual(
            affine_padic_target_height(((2,),), (1,), 2),
            0,
        )
        self.assertEqual(
            affine_padic_target_height(((2,),), (1,), 3),
            INFINITE,
        )
        self.assertEqual(
            affine_padic_target_height(((2,),), (2,), 2),
            INFINITE,
        )

    def test_free_cokernel_target_has_finite_height_at_each_fixed_prime(self):
        matrix = ((0,),)
        target = (12,)
        self.assertEqual(affine_padic_target_height(matrix, target, 2), 2)
        self.assertEqual(affine_padic_target_height(matrix, target, 3), 1)
        self.assertEqual(affine_padic_target_height(matrix, target, 5), 0)

    def test_finite_ladder_is_true_prefix_then_false_suffix(self):
        spectrum = finite_padic_image_spectrum(
            ((8,),),
            (4,),
            2,
            5,
            resolve_exact_height=True,
        )
        self.assertEqual(
            spectrum.solvable_flags,
            (True, True, False, False, False),
        )
        self.assertEqual(spectrum.first_unsolvable_exponent, 3)
        self.assertEqual(spectrum.observed_height_lower_bound, 2)
        self.assertEqual(spectrum.exact_height, 2)

    def test_no_failure_in_finite_ladder_only_gives_lower_bound_when_exact_not_resolved(self):
        spectrum = finite_padic_image_spectrum(
            ((2,),),
            (1,),
            3,
            6,
            resolve_exact_height=False,
        )
        self.assertTrue(spectrum.no_failure_observed)
        self.assertEqual(spectrum.observed_height_lower_bound, 6)
        self.assertIsNone(spectrum.exact_height)

        resolved = finite_padic_image_spectrum(
            ((2,),),
            (1,),
            3,
            6,
            resolve_exact_height=True,
        )
        self.assertEqual(resolved.exact_height, INFINITE)

    def test_reachable_and_deep_image_obstructed_targets_match_through_declared_depth(self):
        for prime in (2, 3, 5):
            for depth in range(1, 6):
                for observed in range(1, depth + 1):
                    self.assertTrue(
                        reachable_vs_deep_image_obstruction_indistinguishable_through(
                            prime,
                            depth,
                            observed,
                        )
                    )
                self.assertFalse(
                    reachable_vs_deep_image_obstruction_indistinguishable_through(
                        prime,
                        depth,
                        depth + 1,
                    )
                )

    def test_deep_image_pair_splits_exactly_at_next_prime_power_level(self):
        prime = 2
        depth = 4
        coefficient = prime ** (depth + 1)
        good = coefficient
        bad = coefficient + prime ** depth
        good_spectrum = finite_padic_image_spectrum(
            ((coefficient,),),
            (good,),
            prime,
            depth + 1,
        )
        bad_spectrum = finite_padic_image_spectrum(
            ((coefficient,),),
            (bad,),
            prime,
            depth + 1,
        )
        self.assertEqual(good_spectrum.solvable_flags, (True,) * (depth + 1))
        self.assertEqual(
            bad_spectrum.solvable_flags,
            (True,) * depth + (False,),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_padic_image_spectrum(((1,),), (0,), 2, 0)
        with self.assertRaises(TypeError):
            finite_padic_image_spectrum(((1,),), (0,), 2, False)
        with self.assertRaises(ValueError):
            reachable_vs_deep_image_obstruction_indistinguishable_through(4, 1, 1)


if __name__ == "__main__":
    unittest.main()
