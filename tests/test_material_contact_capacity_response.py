import itertools
import unittest

from enterprise_math.material_contact_capacity_response import (
    MATERIAL_CAPACITY_INSUFFICIENT,
    MATERIAL_CAPACITY_RESOLVED,
    capacity_relation_is_permutation_closed,
    impulse_respects_contact_capacities,
    minimum_total_response_under_capacities,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
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


class MaterialContactCapacityResponseTests(unittest.TestCase):
    def test_symmetric_q_one_star_keeps_full_unit_relation_under_equal_capacity(self):
        state = star_state(3, 1)
        report = minimum_total_response_under_capacities(state, (1, 1, 1))
        self.assertEqual(report.status, MATERIAL_CAPACITY_RESOLVED)
        self.assertEqual(report.minimum_total_impulse, 1)
        self.assertEqual(
            set(report.response_relation),
            {(1, 0, 0), (0, 1, 0), (0, 0, 1)},
        )
        self.assertFalse(report.single_valued)
        self.assertTrue(
            capacity_relation_is_permutation_closed(
                report.response_relation,
                tuple(itertools.permutations(range(3))),
            )
        )

    def test_asymmetric_capacity_can_select_one_response_without_id_tie_break(self):
        state = star_state(3, 1)
        report = minimum_total_response_under_capacities(state, (1, 0, 0))
        self.assertTrue(report.resolved)
        self.assertTrue(report.single_valued)
        self.assertEqual(report.response_relation, ((1, 0, 0),))
        self.assertFalse(
            capacity_relation_is_permutation_closed(
                report.response_relation,
                ((1, 0, 2),),
            )
        )

    def test_zero_capacity_is_material_insufficiency_not_search_underresolution(self):
        state = star_state(3, 1)
        report = minimum_total_response_under_capacities(state, (0, 0, 0))
        self.assertEqual(report.status, MATERIAL_CAPACITY_INSUFFICIENT)
        self.assertFalse(report.resolved)
        self.assertIsNone(report.minimum_total_impulse)
        self.assertEqual(report.response_relation, ())
        self.assertEqual(report.total_available_capacity, 0)

    def test_q_two_unit_cap_removes_concentrated_shapes_but_preserves_split_orbit(self):
        state = star_state(3, 2)
        report = minimum_total_response_under_capacities(state, (1, 1, 1))
        self.assertTrue(report.resolved)
        self.assertEqual(report.minimum_total_impulse, 2)
        self.assertEqual(
            set(report.response_relation),
            {(1, 1, 0), (1, 0, 1), (0, 1, 1)},
        )
        self.assertTrue(
            capacity_relation_is_permutation_closed(
                report.response_relation,
                tuple(itertools.permutations(range(3))),
            )
        )

    def test_q_two_capacity_two_recovers_full_unconstrained_minimum_relation(self):
        state = star_state(3, 2)
        report = minimum_total_response_under_capacities(state, (2, 2, 2))
        self.assertEqual(report.minimum_total_impulse, 2)
        self.assertEqual(len(report.response_relation), 6)
        self.assertEqual(
            set(report.response_relation),
            {
                (2, 0, 0), (0, 2, 0), (0, 0, 2),
                (1, 1, 0), (1, 0, 1), (0, 1, 1),
            },
        )

    def test_material_capacity_can_make_weighted_path_unresolvable_in_current_tick(self):
        state = path_state((2, 3, 5), (6, 6, 0))
        insufficient = minimum_total_response_under_capacities(state, (4, 6))
        self.assertEqual(insufficient.status, MATERIAL_CAPACITY_INSUFFICIENT)
        resolved = minimum_total_response_under_capacities(state, (4, 7))
        self.assertEqual(resolved.response_relation, ((4, 7),))
        self.assertEqual(resolved.minimum_total_impulse, 11)

    def test_capacity_only_removes_candidates_and_never_creates_lower_total_than_unconstrained_oracle(self):
        states = (star_state(3, 1), star_state(3, 2))
        capacity_families = (
            ((1, 1, 1), (1, 0, 1), (2, 1, 0)),
            ((1, 1, 1), (2, 2, 2), (2, 1, 0)),
        )
        unconstrained_minima = (1, 2)
        for state, families, unconstrained in zip(
            states, capacity_families, unconstrained_minima
        ):
            for capacities in families:
                report = minimum_total_response_under_capacities(state, capacities)
                if report.resolved:
                    self.assertGreaterEqual(report.minimum_total_impulse, unconstrained)
                    self.assertTrue(
                        all(
                            impulse_respects_contact_capacities(vector, capacities)
                            for vector in report.response_relation
                        )
                    )

    def test_more_capacity_cannot_destroy_an_already_feasible_response_vector(self):
        state = star_state(3, 2)
        low = (1, 1, 1)
        high = (2, 2, 2)
        low_relation = minimum_total_response_under_capacities(state, low)
        high_relation = minimum_total_response_under_capacities(state, high)
        self.assertTrue(low_relation.resolved)
        self.assertTrue(high_relation.resolved)
        self.assertTrue(
            set(low_relation.response_relation).issubset(
                set(high_relation.response_relation)
            )
        )

    def test_validation(self):
        state = star_state(3, 1)
        with self.assertRaises(ValueError):
            minimum_total_response_under_capacities(state, (1, 1))
        with self.assertRaises(ValueError):
            minimum_total_response_under_capacities(state, (1, -1, 1))
        with self.assertRaises(ValueError):
            impulse_respects_contact_capacities((1, 0), (1,))
        with self.assertRaises(ValueError):
            impulse_respects_contact_capacities((1, -1), (1, 1))
        with self.assertRaises(ValueError):
            capacity_relation_is_permutation_closed((), ((0,),))
        with self.assertRaises(ValueError):
            capacity_relation_is_permutation_closed(((1, 0),), ((0,),))


if __name__ == "__main__":
    unittest.main()
