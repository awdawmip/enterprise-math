import unittest
from itertools import combinations

from enterprise_math.precision_product_language_factorization import (
    BIT_ACTIONS,
    coupled_and_observable,
    coupled_correlation_counterexample,
    full_product_observable,
    full_vector_factorization_holds,
    marginal_action_sets,
    product_of_marginal_partitions,
    signature_partition,
)


class PrecisionProductLanguageFactorizationTests(unittest.TestCase):
    def test_full_product_observation_factorizes_for_every_nonempty_bit_action_set(self):
        for size in range(1, len(BIT_ACTIONS) + 1):
            for actions in combinations(BIT_ACTIONS, size):
                self.assertTrue(full_vector_factorization_holds(actions))
                self.assertEqual(
                    signature_partition(actions, full_product_observable),
                    product_of_marginal_partitions(actions),
                )

    def test_coupled_observation_makes_joint_action_correlation_visible(self):
        diagonal = ((0, 0), (1, 1))
        cross = ((0, 1), (1, 0))
        self.assertEqual(len(diagonal), len(cross))
        self.assertEqual(marginal_action_sets(diagonal), marginal_action_sets(cross))

        diagonal_partition = signature_partition(diagonal, coupled_and_observable)
        cross_partition = signature_partition(cross, coupled_and_observable)

        self.assertEqual(
            diagonal_partition,
            frozenset(
                {
                    frozenset({(0, 0)}),
                    frozenset({(0, 1), (1, 0)}),
                    frozenset({(1, 1)}),
                }
            ),
        )
        self.assertEqual(
            cross_partition,
            frozenset(
                {
                    frozenset({(0, 0), (1, 1)}),
                    frozenset({(0, 1)}),
                    frozenset({(1, 0)}),
                }
            ),
        )
        self.assertNotEqual(diagonal_partition, cross_partition)

    def test_counterexample_helper_preserves_same_marginals_and_count(self):
        left, right = coupled_correlation_counterexample()
        self.assertNotEqual(left, right)
        self.assertEqual(len(left), 3)
        self.assertEqual(len(right), 3)

    def test_full_vector_and_coupled_observation_have_different_factorization_behavior(self):
        actions = ((0, 0), (1, 1))
        self.assertTrue(full_vector_factorization_holds(actions))
        self.assertNotEqual(
            signature_partition(actions, coupled_and_observable),
            product_of_marginal_partitions(actions),
        )


if __name__ == "__main__":
    unittest.main()
