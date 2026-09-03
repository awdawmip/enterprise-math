from fractions import Fraction
import unittest

from enterprise_math.brc_feedback import (
    FeedbackEvent,
    conditional_feedback_kernel,
    feedback_additive_radius,
    feedback_circuit_atoms,
    feedback_condensation,
    feedback_event,
    feedback_interaction_girth,
    feedback_mobius_interaction_factors,
    feedback_subset_zeta_factors,
)
from enterprise_math.brc_rational_holonomy import (
    rational_from_prime_valuations,
    rational_power_skeleton_thickness,
    rational_prime_valuations,
    rational_squarefree_skeleton_thickness,
    rational_tree_gauge_normal_form,
)
from enterprise_math.brc_recurrent_invariants import (
    recurrent_edge_deletion_zeta_factor,
    recurrent_edge_multiplicative_radius,
    recurrent_edge_response,
    recurrent_equal_slack_certificate,
    recurrent_log_response_hessian,
    recurrent_loop_zeta,
)

Q = Fraction


class RecurrentInvariantTests(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]

    def test_loop_zeta_and_equal_slack(self) -> None:
        self.assertEqual(recurrent_loop_zeta(self.matrix), Q(12))
        cert = recurrent_equal_slack_certificate(self.matrix)
        self.assertTrue(cert.verify())
        self.assertEqual(cert.common_denominator, 6)
        self.assertEqual(cert.determinant_slack, 3)
        self.assertEqual(cert.integer_potential, (5, 9))
        self.assertEqual(cert.loop_zeta, Q(12))

    def test_edge_response_radius_and_deletion(self) -> None:
        response = recurrent_edge_response(self.matrix, 0, 1, Q(1, 2))
        self.assertEqual(response, Q(3))
        self.assertEqual(
            recurrent_edge_multiplicative_radius(self.matrix, 0, 1, Q(1, 2)),
            Q(4, 3),
        )
        self.assertEqual(
            recurrent_edge_deletion_zeta_factor(self.matrix, 0, 1, Q(1, 2)),
            Q(4),
        )

    def test_exact_response_hessian(self) -> None:
        branches = [(0, 1, Q(1, 2)), (1, 0, Q(1, 2)), (1, 1, Q(2, 3))]
        hessian = recurrent_log_response_hessian(self.matrix, branches)
        self.assertEqual(len(hessian), 3)
        for i in range(3):
            for j in range(3):
                self.assertEqual(hessian[i][j], hessian[j][i])
                self.assertGreaterEqual(hessian[i][j], 0)


class RationalHolonomyTests(unittest.TestCase):
    def test_prime_valuation_round_trip(self) -> None:
        q = Q(18, 25)
        valuations = rational_prime_valuations(q)
        self.assertEqual(valuations, ((2, 1), (3, 2), (5, -2)))
        self.assertEqual(rational_from_prime_valuations(valuations), q)

    def test_squarefree_and_mod3_decomposition(self) -> None:
        square = rational_squarefree_skeleton_thickness(Q(18, 25))
        self.assertTrue(square.verify())
        self.assertEqual(square.skeleton, 2)
        self.assertEqual(square.thickness, Q(3, 5))

        cubic = rational_power_skeleton_thickness(Q(12, 25), 3)
        self.assertTrue(cubic.verify())
        self.assertEqual(cubic.skeleton, 60)
        self.assertEqual(cubic.thickness, Q(1, 5))

    def test_tree_gauge_normal_form(self) -> None:
        normal = rational_tree_gauge_normal_form(
            3,
            [(0, 1, Q(2)), (1, 2, Q(3)), (0, 2, Q(5))],
            root=0,
            tree_edge_indices=[0, 1],
        )
        self.assertEqual(normal.vertex_potentials, (Q(1), Q(1, 2), Q(1, 6)))
        self.assertEqual(normal.normalized_edge_weights, (Q(1), Q(1), Q(5, 6)))
        self.assertEqual(normal.fundamental_holonomies(), ((2, Q(5, 6)),))
        self.assertEqual(
            normal.prime_coordinates(),
            ((2, ((2, -1), (3, -1), (5, 1))),),
        )


class FeedbackFoundationTests(unittest.TestCase):
    def test_typed_constructor_rejects_bool_mass(self) -> None:
        with self.assertRaises(TypeError):
            feedback_event(0, 0, True)
        self.assertEqual(feedback_event(0, 0, 1).mass, Q(1))

    def test_single_feedback_condensation_and_radius(self) -> None:
        background = [[Q(0), Q(1, 2)], [Q(0), Q(0)]]
        event = FeedbackEvent(1, 0, Q(1))
        analysis = feedback_condensation(background, [event])
        self.assertTrue(analysis.stable)
        self.assertEqual(analysis.feedback_kernel, ((Q(1, 2),),))
        self.assertEqual(analysis.loop_zeta_factor, Q(2))
        self.assertEqual(feedback_additive_radius(background, 1, 0), Q(2))

    def test_conditional_kernel_risk_creation(self) -> None:
        background = [[Q(0) for _ in range(4)] for _ in range(4)]
        background[1][2] = Q(1, 2)
        background[3][0] = Q(1, 3)
        installed = [FeedbackEvent(0, 1, Q(3, 2))]
        candidate = [FeedbackEvent(2, 3, Q(1))]
        conditional = conditional_feedback_kernel(background, installed, candidate)
        self.assertEqual(conditional, ((Q(1, 4),),))

    def test_pure_third_order_mobius_and_circuit_atom(self) -> None:
        background = [[Q(0) for _ in range(3)] for _ in range(3)]
        events = [
            FeedbackEvent(0, 1, Q(1, 2)),
            FeedbackEvent(1, 2, Q(1, 2)),
            FeedbackEvent(2, 0, Q(1, 2)),
        ]
        zeta = dict(feedback_subset_zeta_factors(background, events))
        interactions = dict(feedback_mobius_interaction_factors(background, events))
        for mask in [1, 2, 4, 3, 5, 6]:
            self.assertEqual(zeta[mask], Q(1))
            self.assertEqual(interactions[mask], Q(1))
        self.assertEqual(zeta[7], Q(8, 7))
        self.assertEqual(interactions[7], Q(8, 7))
        self.assertEqual(feedback_interaction_girth(background, events), 3)
        atoms = feedback_circuit_atoms(background, events)
        self.assertEqual(len(atoms), 1)
        self.assertEqual(atoms[0].event_indices, (0, 1, 2))
        self.assertEqual(atoms[0].rational_holonomy, Q(1, 8))
        self.assertEqual(atoms[0].interaction_factor, Q(8, 7))


if __name__ == "__main__":
    unittest.main()
