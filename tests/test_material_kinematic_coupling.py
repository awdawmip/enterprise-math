import unittest

from enterprise_math.material_hysteresis import MaterialHistoryState, RETURNING
from enterprise_math.material_kinematic_coupling import (
    rebound_budget,
    rebound_budget_from_material_state,
    rebound_budget_scale_report,
)


class MaterialKinematicCouplingTests(unittest.TestCase):
    def test_zero_and_full_response_are_exact_endpoints(self):
        self.assertEqual(rebound_budget(17, 0, 100).returned_budget, 0)
        self.assertEqual(rebound_budget(17, 100, 100).returned_budget, 17)

    def test_budget_split_retains_exact_product_remainder(self):
        report = rebound_budget(17, 37, 100)
        self.assertEqual(report.returned_budget, 6)
        self.assertEqual(report.unreturned_budget, 11)
        self.assertEqual(report.product_remainder, 29)
        self.assertEqual(17 * 37, 100 * 6 + 29)

    def test_branch_aware_material_state_can_drive_declared_budget_coupling(self):
        state = MaterialHistoryState(
            deformation_index=3,
            branch=RETURNING,
            response_sample=375,
        )
        report = rebound_budget_from_material_state(20, state, amplitude=1000)
        self.assertEqual(report.returned_budget, 7)
        self.assertEqual(report.unreturned_budget, 13)
        self.assertEqual(report.product_remainder, 500)

    def test_joint_material_scale_refinement_is_exactly_invariant(self):
        for budget in range(0, 20):
            for amplitude in range(1, 15):
                for response in range(amplitude + 1):
                    for refinement in range(1, 6):
                        report = rebound_budget_scale_report(
                            budget,
                            response,
                            amplitude,
                            material_refinement=refinement,
                            motion_refinement=1,
                        )
                        self.assertEqual(
                            report.material_refined.returned_budget,
                            report.base.returned_budget,
                        )

    def test_motion_budget_refinement_defect_is_exact_bounded_carry(self):
        saw_positive = False
        for budget in range(0, 20):
            for amplitude in range(1, 15):
                for response in range(amplitude + 1):
                    for refinement in range(1, 7):
                        report = rebound_budget_scale_report(
                            budget,
                            response,
                            amplitude,
                            material_refinement=1,
                            motion_refinement=refinement,
                        )
                        self.assertEqual(
                            report.motion_refinement_defect,
                            report.expected_motion_defect_from_remainder,
                        )
                        self.assertGreaterEqual(report.motion_refinement_defect, 0)
                        self.assertLess(
                            report.motion_refinement_defect,
                            refinement,
                        )
                        saw_positive |= report.motion_refinement_defect > 0
        self.assertTrue(saw_positive)

    def test_coupling_does_not_invent_budget(self):
        for budget in range(0, 30):
            for amplitude in range(1, 20):
                for response in range(amplitude + 1):
                    report = rebound_budget(budget, response, amplitude)
                    self.assertEqual(
                        report.returned_budget + report.unreturned_budget,
                        budget,
                    )
                    self.assertLessEqual(report.returned_budget, budget)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            rebound_budget(-1, 1, 10)
        with self.assertRaises(ValueError):
            rebound_budget(1, 11, 10)
        with self.assertRaises(ValueError):
            rebound_budget(1, 1, 0)


if __name__ == "__main__":
    unittest.main()
