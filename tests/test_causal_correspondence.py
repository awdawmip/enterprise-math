import unittest

from enterprise_math.causal_correspondence import (
    coarse_middle_shadow,
    composite_multiplicity_from_witnesses,
    induced_continuation_profile,
    matrix_shadow_composition,
    witness_multiplicity,
)


class CausalCorrespondenceTests(unittest.TestCase):
    def test_exact_middle_witness_count_equals_matrix_shadow_composition(self):
        left = {
            "r0": ("x", "y0"),
            "r1": ("x", "y0"),
            "r2": ("x", "y1"),
        }
        right = {
            "s0": ("y0", "z"),
            "s1": ("y1", "z"),
            "s2": ("y1", "z"),
        }
        exact = composite_multiplicity_from_witnesses(left, right)
        shadow = matrix_shadow_composition(
            witness_multiplicity(left),
            witness_multiplicity(right),
        )
        self.assertEqual(exact, {("x", "z"): 4})
        self.assertEqual(shadow, exact)

    def test_coarse_middle_can_create_false_cross_pairings(self):
        left = {"r": ("x0", "y0")}
        right = {"s": ("y1", "z1")}
        self.assertEqual(composite_multiplicity_from_witnesses(left, right), {})

        middle_to_coarse = {"y0": "Y", "y1": "Y"}
        coarse_left = coarse_middle_shadow(
            witness_multiplicity(left), middle_to_coarse, middle_is_target=True
        )
        coarse_right = coarse_middle_shadow(
            witness_multiplicity(right), middle_to_coarse, middle_is_target=False
        )
        self.assertEqual(
            matrix_shadow_composition(coarse_left, coarse_right),
            {("x0", "z1"): 1},
        )
        with self.assertRaises(ValueError):
            induced_continuation_profile(witness_multiplicity(right), middle_to_coarse)

    def test_future_safe_middle_uses_one_induced_profile_not_summed_profiles(self):
        left = {
            "r0": ("x", "y0"),
            "r1": ("x", "y1"),
        }
        right = {
            "s00": ("y0", "z0"),
            "s01": ("y0", "z1"),
            "s10": ("y1", "z0"),
            "s11": ("y1", "z1"),
        }
        exact = composite_multiplicity_from_witnesses(left, right)
        self.assertEqual(exact, {("x", "z0"): 2, ("x", "z1"): 2})

        middle_to_coarse = {"y0": "Y", "y1": "Y"}
        coarse_left = coarse_middle_shadow(
            witness_multiplicity(left), middle_to_coarse, middle_is_target=True
        )
        induced_right = induced_continuation_profile(
            witness_multiplicity(right), middle_to_coarse
        )
        self.assertEqual(induced_right, {("Y", "z0"): 1, ("Y", "z1"): 1})
        self.assertEqual(
            matrix_shadow_composition(coarse_left, induced_right),
            exact,
        )

    def test_blindly_summing_both_sides_double_counts_safe_fiber(self):
        left = {
            "r0": ("x", "y0"),
            "r1": ("x", "y1"),
        }
        right = {
            "s00": ("y0", "z0"),
            "s10": ("y1", "z0"),
        }
        middle_to_coarse = {"y0": "Y", "y1": "Y"}
        coarse_left = coarse_middle_shadow(
            witness_multiplicity(left), middle_to_coarse, middle_is_target=True
        )
        blindly_summed_right = coarse_middle_shadow(
            witness_multiplicity(right), middle_to_coarse, middle_is_target=False
        )
        self.assertEqual(
            matrix_shadow_composition(coarse_left, blindly_summed_right),
            {("x", "z0"): 4},
        )
        self.assertEqual(
            composite_multiplicity_from_witnesses(left, right),
            {("x", "z0"): 2},
        )


if __name__ == "__main__":
    unittest.main()
