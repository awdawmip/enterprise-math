import itertools
import unittest

from enterprise_math.relation_dynamics import (
    aggregate_update,
    coarsening_update_naturality,
    primitive_transfer_update,
    update_weighted_relation_field,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


class RelationDynamicsTests(unittest.TestCase):
    def test_relation_update_matches_direct_total_update(self):
        block_sizes = (2, 1, 3, 2)
        for totals in itertools.product(range(-2, 3), repeat=4):
            field = weighted_relation_field(block_sizes, totals)
            for receiver in range(4):
                for donor in range(4):
                    update = primitive_transfer_update(4, receiver, donor)
                    updated_field = update_weighted_relation_field(
                        block_sizes, field, update
                    )
                    updated_totals = tuple(
                        total + delta for total, delta in zip(totals, update)
                    )
                    self.assertEqual(
                        updated_field,
                        weighted_relation_field(block_sizes, updated_totals),
                    )

    def test_partition_coarsening_commutes_with_all_small_zero_sum_updates(self):
        block_sizes = (1, 2, 1, 3, 2)
        totals = (3, -2, 4, -3, -2)
        field = weighted_relation_field(block_sizes, totals)
        partition = ((0, 1), (2, 4), (3,))
        for prefix in itertools.product(range(-1, 2), repeat=4):
            update = prefix + (-sum(prefix),)
            left, right = coarsening_update_naturality(
                block_sizes, field, update, partition
            )
            self.assertEqual(left, right)

    def test_internal_transfer_becomes_identity_on_coarse_quotient(self):
        update = primitive_transfer_update(4, receiver=0, donor=1)
        partition = ((0, 1), (2,), (3,))
        self.assertEqual(aggregate_update(update, partition), (0, 0, 0))

    def test_cross_block_transfer_becomes_coarse_primitive_transfer(self):
        update = primitive_transfer_update(4, receiver=0, donor=2)
        partition = ((0, 1), (2,), (3,))
        self.assertEqual(aggregate_update(update, partition), (1, -1, 0))


if __name__ == "__main__":
    unittest.main()
