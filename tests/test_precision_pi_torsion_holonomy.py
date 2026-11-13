from fractions import Fraction
from itertools import combinations
import unittest

from enterprise_math.precision_pi_torsion_holonomy import (
    VERTICES,
    add_edge_states,
    beta_factorized_ratio,
    beta_kernel,
    direct_probability_ratio,
    edge_total,
    endpoint_sum,
    endpoint_sum_matrix,
    exact_certificate,
    face_contrast,
    face_difference_lift,
    face_double_lift,
    matching_sums,
    matrix_multiply,
    normalized_covolume_ratio_square,
    residual_holonomy_sign,
    root_lattice_gram,
    saddle_certificate,
    saturation_index,
    scalar_matrix_multiply,
    scale_edge_state,
    torsion_bit_on_zero_matching,
    transpose,
    determinant,
)


class PrecisionPiTorsionHolonomyTests(unittest.TestCase):
    def test_root_lattice_covolume_squares(self) -> None:
        self.assertEqual(determinant(root_lattice_gram(3)), 4)
        self.assertEqual(determinant(root_lattice_gram(5)), 6)

    def test_endpoint_sum_metric_and_saturation(self) -> None:
        matrix = endpoint_sum_matrix()
        image_gram = matrix_multiply(
            matrix_multiply(transpose(matrix), root_lattice_gram(5)),
            matrix,
        )
        self.assertEqual(image_gram, scalar_matrix_multiply(2, root_lattice_gram(3)))
        self.assertEqual(determinant(image_gram), 32)
        self.assertEqual(saturation_index(), 2)

    def test_normalization_is_torsion_reduced_covolume_ratio(self) -> None:
        self.assertEqual(normalized_covolume_ratio_square(), Fraction(1, 4))

    def test_each_face_contrast_is_the_nontrivial_torsion_class(self) -> None:
        for omitted in VERTICES:
            contrast = face_contrast(omitted)
            self.assertEqual(edge_total(contrast), 0)
            self.assertEqual(matching_sums(contrast), (0, 0, 0))
            self.assertEqual(torsion_bit_on_zero_matching(contrast), 1)
            self.assertEqual(residual_holonomy_sign(contrast), -1)
            lift = face_double_lift(omitted)
            self.assertEqual(sum(lift.values()), 0)
            self.assertEqual(endpoint_sum(lift), scale_edge_state(2, contrast))

    def test_all_face_contrasts_are_one_quotient_class(self) -> None:
        for source, target in combinations(VERTICES, 2):
            difference = add_edge_states(face_contrast(target), face_contrast(source), -1)
            lift = face_difference_lift(source, target)
            self.assertEqual(sum(lift.values()), 0)
            self.assertEqual(endpoint_sum(lift), difference)

    def test_exact_two_beta_factorization(self) -> None:
        for n in range(1, 31):
            self.assertEqual(direct_probability_ratio(n), beta_factorized_ratio(n))

    def test_unique_balance_saddle_certificate(self) -> None:
        certificate = saddle_certificate()
        self.assertEqual(certificate["point"], (Fraction(2, 3), Fraction(1, 2)))
        self.assertEqual(certificate["kernel_value"], 1)
        self.assertEqual(certificate["negative_log_hessian"], ((27, 0), (0, 8)))
        self.assertEqual(certificate["hessian_determinant"], 216)
        self.assertEqual(beta_kernel(Fraction(2, 3), Fraction(1, 2)), 1)

    def test_complete_exact_certificate(self) -> None:
        certificate = exact_certificate(beta_depth=30)
        self.assertEqual(certificate["status"], "PASS")
        self.assertEqual(certificate["residual_torsion_order"], 2)
        self.assertEqual(certificate["normalized_covolume_ratio_square"], Fraction(1, 4))


if __name__ == "__main__":
    unittest.main()
