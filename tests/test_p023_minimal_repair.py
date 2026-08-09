import ast
import inspect
import unittest

import enterprise_math.p023_minimal_repair as repair
from enterprise_math.p023_minimal_repair import (
    boundary_crossing_bit,
    enumerate_split_residues,
    fiber_splits,
    projected_multiple_collapse,
    repaired_precision_state,
    split_fiber_period,
    split_fibers_per_period,
)


class P023MinimalRepairTests(unittest.TestCase):
    def test_repaired_state_exactly_matches_coarsest_output_partition_bounded(self):
        for ratio in range(1, 13):
            for divisor in range(1, 13):
                for coarse in range(20):
                    states = range(coarse * ratio, (coarse + 1) * ratio)
                    for left in states:
                        for right in states:
                            same_repair = repaired_precision_state(
                                left, ratio, divisor
                            ) == repaired_precision_state(right, ratio, divisor)
                            same_output = projected_multiple_collapse(
                                left, ratio, divisor
                            ) == projected_multiple_collapse(right, ratio, divisor)
                            self.assertEqual(same_repair, same_output)

    def test_bit_is_constant_exactly_on_nonsplitting_fibers(self):
        for ratio in range(1, 15):
            for divisor in range(1, 15):
                period = split_fiber_period(ratio, divisor)
                for coarse in range(period):
                    bits = {
                        boundary_crossing_bit(n, ratio, divisor)
                        for n in range(coarse * ratio, (coarse + 1) * ratio)
                    }
                    self.assertEqual(len(bits) == 2, fiber_splits(coarse, ratio, divisor))

    def test_exact_split_count_formula(self):
        for ratio in range(1, 40):
            for divisor in range(1, 40):
                residues = enumerate_split_residues(ratio, divisor)
                self.assertEqual(len(residues), split_fibers_per_period(ratio, divisor))

    def test_no_split_iff_divisibility_comparable(self):
        for ratio in range(1, 30):
            for divisor in range(1, 30):
                comparable = ratio % divisor == 0 or divisor % ratio == 0
                self.assertEqual(split_fibers_per_period(ratio, divisor) == 0, comparable)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(repair))
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
