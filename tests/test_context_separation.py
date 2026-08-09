import unittest
from itertools import combinations, product
from math import comb

from enterprise_math.context_separation import (
    apply_context_path,
    context_split_spectrum,
    contextual_refinement_chain,
    minimum_distinguishing_context,
    pair_separation_depth_from_chain,
    pair_separation_matrix,
    partition_collision_coefficients,
    reconstruct_partition_from_separation,
    reverse_context_distance,
    subset_separation_depth,
    time_kernel_is_monotone,
    time_kernel_partition,
    unary_partition_compatible,
)
from enterprise_math.contextual_closure import FiniteOperation
from enterprise_math.predictive_closure import observation_partition, partition_refines


class ContextSeparationTests(unittest.TestCase):
    def test_separation_matrix_reconstructs_every_refinement_level(self) -> None:
        states = (0, 1, 2, 3)
        table = (
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 3, 1,
        )
        operation = FiniteOperation(
            "mu", 2, lambda args: table[4 * args[0] + args[1]]
        )
        labels = (0, 1, 0, 0)
        observation = lambda x: labels[x]
        chain = contextual_refinement_chain(states, (operation,), observation)
        separation = pair_separation_matrix(states, chain)
        for depth, expected in enumerate(chain):
            self.assertEqual(
                reconstruct_partition_from_separation(states, separation, depth),
                expected,
            )

    def test_shortest_context_length_equals_first_separation_depth(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        chain = contextual_refinement_chain(states, (operation,), observation)
        for x, y in combinations(states, 2):
            depth = pair_separation_depth_from_chain(chain, x, y)
            path = minimum_distinguishing_context(
                states, (operation,), observation, x, y
            )
            if depth is None:
                self.assertIsNone(path)
            else:
                self.assertIsNotNone(path)
                self.assertEqual(len(path), depth)
                self.assertNotEqual(
                    observation(apply_context_path(path, (operation,), x)),
                    observation(apply_context_path(path, (operation,), y)),
                )

    def test_exhaustive_two_state_binary_shortest_context_certificates(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for labels in product((0, 1), repeat=2):
                observation = lambda x, labels=labels: labels[x]
                chain = contextual_refinement_chain(states, (operation,), observation)
                depth = pair_separation_depth_from_chain(chain, 0, 1)
                path = minimum_distinguishing_context(
                    states, (operation,), observation, 0, 1
                )
                if depth is None:
                    self.assertIsNone(path)
                else:
                    self.assertIsNotNone(path)
                    self.assertEqual(len(path), depth)

    def test_reverse_context_distance_satisfies_ultrametric_inequality(self) -> None:
        states = (0, 1, 2, 3)
        table = (
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 3, 1,
        )
        operation = FiniteOperation(
            "mu", 2, lambda args: table[4 * args[0] + args[1]]
        )
        labels = (0, 1, 0, 0)
        observation = lambda x: labels[x]
        chain = contextual_refinement_chain(states, (operation,), observation)
        stable_depth = len(chain) - 1
        separation = pair_separation_matrix(states, chain)

        for x, y, z in product(states, repeat=3):
            dxy = reverse_context_distance(stable_depth, separation[(x, y)])
            dyz = reverse_context_distance(stable_depth, separation[(y, z)])
            dxz = reverse_context_distance(stable_depth, separation[(x, z)])
            self.assertLessEqual(dxz, max(dxy, dyz))

    def test_higher_subset_depth_is_minimum_pairwise_depth(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        chain = contextual_refinement_chain(states, (operation,), observation)
        separation = pair_separation_matrix(states, chain)
        for size in range(2, len(states) + 1):
            for subset in combinations(states, size):
                depth = subset_separation_depth(subset, separation)
                finite_pair_depths = [
                    separation[pair]
                    for pair in combinations(subset, 2)
                    if separation[pair] is not None
                ]
                expected = min(finite_pair_depths) if finite_pair_depths else None
                self.assertEqual(depth, expected)

    def test_split_coefficients_count_first_distinguished_subsets(self) -> None:
        states = (0, 1, 2, 3, 4)
        operation = FiniteOperation(
            "step", 1, lambda args: (0, 0, 4, 4, 4)[args[0]]
        )
        observation = lambda x: 0 if x < 4 else 1
        chain = contextual_refinement_chain(states, (operation,), observation)
        increments = context_split_spectrum(chain)
        self.assertEqual(len(increments), len(chain) - 1)
        for depth, increment in enumerate(increments):
            coarse_map = {
                state: block for block in chain[depth] for state in block
            }
            fine_map = {
                state: block for block in chain[depth + 1] for state in block
            }
            for size in range(2, len(states) + 1):
                count = 0
                for subset in combinations(states, size):
                    if (
                        len({coarse_map[state] for state in subset}) == 1
                        and len({fine_map[state] for state in subset}) > 1
                    ):
                        count += 1
                coefficient = increment[size - 1] if size - 1 < len(increment) else 0
                self.assertEqual(coefficient, count)

    def test_context_split_spectrum_telescopes(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        chain = contextual_refinement_chain(states, (operation,), observation)
        increments = context_split_spectrum(chain)
        start = partition_collision_coefficients(chain[0])
        finish = partition_collision_coefficients(chain[-1])
        length = max(len(start), len(finish), *(len(row) for row in increments))
        for index in range(length):
            left = (start[index] if index < len(start) else 0) - (
                finish[index] if index < len(finish) else 0
            )
            right = sum(row[index] if index < len(row) else 0 for row in increments)
            self.assertEqual(left, right)

    def test_unlabelled_split_spectrum_does_not_recover_labelled_history(self) -> None:
        states = (0, 1, 2, 3, 4)
        observation = lambda x: 0 if x < 4 else 1
        first = FiniteOperation(
            "first", 1, lambda args: (0, 0, 4, 4, 4)[args[0]]
        )
        second = FiniteOperation(
            "second", 1, lambda args: (0, 4, 0, 4, 4)[args[0]]
        )
        chain_first = contextual_refinement_chain(states, (first,), observation)
        chain_second = contextual_refinement_chain(states, (second,), observation)
        self.assertEqual(
            tuple(partition_collision_coefficients(p) for p in chain_first),
            tuple(partition_collision_coefficients(p) for p in chain_second),
        )
        sep_first = pair_separation_matrix(states, chain_first)
        sep_second = pair_separation_matrix(states, chain_second)
        self.assertNotEqual(sep_first[(0, 1)], sep_second[(0, 1)])
        self.assertNotEqual(sep_first[(0, 2)], sep_second[(0, 2)])

    def test_more_operations_can_only_separate_at_same_or_smaller_depth(self) -> None:
        states = (0, 1, 2, 3)
        observation = lambda x: 0 if x < 3 else 1
        f = FiniteOperation("f", 1, lambda args: (0, 0, 1, 0)[args[0]])
        g = FiniteOperation("g", 1, lambda args: (0, 3, 0, 0)[args[0]])
        f_chain = contextual_refinement_chain(states, (f,), observation)
        joint_chain = contextual_refinement_chain(states, (f, g), observation)
        f_sep = pair_separation_matrix(states, f_chain)
        joint_sep = pair_separation_matrix(states, joint_chain)
        joint_h = len(joint_chain)
        f_h = len(f_chain)
        infinity = joint_h + f_h + 10
        for x, y in product(states, repeat=2):
            left = joint_sep[(x, y)] if joint_sep[(x, y)] is not None else infinity
            right = f_sep[(x, y)] if f_sep[(x, y)] is not None else infinity
            self.assertLessEqual(left, right)

    def test_stable_contextual_closure_restores_time_kernel_monotonicity(self) -> None:
        states = (0, 1, 2)
        observation = lambda x: 0 if x < 2 else 1
        fine_map = (0, 2, 2)
        operation_function = lambda x: fine_map[x]
        operation = FiniteOperation("F", 1, lambda args: operation_function(args[0]))
        chain = contextual_refinement_chain(states, (operation,), observation)
        raw = chain[0]
        stable = chain[-1]

        self.assertFalse(unary_partition_compatible(states, operation_function, raw))
        self.assertFalse(time_kernel_is_monotone(states, operation_function, raw, 3))
        self.assertTrue(unary_partition_compatible(states, operation_function, stable))
        self.assertTrue(time_kernel_is_monotone(states, operation_function, stable, 3))

        raw_zero = time_kernel_partition(states, operation_function, raw, 0)
        raw_one = time_kernel_partition(states, operation_function, raw, 1)
        self.assertFalse(partition_refines(raw_zero, raw_one))
        self.assertFalse(partition_refines(raw_one, raw_zero))

    def test_context_axis_decreases_collisions_while_closed_time_row_increases(self) -> None:
        states = (0, 1, 2)
        observation = lambda x: 0 if x < 2 else 1
        fine_map = (0, 2, 2)
        operation_function = lambda x: fine_map[x]
        operation = FiniteOperation("F", 1, lambda args: operation_function(args[0]))
        chain = contextual_refinement_chain(states, (operation,), observation)

        # Context refinement only splits fibers, so all P011 coefficients decrease.
        for coarse, fine in zip(chain, chain[1:]):
            coarse_coeff = partition_collision_coefficients(coarse)
            fine_coeff = partition_collision_coefficients(fine)
            length = max(len(coarse_coeff), len(fine_coeff))
            for index in range(length):
                self.assertGreaterEqual(
                    coarse_coeff[index] if index < len(coarse_coeff) else 0,
                    fine_coeff[index] if index < len(fine_coeff) else 0,
                )

        # On the stable congruent row, deterministic time can only merge histories.
        stable = chain[-1]
        partitions = [
            time_kernel_partition(states, operation_function, stable, step)
            for step in range(3)
        ]
        for old, new in zip(partitions, partitions[1:]):
            old_coeff = partition_collision_coefficients(old)
            new_coeff = partition_collision_coefficients(new)
            length = max(len(old_coeff), len(new_coeff))
            for index in range(length):
                self.assertLessEqual(
                    old_coeff[index] if index < len(old_coeff) else 0,
                    new_coeff[index] if index < len(new_coeff) else 0,
                )


if __name__ == "__main__":
    unittest.main()
