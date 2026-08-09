import unittest

from enterprise_math.causal_scale_duality import (
    action_language_compatible_with_block,
    coarsest_block_scale_for_actions,
    dual_compatibility_certificate,
    smallest_shared_safe_translation,
    translation_compatible_with_structures,
)


class CausalScaleDualityTests(unittest.TestCase):
    def test_gcd_is_coarsest_block_compatible_with_all_actions(self):
        generators = (12, 18, 30)
        self.assertEqual(coarsest_block_scale_for_actions(generators), 6)
        self.assertTrue(action_language_compatible_with_block(generators, 6))
        self.assertTrue(action_language_compatible_with_block(generators, 3))
        self.assertFalse(action_language_compatible_with_block(generators, 12))

    def test_lcm_is_smallest_shared_safe_translation(self):
        periods = (4, 6, 10)
        self.assertEqual(smallest_shared_safe_translation(periods), 60)
        self.assertTrue(translation_compatible_with_structures(60, periods))
        self.assertTrue(translation_compatible_with_structures(120, periods))
        for translation in range(1, 60):
            self.assertFalse(translation_compatible_with_structures(translation, periods))

    def test_more_future_actions_can_only_refine_gcd_scale(self):
        before = coarsest_block_scale_for_actions((12, 18))
        after = coarsest_block_scale_for_actions((12, 18, 20))
        self.assertEqual((before, after), (6, 2))

    def test_more_structure_constraints_can_only_coarsen_shared_translation(self):
        before = smallest_shared_safe_translation((4, 6))
        after = smallest_shared_safe_translation((4, 6, 10))
        self.assertEqual((before, after), (12, 60))
        self.assertEqual(after % before, 0)

    def test_dual_certificate_keeps_two_causal_questions_separate(self):
        self.assertEqual(
            dual_compatibility_certificate((6, 12, 18), (4, 6)),
            (6, 12),
        )


if __name__ == "__main__":
    unittest.main()
