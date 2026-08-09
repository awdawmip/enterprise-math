import ast
import inspect
import unittest

from enterprise_math import p017_p018_bonferroni_defect as defect_module
from enterprise_math.p017_p018_bonferroni_defect import (
    family_bonferroni_defect,
    odd_bonferroni_point_defect,
)


class P017P018BonferroniDefectTests(unittest.TestCase):
    def test_point_defect_is_exact_binomial_tail_coordinate(self):
        for order in (1, 3, 5, 7):
            for support_size in range(0, 13):
                data = odd_bonferroni_point_defect(support_size, order)
                expected = 0
                if support_size > order:
                    from math import comb
                    expected = comb(support_size - 1, order)
                self.assertEqual(data["defect"], expected)

    def test_order_five_ignores_supports_up_to_five_exactly(self):
        for support_size in range(0, 6):
            data = odd_bonferroni_point_defect(support_size, 5)
            self.assertEqual(data["defect"], 0)
        self.assertEqual(odd_bonferroni_point_defect(6, 5)["defect"], 1)
        self.assertEqual(odd_bonferroni_point_defect(7, 5)["defect"], 6)

    def test_family_identity(self):
        data = family_bonferroni_defect((0, 1, 2, 5, 6, 7), 5)
        self.assertEqual(data["nonempty_union"], 5)
        self.assertEqual(data["high_support_defect"], 7)
        self.assertEqual(data["bonferroni_upper"], 12)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            odd_bonferroni_point_defect(3, 2)
        with self.assertRaises(ValueError):
            family_bonferroni_defect((), 3)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(defect_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
