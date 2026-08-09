import unittest
from itertools import combinations

from enterprise_math.box_collapse import LabeledIntegerBox, intersect_boxes
from enterprise_math.box_conflict_repair import (
    box_conflict_edges,
    common_target_exists_after_deletions,
    deletion_set_is_vertex_cover,
    minimum_common_target_deletion_sets,
    target_first_common_target_repair,
)


class BoxConflictRepairTests(unittest.TestCase):
    def test_conflict_graph_exactly_matches_common_target_existence_after_deletions(self):
        boxes = (
            LabeledIntegerBox(0, (0, 0), (2, 2)),
            LabeledIntegerBox(1, (1, 1), (3, 3)),
            LabeledIntegerBox(2, (4, 0), (6, 2)),
            LabeledIntegerBox(3, (2, -1), (5, 1)),
        )
        labels = [box.label for box in boxes]
        edges = box_conflict_edges(boxes)
        for count in range(len(labels)):
            for removed in combinations(labels, count):
                remaining = [box for box in boxes if box.label not in removed]
                direct = True if len(remaining) == 1 else intersect_boxes(remaining) is not None
                self.assertEqual(
                    common_target_exists_after_deletions(boxes, removed),
                    direct,
                )
                self.assertEqual(
                    deletion_set_is_vertex_cover(edges, removed),
                    direct,
                )

    def test_pair_first_and_target_first_repair_oracles_agree(self):
        families = (
            (
                LabeledIntegerBox(0, (0,), (1,)),
                LabeledIntegerBox(1, (3,), (4,)),
                LabeledIntegerBox(2, (0,), (1,)),
            ),
            (
                LabeledIntegerBox(0, (0, 0), (3, 3)),
                LabeledIntegerBox(1, (2, 2), (5, 5)),
                LabeledIntegerBox(2, (4, 0), (7, 2)),
                LabeledIntegerBox(3, (1, -2), (4, 1)),
            ),
            (
                LabeledIntegerBox(0, (-1000, -1000), (-900, -900)),
                LabeledIntegerBox(1, (0, 0), (100, 100)),
                LabeledIntegerBox(2, (-950, -950), (50, 50)),
                LabeledIntegerBox(3, (25, 25), (75, 75)),
            ),
        )
        for boxes in families:
            pair_first = minimum_common_target_deletion_sets(boxes)
            target_first = target_first_common_target_repair(boxes)
            self.assertEqual(
                target_first.minimum_deletions,
                pair_first.minimum_deletions,
            )
            self.assertEqual(
                set(target_first.minimum_deletion_sets),
                set(pair_first.minimum_deletion_sets),
            )
            self.assertEqual(
                target_first.maximum_occupancy,
                len(boxes) - pair_first.minimum_deletions,
            )

    def test_minimum_repair_is_exact_vertex_cover_oracle(self):
        # Conflict path 0--1--2.  Removing 1 alone restores pairwise/global
        # intersection, while removing 0 or 2 alone leaves one conflict edge.
        boxes = (
            LabeledIntegerBox(0, (0,), (1,)),
            LabeledIntegerBox(1, (3,), (4,)),
            LabeledIntegerBox(2, (0,), (1,)),
        )
        repair = minimum_common_target_deletion_sets(boxes)
        target_first = target_first_common_target_repair(boxes)
        self.assertEqual(repair.conflict_edges, ((0, 1), (1, 2)))
        self.assertEqual(repair.minimum_deletions, 1)
        self.assertEqual(repair.minimum_deletion_sets, (frozenset({1}),))
        self.assertEqual(target_first.maximum_occupancy, 2)
        self.assertEqual(target_first.minimum_deletion_sets, (frozenset({1}),))
        self.assertTrue(common_target_exists_after_deletions(boxes, (1,)))

    def test_current_existence_bit_is_not_future_deletion_sufficient(self):
        one_edge = (
            LabeledIntegerBox(0, (0,), (1,)),
            LabeledIntegerBox(1, (3,), (4,)),
            LabeledIntegerBox(2, (0,), (4,)),
        )
        path = (
            LabeledIntegerBox(0, (0,), (1,)),
            LabeledIntegerBox(1, (3,), (4,)),
            LabeledIntegerBox(2, (0,), (1,)),
        )
        self.assertIsNone(intersect_boxes(one_edge))
        self.assertIsNone(intersect_boxes(path))
        # Both are currently false, but deleting box 0 distinguishes them.
        self.assertTrue(common_target_exists_after_deletions(one_edge, (0,)))
        self.assertFalse(common_target_exists_after_deletions(path, (0,)))

    def test_nonempty_current_family_needs_no_extra_state_for_deletion_only_existence(self):
        boxes = (
            LabeledIntegerBox(0, (0, 0), (3, 3)),
            LabeledIntegerBox(1, (1, 1), (4, 4)),
            LabeledIntegerBox(2, (2, 0), (5, 2)),
        )
        self.assertEqual(box_conflict_edges(boxes), ())
        labels = [box.label for box in boxes]
        for count in range(len(labels)):
            for removed in combinations(labels, count):
                self.assertTrue(common_target_exists_after_deletions(boxes, removed))
        repair = minimum_common_target_deletion_sets(boxes)
        target_first = target_first_common_target_repair(boxes)
        self.assertEqual(repair.minimum_deletions, 0)
        self.assertEqual(repair.minimum_deletion_sets, (frozenset(),))
        self.assertEqual(target_first.maximum_occupancy, len(boxes))
        self.assertEqual(target_first.minimum_deletions, 0)

    def test_conflict_graph_is_not_enough_for_future_bounds(self):
        first = (
            LabeledIntegerBox(0, (0,), (5,)),
            LabeledIntegerBox(1, (2,), (7,)),
        )
        second = (
            LabeledIntegerBox(0, (10,), (15,)),
            LabeledIntegerBox(1, (12,), (17,)),
        )
        self.assertEqual(box_conflict_edges(first), box_conflict_edges(second))
        self.assertEqual(box_conflict_edges(first), ())
        self.assertNotEqual(intersect_boxes(first).lows, intersect_boxes(second).lows)
        self.assertNotEqual(intersect_boxes(first).highs, intersect_boxes(second).highs)

    def test_bounded_families_match_pair_and_target_repair_sets(self):
        library = (
            LabeledIntegerBox(0, (-3, -2), (0, 1)),
            LabeledIntegerBox(1, (-1, -1), (2, 2)),
            LabeledIntegerBox(2, (1, -2), (4, 0)),
            LabeledIntegerBox(3, (3, 0), (5, 3)),
            LabeledIntegerBox(4, (0, 2), (3, 5)),
            LabeledIntegerBox(5, (-4, 1), (-1, 4)),
        )
        for count in range(2, len(library) + 1):
            for indices in combinations(range(len(library)), count):
                boxes = tuple(library[index] for index in indices)
                pair_first = minimum_common_target_deletion_sets(boxes)
                target_first = target_first_common_target_repair(boxes)
                self.assertEqual(
                    target_first.minimum_deletions,
                    pair_first.minimum_deletions,
                    boxes,
                )
                self.assertEqual(
                    set(target_first.minimum_deletion_sets),
                    set(pair_first.minimum_deletion_sets),
                    boxes,
                )

    def test_invalid_removal_is_rejected(self):
        boxes = (
            LabeledIntegerBox(0, (0,), (1,)),
            LabeledIntegerBox(1, (2,), (3,)),
        )
        with self.assertRaises(ValueError):
            common_target_exists_after_deletions(boxes, (0, 1))
        with self.assertRaises(ValueError):
            common_target_exists_after_deletions(boxes, (99,))


if __name__ == "__main__":
    unittest.main()
