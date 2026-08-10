import unittest

from enterprise_math.p017_directional_root_factor_precision import (
    factor_given_root_repair_factor,
    factor_root_images,
    root_factor_directed_depths,
    root_factor_labels,
    root_given_factor_repair_factor,
)


class P017DirectionalRootFactorPrecisionTests(unittest.TestCase):
    def test_factor_to_root_repair_is_globally_binary_on_bounded_range(self) -> None:
        for k in range(2, 300):
            self.assertLessEqual(root_given_factor_repair_factor(k), 2)

    def test_binary_factor_to_root_bound_is_sharp(self) -> None:
        self.assertEqual(root_given_factor_repair_factor(18), 2)
        self.assertEqual(factor_root_images(18)[7], frozenset({6, 7}))

    def test_root_to_factor_direction_can_need_eight_symbols(self) -> None:
        labels = root_factor_labels(1737)[45]
        self.assertEqual(
            labels,
            frozenset({1429, 1439, 1447, 1451, 1459, 1471, 1481, 1489}),
        )
        self.assertEqual(factor_given_root_repair_factor(1737), 8)

    def test_directional_binary_depths_are_one_versus_three_at_k1737(self) -> None:
        data = root_factor_directed_depths(1737, base=2)
        self.assertEqual(data["factor_to_root_factor"], 2)
        self.assertEqual(data["root_to_factor_factor"], 8)
        self.assertEqual(data["factor_to_root_depth"], 1)
        self.assertEqual(data["root_to_factor_depth"], 3)


if __name__ == "__main__":
    unittest.main()
