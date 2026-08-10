import unittest
from itertools import product

from enterprise_math.precision_relation_rank_compiler import (
    compile_relation_rank_state,
    full_translation_relation_class_count,
    induced_relation_actions,
    matrix_rank_mod_prime,
    relation_matrix_is_surjective,
    relation_rank_class_count,
    relation_rank_partition_is_exact,
    relation_vector,
    representation_exponent_codimension,
)


class PrecisionRelationRankCompilerTests(unittest.TestCase):
    def test_matrix_rank_mod_prime_detects_relation_rank(self):
        self.assertEqual(matrix_rank_mod_prime(((1, -1),), 2), 1)
        self.assertEqual(matrix_rank_mod_prime(((1, 0, 1), (0, 1, 1)), 2), 2)
        self.assertEqual(matrix_rank_mod_prime(((2, 0),), 2), 0)
        self.assertTrue(relation_matrix_is_surjective(((1, 0, 1), (0, 1, 1)), 2))
        self.assertFalse(relation_matrix_is_surjective(((2, 0),), 2))

    def test_relation_vector_and_induced_actions_are_linear(self):
        matrix = ((1, -1),)
        prime = 2
        cap = 3
        self.assertEqual(relation_vector((6, 1), matrix, prime, cap), (5,))
        actions = ((0, 0), (1, 0), (0, 2), (3, 5))
        self.assertEqual(
            induced_relation_actions(actions, matrix, prime, cap),
            tuple(sorted({(0,), (1,), (6,)})),
        )

    def test_rank_one_difference_compiler_matches_literal_product_future(self):
        actions = ((0, 0), (1, 0), (0, 1))
        self.assertTrue(
            relation_rank_partition_is_exact(
                actions, ((1, -1),), 2, 2
            )
        )

    def test_rank_two_relation_compiler_matches_literal_product_future(self):
        matrix = ((1, 0, 1), (0, 1, 1))
        actions = (
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        self.assertTrue(relation_rank_partition_is_exact(actions, matrix, 2, 1))
        self.assertTrue(relation_rank_partition_is_exact(actions, matrix, 2, 2))

    def test_full_translation_complexity_depends_on_relation_rank(self):
        prime = 2
        cap = 3
        modulus = prime**cap

        rank_one_matrix = ((1, -1),)
        rank_one_actions = tuple(product(range(modulus), repeat=2))
        self.assertEqual(
            full_translation_relation_class_count(rank_one_matrix, prime, cap),
            8,
        )
        self.assertEqual(
            relation_rank_class_count(
                rank_one_actions, rank_one_matrix, prime, cap
            ),
            8,
        )
        self.assertEqual(representation_exponent_codimension(2, 1, cap), 3)

        rank_two_matrix = ((1, 0, 1), (0, 1, 1))
        self.assertEqual(
            full_translation_relation_class_count(rank_two_matrix, prime, cap),
            64,
        )
        self.assertEqual(representation_exponent_codimension(3, 2, cap), 3)

    def test_full_translation_relation_rank_formula_is_p_power(self):
        for prime, cap, ambient, rank in (
            (2, 2, 3, 1),
            (2, 2, 3, 2),
            (3, 2, 4, 2),
            (5, 1, 3, 1),
        ):
            matrix = tuple(
                tuple(1 if column == row else 0 for column in range(ambient))
                for row in range(rank)
            )
            self.assertEqual(
                full_translation_relation_class_count(matrix, prime, cap),
                prime ** (cap * rank),
            )
            self.assertEqual(
                representation_exponent_codimension(ambient, rank, cap),
                cap * (ambient - rank),
            )

    def test_equal_relation_state_gets_equal_compiled_token(self):
        matrix = ((1, -1),)
        actions = ((0, 0), (1, 0))
        left = (0, 0)
        right = (1, 1)
        self.assertEqual(relation_vector(left, matrix, 2, 2), (0,))
        self.assertEqual(relation_vector(right, matrix, 2, 2), (0,))
        self.assertEqual(
            compile_relation_rank_state(left, actions, matrix, 2, 2),
            compile_relation_rank_state(right, actions, matrix, 2, 2),
        )

    def test_rank_deficient_matrix_fails_closed_for_exact_count(self):
        matrix = ((2, 0),)
        with self.assertRaises(ValueError):
            relation_rank_class_count(((0, 0),), matrix, 2, 3)
        with self.assertRaises(ValueError):
            full_translation_relation_class_count(matrix, 2, 3)


if __name__ == "__main__":
    unittest.main()
