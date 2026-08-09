import unittest

from enterprise_math.clearance_precision import ACTIVE_COUNT, ACTIVE_SET, SCALAR_DEPTH
from enterprise_math.material_anisotropy_2d import anisotropic_material_profile_2d
from enterprise_math.material_anisotropy_visibility_2d import (
    kinematic_anisotropy_visibility_2d,
)
from enterprise_math.material_response import explicit_material_curve_profile


def profile(samples, amplitude=5):
    return explicit_material_curve_profile(samples, samples, amplitude)


class MaterialAnisotropyVisibility2DTests(unittest.TestCase):
    def test_budget_can_hide_and_reveal_exact_active_set_nonmonotonically(self):
        family = anisotropic_material_profile_2d(
            profile((0, 2)),
            profile((0, 3)),
            profile((0, 5)),
        )
        observables = [
            kinematic_anisotropy_visibility_2d(
                family, collapse_factor=2, incoming_budget=budget
            ).minimum_clearance_observable
            for budget in (1, 2, 3, 4, 5)
        ]
        self.assertEqual(
            observables,
            [ACTIVE_COUNT, ACTIVE_SET, ACTIVE_COUNT, ACTIVE_SET, ACTIVE_SET],
        )

    def test_zero_budget_hides_all_material_anisotropy_from_kinematic_future(self):
        family = anisotropic_material_profile_2d(
            profile((0, 2, 4)),
            profile((0, 3, 5)),
            profile((0, 5, 5)),
        )
        report = kinematic_anisotropy_visibility_2d(family, 3, 0)
        self.assertEqual(report.minimum_clearance_observable, SCALAR_DEPTH)
        self.assertTrue(
            all(depth.minimum_clearance_observable == SCALAR_DEPTH for depth in report.depths)
        )

    def test_collapse_factor_can_hide_deeper_anisotropy(self):
        family = anisotropic_material_profile_2d(
            profile((0, 2, 2), 5),
            profile((0, 2, 3), 5),
            profile((0, 2, 5), 5),
        )
        shallow = kinematic_anisotropy_visibility_2d(
            family, collapse_factor=2, incoming_budget=5
        )
        deeper = kinematic_anisotropy_visibility_2d(
            family, collapse_factor=3, incoming_budget=5
        )
        self.assertEqual(shallow.represented_max_depth, 1)
        self.assertEqual(shallow.minimum_clearance_observable, SCALAR_DEPTH)
        self.assertEqual(deeper.represented_max_depth, 2)
        self.assertEqual(deeper.minimum_clearance_observable, ACTIVE_SET)

    def test_x_y_alias_with_distinct_corner_requires_only_active_count(self):
        family = anisotropic_material_profile_2d(
            profile((0, 2)),
            profile((0, 3)),
            profile((0, 5)),
        )
        report = kinematic_anisotropy_visibility_2d(family, 2, 3)
        depth = report.depths[0]
        self.assertEqual(
            (depth.x_returned_budget, depth.y_returned_budget, depth.corner_returned_budget),
            (1, 1, 3),
        )
        self.assertEqual(depth.minimum_clearance_observable, ACTIVE_COUNT)
        self.assertEqual(report.minimum_clearance_observable, ACTIVE_COUNT)

    def test_multiple_depths_take_join_of_local_requirements(self):
        family = anisotropic_material_profile_2d(
            profile((0, 2, 2), 5),
            profile((0, 2, 3), 5),
            profile((0, 5, 5), 5),
        )
        report = kinematic_anisotropy_visibility_2d(family, 3, 5)
        self.assertEqual(
            [depth.minimum_clearance_observable for depth in report.depths],
            [ACTIVE_COUNT, ACTIVE_SET],
        )
        self.assertEqual(report.minimum_clearance_observable, ACTIVE_SET)

    def test_invalid_budget_and_factor_are_rejected(self):
        common = profile((0, 5))
        family = anisotropic_material_profile_2d(common, common, common)
        with self.assertRaises(ValueError):
            kinematic_anisotropy_visibility_2d(family, 0, 1)
        with self.assertRaises(ValueError):
            kinematic_anisotropy_visibility_2d(family, 2, -1)
        with self.assertRaises(ValueError):
            kinematic_anisotropy_visibility_2d(family, 2, 1, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()