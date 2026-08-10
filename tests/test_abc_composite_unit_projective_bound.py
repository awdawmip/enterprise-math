import unittest
from fractions import Fraction

from enterprise_math.abc_composite_unit_projective_bound import (
    composite_support_load_bound_holds,
    composite_unit_projective_bound,
    oesterle_to_composite_unit_projective_eta_threshold,
)


class AbcCompositeUnitProjectiveBoundTests(unittest.TestCase):
    def test_composite_support_load_bound(self) -> None:
        for n in (8, 9, 242, 243, 288, 289, 57121, 57122):
            self.assertTrue(composite_support_load_bound_holds(n))

    def test_hard_unit_examples_obey_elementary_radical_bound(self) -> None:
        for b, c in ((8, 9), (242, 243), (288, 289), (512, 513), (57121, 57122)):
            data = composite_unit_projective_bound(b, c)
            self.assertLessEqual(data.squared_bound_left, data.squared_bound_right)

    def test_prime_exception_is_not_hidden(self) -> None:
        with self.assertRaises(ValueError):
            composite_unit_projective_bound(7, 8)

    def test_direct_oesterle_threshold(self) -> None:
        self.assertEqual(
            oesterle_to_composite_unit_projective_eta_threshold(Fraction(3, 2)),
            Fraction(5, 6),
        )
        self.assertEqual(
            oesterle_to_composite_unit_projective_eta_threshold(Fraction(4, 3)),
            Fraction(3, 4),
        )


if __name__ == "__main__":
    unittest.main()
