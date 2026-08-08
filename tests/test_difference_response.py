import unittest

from enterprise_math.core import collapse
from enterprise_math.difference_response import (
    admissible_difference,
    collapse_commutator_holonomy,
    collapse_projection_defect,
    collapse_response_is_same_basin,
    composed_response,
    identity_response,
    path_holonomy,
    quotient_response,
    response,
    response_is_zero_collision,
    suffix_holonomy,
    zero_response_matches_endpoint_equality,
)
from enterprise_math.precision_signed_holonomy import signed_defect_transport


class DifferenceResponseTests(unittest.TestCase):
    def test_response_lands_in_target_difference_fiber(self):
        operations = [
            lambda value: value,
            lambda value: value // 2,
            lambda value: collapse(value, 2),
            lambda value: 3 * value + 1,
        ]
        for operation in operations:
            for base_state in range(60):
                for difference in range(-base_state, 41):
                    result = response(operation, base_state, difference)
                    target_base = operation(base_state)
                    self.assertTrue(admissible_difference(target_base, result))

    def test_identity_and_exact_chain_law(self):
        for base_state in range(50):
            for difference in range(-base_state, 31):
                self.assertEqual(identity_response(base_state, difference), difference)
                first = lambda value: value // 3
                second = lambda value: collapse(value, 2)
                direct, staged = composed_response(
                    first, second, base_state, difference
                )
                self.assertEqual(direct, staged)

    def test_common_suffix_holonomy_propagates_by_response(self):
        first_path = lambda value: collapse(value, 2) // 2
        second_path = lambda value: collapse(value // 2, 2)
        suffixes = [
            lambda value: value,
            lambda value: value // 3,
            lambda value: collapse(value, 3),
        ]
        for suffix in suffixes:
            for state in range(120):
                direct, propagated = suffix_holonomy(
                    first_path, second_path, suffix, state
                )
                self.assertEqual(direct, propagated)

    def test_quotient_response_is_signed_precision_transport(self):
        for modulus in range(1, 10):
            for base_state in range(50):
                for difference in range(-base_state, 31):
                    self.assertEqual(
                        quotient_response(base_state, difference, modulus),
                        signed_defect_transport(modulus, base_state, difference),
                    )

    def test_zero_response_is_exactly_collision(self):
        operations = [
            lambda value: value // 4,
            lambda value: collapse(value, 2),
            lambda value: collapse(value, 3),
        ]
        for operation in operations:
            for base_state in range(80):
                for difference in range(-base_state, 31):
                    zero = response_is_zero_collision(
                        operation, base_state, difference
                    )
                    self.assertEqual(
                        zero,
                        operation(base_state + difference) == operation(base_state),
                    )

    def test_zero_response_persists_under_deterministic_suffix(self):
        first = lambda value: value // 5
        suffix = lambda value: collapse(value, 2)
        for base_state in range(80):
            for difference in range(-base_state, 31):
                if response(first, base_state, difference) == 0:
                    direct, staged = composed_response(
                        first, suffix, base_state, difference
                    )
                    self.assertEqual(staged, 0)
                    self.assertEqual(direct, 0)

    def test_cumulative_zero_response_matches_endpoint_equality(self):
        operations = [
            lambda value: value // 2,
            lambda value: collapse(value, 2),
            lambda value: value // 3,
        ]
        for base_state in range(80):
            for difference in range(-base_state, 31):
                expected = zero_response_matches_endpoint_equality(
                    operations, base_state, difference
                )
                current_one = base_state
                current_two = base_state + difference
                for operation in operations:
                    current_one = operation(current_one)
                    current_two = operation(current_two)
                self.assertEqual(expected, current_one == current_two)

    def test_collapse_zero_response_is_same_root_basin(self):
        for power in range(2, 6):
            for base_state in range(100):
                for difference in range(-base_state, 31):
                    zero = collapse_response_is_same_basin(
                        base_state, difference, power
                    )
                    self.assertEqual(
                        zero,
                        collapse(base_state, power)
                        == collapse(base_state + difference, power),
                    )

    def test_representative_core_holonomy_cells(self):
        for state in range(100):
            # Projection/projection is checked elsewhere through quotient path coherence.
            # Comparable collapse exponents commute globally by P003.
            self.assertEqual(collapse_commutator_holonomy(state, 2, 4), 0)
            self.assertEqual(collapse_commutator_holonomy(state, 3, 6), 0)

        # Incomparable exponents have an explicit P003 witness.
        self.assertNotEqual(collapse_commutator_holonomy(2**3, 2, 3), 0)

        # Collapse/projection squares can carry signed holonomy in either direction.
        self.assertEqual(collapse_projection_defect(2, 2, 2), 1)
        self.assertLess(collapse_projection_defect(2**4, 4, 2), 0)

    def test_path_holonomy_orientation(self):
        first = lambda value: value // 2
        second = lambda value: collapse(value, 2)
        for state in range(80):
            forward = path_holonomy(first, second, state)
            backward = path_holonomy(second, first, state)
            self.assertEqual(forward, -backward)


if __name__ == "__main__":
    unittest.main()
