import itertools
import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p018_p023_power_free_action_basis import (
    is_r_power_free,
    minimal_root_quotient_action_basis,
)
from enterprise_math.p018_p023_quotient_word_basis import (
    binary_present_observation_regime,
    minimal_r_power_free_for_omega,
    omega_with_multiplicity,
    prime_generator_basis,
    prime_generator_required_horizon,
    prime_generator_required_horizon_via_packing,
    quotient_word_language_covers_power_free_boundaries,
    quotient_word_language_separates_bounded_domain,
    quotient_word_product,
    quotient_word_state,
    reachable_quotient_products,
)


def words_over(generators: tuple[int, ...], horizon: int):
    yield ()
    for length in range(1, horizon + 1):
        yield from itertools.product(generators, repeat=length)


def literal_word_language_separates(
    max_state: int, root_exp: int, generators: tuple[int, ...], horizon: int
) -> bool:
    words = tuple(words_over(generators, horizon))
    signatures = []
    for q in range(max_state + 1):
        signature = tuple(
            integer_nth_root(quotient_word_state(q, word), root_exp)
            for word in words
        )
        signatures.append(signature)
    return len(signatures) == len(set(signatures))


class P018P023QuotientWordBasisTests(unittest.TestCase):
    def test_literal_word_flattens_to_product_denominator(self):
        for q in range(0, 80):
            for word in words_over((2, 3, 5), 3):
                product = quotient_word_product(word)
                self.assertEqual(quotient_word_state(q, word), q // product)

    def test_exact_criterion_matches_literal_word_signatures(self):
        universe = (2, 3, 4, 5, 6)
        for root_exp in range(1, 4):
            for max_state in range(1, 7):
                available = tuple(a for a in universe if a <= max_state)
                for horizon in range(0, 3):
                    for mask in range(1 << len(available)):
                        generators = tuple(
                            available[i]
                            for i in range(len(available))
                            if (mask >> i) & 1
                        )
                        literal = literal_word_language_separates(
                            max_state, root_exp, generators, horizon
                        )
                        criterion = quotient_word_language_covers_power_free_boundaries(
                            max_state, root_exp, generators, horizon
                        )
                        effective = quotient_word_language_separates_bounded_domain(
                            max_state, root_exp, generators, horizon
                        )
                        self.assertEqual(literal, criterion)
                        self.assertEqual(effective, criterion)

    def test_empty_word_supplies_effective_action_one(self):
        self.assertEqual(reachable_quotient_products((), 0, max_product=10), (1,))
        for root_exp in range(1, 5):
            for max_state in range(1, 20):
                canonical = set(
                    minimal_root_quotient_action_basis(max_state, root_exp)
                )
                primitive_one_step = tuple(sorted(canonical - {1}))
                effective = set(
                    reachable_quotient_products(
                        primitive_one_step, 1, max_product=max_state
                    )
                )
                self.assertTrue(canonical <= effective)
                self.assertTrue(
                    quotient_word_language_separates_bounded_domain(
                        max_state, root_exp, primitive_one_step, 1
                    )
                )

    def test_prime_generator_horizon_is_exact(self):
        for root_exp in range(2, 5):
            for max_state in range(2, 60):
                primes = prime_generator_basis(max_state)
                horizon = prime_generator_required_horizon(max_state, root_exp)
                self.assertTrue(
                    quotient_word_language_separates_bounded_domain(
                        max_state, root_exp, primes, horizon
                    )
                )
                if horizon > 1:
                    self.assertFalse(
                        quotient_word_language_separates_bounded_domain(
                            max_state, root_exp, primes, horizon - 1
                        )
                    )

    def test_power_free_omega_packing_matches_direct_horizon(self):
        for root_exp in range(2, 7):
            for max_state in range(1, 500):
                self.assertEqual(
                    prime_generator_required_horizon_via_packing(
                        max_state, root_exp
                    ),
                    prime_generator_required_horizon(max_state, root_exp),
                )

    def test_minimal_packing_representative_has_requested_omega(self):
        for root_exp in range(2, 7):
            for total_omega in range(0, 14):
                candidate = minimal_r_power_free_for_omega(
                    total_omega, root_exp
                )
                self.assertEqual(
                    omega_with_multiplicity(candidate), total_omega
                )
                self.assertTrue(is_r_power_free(candidate, root_exp))
                # Full-prefix minimality is reserved for genuinely small cases;
                # large primorial-scale candidates are validated instead by the
                # independent horizon-vs-direct scan above.
                if candidate <= 2000:
                    for smaller in range(1, candidate):
                        if omega_with_multiplicity(smaller) == total_omega:
                            self.assertFalse(is_r_power_free(smaller, root_exp))

    def test_binary_present_observation_can_require_full_one_step_basis(self):
        root_exp = 4
        max_state = 10
        self.assertTrue(binary_present_observation_regime(max_state, root_exp))
        observed = {
            integer_nth_root(q, root_exp) for q in range(max_state + 1)
        }
        self.assertEqual(observed, {0, 1})
        self.assertEqual(
            minimal_root_quotient_action_basis(max_state, root_exp),
            tuple(range(1, max_state + 1)),
        )

        primes = prime_generator_basis(max_state)
        self.assertFalse(
            quotient_word_language_separates_bounded_domain(
                max_state, root_exp, primes, 1
            )
        )
        horizon = prime_generator_required_horizon(max_state, root_exp)
        self.assertTrue(
            quotient_word_language_separates_bounded_domain(
                max_state, root_exp, primes, horizon
            )
        )

    def test_binary_present_regime_has_exact_log2_prime_horizon(self):
        for root_exp in range(2, 8):
            for max_state in range(1, 2**root_exp):
                self.assertTrue(
                    binary_present_observation_regime(max_state, root_exp)
                )
                self.assertEqual(
                    prime_generator_required_horizon(max_state, root_exp),
                    max_state.bit_length() - 1,
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            quotient_word_state(-1, ())
        with self.assertRaises(ValueError):
            quotient_word_state(5, (0,))
        with self.assertRaises(ValueError):
            reachable_quotient_products((2,), -1)
        with self.assertRaises(ValueError):
            prime_generator_required_horizon(10, 0)
        with self.assertRaises(ValueError):
            minimal_r_power_free_for_omega(1, 1)


if __name__ == "__main__":
    unittest.main()
