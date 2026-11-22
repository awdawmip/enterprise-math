import ast
import inspect
import unittest

from enterprise_math import p017_p018_bonferroni_primorial as primorial_module
from enterprise_math.p017_p018_bonferroni_primorial import (
    odd_primorial,
    residual_bonferroni_defect_localization,
    residual_defect_free_threshold,
)


class P017P018BonferroniPrimorialTests(unittest.TestCase):
    def test_exact_reference_thresholds(self):
        self.assertEqual(odd_primorial(5), 15015)
        self.assertEqual(odd_primorial(7), 4_849_845)
        self.assertEqual(residual_defect_free_threshold(3)["odd_primorial_barrier"], 15015)
        self.assertEqual(residual_defect_free_threshold(5)["odd_primorial_barrier"], 4_849_845)

    def test_reference_residual_cells_are_defect_free_at_low_order(self):
        for k, radius in ((64, 47), (118, 5), (631, 93)):
            data = residual_bonferroni_defect_localization(k, radius, 3)
            self.assertTrue(data["residual_defect_free"])

    def test_order_five_barrier_dominates_known_large_critical_scales(self):
        barrier = residual_defect_free_threshold(5)["odd_primorial_barrier"]
        for k in (8191, 65536, 131071, 524287):
            self.assertLess(k, barrier)

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            residual_defect_free_threshold(2)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(primorial_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
