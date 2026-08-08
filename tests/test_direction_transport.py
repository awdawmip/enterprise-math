import ast
import inspect
import unittest

import enterprise_math.direction_transport as transport
from enterprise_math.direction_transport import (
    canonical_one_to_one_transport,
    direction_transport_matrix,
    transport_branching_profile,
    transport_merging_profile,
    transport_obstruction,
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
