import unittest
from itertools import product
from math import comb

from enterprise_math.causal_inventory_operator import (
    apply_compiled_inventory_operator,
    compile_inventory_operator,
    higher_operator_terms,
    operator_interaction_order,
)


class CausalInventoryOperatorTests(unittest.TestCase):
    def test_additive_operator_compiles_to_order_one_only(self):
        input_types = ("a", "b")
        output_types = ("x", "y")
        maxima = (3, 3)
        table = {
            (a, b): {"x": 2 * a + b, "y": 3 * b}
            for a, b in product(range(4), range(4))
        }
        compiled = compile_inventory_operator(input_types, output_types, maxima, table)
        self.assertEqual(operator_interaction_order(compiled), 1)
        self.assertEqual(higher_operator_terms(compiled), {})
        for state, expected in table.items():
            actual = apply_compiled_inventory_operator(compiled, output_types, state)
            expected_nonzero = {key: value for key, value in expected.items() if value}
            self.assertEqual(actual, expected_nonzero)

    def test_cross_pair_creation_is_exact_order_two_operator(self):
        input_types = ("a", "b")
        output_types = ("pair",)
        maxima = (3, 3)
        table = {
            (a, b): {"pair": a * b}
            for a, b in product(range(4), range(4))
        }
        compiled = compile_inventory_operator(input_types, output_types, maxima, table)
        self.assertEqual(operator_interaction_order(compiled), 2)
        self.assertEqual(compiled[((1, 1), "pair")], 1)
        self.assertEqual(higher_operator_terms(compiled), {((1, 1), "pair"): 1})

    def test_same_type_pair_creation_is_exact_order_two_operator(self):
        input_types = ("a",)
        output_types = ("pair",)
        maxima = (6,)
        table = {(a,): {"pair": comb(a, 2)} for a in range(7)}
        compiled = compile_inventory_operator(input_types, output_types, maxima, table)
        self.assertEqual(compiled[((2,), "pair")], 1)
        self.assertEqual(operator_interaction_order(compiled), 2)

    def test_three_body_creation_has_exact_order_three(self):
        input_types = ("a", "b", "c")
        output_types = ("triple",)
        maxima = (2, 2, 2)
        table = {
            (a, b, c): {"triple": a * b * c}
            for a, b, c in product(range(3), range(3), range(3))
        }
        compiled = compile_inventory_operator(input_types, output_types, maxima, table)
        self.assertEqual(compiled[((1, 1, 1), "triple")], 1)
        self.assertEqual(operator_interaction_order(compiled), 3)

    def test_mixed_operator_reconstructs_exactly(self):
        input_types = ("a", "b")
        output_types = ("x", "pair")
        maxima = (3, 3)
        table = {
            (a, b): {
                "x": a + 2 * b,
                "pair": 4 * a * b + 3 * comb(a, 2),
            }
            for a, b in product(range(4), range(4))
        }
        compiled = compile_inventory_operator(input_types, output_types, maxima, table)
        self.assertEqual(operator_interaction_order(compiled), 2)
        self.assertEqual(compiled[((1, 1), "pair")], 4)
        self.assertEqual(compiled[((2, 0), "pair")], 3)
        for state, expected in table.items():
            actual = apply_compiled_inventory_operator(compiled, output_types, state)
            expected_nonzero = {key: value for key, value in expected.items() if value}
            self.assertEqual(actual, expected_nonzero)


if __name__ == "__main__":
    unittest.main()
