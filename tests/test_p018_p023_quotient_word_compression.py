import itertools
import unittest

from enterprise_math.p018_p023_quotient_word_basis import (
    omega_with_multiplicity,
    prime_generator_basis,
    prime_generator_required_horizon,
    quotient_word_language_separates_bounded_domain,
)
from enterprise_math.p018_p023_quotient_word_compression import (
    binary_penultimate_single_macro_solutions,
    direct_prime_macro_separator,
    maximal_omega_power_free_boundaries,
    max_macro_compression,
    minimum_penultimate_semiprime_cover,
    omega_filtered_macro_alphabet,
    omega_filtered_boundary_word_length,
    omega_filtered_required_horizon,
    omega_filtered_separates_at_horizon,
    penultimate_minimum_extra_count,
    power_free_semiprime_candidates,
    prime_macro_language_separates_at_horizon,
    semiprime_covers_maximal_boundaries,
    shortest_prime_macro_word_length,
)
from enterprise_math.p018_p023_power_free_action_basis import (
    minimal_root_quotient_action_basis,
)


def all_subsets(values: tuple[int, ...]):
    for mask in range(1 << len(values)):
        yield tuple(values[i] for i in range(len(values)) if (mask >> i) & 1)


def direct_shortest_product_length(boundary: int, macros: tuple[int, ...]) -> int:
    generators = tuple(
        p for p in prime_generator_basis(boundary)
    ) + tuple(g for g in macros if g <= boundary)
    distances = {1: 0}
    frontier = {1}
    for depth in range(1, omega_with_multiplicity(boundary) + 1):
        frontier = {
            product * generator
            for product in frontier
            for generator in generators
            if boundary % (product * generator) == 0
        }
        for product in frontier:
            distances.setdefault(product, depth)
        if boundary in distances:
            return distances[boundary]
    raise AssertionError("prime generators always factor the boundary")


class P018P023QuotientWordCompressionTests(unittest.TestCase):
    def test_exact_compression_formula_matches_direct_factor_words(self):
        for boundary in range(2, 70):
            composites = tuple(
                value
                for value in range(4, boundary + 1)
                if value not in prime_generator_basis(boundary)
            )
            sample = composites[:5]
            for macros in all_subsets(sample):
                self.assertEqual(
                    shortest_prime_macro_word_length(boundary, macros),
                    direct_shortest_product_length(boundary, macros),
                )
                self.assertLessEqual(
                    max_macro_compression(boundary, macros),
                    omega_with_multiplicity(boundary) - 1,
                )

    def test_packing_separator_matches_literal_product_bridge(self):
        for root_exp in range(2, 5):
            for max_state in range(1, 13):
                composites = tuple(
                    value
                    for value in range(4, max_state + 1)
                    if value not in prime_generator_basis(max_state)
                )
                sample = composites[:4]
                for horizon in range(1, 4):
                    for macros in all_subsets(sample):
                        packing = prime_macro_language_separates_at_horizon(
                            max_state, root_exp, macros, horizon
                        )
                        literal = direct_prime_macro_separator(
                            max_state, root_exp, macros, horizon
                        )
                        self.assertEqual(packing, literal)

    def test_penultimate_semiprime_cover_matches_bruteforce_extra_count(self):
        for root_exp in range(2, 5):
            for max_state in range(2, 14):
                level = prime_generator_required_horizon(max_state, root_exp)
                if level <= 1:
                    self.assertEqual(
                        penultimate_minimum_extra_count(max_state, root_exp), 0
                    )
                    continue
                horizon = level - 1
                composites = tuple(
                    value
                    for value in range(4, max_state + 1)
                    if value not in prime_generator_basis(max_state)
                )
                brute = None
                for size in range(len(composites) + 1):
                    if any(
                        prime_macro_language_separates_at_horizon(
                            max_state, root_exp, chosen, horizon
                        )
                        for chosen in itertools.combinations(composites, size)
                    ):
                        brute = size
                        break
                self.assertIsNotNone(brute)
                cover = minimum_penultimate_semiprime_cover(
                    max_state, root_exp
                )
                self.assertEqual(len(cover), brute)
                self.assertTrue(
                    semiprime_covers_maximal_boundaries(
                        max_state, root_exp, cover
                    )
                )
                self.assertTrue(set(cover) <= set(
                    power_free_semiprime_candidates(max_state, root_exp)
                ))

    def test_binary_penultimate_single_macro_classification(self):
        for max_state in range(8, 100):
            root_exp = max_state.bit_length()
            self.assertLess(max_state, 2**root_exp)
            level = max_state.bit_length() - 1
            horizon = level - 1
            predicted = binary_penultimate_single_macro_solutions(
                max_state, root_exp
            )
            actual = tuple(
                macro
                for macro in range(4, max_state + 1)
                if macro not in prime_generator_basis(max_state)
                and prime_macro_language_separates_at_horizon(
                    max_state, root_exp, (macro,), horizon
                )
            )
            self.assertEqual(predicted, actual)
            self.assertEqual(
                penultimate_minimum_extra_count(max_state, root_exp), 1
            )

    def test_binary_maximal_omega_boundary_shape(self):
        for max_state in range(8, 150):
            root_exp = max_state.bit_length()
            level = max_state.bit_length() - 1
            expected = [2**level]
            second = 3 * 2 ** (level - 1)
            if second <= max_state:
                expected.append(second)
            self.assertEqual(
                maximal_omega_power_free_boundaries(max_state, root_exp),
                tuple(expected),
            )

    def test_macro_four_reduces_binary_prime_horizon_by_one(self):
        for max_state in range(8, 150):
            root_exp = max_state.bit_length()
            level = prime_generator_required_horizon(max_state, root_exp)
            self.assertEqual(level, max_state.bit_length() - 1)
            self.assertFalse(
                quotient_word_language_separates_bounded_domain(
                    max_state,
                    root_exp,
                    prime_generator_basis(max_state),
                    level - 1,
                )
            )
            self.assertTrue(
                prime_macro_language_separates_at_horizon(
                    max_state, root_exp, (4,), level - 1
                )
            )

    def test_omega_filtration_exact_word_lengths(self):
        for root_exp in range(2, 6):
            for max_state in range(2, 45):
                level = prime_generator_required_horizon(max_state, root_exp)
                for capacity in range(1, max(2, level + 1)):
                    alphabet = omega_filtered_macro_alphabet(
                        max_state, root_exp, capacity
                    )
                    macros = tuple(
                        g
                        for g in alphabet
                        if g not in prime_generator_basis(max_state)
                    )
                    for boundary in minimal_root_quotient_action_basis(
                        max_state, root_exp
                    ):
                        if boundary == 1:
                            continue
                        direct = direct_shortest_product_length(
                            boundary, macros
                        )
                        self.assertEqual(
                            direct,
                            omega_filtered_boundary_word_length(
                                boundary, capacity
                            ),
                        )

    def test_omega_filtration_exact_storage_depth_product_law(self):
        for root_exp in range(2, 6):
            for max_state in range(1, 50):
                level = prime_generator_required_horizon(max_state, root_exp)
                for capacity in range(1, max(2, level + 2)):
                    alphabet = omega_filtered_macro_alphabet(
                        max_state, root_exp, capacity
                    )
                    predicted_horizon = omega_filtered_required_horizon(
                        max_state, root_exp, capacity
                    )
                    self.assertEqual(
                        predicted_horizon,
                        (level + capacity - 1) // capacity,
                    )
                    for horizon in range(0, predicted_horizon + 2):
                        direct = quotient_word_language_separates_bounded_domain(
                            max_state,
                            root_exp,
                            alphabet,
                            horizon,
                        )
                        self.assertEqual(
                            direct,
                            omega_filtered_separates_at_horizon(
                                max_state,
                                root_exp,
                                capacity,
                                horizon,
                            ),
                        )

    def test_omega_filtration_endpoints(self):
        for root_exp in range(2, 6):
            for max_state in range(2, 60):
                level = prime_generator_required_horizon(max_state, root_exp)
                self.assertEqual(
                    omega_filtered_macro_alphabet(max_state, root_exp, 1),
                    prime_generator_basis(max_state),
                )
                if level > 0:
                    self.assertEqual(
                        omega_filtered_macro_alphabet(
                            max_state, root_exp, level
                        ),
                        tuple(
                            b
                            for b in minimal_root_quotient_action_basis(
                                max_state, root_exp
                            )
                            if b >= 2
                        ),
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            shortest_prime_macro_word_length(10, (3,))
        with self.assertRaises(ValueError):
            binary_penultimate_single_macro_solutions(7, 4)
        with self.assertRaises(ValueError):
            binary_penultimate_single_macro_solutions(20, 4)
        with self.assertRaises(ValueError):
            semiprime_covers_maximal_boundaries(20, 4, (8,))


if __name__ == "__main__":
    unittest.main()
