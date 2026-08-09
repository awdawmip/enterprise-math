import unittest

from enterprise_math.causal_basin_periodicity import (
    growth_widths,
    period_capacity,
    periodic_superblock_translations,
    periodic_translation_identity,
    periodic_translation_preserves_basin_detail,
    widths_are_periodic,
)
from enterprise_math.causal_basin_state import linear_growth


class CausalBasinPeriodicityTests(unittest.TestCase):
    def test_constant_width_is_period_one_special_case(self):
        growth = linear_growth(5, 20)
        widths = growth_widths(growth)
        self.assertTrue(widths_are_periodic(widths, 1))
        self.assertEqual(period_capacity(widths, 1), 5)
        total, verified = periodic_translation_identity(growth, 1)
        self.assertEqual(total, 5)
        self.assertTrue(verified)
        for level in range(10):
            for detail in range(5):
                self.assertTrue(
                    periodic_translation_preserves_basin_detail(growth, 1, level, detail)
                )

    def test_nonconstant_period_two_widths_generate_safe_superblock(self):
        # Width pattern 2,3,2,3,... -> complete levels 0,2,5,7,10,...
        growth = [0]
        widths = (2, 3) * 8
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        self.assertTrue(widths_are_periodic(growth_widths(growth), 2))
        total, verified = periodic_translation_identity(growth, 2)
        self.assertEqual(total, 5)
        self.assertTrue(verified)
        for level in range(10):
            for detail in range(growth[level + 1] - growth[level]):
                self.assertTrue(
                    periodic_translation_preserves_basin_detail(growth, 2, level, detail)
                )
        self.assertEqual(
            periodic_superblock_translations(growth_widths(growth), 2, 4),
            (5, 10, 15, 20),
        )

    def test_wrong_period_is_rejected(self):
        widths = (2, 3, 2, 3, 2, 3)
        self.assertFalse(widths_are_periodic(widths, 1))
        with self.assertRaises(ValueError):
            period_capacity(widths, 1)

    def test_periodic_width_can_be_nonconstant_without_being_polynomial_degree_zero_locally(self):
        widths = (1, 4, 2, 1, 4, 2, 1, 4, 2)
        self.assertTrue(widths_are_periodic(widths, 3))
        self.assertEqual(period_capacity(widths, 3), 7)


if __name__ == "__main__":
    unittest.main()
