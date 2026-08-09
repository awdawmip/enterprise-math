import itertools
import unittest

from enterprise_math.material_star_refinement_carry import (
    star_first_strict_cost_drop_multiplier,
    star_refinement_carry_report,
    star_refinement_residue_carry,
    star_scaled_coarse_minimum_relation,
    star_symmetry_before_cost_drop_multiplier,
)
from enterprise_math.material_star_response_precision_phase import (
    star_general_final_score_numerators,
    star_minimum_response_relation_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
)


class MaterialStarRefinementCarryTests(unittest.TestCase):
    def test_exact_carry_and_minimum_total_identity_exhaustive(self):
        checked = 0
        for k in range(2, 8):
            for q in range(1, 6):
                for s in range(1, 7):
                    coarse = star_response_refinement_phase(k, q, s)
                    for multiplier in range(1, 7):
                        report = star_refinement_carry_report(
                            k, q, s, multiplier
                        )
                        expected_carry, expected_residue = divmod(
                            multiplier * coarse.residue, k + 1
                        )
                        self.assertEqual(report.carry, expected_carry)
                        self.assertEqual(report.fine_residue, expected_residue)
                        self.assertEqual(
                            report.fine_minimum_total_numerator,
                            multiplier * report.coarse_minimum_total_numerator
                            - expected_carry,
                        )
                        self.assertEqual(
                            report.cross_multiplied_cost_drop,
                            s * expected_carry,
                        )
                        checked += 1
        self.assertGreater(checked, 1000)

    def test_scaled_coarse_minima_are_always_fine_feasible(self):
        checked = 0
        for k in range(2, 6):
            for q in range(1, 5):
                for s in range(1, 5):
                    for multiplier in range(1, 5):
                        fine = s * multiplier
                        for vector in star_scaled_coarse_minimum_relation(
                            k, q, s, multiplier
                        ):
                            self.assertTrue(
                                all(
                                    score >= 0
                                    for score in star_general_final_score_numerators(
                                        vector, q, fine
                                    )
                                )
                            )
                        checked += 1
        self.assertGreater(checked, 200)

    def test_no_carry_exactly_preserves_scaled_minima_but_can_add_new_witnesses(self):
        checked = 0
        for k in range(2, 6):
            for q in range(1, 4):
                for s in range(1, 5):
                    for multiplier in range(1, 5):
                        report = star_refinement_carry_report(
                            k, q, s, multiplier
                        )
                        scaled = set(
                            star_scaled_coarse_minimum_relation(
                                k, q, s, multiplier
                            )
                        )
                        fine = set(
                            star_minimum_response_relation_at_precision(
                                k, q, s * multiplier
                            )
                        )
                        self.assertEqual(
                            report.scaled_coarse_minima_remain_fine_minima,
                            report.carry == 0,
                        )
                        if report.carry == 0:
                            self.assertTrue(scaled.issubset(fine))
                        else:
                            self.assertTrue(scaled.isdisjoint(fine))
                        if (
                            report.carry == 0
                            and multiplier > 1
                            and report.coarse_residue > 0
                        ):
                            self.assertTrue(report.new_minimum_witnesses_without_cost_drop)
                            self.assertGreater(len(fine), len(scaled))
                        checked += 1
        self.assertGreater(checked, 100)

    def test_first_strict_cost_drop_multiplier_is_exact(self):
        for k in range(2, 10):
            for q in range(1, 8):
                for s in range(1, 8):
                    coarse = star_response_refinement_phase(k, q, s)
                    expected = (
                        None
                        if coarse.residue == 0
                        else (k + coarse.residue) // coarse.residue
                    )
                    actual = star_first_strict_cost_drop_multiplier(k, q, s)
                    self.assertEqual(actual, expected)
                    if actual is None:
                        for multiplier in range(1, k + 3):
                            carry, _ = star_refinement_residue_carry(
                                k, q, s, multiplier
                            )
                            self.assertEqual(carry, 0)
                    else:
                        for multiplier in range(1, actual):
                            carry, _ = star_refinement_residue_carry(
                                k, q, s, multiplier
                            )
                            self.assertEqual(carry, 0)
                        carry, _ = star_refinement_residue_carry(
                            k, q, s, actual
                        )
                        self.assertGreater(carry, 0)

    def test_symmetry_can_arrive_before_any_cost_drop(self):
        checked = 0
        for k in range(2, 10):
            for q in range(1, 8):
                for s in range(1, 8):
                    coarse = star_response_refinement_phase(k, q, s)
                    residue = coarse.residue
                    actual = star_symmetry_before_cost_drop_multiplier(k, q, s)
                    expected = (
                        k // residue
                        if residue > 0 and k % residue == 0
                        else None
                    )
                    self.assertEqual(actual, expected)
                    if actual is not None:
                        report = star_refinement_carry_report(
                            k, q, s, actual
                        )
                        self.assertEqual(report.carry, 0)
                        self.assertEqual(report.fine_residue, k)
                        self.assertTrue(report.fine_symmetric_minimum_exists)
                        self.assertEqual(report.cross_multiplied_cost_drop, 0)
                        checked += 1
        self.assertGreater(checked, 20)

    def test_reference_k3_q1_refinement_sequence_separates_cost_and_witness_changes(self):
        expected = {
            1: (1, 3, False, 0),
            2: (2, 6, False, 0),
            3: (3, 10, True, 0),
            4: (0, 1, True, 1),
        }
        for multiplier, (residue, count, symmetric, carry) in expected.items():
            phase = star_response_refinement_phase(3, 1, multiplier)
            report = star_refinement_carry_report(3, 1, 1, multiplier)
            self.assertEqual(phase.residue, residue)
            self.assertEqual(phase.minimum_response_count, count)
            self.assertEqual(phase.symmetry_minimum_compatible, symmetric)
            self.assertEqual(report.carry, carry)

        phase1 = star_response_refinement_phase(3, 1, 1)
        phase2 = star_response_refinement_phase(3, 1, 2)
        phase3 = star_response_refinement_phase(3, 1, 3)
        phase4 = star_response_refinement_phase(3, 1, 4)

        # Physical minimum is unchanged at 1 through s=1,2,3.
        self.assertEqual(phase1.minimum_total_numerator, 1)
        self.assertEqual(phase2.minimum_total_numerator, 2)
        self.assertEqual(phase3.minimum_total_numerator, 3)
        self.assertEqual(
            star_symmetric_minimum_numerators(3, 1, 3),
            (1, 1, 1),
        )

        # Yet s=2 already has genuinely new minimum allocations.
        coarse_scaled = set(star_scaled_coarse_minimum_relation(3, 1, 1, 2))
        fine_relation = set(star_minimum_response_relation_at_precision(3, 1, 2))
        self.assertIn((1, 1, 0), fine_relation)
        self.assertNotIn((1, 1, 0), coarse_scaled)
        self.assertGreater(len(fine_relation), len(coarse_scaled))

        # At s=4 the first carry lowers the normalized cost from 1 to 3/4.
        self.assertEqual(phase4.minimum_total_numerator, 3)
        self.assertEqual(phase4.residue, 0)
        self.assertEqual(
            star_minimum_response_relation_at_precision(3, 1, 4),
            ((1, 1, 1),),
        )

    def test_carry_positive_scaled_old_minima_overdeliver_by_exact_carry(self):
        for k in range(2, 6):
            for q in range(1, 4):
                for s in range(1, 5):
                    for multiplier in range(2, 6):
                        report = star_refinement_carry_report(k, q, s, multiplier)
                        if report.carry == 0:
                            continue
                        scaled = star_scaled_coarse_minimum_relation(
                            k, q, s, multiplier
                        )
                        for vector in scaled:
                            self.assertEqual(
                                sum(vector) - report.fine_minimum_total_numerator,
                                report.carry,
                            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            star_refinement_residue_carry(3, 1, 1, 0)
        with self.assertRaises(ValueError):
            star_scaled_coarse_minimum_relation(3, 1, 1, 0)


if __name__ == "__main__":
    unittest.main()
