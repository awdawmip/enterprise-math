import unittest
from fractions import Fraction

from enterprise_math.safe_operation_information import (
    collision_term_product,
    partial_augmented_collision_factor,
    partial_collision_information_terms,
    partial_collision_terms_reconstruct_probability,
    partial_constraint_zero_reason,
    source_multiplicity_constraint_mass,
    total_collision_factor,
    total_collision_information_terms,
    total_collision_terms_reconstruct_probability,
    total_constraint_zero_reason,
)
from enterprise_math.safe_operation_collision_moments import (
    safe_partial_probability,
    safe_total_probability,
)


def partition_from_sizes(sizes):
    result = {}
    state = 0
    for label, size in enumerate(sizes):
        for _ in range(size):
            result[state] = label
            state += 1
    return result


class SafeOperationInformationTests(unittest.TestCase):
    def test_total_collision_terms_reconstruct_exact_safe_probability(self):
        shapes = (
            (5,),
            (4, 1),
            (3, 2),
            (3, 1, 1),
            (2, 2, 1),
            (1, 1, 1, 1, 1),
            (3, 2, 1),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            terms = total_collision_information_terms(partition)
            self.assertEqual(
                collision_term_product(terms),
                safe_total_probability(partition),
            )
            self.assertTrue(
                total_collision_terms_reconstruct_probability(partition)
            )
            for term in terms:
                self.assertEqual(
                    term.renyi_coefficient,
                    term.source_block_size - 1,
                )
                self.assertFalse(term.augmented_with_undefined)

    def test_partial_augmented_terms_reconstruct_exact_safe_probability(self):
        shapes = (
            (5,),
            (4, 1),
            (3, 2),
            (3, 1, 1),
            (2, 2, 1),
            (1, 1, 1, 1, 1),
            (3, 2, 1),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            terms = partial_collision_information_terms(partition)
            self.assertEqual(
                collision_term_product(terms),
                safe_partial_probability(partition),
            )
            self.assertTrue(
                partial_collision_terms_reconstruct_probability(partition)
            )
            self.assertTrue(
                all(term.augmented_with_undefined for term in terms)
            )

    def test_partial_collision_factor_is_exact_augmented_target_distribution(self):
        partition = partition_from_sizes((3, 2))
        self.assertEqual(
            partial_augmented_collision_factor(partition, 2),
            Fraction(1 + 3**2 + 2**2, 6**2),
        )
        self.assertEqual(
            partial_augmented_collision_factor(partition, 3),
            Fraction(1 + 3**3 + 2**3, 6**3),
        )

    def test_total_endpoint_reconnection_has_two_different_zero_mechanisms(self):
        for n in range(2, 9):
            indiscrete = partition_from_sizes((n,))
            discrete = partition_from_sizes((1,) * n)
            self.assertEqual(
                total_constraint_zero_reason(indiscrete),
                "INDISCRETE_TARGET_ENTROPY_ZERO",
            )
            self.assertEqual(
                total_constraint_zero_reason(discrete),
                "DISCRETE_SOURCE_MULTIPLICITY_ZERO",
            )
            self.assertEqual(safe_total_probability(indiscrete), 1)
            self.assertEqual(safe_total_probability(discrete), 1)

    def test_every_genuine_intermediate_total_partition_has_positive_constraint_term(self):
        shapes = (
            (2, 1),
            (2, 2),
            (3, 1),
            (3, 2),
            (2, 2, 1),
            (4, 1, 1),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            self.assertEqual(
                total_constraint_zero_reason(partition),
                "INTERMEDIATE_POSITIVE_CONSTRAINT",
            )
            terms = total_collision_information_terms(partition)
            self.assertTrue(any(term.contributes_constraint for term in terms))

    def test_partial_indiscrete_endpoint_stays_constrained_because_undefined_is_visible(self):
        for n in range(2, 9):
            indiscrete = partition_from_sizes((n,))
            discrete = partition_from_sizes((1,) * n)
            self.assertLess(safe_partial_probability(indiscrete), 1)
            self.assertEqual(
                partial_constraint_zero_reason(indiscrete),
                "POSITIVE_CONSTRAINT",
            )
            term = partial_collision_information_terms(indiscrete)[0]
            self.assertGreater(term.renyi_coefficient, 0)
            self.assertLess(term.collision_factor, 1)

            self.assertEqual(safe_partial_probability(discrete), 1)
            self.assertEqual(
                partial_constraint_zero_reason(discrete),
                "DISCRETE_SOURCE_MULTIPLICITY_ZERO",
            )

    def test_source_multiplicity_mass_is_n_minus_block_count(self):
        shapes = (
            (5,),
            (4, 1),
            (3, 2),
            (2, 2, 1),
            (1, 1, 1, 1, 1),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            expected = sum(shape) - len(shape)
            self.assertEqual(
                source_multiplicity_constraint_mass(
                    total_collision_information_terms(partition)
                ),
                expected,
            )
            self.assertEqual(
                source_multiplicity_constraint_mass(
                    partial_collision_information_terms(partition)
                ),
                expected,
            )

    def test_order_one_collision_factor_is_one_only_for_total_distribution(self):
        partition = partition_from_sizes((3, 2, 1))
        self.assertEqual(total_collision_factor(partition, 1), 1)
        # The augmented partial target probabilities still sum to one, so order
        # one is also exactly one; the endpoint asymmetry comes from source
        # block size >1 at the indiscrete partition, not from broken normalization.
        self.assertEqual(partial_augmented_collision_factor(partition, 1), 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            total_collision_factor({}, 2)
        with self.assertRaises(ValueError):
            total_collision_factor({0: 0}, 0)
        with self.assertRaises(TypeError):
            partial_augmented_collision_factor({0: 0}, True)


if __name__ == "__main__":
    unittest.main()
