import itertools
import unittest

from enterprise_math.guard_image_lattice import (
    all_guards_descend,
    guard_image_is_full_rank,
    guard_kernel_image_generators,
    guard_kernel_image_rank,
    guard_rank_one_step,
    integer_matrix_rank,
    partition_kernel_basis,
    rank_one_lattice_step,
    rank_one_threshold_pattern_interval,
    rank_one_threshold_pattern_reachable,
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
        # Here W(K_A)=2 Z^2. Every affine coset g+2 Z^2 reaches all four
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

    def test_rank_one_step_recovers_exact_subgroup_generator(self):
        self.assertEqual(
            rank_one_lattice_step(((4, 6), (-6, -9), (2, 3))),
            (2, 3),
        )
        self.assertEqual(
            rank_one_lattice_step(((-8, 4, 0), (12, -6, 0))),
            (4, -2, 0),
        )

    def test_guard_rank_one_step_from_partition_coefficients(self):
        partition = ((0, 1, 2),)
        guards = (
            (0, 1, 2),
            (0, 2, 4),
        )
        self.assertEqual(guard_kernel_image_rank(guards, partition), 1)
        self.assertEqual(guard_rank_one_step(guards, partition), (1, 2))

    def test_rank_one_threshold_pattern_interval_matches_bruteforce(self):
        steps = ((1, 1), (1, -1), (2, 3), (0, 2), (3, 0))
        for step in steps:
            for base in itertools.product(range(-3, 4), repeat=2):
                for pattern in itertools.product((False, True), repeat=2):
                    interval = rank_one_threshold_pattern_interval(
                        base, step, pattern
                    )
                    brute = [
                        t
                        for t in range(-60, 61)
                        if all(
                            (base[index] + t * step[index] >= 0)
                            if pattern[index]
                            else (base[index] + t * step[index] < 0)
                            for index in range(2)
                        )
                    ]
                    if interval is None:
                        self.assertEqual(brute, [], msg=(base, step, pattern))
                        self.assertFalse(
                            rank_one_threshold_pattern_reachable(
                                base, step, pattern
                            )
                        )
                        continue

                    lower, upper = interval
                    self.assertTrue(
                        rank_one_threshold_pattern_reachable(base, step, pattern)
                    )
                    self.assertTrue(brute, msg=(base, step, pattern, interval))
                    for t in brute:
                        if lower is not None:
                            self.assertGreaterEqual(t, lower)
                        if upper is not None:
                            self.assertLessEqual(t, upper)

                    # Every point in the finite part of the predicted interval
                    # must realize the pattern exactly.
                    check_lower = lower if lower is not None else -20
                    check_upper = upper if upper is not None else 20
                    for t in range(max(check_lower, -20), min(check_upper, 20) + 1):
                        self.assertTrue(
                            all(
                                (base[index] + t * step[index] >= 0)
                                if pattern[index]
                                else (base[index] + t * step[index] < 0)
                                for index in range(2)
                            )
                        )

    def test_same_rank_one_rank_can_have_different_reachable_patterns(self):
        base = (0, 0)
        diagonal = (1, 1)
        anti_diagonal = (1, -1)
        patterns = tuple(itertools.product((False, True), repeat=2))
        diagonal_reachable = {
            pattern
            for pattern in patterns
            if rank_one_threshold_pattern_reachable(base, diagonal, pattern)
        }
        anti_reachable = {
            pattern
            for pattern in patterns
            if rank_one_threshold_pattern_reachable(base, anti_diagonal, pattern)
        }
        self.assertNotEqual(diagonal_reachable, anti_reachable)


if __name__ == "__main__":
    unittest.main()
