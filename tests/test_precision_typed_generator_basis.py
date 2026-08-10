import unittest

from enterprise_math.precision_typed_generator_basis import (
    compile_unary_operations,
    forbidden_coarse_partitions,
    inclusion_minimal_private_witnesses,
    kill_table,
    maximum_generator_disjoint_forbidden_packing,
    minimum_carrier_basis_masks,
    minimum_semantic_operation_basis_masks,
    quotient_operation_reconstructible,
    selected_indices,
    transformation_monoid_closure,
    unary_operation_stable,
)


class TypedGeneratorBasisTests(unittest.TestCase):
    def test_ping_pong_basis_has_integer_optimality_certificate(self):
        f = (0, 0, 2, 2)
        g = (0, 1, 1, 3)
        p0 = (0, 1, 1, 1)
        target = compile_unary_operations(p0, (f, g))
        self.assertEqual(target, (0, 1, 2, 3))
        worlds, masks = kill_table(p0, target, (f, g), unary_operation_stable)
        bases = minimum_carrier_basis_masks(2, masks)
        self.assertEqual(bases, (3,))
        private = inclusion_minimal_private_witnesses(3, worlds, masks, 2)
        self.assertEqual({i for i, _ in private}, {0, 1})
        packing = maximum_generator_disjoint_forbidden_packing(worlds, masks, 2)
        self.assertEqual(len(packing), 2)

    def test_contextual_redundancy_is_not_monotone(self):
        f = (0, 0, 0, 1)
        g = (0, 0, 3, 0)
        p0 = (0, 1, 0, 0)
        self.assertEqual(compile_unary_operations(p0, (g,)), p0)
        self.assertNotEqual(
            compile_unary_operations(p0, (f,)),
            compile_unary_operations(p0, (f, g)),
        )

    def test_pairwise_merge_checks_do_not_lock_global_carrier(self):
        p0 = (0, 0, 0, 1)
        cycle = (1, 2, 0, 3)
        splitter = (3, 1, 2, 3)
        target = compile_unary_operations(p0, (cycle, splitter))
        self.assertEqual(target, (0, 1, 2, 3))
        one_pair_worlds = [
            p for p in forbidden_coarse_partitions(p0, target)
            if len(set(p)) == 3
        ]
        self.assertTrue(one_pair_worlds)
        self.assertTrue(all(not unary_operation_stable(p, cycle) for p in one_pair_worlds))
        self.assertTrue(unary_operation_stable(p0, cycle))
        self.assertEqual(compile_unary_operations(p0, (cycle,)), p0)

    def test_carrier_basis_can_be_strictly_smaller_than_semantic_basis(self):
        p0 = (0, 1)
        swap = (1, 0)
        target = compile_unary_operations(p0, (swap,))
        worlds, masks = kill_table(p0, target, (swap,), unary_operation_stable)
        self.assertEqual(worlds, ())
        self.assertEqual(minimum_carrier_basis_masks(1, masks), (0,))
        semantic = minimum_semantic_operation_basis_masks(target, (swap,))
        self.assertEqual(semantic, (1,))

    def test_quotient_only_reconstruction_can_remove_fine_nonidentity(self):
        target = (0, 0, 1, 1)
        within_block_swap = (1, 0, 3, 2)
        self.assertTrue(quotient_operation_reconstructible(target, (), within_block_swap))
        fine_identity_closure = transformation_monoid_closure((), 4)
        self.assertNotIn(within_block_swap, fine_identity_closure)
        self.assertEqual(minimum_semantic_operation_basis_masks(target, (within_block_swap,)), (0,))

    def test_selected_indices_are_integer_mask_based(self):
        self.assertEqual(selected_indices(0b10101, 5), (0, 2, 4))


if __name__ == "__main__":
    unittest.main()
