import unittest
from functools import lru_cache
from itertools import product

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
    apply_contact_material_tick,
)
from enterprise_math.material_contact_tick_policy import (
    GREEDY_CHOOSERS,
    compare_batched_tick_to_guarded_sequential,
    coupling_is_diagonal,
    coupling_is_z_matrix,
    diagonal_guarded_realizable_closed_form,
    exact_guarded_impulse_realization,
    score_after_counts,
    z_greedy_guarded_realization,
)


PATH = ContactNetworkMomentum1D(
    masses=(1, 1, 1),
    momenta=(2, 1, 0),
    contacts=(
        ContactChannel1D(0, 1, 1),
        ContactChannel1D(1, 2, 1),
    ),
)

STAR_Q1 = ContactNetworkMomentum1D(
    masses=(1, 1, 1, 1),
    momenta=(1, 0, 0, 0),
    contacts=(
        ContactChannel1D(0, 1, 1),
        ContactChannel1D(0, 2, 1),
        ContactChannel1D(0, 3, 1),
    ),
)


def direct_step(scores, coupling, action):
    if scores[action] >= 0:
        return None
    return tuple(
        scores[row] + coupling[row][action]
        for row in range(len(scores))
    )


def direct_guarded_realizable(initial_scores, coupling, target_counts):
    """Independent literal-action DFS oracle; it does not use prefix formulas."""
    target = tuple(target_counts)

    @lru_cache(maxsize=None)
    def visit(scores, remaining):
        if not any(remaining):
            return True
        for action, count in enumerate(remaining):
            if count == 0:
                continue
            after = direct_step(scores, coupling, action)
            if after is None:
                continue
            nxt = tuple(
                value - (1 if index == action else 0)
                for index, value in enumerate(remaining)
            )
            if visit(after, nxt):
                return True
        return False

    return visit(tuple(initial_scores), target)


def direct_word_is_legal(initial_scores, coupling, word):
    current = tuple(initial_scores)
    for action in word:
        current = direct_step(current, coupling, action)
        if current is None:
            return False
    return True


def word_counts(word, dimension):
    return tuple(word.count(index) for index in range(dimension))


class MaterialContactTickPolicyTests(unittest.TestCase):
    def test_prefix_score_formula_matches_direct_unguarded_column_addition(self):
        coupling = (
            (2, -1, 0),
            (-1, 2, -1),
            (0, -1, 2),
        )
        initial = (-3, -1, 2)
        for counts in product(range(3), repeat=3):
            direct = list(initial)
            for action, count in enumerate(counts):
                for _ in range(count):
                    direct = [
                        direct[row] + coupling[row][action]
                        for row in range(3)
                    ]
            self.assertEqual(
                score_after_counts(initial, coupling, counts),
                tuple(direct),
            )

    def test_exact_count_lattice_bfs_matches_independent_literal_oracle(self):
        matrices = (
            ((2, -1), (-1, 2)),
            ((2, -2), (0, 1)),
            ((0, -1), (-2, -1)),
            ((2, 1), (1, 2)),
            ((1, 2), (-1, 1)),
        )
        for coupling in matrices:
            for initial in product(range(-2, 2), repeat=2):
                for target in product(range(3), repeat=2):
                    expected = direct_guarded_realizable(
                        initial,
                        coupling,
                        target,
                    )
                    actual = exact_guarded_impulse_realization(
                        initial,
                        coupling,
                        target,
                    )
                    self.assertEqual(
                        actual.realizable,
                        expected,
                        (initial, coupling, target),
                    )
                    if actual.realizable:
                        self.assertIsNotNone(actual.word)
                        assert actual.word is not None
                        self.assertEqual(
                            word_counts(actual.word, 2),
                            target,
                        )
                        self.assertTrue(
                            direct_word_is_legal(
                                initial,
                                coupling,
                                actual.word,
                            )
                        )

    def test_z_greedy_all_declared_policies_match_exact_realizability(self):
        z_matrices = (
            ((2, -1), (-1, 2)),
            ((2, -2), (0, 1)),
            ((0, -1), (-2, -1)),
            ((-1, 0), (-1, 3)),
            ((2, 0), (0, 2)),
        )
        for coupling in z_matrices:
            self.assertTrue(coupling_is_z_matrix(coupling))
            for initial in product(range(-2, 2), repeat=2):
                for target in product(range(3), repeat=2):
                    exact = direct_guarded_realizable(
                        initial,
                        coupling,
                        target,
                    )
                    for policy in GREEDY_CHOOSERS:
                        greedy = z_greedy_guarded_realization(
                            initial,
                            coupling,
                            target,
                            policy=policy,
                        )
                        self.assertEqual(
                            greedy.realizable,
                            exact,
                            (initial, coupling, target, policy),
                        )
                        if greedy.realizable:
                            self.assertIsNotNone(greedy.word)
                            assert greedy.word is not None
                            self.assertEqual(
                                word_counts(greedy.word, 2),
                                target,
                            )
                            self.assertTrue(
                                direct_word_is_legal(
                                    initial,
                                    coupling,
                                    greedy.word,
                                )
                            )

    def test_three_contact_z_examples_match_bfs_for_small_targets(self):
        matrices = (
            (
                (2, -1, 0),
                (-1, 2, -1),
                (0, -1, 2),
            ),
            (
                (2, -1, -1),
                (-1, 2, -1),
                (-1, -1, 2),
            ),
        )
        initials = (
            (-1, -1, -1),
            (-2, 0, -1),
            (0, -2, -2),
        )
        targets = tuple(
            target
            for target in product(range(3), repeat=3)
            if sum(target) <= 4
        )
        for coupling in matrices:
            for initial in initials:
                for target in targets:
                    exact = exact_guarded_impulse_realization(
                        initial,
                        coupling,
                        target,
                    ).realizable
                    for policy in GREEDY_CHOOSERS:
                        greedy = z_greedy_guarded_realization(
                            initial,
                            coupling,
                            target,
                            policy=policy,
                        )
                        self.assertEqual(greedy.realizable, exact)

    def test_diagonal_closed_form_matches_literal_oracle_for_all_diagonal_signs(self):
        diagonal_pairs = tuple(product(range(-2, 3), repeat=2))
        for left, right in diagonal_pairs:
            coupling = ((left, 0), (0, right))
            self.assertTrue(coupling_is_diagonal(coupling))
            for initial in product(range(-2, 2), repeat=2):
                for target in product(range(4), repeat=2):
                    expected = direct_guarded_realizable(
                        initial,
                        coupling,
                        target,
                    )
                    actual = diagonal_guarded_realizable_closed_form(
                        initial,
                        coupling,
                        target,
                    )
                    self.assertEqual(
                        actual,
                        expected,
                        (initial, coupling, target),
                    )

    def test_negative_diagonal_hidden_assumption_regression(self):
        # The first action is illegal even though the last arithmetic-progression
        # endpoint would be negative.  Checking only the last endpoint is wrong.
        self.assertFalse(
            diagonal_guarded_realizable_closed_form(
                (1,),
                ((-2,),),
                (2,),
            )
        )
        self.assertTrue(
            diagonal_guarded_realizable_closed_form(
                (-1,),
                ((-2,),),
                (4,),
            )
        )

    def test_positive_branching_batch_vector_can_be_causally_unrealizable(self):
        coupling = (
            (2, 1, 1),
            (1, 2, 1),
            (1, 1, 2),
        )
        initial = (-1, -1, -1)
        target = (1, 1, 1)
        exact = exact_guarded_impulse_realization(
            initial,
            coupling,
            target,
        )
        self.assertFalse(exact.realizable)
        self.assertFalse(coupling_is_z_matrix(coupling))
        for first in range(3):
            after_first = direct_step(initial, coupling, first)
            self.assertIsNotNone(after_first)
            assert after_first is not None
            for other in range(3):
                if other != first:
                    self.assertEqual(after_first[other], 0)

    def test_positive_coupling_can_have_one_legal_order_without_commuting_domains(self):
        coupling = ((2, 1), (1, 2))
        initial = (-1, -2)
        target = (1, 1)
        exact = exact_guarded_impulse_realization(initial, coupling, target)
        self.assertTrue(exact.realizable)
        self.assertEqual(exact.word, (0, 1))
        self.assertTrue(direct_word_is_legal(initial, coupling, (0, 1)))
        self.assertFalse(direct_word_is_legal(initial, coupling, (1, 0)))

    def test_material_path_batch_has_guarded_realization_with_same_after_state(self):
        reservoirs = (
            ContactMaterialImpulseState(1, 1, 0),
            ContactMaterialImpulseState(1, 1, 0),
        )
        tick = apply_contact_material_tick(PATH, reservoirs, (1, 1))
        self.assertEqual(tick.delivered_impulse_vector, (1, 1))
        report = compare_batched_tick_to_guarded_sequential(tick)
        self.assertTrue(report.z_coupled)
        self.assertTrue(report.guarded_realizable)
        self.assertTrue(report.batch_after_matches_guarded_after)
        self.assertIsNotNone(report.guarded_word)

    def test_material_star_batch_is_exact_but_has_no_guarded_realization(self):
        reservoirs = tuple(
            ContactMaterialImpulseState(1, 1, 0)
            for _ in range(3)
        )
        tick = apply_contact_material_tick(
            STAR_Q1,
            reservoirs,
            (1, 1, 1),
        )
        self.assertEqual(tick.delivered_impulse_vector, (1, 1, 1))
        report = compare_batched_tick_to_guarded_sequential(tick)
        self.assertFalse(report.z_coupled)
        self.assertFalse(report.guarded_realizable)
        self.assertIsNone(report.guarded_word)
        self.assertIsNone(report.batch_after_matches_guarded_after)
        self.assertEqual(tick.after.total_momentum, STAR_Q1.total_momentum)

    def test_validation(self):
        with self.assertRaises(ValueError):
            exact_guarded_impulse_realization((-1,), ((1,),), (-1,))
        with self.assertRaises(ValueError):
            z_greedy_guarded_realization(
                (-1, -1),
                ((2, 1), (1, 2)),
                (1, 1),
            )
        with self.assertRaises(ValueError):
            z_greedy_guarded_realization(
                (-1,),
                ((1,),),
                (1,),
                policy="UNKNOWN",
            )
        with self.assertRaises(ValueError):
            diagonal_guarded_realizable_closed_form(
                (-1, -1),
                ((2, -1), (-1, 2)),
                (1, 1),
            )


if __name__ == "__main__":
    unittest.main()
