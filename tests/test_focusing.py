import ast
import inspect
import unittest
from fractions import Fraction

import enterprise_math.focusing as focusing
from enterprise_math.focusing import (
    branch_clock_focusing_identity,
    branching_collision_rate_numerators,
    finite_focusing_step_bound,
    focusing_margin,
    no_sink_branch_clock_budget,
    relative_expansion_change_numerator,
    strict_focusing_step,
    verify_strict_focusing_trajectory,
)


class IntegerFocusingTests(unittest.TestCase):
    def test_focusing_margin_is_negative_expansion(self):
        vertices = [0, 1, 2]
        edges = [(0, 2), (1, 2)]
        self.assertEqual(focusing_margin(vertices, edges, [0, 1]), 1)
        self.assertTrue(strict_focusing_step(vertices, edges, [0, 1]))

    def test_finite_focusing_bound(self):
        self.assertEqual(finite_focusing_step_bound(7, 1), 7)
        self.assertEqual(finite_focusing_step_bound(7, 2), 4)
        self.assertEqual(finite_focusing_step_bound(8, 3), 3)

    def test_strict_focusing_trajectory_reaches_empty_section(self):
        vertices = list(range(6))
        edges = [
            (0, 3),
            (1, 3),
            (2, 4),
            (3, 5),
            (4, 5),
        ]
        data = verify_strict_focusing_trajectory(
            vertices, edges, [0, 1, 2], steps=3, minimum_margin=1
        )
        self.assertTrue(data["condition_holds"])
        self.assertEqual([len(section) for section in data["sections"]], [3, 2, 1, 0])
        self.assertEqual(data["expansions"], (-1, -1, -1))
        self.assertEqual(data["extinct_index"], 3)
        self.assertLessEqual(data["extinct_index"], data["bound"])

    def test_relative_expansion_numerator_matches_exact_rational_sign(self):
        cases = [
            (5, 2, 7, 1),
            (5, -1, 4, -2),
            (3, 0, 3, 0),
            (4, 3, 7, 6),
        ]
        for n0, xi0, n1, xi1 in cases:
            numerator = relative_expansion_change_numerator(n0, xi0, n1, xi1)
            exact_change = Fraction(xi1, n1) - Fraction(xi0, n0)
            self.assertEqual((numerator > 0) - (numerator < 0), (exact_change > 0) - (exact_change < 0))

    def test_branch_collision_rate_decomposition(self):
        data = branching_collision_rate_numerators(
            current_size=4,
            next_size=5,
            current_branching=3,
            next_branching=2,
            current_collision=1,
            next_collision=3,
        )
        self.assertEqual(data["branch_numerator"], -7)
        self.assertEqual(data["collision_numerator"], 7)
        self.assertEqual(data["expansion_change_numerator"], -14)
        self.assertLessEqual(data["branch_numerator"], 0)
        self.assertGreaterEqual(data["collision_numerator"], 0)
        self.assertLessEqual(data["expansion_change_numerator"], 0)

    def test_branch_clock_budget_is_intrinsic_branch_surplus(self):
        vertices = [0, 1, 2, 3, 4]
        edges = [(0, 2), (0, 3), (1, 3), (1, 4)]
        self.assertEqual(no_sink_branch_clock_budget(vertices, edges, [0, 1]), 2)
        data = branch_clock_focusing_identity(vertices, edges, [0, 1])
        self.assertEqual(data["branch_clock_budget"], 2)
        self.assertEqual(data["collision_excess"], 1)
        self.assertEqual(data["expansion"], 1)

    def test_zero_branch_clock_budget_can_be_marginal_or_contracting(self):
        vertices = [0, 1, 2, 3]
        injective_edges = [(0, 2), (1, 3)]
        merging_edges = [(0, 2), (1, 2)]
        marginal = branch_clock_focusing_identity(vertices, injective_edges, [0, 1])
        contracting = branch_clock_focusing_identity(vertices, merging_edges, [0, 1])
        self.assertEqual(marginal, {"expansion": 0, "branch_clock_budget": 0, "collision_excess": 0})
        self.assertEqual(contracting, {"expansion": -1, "branch_clock_budget": 0, "collision_excess": 1})

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(focusing))
        float_constants = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        true_divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(float_constants, [])
        self.assertEqual(true_divisions, [])


if __name__ == "__main__":
    unittest.main()
