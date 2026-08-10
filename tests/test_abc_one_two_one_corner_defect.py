import unittest
from fractions import Fraction

from enterprise_math.abc_one_two_one_corner_defect import (
    first_witness_modular_alignment_is_sharp,
    modular_corner_defect,
)


class AbcOneTwoOneCornerDefectTests(unittest.TestCase):
    def test_classic_radius_601_gap_is_forced_modular_defect(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        data = modular_corner_defect(a, b, c, 601)
        self.assertEqual(data.modulus, 19683)
        self.assertEqual(data.outer_deficits, (0, 15))
        self.assertEqual(data.weighted_defect, 41_976_150)
        self.assertEqual(data.alignment_lower_bound, Fraction(6611, 6561))
        self.assertTrue(first_witness_modular_alignment_is_sharp(a, b, c, 601))

    def test_exact_projective_radius_has_zero_modular_defect(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        data = modular_corner_defect(a, b, c, 6561)
        self.assertEqual(data.outer_deficits, (0, 0))
        self.assertEqual(data.weighted_defect, 0)
        self.assertEqual(data.alignment_lower_bound, 1)

    def test_radius_600_has_strict_modular_corner_loss(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        data = modular_corner_defect(a, b, c, 600)
        self.assertGreater(data.weighted_defect, 0)
        self.assertGreaterEqual(data.alignment_lower_bound, 1)


if __name__ == "__main__":
    unittest.main()
