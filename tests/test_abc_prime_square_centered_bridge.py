import unittest
from fractions import Fraction

from enterprise_math.abc_prime_square_centered_bridge import (
    p018_centered_shell_bridge,
    prime_square_centered_bridge,
    prime_square_difference_threshold_holds,
)


class PrimeSquareCenteredBridgeTests(unittest.TestCase):
    def test_exact_dual_quadratic_coordinates(self) -> None:
        bridge = prime_square_centered_bridge(5, 59)
        self.assertEqual((bridge.center, bridge.radius), (32, 27))
        self.assertEqual(bridge.p018_product_shell, 5 * 59)
        self.assertEqual(bridge.p025_difference_shell, 59**2 - 5**2)
        self.assertEqual(bridge.abc, (25, 3456, 3481))
        self.assertEqual(bridge.projective_atom_value, Fraction(9, 2))
        self.assertFalse(bridge.in_p018_size_range)
        self.assertTrue(prime_square_difference_threshold_holds(5, 59, 4))
        self.assertFalse(prime_square_difference_threshold_holds(5, 59, 5))

    def test_bridge_inside_canonical_p018_size_range(self) -> None:
        data = p018_centered_shell_bridge(73, 89)
        bridge = data["bridge"]
        self.assertEqual((bridge.center, bridge.radius), (81, 8))
        self.assertTrue(bridge.in_p018_size_range)
        self.assertEqual(bridge.p018_product_shell, 6497)
        self.assertEqual(bridge.p025_difference_shell, 2592)
        self.assertEqual(bridge.projective_atom_value, Fraction(4, 3))
        self.assertEqual(data["p018_shell_data"]["pair"], (73, 89))
        self.assertEqual(data["p018_shell_data"]["shell"], [6497])

    def test_another_p018_range_activation(self) -> None:
        bridge = prime_square_centered_bridge(503, 521)
        self.assertEqual((bridge.center, bridge.radius), (512, 9))
        self.assertTrue(bridge.in_p018_size_range)
        self.assertEqual(bridge.projective_atom_value, Fraction(3, 2))

    def test_small_subunit_pair(self) -> None:
        bridge = prime_square_centered_bridge(3, 5)
        self.assertEqual((bridge.center, bridge.radius), (4, 1))
        self.assertEqual(bridge.projective_atom_value, Fraction(1, 2))
        self.assertFalse(prime_square_difference_threshold_holds(3, 5, 1))

    def test_p018_size_gate_remains_explicit(self) -> None:
        with self.assertRaises(ValueError):
            p018_centered_shell_bridge(5, 59)


if __name__ == "__main__":
    unittest.main()
