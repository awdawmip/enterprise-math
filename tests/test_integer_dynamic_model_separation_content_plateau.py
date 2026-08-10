import unittest

from enterprise_math.integer_dynamic_model_separation_horizon import (
    dynamic_model_separation_horizon_report,
)


class IntegerDynamicModelSeparationContentPlateauTests(unittest.TestCase):
    def test_equal_consecutive_contents_can_hide_later_refinement(self):
        # One action contains two independent chains.
        # Chain 1 differs immediately by coefficient 6 and then loops.
        # Chain 2 agrees for two steps and differs only at the third by 4.
        # With observations e1 and e3, the difference-content sequence is
        # 0, 6, 6, 2.  Thus scalar content has a one-step plateau before later
        # refinement; only the full block-module plateau is a stop certificate.
        left = (
            (0, 0, 0, 0, 0, 0),  # e1 -> 0
            (0, 1, 0, 0, 0, 0),  # e2 -> e2
            (0, 0, 0, 1, 0, 0),  # e3 -> e4
            (0, 0, 0, 0, 1, 0),  # e4 -> e5
            (0, 0, 0, 0, 0, 0),  # e5 -> 0
            (0, 0, 0, 0, 0, 1),  # e6 -> e6
        )
        right = (
            (0, 6, 0, 0, 0, 0),  # e1 -> 6 e2
            (0, 1, 0, 0, 0, 0),  # e2 -> e2
            (0, 0, 0, 1, 0, 0),  # e3 -> e4
            (0, 0, 0, 0, 1, 0),  # e4 -> e5
            (0, 0, 0, 0, 0, 4),  # e5 -> 4 e6
            (0, 0, 0, 0, 0, 1),  # e6 -> e6
        )
        observation = (
            (1, 0, 0, 0, 0, 0),
            (0, 0, 1, 0, 0, 0),
        )
        report = dynamic_model_separation_horizon_report(
            (left,),
            observation,
            (right,),
            observation,
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(
            tuple(by_horizon[h].difference_content for h in range(4)),
            (0, 6, 6, 2),
        )
        self.assertNotEqual(
            by_horizon[1].block_future_basis,
            by_horizon[2].block_future_basis,
        )
        self.assertNotEqual(
            by_horizon[2].block_future_basis,
            by_horizon[3].block_future_basis,
        )

        # Mod 3 is hidden during the apparent scalar plateau, then separates at h3.
        self.assertEqual(report.first_distinguishing_horizon(3), 3)
        # Mod 2 divides both 6 and 2, so it remains indistinguishable forever.
        self.assertIsNone(report.first_distinguishing_horizon(2))

    def test_full_module_plateau_remains_the_only_online_stop_certificate(self):
        action = (
            (0, 1),
            (0, 0),
        )
        report = dynamic_model_separation_horizon_report(
            (action,),
            ((1, 0),),
            (action,),
            ((1, 0),),
        )
        self.assertEqual(report.steps[0].difference_content, 0)
        self.assertEqual(report.steps[1].difference_content, 0)
        self.assertEqual(
            report.steps[0].block_future_basis,
            report.steps[1].block_future_basis,
        )
        self.assertEqual(report.exact_block_stabilization_horizon, 0)


if __name__ == "__main__":
    unittest.main()
