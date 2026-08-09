import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_response_relation import (
    IMPULSE_UNDERRESOLVED,
    MINIMUM_TOTAL_RESOLVED,
    bounded_minimum_total_response_relation,
    contact_impulse_candidate_is_feasible,
    minimum_relation_is_permutation_closed,
    weak_compositions,
)


def star_state(leaf_count, closing_score):
    return ContactNetworkMomentum1D(
        masses=(1,) * (leaf_count + 1),
        momenta=(closing_score,) + (0,) * leaf_count,
        contacts=tuple(
            ContactChannel1D(0, leaf, 1)
            for leaf in range(1, leaf_count + 1)
        ),
    )


def path_state(masses, momenta):
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


class MaterialContactResponseRelationTests(unittest.TestCase):
    def test_weak_compositions_have_exact_count_and_total(self):
        for total in range(0, 7):
            for parts in range(1, 6):
                compositions = weak_compositions(total, parts)
                self.assertEqual(
                    len(compositions),
                    __import__("math").comb(total + parts - 1, parts - 1),
                )
                self.assertTrue(all(sum(vector) == total for vector in compositions))
                self.assertEqual(len(set(compositions)), len(compositions))

    def test_single_pair_relation_is_single_valued(self):
        state = path_state((1, 1), (1, 0))
        report = bounded_minimum_total_response_relation(state, 3)
        self.assertEqual(report.status, MINIMUM_TOTAL_RESOLVED)
        self.assertTrue(report.single_valued)
        self.assertEqual(report.minimum_total_impulse, 1)
        self.assertEqual(report.response_relation, ((1,),))
        self.assertEqual(report.final_score_vectors, ((1,),))

    def test_q_one_three_leaf_star_returns_full_unit_relation(self):
        state = star_state(3, 1)
        report = bounded_minimum_total_response_relation(state, 1)
        self.assertEqual(report.minimum_total_impulse, 1)
        self.assertEqual(
            set(report.response_relation),
            {(1, 0, 0), (0, 1, 0), (0, 0, 1)},
        )
        self.assertFalse(report.single_valued)
        permutations = tuple(itertools.permutations(range(3)))
        self.assertTrue(
            minimum_relation_is_permutation_closed(
                report.response_relation, permutations
            )
        )

    def test_general_star_q_two_relation_has_six_minimizers(self):
        state = star_state(3, 2)
        under = bounded_minimum_total_response_relation(state, 1)
        self.assertEqual(under.status, IMPULSE_UNDERRESOLVED)
        self.assertFalse(under.resolved)
        self.assertEqual(under.response_relation, ())

        report = bounded_minimum_total_response_relation(state, 2)
        self.assertEqual(report.status, MINIMUM_TOTAL_RESOLVED)
        self.assertEqual(report.minimum_total_impulse, 2)
        self.assertEqual(len(report.response_relation), 6)
        self.assertEqual(
            set(report.response_relation),
            {
                (2, 0, 0), (0, 2, 0), (0, 0, 2),
                (1, 1, 0), (1, 0, 1), (0, 1, 1),
            },
        )

    def test_weighted_path_can_still_collapse_to_single_minimum_total_relation(self):
        state = path_state((2, 3, 5), (6, 6, 0))
        report = bounded_minimum_total_response_relation(state, 11)
        self.assertEqual(report.status, MINIMUM_TOTAL_RESOLVED)
        self.assertEqual(report.minimum_total_impulse, 11)
        self.assertEqual(report.response_relation, ((4, 7),))

    def test_first_feasible_layer_is_global_minimum_within_all_smaller_totals(self):
        states = (
            path_state((1, 1, 1), (2, 1, 0)),
            path_state((2, 3, 5), (6, 6, 0)),
            star_state(3, 1),
            star_state(3, 2),
        )
        budgets = (5, 14, 4, 5)
        for state, budget in zip(states, budgets):
            report = bounded_minimum_total_response_relation(state, budget)
            self.assertTrue(report.resolved)
            total = report.minimum_total_impulse
            self.assertIsNotNone(total)
            for smaller in range(total):
                self.assertFalse(
                    any(
                        contact_impulse_candidate_is_feasible(state, candidate)
                        for candidate in weak_compositions(smaller, len(state.contacts))
                    )
                )
            self.assertTrue(
                all(
                    contact_impulse_candidate_is_feasible(state, candidate)
                    for candidate in report.response_relation
                )
            )

    def test_distinct_minimum_total_vectors_are_componentwise_incomparable(self):
        report = bounded_minimum_total_response_relation(star_state(4, 2), 2)
        self.assertTrue(report.resolved)
        for left_index, left in enumerate(report.response_relation):
            for right in report.response_relation[left_index + 1:]:
                self.assertFalse(all(a <= b for a, b in zip(left, right)))
                self.assertFalse(all(b <= a for a, b in zip(left, right)))

    def test_budget_underresolution_does_not_claim_global_infeasibility(self):
        state = path_state((2, 3, 5), (6, 6, 0))
        report = bounded_minimum_total_response_relation(state, 10)
        self.assertEqual(report.status, IMPULSE_UNDERRESOLVED)
        self.assertIsNone(report.minimum_total_impulse)
        self.assertEqual(report.response_relation, ())
        # Raising only the declared search budget resolves the exact same state.
        resolved = bounded_minimum_total_response_relation(state, 11)
        self.assertEqual(resolved.response_relation, ((4, 7),))

    def test_candidate_and_permutation_validation(self):
        state = star_state(3, 1)
        with self.assertRaises(ValueError):
            contact_impulse_candidate_is_feasible(state, (1, 0))
        with self.assertRaises(ValueError):
            contact_impulse_candidate_is_feasible(state, (1, -1, 0))
        with self.assertRaises(ValueError):
            bounded_minimum_total_response_relation(state, -1)
        with self.assertRaises(ValueError):
            weak_compositions(-1, 2)
        with self.assertRaises(ValueError):
            weak_compositions(1, 0)
        with self.assertRaises(ValueError):
            minimum_relation_is_permutation_closed((), ((0,),))
        with self.assertRaises(ValueError):
            minimum_relation_is_permutation_closed(((1, 0),), ((0,),))


if __name__ == "__main__":
    unittest.main()
