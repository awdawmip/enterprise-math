import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
    impulse_vector_makes_all_contacts_nonclosing,
)
from enterprise_math.material_z_contact_least_action_1d import (
    CYCLE,
    PATH,
    contact_coupling_is_z_matrix,
    contact_z_local_sign_condition,
    solve_z_contact_network_least_action,
    z_contact_topology_report,
)


class MaterialZContactLeastAction1DTests(unittest.TestCase):
    def test_local_degree_sign_criterion_equals_direct_z_gram_on_all_four_body_directed_simple_graphs(self):
        body_count = 4
        possible = tuple(itertools.combinations(range(body_count), 2))
        checked = 0
        for choices in itertools.product((0, 1, -1), repeat=len(possible)):
            contacts = tuple(
                ContactChannel1D(left, right, choice)
                for (left, right), choice in zip(possible, choices)
                if choice
            )
            state = ContactNetworkMomentum1D(
                masses=(2, 3, 5, 7),
                momenta=(0, 0, 0, 0),
                contacts=contacts,
            )
            self.assertEqual(
                contact_z_local_sign_condition(state),
                contact_coupling_is_z_matrix(state),
            )
            report = z_contact_topology_report(state)
            self.assertEqual(report.local_sign_condition, report.coupling_is_z_matrix)
            checked += 1
        self.assertEqual(checked, 3 ** len(possible))

    def test_z_components_are_only_paths_or_cycles(self):
        path = ContactNetworkMomentum1D(
            masses=(1, 3, 2, 1),
            momenta=(9, 0, 6, 4),
            contacts=(
                ContactChannel1D(0, 3, 1),
                ContactChannel1D(2, 0, 1),
                ContactChannel1D(1, 3, -1),
            ),
        )
        report = z_contact_topology_report(path)
        self.assertTrue(report.coupling_is_z_matrix)
        self.assertEqual(tuple(component.kind for component in report.components), (PATH,))

        cycle = ContactNetworkMomentum1D(
            masses=(1, 2, 3),
            momenta=(1, 2, 3),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        cycle_report = z_contact_topology_report(cycle)
        self.assertTrue(cycle_report.coupling_is_z_matrix)
        self.assertEqual(tuple(component.kind for component in cycle_report.components), (CYCLE,))

    def test_arbitrarily_labeled_coherent_path_reuses_weighted_least_action(self):
        state = ContactNetworkMomentum1D(
            masses=(3, 1, 1, 2),
            momenta=(9, 0, 6, 4),
            contacts=(
                ContactChannel1D(0, 3, 1),
                ContactChannel1D(2, 0, 1),
                ContactChannel1D(1, 3, -1),
            ),
        )
        # Traversal is body 2 -> 0 -> 3 -> 1.  The weighted path solution in
        # traversal contact order is (4,5,3), hence original edge order is (5,4,3).
        self.assertEqual(contact_relative_scores(state), (-6, -18, -12))
        solution = solve_z_contact_network_least_action(state)
        self.assertEqual(solution.impulse_vector, (5, 4, 3))
        self.assertEqual(solution.final_scores, (2, 4, 0))
        self.assertEqual(sum(solution.final_momenta), sum(state.momenta))
        self.assertEqual(solution.component_solutions[0][0], PATH)

    def test_disconnected_paths_solve_independently(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2, 1, 2),
            momenta=(4, 4, 3, 2),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        self.assertEqual(contact_relative_scores(state), (-4, -4))
        report = z_contact_topology_report(state)
        self.assertTrue(report.coupling_is_z_matrix)
        self.assertEqual(tuple(component.kind for component in report.components), (PATH, PATH))
        solution = solve_z_contact_network_least_action(state)
        self.assertEqual(solution.impulse_vector, (2, 2))
        # Each isolated weighted pair has K=(3) and initial score -4, so the
        # least integer impulse is ceil(4/3)=2 and leaves the exact unavoidable
        # positive surplus -4+3*2=+2.  Independence does not imply exact zero.
        self.assertEqual(solution.final_scores, (2, 2))

    def test_coherent_cycle_with_all_nonpositive_scores_is_already_zero(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2, 3),
            momenta=(1, 2, 3),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        self.assertEqual(contact_relative_scores(state), (0, 0, 0))
        solution = solve_z_contact_network_least_action(state)
        self.assertEqual(solution.impulse_vector, (0, 0, 0))
        self.assertEqual(solution.final_scores, (0, 0, 0))
        self.assertEqual(solution.component_solutions[0][0], CYCLE)

    def test_coherent_cycle_cannot_have_nonzero_all_nonpositive_score_vector_on_bounded_momenta(self):
        contacts = (
            ContactChannel1D(0, 1, 1),
            ContactChannel1D(1, 2, 1),
            ContactChannel1D(2, 0, 1),
        )
        for momenta in itertools.product(range(-3, 4), repeat=3):
            state = ContactNetworkMomentum1D(
                masses=(2, 3, 5),
                momenta=momenta,
                contacts=contacts,
            )
            scores = contact_relative_scores(state)
            if all(score <= 0 for score in scores):
                self.assertEqual(scores, (0, 0, 0))

    def test_degree_three_star_is_sharp_failure_of_least_action_lattice(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        self.assertEqual(contact_relative_scores(state), (-1, -1, -1))
        self.assertEqual(
            contact_coupling_gram(state),
            ((2, 1, 1), (1, 2, 1), (1, 1, 2)),
        )
        self.assertFalse(contact_coupling_is_z_matrix(state))
        self.assertFalse(contact_z_local_sign_condition(state))
        for candidate in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            self.assertTrue(impulse_vector_makes_all_contacts_nonclosing(state, candidate))
        self.assertFalse(impulse_vector_makes_all_contacts_nonclosing(state, (0, 0, 0)))
        with self.assertRaises(ValueError):
            solve_z_contact_network_least_action(state)

    def test_degree_two_same_incidence_sign_already_breaks_z_coupling(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(1, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        self.assertEqual(contact_coupling_gram(state), ((2, 1), (1, 2)))
        self.assertFalse(contact_coupling_is_z_matrix(state))
        self.assertFalse(contact_z_local_sign_condition(state))

    def test_z_path_requires_no_initially_separating_contact(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(0, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        self.assertTrue(contact_coupling_is_z_matrix(state))
        self.assertTrue(any(score > 0 for score in contact_relative_scores(state)))
        with self.assertRaises(ValueError):
            solve_z_contact_network_least_action(state)


if __name__ == "__main__":
    unittest.main()
