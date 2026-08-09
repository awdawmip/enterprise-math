import unittest

from enterprise_math.causal_close_packing_stack import (
    is_close_packed_registry_sequence,
    modes_from_stack,
    next_orientation,
    orientation_sequence,
    stack_from_modes,
)


class CausalClosePackingStackTests(unittest.TestCase):
    def test_repeated_c_generates_fcc_abc_stacking(self):
        stack = stack_from_modes((0, 1), ("c",) * 7)
        self.assertEqual(stack, (0, 1, 2, 0, 1, 2, 0, 1, 2))
        self.assertTrue(is_close_packed_registry_sequence(stack))
        self.assertEqual(modes_from_stack(stack), ("c",) * 7)

    def test_repeated_h_generates_hcp_ab_stacking(self):
        stack = stack_from_modes((0, 1), ("h",) * 7)
        self.assertEqual(stack, (0, 1, 0, 1, 0, 1, 0, 1, 0))
        self.assertTrue(is_close_packed_registry_sequence(stack))
        self.assertEqual(modes_from_stack(stack), ("h",) * 7)

    def test_c_preserves_relative_orientation_and_h_flips_it(self):
        self.assertEqual(next_orientation(1, "c"), 1)
        self.assertEqual(next_orientation(-1, "c"), -1)
        self.assertEqual(next_orientation(1, "h"), -1)
        self.assertEqual(next_orientation(-1, "h"), 1)

    def test_registry_chart_reduces_to_binary_relative_orientation_sequence(self):
        stack = (0, 1, 2, 1, 0, 2)
        self.assertTrue(is_close_packed_registry_sequence(stack))
        orientations = orientation_sequence(stack)
        self.assertTrue(all(value in (-1, 1) for value in orientations))
        self.assertEqual(len(orientations), len(stack) - 1)
        # The h/c word is recovered only from whether consecutive relative
        # orientations agree or flip; absolute A/B/C labels are not required.
        modes = modes_from_stack(stack)
        for before, after, mode in zip(orientations, orientations[1:], modes):
            self.assertEqual(after, next_orientation(before, mode))

    def test_arbitrary_hc_word_remains_close_packed(self):
        for modes in (
            ("c", "h", "c", "h", "h", "c"),
            ("h", "c", "c", "h", "c", "c"),
        ):
            stack = stack_from_modes((0, 1), modes)
            self.assertTrue(is_close_packed_registry_sequence(stack))
            self.assertEqual(modes_from_stack(stack), modes)


if __name__ == "__main__":
    unittest.main()
