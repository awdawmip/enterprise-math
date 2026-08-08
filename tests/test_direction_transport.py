import ast
import inspect
import unittest

import enterprise_math.direction_transport as transport
from enterprise_math.direction_transport import (
    canonical_one_to_one_transport,
    composable_two_path_witnesses,
    compose_two_path_witnesses,
    direction_transport_matrix,
    exact_three_path_count,
    is_uniform_profile,
    naive_matrix_product_entry,
    predecessor_witness_profile,
    successor_witness_profile,
    transport_branching_profile,
    transport_merging_profile,
    transport_obstruction,
    uniform_fiber_cross_multiplication_holds,
)


class DirectionTransportTests(unittest.TestCase):
    def test_permutation_support_gives_canonical_matching(self):
        current = [
            [("a", "x"), ("b", "y")],
            [("c", "z")],
        ]
        nxt = [
            [("z", "q")],
            [("x", "r"), ("y", "s")],
        ]
        matrix = direction_transport_matrix(current, nxt)
        self.assertEqual(matrix, ((0, 2), (1, 0)))
        self.assertEqual(canonical_one_to_one_transport(matrix), (1, 0))
        self.assertIsNone(transport_obstruction(matrix))

    def test_split_is_relation_not_functional_identity(self):
        current = [[("a", "x"), ("b", "y")]]
        nxt = [[("x", "p")], [("y", "q")]]
        matrix = direction_transport_matrix(current, nxt)
        self.assertEqual(matrix, ((1, 1),))
        self.assertEqual(transport_branching_profile(matrix), (2,))
        self.assertEqual(transport_merging_profile(matrix), (1, 1))
        self.assertIsNone(canonical_one_to_one_transport(matrix))
        self.assertEqual(transport_obstruction(matrix), "split")

    def test_merge_is_relation_not_invertible_identity(self):
        current = [[("a", "x")], [("b", "y")]]
        nxt = [[("x", "p"), ("y", "q")]]
        matrix = direction_transport_matrix(current, nxt)
        self.assertEqual(matrix, ((1,), (1,)))
        self.assertEqual(transport_obstruction(matrix), "merge")

    def test_birth_or_death_blocks_matching(self):
        matrix = ((1, 0), (0, 0))
        self.assertEqual(transport_obstruction(matrix), "birth_or_death")

    def test_two_path_multiplicity_does_not_break_class_identity(self):
        current = [[("a", "x"), ("b", "x")]]
        nxt = [[("x", "p"), ("x", "q")]]
        matrix = direction_transport_matrix(current, nxt)
        self.assertEqual(matrix, ((4,),))
        self.assertEqual(canonical_one_to_one_transport(matrix), (0,))

    def test_cardinality_matrix_product_overcounts_three_path_composition(self):
        first = [("a", "x"), ("b", "y")]
        second = [("x", "p"), ("y", "q")]
        third = [("p", "r"), ("q", "s")]
        left_count = len(composable_two_path_witnesses(first, second))
        right_count = len(composable_two_path_witnesses(second, third))
        self.assertEqual((left_count, right_count), (2, 2))
        self.assertEqual(naive_matrix_product_entry(left_count, right_count), 4)
        self.assertEqual(exact_three_path_count(first, second, third), 2)

    def test_witness_join_composes_only_on_same_middle_incidence(self):
        first = [("a", "x"), ("b", "y")]
        second = [("x", "p"), ("y", "q")]
        third = [("p", "r"), ("q", "s")]
        left = composable_two_path_witnesses(first, second)
        right = composable_two_path_witnesses(second, third)
        composed = compose_two_path_witnesses(left, right)
        self.assertEqual(
            set(composed),
            {
                (("a", "x"), ("x", "p"), ("p", "r")),
                (("b", "y"), ("y", "q"), ("q", "s")),
            },
        )

    def test_uniform_predecessor_profile_makes_cardinality_data_sufficient(self):
        first = [("a", "x"), ("b", "y")]
        middle = [("x", "p"), ("y", "q")]
        third = [("p", "r"), ("p", "s"), ("q", "t")]
        predecessor = predecessor_witness_profile(first, middle)
        successor = successor_witness_profile(middle, third)
        self.assertEqual(predecessor, (1, 1))
        self.assertEqual(successor, (2, 1))
        self.assertTrue(is_uniform_profile(predecessor))
        self.assertFalse(is_uniform_profile(successor))
        self.assertTrue(uniform_fiber_cross_multiplication_holds(first, middle, third))
        self.assertEqual(2 * exact_three_path_count(first, middle, third), 2 * 3)

    def test_nonuniform_both_sides_reject_cardinality_sufficiency(self):
        first = [("a", "x"), ("b", "x"), ("c", "y")]
        middle = [("x", "p"), ("y", "q")]
        third = [("p", "r"), ("q", "s"), ("q", "t")]
        self.assertEqual(predecessor_witness_profile(first, middle), (2, 1))
        self.assertEqual(successor_witness_profile(middle, third), (1, 2))
        with self.assertRaises(ValueError):
            uniform_fiber_cross_multiplication_holds(first, middle, third)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(transport))
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
