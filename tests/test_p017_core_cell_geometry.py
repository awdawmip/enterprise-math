import math
import unittest

from enterprise_math.p017_core_cell_geometry import (
    prefix_large_core_exclusion,
    repeated_full_core_spacing,
    signed_shared_core_geometry,
)
from enterprise_math.p017_core_cell_lattice import exact_full_core_pair, exact_full_core_strata


class P017CoreCellGeometryTests(unittest.TestCase):
    def test_signed_shared_core_divisibility(self) -> None:
        for k in range(5, 100):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            for index, left in enumerate(radii):
                for right in radii[index + 1 : index + 9]:
                    data = signed_shared_core_geometry(k, left, right)
                    self.assertEqual(
                        data["radius_difference"] % (2 * data["same_side_overlap"]), 0
                    )
                    self.assertEqual(
                        data["radius_sum"] % (2 * data["cross_side_overlap"]), 0
                    )
                    self.assertEqual(
                        data["radius_square_difference"] % (4 * data["total_overlap"]), 0
                    )

    def test_four_overlap_classes_are_pairwise_coprime(self) -> None:
        for k in range(5, 80):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            for index, left in enumerate(radii):
                for right in radii[index + 1 : index + 7]:
                    data = signed_shared_core_geometry(k, left, right)
                    values = [
                        data["lower_lower_gcd"],
                        data["upper_upper_gcd"],
                        data["lower_upper_gcd"],
                        data["upper_lower_gcd"],
                    ]
                    for i, first in enumerate(values):
                        for second in values[i + 1 :]:
                            self.assertEqual(math.gcd(first, second), 1)

    def test_repeated_exact_cell_recovers_2ab_spacing(self) -> None:
        saw_repeat = False
        for k in range(5, 220):
            strata = exact_full_core_strata(k)
            for (_a, _b), radii in strata.items():
                if len(radii) < 2:
                    continue
                saw_repeat = True
                for left, right in zip(radii, radii[1:]):
                    data = repeated_full_core_spacing(k, left, right)
                    self.assertEqual(
                        data["radius_difference"] % data["spacing_modulus"], 0
                    )
        self.assertTrue(saw_repeat)

    def test_shared_core_same_side_forces_radius_spacing(self) -> None:
        for k in range(5, 100):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            for index, left in enumerate(radii):
                a, b = exact_full_core_pair(k, left)
                for right in radii[index + 1 : index + 7]:
                    c, d = exact_full_core_pair(k, right)
                    self.assertEqual(abs(left - right) % (2 * math.gcd(a, c)), 0)
                    self.assertEqual(abs(left - right) % (2 * math.gcd(b, d)), 0)
                    self.assertEqual((left + right) % (2 * math.gcd(a, d)), 0)
                    self.assertEqual((left + right) % (2 * math.gcd(b, c)), 0)

    def test_prefix_large_core_exclusion(self) -> None:
        for k in range(10, 100):
            center = k * (k + 1)
            for radius_limit in (max(1, k // 5), max(1, k // 3)):
                for divisor in range(3, k + 1, 2):
                    if math.gcd(divisor, center) != 1:
                        continue
                    data = prefix_large_core_exclusion(k, divisor, radius_limit)
                    if divisor > radius_limit:
                        self.assertLessEqual(len(data["lower_hits"]), 1)
                        self.assertLessEqual(len(data["upper_hits"]), 1)
                    if divisor > 2 * radius_limit:
                        self.assertLessEqual(data["total_hits"], 1)


if __name__ == "__main__":
    unittest.main()
