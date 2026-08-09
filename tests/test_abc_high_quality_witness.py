import unittest

from enterprise_math.abc_high_quality_witness import (
    CLASSIC_A,
    CLASSIC_B,
    CLASSIC_C,
    classic_basis_vector,
    classic_exact_witness_precision,
    classic_generator_rows,
    classic_high_quality_profile,
    classic_radius_600_obstruction_table,
    classic_reduced_kernel_basis,
    classic_triple,
)


class ClassicHighQualityWitnessTests(unittest.TestCase):
    def test_classic_triple_and_quality(self) -> None:
        self.assertEqual(classic_triple(), (2, 6_436_341, 6_436_343))
        self.assertEqual(CLASSIC_A + CLASSIC_B, CLASSIC_C)
        profile = classic_high_quality_profile()
        self.assertEqual(profile["radical"], 15_042)
        self.assertTrue(profile["high_quality_3_over_2"])
        self.assertGreater(profile["c_squared"], profile["radical_cubed"])

    def test_exact_generator_rows(self) -> None:
        rows = classic_generator_rows()
        self.assertEqual(rows["coordinates"], (2, 3, 23, 109))
        self.assertEqual(rows["alpha"], (1, 21_454_470, -1_399_205, 59_049))
        self.assertEqual(rows["beta"], (-327, 2_180, 0, 6))

    def test_reduced_basis_is_unimodular_and_diagonalizes_degeneracy(self) -> None:
        profile = classic_reduced_kernel_basis()
        self.assertEqual(profile["transform_determinant"], -1)
        self.assertEqual(
            profile["basis"],
            (
                (20, 3, 46, 0),
                (10, 0, 23, 545),
                (721, -20, -310, -79),
            ),
        )
        self.assertEqual(profile["beta_values"], (0, 0, -279_841))

    def test_radius_600_obstruction_has_ten_strict_rows(self) -> None:
        table = classic_radius_600_obstruction_table()
        self.assertEqual(len(table), 10)
        self.assertTrue(
            all(row["A_lower_from_p23"] > row["A_upper_from_p2"] for row in table)
        )
        self.assertEqual(
            [(row["C"], row["B"], row["gap"]) for row in table[:2]],
            [(1, 0, 1), (1, 1, 1)],
        )

    def test_explicit_radius_601_witness(self) -> None:
        self.assertEqual(classic_basis_vector(6, 0, -1), (-601, 38, 586, 79))
        certificate = classic_exact_witness_precision()
        self.assertEqual(certificate["mu"], 601)
        self.assertEqual(certificate["explicit_witness"], (-601, 38, 586, 79))
        self.assertEqual(certificate["lambda_abc"], 597)
        self.assertEqual(certificate["combined_floor"], 597)
        self.assertEqual(certificate["nondegeneracy_overhead_over_certified_floor"], 4)
        self.assertEqual(certificate["U2"], 59_049)

    def test_additive_basis_has_small_degenerate_state(self) -> None:
        certificate = classic_exact_witness_precision()
        self.assertEqual(certificate["additive_radius_upper_certificate"], 46)
        self.assertLess(certificate["additive_radius_upper_certificate"], certificate["lambda_abc"])


if __name__ == "__main__":
    unittest.main()
