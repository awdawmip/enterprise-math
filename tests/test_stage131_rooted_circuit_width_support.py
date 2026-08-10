import unittest

from enterprise_math.stage131_rooted_circuit_table_explosion import (
    rooted_circuit_count,
    rooted_circuit_count_lower_bound,
    rooted_circuit_count_upper_bound,
    rooted_circuit_width_polynomial,
)


class Stage131RootedCircuitWidthSupportTests(unittest.TestCase):
    def test_every_width_from_two_through_all_leaves_occurs(self):
        for height in range(1, 10):
            polynomial = rooted_circuit_width_polynomial(height)
            self.assertEqual(
                set(polynomial),
                set(range(2, (1 << height) + 1)),
            )
            self.assertTrue(all(coefficient > 0 for coefficient in polynomial.values()))

    def test_rooted_circuit_count_is_exponential_in_leaf_count_between_simple_bounds(self):
        for height in range(2, 10):
            leaves = 1 << height
            count = rooted_circuit_count(height)
            self.assertGreaterEqual(count, 1 << (leaves // 2))
            self.assertLess(count, 1 << (leaves - 1))
            self.assertEqual(rooted_circuit_count_lower_bound(height), 1 << (leaves // 2))
            self.assertEqual(rooted_circuit_count_upper_bound(height), 1 << (leaves - 1))


if __name__ == "__main__":
    unittest.main()
