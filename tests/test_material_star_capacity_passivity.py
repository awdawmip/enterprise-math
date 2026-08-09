import unittest
from itertools import product

from enterprise_math.material_star_capacity_passivity import (
    symmetric_star_capped_passivity_report,
)
from enterprise_math.material_star_response_energy_bridge import (
    star_equal_mass_kinetic_change_numerator,
)
from enterprise_math.material_star_response_precision_phase import (
    star_general_final_score_numerators,
)


class MaterialStarCapacityPassivityTests(unittest.TestCase):
    def test_soft_leaf_forces_overresponse_but_capped_minimum_remains_passive(self):
        report = symmetric_star_capped_passivity_report(
            leaf_count=2,
            closing_quantum=10,
            denominator=1,
            capacity_numerators=(2, 8),
        )
        self.assertTrue(report.capacity.feasible)
        self.assertEqual(report.capped_minimum_total_numerator, 8)
        self.assertEqual(report.capacity.unconstrained_minimum_total_numerator, 7)
        self.assertEqual(report.capacity.topology_overresponse_numerator, 1)
        self.assertEqual(report.contact_lower_bound_numerator, 2)
        self.assertEqual(report.kinetic_change_upper_bound_numerator, -56)
        self.assertTrue(report.guaranteed_passive)
        self.assertTrue(report.strict_upper_bound_dissipation)

        # One exact capped-minimum witness: (2,6), both final scores nonclosing.
        response = (2, 6)
        self.assertEqual(sum(response), 8)
        self.assertTrue(
            all(
                score >= 0
                for score in star_general_final_score_numerators(
                    response, closing_quantum=10, denominator=1
                )
            )
        )
        self.assertLessEqual(
            star_equal_mass_kinetic_change_numerator(response, 10, 1),
            report.kinetic_change_upper_bound_numerator,
        )

    def test_zero_capacity_leaf_can_drive_minimum_total_to_Q_without_becoming_active(self):
        # k=3,q=1,s=5 => Q=5.  The zero-capacity first leaf forces S_cap=Q.
        report = symmetric_star_capped_passivity_report(
            leaf_count=3,
            closing_quantum=1,
            denominator=5,
            capacity_numerators=(0, 3, 3),
        )
        self.assertTrue(report.capacity.feasible)
        self.assertEqual(report.capped_minimum_total_numerator, 5)
        self.assertEqual(report.contact_lower_bound_numerator, 0)
        self.assertEqual(report.kinetic_change_upper_bound_numerator, 0)
        self.assertTrue(report.guaranteed_passive)
        self.assertFalse(report.strict_upper_bound_dissipation)

        # A capped-minimum witness remains strictly dissipative even though the
        # no-cap upper envelope reaches zero.
        witness = (0, 2, 3)
        self.assertEqual(sum(witness), 5)
        self.assertTrue(
            all(
                score >= 0
                for score in star_general_final_score_numerators(
                    witness, 1, 5
                )
            )
        )
        self.assertLess(
            star_equal_mass_kinetic_change_numerator(witness, 1, 5),
            0,
        )

    def test_infeasible_capacity_box_does_not_claim_passivity(self):
        report = symmetric_star_capped_passivity_report(
            2, 10, 1, (1, 7)
        )
        self.assertFalse(report.capacity.feasible)
        self.assertIsNone(report.capped_minimum_total_numerator)
        self.assertIsNone(report.contact_lower_bound_numerator)
        self.assertIsNone(report.kinetic_change_upper_bound_numerator)
        self.assertFalse(report.guaranteed_passive)
        self.assertFalse(report.strict_upper_bound_dissipation)

    def test_bounded_cap_box_oracle_confirms_every_minimum_total_response_is_passive(self):
        checked = 0
        for leaf_count in (2, 3):
            for q in range(1, 4):
                for denominator in range(1, 4):
                    demand = q * denominator
                    for capacities in product(
                        range(demand + 1), repeat=leaf_count
                    ):
                        report = symmetric_star_capped_passivity_report(
                            leaf_count,
                            q,
                            denominator,
                            capacities,
                        )
                        feasible = []
                        for vector in product(
                            *(range(capacity + 1) for capacity in capacities)
                        ):
                            if all(
                                score >= 0
                                for score in star_general_final_score_numerators(
                                    vector, q, denominator
                                )
                            ):
                                feasible.append(vector)
                        if not feasible:
                            self.assertFalse(report.guaranteed_passive)
                            continue
                        checked += 1
                        minimum_total = min(sum(vector) for vector in feasible)
                        minima = [
                            vector
                            for vector in feasible
                            if sum(vector) == minimum_total
                        ]
                        self.assertTrue(report.guaranteed_passive)
                        self.assertEqual(
                            report.capped_minimum_total_numerator,
                            minimum_total,
                        )
                        energies = [
                            star_equal_mass_kinetic_change_numerator(
                                vector, q, denominator
                            )
                            for vector in minima
                        ]
                        self.assertTrue(all(change <= 0 for change in energies))
                        self.assertLessEqual(
                            max(energies),
                            report.kinetic_change_upper_bound_numerator,
                        )
        self.assertGreater(checked, 100)

    def test_arbitrary_feasible_overresponse_is_not_claimed_passive(self):
        # The theorem is deliberately minimum-total only.  At k=2,Q=1 the
        # feasible vector (3,3) strongly over-delivers and injects energy.
        self.assertTrue(
            all(
                score >= 0
                for score in star_general_final_score_numerators((3, 3), 1, 1)
            )
        )
        self.assertGreater(
            star_equal_mass_kinetic_change_numerator((3, 3), 1, 1),
            0,
        )


if __name__ == "__main__":
    unittest.main()
