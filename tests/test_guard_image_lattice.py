import itertools
import unittest

from enterprise_math.guard_image_lattice import (
    all_guards_descend,
    guard_image_is_full_rank,
    guard_kernel_image_generators,
    guard_kernel_image_rank,
    integer_matrix_rank,
    partition_kernel_basis,
)


class GuardImageLatticeTests(unittest.TestCase):
    def test_partition_kernel_basis_has_expected_rank_and_zero_block_sums(self):
        partition = ((0, 1, 2), (3, 4), (5,))
        basis = partition_kernel_basis(6, partition)
        self.assertEqual(len(basis), 3)
        for vector in basis:
            self.assertEqual(sum(vector[index] for index in partition[0]), 0)
            self.assertEqual(sum(vector[index] for index in partition[1]), 0)
            self.assertEqual(sum(vector[index] for index in partition[2]), 0)

    def test_visible_guard_family_has_zero_hidden_rank(self):
        partition = ((0, 1), (2, 3))
        guards = (
            (2, 2, -1, -1),
            (0, 0, 5, 5),
        )
        self.assertEqual(guard_kernel_image_rank(guards, partition), 0)
        self.assertTrue(all_guards_descend(guards, partition))
        self.assertFalse(guard_image_is_full_rank(guards, partition))

    def test_independent_hidden_guards_have_full_rank_image(self):
        partition = ((0, 1), (2, 3))
        guards = (
            (1, -1, 0, 0),
            (0, 0, 1, -1),
        )
        self.assertEqual(
            guard_kernel_image_generators(guards, partition),
            ((-2, 0), (0, -2)),
        )
        self.assertEqual(guard_kernel_image_rank(guards, partition), 2)
        self.assertTrue(guard_image_is_full_rank(guards, partition))

    def test_dependent_hidden_guards_have_partial_rank(self):
        partition = ((0, 1, 2),)
        guards = (
            (1, -1, 0),
            (2, -2, 0),
        )
        self.assertEqual(guard_kernel_image_rank(guards, partition), 1)
        self.assertFalse(all_guards_descend(guards, partition))
        self.assertFalse(guard_image_is_full_rank(guards, partition))

    def test_fraction_free_rank_matches_minor_expectations(self):
        cases = (
            ((), 0, 0),
            (((0, 0),), 2, 0),
            (((2, 4), (1, 2)), 2, 1),
            (((2, 0), (0, 3)), 2, 2),
            (((1, 2, 3), (2, 4, 6), (0, 1, 1)), 3, 2),
        )
        for rows, width, expected in cases:
            self.assertEqual(integer_matrix_rank(rows, width), expected)

    def test_rank_is_invariant_under_small_integer_row_scaling_and_addition(self):
        base = ((1, 2, 0), (0, 1, 1))
        variants = (
            base,
            ((2, 4, 0), (0, -3, -3)),
            ((1, 3, 1), (0, 1, 1)),
        )
        for matrix in variants:
            self.assertEqual(integer_matrix_rank(matrix), 2)

    def test_full_rank_guard_cosets_hit_every_open_orthant_in_reference_case(self):
        # Here W(K_A)=2 Z^2.  Every affine coset g+2 Z^2 reaches all four
        # strict sign patterns by choosing sufficiently large signed integers.
        for base in itertools.product(range(-2, 3), repeat=2):
            hits = set()
            for left in range(-5, 6):
                for right in range(-5, 6):
                    score = (base[0] + 2 * left, base[1] + 2 * right)
                    if score[0] == 0 or score[1] == 0:
                        continue
                    hits.add((score[0] > 0, score[1] > 0))
            self.assertEqual(
                hits,
                {(False, False), (False, True), (True, False), (True, True)},
            )


if __name__ == "__main__":
    unittest.main()
