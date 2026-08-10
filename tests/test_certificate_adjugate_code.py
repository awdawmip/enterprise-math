import unittest

from enterprise_math.certificate_adjugate_code import (
    certificate_target_code,
    certificate_target_coordinates,
    certificate_target_is_attainable,
    square_certificate_congruence_code,
    square_lattice_congruence_code,
)
from enterprise_math.certificate_image_index import lattice_defect_signature


class CertificateAdjugateCodeTests(unittest.TestCase):
    def test_same_smith_type_can_have_different_labelled_membership(self) -> None:
        relation_basis = ((1, 0, 1), (0, 1, 1))

        first_rows = ((2, 0, 0), (0, 1, 0))
        first = square_certificate_congruence_code(relation_basis, first_rows)
        first_signature = lattice_defect_signature(((2, 0), (0, 1)))

        second_rows = ((1, 1, 0), (1, -1, 0))
        second = square_certificate_congruence_code(relation_basis, second_rows)
        second_signature = lattice_defect_signature(((1, 1), (1, -1)))

        self.assertEqual(first_signature.invariant_factors, (1, 2))
        self.assertEqual(second_signature.invariant_factors, (1, 2))

        target = (0, 1)
        self.assertTrue(certificate_target_is_attainable(first, target))
        self.assertFalse(certificate_target_is_attainable(second, target))
        self.assertEqual(certificate_target_code(first, target), (0, 0))
        self.assertNotEqual(certificate_target_code(second, target), (0, 0))

    def test_exact_coordinates_recovered_for_attainable_target(self) -> None:
        relation_basis = ((1, 0, 1), (0, 1, 1))
        rows = ((2, 0, 0), (0, 1, 0))
        code = square_certificate_congruence_code(relation_basis, rows)
        self.assertEqual(certificate_target_coordinates(code, (6, -2)), (3, -2))
        with self.assertRaises(ValueError):
            certificate_target_coordinates(code, (1, 0))

    def test_scalar_code_is_mod_eta(self) -> None:
        code = square_lattice_congruence_code(((5,),))
        self.assertEqual(code.modulus, 5)
        self.assertEqual(certificate_target_code(code, (12,)), (2,))
        self.assertTrue(certificate_target_is_attainable(code, (15,)))
        self.assertFalse(certificate_target_is_attainable(code, (12,)))

    def test_adjugate_code_exact_for_nonsymmetric_basis(self) -> None:
        code = square_lattice_congruence_code(((2, 1), (1, 3)))
        self.assertEqual(abs(code.determinant), 5)
        target = (8, 9)
        # columns (2,1),(1,3) with coordinates (3,2)
        self.assertTrue(certificate_target_is_attainable(code, target))
        self.assertEqual(certificate_target_coordinates(code, target), (3, 2))


if __name__ == "__main__":
    unittest.main()
