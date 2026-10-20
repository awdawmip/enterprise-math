import unittest

from enterprise_math.p018_p023_quotient_word_basis import (
    prime_generator_basis,
    prime_generator_required_horizon,
    quotient_word_language_separates_bounded_domain,
)
from enterprise_math.p018_p023_quotient_word_least_phase import (
    composite_omission_witness_alphabet,
    deleted_composite_two_factor_word,
    forced_generator_core_at_horizon,
    least_alphabet_phase,
    least_primitive_generator_alphabet_at_horizon,
    nontrivial_power_free_word_basis,
    omission_witness_is_structurally_valid,
)


def all_subsets(values: tuple[int, ...]):
    for mask in range(1 << len(values)):
        yield tuple(values[i] for i in range(len(values)) if (mask >> i) & 1)


class P018P023QuotientWordLeastPhaseTests(unittest.TestCase):
    def test_horizon_one_least_is_nontrivial_power_free_basis(self):
        for root_exp in range(2, 5):
            for max_state in range(1, 16):
                basis = nontrivial_power_free_word_basis(max_state, root_exp)
                self.assertTrue(
                    quotient_word_language_separates_bounded_domain(
                        max_state, root_exp, basis, 1
                    )
                )
                for omitted in basis:
                    smaller = tuple(x for x in basis if x != omitted)
                    self.assertFalse(
                        quotient_word_language_separates_bounded_domain(
                            max_state, root_exp, smaller, 1
                        )
                    )

    def test_every_composite_can_be_omitted_from_some_horizon_two_separator(self):
        for root_exp in range(2, 6):
            for max_state in range(4, 50):
                for omitted in range(4, max_state + 1):
                    try:
                        left, right = deleted_composite_two_factor_word(omitted)
                    except ValueError:
                        continue
                    alphabet = composite_omission_witness_alphabet(
                        max_state, root_exp, omitted
                    )
                    self.assertNotIn(omitted, alphabet)
                    self.assertTrue(
                        omission_witness_is_structurally_valid(
                            max_state, root_exp, omitted
                        )
                    )
                    self.assertEqual(left * right, omitted)
                    self.assertTrue(
                        quotient_word_language_separates_bounded_domain(
                            max_state, root_exp, alphabet, 2
                        )
                    )

    def test_small_exhaustive_forced_core_and_least_existence(self):
        for root_exp in range(2, 5):
            for max_state in range(1, 9):
                universe = tuple(range(2, max_state + 1))
                for horizon in range(1, 5):
                    separating = [
                        set(generators)
                        for generators in all_subsets(universe)
                        if quotient_word_language_separates_bounded_domain(
                            max_state, root_exp, generators, horizon
                        )
                    ]
                    self.assertTrue(separating)
                    forced = set.intersection(*separating)
                    self.assertEqual(
                        forced,
                        set(
                            forced_generator_core_at_horizon(
                                max_state, root_exp, horizon
                            )
                        ),
                    )
                    predicted = least_primitive_generator_alphabet_at_horizon(
                        max_state, root_exp, horizon
                    )
                    least = [
                        candidate
                        for candidate in separating
                        if all(candidate <= other for other in separating)
                    ]
                    if predicted is None:
                        self.assertEqual(least, [])
                    else:
                        self.assertEqual(least, [set(predicted)])

    def test_intermediate_no_least_examples_exist_for_every_root_order(self):
        examples = ((2, 30), (3, 12), (4, 8), (5, 8))
        for root_exp, max_state in examples:
            required = prime_generator_required_horizon(max_state, root_exp)
            self.assertGreater(required, 2)
            self.assertEqual(
                least_alphabet_phase(max_state, root_exp, 2), "NO_LEAST"
            )
            self.assertIsNone(
                least_primitive_generator_alphabet_at_horizon(
                    max_state, root_exp, 2
                )
            )
            self.assertEqual(
                forced_generator_core_at_horizon(max_state, root_exp, 2),
                prime_generator_basis(max_state),
            )

    def test_prime_phase_begins_at_exact_prime_horizon(self):
        for root_exp in range(2, 7):
            for max_state in range(1, 120):
                required = prime_generator_required_horizon(max_state, root_exp)
                for horizon in range(2, 7):
                    predicted = least_primitive_generator_alphabet_at_horizon(
                        max_state, root_exp, horizon
                    )
                    if horizon >= required:
                        self.assertEqual(predicted, prime_generator_basis(max_state))
                        self.assertEqual(
                            least_alphabet_phase(max_state, root_exp, horizon),
                            "PRIME_LEAST",
                        )
                    else:
                        self.assertIsNone(predicted)
                        self.assertEqual(
                            least_alphabet_phase(max_state, root_exp, horizon),
                            "NO_LEAST",
                        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            nontrivial_power_free_word_basis(10, 1)
        with self.assertRaises(ValueError):
            forced_generator_core_at_horizon(10, 2, 0)
        with self.assertRaises(ValueError):
            composite_omission_witness_alphabet(10, 2, 7)
        with self.assertRaises(ValueError):
            deleted_composite_two_factor_word(1)


if __name__ == "__main__":
    unittest.main()
