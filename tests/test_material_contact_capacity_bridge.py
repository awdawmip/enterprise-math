import unittest
from itertools import product

from enterprise_math.material_contact_capacity_bridge import (
    symmetric_star_material_capacity_report,
    weighted_chain_material_capacity_report,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    impulse_vector_makes_all_contacts_nonclosing,
)
from enterprise_math.material_star_response_precision_phase import (
    star_general_final_score_numerators,
    star_minimum_response_relation_at_precision,
)


class MaterialContactCapacityBridgeTests(unittest.TestCase):
    def test_weighted_chain_capacity_is_exact_componentwise_least_action_threshold(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2, 1),
            momenta=(4, 4, 0),
            contacts=(ContactChannel1D(0, 1), ContactChannel1D(1, 2)),
        )
        exact = weighted_chain_material_capacity_report(state, 3, (6, 6))
        self.assertEqual(exact.least_required_numerators, (6, 6))
        self.assertEqual(exact.deficit_numerators, (0, 0))
        self.assertTrue(exact.feasible)

        soft_first = weighted_chain_material_capacity_report(state, 3, (5, 20))
        self.assertEqual(soft_first.least_required_numerators, (6, 6))
        self.assertEqual(soft_first.deficit_numerators, (1, 0))
        self.assertFalse(soft_first.feasible)

        # Independent bounded check: arbitrarily over-delivering the second
        # path contact cannot rescue the first contact's one-numerator deficit.
        scaled = ContactNetworkMomentum1D(
            masses=state.masses,
            momenta=tuple(3 * value for value in state.momenta),
            contacts=state.contacts,
        )
        self.assertFalse(
            any(
                impulse_vector_makes_all_contacts_nonclosing(scaled, candidate)
                for candidate in product(range(6), range(21))
            )
        )

    def test_branching_star_can_compensate_one_soft_leaf_by_exact_overresponse_elsewhere(self):
        report = symmetric_star_material_capacity_report(
            leaf_count=2,
            closing_quantum=10,
            denominator=1,
            capacity_numerators=(2, 8),
        )
        self.assertTrue(report.feasible)
        self.assertEqual(report.baseline_numerator, 3)
        self.assertEqual(report.residue_numerator, 1)
        self.assertEqual(report.unconstrained_minimum_total_numerator, 7)
        self.assertEqual(report.capped_minimum_total_numerator, 8)
        self.assertEqual(report.topology_overresponse_numerator, 1)
        self.assertFalse(report.unconstrained_minimum_relation_available)
        self.assertTrue(
            all(
                score >= 0
                for score in star_general_final_score_numerators((2, 6), 10, 1)
            )
        )

    def test_star_capacity_can_be_genuinely_insufficient(self):
        report = symmetric_star_material_capacity_report(
            leaf_count=2,
            closing_quantum=10,
            denominator=1,
            capacity_numerators=(1, 7),
        )
        self.assertFalse(report.feasible)
        self.assertIsNone(report.capped_minimum_total_numerator)
        self.assertIsNone(report.topology_overresponse_numerator)
        self.assertFalse(
            any(
                all(
                    score >= 0
                    for score in star_general_final_score_numerators(candidate, 10, 1)
                )
                for candidate in product(range(2), range(8))
            )
        )

    def test_star_unconstrained_minimum_survives_when_every_cap_reaches_baseline(self):
        report = symmetric_star_material_capacity_report(2, 10, 1, (3, 4))
        self.assertTrue(report.feasible)
        self.assertTrue(report.unconstrained_minimum_relation_available)
        self.assertEqual(report.capped_minimum_total_numerator, 7)
        self.assertEqual(report.topology_overresponse_numerator, 0)

    def test_refined_denominator_exposes_same_topology_compensation_in_numerator_lattice(self):
        # k=3,q=1,s=5 => Q=5, baseline t=1, residue r=1, S*=4.
        # A zero-capacity first leaf can still be separated by over-delivery on
        # the other leaves: the capped minimum rises exactly to 5.
        report = symmetric_star_material_capacity_report(3, 1, 5, (0, 3, 3))
        self.assertTrue(report.feasible)
        self.assertEqual(report.scaled_closing_demand, 5)
        self.assertEqual(report.baseline_numerator, 1)
        self.assertEqual(report.residue_numerator, 1)
        self.assertEqual(report.unconstrained_minimum_total_numerator, 4)
        self.assertEqual(report.capped_minimum_total_numerator, 5)
        self.assertEqual(report.topology_overresponse_numerator, 1)

    def test_star_closed_form_matches_independent_bounded_cap_box_oracle(self):
        for leaf_count in range(2, 5):
            for closing_quantum in range(1, 4):
                for denominator in range(1, 3):
                    demand = closing_quantum * denominator
                    relation = star_minimum_response_relation_at_precision(
                        leaf_count, closing_quantum, denominator
                    )
                    for capacities in product(range(demand + 1), repeat=leaf_count):
                        report = symmetric_star_material_capacity_report(
                            leaf_count,
                            closing_quantum,
                            denominator,
                            capacities,
                        )
                        feasible_totals = []
                        for candidate in product(
                            *(range(capacity + 1) for capacity in capacities)
                        ):
                            if all(
                                score >= 0
                                for score in star_general_final_score_numerators(
                                    candidate,
                                    closing_quantum,
                                    denominator,
                                )
                            ):
                                feasible_totals.append(sum(candidate))
                        self.assertEqual(report.feasible, bool(feasible_totals))
                        self.assertEqual(
                            report.capped_minimum_total_numerator,
                            min(feasible_totals) if feasible_totals else None,
                        )
                        minimum_relation_available = any(
                            all(value <= cap for value, cap in zip(vector, capacities))
                            for vector in relation
                        )
                        self.assertEqual(
                            report.unconstrained_minimum_relation_available,
                            minimum_relation_available,
                        )

    def test_invalid_capacities_are_rejected(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1),),
        )
        with self.assertRaises(ValueError):
            weighted_chain_material_capacity_report(state, 0, (1,))
        with self.assertRaises(ValueError):
            weighted_chain_material_capacity_report(state, 1, (-1,))
        with self.assertRaises(ValueError):
            symmetric_star_material_capacity_report(3, 1, 1, (1, 2))
        with self.assertRaises(ValueError):
            symmetric_star_material_capacity_report(3, 1, 1, (1, -1, 1))


if __name__ == "__main__":
    unittest.main()
