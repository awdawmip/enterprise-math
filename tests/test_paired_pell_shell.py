import unittest
from fractions import Fraction

from enterprise_math.paired_pell_shell import (
    geometric_tail_bound,
    n58_certificate,
    n58_integer_constants,
    n58_ratio_certificate,
    paired_pell_certificate,
)


class PairedPellShellTests(unittest.TestCase):
    def test_n58_pair(self):
        cert = n58_certificate()
        self.assertEqual(cert.P, 99)
        self.assertEqual(cert.positive_shell, 2 * 70**2)
        self.assertEqual(cert.negative_shell, 58 * 13**2)
        self.assertEqual(cert.fourth_residual, 99**4 - 1)
        self.assertEqual(cert.fused_shell, 99**4 - 1)
        self.assertEqual(cert.fugacity, Fraction(1, 99**4))

    def test_other_shared_P_pairs(self):
        cert3 = paired_pell_certificate(3, 2, 2, 10, 1)
        self.assertEqual(cert3.fused_shell, 3**4 - 1)
        cert7 = paired_pell_certificate(7, 3, 4, 2, 5)
        self.assertEqual(cert7.fused_shell, 7**4 - 1)

    def test_invalid_pair_rejected(self):
        with self.assertRaises(ValueError):
            paired_pell_certificate(99, 2, 69, 58, 13)

    def test_n58_integer_constants(self):
        values = n58_integer_constants()
        self.assertEqual(values["four_times_P"], 396)
        self.assertEqual(values["P_squared"], 9801)
        self.assertEqual(values["ramanujan_linear_n"], 26390)
        self.assertTrue(values["ramanujan_constant_certificate"])

    def test_tail_bound(self):
        q = n58_ratio_certificate()
        self.assertEqual(q, Fraction(25, 99**4))
        first = Fraction(7, 1000)
        self.assertEqual(geometric_tail_bound(first, q), first / (1 - q))
        with self.assertRaises(ValueError):
            geometric_tail_bound(first, Fraction(1, 1))


if __name__ == "__main__":
    unittest.main()
