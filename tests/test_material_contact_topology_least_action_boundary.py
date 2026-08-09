import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from enterprise_math.material_contact_topology_least_action_boundary import (
    contact_gram_is_z_matrix,
    contact_z_topology_certificate,
    z_cycle_nonseparating_scores_are_comoving,
)


def network_state(body_count, edges, normals, masses=None, momenta=None):
    if masses is None:
        masses = (1,) * body_count
    if momenta is None:
        momenta = (0,) * body_count
    return ContactNetworkMomentum1D(
        masses=tuple(masses),
        momenta=tuple(momenta),
        contacts=tuple(
            ContactChannel1D(left, right, normal)
            for (left, right), normal in zip(edges, normals)
        ),
    )


def greedy_unit_updates(state, priority):
    gram = contact_coupling_gram(state)
    scores = list(contact_relative_scores(state))
    impulses = [0] * len(state.contacts)
    for _ in range(32):
        violated = {index for index, score in enumerate(scores) if score < 0}
        if not violated:
            return tuple(impulses), tuple(scores)
        chosen = next(index for index in priority if index in violated)
        impulses[chosen] += 1
        for row in range(len(scores)):
            scores[row] += gram[row][chosen]
    raise AssertionError("bounded branching comparator did not terminate")


class MaterialContactTopologyLeastActionBoundaryTests(unittest.TestCase):
    def test_exact_z_topology_characterization_exhaustive_through_four_bodies(self):
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
                    masses = tuple(range(1, body_count + 1))
                    state = network_state(body_count, edges, normals, masses=masses)
                    certificate = contact_z_topology_certificate(state)
                    gram = contact_coupling_gram(state)
                    direct = all(
                        row == col or gram[row][col] <= 0
                        for row in range(len(gram))
                        for col in range(len(gram))
                    )
                    self.assertEqual(certificate.gram_is_z_matrix, direct)
                    self.assertEqual(contact_gram_is_z_matrix(state), direct)
                    self.assertEqual(
                        certificate.topology_condition_holds,
                        not certificate.branching_bodies
                        and not certificate.degree_two_orientation_defects,
                    )
                    if direct:
                        self.assertTrue(certificate.z_components_are_paths_or_cycles)
                        self.assertFalse(certificate.branching_bodies)
                    checked += 1
        self.assertGreater(checked, 700)

    def test_canonical_paths_and_directed_cycles_are_exact_z_components(self):
        path = network_state(
            5,
            ((0, 1), (1, 2), (2, 3), (3, 4)),
            (1, 1, 1, 1),
            masses=(2, 3, 5, 7, 11),
        )
        path_certificate = contact_z_topology_certificate(path)
        self.assertTrue(path_certificate.gram_is_z_matrix)
        self.assertEqual(tuple(component.kind for component in path_certificate.components), ("PATH",))

        cycle = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 3, 1),
                ContactChannel1D(3, 0, 1),
            ),
        )
        cycle_certificate = contact_z_topology_certificate(cycle)
        self.assertTrue(cycle_certificate.gram_is_z_matrix)
        self.assertEqual(tuple(component.kind for component in cycle_certificate.components), ("CYCLE",))
        self.assertEqual(cycle_certificate.cycle_score_sums, (((0, 1, 2, 3), 0),))

    def test_degree_two_orientation_defect_is_exact_positive_coupling_witness(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, -1),
            ),
        )
        certificate = contact_z_topology_certificate(state)
        self.assertFalse(certificate.gram_is_z_matrix)
        self.assertEqual(certificate.body_degrees, (1, 2, 1))
        self.assertEqual(certificate.degree_two_orientation_defects, (1,))
        self.assertGreater(certificate.coupling_gram[0][1], 0)

    def test_directed_cycle_score_sum_is_zero_and_all_nonseparating_means_comoving(self):
        contacts = (
            ContactChannel1D(0, 1, 1),
            ContactChannel1D(1, 2, 1),
            ContactChannel1D(2, 0, 1),
        )
        mixed = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(7, -1, 4),
            contacts=contacts,
        )
        mixed_scores = contact_relative_scores(mixed)
        self.assertEqual(sum(mixed_scores), 0)
        self.assertTrue(any(score < 0 for score in mixed_scores))
        self.assertTrue(any(score > 0 for score in mixed_scores))
        with self.assertRaises(ValueError):
            z_cycle_nonseparating_scores_are_comoving(mixed)

        comoving = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(2, 3, 5),
            contacts=contacts,
        )
        self.assertEqual(contact_relative_scores(comoving), (0, 0, 0))
        self.assertTrue(z_cycle_nonseparating_scores_are_comoving(comoving))

        checked = 0
        for momenta in itertools.product(range(-2, 3), repeat=3):
            state = ContactNetworkMomentum1D(
                masses=(1, 1, 1),
                momenta=momenta,
                contacts=contacts,
            )
            scores = contact_relative_scores(state)
            if any(score > 0 for score in scores):
                continue
            self.assertEqual(scores, (0, 0, 0))
            self.assertTrue(z_cycle_nonseparating_scores_are_comoving(state))
            checked += 1
        self.assertGreater(checked, 0)

    def test_three_edge_star_is_minimal_branching_policy_counterexample(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        certificate = contact_z_topology_certificate(state)
        self.assertFalse(certificate.gram_is_z_matrix)
        self.assertEqual(certificate.branching_bodies, (0,))
        self.assertEqual(contact_relative_scores(state), (-1, -1, -1))
        self.assertEqual(
            certificate.coupling_gram,
            ((2, 1, 1), (1, 2, 1), (1, 1, 2)),
        )

        feasible_units = []
        for chosen in range(3):
            impulse = tuple(1 if index == chosen else 0 for index in range(3))
            step = apply_contact_impulse_vector(state, impulse)
            self.assertTrue(all(score >= 0 for score in step.relative_scores_after))
            feasible_units.append(impulse)
        self.assertEqual(
            tuple(
                min(candidate[index] for candidate in feasible_units)
                for index in range(3)
            ),
            (0, 0, 0),
        )
        self.assertTrue(
            any(
                score < 0
                for score in apply_contact_impulse_vector(state, (0, 0, 0)).relative_scores_after
            )
        )

        terminal = {
            greedy_unit_updates(state, priority)[0]
            for priority in itertools.permutations(range(3))
        }
        self.assertEqual(terminal, {(1, 0, 0), (0, 1, 0), (0, 0, 1)})

    def test_mixed_components_only_force_cycle_contacts_to_comove(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1, 1),
            momenta=(2, 2, 2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
                ContactChannel1D(3, 4, 1),
            ),
        )
        scores = contact_relative_scores(state)
        self.assertEqual(scores[:3], (0, 0, 0))
        self.assertEqual(scores[3], -1)
        certificate = contact_z_topology_certificate(state)
        self.assertTrue(certificate.gram_is_z_matrix)
        self.assertEqual(
            tuple(sorted(component.kind for component in certificate.components)),
            ("CYCLE", "PATH"),
        )
        self.assertTrue(z_cycle_nonseparating_scores_are_comoving(state))


if __name__ == "__main__":
    unittest.main()
