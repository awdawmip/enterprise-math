import unittest

from enterprise_math.material_validation import FixedDomainMaterialFit, IntegerErrorReport
from experiments.e001_treloar_state_precision_benchmark import (
    COLLAPSE_FACTOR,
    dense_response_branch,
    fold_state_cost,
)


class E001MaterialStateParetoTests(unittest.TestCase):
    @staticmethod
    def _synthetic_fit() -> FixedDomainMaterialFit:
        return FixedDomainMaterialFit(
            lower_deformation=100,
            upper_deformation=761,
            amplitude=16,
            input_root_power=1,
            output_hardening_power=1,
            output_scale=100,
            training_indices=(0,),
            predictions=(0,),
            training_error=IntegerErrorReport(
                count=1,
                sse=0,
                absolute_error=0,
                max_absolute_error=0,
            ),
        )

    def test_dense_branch_uses_declared_deformation_depth_domain(self):
        response = dense_response_branch(self._synthetic_fit())
        self.assertEqual(len(response), COLLAPSE_FACTOR)
        self.assertEqual(response[0], 0)
        self.assertEqual(response[-1], 100)

    def test_material_observable_never_refines_raw_depth_future(self):
        report = fold_state_cost(
            amplitude=16,
            fold_index=0,
            fit=self._synthetic_fit(),
            test_count=1,
            test_sse=0,
            dimension=3,
            horizon=4,
        )
        self.assertLessEqual(report.material_future_classes, report.raw_future_classes)
        self.assertGreater(report.dense_response_levels, 1)
        self.assertGreater(report.adjacent_plateau_steps, 0)


if __name__ == "__main__":
    unittest.main()
