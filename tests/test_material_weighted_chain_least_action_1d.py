import itertools
import unittest

from enterprise_math.material_chain_consensus_impulse_1d import (
    chain_minimum_impulse_from_momenta,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
)
from enterprise_math.material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
    weighted_chain_candidate_is_feasible,
    weighted_chain_feasible_upper_witness,
    weighted_chain_priority,
)


def chain_state(masses, momenta):
    masses = tuple(masses)
    momenta = tuple(momenta)
    return ContactNetworkMomentum1D(
        masses=masses,
        momenta=momenta,
        contacts=tuple(
            ContactChannel1D(index, index + 1, 1)
            for index in range(len(masses) - 1)
        ),
    )


class MaterialWeightedChainLeastAction1DTests(unittest.TestCase):
    def test_reference_unequal_mass_examples(self):
        cases = (
            ((1, 2, 1), (4, 4, 0), (2, 2), (0, 0)),
            ((2, 3, 5), (6, 6, 0), (4, 7), (0, 12)),
            ((2, 3, 5), (10, 9, 0), (7, 10), (15, 0)),
            ((1, 3, 2, 1), (6, 9, 4, 0), (4, 5, 3), (4, 2, 0)),
        )
        for masses, momenta, impulse, scores in cases:
            solution = solve_weighted_chain_least_action(
                chain_state(masses, momenta)
            )
            self.assertEqual(solution.impulse_vector, impulse)
            self.assertEqual(solution.final_scores, scores)
            self.assertEqual(solution.increment_count, sum(impulse))
            self.assertEqual(
                sum(solution.final_momenta),
                sum(momenta),
            )

    def test_path_coupling_has_z_matrix_sign_pattern(self):
        for masses in (
            (1, 2),
            (2, 3, 5),
            (1, 3, 2, 5),
            (4, 1, 7, 2, 3),
        ):
            state = chain_state(masses, (0,) * len(masses))
            gram = contact_coupling_gram(state)
            for row in range(len(gram)):
                self.assertGreater(gram[row][row], 0)
                for col in range(len(gram)):
                    if row != col:
                        self.assertLessEqual(gram[row][col], 0)

    def test_explicit_upper_witness_is_always_feasible_on_small_domain(self):
        for body_count in range(2, 5):
            for masses in itertools.product(range(1, 4), repeat=body_count):
                for momenta in itertools.product(range(-2, 3), repeat=body_count):
                    state = chain_state(masses, momenta)
                    if any(score > 0 for score in contact_relative_scores(state)):
                        continue
                    witness = weighted_chain_feasible_upper_witness(state)
                    self.assertTrue(
                        weighted_chain_candidate_is_feasible(
                            state, witness.prefix_impulse_vector
                        )
                    )
                    self.assertTrue(
                        all(value >= 0 for value in witness.prefix_impulse_vector)
                    )
                    self.assertTrue(all(score >= 0 for score in witness.final_scores))
                    self.assertEqual(
                        sum(witness.final_momenta),
                        sum(momenta),
                    )

    def test_left_and_right_priorities_converge_to_same_solution_exhaustively(self):
        checked = 0
        for body_count in range(2, 5):
            contact_count = body_count - 1
            left = tuple(range(contact_count))
            right = tuple(reversed(left))
            mass_values = range(1, 4) if body_count < 4 else range(1, 3)
            for masses in itertools.product(mass_values, repeat=body_count):
                for momenta in itertools.product(range(-2, 3), repeat=body_count):
                    state = chain_state(masses, momenta)
                    if any(score > 0 for score in contact_relative_scores(state)):
                        continue
                    left_solution = solve_weighted_chain_least_action(state, left)
                    right_solution = solve_weighted_chain_least_action(state, right)
                    self.assertEqual(
                        left_solution.impulse_vector,
                        right_solution.impulse_vector,
                    )
                    self.assertEqual(
                        left_solution.final_momenta,
                        right_solution.final_momenta,
                    )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_all_priority_permutations_agree_on_selected_four_body_states(self):
        states = (
            chain_state((1, 3, 2, 1), (6, 9, 4, 0)),
            chain_state((2, 5, 3, 4), (7, 12, 2, 0)),
            chain_state((3, 2, 7, 1), (8, 3, 5, -1)),
        )
        for state in states:
            if any(score > 0 for score in contact_relative_scores(state)):
                continue
            results = {
                solve_weighted_chain_least_action(state, priority).impulse_vector
                for priority in itertools.permutations(range(len(state.contacts)))
            }
            self.assertEqual(len(results), 1)

    def test_solver_is_componentwise_least_against_independent_small_candidate_oracle(self):
        checked = 0
        for body_count in range(2, 4):
            for masses in itertools.product(range(1, 4), repeat=body_count):
                for momenta in itertools.product(range(-2, 3), repeat=body_count):
                    state = chain_state(masses, momenta)
                    if any(score > 0 for score in contact_relative_scores(state)):
                        continue
                    solution = solve_weighted_chain_least_action(state)
                    ranges = tuple(range(value + 3) for value in solution.impulse_vector)
                    feasible_count = 0
                    for candidate in itertools.product(*ranges):
                        if not weighted_chain_candidate_is_feasible(state, candidate):
                            continue
                        feasible_count += 1
                        self.assertTrue(
                            all(
                                candidate[index] >= solution.impulse_vector[index]
                                for index in range(len(candidate))
                            )
                        )
                    self.assertGreater(feasible_count, 0)
                    checked += 1
        self.assertGreater(checked, 100)

    def test_feasible_set_is_closed_under_coordinatewise_min_on_small_examples(self):
        states = (
            chain_state((1, 2, 1), (4, 4, 0)),
            chain_state((2, 3, 5), (6, 6, 0)),
            chain_state((1, 3, 2, 1), (6, 9, 4, 0)),
        )
        for state in states:
            solution = solve_weighted_chain_least_action(state)
            upper = solution.feasible_upper_impulse
            feasible = []
            for candidate in itertools.product(
                *(range(value + 1) for value in upper)
            ):
                if weighted_chain_candidate_is_feasible(state, candidate):
                    feasible.append(candidate)
            self.assertTrue(feasible)
            for left in feasible[:40]:
                for right in feasible[-40:]:
                    meet = tuple(min(a, b) for a, b in zip(left, right))
                    self.assertTrue(weighted_chain_candidate_is_feasible(state, meet))

    def test_equal_mass_specialization_matches_balanced_consensus_owner(self):
        values = range(-2, 3)
        for body_count in range(2, 6):
            for nondecreasing in itertools.combinations_with_replacement(
                values, body_count
            ):
                momenta = tuple(reversed(nondecreasing))
                state = chain_state((3,) * body_count, momenta)
                weighted = solve_weighted_chain_least_action(state)
                self.assertEqual(
                    weighted.impulse_vector,
                    chain_minimum_impulse_from_momenta(momenta),
                )

    def test_priority_and_hypothesis_validation(self):
        self.assertEqual(weighted_chain_priority(3), (0, 1, 2))
        self.assertEqual(weighted_chain_priority(3, (2, 0, 1)), (2, 0, 1))
        with self.assertRaises(ValueError):
            weighted_chain_priority(0)
        with self.assertRaises(ValueError):
            weighted_chain_priority(3, (0, 1))
        with self.assertRaises(ValueError):
            weighted_chain_priority(3, (0, 1, 1))
        with self.assertRaises(ValueError):
            weighted_chain_priority(3, (0, 1, True))

        separating = chain_state((1, 2, 1), (0, 0, 1))
        with self.assertRaises(ValueError):
            solve_weighted_chain_least_action(separating)

        noncanonical = ContactNetworkMomentum1D(
            masses=(1, 2, 1),
            momenta=(4, 4, 0),
            contacts=(
                ContactChannel1D(1, 0, -1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        with self.assertRaises(ValueError):
            solve_weighted_chain_least_action(noncanonical)


if __name__ == "__main__":
    unittest.main()
