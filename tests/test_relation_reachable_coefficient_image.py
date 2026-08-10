import itertools
import unittest

from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    modular_semiring,
    product_semiring,
    words_through_horizon,
)
from enterprise_math.relation_local_count_code_capacity import (
    finite_code_capacity,
    natural_code_injective_through,
)
from enterprise_math.relation_reachable_coefficient_image import (
    boolean_modular_carrier_report,
    boolean_modular_natural_image,
    boolean_modular_product_elements,
    boolean_modular_reachable_carrier_size,
    modular_product_carrier_report,
    modular_product_full_carrier_size,
    modular_product_natural_image_size,
    natural_image_is_closed_on_samples,
    zero_aware_and_full_boolean_modular_branching_agree,
    zero_aware_and_full_boolean_modular_traces_agree,
    zero_aware_modular_elements,
    zero_aware_modular_semiring,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


class RelationReachableCoefficientImageTests(unittest.TestCase):
    def test_zero_aware_elements_equal_boolean_modular_natural_image(self):
        for modulus in range(2, 9):
            zero_aware = set(zero_aware_modular_elements(modulus))
            natural_image = set(boolean_modular_natural_image(modulus))
            self.assertEqual(zero_aware, natural_image)
            self.assertEqual(len(zero_aware), modulus + 1)
            self.assertEqual(boolean_modular_reachable_carrier_size(modulus), modulus + 1)

    def test_zero_aware_semiring_is_closed_and_matches_product_operations_on_reachable_values(self):
        for modulus in range(2, 8):
            zero_aware = zero_aware_modular_semiring(modulus)
            full = product_semiring(boolean_semiring(), modular_semiring(modulus))
            elements = zero_aware_modular_elements(modulus)
            element_set = set(elements)
            for left in elements:
                for right in elements:
                    self.assertIn(zero_aware.add(left, right), element_set)
                    self.assertIn(zero_aware.mul(left, right), element_set)
                    self.assertEqual(zero_aware.add(left, right), full.add(left, right))
                    self.assertEqual(zero_aware.mul(left, right), full.mul(left, right))
            self.assertTrue(natural_image_is_closed_on_samples(zero_aware, 3 * modulus))

    def test_boolean_modular_carrier_compression_counts(self):
        for modulus in range(2, 10):
            report = boolean_modular_carrier_report(modulus)
            self.assertEqual(report.ambient_carrier_size, 2 * modulus)
            self.assertEqual(report.reachable_carrier_size, modulus + 1)
            self.assertEqual(report.unreachable_carrier_states, modulus - 1)
            self.assertTrue(report.has_carrier_overprecision)
            self.assertEqual(len(boolean_modular_product_elements(modulus)), 2 * modulus)

    def test_modular_product_reachable_image_is_lcm_compatible_subring(self):
        cases = (
            ((2, 3), 6, 6),
            ((4, 6), 24, 12),
            ((6, 9), 54, 18),
            ((4, 6, 9), 216, 36),
        )
        for moduli, full, reachable in cases:
            self.assertEqual(modular_product_full_carrier_size(moduli), full)
            self.assertEqual(modular_product_natural_image_size(moduli), reachable)
            report = modular_product_carrier_report(moduli)
            self.assertEqual(report.ambient_carrier_size, full)
            self.assertEqual(report.reachable_carrier_size, reachable)
            self.assertEqual(report.unreachable_carrier_states, full - reachable)
            self.assertEqual(report.has_carrier_overprecision, full > reachable)

    def test_coprime_crt_product_has_no_coefficient_carrier_overprecision(self):
        report = modular_product_carrier_report((2, 3, 5))
        self.assertEqual(report.ambient_carrier_size, 30)
        self.assertEqual(report.reachable_carrier_size, 30)
        self.assertFalse(report.has_carrier_overprecision)

    def test_zero_aware_has_same_local_count_capacity_as_full_boolean_modular_product(self):
        for modulus in range(2, 8):
            zero_aware = zero_aware_modular_semiring(modulus)
            full = product_semiring(boolean_semiring(), modular_semiring(modulus))
            self.assertTrue(natural_code_injective_through(zero_aware, modulus))
            self.assertFalse(natural_code_injective_through(zero_aware, modulus + 1))
            self.assertEqual(finite_code_capacity(zero_aware, 2 * modulus + 2), modulus)
            self.assertEqual(
                finite_code_capacity(full, 2 * modulus + 2),
                modulus,
            )

    def test_zero_aware_and_full_product_branching_agree_exhaustively_on_two_state_relations(self):
        states = (0, 1)
        relations = all_two_state_relations()
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for modulus in (2, 3, 4):
            for first in relations:
                for second in relations:
                    family = {"a": first, "b": second}
                    for observation in observations:
                        for horizon in range(4):
                            self.assertTrue(
                                zero_aware_and_full_boolean_modular_branching_agree(
                                    states,
                                    family,
                                    observation,
                                    horizon,
                                    modulus,
                                )
                            )

    def test_zero_aware_and_full_product_terminal_traces_agree(self):
        states = (0, 1)
        relations = {
            "a": frozenset({(0, 0), (0, 1), (1, 1)}),
            "b": frozenset({(0, 1), (1, 0)}),
        }
        observation = lambda state: state
        words = words_through_horizon(tuple(relations), 5)
        for modulus in (2, 3, 5):
            for source in states:
                for word in words:
                    self.assertTrue(
                        zero_aware_and_full_boolean_modular_traces_agree(
                            states,
                            relations,
                            observation,
                            source,
                            word,
                            modulus,
                        )
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            zero_aware_modular_semiring(1)
        with self.assertRaises(TypeError):
            boolean_modular_product_elements(False)
        with self.assertRaises(ValueError):
            modular_product_full_carrier_size(())
        with self.assertRaises(ValueError):
            natural_image_is_closed_on_samples(zero_aware_modular_semiring(2), -1)


if __name__ == "__main__":
    unittest.main()
