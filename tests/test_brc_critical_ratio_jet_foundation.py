from fractions import Fraction
import unittest

from enterprise_math.brc_critical_ratio_jet import (
    critical_ratio_first_response,
    critical_ratio_jet,
    full_powered_ratio_jet,
    powered_critical_gauge,
)

Q = Fraction


class CriticalRatioJetFoundationTests(unittest.TestCase):
    def test_powered_gauge_can_stay_rational_for_algebraic_mean(self):
        branches = (
            (0, 1, Q(1, 2)),
            (1, 0, Q(1, 3)),
        )
        gauge = powered_critical_gauge(2, branches)
        self.assertEqual(gauge.analysis.reference_cycle_length, 2)
        self.assertEqual(gauge.analysis.reference_cycle_product, Q(1, 6))
        self.assertEqual(gauge.potential_map, {0: Q(1), 1: Q(2, 3)})

    def test_critical_ratio_jet(self):
        branches = (
            (0, 0, Q(1, 2)), (0, 0, Q(1, 4)),
            (0, 1, Q(1, 2)), (0, 1, Q(1, 3)),
            (1, 0, Q(1, 2)),
            (1, 1, Q(1, 2)),
        )
        jet = critical_ratio_jet(2, branches)
        self.assertEqual(jet.ratios, (Q(1), Q(2, 3), Q(1, 2)))
        self.assertEqual(jet.layers[0], jet.analysis.critical_matrix)
        self.assertEqual(jet.moment(0)[0][0], 2)
        self.assertEqual(jet.moment(1)[0][0], Q(3, 2))

    def test_full_powered_jet_and_exact_moment(self):
        branches = (
            (0, 1, Q(1, 2)),
            (0, 1, Q(1, 4)),
            (1, 0, Q(1, 3)),
            (0, 0, Q(1, 10)),
        )
        jet = full_powered_ratio_jet(2, branches)
        self.assertEqual(jet.ratios, (Q(1), Q(1, 4), Q(3, 50)))
        self.assertEqual(jet.critical_matrix, ((0, 1), (1, 0)))
        self.assertEqual(jet.normalized_moment(0), ((Q(1), Q(2)), (Q(1), Q(0))))
        self.assertEqual(jet.normalized_moment(1), ((Q(3, 50), Q(5, 4)), (Q(1), Q(0))))

    def test_first_response_state_branching_core(self):
        # K=ones(2), largest strict ratio 1/2 on E00.
        branches = (
            (0, 0, Q(1)), (0, 0, Q(1, 2)),
            (0, 1, Q(1)),
            (1, 0, Q(1)),
            (1, 1, Q(1)),
        )
        jet = full_powered_ratio_jet(2, branches)
        state = critical_ratio_first_response(jet)
        self.assertEqual(state.critical_matrix, ((1, 1), (1, 1)))
        self.assertEqual(state.ratio, Q(1, 2))
        self.assertEqual(state.p0, (1, -2))
        self.assertEqual(state.p1, (0, -1, 1))
        self.assertEqual(state.root.exact_root, Q(1, 2))
        self.assertEqual(state.remainder_ratio, Q(1, 4))

    def test_reducible_full_jet_is_rejected(self):
        branches = (
            (0, 0, Q(1)),
            (1, 1, Q(1)),
        )
        with self.assertRaises(ValueError):
            full_powered_ratio_jet(2, branches)

    def test_typed_guards(self):
        with self.assertRaises(TypeError):
            powered_critical_gauge(1, ((0, 0, True),))
        with self.assertRaises(ValueError):
            powered_critical_gauge(1, ((0, 0, Q(-1)),))


if __name__ == "__main__":
    unittest.main()
