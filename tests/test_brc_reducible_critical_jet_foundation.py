from fractions import Fraction
import unittest

from enterprise_math.brc_reducible_critical_jet import (
    characteristic_ratio_jet,
    first_newton_edge_state,
    first_root_active_layer,
    global_strict_powered_gauge,
)

Q = Fraction


class ReducibleCriticalJetFoundationTests(unittest.TestCase):
    def test_global_strict_gauge_separates_equality_and_strict_branches(self):
        branches = (
            (0, 0, Q(1)),
            (1, 1, Q(1)),
            (0, 1, Q(1, 2)),
            (1, 0, Q(1, 3)),
        )
        gauge = global_strict_powered_gauge(2, branches)
        self.assertEqual(gauge.critical_matrix, ((1, 0), (0, 1)))
        self.assertTrue(Q(0) < gauge.contraction_rate < 1)
        for record in gauge.branch_ratios:
            if record.critical_dominant:
                self.assertEqual(record.ratio, 1)
            else:
                self.assertTrue(Q(0) < record.ratio < 1)

    def test_feed_forward_layer_is_absent_from_characteristic_jet(self):
        branches = (
            (0, 0, Q(1)), (0, 0, Q(1)),
            (1, 1, Q(1)),
            (0, 1, Q(1, 2)),
        )
        state = characteristic_ratio_jet(2, branches)
        self.assertEqual(state.critical_matrix, ((2, 0), (0, 1)))
        self.assertEqual(tuple(layer.base for layer in state.layers), (Q(1),))
        self.assertIsNone(first_root_active_layer(state))

    def test_closed_excursion_is_root_active(self):
        branches = (
            (0, 0, Q(1)), (0, 0, Q(1)),
            (1, 1, Q(1)),
            (0, 1, Q(1, 2)),
            (1, 0, Q(1, 2)),
        )
        state = characteristic_ratio_jet(2, branches)
        active = first_root_active_layer(state)
        self.assertIsNotNone(active)
        assert active is not None
        self.assertEqual(active.base, Q(1, 4))
        self.assertEqual(active.polynomial, (0, 0, -1))
        self.assertEqual(active.root.exact_root, Q(1, 2))

    def test_tied_root_routes_to_newton_edge(self):
        branches = (
            (0, 0, Q(1)),
            (1, 1, Q(1)),
            (0, 1, Q(1, 2)),
            (1, 0, Q(1, 2)),
        )
        state = characteristic_ratio_jet(2, branches)
        with self.assertRaises(ValueError):
            first_root_active_layer(state)
        newton = first_newton_edge_state(state)
        self.assertEqual(newton.root_multiplicity, 2)
        self.assertEqual(newton.representative_base, Q(1, 4))
        self.assertEqual(newton.representative_degree, 2)
        self.assertEqual(newton.rational_edge_polynomial, (Q(-1), Q(0), Q(1)))

    def test_contact_order_one_scale(self):
        # Two tied critical self-loops; a strict parallel branch on state 0
        # produces G(z)=-z(1-z), hence q=1 and candidate scale eta itself.
        branches = (
            (0, 0, Q(1)), (0, 0, Q(1, 2)),
            (1, 1, Q(1)),
        )
        state = characteristic_ratio_jet(2, branches)
        newton = first_newton_edge_state(state)
        self.assertEqual(newton.root_multiplicity, 2)
        self.assertEqual(newton.representative_base, Q(1, 2))
        self.assertEqual(newton.representative_degree, 1)

    def test_typed_guards(self):
        with self.assertRaises(TypeError):
            global_strict_powered_gauge(1, ((0, 0, True),))
        with self.assertRaises(ValueError):
            global_strict_powered_gauge(1, ((0, 0, Q(-1)),))


if __name__ == "__main__":
    unittest.main()
