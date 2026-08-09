import unittest

from enterprise_math.material_hysteresis import trace_deformation_schedule
from enterprise_math.material_loop_geometry import (
    boundary_lattice_steps,
    material_loop_geometry,
    signed_twice_lattice_area,
)
from enterprise_math.material_response import material_curve_profile


class MaterialLoopGeometryTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_reference_realized_history_forms_closed_integer_loop(self):
        schedule = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        states = trace_deformation_schedule(self.profile, schedule)
        geometry = material_loop_geometry(states)
        self.assertTrue(geometry.closed)
        self.assertEqual(geometry.vertices[0], (0, 0))
        self.assertEqual(geometry.vertices[-1], (0, 0))
        self.assertIsNotNone(geometry.signed_twice_area)
        self.assertEqual(
            geometry.absolute_twice_area,
            abs(geometry.signed_twice_area),
        )
        self.assertGreater(geometry.absolute_twice_area, 0)
        self.assertGreater(geometry.boundary_lattice_steps, 0)

    def test_symmetric_loading_return_curve_has_zero_loop_area(self):
        symmetric = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )
        schedule = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        geometry = material_loop_geometry(
            trace_deformation_schedule(symmetric, schedule)
        )
        self.assertTrue(geometry.closed)
        self.assertEqual(geometry.signed_twice_area, 0)
        self.assertEqual(geometry.absolute_twice_area, 0)

    def test_open_history_does_not_invent_closed_loop_area(self):
        states = trace_deformation_schedule(self.profile, (0, 1, 2, 3, 4))
        geometry = material_loop_geometry(states)
        self.assertFalse(geometry.closed)
        self.assertIsNone(geometry.signed_twice_area)
        self.assertIsNone(geometry.absolute_twice_area)
        self.assertIsNone(geometry.boundary_lattice_steps)

    def test_manual_unit_square_has_twice_area_two(self):
        vertices = ((0, 0), (1, 0), (1, 1), (0, 1), (0, 0))
        self.assertEqual(signed_twice_lattice_area(vertices), 2)
        self.assertEqual(boundary_lattice_steps(vertices), 4)

    def test_area_requires_explicitly_closed_vertex_path(self):
        with self.assertRaises(ValueError):
            signed_twice_lattice_area(((0, 0), (1, 0), (1, 1)))


if __name__ == "__main__":
    unittest.main()
