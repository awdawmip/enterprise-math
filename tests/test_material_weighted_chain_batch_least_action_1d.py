import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_relative_scores,
)
from enterprise_math.material_weighted_chain_batch_least_action_1d import (
    solve_weighted_chain_batch_least_action,
)
from enterprise_math.material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
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


class MaterialWeightedChainBatchLeastAction1DTests(unittest.TestCase):
    def test_batch_solver_matches_unit_solver_on_reference_examples(self):
        states = (
            chain_state((1, 2, 1), (4, 4, 0)),
            chain_state((2, 3, 5), (6, 6, 0)),
            chain_state((2, 3, 5), (10, 9, 0)),
            chain_state((1, 3, 2, 1), (6, 9, 4, 0)),
        )
        for state in states:
            unit = solve_weighted_chain_least_action(state)
            batch = solve_weighted_chain_batch_least_action(state)
            self.assertEqual(batch.impulse_vector, unit.impulse_vector)
            self.assertEqual(batch.final_scores, unit.final_scores)
            self.assertEqual(batch.final_momenta, unit.final_momenta)
            self.assertLessEqual(batch.batch_count, unit.increment_count)

    def test_every_batch_is_exact_local_ceil_repair(self):
        state = chain_state((2, 3, 5), (10, 9, 0))
        report = solve_weighted_chain_batch_least_action(state)
        self.assertTrue(report.events)
        for event in report.events:
            expected = (
                -event.score_before + event.diagonal_coupling - 1
            ) // event.diagonal_coupling
            self.assertEqual(event.batch_size, expected)
            self.assertGreater(event.batch_size, 0)
            self.assertEqual(
                event.impulse_after,
                event.impulse_before + event.batch_size,
            )
            self.assertGreaterEqual(
                event.scores_after[event.contact_index],
                0,
            )

    def test_left_and_right_batch_priorities_match_exhaustively(self):
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
                    left_result = solve_weighted_chain_batch_least_action(state, left)
                    right_result = solve_weighted_chain_batch_least_action(state, right)
                    self.assertEqual(
                        left_result.impulse_vector,
                        right_result.impulse_vector,
                    )
                    self.assertEqual(
                        left_result.final_scores,
                        right_result.final_scores,
                    )
                    self.assertEqual(
                        left_result.impulse_vector,
                        solve_weighted_chain_least_action(state).impulse_vector,
                    )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_all_priorities_match_on_selected_four_body_states(self):
        states = (
            chain_state((1, 3, 2, 1), (6, 9, 4, 0)),
            chain_state((2, 5, 3, 4), (7, 12, 2, 0)),
        )
        for state in states:
            if any(score > 0 for score in contact_relative_scores(state)):
                continue
            results = {
                solve_weighted_chain_batch_least_action(state, priority).impulse_vector
                for priority in itertools.permutations(range(len(state.contacts)))
            }
            self.assertEqual(len(results), 1)

    def test_batching_can_use_strictly_fewer_events_than_unit_updates(self):
        state = chain_state((2, 3, 5), (10, 9, 0))
        unit = solve_weighted_chain_least_action(state)
        batch = solve_weighted_chain_batch_least_action(state)
        self.assertEqual(unit.impulse_vector, (7, 10))
        self.assertEqual(unit.increment_count, 17)
        self.assertLess(batch.batch_count, unit.increment_count)
        self.assertEqual(batch.delivered_impulse_quanta, 17)

    def test_explicit_upper_witness_bounds_every_intermediate_batch_impulse(self):
        state = chain_state((1, 3, 2, 1), (6, 9, 4, 0))
        report = solve_weighted_chain_batch_least_action(state)
        running = [0] * len(state.contacts)
        for event in report.events:
            running[event.contact_index] = event.impulse_after
            self.assertTrue(
                all(
                    running[index] <= report.feasible_upper_impulse[index]
                    for index in range(len(running))
                )
            )

    def test_already_nonclosing_chain_has_no_batch_events(self):
        state = chain_state((2, 3, 5), (0, 0, 0))
        report = solve_weighted_chain_batch_least_action(state)
        self.assertEqual(report.impulse_vector, (0, 0))
        self.assertEqual(report.batch_count, 0)
        self.assertEqual(report.final_scores, (0, 0))


if __name__ == "__main__":
    unittest.main()
