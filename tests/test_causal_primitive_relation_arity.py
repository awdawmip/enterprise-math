import unittest
from itertools import product

from enterprise_math.causal_primitive_link_profile import a_roots
from enterprise_math.causal_primitive_relation_arity import (
    full_translation_kernel_rank,
    minimum_unit_subset_relation_arity,
    relation_rank_through_arity,
)


def simple_cubic_roots():
    roots = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            roots.append(tuple(vector))
    return tuple(roots)


def bcc_roots():
    return tuple(product((-1, 1), repeat=3))


class CausalPrimitiveRelationArityTests(unittest.TestCase):
    def test_sc_kernel_is_generated_by_inverse_pairs(self):
        roots = simple_cubic_roots()
        self.assertEqual(full_translation_kernel_rank(roots), 3)
        self.assertEqual(relation_rank_through_arity(roots, 2), 3)
        self.assertEqual(minimum_unit_subset_relation_arity(roots, 4), 2)

    def test_fcc_needs_ternary_primitive_composition_relations(self):
        roots = a_roots(3)
        self.assertEqual(full_translation_kernel_rank(roots), 9)
        self.assertEqual(relation_rank_through_arity(roots, 2), 6)
        self.assertEqual(relation_rank_through_arity(roots, 3), 9)
        self.assertEqual(minimum_unit_subset_relation_arity(roots, 4), 3)

    def test_bcc_pair_layer_misses_one_global_relation_and_four_body_closes_it(self):
        roots = bcc_roots()
        self.assertEqual(full_translation_kernel_rank(roots), 5)
        self.assertEqual(relation_rank_through_arity(roots, 2), 4)
        self.assertEqual(relation_rank_through_arity(roots, 3), 4)
        self.assertEqual(relation_rank_through_arity(roots, 4), 5)
        self.assertEqual(minimum_unit_subset_relation_arity(roots, 4), 4)


if __name__ == "__main__":
    unittest.main()
