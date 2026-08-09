import unittest
from fractions import Fraction

from enterprise_math.abc_nonunit_projective_bound import (
    nonunit_projective_bound,
    oesterle_to_nonunit_projective_eta_threshold,
)


class AbcNonunitProjectiveBoundTests(unittest.TestCase):
    def test_classic_high_quality_nonunit_bound(self) -> None:
        data = nonunit_projective_bound(2, 3**10 * 109, 23**5)
        self.assertEqual(data.radical_product, 15042)
        self.assertEqual(data.sigma_projective, Fraction(6561, 11))
        self.assertLessEqual(data.squared_bound_left, data.squared_bound_right)

    def test_small_nonunit_examples(self) -> None:
        for triple in ((2, 3, 5), (2, 7, 9), (5, 7, 12), (3, 125, 128)):
            data = nonunit_projective_bound(*triple)
            self.assertLessEqual(data.squared_bound_left, data.squared_bound_right)

    def test_unit_slice_is_deliberately_not_hidden(self) -> None:
        with self.assertRaises(ValueError):
            nonunit_projective_bound(1, 242, 243)

    def test_oesterle_exponent_transfer_is_direct_on_nonunit_slice(self) -> None:
        self.assertEqual(
            oesterle_to_nonunit_projective_eta_threshold(Fraction(2, 1)),
            Fraction(3, 4),
        )
        self.assertEqual(
            oesterle_to_nonunit_projective_eta_threshold(Fraction(3, 2)),
            Fraction(2, 3),
        )


if __name__ == "__main__":
    unittest.main()
