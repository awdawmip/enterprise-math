import unittest

from enterprise_math.matrix_access_word_norm import (
    matrix_access_radius,
    matrix_image_at_radius,
    minkowski_radius_law_holds,
    one_step_image,
    relation_subgroup_one_step_failure_counterexample,
    repeated_one_step_image,
    word_norm_triangle_holds,
)
from enterprise_math.relation_shared_prime_rank import derivative_coefficient_matrix


class MatrixAccessWordNormTests(unittest.TestCase):
    def test_single_shared_prime_line_is_word_norm(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((4, 8))
        self.assertEqual(matrix, ((4,), (12,)))
        self.assertEqual(
            one_step_image(matrix),
            frozenset({(-4, -12), (0, 0), (4, 12)}),
        )
        self.assertEqual(matrix_access_radius(matrix, (4, 12), max_radius=1), 1)
        self.assertEqual(matrix_access_radius(matrix, (8, 24), max_radius=2), 2)

    def test_exact_minkowski_radius_law(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 4, 6))
        for r in range(4):
            for s in range(4):
                self.assertTrue(minkowski_radius_law_holds(matrix, r, s))
                self.assertEqual(
                    matrix_image_at_radius(matrix, r + s),
                    repeated_one_step_image(matrix, r + s),
                )

    def test_shared_prime_joint_access_rejects_false_separate_state(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 4, 6))
        self.assertEqual(matrix_access_radius(matrix, (1, 4, 5), max_radius=1), 1)
        with self.assertRaises(ValueError):
            matrix_access_radius(matrix, (0, 4, 4), max_radius=5)

    def test_word_norm_triangle_inequality(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 4, 6))
        self.assertTrue(
            word_norm_triangle_holds(
                matrix,
                (1, 4, 5),
                (-1, -4, -1),
                max_radius=2,
            )
        )

    def test_relation_subgroup_need_not_be_generated_at_radius_one(self) -> None:
        data = relation_subgroup_one_step_failure_counterexample()
        self.assertEqual(data["blocks"], (2, 4, 6))
        self.assertEqual(data["relation"], (4, 1, -2))
        self.assertEqual(data["relation_derivative_row"], (2, -4))
        self.assertEqual(data["radius_one_relation_image"], ((0, 0, 0),))
        self.assertEqual(data["radius_two_target"], (2, 8, 8))
        self.assertEqual(data["ambient_access_radius"], 2)

    def test_prime_coprime_matrix_calibration(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((6, 35, 41))
        self.assertEqual(matrix_access_radius(matrix, (3, -1, 2), max_radius=2), 2)
        self.assertTrue(minkowski_radius_law_holds(matrix, 2, 3))


if __name__ == "__main__":
    unittest.main()
