import unittest
from itertools import product
from math import comb

from enterprise_math.material_clearance_shells import (
    COARSE_ONLY_CONTACT,
    PRIMITIVE_CONTACT,
    RESOLVED,
    active_axis_count_multiplicity,
    clearance_layer_signature,
    clearance_shell_multiplicity,
    specific_active_set_multiplicity,
)


class MaterialClearanceShellTests(unittest.TestCase):
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

    def test_generic_signature_separates_contact_status_and_direction_witness(self):
        primitive = clearance_layer_signature((0, 0, 0), 4)
        self.assertEqual(primitive.status, PRIMITIVE_CONTACT)
        self.assertIsNone(primitive.layer_depth)

        resolved = clearance_layer_signature((1, 4, 0), 4)
        self.assertEqual(resolved.status, RESOLVED)
        self.assertIsNone(resolved.layer_depth)

        one_axis = clearance_layer_signature((2, 0), 4)
        tied = clearance_layer_signature((2, 2), 4)
        self.assertEqual(one_axis.status, COARSE_ONLY_CONTACT)
        self.assertEqual(tied.status, COARSE_ONLY_CONTACT)
        self.assertEqual(one_axis.layer_depth, 2)
        self.assertEqual(tied.layer_depth, 2)
        self.assertEqual(one_axis.active_indices, (0,))
        self.assertEqual(tied.active_indices, (0, 1))
        self.assertEqual(one_axis.shell_multiplicity, tied.shell_multiplicity)
        self.assertNotEqual(
            one_axis.specific_active_set_multiplicity,
            tied.specific_active_set_multiplicity,
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

    def test_signature_matches_direct_shell_depth_on_small_boxes(self):
        for dimension in range(1, 4):
            for factor in range(2, 6):
                for vector in product(range(factor + 1), repeat=dimension):
                    signature = clearance_layer_signature(vector, factor)
                    gap = max(vector)
                    if gap == 0:
                        self.assertEqual(signature.status, PRIMITIVE_CONTACT)
                    elif gap >= factor:
                        self.assertEqual(signature.status, RESOLVED)
                    else:
                        self.assertEqual(signature.status, COARSE_ONLY_CONTACT)
                        self.assertEqual(signature.layer_depth, factor - gap)
                        self.assertEqual(
                            signature.active_indices,
                            tuple(i for i, value in enumerate(vector) if value == gap),
                        )

    def test_invalid_shell_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            clearance_shell_multiplicity(0, 3, 1)
        with self.assertRaises(ValueError):
            clearance_shell_multiplicity(2, 3, 3)
        with self.assertRaises(ValueError):
            active_axis_count_multiplicity(2, 3, 1, 3)
        with self.assertRaises(ValueError):
            clearance_layer_signature((), 3)
        with self.assertRaises(ValueError):
            clearance_layer_signature((0, -1), 3)


if __name__ == "__main__":
    unittest.main()
