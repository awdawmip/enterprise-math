import unittest

from enterprise_math.causal_basin_state import linear_growth, square_growth
from enterprise_math.causal_safe_translation_rigidity import (
    certificate_preserves_detail,
    first_tail_period_certificate,
    tail_period_certificate,
    translation_is_safe_from_level,
)


class CausalSafeTranslationRigidityTests(unittest.TestCase):
    def test_constant_width_has_period_one_translation(self):
        growth = linear_growth(5, 30)
        certificate = tail_period_certificate(growth, 0, 1)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.value_translation, 5)
        self.assertTrue(certificate_preserves_detail(growth, certificate))
        self.assertTrue(translation_is_safe_from_level(growth, 5, 0))

    def test_period_two_widths_have_translation_equal_one_cycle_capacity(self):
        widths = (2, 3) * 12
        growth = [0]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        certificate = tail_period_certificate(growth, 0, 2)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.value_translation, 5)
        self.assertTrue(certificate_preserves_detail(growth, certificate))
        self.assertTrue(translation_is_safe_from_level(growth, 5, 0))

    def test_irregular_prefix_can_have_eventually_periodic_safe_tail(self):
        widths = (4, 1, 2) + (2, 3) * 10
        growth = [0]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        certificate = tail_period_certificate(growth, 3, 2)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.value_translation, 5)
        self.assertTrue(certificate_preserves_detail(growth, certificate))
        self.assertTrue(translation_is_safe_from_level(growth, 5, 3))
        # The irregular prefix need not respect the same coarse law globally.
        self.assertFalse(translation_is_safe_from_level(growth, 5, 0))

    def test_square_growth_has_no_small_tail_period_certificate(self):
        growth = square_growth(50)
        self.assertIsNone(first_tail_period_certificate(growth, 10, 8))
        for start in (0, 5, 10):
            self.assertFalse(translation_is_safe_from_level(growth, 5, start))

    def test_discovery_helper_finds_smallest_value_period_on_periodic_sample(self):
        widths = (1, 4, 2) * 8
        growth = [0]
        for width in widths:
            growth.append(growth[-1] + width)
        growth = tuple(growth)
        certificate = first_tail_period_certificate(growth, 2, 6)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.value_translation, 7)
        self.assertEqual(certificate.level_period, 3)


if __name__ == "__main__":
    unittest.main()
