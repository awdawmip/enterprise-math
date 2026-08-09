import ast
import inspect
import unittest

import enterprise_math.p023_reductive_borrow as rb
from enterprise_math.core import collapse
from enterprise_math.division import multiple_collapse
from enterprise_math.p023_reductive_borrow import (
    multiple_collapse_borrow,
    power_collapse_borrow,
    precision_borrow_from_gap,
    projected_reductive_identity,
)


class P023ReductiveBorrowTests(unittest.TestCase):
    def test_identity_for_all_reductive_target_values_bounded(self):
        for n in range(120):
            for transformed in range(n + 1):
                for ratio in range(1, 15):
                    coarse, borrow, after = projected_reductive_identity(
                        n, transformed, ratio
                    )
                    self.assertEqual(after, coarse - borrow)
                    self.assertGreaterEqual(borrow, 0)

    def test_multiple_collapse_is_instance(self):
        for n in range(180):
            for ratio in range(1, 12):
                for divisor in range(1, 12):
                    transformed = multiple_collapse(n, divisor)
                    expected = n // ratio - transformed // ratio
                    self.assertEqual(
                        multiple_collapse_borrow(n, ratio, divisor), expected
                    )

    def test_power_collapse_is_instance(self):
        for n in range(250):
            for ratio in range(1, 12):
                for exponent in range(1, 6):
                    transformed = collapse(n, exponent)
                    expected = n // ratio - transformed // ratio
                    self.assertEqual(
                        power_collapse_borrow(n, ratio, exponent), expected
                    )

    def test_gap_formula_matches_direct_coarse_loss(self):
        for n in range(100):
            for transformed in range(n + 1):
                for ratio in range(1, 10):
                    direct = n // ratio - transformed // ratio
                    formula = precision_borrow_from_gap(n, transformed, ratio)
                    self.assertEqual(formula, direct)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(rb))
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
