import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_repair_tradeoff as tradeoff_module
from enterprise_math.p017_p018_token_repair_tradeoff import (
    critical_524287_order5_binary_tradeoff,
)


class P017P018TokenRepairTradeoffTests(unittest.TestCase):
    def test_critical_order_five_fiber_is_exactly_binary(self):
        data = critical_524287_order5_binary_tradeoff()
        self.assertEqual(data["minimum_order5_token"], 255_255)
        self.assertEqual(data["second_order5_token"], 285_285)
        self.assertEqual(data["only_possible_three_slot_token"], 255_255)
        self.assertEqual(data["minimum_token_signed_points"], (-345_469, 165_041))
        self.assertEqual(data["actual_order5_max_token_fiber"], 2)
        self.assertEqual(data["binary_repair_symbols_needed_for_exact_incidence"], 2)
        self.assertEqual(data["binary_repair_bits"], 1)

    def test_child_quotient_root_is_a_natural_binary_repair_observable(self):
        data = critical_524287_order5_binary_tradeoff()
        self.assertEqual(data["full_block_quotients"], (1723, 21977))
        self.assertEqual(data["child_quotient_roots"], (41, 148))
        self.assertNotEqual(*data["child_quotient_roots"])
        self.assertTrue(data["child_root_repairs_minimum_fiber"])

    def test_one_odd_order_quantum_removes_the_binary_repair(self):
        data = critical_524287_order5_binary_tradeoff()
        self.assertEqual(data["order5"]["universal_signed_reuse_capacity"], 3)
        self.assertEqual(data["order7"]["universal_signed_reuse_capacity"], 1)
        self.assertEqual(data["order7_repair_symbols_needed"], 1)
        self.assertEqual(data["order7_repair_bits"], 0)
        self.assertEqual(data["proof_order_quantum_exchange"], (5, 1, 7, 0))

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
