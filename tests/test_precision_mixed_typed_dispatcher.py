import unittest

from enterprise_math.precision_mixed_typed_dispatcher import (
    RelationChannel,
    Semiring,
    boolean_star,
    compile_mixed_typed,
    lifted_partition_with_bottom,
    matrix_mul,
    partial_totalization,
    ping_pong_operations,
    quotient_matrix,
    raw_common_refinement,
    relation_is_block_sum_stable,
)


class MixedTypedDispatcherTests(unittest.TestCase):
    def test_two_operations_can_cross_activate(self):
        f = (0, 0, 0, 1)
        g = (0, 0, 3, 0)
        p0 = (0, 1, 0, 0)
        f_only = compile_mixed_typed(p0, total_unary_ops=(f,)).partition
        g_only = compile_mixed_typed(p0, total_unary_ops=(g,)).partition
        raw = raw_common_refinement(f_only, g_only)
        joint = compile_mixed_typed(p0, total_unary_ops=(f, g)).partition
        self.assertEqual(f_only, (0, 1, 0, 2))
        self.assertEqual(g_only, p0)
        self.assertEqual(raw, f_only)
        self.assertEqual(joint, (0, 1, 2, 3))

    def test_ping_pong_bound_is_sharp(self):
        n = 8
        f, g, p0 = ping_pong_operations(n)
        result = compile_mixed_typed(p0, total_unary_ops=(f, g))
        self.assertEqual(len(result.history) - 1, n - 2)
        self.assertEqual(result.partition, tuple(range(n)))

    def test_partial_legality_is_part_of_signature(self):
        partial = (None, 0, None)
        result = compile_mixed_typed((0, 0, 0), partial_unary_ops=(partial,))
        self.assertEqual(result.partition, (0, 1, 0))
        self.assertEqual(result.descended_partial_unary, ((None, 0),))

    def test_partial_totalization_uses_distinct_bottom(self):
        partial = (None, 0, None)
        total = partial_totalization(partial)
        lifted = lifted_partition_with_bottom((0, 1, 0))
        result = compile_mixed_typed(lifted, total_unary_ops=(total,))
        self.assertEqual(result.partition, lifted)

    def test_count_relation_and_descended_rows(self):
        weights = (
            (0, 1, 0),
            (0, 0, 1),
            (1, 0, 0),
        )
        count = RelationChannel("count", weights, 0, lambda a, b: a + b)
        result = compile_mixed_typed((0, 0, 0), relation_channels=(count,))
        self.assertEqual(result.partition, (0, 0, 0))
        self.assertEqual(result.descended_relation_rows, (((1,),),))

    def test_semiring_product_descends(self):
        nat = Semiring(0, 1, lambda a, b: a + b, lambda a, b: a * b)
        p = (0, 0, 1)
        left = (
            (1, 0, 1),
            (0, 1, 1),
            (0, 0, 1),
        )
        right = (
            (1, 1, 0),
            (1, 1, 0),
            (0, 0, 1),
        )
        self.assertTrue(relation_is_block_sum_stable(p, left, nat))
        self.assertTrue(relation_is_block_sum_stable(p, right, nat))
        product = matrix_mul(left, right, nat)
        self.assertTrue(relation_is_block_sum_stable(p, product, nat))
        self.assertEqual(
            quotient_matrix(p, product, nat),
            matrix_mul(quotient_matrix(p, left, nat), quotient_matrix(p, right, nat), nat),
        )

    def test_boolean_reachability_descends(self):
        boolean = Semiring(False, True, lambda a, b: a or b, lambda a, b: a and b)
        p = (0, 0, 1)
        rel = (
            (False, True, True),
            (True, False, True),
            (False, False, True),
        )
        self.assertTrue(relation_is_block_sum_stable(p, rel, boolean))
        fine_star = boolean_star(rel)
        coarse = quotient_matrix(p, rel, boolean)
        self.assertEqual(quotient_matrix(p, fine_star, boolean), boolean_star(coarse))


if __name__ == "__main__":
    unittest.main()
