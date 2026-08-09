import unittest

from enterprise_math.core import collapse
from enterprise_math.difference_response import response
from enterprise_math.state_pair import (
    composed_pair_map,
    critical_square_pair,
    cumulative_kernel_monotone,
    diagonal_is_absorbing,
    difference_to_pair,
    endpoint_pair,
    kernel_equals_diagonal_preimage,
    kernel_monotonic_under_suffix,
    on_diagonal,
    pair_map,
    pair_to_difference,
    suffix_pair_propagation,
)


class StatePairTests(unittest.TestCase):
    def test_pair_identity_and_composition(self):
        identity = lambda value: value
        first = lambda value: value // 2
        second = lambda value: value * value + 1
        for left in range(40):
            for right in range(40):
                pair = (left, right)
                self.assertEqual(pair_map(identity, pair), pair)
                direct, staged = composed_pair_map(first, second, pair)
                self.assertEqual(direct, staged)

    def test_diagonal_is_absorbing(self):
        operations = [
            lambda value: value,
            lambda value: value // 3,
            lambda value: collapse(value, 2),
            lambda value: value * 2 + 1,
        ]
        for operation in operations:
            for state in range(80):
                self.assertTrue(diagonal_is_absorbing(operation, state))
                self.assertTrue(on_diagonal(pair_map(operation, (state, state))))

    def test_kernel_relation_is_diagonal_preimage(self):
        operations = [
            lambda value: value // 4,
            lambda value: collapse(value, 2),
            lambda value: collapse(value, 3),
        ]
        for operation in operations:
            for left in range(60):
                for right in range(60):
                    expected = operation(left) == operation(right)
                    self.assertEqual(
                        kernel_equals_diagonal_preimage(operation, left, right),
                        expected,
                    )

    def test_pair_difference_coordinates_are_inverse(self):
        for first in range(60):
            for second in range(60):
                coordinates = pair_to_difference(first, second)
                self.assertEqual(difference_to_pair(*coordinates), (first, second))

        for base_state in range(60):
            for difference in range(-base_state, 31):
                pair = difference_to_pair(base_state, difference)
                self.assertEqual(pair_to_difference(*pair), (base_state, difference))

    def test_same_signed_defect_does_not_determine_response(self):
        quotient = lambda value: value // 2
        self.assertEqual(response(quotient, 0, 1), 0)
        self.assertEqual(response(quotient, 1, 1), 1)

        square_collapse = lambda value: collapse(value, 2)
        self.assertEqual(response(square_collapse, 1, 1), 0)
        self.assertEqual(response(square_collapse, 3, 1), 3)

    def test_common_suffix_pair_propagation(self):
        first_path = lambda value: collapse(value, 2) // 2
        second_path = lambda value: collapse(value // 2, 2)
        suffixes = [
            lambda value: value,
            lambda value: value // 3,
            lambda value: collapse(value, 3),
        ]
        for state in range(100):
            for suffix in suffixes:
                direct, propagated = suffix_pair_propagation(
                    first_path, second_path, suffix, state
                )
                self.assertEqual(direct, propagated)

    def test_critical_square_pair_is_diagonal_exactly_when_square_commutes(self):
        for power in range(2, 5):
            operation = lambda value, p=power: collapse(value, p)
            for ratio in range(1, 6):
                for state in range(100):
                    pair = critical_square_pair(
                        operation, operation, state, ratio
                    )
                    self.assertEqual(
                        on_diagonal(pair),
                        operation(state) // ratio
                        == operation(state // ratio),
                    )

    def test_kernel_membership_persists_under_suffix(self):
        first = lambda value: value // 5
        suffixes = [
            lambda value: collapse(value, 2),
            lambda value: value // 3,
            lambda value: value * 2 + 1,
        ]
        for suffix in suffixes:
            for left in range(80):
                for right in range(80):
                    self.assertTrue(
                        kernel_monotonic_under_suffix(
                            first, suffix, left, right
                        )
                    )

    def test_cumulative_kernel_monotonicity(self):
        prefixes = [
            lambda value: value // 2,
            lambda value: collapse(value, 2),
        ]
        next_operations = [
            lambda value: value // 3,
            lambda value: collapse(value, 3),
        ]
        for next_operation in next_operations:
            for left in range(80):
                for right in range(80):
                    self.assertTrue(
                        cumulative_kernel_monotone(
                            prefixes, next_operation, left, right
                        )
                    )

    def test_endpoint_pair_matches_direct_paths(self):
        first = lambda value: value // 2
        second = lambda value: collapse(value, 2)
        for state in range(80):
            self.assertEqual(
                endpoint_pair(first, second, state),
                (first(state), second(state)),
            )


if __name__ == "__main__":
    unittest.main()
