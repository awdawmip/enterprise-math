import unittest

from enterprise_math.relation_shared_prime_rank import (
    derivative_coefficient_matrix,
    derivative_values_from_fine_coordinates,
    fine_coordinates_are_relation_adapted,
    individual_block_ideal_relation_membership,
    shared_prime_independence_counterexample,
    shared_prime_relation_system,
)


class RelationSharedPrimeRankTests(unittest.TestCase):
    def test_shared_prime_246_rank_is_one(self) -> None:
        system = shared_prime_relation_system((2, 4, 6), ((1, 1, -1),))
        self.assertEqual(system.prime_coordinates, (2, 3))
        self.assertEqual(
            system.derivative_matrix,
            ((1, 0), (4, 0), (3, 2)),
        )
        self.assertEqual(system.relation_derivative_matrix, ((2, -2),))
        self.assertEqual(system.derivative_rank, 2)
        self.assertEqual(system.relation_derivative_rank, 1)
        self.assertEqual(system.compressed_rank, 1)

        self.assertTrue(fine_coordinates_are_relation_adapted(system, (1, 1)))
        self.assertEqual(derivative_values_from_fine_coordinates(system, (1, 1)), (1, 4, 5))
        self.assertFalse(fine_coordinates_are_relation_adapted(system, (1, 0)))

    def test_pairwise_coprime_case_recovers_stage26_rank(self) -> None:
        system = shared_prime_relation_system((6, 35, 41), ((1, 1, -1),))
        self.assertEqual(system.prime_coordinates, (2, 3, 5, 7, 41))
        self.assertEqual(system.derivative_rank, 3)
        self.assertEqual(system.relation_derivative_rank, 1)
        self.assertEqual(system.compressed_rank, 2)

    def test_no_relation_shared_blocks_can_already_have_reduced_rank(self) -> None:
        system = shared_prime_relation_system((4, 8), ())
        self.assertEqual(system.prime_coordinates, (2,))
        self.assertEqual(system.derivative_matrix, ((4,), (12,)))
        self.assertEqual(system.derivative_rank, 1)
        self.assertEqual(system.relation_derivative_rank, 0)
        self.assertEqual(system.compressed_rank, 1)

    def test_separate_block_ideals_create_false_state(self) -> None:
        data = shared_prime_independence_counterexample()
        self.assertEqual(data["blocks"], (2, 4, 6))
        self.assertEqual(data["compressed_rank"], 1)
        self.assertEqual(data["false_separate_ideal_state"], (0, 4, 4))
        self.assertTrue(
            individual_block_ideal_relation_membership(
                (2, 4, 6),
                ((1, 1, -1),),
                (0, 4, 4),
            )
        )

    def test_derivative_matrix_for_mixed_exponents(self) -> None:
        primes, matrix = derivative_coefficient_matrix((8, 9, 17))
        self.assertEqual(primes, (2, 3, 17))
        self.assertEqual(matrix, ((12, 0, 0), (0, 6, 0), (0, 0, 1)))
        system = shared_prime_relation_system((8, 9, 17), ((1, 1, -1),))
        self.assertEqual(system.compressed_rank, 2)

    def test_invalid_relation_rejected(self) -> None:
        with self.assertRaises(ValueError):
            shared_prime_relation_system((2, 4, 6), ((1, -1, 0),))


if __name__ == "__main__":
    unittest.main()
