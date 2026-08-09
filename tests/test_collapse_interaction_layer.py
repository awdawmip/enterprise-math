import unittest

from enterprise_math.collapse_interaction_layer import (
    collapse_interaction_layer,
    collapse_layer_depth,
    refinement_layer_depth,
)


class CollapseInteractionLayerTests(unittest.TestCase):
    def test_factor_generates_exact_positive_gap_layer_thickness(self):
        for factor in range(1, 20):
            layer = collapse_interaction_layer(factor)
            self.assertEqual(layer.thickness_states, factor - 1)
            self.assertEqual(layer.primitive_gaps, tuple(range(1, factor)))
            self.assertEqual(
                set(layer.depths),
                set(range(1, factor)),
            )

    def test_gap_to_depth_is_exact_bijection(self):
        factor = 7
        self.assertEqual(
            tuple(collapse_layer_depth(gap, factor) for gap in range(1, factor)),
            (6, 5, 4, 3, 2, 1),
        )

    def test_primitive_contact_is_not_misclassified_as_coarse_gap_depth(self):
        for factor in range(1, 10):
            self.assertIsNone(collapse_layer_depth(0, factor))

    def test_resolved_positive_gap_is_outside_layer(self):
        factor = 5
        for gap in range(factor, factor + 5):
            self.assertIsNone(collapse_layer_depth(gap, factor))

    def test_refinement_monotonically_reduces_depth_until_extinction(self):
        gap = 3
        depths = [
            collapse_layer_depth(gap, factor)
            for factor in range(8, 0, -1)
        ]
        self.assertEqual(depths, (5, 4, 3, 2, 1, None, None, None))
        self.assertEqual(refinement_layer_depth(gap, 8, 4), (5, 1))
        self.assertEqual(refinement_layer_depth(gap, 8, 3), (5, None))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            collapse_interaction_layer(0)
        with self.assertRaises(ValueError):
            collapse_layer_depth(-1, 3)
        with self.assertRaises(ValueError):
            refinement_layer_depth(1, 2, 3)


if __name__ == "__main__":
    unittest.main()
