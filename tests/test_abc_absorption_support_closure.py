import math
import unittest

from enterprise_math.abc_absorption_support_closure import (
    absorption_floor_prime_support,
    absorption_support_closes_at_second_order,
    exponent_only_obstruction_example,
    first_order_prime_support,
    second_order_absorption_candidate_support,
    valuation_exponent_prime_support,
)


class AbcAbsorptionSupportClosureTests(unittest.TestCase):
    def test_exponent_only_obstruction_requires_second_order(self) -> None:
        data = exponent_only_obstruction_example()
        self.assertEqual(data["first_order_support"], (2, 3, 11))
        self.assertIn(5, data["valuation_exponent_support"])
        self.assertEqual(data["absorption_floor_support"], (5,))
        self.assertNotIn(5, data["first_order_support"])

    def test_known_examples_close_at_second_order(self) -> None:
        for triple in (
            (1, 8, 9),
            (1, 3, 4),
            (1, 242, 243),
            (1, 512, 513),
            (2, 7, 9),
            (5, 7, 12),
            (25, 704, 729),
        ):
            self.assertTrue(absorption_support_closes_at_second_order(*triple))

    def test_bounded_primitive_scan_has_no_third_order_prime_label(self) -> None:
        checked = 0
        for c in range(3, 90):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                self.assertTrue(absorption_support_closes_at_second_order(a, b, c))
                checked += 1
        self.assertGreater(checked, 1000)

    def test_support_layers_are_distinct(self) -> None:
        self.assertEqual(first_order_prime_support(1, 31, 32), (2, 31))
        self.assertEqual(valuation_exponent_prime_support(1, 31, 32), (5,))
        self.assertEqual(second_order_absorption_candidate_support(1, 31, 32), (2, 5, 31))
        self.assertEqual(absorption_floor_prime_support(1, 31, 32), (5,))


if __name__ == "__main__":
    unittest.main()
