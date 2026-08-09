import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p017_mirror_product_bridge import (
    fixed_product_channel,
    joint_product_root,
)
from enterprise_math.p017_mirror_product_precision import (
    cubic_product_collision_ambiguity,
    moving_state_power_root_collision_kernel,
    residual_cubic_core_product_observation,
)


class P017MirrorProductPrecisionTests(unittest.TestCase):
    def test_general_moving_state_kernel_on_quartic_collision(self):
        data = moving_state_power_root_collision_kernel(6, 3, 5, 3, 2, 4)
        self.assertEqual(data["common_root"], 4)
        self.assertEqual(data["product_gap"], 2)
        self.assertLess(data["lhs"], data["rhs"])
        self.assertLess(data["moving_budget"], 36)

    def test_every_bounded_cubic_collision_is_between_adjacent_odds(self):
        saw_collision = False
        for k in range(4, 85):
            buckets: dict[int, list[tuple[int, int]]] = {}
            for product in range(1, k, 2):
                channel = fixed_product_channel(k, product)
                for radius in channel["radii"]:
                    quotient = joint_product_root(k, radius, product)["joint_quotient"]
                    root = integer_nth_root(quotient, 3)
                    buckets.setdefault(root, []).append((product, radius))
            for root, entries in buckets.items():
                products = sorted({product for product, _radius in entries})
                self.assertLessEqual(len(products), 2)
                if len(products) != 2:
                    continue
                saw_collision = True
                self.assertEqual(products[1] - products[0], 2)
                left = next(radius for product, radius in entries if product == products[0])
                right = next(radius for product, radius in entries if product == products[1])
                data = cubic_product_collision_ambiguity(
                    k, products[0], products[1], left, right
                )
                self.assertEqual(data["common_root"], root)
                self.assertEqual(data["repair_cardinality"], 2)
                self.assertEqual(data["repair_bits"], 1)
        self.assertTrue(saw_collision)

    def test_actual_residual_hard_core_attains_one_bit_ambiguity(self):
        smaller = residual_cubic_core_product_observation(88, 63)
        larger = residual_cubic_core_product_observation(88, 31)
        self.assertEqual(smaller["core_product"], 85)
        self.assertEqual(larger["core_product"], 87)
        self.assertEqual(smaller["cubic_joint_root"], 89)
        self.assertEqual(larger["cubic_joint_root"], 89)
        data = cubic_product_collision_ambiguity(88, 85, 87, 63, 31)
        self.assertEqual(data["repair_bits"], 1)

    def test_residual_cubic_root_never_has_three_core_products_on_bounded_domain(self):
        for k in range(16, 145):
            buckets: dict[int, set[int]] = {}
            for radius in range(1, k):
                try:
                    data = residual_cubic_core_product_observation(k, radius)
                except ValueError:
                    continue
                buckets.setdefault(data["cubic_joint_root"], set()).add(data["core_product"])
            for products in buckets.values():
                self.assertLessEqual(len(products), 2)
                if len(products) == 2:
                    ordered = sorted(products)
                    self.assertEqual(ordered[1] - ordered[0], 2)


if __name__ == "__main__":
    unittest.main()
