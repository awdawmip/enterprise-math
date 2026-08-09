import unittest
from fractions import Fraction

from enterprise_math.abc_multi_certificate import (
    certificate_vector,
    full_rank_certificate_rows_are_block_value_injective,
    multi_certificate_image,
    recover_block_value_from_two_independent_rows,
    same_smith_different_labelled_image_counterexample,
)


class AbcMultiCertificateTests(unittest.TestCase):
    def test_any_number_of_certificates_has_rank_at_most_two(self) -> None:
        rows = ((1, 0), (0, 1), (-3, 2), (4, 7), (11, -5))
        image = multi_certificate_image(2, 3, 5, rows)
        self.assertEqual(image.lattice_basis, ((1, 0), (0, 1)))
        self.assertEqual(image.rational_rank, 2)
        self.assertLessEqual(image.rational_rank, 2)
        self.assertEqual(
            certificate_vector(rows, 2, -1),
            (2, -1, -8, 1, 27),
        )

    def test_wronskian_plus_one_independent_form_recovers_block_values(self) -> None:
        rows = ((-3, 2), (1, 1))
        self.assertTrue(
            full_rank_certificate_rows_are_block_value_injective(2, 3, 5, rows)
        )
        values = certificate_vector(rows, 4, -2)
        recovered = recover_block_value_from_two_independent_rows(rows, values)
        self.assertEqual(recovered, (Fraction(4), Fraction(-2)))

    def test_dependent_certificates_do_not_recover_rank_two_block_state(self) -> None:
        rows = ((-3, 2), (-6, 4), (9, -6))
        image = multi_certificate_image(2, 3, 5, rows)
        self.assertEqual(image.rational_rank, 1)
        self.assertFalse(
            full_rank_certificate_rows_are_block_value_injective(2, 3, 5, rows)
        )

    def test_unit_relation_domain_is_rank_one(self) -> None:
        image = multi_certificate_image(1, 8, 9, ((0, 1), (0, 2)))
        self.assertEqual(len(image.lattice_basis), 1)
        self.assertEqual(image.rational_rank, 1)
        self.assertTrue(
            full_rank_certificate_rows_are_block_value_injective(
                1, 8, 9, ((0, 1), (0, 2))
            )
        )

    def test_smith_invariants_do_not_determine_labelled_image(self) -> None:
        data = same_smith_different_labelled_image_counterexample()
        self.assertEqual(data["invariant_factors"], (1, 2))
        self.assertEqual(data["distinguishing_target"], (1, 0))
        self.assertEqual(data["membership"], (True, False))

    def test_nontrivial_compressed_lattice_changes_image_invariants(self) -> None:
        rows = ((-7, 2), (1, 0), (0, 1))
        image = multi_certificate_image(2, 7, 9, rows)
        self.assertEqual(image.lattice_basis, ((6, 0), (5, 1)))
        self.assertEqual(image.rational_rank, 2)
        self.assertEqual(image.generator_columns[0], (-42, 6, 0))
        self.assertEqual(image.generator_columns[1], (-33, 5, 1))

    def test_recovery_rejects_dependent_rows(self) -> None:
        with self.assertRaises(ValueError):
            recover_block_value_from_two_independent_rows(
                ((1, 2), (2, 4)),
                (3, 6),
            )


if __name__ == "__main__":
    unittest.main()
