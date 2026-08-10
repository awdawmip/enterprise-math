import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p017_mirror_product_bridge import (
    fixed_product_channel,
    joint_product_root,
)
from enterprise_math.p017_mirror_product_precision import (
    cubic_core_product_candidate_window,
    cubic_product_collision_ambiguity,
    moving_state_power_root_collision_kernel,
    residual_cubic_core_product_observation,
    residual_cubic_product_decoder,
    select_cubic_product_with_divisor,
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

    def test_explicit_cubic_decoder_window_is_sharp(self):
        data = cubic_core_product_candidate_window(88, 89)
        self.assertEqual(data["odd_candidates"], (85, 87))
        self.assertEqual(data["candidate_count"], 2)
        self.assertEqual(data["repair_bits"], 1)
        self.assertLess(data["width_numerator"], 4 * data["width_denominator"])

        self.assertEqual(
            select_cubic_product_with_divisor(88, 89, 5)["decoded_product"], 85
        )
        self.assertEqual(
            select_cubic_product_with_divisor(88, 89, 3)["decoded_product"], 87
        )

    def test_true_product_always_lies_in_cubic_decoder_window(self):
        for k in range(6, 75):
            for product in range(1, k, 2):
                channel = fixed_product_channel(k, product)
                for radius in channel["radii"]:
                    quotient = joint_product_root(k, radius, product)["joint_quotient"]
                    cubic_root = integer_nth_root(quotient, 3)
                    if cubic_root < k:
                        continue
                    window = cubic_core_product_candidate_window(k, cubic_root)
                    self.assertIn(product, window["odd_candidates"])
                    self.assertLessEqual(window["candidate_count"], 2)
                    if window["candidate_count"] == 2:
                        left, right = window["odd_candidates"]
                        self.assertEqual(right - left, 2)

    def test_actual_residual_hard_core_attains_one_bit_ambiguity(self):
        smaller = residual_cubic_core_product_observation(88, 63)
        larger = residual_cubic_core_product_observation(88, 31)
        self.assertEqual(smaller["core_product"], 85)
        self.assertEqual(larger["core_product"], 87)
        self.assertEqual(smaller["cubic_joint_root"], 89)
        self.assertEqual(larger["cubic_joint_root"], 89)
        data = cubic_product_collision_ambiguity(88, 85, 87, 63, 31)
        self.assertEqual(data["repair_bits"], 1)

        decoded_small = residual_cubic_product_decoder(88, 63)
        decoded_large = residual_cubic_product_decoder(88, 31)
        self.assertEqual(decoded_small["candidate_products"], (85, 87))
        self.assertEqual(decoded_large["candidate_products"], (85, 87))
        self.assertEqual(decoded_small["decoded_product"], 85)
        self.assertEqual(decoded_large["decoded_product"], 87)
        self.assertEqual(decoded_small["remaining_product_repair_bits"], 0)
        self.assertEqual(decoded_large["remaining_product_repair_bits"], 0)

    def test_residual_decoder_uses_small_core_to_remove_product_label(self):
        saw_two_candidate_window = False
        for k in range(16, 125):
            for radius in range(1, k):
                try:
                    data = residual_cubic_product_decoder(k, radius)
                except ValueError:
                    continue
                self.assertIn(data["core_product"], data["candidate_products"])
                self.assertEqual(data["decoded_product"], data["core_product"])
                self.assertEqual(data["remaining_product_repair_bits"], 0)
                if data["candidate_count"] == 2:
                    saw_two_candidate_window = True
                    left, right = data["candidate_products"]
                    self.assertEqual(right - left, 2)
                    selector = data["small_core_selector"]
                    self.assertEqual(
                        sum(candidate % selector == 0 for candidate in data["candidate_products"]),
                        1,
                    )
        self.assertTrue(saw_two_candidate_window)

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
