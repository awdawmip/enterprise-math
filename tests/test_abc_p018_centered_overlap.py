import unittest

from enterprise_math.abc_p018_centered_overlap import (
    centered_height_power_profile,
    centered_overlap_small_radical_state,
)


class CenteredOverlapSmallRadicalTests(unittest.TestCase):
    def test_73_89_overlap_at_threshold_one(self) -> None:
        state = centered_overlap_small_radical_state(73, 89, 1)
        self.assertEqual((state.bridge.center, state.bridge.radius), (81, 8))
        self.assertEqual(state.center_radius_product, 648)
        self.assertEqual(state.product_radical, 6)
        self.assertLessEqual(state.exact_radius_bound_lhs, 8)
        self.assertLess(state.product_square, state.center_cube)
        self.assertLess(1 * 1 * state.product_radical**2, 81)

    def test_503_521_overlap_has_threshold_one_only(self) -> None:
        state = centered_overlap_small_radical_state(503, 521, 1)
        self.assertEqual((state.bridge.center, state.bridge.radius), (512, 9))
        self.assertEqual(state.product_radical, 6)
        self.assertLessEqual(state.product_radical, 9)
        with self.assertRaises(ValueError):
            centered_overlap_small_radical_state(503, 521, 2)

    def test_997_1051_overlap_has_large_projective_gain(self) -> None:
        state = centered_overlap_small_radical_state(997, 1051, 4)
        self.assertEqual((state.bridge.center, state.bridge.radius), (1024, 27))
        self.assertEqual(state.product_radical, 6)
        self.assertLessEqual(4 * 6, 27)

    def test_outside_p018_range_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            centered_overlap_small_radical_state(5, 59, 1)

    def test_formal_power_profile(self) -> None:
        self.assertEqual(
            centered_height_power_profile(),
            {
                "product_height_power": (3, 2),
                "radical_height_power": (1, 2),
            },
        )


if __name__ == "__main__":
    unittest.main()
