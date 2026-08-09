import unittest

from enterprise_math.abc_absorption_rank2 import (
    common_kernel_direction,
    parameter_interval_for_radius,
    rank_two_absorption_optimum,
)


class AbcAbsorptionRankTwoTests(unittest.TestCase):
    def test_common_kernel_directions(self) -> None:
        self.assertEqual(common_kernel_direction(2, 3, 5), (2, 3, 5))
        self.assertEqual(common_kernel_direction(2, 7, 9), (4, 3, 14))
        self.assertEqual(common_kernel_direction(1, 242, 243), (4, 0, -11))

    def test_exact_235_optimum(self) -> None:
        result = rank_two_absorption_optimum(2, 3, 5)
        self.assertEqual(result.radius, 2)
        self.assertEqual(result.absorption_redundancy, 1)
        self.assertEqual(max(abs(x) for x in result.witness), 2)

    def test_exact_279_optimum(self) -> None:
        result = rank_two_absorption_optimum(2, 7, 9)
        self.assertEqual(result.radius, 5)
        self.assertEqual(result.absorption_redundancy, 1)
        self.assertEqual(result.witness, (1, 1, 5))

    def test_exact_1242243_optimum_without_ball_enumeration(self) -> None:
        result = rank_two_absorption_optimum(1, 242, 243)
        self.assertEqual(result.particular_witness, (-405, 11, 1215))
        self.assertEqual(result.homogeneous_direction, (4, 0, -11))
        self.assertEqual(result.parameter, 108)
        self.assertEqual(result.witness, (27, 11, 27))
        self.assertEqual(result.radius, 27)
        self.assertEqual(result.absorption_redundancy, 5)

    def test_interval_boundary_detects_optimum(self) -> None:
        particular = (-405, 11, 1215)
        direction = (4, 0, -11)
        self.assertIsNone(parameter_interval_for_radius(particular, direction, 26))
        self.assertEqual(parameter_interval_for_radius(particular, direction, 27), (108, 108))

    def test_requires_exactly_three_prime_coordinates(self) -> None:
        with self.assertRaises(ValueError):
            rank_two_absorption_optimum(1, 8, 9)


if __name__ == "__main__":
    unittest.main()
