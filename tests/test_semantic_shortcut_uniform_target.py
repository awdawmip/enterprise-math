import unittest

from enterprise_math.semantic_shortcut_uniform_target import (
    minimum_uniform_one_round_catalogue_size,
    target_specific_catalogue_size,
    target_specific_shortcut_catalogue,
    uniform_catalogue_is_strictly_larger_for_full_target,
)


class SemanticShortcutUniformTargetTests(unittest.TestCase):
    def test_uniform_minimum_matches_all_small_support_masks(self):
        self.assertEqual(minimum_uniform_one_round_catalogue_size(8, 1), 8)
        self.assertEqual(minimum_uniform_one_round_catalogue_size(8, 2), 36)
        self.assertEqual(minimum_uniform_one_round_catalogue_size(8, 4), 162)

    def test_full_target_specific_catalogue_is_only_chunk_count(self):
        target = (1 << 20) - 1
        catalogue = target_specific_shortcut_catalogue(target, 20, 3)
        self.assertEqual(len(catalogue), 7)
        self.assertTrue(all(mask.bit_count() <= 3 for mask in catalogue))
        combined = 0
        for mask in catalogue:
            combined |= mask
        self.assertEqual(combined, target)

    def test_uniform_vs_target_specific_gap_can_be_large(self):
        target = (1 << 20) - 1
        self.assertEqual(target_specific_catalogue_size(target, 20, 3), 7)
        self.assertEqual(minimum_uniform_one_round_catalogue_size(20, 3), 1350)
        self.assertTrue(uniform_catalogue_is_strictly_larger_for_full_target(20, 3))

    def test_depth_one_uniform_and_full_target_storage_coincide_only_for_one_generator(self):
        self.assertFalse(uniform_catalogue_is_strictly_larger_for_full_target(1, 1))
        self.assertTrue(uniform_catalogue_is_strictly_larger_for_full_target(4, 1))


if __name__ == "__main__":
    unittest.main()
