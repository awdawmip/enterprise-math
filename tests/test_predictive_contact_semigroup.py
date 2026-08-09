import itertools
import unittest

from enterprise_math.predictive_contact_semigroup import (
    action_gcd,
    action_language_is_bidirectional,
    apply_bidirectional_coordinate_action,
    bidirectional_contact_coordinate,
    bidirectional_contact_from_coordinate,
    closing_shell_semigroup_class_count,
    closing_shell_semigroup_rank,
    reachable_positive_sums,
    separating_gcd_class_count,
    separating_gcd_is_minimal,
    separating_semigroup_class_count,
    separating_semigroup_holes,
    separating_semigroup_rank,
)
from enterprise_math.predictive_quotient import (
    finite_horizon_partition,
    restricted_block_count,
    stable_predictive_partition,
)


class OneSidedSemigroupTests(unittest.TestCase):
    def test_reachable_sums_bounded_and_stable(self) -> None:
        self.assertEqual(reachable_positive_sums((4, 6), 7, None), (0, 4, 6))
        self.assertEqual(reachable_positive_sums((4, 6), 13, None), (0, 4, 6, 8, 10, 12))
        self.assertEqual(reachable_positive_sums((4, 6), 13, 1), (0, 4, 6))
        self.assertEqual(reachable_positive_sums((4, 6), 13, 2), (0, 4, 6, 8, 10, 12))

    def test_separating_class_count_matches_direct_future_signatures(self) -> None:
        families = ((2,), (4, 6), (6, 10), (4, 7), (6, 9, 20))
        for precision in range(1, 18):
            for actions in families:
                for horizon in range(0, 6):
                    words = [()]
                    for length in range(1, horizon + 1):
                        words.extend(itertools.product(actions, repeat=length))
                    signatures = set()
                    ranks = set()
                    for gap in range(precision):
                        signatures.add(
                            tuple(
                                gap + sum(word) < precision
                                for word in words
                            )
                        )
                        ranks.add(
                            separating_semigroup_rank(
                                gap,
                                precision,
                                actions,
                                horizon,
                            )
                        )
                    self.assertEqual(len(signatures), len(ranks))
                    self.assertEqual(
                        len(signatures),
                        separating_semigroup_class_count(
                            precision,
                            actions,
                            horizon,
                        ),
                    )

    def test_stable_one_sided_gcd_can_over_refine(self) -> None:
        precision = 7
        actions = (4, 6)
        self.assertEqual(action_gcd(actions), 2)
        self.assertEqual(separating_semigroup_holes(precision, actions), (2,))
        self.assertEqual(separating_semigroup_class_count(precision, actions), 3)
        self.assertEqual(separating_gcd_class_count(precision, actions), 4)
        self.assertFalse(separating_gcd_is_minimal(precision, actions))

    def test_gcd_is_minimal_exactly_when_all_small_gcd_multiples_are_reachable(self) -> None:
        for precision in range(1, 30):
            for actions in ((2,), (4, 6), (6, 10), (4, 8, 12), (6, 9, 20)):
                holes = separating_semigroup_holes(precision, actions)
                self.assertEqual(separating_gcd_is_minimal(precision, actions), not holes)
                if not holes:
                    self.assertEqual(
                        separating_semigroup_class_count(precision, actions),
                        separating_gcd_class_count(precision, actions),
                    )
                else:
                    self.assertLess(
                        separating_semigroup_class_count(precision, actions),
                        separating_gcd_class_count(precision, actions),
                    )

    def test_generic_compiler_reconstructs_one_sided_semigroup_classes(self) -> None:
        cases = ((7, (4, 6)), (11, (4, 6)), (17, (6, 10)), (19, (6, 9, 20)))
        for precision, actions in cases:
            for horizon in range(0, 6):
                cap = precision + (horizon + 4) * max(actions)
                states = tuple(range(cap + 1))
                named = {
                    f"sep_{action}": (
                        lambda gap, a=action, c=cap: min(c, gap + a)
                    )
                    for action in actions
                }
                observe = lambda gap, d=precision: gap < d
                partition = finite_horizon_partition(states, named, observe, horizon)
                initial_contact = tuple(range(precision))
                self.assertEqual(
                    restricted_block_count(states, partition, initial_contact),
                    separating_semigroup_class_count(precision, actions, horizon),
                )

    def test_closing_shell_formula_matches_direct_signatures(self) -> None:
        for shell_width in range(1, 18):
            for actions in ((2,), (4, 6), (3, 5), (6, 10)):
                for horizon in range(0, 5):
                    words = [()]
                    for length in range(1, horizon + 1):
                        words.extend(itertools.product(actions, repeat=length))
                    signatures = set()
                    ranks = set()
                    for offset in range(shell_width):
                        signatures.add(
                            tuple(
                                sum(word) > offset
                                for word in words
                            )
                        )
                        ranks.add(
                            closing_shell_semigroup_rank(
                                offset,
                                shell_width,
                                actions,
                                horizon,
                            )
                        )
                    self.assertEqual(len(signatures), len(ranks))
                    self.assertEqual(
                        len(signatures),
                        closing_shell_semigroup_class_count(
                            shell_width,
                            actions,
                            horizon,
                        ),
                    )


class BidirectionalSignedLanguageTests(unittest.TestCase):
    def test_bidirectional_does_not_require_paired_magnitudes(self) -> None:
        actions = (6, -10)
        self.assertTrue(action_language_is_bidirectional(actions))
        self.assertEqual(action_gcd(actions), 2)
        for precision in range(1, 20):
            for gap in range(0, 50):
                coordinate = bidirectional_contact_coordinate(gap, precision, actions)
                self.assertEqual(bidirectional_contact_from_coordinate(coordinate), gap < precision)
                for action in actions:
                    next_gap = max(0, gap + action)
                    next_coordinate = bidirectional_contact_coordinate(
                        next_gap,
                        precision,
                        actions,
                    )
                    self.assertEqual(
                        next_coordinate,
                        apply_bidirectional_coordinate_action(
                            coordinate,
                            precision,
                            action,
                            actions,
                        ),
                    )

    def test_generic_compiler_partition_equals_bidirectional_gcd_coordinate(self) -> None:
        cases = (
            (11, (6, -10), 70),
            (17, (6, 14, -10), 90),
            (19, (9, -15), 100),
            (23, (10, 14, -6), 110),
        )
        for precision, actions, cap in cases:
            states = tuple(range(cap + 1))
            named = {
                f"move_{index}_{action}": (
                    lambda gap, a=action, c=cap: min(c, max(0, gap + a))
                )
                for index, action in enumerate(actions)
            }
            observe = lambda gap, d=precision: gap < d
            stable = stable_predictive_partition(states, named, observe)
            by_label = {}
            by_coordinate = {}
            for state, label in zip(states, stable.partition):
                coordinate = bidirectional_contact_coordinate(state, precision, actions)
                old_coordinate = by_label.setdefault(label, coordinate)
                self.assertEqual(old_coordinate, coordinate)
                old_label = by_coordinate.setdefault(coordinate, label)
                self.assertEqual(old_label, label)


if __name__ == "__main__":
    unittest.main()
