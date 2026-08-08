import ast
import inspect
import unittest

import enterprise_math.core as core
from enterprise_math import (
    basin_for_root,
    collapse,
    integer_nth_root,
    preimage_count,
    project_scale,
    scaled_root,
)


class CoreTests(unittest.TestCase):
    def test_square_root_examples(self):
        self.assertEqual(integer_nth_root(2, 2), 1)
        self.assertEqual(integer_nth_root(200, 2), 14)
        self.assertEqual(integer_nth_root(20000, 2), 141)

    def test_characterization(self):
        for p in range(1, 6):
            for n in range(0, 500):
                k = integer_nth_root(n, p)
                self.assertLessEqual(k**p, n)
                self.assertLess(n, (k + 1) ** p)

    def test_exact_powers(self):
        for p in range(1, 6):
            for k in range(0, 30):
                self.assertEqual(integer_nth_root(k**p, p), k)

    def test_collapse_contracts_and_is_idempotent(self):
        for p in range(1, 6):
            for n in range(0, 500):
                c = collapse(n, p)
                self.assertLessEqual(c, n)
                self.assertEqual(collapse(c, p), c)

    def test_collapse_is_monotone(self):
        for p in range(1, 6):
            last = -1
            for n in range(0, 500):
                current = collapse(n, p)
                self.assertGreaterEqual(current, last)
                last = current

    def test_basin_and_preimage_count(self):
        self.assertEqual(basin_for_root(141, 2), (19881, 20163))
        self.assertEqual(preimage_count(141, 2), 283)
        for p in range(1, 5):
            for k in range(0, 20):
                start, end = basin_for_root(k, p)
                self.assertEqual(preimage_count(k, p), (k + 1) ** p - k**p)
                for n in range(start, end + 1):
                    self.assertEqual(collapse(n, p), k**p)

    def test_scale_compatibility(self):
        for p in range(1, 5):
            for base in range(2, 8):
                for n in range(0, 80):
                    for level in range(0, 3):
                        coarse = scaled_root(n, p, base, level)
                        fine = scaled_root(n, p, base, level + 1)
                        self.assertEqual(project_scale(fine, base), coarse)

    def test_reference_core_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(core))
        float_constants = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        true_divisions = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(float_constants, [])
        self.assertEqual(true_divisions, [])


if __name__ == "__main__":
    unittest.main()
