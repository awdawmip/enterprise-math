import unittest

from enterprise_math.abc_block_mu import (
    compressed_additive_states_at_radius,
    degenerate_scaling_parameter,
    exact_minimum_nondegenerate_witness_radius,
    reachable_block_derivative_values,
)
from enterprise_math.abc_witness_precision import minimal_witness_cost


class AbcBlockMuTests(unittest.TestCase):
    def test_wronskian_zero_is_exact_scaling_line(self) -> None:
        self.assertEqual(degenerate_scaling_parameter(2, 3, 5, 2, 3), 1)
        self.assertEqual(degenerate_scaling_parameter(2, 3, 5, -4, -6), -2)
        self.assertIsNone(degenerate_scaling_parameter(2, 3, 5, 0, 1))

    def test_block_reachable_values_are_scalar_dynamic_sets(self) -> None:
        self.assertEqual(reachable_block_derivative_values(9, 1), frozenset({-6, 0, 6}))
        values = reachable_block_derivative_values(12, 1)
        self.assertIn(-16, values)
        self.assertIn(0, values)
        self.assertIn(16, values)
        self.assertLessEqual(len(values), 9)

    def test_235_escapes_scaling_line_at_radius_one(self) -> None:
        states = compressed_additive_states_at_radius(2, 3, 5, 1)
        self.assertIn((-1, 0, -1), states)
        solution = exact_minimum_nondegenerate_witness_radius(2, 3, 5)
        self.assertEqual(solution.mu, 1)
        self.assertEqual(solution.floor_access_upper_bound, 2)
        self.assertNotEqual(solution.wronskian, 0)

    def test_same_radical_189_needs_radius_two(self) -> None:
        radius_one = compressed_additive_states_at_radius(1, 8, 9, 1)
        self.assertEqual(radius_one, ((0, 0, 0),))
        solution = exact_minimum_nondegenerate_witness_radius(1, 8, 9)
        self.assertEqual(solution.mu, 2)
        self.assertEqual(solution.derivative_values, (0, -12, -12))
        self.assertEqual(solution.absorption_redundancy, 1)

    def test_tradeoff_examples_recover_known_mu(self) -> None:
        for triple, expected in (
            ((2, 7, 9), 1),
            ((5, 7, 12), 1),
            ((5, 27, 32), 3),
            ((14, 15, 29), 1),
        ):
            solution = exact_minimum_nondegenerate_witness_radius(*triple)
            self.assertEqual(solution.mu, expected)
            self.assertLessEqual(solution.mu, solution.floor_access_upper_bound)
            self.assertEqual(solution.mu, minimal_witness_cost(*triple, max_bound=max(3, expected)))

    def test_arbitrary_support_four_coordinate_example(self) -> None:
        solution = exact_minimum_nondegenerate_witness_radius(25, 704, 729)
        self.assertEqual(solution.mu, 6)
        self.assertEqual(solution.floor_access_upper_bound, 6)
        self.assertEqual(solution.absorption_redundancy, 6)
        self.assertEqual(solution.mu, minimal_witness_cost(25, 704, 729, max_bound=6))

    def test_unit_relation_can_have_mu_equal_nu_far_from_one(self) -> None:
        first = exact_minimum_nondegenerate_witness_radius(1, 242, 243)
        self.assertEqual(first.mu, 27)
        self.assertEqual(first.floor_access_upper_bound, 27)

        second = exact_minimum_nondegenerate_witness_radius(1, 512, 513)
        self.assertEqual(second.mu, 13)
        self.assertEqual(second.floor_access_upper_bound, 13)


if __name__ == "__main__":
    unittest.main()
