import itertools
import unittest

from enterprise_math.partition_dynamics import (
    internal_update_basis,
    lift_coarse_update,
    partition_internal_update_rank,
    primitive_transfer_image,
    update_lattice_dimension,
)
from enterprise_math.relation_dynamics import aggregate_update


class PartitionDynamicsTests(unittest.TestCase):
    def test_update_dimension_and_kernel_rank(self):
        partitions = {
            4: (((0, 1), (2,), (3,)), ((0, 1), (2, 3))),
            5: (((0, 1, 2), (3,), (4,)), ((0, 2), (1, 3, 4))),
        }
        for block_count, families in partitions.items():
            self.assertEqual(update_lattice_dimension(block_count), block_count - 1)
            for partition in families:
                basis = internal_update_basis(block_count, partition)
                self.assertEqual(
                    len(basis),
                    partition_internal_update_rank(block_count, partition),
                )
                self.assertEqual(
                    len(basis),
                    block_count - len(partition),
                )
                for vector in basis:
                    self.assertEqual(
                        aggregate_update(vector, partition),
                        (0,) * len(partition),
                    )

    def test_every_small_coarse_update_has_an_integer_lift(self):
        block_count = 6
        partition = ((0, 1), (2, 4), (3, 5))
        for left, middle in itertools.product(range(-3, 4), repeat=2):
            coarse = (left, middle, -left - middle)
            fine = lift_coarse_update(block_count, partition, coarse)
            self.assertEqual(sum(fine), 0)
            self.assertEqual(aggregate_update(fine, partition), coarse)

    def test_primitive_transfer_image_is_zero_inside_one_coarse_block(self):
        partition = ((0, 1), (2, 3), (4,))
        self.assertEqual(
            primitive_transfer_image(5, partition, receiver=0, donor=1),
            (0, 0, 0),
        )
        self.assertEqual(
            primitive_transfer_image(5, partition, receiver=2, donor=3),
            (0, 0, 0),
        )

    def test_primitive_transfer_survives_between_coarse_blocks(self):
        partition = ((0, 1), (2, 3), (4,))
        self.assertEqual(
            primitive_transfer_image(5, partition, receiver=0, donor=2),
            (1, -1, 0),
        )
        self.assertEqual(
            primitive_transfer_image(5, partition, receiver=4, donor=1),
            (-1, 0, 1),
        )


if __name__ == "__main__":
    unittest.main()
