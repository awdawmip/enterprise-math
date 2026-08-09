import unittest

from enterprise_math.causal_basin_state import linear_growth, square_growth
from enterprise_math.causal_safe_translations import (
    linear_safe_translation,
    periodic_detail_preserving_translation,
    safe_set_closed_under_addition,
    safe_translations_on_sample,
    translation_is_safe_on_levels,
)


class CausalSafeTranslationsTests(unittest.TestCase):
    def test_linear_growth_safe_monoid_is_block_multiples(self):
        d = 5
        growth = linear_growth(d, 80)
        levels = tuple(range(30))
        for translation in range(31):
            self.assertEqual(
                translation_is_safe_on_levels(growth, translation, levels),
                linear_safe_translation(d, translation),
            )
        safe = safe_translations_on_sample(growth, 30, levels)
        self.assertEqual(safe, (0, 5, 10, 15, 20, 25, 30))
        self.assertTrue(safe_set_closed_under_addition(growth, safe, levels))

    def test_square_growth_has_no_positive_small_safe_translation_on_deep_sample(self):
        growth = square_growth(120)
        levels = tuple(range(1, 60))
        safe = safe_translations_on_sample(growth, 20, levels)
        self.assertEqual(safe, (0,))

    def test_nonconstant_period_two_widths_have_detail_preserving_superblock_translation(self):
        widths = (2, 3) * 20
        growth = [0]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        total, verdict = periodic_detail_preserving_translation(growth, 2)
        self.assertEqual(total, 5)
        self.assertTrue(verdict)
        levels = tuple(range(20))
        for multiplier in range(1, 5):
            self.assertTrue(
                translation_is_safe_on_levels(growth, multiplier * total, levels)
            )

    def test_nonperiodic_widths_fail_detail_preserving_period_test(self):
        widths = (2, 3, 2, 4, 2, 3, 2, 4, 2)
        growth = [0]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        _, verdict = periodic_detail_preserving_translation(growth, 2)
        self.assertFalse(verdict)

    def test_periodic_iff_constant_period_shift_on_represented_growth(self):
        widths = (1, 4, 2) * 6
        growth = [7]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        total, verdict = periodic_detail_preserving_translation(growth, 3)
        self.assertTrue(verdict)
        self.assertEqual(total, 7)
        self.assertTrue(
            all(
                growth[index + 3] - growth[index] == 7
                for index in range(len(growth) - 3)
            )
        )


if __name__ == "__main__":
    unittest.main()
