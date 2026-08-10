import ast
import inspect
import unittest

from enterprise_math import p017_p018_final_quantum_tradeoff as tradeoff_module
from enterprise_math.p017_p018_final_quantum_tradeoff import (
    final_quantum_repair_tradeoff,
)


class P017P018FinalQuantumTradeoffTests(unittest.TestCase):
    def test_reference_critical_scales_have_bounded_penultimate_repair(self):
        expected = {
            8191: (3, 5, (13, 17), 221, 8),
            65_536: (3, 5, (13, 17), 221, 57),
            131_071: (3, 5, (13, 17), 221, 114),
            524_287: (5, 7, (19, 23), 437, 3),
            2_147_483_647: (7, 9, (29, 31), 899, 20),
        }
        for k, (prev_order, terminal, pair, scale, capacity) in expected.items():
            data = final_quantum_repair_tradeoff(k)
            self.assertEqual(data["penultimate_order"], prev_order)
            self.assertEqual(data["terminal_order"], terminal)
            self.assertEqual(data["final_prime_pair"], pair)
            self.assertEqual(data["final_pair_scale_factor"], scale)
            self.assertEqual(data["penultimate_universal_capacity"], capacity)
            self.assertLessEqual(data["repair_symbol_ceiling"], scale)
            self.assertEqual(data["terminal_repair_symbol_count"], 1)
            self.assertTrue(data["terminal_repair_is_trivial"])

    def test_bounded_scales_respect_final_pair_repair_ceiling(self):
        for k in range(4, 2000):
            data = final_quantum_repair_tradeoff(k)
            if data["penultimate_order"] is None:
                continue
            if data.get("final_pair_scale_factor") is None:
                continue
            self.assertLessEqual(
                data["repair_symbol_ceiling"],
                data["final_pair_scale_factor"],
            )

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(tradeoff_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
