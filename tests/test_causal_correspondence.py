import unittest

from enterprise_math.causal_correspondence import (
    coarse_middle_shadow,
    composite_multiplicity_from_witnesses,
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
        # y0 contributes 2*1, y1 contributes 1*2.
        self.assertEqual(exact, {("x", "z"): 4})
        self.assertEqual(shadow, exact)

    def test_coarse_middle_can_create_false_cross_pairings(self):
        # x0 can reach only y0, and y1 can reach only z1.  There is no exact
        # two-step x0->z1 witness because y0 != y1.
        left = {"r": ("x0", "y0")}
        right = {"s": ("y1", "z1")}
        exact = composite_multiplicity_from_witnesses(left, right)
        self.assertEqual(exact, {})

        middle_to_coarse = {"y0": "Y", "y1": "Y"}
        coarse_left = coarse_middle_shadow(
            witness_multiplicity(left), middle_to_coarse, middle_is_target=True
        )
        coarse_right = coarse_middle_shadow(
            witness_multiplicity(right), middle_to_coarse, middle_is_target=False
        )
        false_shadow = matrix_shadow_composition(coarse_left, coarse_right)
        self.assertEqual(false_shadow, {("x0", "z1"): 1})

    def test_future_safe_middle_collapse_does_not_change_continuation_profile(self):
        # y0 and y1 can be safely merged here because they have identical
        # continuation profiles to z0,z1.
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
        coarse_right = coarse_middle_shadow(
            witness_multiplicity(right), middle_to_coarse, middle_is_target=False
        )
        # Naively multiplying aggregated counts still overcounts by the fiber
        # size (2): aggregation is not a normalization.  This is intentional and
        # shows that anonymous matrix entries need a proved composition rule,
        # not merely equal profiles.
        self.assertEqual(
            matrix_shadow_composition(coarse_left, coarse_right),
            {("x", "z0"): 4, ("x", "z1"): 4},
        )


if __name__ == "__main__":
    unittest.main()
