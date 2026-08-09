import math
import unittest

from enterprise_math.p017_mirror_product_bridge import (
    fixed_product_channel,
    p017_mirror_product_embedding,
    quadratic_mirror_embedding,
    residual_hard_core_joint_channel,
    separated_product_channels,
    shared_core_gap_transport,
)


class P017MirrorProductBridgeTests(unittest.TestCase):
    def test_general_quadratic_mirror_embedding_including_lower_boundary(self):
        data = quadratic_mirror_embedding(5, 3)
        self.assertEqual(data["value"], 16)
        self.assertEqual(data["root"], 4)
        self.assertEqual(data["gap"], 0)

    def test_p017_embedding_is_exact_on_bounded_domain(self):
        for k in range(2, 90):
            center = k * (k + 1)
            for radius in range(1, k):
                data = p017_mirror_product_embedding(k, radius)
                self.assertEqual(data["product"], (center - radius) * (center + radius))
                self.assertEqual(data["root"], center - 1)
                self.assertEqual(data["gap"], 2 * center - 1 - radius * radius)
                self.assertEqual(data["product_root_carry"], k - 1)
                self.assertEqual(data["higher_offset"], center - radius * radius)

    def test_fixed_product_channels_use_at_most_two_adjacent_roots(self):
        saw_two_state_channel = False
        for k in range(2, 85):
            for product in range(1, k, 2):
                data = fixed_product_channel(k, product)
                roots = data["roots"]
                self.assertLessEqual(len(roots), 2)
                if len(roots) == 2:
                    self.assertEqual(roots[1] - roots[0], 1)
                    saw_two_state_channel = True
        self.assertTrue(saw_two_state_channel)

        sharp = fixed_product_channel(7, 5)
        self.assertEqual(sharp["roots"], (24, 25))

    def test_distinct_odd_product_channels_are_separated(self):
        for k in range(6, 55):
            channels = {
                product: fixed_product_channel(k, product)
                for product in range(1, k, 2)
            }
            nonempty = [p for p, data in channels.items() if data["radii"]]
            for i, smaller in enumerate(nonempty):
                for larger in nonempty[i + 1 :]:
                    small_data = channels[smaller]
                    large_data = channels[larger]
                    self.assertGreaterEqual(
                        min(small_data["roots"]), max(large_data["roots"]) + 2
                    )
                    separated_product_channels(
                        k,
                        smaller,
                        larger,
                        small_data["radii"][0],
                        large_data["radii"][0],
                    )

        # Close finite boundary found by exhaustive search: the proved gap is
        # >=2, while this small example has gap 4.
        small = fixed_product_channel(12, 9)
        large = fixed_product_channel(12, 11)
        self.assertEqual(small["roots"], (51,))
        self.assertEqual(large["roots"], (46, 47))
        self.assertEqual(min(small["roots"]) - max(large["roots"]), 4)

    def test_residual_hard_core_joint_root_recovers_product_channel(self):
        # One exact full-core product can genuinely occupy two adjacent roots,
        # so CG07 is sharp and CG09 must decode the product rather than a unique
        # radius or orientation.
        left = residual_hard_core_joint_channel(214, 37)
        right = residual_hard_core_joint_channel(214, 149)
        self.assertEqual(left["core_product"], 93)
        self.assertEqual(right["core_product"], 93)
        self.assertEqual(left["joint_root"], 4771)
        self.assertEqual(right["joint_root"], 4770)

        # Across the bounded residual hard core, no one joint-root state can
        # represent two distinct core products.  This is a regression of CG08,
        # not the proof of it.
        for k in range(6, 150):
            center = k * (k + 1)
            seen: dict[int, int] = {}
            for radius in range(1, k):
                if math.gcd(radius, center) != 1:
                    continue
                try:
                    data = residual_hard_core_joint_channel(k, radius)
                except ValueError:
                    continue
                root = data["joint_root"]
                product = data["core_product"]
                if root in seen:
                    self.assertEqual(seen[root], product)
                else:
                    seen[root] = product

    def test_shared_core_geometry_transports_to_higher_gap(self):
        for k in range(8, 45):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            for left, right in zip(radii, radii[1:]):
                data = shared_core_gap_transport(k, left, right)
                self.assertEqual(
                    data["gap_difference"], abs(left * left - right * right)
                )
                self.assertEqual(
                    data["gap_difference"] % data["shared_core_divisor"], 0
                )


if __name__ == "__main__":
    unittest.main()
