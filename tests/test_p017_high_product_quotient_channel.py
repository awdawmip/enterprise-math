import unittest

from enterprise_math.p017_high_product_quotient_channel import (
    exact_high_product_quotient,
    exact_quotient_collision_kernel,
    terminal_exact_quotient_injectivity,
)


class P017HighProductQuotientChannelTests(unittest.TestCase):
    def test_same_S_square_root_collision_is_split_by_exact_Q(self):
        rows = (
            (37, 21, 5, 136_211),
            (23, 35, 3, 136_219),
            (47, 15, 7, 136_203),
        )
        quotients = []
        for point, radical, prime, expected_q in rows:
            data = exact_high_product_quotient(61, point, radical * prime)
            self.assertEqual(data["combined_product"], 105)
            self.assertEqual(data["exact_joint_quotient"], expected_q)
            self.assertGreater(data["exact_joint_quotient"], 61 * 61)
            quotients.append(data["exact_joint_quotient"])
        self.assertEqual(len(set(quotients)), 3)

    def test_k9070_duplicate_square_root_product_has_distinct_exact_quotients(self):
        left = exact_high_product_quotient(9_070, 233, 69_069)
        right = exact_high_product_quotient(9_070, 779, 69_069)
        self.assertEqual(left["exact_joint_quotient"], 98_003_534_719)
        self.assertEqual(right["exact_joint_quotient"], 98_003_534_711)
        self.assertNotEqual(left["exact_joint_quotient"], right["exact_joint_quotient"])

    def test_generic_exact_Q_leaves_only_orientation_bit(self):
        data = exact_quotient_collision_kernel(61, 23, 105, -23, 105)
        self.assertTrue(data["same_product"])
        self.assertTrue(data["same_radius_magnitude"])
        self.assertTrue(data["orientation_ambiguous"])

    def test_terminal_exact_Q_is_signed_row_injective(self):
        data = terminal_exact_quotient_injectivity(
            61,
            23,
            21,
            5,
            23,
            21,
            5,
        )
        self.assertTrue(data["signed_row_injective"])
        self.assertEqual(data["terminal_support_depth"], 2)
        self.assertEqual(data["remaining_repair_bits"], 0)

    def test_high_product_bound_is_required(self):
        with self.assertRaises(ValueError):
            exact_high_product_quotient(61, 1, 15)


if __name__ == "__main__":
    unittest.main()
