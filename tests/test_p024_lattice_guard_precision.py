import unittest
from itertools import product

from enterprise_math.lattice_guard_precision import (
    IntegerGuard,
    classify_projected_action_monoid,
    direct_future_guard_signature,
    dot,
    guard_rank_signature,
    nonnegative_2d_semigroup_contains,
    positive_zero_relation_inverse_words,
    primitive_score_vector,
    rank_box_sizes,
    reachable_translation_sums,
)


class LatticeGuardPrecisionTests(unittest.TestCase):
    def test_nonprimitive_guard_normalization_is_exact(self) -> None:
        guard = IntegerGuard((2, 4), 3)
        self.assertEqual(guard.coefficient_gcd, 2)
        self.assertEqual(guard.primitive_row, (1, 2))
        self.assertEqual(guard.primitive_threshold, 2)
        for point in product(range(-4, 5), repeat=2):
            self.assertEqual(guard.evaluate(point), dot((1, 2), point) >= 2)

    def test_rank_signature_equals_direct_future_signature_equivalence(self) -> None:
        cases = [
            (
                (IntegerGuard((1,), 0),),
                ((2,), (3,)),
                range(-7, 8),
                3,
            ),
            (
                (IntegerGuard((2,), 1), IntegerGuard((-3,), 2)),
                ((1,), (-2,)),
                range(-6, 7),
                2,
            ),
            (
                (IntegerGuard((1, 1), 0), IntegerGuard((1, -2), 1)),
                ((1, 0), (0, 1)),
                range(-2, 3),
                2,
            ),
            (
                (IntegerGuard((2, 2), 1), IntegerGuard((0, 3), -1)),
                ((1, 1), (-1, 0)),
                range(-2, 3),
                2,
            ),
        ]

        for guards, actions, coordinate_range, horizon in cases:
            dimension = len(guards[0].row)
            points = list(product(coordinate_range, repeat=dimension))
            direct = {
                point: direct_future_guard_signature(point, guards, actions, horizon)
                for point in points
            }
            ranks = {
                point: guard_rank_signature(point, guards, actions, horizon)
                for point in points
            }
            for left in points:
                for right in points:
                    self.assertEqual(
                        direct[left] == direct[right],
                        ranks[left] == ranks[right],
                        msg=(guards, actions, horizon, left, right),
                    )

    def test_kernel_of_guard_score_map_is_future_invisible(self) -> None:
        guards = (
            IntegerGuard((1, 1), 0),
            IntegerGuard((2, 2), 3),
        )
        actions = ((2, -1), (-3, 4))
        base = (5, -2)
        shifted = (base[0] + 7, base[1] - 7)
        self.assertEqual(primitive_score_vector(base, guards), primitive_score_vector(shifted, guards))
        for horizon in range(5):
            self.assertEqual(
                direct_future_guard_signature(base, guards, actions, horizon),
                direct_future_guard_signature(shifted, guards, actions, horizon),
            )
            self.assertEqual(
                guard_rank_signature(base, guards, actions, horizon),
                guard_rank_signature(shifted, guards, actions, horizon),
            )

    def test_surjective_coordinate_scores_realize_product_rank_box(self) -> None:
        guards = (
            IntegerGuard((1, 0), 2),
            IntegerGuard((0, 1), -1),
        )
        actions = ((1, 0), (0, -1))
        horizon = 2
        sizes = rank_box_sizes(guards, actions, horizon)
        signatures = {
            guard_rank_signature(point, guards, actions, horizon)
            for point in product(range(-8, 9), repeat=2)
        }
        self.assertEqual(len(signatures), sizes[0] * sizes[1])
        self.assertEqual(signatures, set(product(range(sizes[0]), range(sizes[1]))))

    def test_score_lattice_can_remove_rank_cells(self) -> None:
        # Primitive score image is {(u,v): u == v (mod 2)}.
        guards = (
            IntegerGuard((1, 1), 2),
            IntegerGuard((1, -1), 2),
        )
        actions = ((1, 0),)
        horizon = 2
        self.assertEqual(rank_box_sizes(guards, actions, horizon), (4, 4))
        signatures = {
            guard_rank_signature(point, guards, actions, horizon)
            for point in product(range(-6, 7), repeat=2)
        }
        self.assertEqual(len(signatures), 14)
        missing = set(product(range(4), repeat=2)) - signatures
        self.assertEqual(missing, {(1, 2), (2, 1)})

    def test_action_monoid_type_is_guard_direction_relative(self) -> None:
        actions = ((1, 1), (-1, 1))
        x_guard = IntegerGuard((1, 0), 0)
        y_guard = IntegerGuard((0, 1), 0)
        self.assertEqual(classify_projected_action_monoid(x_guard, actions).kind, "two_sided_group")
        self.assertEqual(classify_projected_action_monoid(x_guard, actions).grain, 1)
        self.assertEqual(classify_projected_action_monoid(y_guard, actions).kind, "positive_semigroup")
        self.assertEqual(classify_projected_action_monoid(y_guard, actions).grain, 1)

    def test_positive_zero_relation_constructs_all_generator_inverses(self) -> None:
        actions = ((1, 0), (0, 1), (-1, -1))
        inverse_words = positive_zero_relation_inverse_words(actions, (1, 1, 1))
        for index, word in enumerate(inverse_words):
            total = [0, 0]
            for count, action in zip(word, actions, strict=True):
                self.assertGreaterEqual(count, 0)
                total[0] += count * action[0]
                total[1] += count * action[1]
            self.assertEqual(tuple(total), tuple(-value for value in actions[index]))

    def test_higher_dimensional_affine_semigroup_can_have_infinite_boundary_holes(self) -> None:
        generators = ((2, 0), (0, 1), (1, 1))
        for k in range(25):
            self.assertTrue(nonnegative_2d_semigroup_contains((2 * k, 0), generators))
            self.assertFalse(nonnegative_2d_semigroup_contains((2 * k + 1, 0), generators))
            # The conductor translate (0,1) + N^2 is contained in the semigroup.
            for y in range(5):
                self.assertTrue(nonnegative_2d_semigroup_contains((k, y + 1), generators))

    def test_aggregate_observable_can_be_strictly_coarser_than_full_guard_rank(self) -> None:
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        actions = ((1, 1),)
        left = (-1, 1)
        right = (1, -1)
        self.assertNotEqual(guard_rank_signature(left, guards, actions, 1), guard_rank_signature(right, guards, actions, 1))

        sums = reachable_translation_sums(actions, 1)
        left_and = tuple(all(guard.evaluate((left[0] + s[0], left[1] + s[1])) for guard in guards) for s in sums)
        right_and = tuple(all(guard.evaluate((right[0] + s[0], right[1] + s[1])) for guard in guards) for s in sums)
        self.assertEqual(left_and, right_and)


if __name__ == "__main__":
    unittest.main()
