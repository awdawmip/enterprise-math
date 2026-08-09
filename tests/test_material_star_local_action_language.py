import itertools
import unittest

from enterprise_math.material_star_local_action_language import (
    star_apply_local_unit_update,
    star_concentrated_unreachable_minimum_witness,
    star_local_legal_contacts,
    star_minimum_relation_is_fully_causally_reachable,
    star_replay_local_contact_word,
    star_reverse_peeling_word,
    star_run_local_unit_policy,
    star_terminal_is_causally_reachable,
)
from enterprise_math.material_star_response_spectrum import (
    star_minimum_relation_parameters,
    star_minimum_total_impulse,
    star_minimum_total_integer_relation,
    star_score_vector,
)


def independent_reachable_states(leaf_count, closing_quantum):
    start = (0,) * leaf_count
    seen = {start}
    stack = [start]
    while stack:
        state = stack.pop()
        total = sum(state)
        for index in range(leaf_count):
            if -closing_quantum + total + state[index] >= 0:
                continue
            updated = list(state)
            updated[index] += 1
            updated = tuple(updated)
            if updated not in seen:
                seen.add(updated)
                stack.append(updated)
    return seen


def independent_terminal_states(leaf_count, closing_quantum):
    return {
        state
        for state in independent_reachable_states(leaf_count, closing_quantum)
        if all(
            -closing_quantum + sum(state) + value >= 0
            for value in state
        )
    }


def independent_static_terminals_through_q(leaf_count, closing_quantum):
    terminals = set()
    for state in itertools.product(
        range(closing_quantum + 1), repeat=leaf_count
    ):
        if sum(state) > closing_quantum:
            continue
        if all(
            -closing_quantum + sum(state) + value >= 0
            for value in state
        ):
            terminals.add(state)
    return terminals


class MaterialStarLocalActionLanguageTests(unittest.TestCase):
    def test_sorted_prefix_reachability_matches_independent_bfs(self):
        checked = 0
        for leaf_count in range(2, 5):
            for closing_quantum in range(1, 7):
                reachable_terminals = independent_terminal_states(
                    leaf_count, closing_quantum
                )
                static_terminals = independent_static_terminals_through_q(
                    leaf_count, closing_quantum
                )
                predicted = {
                    state
                    for state in static_terminals
                    if star_terminal_is_causally_reachable(
                        state, closing_quantum
                    )
                }
                self.assertEqual(predicted, reachable_terminals)
                checked += len(static_terminals)
        self.assertGreater(checked, 100)

    def test_reverse_peeling_constructs_a_legal_forward_word_for_every_small_terminal(self):
        checked = 0
        for leaf_count in range(2, 5):
            for closing_quantum in range(1, 7):
                for terminal in independent_terminal_states(
                    leaf_count, closing_quantum
                ):
                    reverse_word = star_reverse_peeling_word(
                        terminal, closing_quantum
                    )
                    self.assertIsNotNone(reverse_word)
                    forward_word = tuple(reversed(reverse_word))
                    self.assertEqual(
                        star_replay_local_contact_word(
                            leaf_count,
                            closing_quantum,
                            forward_word,
                        ),
                        terminal,
                    )
                    checked += 1
        self.assertGreater(checked, 50)

    def test_static_minimum_full_reachability_has_exact_baseline_boundary(self):
        checked = 0
        for leaf_count in range(2, 8):
            for closing_quantum in range(1, 25):
                _, baseline, _ = star_minimum_relation_parameters(
                    leaf_count, closing_quantum
                )
                relation = star_minimum_total_integer_relation(
                    leaf_count, closing_quantum
                )
                actual = all(
                    star_terminal_is_causally_reachable(
                        vector, closing_quantum
                    )
                    for vector in relation
                )
                expected = closing_quantum == 1 or baseline >= 1
                self.assertEqual(actual, expected)
                self.assertEqual(
                    star_minimum_relation_is_fully_causally_reachable(
                        leaf_count, closing_quantum
                    ),
                    expected,
                )
                checked += 1
        self.assertGreater(checked, 100)

    def test_k2_q2_is_first_static_minimum_relation_with_unreachable_members(self):
        relation = set(star_minimum_total_integer_relation(2, 2))
        self.assertEqual(relation, {(2, 0), (1, 1), (0, 2)})
        reachable = {
            vector
            for vector in relation
            if star_terminal_is_causally_reachable(vector, 2)
        }
        self.assertEqual(reachable, {(1, 1)})
        self.assertEqual(
            star_concentrated_unreachable_minimum_witness(2, 2),
            (2, 0),
        )

        for leaf_count in range(2, 9):
            self.assertTrue(
                star_minimum_relation_is_fully_causally_reachable(
                    leaf_count, 1
                )
            )
            self.assertIsNone(
                star_concentrated_unreachable_minimum_witness(
                    leaf_count, 1
                )
            )

    def test_concentrated_witness_exists_exactly_for_two_through_k_closing(self):
        for leaf_count in range(2, 10):
            for closing_quantum in range(1, leaf_count + 3):
                witness = star_concentrated_unreachable_minimum_witness(
                    leaf_count, closing_quantum
                )
                expected = 2 <= closing_quantum <= leaf_count
                self.assertEqual(witness is not None, expected)
                if witness is not None:
                    self.assertEqual(
                        sum(witness),
                        star_minimum_total_impulse(
                            leaf_count, closing_quantum
                        ),
                    )
                    self.assertTrue(
                        all(
                            score >= 0
                            for score in star_score_vector(
                                witness, closing_quantum
                            )
                        )
                    )
                    self.assertFalse(
                        star_terminal_is_causally_reachable(
                            witness, closing_quantum
                        )
                    )

    def test_k2_q3_local_schedulers_change_total_delivered_impulse(self):
        lowest = star_run_local_unit_policy(2, 3, "LOWEST_INDEX")
        balanced = star_run_local_unit_policy(2, 3, "LEAST_USED")

        self.assertEqual(lowest.contact_word, (0, 0, 1))
        self.assertEqual(lowest.terminal_impulse, (2, 1))
        self.assertEqual(lowest.terminal_scores, (2, 1))
        self.assertEqual(lowest.delivered_total, 3)
        self.assertEqual(lowest.global_minimum_total, 2)
        self.assertEqual(lowest.overdelivery, 1)

        self.assertEqual(balanced.contact_word, (0, 1))
        self.assertEqual(balanced.terminal_impulse, (1, 1))
        self.assertEqual(balanced.terminal_scores, (0, 0))
        self.assertEqual(balanced.delivered_total, 2)
        self.assertEqual(balanced.global_minimum_total, 2)
        self.assertEqual(balanced.overdelivery, 0)

        self.assertEqual(
            {sum(state) for state in independent_terminal_states(2, 3)},
            {2, 3},
        )

    def test_q_one_and_q_two_have_schedule_independent_terminal_total(self):
        for leaf_count in range(2, 9):
            self.assertEqual(
                {sum(state) for state in independent_terminal_states(leaf_count, 1)},
                {1},
            )
            self.assertEqual(
                {sum(state) for state in independent_terminal_states(leaf_count, 2)},
                {2},
            )
        # k=2 is the smallest allowed star, so k=2,q=3 is the first possible
        # closing magnitude where terminal total can depend on local schedule.
        self.assertEqual(
            {sum(state) for state in independent_terminal_states(2, 3)},
            {2, 3},
        )

    def test_every_executed_local_word_has_length_at_most_q(self):
        for leaf_count in range(2, 6):
            for closing_quantum in range(1, 10):
                states = independent_reachable_states(
                    leaf_count, closing_quantum
                )
                self.assertLessEqual(
                    max(sum(state) for state in states),
                    closing_quantum,
                )
                for policy in ("LOWEST_INDEX", "LEAST_USED"):
                    report = star_run_local_unit_policy(
                        leaf_count, closing_quantum, policy
                    )
                    self.assertLessEqual(
                        len(report.contact_word), closing_quantum
                    )
                    self.assertTrue(
                        star_terminal_is_causally_reachable(
                            report.terminal_impulse,
                            closing_quantum,
                        )
                    )

    def test_legal_contact_surface_matches_direct_negative_scores(self):
        for leaf_count in range(2, 5):
            for closing_quantum in range(1, 6):
                for state in independent_reachable_states(
                    leaf_count, closing_quantum
                ):
                    scores = star_score_vector(state, closing_quantum)
                    expected = tuple(
                        index
                        for index, score in enumerate(scores)
                        if score < 0
                    )
                    self.assertEqual(
                        star_local_legal_contacts(
                            state, closing_quantum
                        ),
                        expected,
                    )

    def test_illegal_local_actions_are_rejected(self):
        self.assertEqual(
            star_apply_local_unit_update((0, 0), 1, 0),
            (1, 0),
        )
        with self.assertRaises(ValueError):
            star_apply_local_unit_update((1, 0), 1, 0)
        with self.assertRaises(ValueError):
            star_apply_local_unit_update((0, 0), 1, 2)
        with self.assertRaises(ValueError):
            star_replay_local_contact_word(2, 1, (0, 1))
        with self.assertRaises(ValueError):
            star_run_local_unit_policy(2, 3, "UNKNOWN")
        with self.assertRaises(ValueError):
            star_terminal_is_causally_reachable((1,), 2)
        with self.assertRaises(ValueError):
            star_terminal_is_causally_reachable((1, -1), 2)


if __name__ == "__main__":
    unittest.main()
