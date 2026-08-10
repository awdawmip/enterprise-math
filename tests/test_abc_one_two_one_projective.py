import unittest
from fractions import Fraction

from enterprise_math.abc_one_two_one_projective import (
    ac_projective_radius_modulus,
    ac_projective_witness_at_radius,
    exact_ac_projective_attainment_radius,
    first_witness_corner_alignment,
)


class AbcOneTwoOneProjectiveTests(unittest.TestCase):
    def test_classic_high_quality_projective_attainment_radius_is_6561(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(ac_projective_radius_modulus(a, b, c), 6561)
        self.assertIsNone(ac_projective_witness_at_radius(a, b, c, 6560))
        witness = exact_ac_projective_attainment_radius(a, b, c, 6561)
        self.assertEqual(witness.radius, 6561)
        self.assertEqual(witness.coordinates, (-6561, 412, 5774, 6561))
        self.assertEqual(witness.absorption_redundancy, 11)
        self.assertEqual(witness.projective_ratio, Fraction(6561, 11))

    def test_classic_first_witness_is_corner_defect_15(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        data = first_witness_corner_alignment(a, b, c, 601)
        self.assertEqual(data.mu, 601)
        self.assertEqual(data.oriented_coordinates, (-601, 38, 79, 586))
        self.assertEqual(data.outer_deficits, (0, 15))
        self.assertEqual(data.congruence_modulus, 19683)
        self.assertEqual(data.congruence_residue, 0)
        self.assertEqual(data.raw_capacity_slack, 41_976_150)
        self.assertEqual(data.projective_alignment_factor, Fraction(6611, 6561))

    def test_projective_exact_witness_occurs_far_after_first_witness(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        first = first_witness_corner_alignment(a, b, c, 601)
        exact_projective = exact_ac_projective_attainment_radius(a, b, c, 6561)
        self.assertGreater(exact_projective.radius, 10 * first.mu)
        self.assertLess(first.projective_alignment_factor, Fraction(101, 100))


if __name__ == "__main__":
    unittest.main()
