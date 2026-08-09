import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from enterprise_math.material_guarded_contact_actions import (
    apply_guarded_contact_unit,
    contact_actor_disables_closing_target,
    contact_cross_guard_delta,
    contact_guarded_unit_is_legal,
    contact_network_has_no_cross_disable_guarantee,
    guarded_contact_pair_report,
)
from enterprise_math.material_z_contact_least_action_1d import (
    z_contact_topology_report,
)


def path_state(momenta=(2, 1, 0)):
    return ContactNetworkMomentum1D(
        masses=(1, 1, 1),
        momenta=tuple(momenta),
        contacts=(
            ContactChannel1D(0, 1, 1),
            ContactChannel1D(1, 2, 1),
        ),
    )


def same_sign_v_state(momenta=(2, 1, 0)):
    return ContactNetworkMomentum1D(
        masses=(1, 1, 1),
        momenta=tuple(momenta),
        contacts=(
            ContactChannel1D(0, 1, 1),
            ContactChannel1D(0, 2, 1),
        ),
    )


def star_state(leaf_count, center_momentum=1):
    return ContactNetworkMomentum1D(
        masses=(1,) * (leaf_count + 1),
        momenta=(center_momentum,) + (0,) * leaf_count,
        contacts=tuple(
            ContactChannel1D(0, leaf + 1, 1)
            for leaf in range(leaf_count)
        ),
    )


class MaterialGuardedContactActionTests(unittest.TestCase):
    def test_unguarded_unit_impulses_commute_exactly_over_small_states(self):
        checked = 0
        for factory in (path_state, same_sign_v_state):
            for momenta in itertools.product(range(-2, 3), repeat=3):
                state = factory(momenta)
                count = len(state.contacts)
                for left, right in itertools.permutations(range(count), 2):
                    left_unit = tuple(1 if i == left else 0 for i in range(count))
                    right_unit = tuple(1 if i == right else 0 for i in range(count))
                    left_then_right = apply_contact_impulse_vector(
                        apply_contact_impulse_vector(state, left_unit).after,
                        right_unit,
                    ).after
                    right_then_left = apply_contact_impulse_vector(
                        apply_contact_impulse_vector(state, right_unit).after,
                        left_unit,
                    ).after
                    self.assertEqual(left_then_right, right_then_left)
                    report = guarded_contact_pair_report(state, left, right)
                    self.assertTrue(report.unguarded_actions_commute)
                    self.assertEqual(
                        report.unguarded_final_momenta,
                        left_then_right.momenta,
                    )
                    checked += 1
        self.assertGreater(checked, 400)

    def test_aligned_z_path_has_guarded_pair_commutation(self):
        state = path_state()
        self.assertEqual(contact_relative_scores(state), (-1, -1))
        self.assertEqual(contact_coupling_gram(state), ((2, -1), (-1, 2)))
        self.assertTrue(contact_network_has_no_cross_disable_guarantee(state))
        report = guarded_contact_pair_report(state, 0, 1)
        self.assertEqual(report.cross_coupling, -1)
        self.assertTrue(report.left_initially_legal)
        self.assertTrue(report.right_initially_legal)
        self.assertTrue(report.both_guarded_orders_defined)
        self.assertTrue(report.guarded_pair_commutes_when_defined)
        self.assertFalse(report.guard_domain_is_order_sensitive)
        self.assertEqual(report.left_then_right_final_momenta, (1, 1, 1))
        self.assertEqual(report.right_then_left_final_momenta, (1, 1, 1))
        self.assertFalse(contact_actor_disables_closing_target(state, 0, 1))
        self.assertFalse(contact_actor_disables_closing_target(state, 1, 0))

    def test_positive_cross_coupling_creates_exact_order_sensitive_guard_domain(self):
        state = same_sign_v_state()
        self.assertEqual(contact_relative_scores(state), (-1, -2))
        self.assertEqual(contact_coupling_gram(state), ((2, 1), (1, 2)))
        self.assertFalse(contact_network_has_no_cross_disable_guarantee(state))
        report = guarded_contact_pair_report(state, 0, 1)
        self.assertEqual(report.cross_coupling, 1)
        self.assertTrue(report.left_initially_legal)
        self.assertTrue(report.right_initially_legal)
        self.assertTrue(report.left_then_right_defined)
        self.assertFalse(report.right_then_left_defined)
        self.assertTrue(report.guard_domain_is_order_sensitive)
        self.assertFalse(report.guarded_pair_commutes_when_defined)
        self.assertFalse(contact_actor_disables_closing_target(state, 0, 1))
        self.assertTrue(contact_actor_disables_closing_target(state, 1, 0))

        after_right = apply_guarded_contact_unit(state, 1).after
        self.assertEqual(contact_relative_scores(after_right), (0, 0))
        self.assertFalse(contact_guarded_unit_is_legal(after_right, 0))

    def test_positive_coupling_competition_band_is_exact_over_small_v_states(self):
        checked = 0
        for momenta in itertools.product(range(-3, 4), repeat=3):
            state = same_sign_v_state(momenta)
            scores = contact_relative_scores(state)
            coupling = contact_cross_guard_delta(state, 0, 1)
            self.assertEqual(coupling, 1)
            if scores[0] < 0 and scores[1] < 0:
                self.assertEqual(
                    contact_actor_disables_closing_target(state, 0, 1),
                    -coupling <= scores[1] < 0,
                )
                self.assertEqual(
                    contact_actor_disables_closing_target(state, 1, 0),
                    -coupling <= scores[0] < 0,
                )
                checked += 1
        self.assertGreater(checked, 20)

    def test_unequal_mass_shared_body_sets_algebraic_competition_width(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(1, 1, 1),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        self.assertEqual(state.body_scale_weights, (15, 10, 6))
        self.assertEqual(contact_relative_scores(state), (-5, -9))
        gram = contact_coupling_gram(state)
        self.assertEqual(gram[0][1], 15)
        self.assertEqual(gram[1][0], 15)
        self.assertEqual(contact_cross_guard_delta(state, 0, 1), 15)
        self.assertTrue(contact_actor_disables_closing_target(state, 0, 1))
        self.assertTrue(contact_actor_disables_closing_target(state, 1, 0))
        after_zero = apply_guarded_contact_unit(state, 0).after
        self.assertEqual(contact_relative_scores(after_zero)[1], 6)

    def test_q1_branching_star_first_action_disables_every_other_closing_guard(self):
        for leaf_count in range(3, 8):
            state = star_state(leaf_count)
            self.assertEqual(contact_relative_scores(state), (-1,) * leaf_count)
            gram = contact_coupling_gram(state)
            self.assertTrue(
                all(
                    row == col or gram[row][col] == 1
                    for row in range(leaf_count)
                    for col in range(leaf_count)
                )
            )
            for actor in range(leaf_count):
                for target in range(leaf_count):
                    if actor == target:
                        continue
                    self.assertTrue(
                        contact_actor_disables_closing_target(
                            state, actor, target
                        )
                    )
                after = apply_guarded_contact_unit(state, actor).after
                self.assertEqual(
                    tuple(
                        score
                        for index, score in enumerate(contact_relative_scores(after))
                        if index != actor
                    ),
                    (0,) * (leaf_count - 1),
                )

    def test_z_topology_owner_matches_no_cross_disable_sign_guarantee(self):
        checked = 0
        for body_count in range(2, 5):
            possible_edges = tuple(itertools.combinations(range(body_count), 2))
            for mask in range(1 << len(possible_edges)):
                edges = tuple(
                    edge
                    for index, edge in enumerate(possible_edges)
                    if mask & (1 << index)
                )
                for normals in itertools.product((-1, 1), repeat=len(edges)):
                    state = ContactNetworkMomentum1D(
                        masses=tuple(range(1, body_count + 1)),
                        momenta=(0,) * body_count,
                        contacts=tuple(
                            ContactChannel1D(a, b, normal)
                            for (a, b), normal in zip(edges, normals)
                        ),
                    )
                    self.assertEqual(
                        contact_network_has_no_cross_disable_guarantee(state),
                        z_contact_topology_report(state).coupling_is_z_matrix,
                    )
                    checked += 1
        self.assertGreater(checked, 700)

    def test_nonpositive_cross_coupling_never_disables_another_closing_contact(self):
        checked = 0
        for momenta in itertools.product(range(-4, 5), repeat=3):
            state = path_state(momenta)
            scores = contact_relative_scores(state)
            if scores[0] < 0 and scores[1] < 0:
                self.assertLessEqual(contact_cross_guard_delta(state, 0, 1), 0)
                self.assertFalse(contact_actor_disables_closing_target(state, 0, 1))
                self.assertFalse(contact_actor_disables_closing_target(state, 1, 0))
                report = guarded_contact_pair_report(state, 0, 1)
                self.assertTrue(report.both_guarded_orders_defined)
                self.assertTrue(report.guarded_pair_commutes_when_defined)
                checked += 1
        self.assertGreater(checked, 20)

    def test_validation(self):
        state = path_state()
        with self.assertRaises(ValueError):
            contact_guarded_unit_is_legal(state, 2)
        with self.assertRaises(ValueError):
            apply_guarded_contact_unit(state, -1)
        with self.assertRaises(ValueError):
            contact_cross_guard_delta(state, 0, 0)
        with self.assertRaises(ValueError):
            contact_actor_disables_closing_target(state, 1, 1)
        with self.assertRaises(ValueError):
            guarded_contact_pair_report(state, 0, 0)


if __name__ == "__main__":
    unittest.main()
