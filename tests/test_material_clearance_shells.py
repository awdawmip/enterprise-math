import unittest
from itertools import product
from math import comb

from enterprise_math.engineering_collision import Body2D, exact_collision
from enterprise_math.material_clearance_shells import (
    COARSE_ONLY_CONTACT,
    PRIMITIVE_CONTACT,
    RESOLVED,
    active_axis_count_multiplicity,
    axis_clearances_2d,
    clearance_layer_signature_2d,
    clearance_shell_multiplicity,
    specific_active_set_multiplicity,
)


class MaterialClearanceShellTests(unittest.TestCase):
    def test_terminal_primitive_contact_matches_exact_square_collision(self):
        bodies = []
        body_id = 0
        for x in range(-3, 4):
            for y in range(-3, 4):
                for radius in range(2):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        for index, left in enumerate(bodies):
            for right in bodies[index + 1 :]:
                gx, gy = axis_clearances_2d(left, right)
                self.assertEqual((gx == 0 and gy == 0), exact_collision(left, right))
                signature = clearance_layer_signature_2d(left, right, 4)
                self.assertEqual(
                    signature.status == PRIMITIVE_CONTACT,
                    exact_collision(left, right),
                )

    def test_shell_multiplicity_matches_direct_nd_enumeration(self):
        for dimension in range(1, 5):
            for factor in range(2, 7):
                total = 0
                for depth in range(1, factor):
                    q = factor - depth
                    direct = sum(
                        max(vector) == q
                        for vector in product(range(factor), repeat=dimension)
                    )
                    formula = clearance_shell_multiplicity(
                        dimension, factor, depth
                    )
                    self.assertEqual(formula, direct)
                    total += formula
                self.assertEqual(total, factor**dimension - 1)

    def test_active_axis_count_formula_matches_direct_enumeration(self):
        for dimension in range(1, 5):
            for factor in range(2, 7):
                for depth in range(1, factor):
                    q = factor - depth
                    shell = [
                        vector
                        for vector in product(range(factor), repeat=dimension)
                        if max(vector) == q
                    ]
                    for active_count in range(1, dimension + 1):
                        direct = sum(
                            sum(value == q for value in vector) == active_count
                            for vector in shell
                        )
                        formula = active_axis_count_multiplicity(
                            dimension, factor, depth, active_count
                        )
                        self.assertEqual(
                            formula,
                            comb(dimension, active_count)
                            * specific_active_set_multiplicity(
                                dimension, factor, depth, active_count
                            ),
                        )
                        self.assertEqual(formula, direct)

    def test_same_scalar_depth_can_hide_different_direction_witness(self):
        left = Body2D(0, 0, 0, 0)
        x_only = Body2D(1, 2, 0, 0)
        tied = Body2D(2, 2, 2, 0)
        x_signature = clearance_layer_signature_2d(left, x_only, 4)
        tie_signature = clearance_layer_signature_2d(left, tied, 4)

        self.assertEqual(x_signature.status, COARSE_ONLY_CONTACT)
        self.assertEqual(tie_signature.status, COARSE_ONLY_CONTACT)
        self.assertEqual(x_signature.layer_depth, 2)
        self.assertEqual(tie_signature.layer_depth, 2)
        self.assertEqual(x_signature.active_axes, ("x",))
        self.assertEqual(tie_signature.active_axes, ("x", "y"))
        self.assertEqual(x_signature.shell_multiplicity, tie_signature.shell_multiplicity)
        self.assertNotEqual(
            x_signature.specific_active_set_multiplicity,
            tie_signature.specific_active_set_multiplicity,
        )

    def test_2d_shell_has_two_arms_and_one_tie_for_each_positive_q(self):
        for factor in range(2, 9):
            for depth in range(1, factor):
                q = factor - depth
                x_only = specific_active_set_multiplicity(2, factor, depth, 1)
                tied = specific_active_set_multiplicity(2, factor, depth, 2)
                self.assertEqual(x_only, q)
                self.assertEqual(tied, 1)
                self.assertEqual(
                    clearance_shell_multiplicity(2, factor, depth),
                    2 * x_only + tied,
                )

    def test_resolved_state_has_no_synthetic_material_depth(self):
        left = Body2D(0, 0, 0, 0)
        right = Body2D(1, 5, 1, 0)
        signature = clearance_layer_signature_2d(left, right, 4)
        self.assertEqual(signature.status, RESOLVED)
        self.assertIsNone(signature.layer_depth)
        self.assertEqual(signature.active_axes, ())

    def test_invalid_shell_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            clearance_shell_multiplicity(0, 3, 1)
        with self.assertRaises(ValueError):
            clearance_shell_multiplicity(2, 3, 3)
        with self.assertRaises(ValueError):
            active_axis_count_multiplicity(2, 3, 1, 3)


if __name__ == "__main__":
    unittest.main()
