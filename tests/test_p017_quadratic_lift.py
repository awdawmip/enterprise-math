import math
import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p017_quadratic_lift import (
    lifted_full_core_square_spacing,
    mirror_product_factor_transport,
    mirror_product_lift,
)


class P017QuadraticLiftTests(unittest.TestCase):
    def test_every_mirror_product_lands_in_target_square_basin(self) -> None:
        for k in range(2, 120):
            center = k * (k + 1)
            for radius in range(1, k):
                data = mirror_product_lift(k, radius)
                self.assertEqual(data["target_root"], center - 1)
                self.assertEqual(integer_nth_root(data["lifted_state"], 2), center - 1)
                self.assertEqual(data["lifted_state"], (center - radius) * (center + radius))

    def test_target_gap_recovers_radius_square(self) -> None:
        for k in range(2, 150):
            center = k * (k + 1)
            for radius in range(1, k):
                data = mirror_product_lift(k, radius)
                self.assertEqual(
                    radius * radius,
                    2 * center - 1 - data["target_gap"],
                )
                self.assertEqual(data["target_offset"], center - radius * radius)

    def test_factor_precision_multiplies_across_mirror_pair(self) -> None:
        for k in range(2, 90):
            for radius in range(1, k):
                data = mirror_product_factor_transport(k, radius)
                self.assertEqual(
                    data["lifted_core_at_k"], data["lower_core"] * data["upper_core"]
                )
                self.assertEqual(
                    data["lifted_tail_at_k"], data["lower_tail"] * data["upper_tail"]
                )
                self.assertEqual(
                    data["lifted_state"], data["lifted_core_at_k"] * data["lifted_tail_at_k"]
                )

    def test_factor_eight_shared_full_core_spacing(self) -> None:
        saw_nontrivial_shared_core = False
        for k in range(5, 120):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            for index, left in enumerate(radii):
                for right in radii[index + 1 : index + 8]:
                    data = lifted_full_core_square_spacing(k, left, right)
                    self.assertEqual(
                        data["radius_square_difference"] % data["required_divisor"], 0
                    )
                    if data["shared_total_core"] > 1:
                        saw_nontrivial_shared_core = True
        self.assertTrue(saw_nontrivial_shared_core)

    def test_r1_maps_to_target_unpaired_upper_state(self) -> None:
        for k in range(2, 80):
            data = mirror_product_lift(k, 1)
            target_root = data["target_root"]
            target_center = target_root * (target_root + 1)
            self.assertEqual(data["target_offset"], target_root)
            self.assertEqual(data["lifted_state"], target_center + target_root)


if __name__ == "__main__":
    unittest.main()
