import unittest
from itertools import product

from enterprise_math.precision_relation_language_compiler import (
    compile_relation_future_state,
    induced_relation_translations,
    relation_compiled_class_count,
    relation_compiler_partition_is_exact,
    relation_future_signature,
    relation_is_surjective,
    relation_value,
)


class PrecisionRelationLanguageCompilerTests(unittest.TestCase):
    def test_difference_relation_turns_joint_translation_into_one_axis_translation(self):
        prime = 2
        cap = 3
        coefficients = (1, -1)
        actions = ((0, 0), (1, 0), (0, 2), (3, 5))
        induced = induced_relation_translations(actions, coefficients, prime, cap)
        expected = tuple(sorted({0, 1, -2 % 8, (3 - 5) % 8}))
        self.assertEqual(induced, expected)

        state = (6, 1)
        relation = relation_value(state, coefficients, prime, cap)
        self.assertEqual(relation, 5)
        self.assertEqual(
            compile_relation_future_state(state, actions, coefficients, prime, cap),
            compile_relation_future_state((5, 0), actions, coefficients, prime, cap),
        )

    def test_relation_compiler_matches_literal_joint_future_signature(self):
        examples = (
            (2, 2, (1, -1), ((0, 0), (1, 0), (0, 1))),
            (2, 3, (1, 1), ((0, 0), (1, 1), (2, 0), (0, 4))),
            (3, 2, (1, -1), ((0, 0), (1, 0), (0, 3), (4, 2))),
            (2, 2, (1, 1, -1), ((0, 0, 0), (1, 0, 0), (0, 1, 1))),
        )
        for prime, cap, coefficients, actions in examples:
            self.assertTrue(
                relation_compiler_partition_is_exact(
                    actions, coefficients, prime, cap
                )
            )

    def test_full_joint_translation_product_can_collapse_to_one_relation_axis(self):
        prime = 2
        cap = 3
        modulus = prime**cap
        coefficients = (1, -1)
        actions = tuple(product(range(modulus), repeat=2))
        self.assertEqual(len(actions), 64)
        self.assertEqual(
            induced_relation_translations(actions, coefficients, prime, cap),
            tuple(range(modulus)),
        )
        self.assertEqual(
            relation_compiled_class_count(actions, coefficients, prime, cap),
            modulus,
        )
        self.assertTrue(
            relation_compiler_partition_is_exact(
                actions, coefficients, prime, cap
            )
        )

    def test_relation_factorization_merges_states_with_same_relation_future(self):
        prime = 2
        cap = 2
        coefficients = (1, -1)
        actions = ((0, 0), (1, 0))
        left = (0, 0)
        right = (1, 1)
        self.assertEqual(
            relation_value(left, coefficients, prime, cap),
            relation_value(right, coefficients, prime, cap),
        )
        self.assertEqual(
            relation_future_signature(left, actions, coefficients, prime, cap),
            relation_future_signature(right, actions, coefficients, prime, cap),
        )
        self.assertEqual(
            compile_relation_future_state(left, actions, coefficients, prime, cap),
            compile_relation_future_state(right, actions, coefficients, prime, cap),
        )

    def test_surjectivity_requires_a_p_unit_coefficient(self):
        self.assertTrue(relation_is_surjective((1, 2), 2))
        self.assertTrue(relation_is_surjective((3, 6), 2))
        self.assertFalse(relation_is_surjective((2, 4), 2))
        with self.assertRaises(ValueError):
            relation_compiled_class_count(((0, 0),), (2, 4), 2, 3)


if __name__ == "__main__":
    unittest.main()
