import itertools
import unittest

from enterprise_math.p018_p023_quotient_word_basis import (
    prime_generator_basis,
    quotient_word_language_separates_bounded_domain,
)
from enterprise_math.p018_p023_quotient_word_storage import (
    minimum_composite_storage_count,
    minimum_storage_alphabets,
    minimum_storage_size,
    multiplicative_partitions_within_horizon,
    normalized_alphabet_satisfies_storage_constraints,
    semantic_storage_candidates,
    storage_oracle_matches_literal_separator,
)


def all_subsets(values: tuple[int, ...]):
    for mask in range(1 << len(values)):
        yield tuple(values[i] for i in range(len(values)) if (mask >> i) & 1)


class P018P023QuotientWordStorageTests(unittest.TestCase):
    def test_multiplicative_partition_dnf_for_twelve(self):
        candidates = semantic_storage_candidates(12, 3)
        partitions = set(
            multiplicative_partitions_within_horizon(12, 3, candidates)
        )
        self.assertEqual(
            partitions,
            {
                (12,),
                (2, 6),
                (3, 4),
                (2, 2, 3),
            },
        )

    def test_partition_oracle_matches_literal_word_bridge_on_small_domains(self):
        for root_exp in range(2, 5):
            for max_state in range(1, 10):
                candidates = semantic_storage_candidates(max_state, root_exp)
                for horizon in range(0, 4):
                    for alphabet in all_subsets(candidates):
                        self.assertTrue(
                            storage_oracle_matches_literal_separator(
                                max_state, root_exp, alphabet, horizon
                            )
                        )

    def test_normalized_constraint_checker_matches_literal_separator(self):
        max_state = 12
        root_exp = 3
        horizon = 2
        for alphabet in (
            (2, 3, 4, 5, 7, 11),
            (2, 3, 5, 6, 7, 11),
            (2, 3, 5, 7, 11, 12),
            (2, 3, 5, 7, 11),
        ):
            self.assertEqual(
                normalized_alphabet_satisfies_storage_constraints(
                    max_state, root_exp, alphabet, horizon
                ),
                quotient_word_language_separates_bounded_domain(
                    max_state, root_exp, alphabet, horizon
                ),
            )

    def test_intermediate_phase_has_multiple_minimum_storage_optima(self):
        # Here L_3(12)=3 and h=2, so the fixed-horizon inclusion order has no
        # least separator.  Minimum cardinality nevertheless exists and has
        # three distinct optima.
        solutions = minimum_storage_alphabets(12, 3, 2)
        self.assertEqual(
            set(solutions),
            {
                (2, 3, 4, 5, 7, 11),
                (2, 3, 5, 6, 7, 11),
                (2, 3, 5, 7, 11, 12),
            },
        )
        self.assertEqual(minimum_storage_size(12, 3, 2), 6)
        self.assertEqual(minimum_composite_storage_count(12, 3, 2), 1)

    def test_adequate_horizon_collapses_storage_optimum_to_primes(self):
        self.assertEqual(
            minimum_storage_alphabets(12, 3, 3),
            (prime_generator_basis(12),),
        )
        self.assertEqual(minimum_storage_size(12, 3, 3), 5)
        self.assertEqual(minimum_composite_storage_count(12, 3, 3), 0)

    def test_zero_horizon_trivial_and_nontrivial_domains(self):
        self.assertEqual(minimum_storage_alphabets(1, 3, 0), ((),))
        self.assertEqual(minimum_storage_size(1, 3, 0), 0)
        self.assertEqual(minimum_storage_alphabets(2, 3, 0), ())
        self.assertIsNone(minimum_storage_size(2, 3, 0))

    def test_forced_prime_core_is_present_in_every_minimum(self):
        for root_exp in range(2, 5):
            for max_state in range(2, 13):
                primes = set(prime_generator_basis(max_state))
                for horizon in range(1, 4):
                    solutions = minimum_storage_alphabets(
                        max_state, root_exp, horizon, max_solutions=8
                    )
                    for alphabet in solutions:
                        self.assertTrue(primes <= set(alphabet))


if __name__ == "__main__":
    unittest.main()
