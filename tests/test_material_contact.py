import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_contact import (
    contact_deformation_steps,
    observe_contact_material,
)
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_response import material_curve_profile


class MaterialContactTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_first_point_contact_maps_to_one_separation_step(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 2, 0, 1)
        self.assertEqual(contact_deformation_steps(left, right), 1)
        observed = observe_contact_material(left, right, self.profile, LOADING)
        self.assertIsNotNone(observed)
        self.assertEqual(observed.deformation_steps, 1)
        self.assertEqual(observed.minimum_axes, ("x",))
        self.assertEqual(observed.material_state.response_sample, 40)

    def test_deeper_overlap_maps_to_larger_integer_deformation_index(self):
        left = Body2D(0, 0, 0, 2)
        right = Body2D(1, 1, 0, 2)
        observed = observe_contact_material(left, right, self.profile, LOADING)
        self.assertIsNotNone(observed)
        self.assertEqual(observed.deformation_steps, 4)
        self.assertEqual(observed.material_state.response_sample, 640)

    def test_same_contact_depth_can_read_different_loading_and_return_samples(self):
        left = Body2D(0, 0, 0, 2)
        right = Body2D(1, 2, 0, 2)
        loading = observe_contact_material(left, right, self.profile, LOADING)
        returning = observe_contact_material(left, right, self.profile, RETURNING)
        self.assertEqual(loading.deformation_steps, returning.deformation_steps)
        self.assertNotEqual(
            loading.material_state.response_sample,
            returning.material_state.response_sample,
        )

    def test_separate_bodies_do_not_enter_material_branch(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 10, 0, 1)
        self.assertIsNone(contact_deformation_steps(left, right))
        self.assertIsNone(observe_contact_material(left, right, self.profile, LOADING))

    def test_unrepresented_contact_depth_is_rejected_not_saturated(self):
        short_profile = material_curve_profile(
            (0, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
        )
        left = Body2D(0, 0, 0, 5)
        right = Body2D(1, 0, 0, 5)
        self.assertEqual(contact_deformation_steps(left, right), 11)
        with self.assertRaises(ValueError):
            observe_contact_material(left, right, short_profile, LOADING)


if __name__ == "__main__":
    unittest.main()
