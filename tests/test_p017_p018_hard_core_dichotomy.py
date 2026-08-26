import ast
import inspect
import unittest

import enterprise_math.p017_p018_hard_core_dichotomy as dichotomy
from enterprise_math.p017_p018_hard_core_bridge import finite_base_risk_triples
from enterprise_math.p017_p018_hard_core_dichotomy import (
    UNIQUE_SMALL_BASE_GAP_PRIME_ROW,
    adjacent_core_reduction,
    enumerate_small_base_gap_mirror_rows,
    enumerate_small_base_gap_prime_rows,
    prime_tail_base_gap_dichotomy,
)


class P017P018HardCoreDichotomyTests(unittest.TestCase):
    def test_close_base_gap_forces_consecutive_odd_cores(self):
        rows = finite_base_risk_triples()
        self.assertEqual(len(rows), 58)
        for k, d, e, _, _ in rows:
            data = adjacent_core_reduction(k, d, e)
            self.assertEqual(e, d + 2)
            self.assertEqual(data["core_gap"], 2)

    def test_complete_close_base_mirror_frontier_has_134_rows(self):
        rows = enumerate_small_base_gap_mirror_rows()
        self.assertEqual(len(rows), 134)
        self.assertTrue(all(row[2] == row[1] + 2 for row in rows))

    def test_unique_prime_pair_in_close_base_frontier(self):
        rows = enumerate_small_base_gap_prime_rows()
        self.assertEqual(rows, (UNIQUE_SMALL_BASE_GAP_PRIME_ROW,))

    def test_unique_sharp_exception(self):
        data = prime_tail_base_gap_dichotomy(64, 7, 9, 47, 1)
        self.assertTrue(data["exceptional"])
        self.assertEqual(data["base_root_gap"], 3)
        self.assertEqual((data["q_d"], data["q_e"]), (601, 457))
        self.assertEqual((data["root_d"], data["root_e"]), (24, 21))

    def test_generic_prime_pair_has_base_gap_at_least_four(self):
        data = prime_tail_base_gap_dichotomy(22, 3, 7, 5, -1)
        self.assertFalse(data["exceptional"])
        self.assertGreaterEqual(data["base_root_gap"], 4)
        self.assertEqual((data["q_d"], data["q_e"]), (167, 73))

    def test_validation(self):
        with self.assertRaises(ValueError):
            prime_tail_base_gap_dichotomy(16, 3, 5, 7, 1)
        with self.assertRaises(ValueError):
            prime_tail_base_gap_dichotomy(64, 7, 9, 47, 0)

    def test_dichotomy_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(dichotomy))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
