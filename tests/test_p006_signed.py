import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.signed import (
    signed_magnitude_collapse,
    signed_magnitude_root,
    signed_order_collapse,
    signed_order_root,
)


class TestP006SignedStateExtension(unittest.TestCase):
    def test_odd_order_root_characterization(self):
        for p in (1, 3, 5):
            for n in range(-200, 201):
                k = signed_order_root(n, p)
                self.assertLessEqual(k**p, n)
                self.assertLess(n, (k + 1) ** p)

    def test_odd_order_root_agrees_with_natural_root_on_nonnegative_states(self):
        for p in (1, 3, 5):
            for n in range(201):
                self.assertEqual(signed_order_root(n, p), integer_nth_root(n, p))

    def test_negative_order_root_uses_ceiling_magnitude(self):
        for p in (1, 3, 5):
            for magnitude in range(1, 201):
                floor_root = integer_nth_root(magnitude, p)
                ceiling_root = floor_root if floor_root**p == magnitude else floor_root + 1
                self.assertEqual(signed_order_root(-magnitude, p), -ceiling_root)

    def test_order_collapse_is_order_contractive_and_idempotent(self):
        for p in (1, 3, 5):
            for n in range(-200, 201):
                value = signed_order_collapse(n, p)
                self.assertLessEqual(value, n)
                self.assertEqual(signed_order_collapse(value, p), value)

    def test_signed_magnitude_collapse_is_odd_magnitude_contractive_and_idempotent(self):
        for p in (1, 2, 3, 4, 5):
            for n in range(-200, 201):
                value = signed_magnitude_collapse(n, p)
                self.assertEqual(signed_magnitude_collapse(-n, p), -value)
                self.assertLessEqual(abs(value), abs(n))
                self.assertEqual(signed_magnitude_collapse(value, p), value)

    def test_signed_magnitude_fixed_points_have_perfect_power_magnitude(self):
        for p in (1, 2, 3, 4, 5):
            for n in range(-200, 201):
                fixed = signed_magnitude_collapse(n, p) == n
                root = integer_nth_root(abs(n), p)
                perfect_magnitude = root**p == abs(n)
                self.assertEqual(fixed, perfect_magnitude)

    def test_two_signed_root_semantics_disagree_on_negative_nonpower(self):
        self.assertEqual(signed_order_root(-2, 3), -2)
        self.assertEqual(signed_magnitude_root(-2, 3), -1)
        self.assertNotEqual(signed_order_root(-2, 3), signed_magnitude_root(-2, 3))

    def test_order_and_magnitude_collapses_move_in_different_orders(self):
        self.assertEqual(signed_order_collapse(-2, 3), -8)
        self.assertEqual(signed_magnitude_collapse(-2, 3), -1)
        self.assertLessEqual(signed_order_collapse(-2, 3), -2)
        self.assertGreaterEqual(signed_magnitude_collapse(-2, 3), -2)

    def test_even_exponents_are_rejected_by_order_root(self):
        for p in (2, 4, 6):
            with self.assertRaises(ValueError):
                signed_order_root(-2, p)
            with self.assertRaises(ValueError):
                signed_order_collapse(2, p)


if __name__ == "__main__":
    unittest.main()
