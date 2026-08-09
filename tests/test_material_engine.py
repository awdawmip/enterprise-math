import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_engine import observe_material_engine_history
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_program import (
    HARDEN,
    RETAIN,
    SOFTEN,
    MaterialOperator,
    material_program_profile,
)


class MaterialEngineTests(unittest.TestCase):
    @staticmethod
    def pair_state(right_x):
        return Body2D(0, 0, 0, 2), Body2D(1, right_x, 0, 2)

    def setUp(self):
        self.program = material_program_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_word=(MaterialOperator(HARDEN, 2),),
            return_word=(
                MaterialOperator(SOFTEN, 1),
                MaterialOperator(RETAIN, 500),
            ),
        )

    def test_geometry_to_material_history_pipeline_closes_without_kinematic_update(self):
        positions = (10, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10)
        report = observe_material_engine_history(
            tuple(self.pair_state(x) for x in positions),
            self.program,
        )
        self.assertEqual(
            report.contact_history.deformation_schedule,
            (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0),
        )
        self.assertEqual(report.contact_history.peak_deformation, 5)
        self.assertEqual(report.cycle.peak_index, 5)
        self.assertEqual(report.cycle.paired_absolute_gap_sum, 400)
        self.assertEqual(report.cycle.paired_loading_excess_sum, 300)

    def test_same_deformation_is_path_sensitive_inside_full_pipeline(self):
        positions = (10, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10)
        report = observe_material_engine_history(
            tuple(self.pair_state(x) for x in positions),
            self.program,
        )
        loading = report.contact_history.material_states[3]
        returning = report.contact_history.material_states[7]
        self.assertEqual(loading.deformation_index, returning.deformation_index)
        self.assertEqual(loading.branch, LOADING)
        self.assertEqual(returning.branch, RETURNING)
        self.assertNotEqual(loading.response_sample, returning.response_sample)

    def test_separate_only_path_never_enters_nonzero_material_response(self):
        report = observe_material_engine_history(
            (self.pair_state(10), self.pair_state(9), self.pair_state(8)),
            self.program,
        )
        self.assertEqual(report.contact_history.peak_deformation, 0)
        self.assertTrue(
            all(
                state.response_sample == 0
                for state in report.contact_history.material_states
            )
        )
        self.assertEqual(report.cycle.paired_absolute_gap_sum, 0)


if __name__ == "__main__":
    unittest.main()
