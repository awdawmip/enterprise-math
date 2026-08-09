import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_uniform_chain_impulse_1d import (
    solve_uniform_chain_nonclosing_impulse,
    uniform_chain_candidate_is_feasible,
    uniform_chain_minimum_impulse_vector,
    uniform_chain_minimum_total_impulse,
    uniform_chain_parity_surplus_contact,
    uniform_chain_score_increment,
)


def chain_state(contact_count, closing_score, offset=0, mass=1):
    return ContactNetworkMomentum1D(
        masses=(mass,) * (contact_count + 1),
        momenta=tuple(
            offset - closing_score * index
            for index in range(contact_count + 1)
        ),
        contacts=tuple(
            ContactChannel1D(index, index + 1, 1)
            for index in range(contact_count)
        ),
    )


class MaterialUniformChainImpulse1DTests(unittest.TestCase):
    def test_closed_form_increment_is_uniform_except_exact_parity_surplus(self):
        for contact_count in range(1, 13):
            for closing_score in range(1, 9):
                increments = uniform_chain_score_increment(
                    contact_count, closing_score
                )
                expected = [closing_score] * contact_count
                surplus = uniform_chain_parity_surplus_contact(
                    contact_count, closing_score
                )
                if surplus is not None:
                    expected[surplus] += 1
                self.assertEqual(increments, tuple(expected))

    def test_minimum_total_closed_form_matches_impulse_vector_sum(self):
        for contact_count in range(1, 20):
            for closing_score in range(1, 12):
                impulses = uniform_chain_minimum_impulse_vector(
                    contact_count, closing_score
                )
                self.assertEqual(
                    sum(impulses),
                    uniform_chain_minimum_total_impulse(
                        contact_count, closing_score
                    ),
                )

    def test_closed_form_is_componentwise_least_against_small_bounded_oracle(self):
        for contact_count in range(1, 5):
            for closing_score in range(1, 4):
                minimum = uniform_chain_minimum_impulse_vector(
                    contact_count, closing_score
                )
                ranges = tuple(range(value + 3) for value in minimum)
                feasible_count = 0
                for candidate in itertools.product(*ranges):
                    if not uniform_chain_candidate_is_feasible(
                        contact_count, closing_score, candidate
                    ):
                        continue
                    feasible_count += 1
                    self.assertTrue(
                        all(
                            candidate[index] >= minimum[index]
                            for index in range(contact_count)
                        )
                    )
                self.assertGreater(feasible_count, 0)

    def test_three_contact_reference_counterexample_has_unique_coordinated_solution_floor(self):
        solution = solve_uniform_chain_nonclosing_impulse(
            chain_state(3, 1, offset=3)
        )
        self.assertEqual(solution.impulse_vector, (2, 3, 2))
        self.assertEqual(solution.minimum_total_impulse, 7)
        self.assertEqual(solution.score_increment, (1, 2, 1))
        self.assertEqual(solution.final_scores, (0, 1, 0))
        self.assertEqual(solution.final_momenta, (1, 1, 2, 2))
        self.assertEqual(solution.parity_surplus_contact, 1)
        self.assertFalse(solution.exact_comoving_consensus)

    def test_even_parity_chain_reaches_exact_integer_comoving_consensus(self):
        solution = solve_uniform_chain_nonclosing_impulse(
            chain_state(2, 1, offset=2)
        )
        self.assertEqual(solution.impulse_vector, (1, 1))
        self.assertEqual(solution.final_scores, (0, 0))
        self.assertEqual(solution.final_momenta, (1, 1, 1))
        self.assertIsNone(solution.parity_surplus_contact)
        self.assertTrue(solution.exact_comoving_consensus)

    def test_odd_parity_obstruction_forms_two_adjacent_integer_momentum_plateaus(self):
        solution = solve_uniform_chain_nonclosing_impulse(
            chain_state(5, 1, offset=5)
        )
        self.assertEqual(solution.impulse_vector, (3, 5, 6, 5, 3))
        self.assertEqual(solution.final_scores, (0, 0, 1, 0, 0))
        self.assertEqual(solution.final_momenta, (2, 2, 2, 3, 3, 3))
        self.assertEqual(sum(solution.final_momenta), sum(solution.before.momenta))

    def test_absolute_momentum_offset_does_not_change_required_contact_impulse(self):
        base = solve_uniform_chain_nonclosing_impulse(chain_state(3, 1, offset=3))
        shifted = solve_uniform_chain_nonclosing_impulse(chain_state(3, 1, offset=103))
        self.assertEqual(base.impulse_vector, shifted.impulse_vector)
        self.assertEqual(base.final_scores, shifted.final_scores)
        self.assertEqual(
            tuple(value + 100 for value in base.final_momenta),
            shifted.final_momenta,
        )

    def test_mass_value_does_not_change_equal_mass_normalized_chain_solution(self):
        first = solve_uniform_chain_nonclosing_impulse(chain_state(4, 3, offset=12, mass=1))
        seventh = solve_uniform_chain_nonclosing_impulse(chain_state(4, 3, offset=12, mass=7))
        self.assertEqual(first.impulse_vector, seventh.impulse_vector)
        self.assertEqual(first.final_scores, seventh.final_scores)

    def test_invalid_chain_hypotheses_are_rejected(self):
        with self.assertRaises(ValueError):
            uniform_chain_minimum_impulse_vector(0, 1)
        with self.assertRaises(ValueError):
            uniform_chain_minimum_impulse_vector(2, 0)
        with self.assertRaises(ValueError):
            uniform_chain_candidate_is_feasible(2, 1, (1,))
        with self.assertRaises(ValueError):
            uniform_chain_candidate_is_feasible(2, 1, (1, -1))

        unequal_mass = ContactNetworkMomentum1D(
            masses=(1, 2, 1),
            momenta=(2, 1, 0),
            contacts=(ContactChannel1D(0, 1, 1), ContactChannel1D(1, 2, 1)),
        )
        with self.assertRaises(ValueError):
            solve_uniform_chain_nonclosing_impulse(unequal_mass)

        reversed_contact = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(ContactChannel1D(1, 0, -1), ContactChannel1D(1, 2, 1)),
        )
        with self.assertRaises(ValueError):
            solve_uniform_chain_nonclosing_impulse(reversed_contact)

        nonuniform_scores = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(3, 2, 0),
            contacts=(ContactChannel1D(0, 1, 1), ContactChannel1D(1, 2, 1)),
        )
        with self.assertRaises(ValueError):
            solve_uniform_chain_nonclosing_impulse(nonuniform_scores)

        already_nonclosing = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(0, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        with self.assertRaises(ValueError):
            solve_uniform_chain_nonclosing_impulse(already_nonclosing)


if __name__ == "__main__":
    unittest.main()
