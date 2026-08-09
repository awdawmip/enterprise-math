import itertools
import unittest

from enterprise_math.p018_p023_power_free_action_basis import (
    action_basis_separates_bounded_domain,
    action_distinguishes_adjacent_boundary,
    adjacent_boundary_actions,
    contains_forced_power_free_basis,
    is_r_power_free,
    minimal_root_quotient_action_basis,
    r_power_free_kernel,
)
from enterprise_math.core import integer_nth_root


class P018P023PowerFreeActionBasisTests(unittest.TestCase):
    def test_power_free_kernel_decomposition(self):
        for root_exp in range(1, 7):
            for n in range(1, 3000):
                kernel = r_power_free_kernel(n, root_exp)
                self.assertTrue(is_r_power_free(kernel, root_exp))
                self.assertEqual(n % kernel, 0)
                quotient = n // kernel
                root = integer_nth_root(quotient, root_exp)
                self.assertEqual(root**root_exp, quotient)

    def test_adjacent_jump_iff_action_times_exact_power(self):
        for root_exp in range(1, 6):
            for q in range(1, 500):
                exact_actions = set(adjacent_boundary_actions(q, root_exp))
                for action in range(1, 500):
                    self.assertEqual(
                        action_distinguishes_adjacent_boundary(q, action, root_exp),
                        action in exact_actions,
                    )

    def test_minimal_basis_separates_dense_bounded_domains(self):
        for root_exp in range(1, 7):
            for max_state in range(0, 250):
                basis = minimal_root_quotient_action_basis(max_state, root_exp)
                self.assertTrue(
                    action_basis_separates_bounded_domain(
                        max_state, root_exp, basis
                    )
                )
                self.assertTrue(
                    contains_forced_power_free_basis(max_state, root_exp, basis)
                )

    def test_every_basis_action_is_forced_by_its_own_boundary(self):
        for root_exp in range(1, 6):
            for max_state in range(1, 150):
                basis = minimal_root_quotient_action_basis(max_state, root_exp)
                for forced in basis:
                    reduced = tuple(a for a in basis if a != forced)
                    self.assertFalse(
                        action_basis_separates_bounded_domain(
                            max_state, root_exp, reduced
                        )
                    )
                    self.assertFalse(
                        contains_forced_power_free_basis(
                            max_state, root_exp, reduced
                        )
                    )
                    # The missing action is forced already by the adjacent
                    # boundary (forced-1, forced).
                    alternatives = set(adjacent_boundary_actions(forced, root_exp))
                    self.assertEqual(alternatives & set(basis), {forced})

    def test_exact_criterion_on_arbitrary_action_sets(self):
        for root_exp in range(1, 4):
            for max_state in range(1, 9):
                universe = list(range(1, max_state + 1))
                for mask in range(1 << max_state):
                    actions = tuple(
                        universe[i]
                        for i in range(max_state)
                        if (mask >> i) & 1
                    )
                    self.assertEqual(
                        action_basis_separates_bounded_domain(
                            max_state, root_exp, actions
                        ),
                        contains_forced_power_free_basis(
                            max_state, root_exp, actions
                        ),
                    )

    def test_unique_minimum_by_bruteforce_small_domains(self):
        for root_exp in range(1, 4):
            for max_state in range(1, 9):
                forced = set(
                    minimal_root_quotient_action_basis(max_state, root_exp)
                )
                universe = list(range(1, max_state + 1))
                minima = []
                best_size = max_state + 1
                for size in range(max_state + 1):
                    if size > best_size:
                        break
                    for combo in itertools.combinations(universe, size):
                        if action_basis_separates_bounded_domain(
                            max_state, root_exp, combo
                        ):
                            if size < best_size:
                                best_size = size
                                minima = [set(combo)]
                            elif size == best_size:
                                minima.append(set(combo))
                    if minima:
                        break
                self.assertEqual(best_size, len(forced))
                self.assertEqual(minima, [forced])

    def test_named_examples(self):
        self.assertEqual(
            minimal_root_quotient_action_basis(10, 2),
            (1, 2, 3, 5, 6, 7, 10),
        )
        self.assertEqual(minimal_root_quotient_action_basis(20, 1), (1,))
        self.assertEqual(r_power_free_kernel(72, 2), 2)
        self.assertEqual(r_power_free_kernel(72, 3), 9)

    def test_validation(self):
        with self.assertRaises(ValueError):
            is_r_power_free(0, 2)
        with self.assertRaises(ValueError):
            is_r_power_free(5, 0)
        with self.assertRaises(ValueError):
            r_power_free_kernel(0, 2)
        with self.assertRaises(ValueError):
            action_basis_separates_bounded_domain(-1, 2, ())
        with self.assertRaises(ValueError):
            action_basis_separates_bounded_domain(10, 0, ())
        with self.assertRaises(ValueError):
            action_basis_separates_bounded_domain(10, 2, (0,))


if __name__ == "__main__":
    unittest.main()
