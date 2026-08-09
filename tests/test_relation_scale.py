import itertools
import unittest

from enterprise_math.relation_scale import (
    coarsen_primitive_relation_state,
    primitive_relation_state,
    relation_scale_chain_product,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


class RelationScaleTests(unittest.TestCase):
    def test_primitive_factorization_round_trips_scale(self):
        for block_sizes in ((1, 1, 1), (2, 2), (4, 6, 10), (3, 6, 9, 12)):
            for totals in itertools.product(range(-2, 3), repeat=len(block_sizes)):
                field = weighted_relation_field(block_sizes, totals)
                scale, primitive_sizes, primitive_field = primitive_relation_state(
                    block_sizes, field
                )
                self.assertEqual(
                    tuple(scale * value for value in primitive_sizes),
                    block_sizes,
                )
                self.assertEqual(
                    tuple(
                        tuple(scale * value for value in row)
                        for row in primitive_field
                    ),
                    field,
                )

    def test_equal_size_partition_creates_relation_scale_carry(self):
        block_sizes = (1, 1, 1, 1)
        totals = (3, -1, 2, -4)
        field = weighted_relation_field(block_sizes, totals)
        scale, primitive_sizes, primitive_field = primitive_relation_state(
            block_sizes, field
        )
        self.assertEqual(scale, 1)

        carry, new_scale, new_sizes, new_field = coarsen_primitive_relation_state(
            scale,
            primitive_sizes,
            primitive_field,
            ((0, 1), (2, 3)),
        )
        self.assertEqual(carry, 2)
        self.assertEqual(new_scale, 2)
        self.assertEqual(new_sizes, (1, 1))
        self.assertEqual(
            new_field,
            weighted_relation_field(new_sizes, (2, -2)),
        )

    def test_unequal_partition_can_have_unit_scale_carry(self):
        block_sizes = (1, 1, 1, 1, 1)
        totals = (2, -1, 3, -2, -2)
        field = weighted_relation_field(block_sizes, totals)
        scale, primitive_sizes, primitive_field = primitive_relation_state(
            block_sizes, field
        )
        carry, new_scale, new_sizes, _ = coarsen_primitive_relation_state(
            scale,
            primitive_sizes,
            primitive_field,
            ((0, 1), (2, 3, 4)),
        )
        self.assertEqual(carry, 1)
        self.assertEqual(new_scale, 1)
        self.assertEqual(new_sizes, (2, 3))

    def test_scale_carries_multiply_along_nested_coarsening(self):
        block_sizes = (1,) * 8
        totals = (4, -1, 3, -2, 1, -3, 2, -4)
        field = weighted_relation_field(block_sizes, totals)
        scale, sizes, relation = primitive_relation_state(block_sizes, field)

        carries = []
        carry, scale, sizes, relation = coarsen_primitive_relation_state(
            scale,
            sizes,
            relation,
            ((0, 1), (2, 3), (4, 5), (6, 7)),
        )
        carries.append(carry)
        self.assertEqual((carry, scale, sizes), (2, 2, (1, 1, 1, 1)))

        carry, scale, sizes, relation = coarsen_primitive_relation_state(
            scale,
            sizes,
            relation,
            ((0, 1), (2, 3)),
        )
        carries.append(carry)
        self.assertEqual((carry, scale, sizes), (2, 4, (1, 1)))

        carry, scale, sizes, relation = coarsen_primitive_relation_state(
            scale,
            sizes,
            relation,
            ((0, 1),),
        )
        carries.append(carry)
        self.assertEqual((carry, scale, sizes), (2, 8, (1,)))
        self.assertEqual(relation_scale_chain_product(1, tuple(carries)), 8)


if __name__ == "__main__":
    unittest.main()
