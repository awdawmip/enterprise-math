import math
import unittest

from enterprise_math.local_law_modulus_design import (
    bad_moduli_for_codebooks,
    codebook_cardinality_lower_bound,
    codebook_difference_spectrum,
    codebook_width_upper_bound,
    first_reflective_padic_exponent,
    first_reflective_padic_exponent_for_single_primitive,
    incomparable_reflective_prime_witnesses,
    joint_modulus,
    least_numeric_reflective_modulus,
    modular_sensor_family_reflects,
    modulus_reflects_codebooks,
    padic_reflection_matches_depth,
    reflective_moduli_upward_closed_sample,
    scaling_by_unit_preserves_reflection,
    single_primitive_capacity,
    single_primitive_reflects,
)


class LocalLawModulusDesignTests(unittest.TestCase):
    def test_difference_divisor_criterion(self):
        codebooks = {"c": frozenset({0, 2, 4})}
        self.assertEqual(codebook_difference_spectrum(codebooks["c"]), frozenset({2, 4}))
        self.assertEqual(bad_moduli_for_codebooks(codebooks), frozenset({2, 4}))
        self.assertFalse(modulus_reflects_codebooks(codebooks, 2))
        self.assertTrue(modulus_reflects_codebooks(codebooks, 3))
        self.assertFalse(modulus_reflects_codebooks(codebooks, 4))
        self.assertTrue(modulus_reflects_codebooks(codebooks, 5))
        self.assertEqual(least_numeric_reflective_modulus(codebooks), 3)

    def test_context_removes_cross_coordinate_bad_modulus(self):
        contextual = {
            "a": frozenset({0, 1}),
            "b": frozenset({0, 4}),
        }
        global_codebook = {"global": frozenset({0, 1, 4})}
        self.assertTrue(modulus_reflects_codebooks(contextual, 3))
        self.assertFalse(modulus_reflects_codebooks(global_codebook, 3))
        self.assertEqual(least_numeric_reflective_modulus(contextual), 3)
        self.assertEqual(least_numeric_reflective_modulus(global_codebook), 5)

    def test_cardinality_and_width_bounds_bracket_numeric_optimum(self):
        codebooks = {"c": frozenset({0, 2, 5})}
        lower = codebook_cardinality_lower_bound(codebooks)
        upper = codebook_width_upper_bound(codebooks)
        minimum = least_numeric_reflective_modulus(codebooks)
        self.assertEqual(lower, 3)
        self.assertEqual(upper, 6)
        self.assertEqual(minimum, 4)
        self.assertLessEqual(lower, minimum)
        self.assertLessEqual(minimum, upper)

    def test_reflective_moduli_are_upward_closed_but_have_no_divisibility_least(self):
        codebooks = {"c": frozenset({0, 6})}
        self.assertTrue(reflective_moduli_upward_closed_sample(codebooks, 100))
        left, right = incomparable_reflective_prime_witnesses(codebooks)
        self.assertNotEqual(left, right)
        self.assertTrue(modulus_reflects_codebooks(codebooks, left))
        self.assertTrue(modulus_reflects_codebooks(codebooks, right))
        self.assertEqual(math.gcd(left, right), 1)

        # Meet closure can fail even among composite reflective moduli.
        self.assertTrue(modulus_reflects_codebooks(codebooks, 4))
        self.assertTrue(modulus_reflects_codebooks(codebooks, 10))
        self.assertFalse(modulus_reflects_codebooks(codebooks, math.gcd(4, 10)))

    def test_padic_first_reflective_depth_is_max_difference_valuation_plus_one(self):
        codebooks = {"c": frozenset({0, 2, 4})}
        self.assertEqual(first_reflective_padic_exponent(codebooks, 2), 3)
        self.assertFalse(padic_reflection_matches_depth(codebooks, 2, 1))
        self.assertFalse(padic_reflection_matches_depth(codebooks, 2, 2))
        self.assertTrue(padic_reflection_matches_depth(codebooks, 2, 3))

        self.assertEqual(first_reflective_padic_exponent(codebooks, 3), 1)
        self.assertTrue(padic_reflection_matches_depth(codebooks, 3, 1))

    def test_single_primitive_capacity_closed_form(self):
        self.assertEqual(single_primitive_capacity(2, 3), 2)
        self.assertTrue(single_primitive_reflects(2, 2, 3))
        self.assertFalse(single_primitive_reflects(2, 3, 3))

        self.assertEqual(single_primitive_capacity(2, 4), 1)
        self.assertFalse(single_primitive_reflects(2, 2, 4))

        self.assertEqual(single_primitive_capacity(2, 5), 4)
        self.assertTrue(single_primitive_reflects(2, 3, 5))

    def test_single_primitive_padic_depth_formula(self):
        # 12 has v_2=2.  To distinguish 0,w,2w,3w needs quotient order >3,
        # so p-adic depth is 2 + 2 = 4: modulus 16.
        self.assertEqual(
            first_reflective_padic_exponent_for_single_primitive(12, 3, 2),
            4,
        )
        self.assertFalse(single_primitive_reflects(12, 3, 8))
        self.assertTrue(single_primitive_reflects(12, 3, 16))

        # Along the 3-adic ladder v_3(12)=1 and d=2 needs one extra base-3
        # digit: modulus 9.
        self.assertEqual(
            first_reflective_padic_exponent_for_single_primitive(12, 2, 3),
            2,
        )
        self.assertTrue(single_primitive_reflects(12, 2, 9))

    def test_unit_scaling_preserves_reflection(self):
        values = frozenset({0, 1, 2})
        self.assertTrue(scaling_by_unit_preserves_reflection(values, 5, 3))
        with self.assertRaises(ValueError):
            scaling_by_unit_preserves_reflection(values, 3, 3)

    def test_crt_sensor_family_depends_only_on_lcm_and_can_have_synergy(self):
        codebooks = {"c": frozenset({0, 1, 4})}
        self.assertFalse(modulus_reflects_codebooks(codebooks, 2))
        self.assertFalse(modulus_reflects_codebooks(codebooks, 3))
        self.assertEqual(joint_modulus((2, 3)), 6)
        self.assertTrue(modular_sensor_family_reflects(codebooks, (2, 3)))
        self.assertTrue(modulus_reflects_codebooks(codebooks, 6))

        # Redundant non-coprime sensors have the same effective code as lcm.
        self.assertEqual(joint_modulus((4, 6)), 12)
        self.assertEqual(
            modular_sensor_family_reflects(codebooks, (4, 6)),
            modulus_reflects_codebooks(codebooks, 12),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            modulus_reflects_codebooks({}, 3)
        with self.assertRaises(ValueError):
            single_primitive_capacity(0, 3)
        with self.assertRaises(ValueError):
            first_reflective_padic_exponent({"c": {0, 1}}, 4)
        with self.assertRaises(ValueError):
            joint_modulus(())


if __name__ == "__main__":
    unittest.main()
