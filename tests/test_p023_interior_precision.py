import ast
import inspect
import itertools
import unittest

import enterprise_math.p023_interior_precision as interior
from enterprise_math.p023_interior_precision import (
    interior_alignment_theorem_holds,
    perfect_power_uniform_precision_witness,
    uniform_floor_quotient_refines,
)


class InteriorPrecisionTests(unittest.TestCase):
    def test_alignment_theorem_exhaustive_on_small_chains(self):
        for size in range(1, 8):
            domains = [range(index + 1) for index in range(size)]
            for values in itertools.product(*domains):
                if any(values[index] > values[index + 1] for index in range(size - 1)):
                    continue
                if any(values[values[index]] != values[index] for index in range(size)):
                    continue
                operation = dict(enumerate(values))
                for ratio in range(1, size + 2):
                    self.assertTrue(interior_alignment_theorem_holds(operation, ratio))

    def test_perfect_power_no_go_witness_broad_grid(self):
        for power in range(2, 8):
            for ratio in range(2, 40):
                data = perfect_power_uniform_precision_witness(power, ratio)
                self.assertEqual(data["left"] // ratio, data["right"] // ratio)
                self.assertNotEqual(
                    data["left_coarse_output"], data["right_coarse_output"]
                )

    def test_uniform_floor_refinement_exact_divisibility(self):
        for finer in range(1, 20):
            for coarser in range(1, 20):
                expected = coarser % finer == 0
                self.assertEqual(
                    uniform_floor_quotient_refines(finer, coarser), expected
                )

    def test_invalid_interior_map_rejected_by_theorem_audit(self):
        with self.assertRaises(ValueError):
            interior_alignment_theorem_holds({0: 0, 1: 0, 2: 1}, 2)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(interior))
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
