import ast
import inspect
import unittest

import enterprise_math.p023_precision_compatibility as pc
from enterprise_math.division import multiple_collapse
from enterprise_math.p023_precision_compatibility import (
    incompatible_multiple_collapse_witness,
    multiple_collapse_induced_state,
    multiple_collapse_projection_compatible,
    precision_project,
    quotient_projection_commutes,
)


class P023PrecisionCompatibilityTests(unittest.TestCase):
    def test_quotient_always_commutes_with_precision_projection_bounded(self):
        for n in range(200):
            for ratio in range(1, 13):
                for divisor in range(1, 13):
                    self.assertTrue(quotient_projection_commutes(n, ratio, divisor))

    def test_multiple_collapse_compatibility_iff_divisibility_comparable(self):
        for ratio in range(1, 15):
            for divisor in range(1, 15):
                expected = ratio % divisor == 0 or divisor % ratio == 0
                self.assertEqual(
                    multiple_collapse_projection_compatible(ratio, divisor), expected
                )
                witness = incompatible_multiple_collapse_witness(ratio, divisor)
                self.assertEqual(witness is None, expected)
                if witness is not None:
                    left, right = witness
                    self.assertEqual(
                        precision_project(left, ratio), precision_project(right, ratio)
                    )
                    self.assertNotEqual(
                        precision_project(multiple_collapse(left, divisor), ratio),
                        precision_project(multiple_collapse(right, divisor), ratio),
                    )

    def test_induced_map_when_divisor_divides_ratio_is_identity(self):
        for ratio in range(1, 13):
            for divisor in range(1, ratio + 1):
                if ratio % divisor:
                    continue
                for coarse in range(20):
                    self.assertEqual(
                        multiple_collapse_induced_state(coarse, ratio, divisor), coarse
                    )

    def test_induced_map_when_ratio_divides_divisor_is_coarse_multiple_collapse(self):
        for ratio in range(1, 8):
            for scale in range(1, 8):
                divisor = ratio * scale
                for n in range(150):
                    coarse = precision_project(n, ratio)
                    expected = multiple_collapse(coarse, scale)
                    actual = precision_project(multiple_collapse(n, divisor), ratio)
                    self.assertEqual(actual, expected)
                    self.assertEqual(
                        multiple_collapse_induced_state(coarse, ratio, divisor), expected
                    )

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(pc))
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
