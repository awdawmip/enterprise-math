import math
import unittest

from enterprise_math.geometry import l1_distance


class TestP012PythagoreanBoundary(unittest.TestCase):
    def test_coordinate_geodesic_additivity(self):
        for a in range(-12, 13):
            for b in range(-12, 13):
                origin = (0, 0)
                corner = (a, 0)
                target = (a, b)
                self.assertEqual(
                    l1_distance(origin, target),
                    l1_distance(origin, corner) + l1_distance(corner, target),
                )

    def test_same_discrete_sphere_contains_different_euclidean_squared_radii(self):
        origin = (0, 0)
        axial = (2, 0)
        diagonal = (1, 1)
        self.assertEqual(l1_distance(origin, axial), 2)
        self.assertEqual(l1_distance(origin, diagonal), 2)
        self.assertNotEqual(2**2 + 0**2, 1**2 + 1**2)

    def test_l1_norm_fails_parallelogram_identity(self):
        x = (1, 0)
        y = (0, 1)
        plus = (x[0] + y[0], x[1] + y[1])
        minus = (x[0] - y[0], x[1] - y[1])
        zero = (0, 0)

        left = l1_distance(zero, plus) ** 2 + l1_distance(zero, minus) ** 2
        right = 2 * l1_distance(zero, x) ** 2 + 2 * l1_distance(zero, y) ** 2
        self.assertEqual(left, 8)
        self.assertEqual(right, 4)
        self.assertNotEqual(left, right)

    def test_number_of_monotone_geodesics(self):
        for a in range(0, 9):
            for b in range(0, 9):
                self.assertEqual(
                    math.comb(a + b, a),
                    math.comb(a + b, b),
                )
                self.assertEqual(l1_distance((0, 0), (a, b)), a + b)


if __name__ == "__main__":
    unittest.main()
