import itertools
import unittest
from math import lcm

from enterprise_math.integer_future_finite_modular_no_go import (
    finite_modular_free_torsion_models,
    finite_modular_free_torsion_no_go,
)
from enterprise_math.integer_future_modular_precision import (
    modular_observation_signature,
)
from enterprise_math.integer_future_smith_precision import (
    integer_smith_precision_profile,
)


class IntegerFutureFiniteModularNoGoTests(unittest.TestCase):
    def test_any_finite_modulus_family_has_an_exact_deep_torsion_mimic(self):
        families = (
            (2,),
            (2, 4, 8),
            (3, 5, 7),
            (4, 6),
            (6, 10, 15),
            (8, 9, 25),
        )
        for moduli in families:
            report = finite_modular_free_torsion_no_go(moduli)
            expected_depth = 1
            for modulus in moduli:
                expected_depth = lcm(expected_depth, modulus)
            self.assertEqual(report.torsion_depth, expected_depth)
            self.assertEqual(report.free_hidden_rank, 1)
            self.assertEqual(report.finite_hidden_rank, 0)
            self.assertTrue(report.modular_matrices_identical)
            self.assertTrue(report.exact_integer_structures_differ)
            self.assertEqual(
                report.finite_smith_factors,
                (1, expected_depth),
            )

    def test_models_agree_on_every_state_in_bounded_torus_for_each_declared_modulus(self):
        moduli = (4, 6, 9)
        free, finite, depth = finite_modular_free_torsion_models(moduli)
        self.assertEqual(depth, 36)
        for modulus in moduli:
            for state in itertools.product(range(modulus), repeat=2):
                self.assertEqual(
                    modular_observation_signature(free, state, modulus),
                    modular_observation_signature(finite, state, modulus),
                )

    def test_one_precision_level_beyond_torsion_depth_separates_the_models(self):
        # Prime-power specialization: free and finite p^K torsion agree through
        # p^K, but modulus p^(K+1) sees the finite coordinate.
        prime = 2
        depth_exponent = 4
        depth = prime ** depth_exponent
        free, finite, _ = finite_modular_free_torsion_models((depth,))
        state = (0, 1)
        self.assertEqual(
            modular_observation_signature(free, state, depth),
            modular_observation_signature(finite, state, depth),
        )
        finer = prime ** (depth_exponent + 1)
        self.assertNotEqual(
            modular_observation_signature(free, state, finer),
            modular_observation_signature(finite, state, finer),
        )

    def test_exact_smith_profiles_show_free_kernel_vs_finite_torsion(self):
        free, finite, depth = finite_modular_free_torsion_models((4, 6))
        self.assertEqual(depth, 12)
        free_profile = integer_smith_precision_profile(free)
        finite_profile = integer_smith_precision_profile(finite)
        self.assertEqual(free_profile.rational_rank, 1)
        self.assertEqual(free_profile.hidden_free_rank, 1)
        self.assertEqual(free_profile.smith_invariant_factors, (1,))
        self.assertEqual(finite_profile.rational_rank, 2)
        self.assertEqual(finite_profile.hidden_free_rank, 0)
        self.assertEqual(finite_profile.smith_invariant_factors, (1, 12))

    def test_adding_one_new_modulus_not_dividing_current_depth_breaks_the_mimic(self):
        free, finite, depth = finite_modular_free_torsion_models((4, 6))
        self.assertEqual(depth, 12)
        # Mod 5 was not included in the original finite experiment set and does
        # not annihilate 12.
        self.assertNotEqual(
            modular_observation_signature(free, (0, 1), 5),
            modular_observation_signature(finite, (0, 1), 5),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_modular_free_torsion_models(())
        with self.assertRaises(ValueError):
            finite_modular_free_torsion_no_go((0,))
        with self.assertRaises(TypeError):
            finite_modular_free_torsion_no_go((False,))


if __name__ == "__main__":
    unittest.main()
