import ast
import inspect
import unittest

import enterprise_math.p023_borrow_cocycle as bc
from enterprise_math.core import collapse
from enterprise_math.p023_borrow_cocycle import (
    compose_reductive_borrow,
    telescoping_borrow_identity,
    trajectory_borrows,
)


class P023BorrowCocycleTests(unittest.TestCase):
    def test_two_step_additivity_bounded(self):
        for n in range(80):
            for mid in range(n + 1):
                for end in range(mid + 1):
                    for ratio in range(1, 10):
                        first = lambda _n, value=mid: value
                        second = lambda _n, value=end: value
                        left, right, total = compose_reductive_borrow(
                            n, first, second, ratio
                        )
                        self.assertEqual(total, left + right)

    def test_trajectory_telescopes(self):
        states = (91, 80, 64, 27, 8, 1)
        for ratio in range(1, 16):
            total, endpoint = telescoping_borrow_identity(states, ratio)
            self.assertEqual(total, endpoint)

    def test_stable_equivalent_collapse_routes_can_redistribute_same_total_borrow(self):
        # W1 = C3 after C2: 8 -> 1.
        route_one = (8, collapse(collapse(8, 2), 3))
        # W2 = C2 after C3 repeated: 8 -> 4 -> 1.
        first = collapse(collapse(8, 3), 2)
        second = collapse(collapse(first, 3), 2)
        route_two = (8, first, second)
        self.assertEqual(route_one, (8, 1))
        self.assertEqual(route_two, (8, 4, 1))
        borrows_one = trajectory_borrows(route_one, 2)
        borrows_two = trajectory_borrows(route_two, 2)
        self.assertEqual(borrows_one, (4,))
        self.assertEqual(borrows_two, (2, 2))
        self.assertEqual(sum(borrows_one), sum(borrows_two))
        self.assertEqual(sum(borrows_one), 4)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(bc))
        floats = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
