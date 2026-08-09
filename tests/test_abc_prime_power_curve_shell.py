import unittest

from enterprise_math.abc_prime_power_curve_shell import (
    prime_power_square_kernel_curve,
)


class AbcPrimePowerCurveShellTests(unittest.TestCase):
    def test_prime_square_shell_is_pell(self) -> None:
        plus = prime_power_square_kernel_curve(239, 2, 1)
        self.assertEqual(plus.curve_type, "pell_conic")
        self.assertEqual(plus.curve_genus, 0)
        self.assertEqual(plus.squarefree_kernel, 2)
        self.assertEqual(plus.square_divisor_root, 169)

        minus = prime_power_square_kernel_curve(17, 2, -1)
        self.assertEqual(minus.curve_type, "pell_conic")
        self.assertEqual(minus.curve_genus, 0)

    def test_exponents_three_and_four_route_to_genus_one(self) -> None:
        cube = prime_power_square_kernel_curve(2, 3, 1)
        self.assertEqual(cube.neighboring_value, 9)
        self.assertEqual(cube.curve_genus, 1)
        self.assertEqual(cube.curve_type, "genus_one_hyperelliptic")

        fourth = prime_power_square_kernel_curve(3, 4, 1)
        self.assertEqual(fourth.curve_genus, 1)
        self.assertEqual(fourth.curve_type, "genus_one_hyperelliptic")

    def test_exponent_five_and_above_route_to_higher_genus(self) -> None:
        fifth = prime_power_square_kernel_curve(2, 5, 1)
        self.assertEqual(fifth.curve_genus, 2)
        self.assertEqual(fifth.curve_type, "higher_genus_hyperelliptic")

        ninth = prime_power_square_kernel_curve(3, 9, -1)
        self.assertEqual(ninth.curve_genus, 4)
        self.assertEqual(ninth.curve_type, "higher_genus_hyperelliptic")

    def test_squarefree_kernel_identity(self) -> None:
        data = prime_power_square_kernel_curve(13, 4, 1)
        Y, k, neighbor = data.curve_identity
        self.assertEqual(Y * Y, k * neighbor)


if __name__ == "__main__":
    unittest.main()
