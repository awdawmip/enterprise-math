import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_coupling_is_diagonal,
    contact_coupling_quadratic_identity,
    contact_graph_is_matching,
    contact_incidence_matrix,
    contact_relative_scores,
    contact_relative_scores_from_a3,
    diagonal_only_nonclosing_impulse_guess,
    impulse_vector_makes_all_contacts_nonclosing,
    verify_matching_independence_equivalence,
)
from enterprise_math.material_pair_impulse_1d import (
    PairMomentumState1D,
    pair_relative_motion_numerator,
)


class MaterialContactNetworkImpulse1DTests(unittest.TestCase):
    def test_single_contact_score_is_a3_relation_specialization_and_pair_sign(self):
        for left_mass in range(1, 5):
            for right_mass in range(1, 5):
                for left_momentum in range(-3, 4):
                    for right_momentum in range(-3, 4):
                        for normal in (-1, 1):
                            network = ContactNetworkMomentum1D(
                                masses=(left_mass, right_mass),
                                momenta=(left_momentum, right_momentum),
                                contacts=(ContactChannel1D(0, 1, normal),),
                            )
                            scores = contact_relative_scores(network)
                            self.assertEqual(scores, contact_relative_scores_from_a3(network))
                            pair = PairMomentumState1D(
                                left_momentum,
                                right_momentum,
                                left_mass,
                                right_mass,
                                normal,
                            )
                            pair_score = pair_relative_motion_numerator(pair)
                            # The network score is a positive integer rescaling of
                            # the same A3 relation coordinate, so only sign and zero
                            # are compared across the two normalizations.
                            self.assertEqual((scores[0] > 0) - (scores[0] < 0), (pair_score > 0) - (pair_score < 0))

    def test_equal_mass_chain_has_exact_edge_coupling_gram(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(3, 2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        self.assertEqual(
            contact_incidence_matrix(network),
            ((-1, 0, 0), (1, -1, 0), (0, 1, -1), (0, 0, 1)),
        )
        self.assertEqual(contact_relative_scores(network), (-1, -1, -1))
        self.assertEqual(
            contact_coupling_gram(network),
            ((2, -1, 0), (-1, 2, -1), (0, -1, 2)),
        )

    def test_arbitrary_delivered_network_impulses_preserve_total_momentum_and_r_plus_Kj(self):
        networks = (
            ContactNetworkMomentum1D(
                masses=(2, 3, 5),
                momenta=(4, -1, 2),
                contacts=(ContactChannel1D(0, 1, 1), ContactChannel1D(1, 2, -1)),
            ),
            ContactNetworkMomentum1D(
                masses=(1, 2, 3, 4),
                momenta=(-2, 3, 1, -1),
                contacts=(ContactChannel1D(0, 2, -1), ContactChannel1D(1, 3, 1)),
            ),
        )
        for network in networks:
            for impulses in itertools.product(range(4), repeat=len(network.contacts)):
                step = apply_contact_impulse_vector(network, impulses)
                self.assertEqual(step.after.total_momentum, network.total_momentum)
                expected = tuple(
                    step.relative_scores_before[row]
                    + sum(
                        step.coupling_gram[row][col] * impulses[col]
                        for col in range(len(impulses))
                    )
                    for row in range(len(impulses))
                )
                self.assertEqual(step.relative_scores_after, expected)

    def test_contact_coupling_is_exact_integer_gram(self):
        network = ContactNetworkMomentum1D(
            masses=(2, 3, 4, 5),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, -1),
                ContactChannel1D(1, 3, 1),
            ),
        )
        for vector in itertools.product(range(-2, 3), repeat=3):
            identity = contact_coupling_quadratic_identity(network, vector)
            self.assertEqual(identity.edge_quadratic, identity.body_square_sum)
            self.assertGreaterEqual(identity.edge_quadratic, 0)

    def test_diagonal_coupling_is_equivalent_to_contact_graph_being_a_matching(self):
        body_count = 4
        possible = tuple(itertools.combinations(range(body_count), 2))
        for mask in range(1 << len(possible)):
            selected = tuple(
                ContactChannel1D(a, b, -1 if edge_index % 2 else 1)
                for edge_index, (a, b) in enumerate(possible)
                if mask & (1 << edge_index)
            )
            state = ContactNetworkMomentum1D(
                masses=(2, 3, 5, 7),
                momenta=(0, 0, 0, 0),
                contacts=selected,
            )
            self.assertEqual(contact_graph_is_matching(state), contact_coupling_is_diagonal(state))
            self.assertEqual(
                verify_matching_independence_equivalence(state),
                contact_graph_is_matching(state),
            )

    def test_diagonal_only_pair_guess_is_exact_for_disjoint_contacts(self):
        contacts = (ContactChannel1D(0, 1, 1), ContactChannel1D(2, 3, -1))
        for momenta in itertools.product(range(-2, 3), repeat=4):
            state = ContactNetworkMomentum1D(
                masses=(1, 2, 3, 4),
                momenta=momenta,
                contacts=contacts,
            )
            self.assertTrue(contact_graph_is_matching(state))
            guess = diagonal_only_nonclosing_impulse_guess(state)
            self.assertTrue(impulse_vector_makes_all_contacts_nonclosing(state, guess))

    def test_pairwise_independent_guess_fails_on_shared_body_chain(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(3, 2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        guess = diagonal_only_nonclosing_impulse_guess(state)
        self.assertEqual(guess, (1, 1, 1))
        guessed = apply_contact_impulse_vector(state, guess)
        self.assertEqual(guessed.relative_scores_after, (0, -1, 0))
        self.assertFalse(impulse_vector_makes_all_contacts_nonclosing(state, guess))

        coordinated = (2, 3, 2)
        solved = apply_contact_impulse_vector(state, coordinated)
        self.assertEqual(solved.relative_scores_after, (0, 1, 0))
        self.assertTrue(impulse_vector_makes_all_contacts_nonclosing(state, coordinated))
        self.assertEqual(solved.after.total_momentum, state.total_momentum)

    def test_swapping_contact_endpoints_and_normal_keeps_incidence_column(self):
        first = ContactNetworkMomentum1D(
            masses=(2, 3),
            momenta=(4, -1),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        swapped = ContactNetworkMomentum1D(
            masses=(2, 3),
            momenta=(4, -1),
            contacts=(ContactChannel1D(1, 0, -1),),
        )
        self.assertEqual(contact_incidence_matrix(first), contact_incidence_matrix(swapped))
        self.assertEqual(contact_relative_scores(first), contact_relative_scores(swapped))
        self.assertEqual(contact_coupling_gram(first), contact_coupling_gram(swapped))

    def test_invalid_networks_and_impulses_are_rejected(self):
        with self.assertRaises(ValueError):
            ContactNetworkMomentum1D((), (), ())
        with self.assertRaises(ValueError):
            ContactNetworkMomentum1D((1,), (0, 1), ())
        with self.assertRaises(ValueError):
            ContactNetworkMomentum1D((0,), (0,), ())
        with self.assertRaises(ValueError):
            ContactNetworkMomentum1D(
                (1, 1),
                (0, 0),
                (ContactChannel1D(0, 2, 1),),
            )
        with self.assertRaises(ValueError):
            ContactNetworkMomentum1D(
                (1, 1),
                (0, 0),
                (ContactChannel1D(0, 1, 1), ContactChannel1D(1, 0, -1)),
            )
        state = ContactNetworkMomentum1D(
            (1, 1),
            (0, 0),
            (ContactChannel1D(0, 1, 1),),
        )
        with self.assertRaises(ValueError):
            apply_contact_impulse_vector(state, ())
        with self.assertRaises(ValueError):
            apply_contact_impulse_vector(state, (-1,))


if __name__ == "__main__":
    unittest.main()
