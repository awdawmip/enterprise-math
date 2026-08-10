import unittest

from enterprise_math.stage131_horn_resource_surface import (
    and_tree_resource_frontier,
    and_tree_resource_point,
    and_tree_resource_table,
    root_frontier_is_inclusion_minimal_premise,
    root_frontier_premise_widths,
    root_frontier_premises,
)
from enterprise_math.stage131_horn_hyperedge_presentation import (
    balanced_binary_and_tree,
)


class Stage131HornResourceSurfaceTests(unittest.TestCase):
    def test_every_level_frontier_is_an_inclusion_minimal_root_premise(self):
        for height in range(1, 7):
            tree = balanced_binary_and_tree(height)
            for gap in range(1, height + 1):
                self.assertTrue(root_frontier_is_inclusion_minimal_premise(tree, gap))
                self.assertEqual(len(root_frontier_premises(tree, gap)), 1 << gap)
            self.assertEqual(
                root_frontier_premise_widths(height),
                tuple(1 << gap for gap in range(1, height + 1)),
            )

    def test_height_eight_resource_points(self):
        expected = {
            1: (255, 510, 2, 8, 8, 0, 0),
            2: (382, 1018, 4, 4, 4, 127, 508),
            3: (318, 1014, 8, 4, 4, 63, 504),
            4: (286, 1006, 16, 2, 3, 31, 496),
            8: (256, 766, 256, 1, 7, 1, 256),
        }
        for span, values in expected.items():
            point = and_tree_resource_point(8, span)
            actual = (
                point.total_rule_count,
                point.total_premise_literals,
                point.maximum_premise_width,
                point.root_round,
                point.full_closure_rounds,
                point.extra_macro_rules,
                point.extra_macro_premise_literals,
            )
            self.assertEqual(actual, values)

    def test_rule_count_and_total_premise_storage_can_move_opposite_to_max_fan_in(self):
        span4 = and_tree_resource_point(8, 4)
        span8 = and_tree_resource_point(8, 8)
        self.assertLess(span8.total_rule_count, span4.total_rule_count)
        self.assertLess(span8.total_premise_literals, span4.total_premise_literals)
        self.assertGreater(span8.maximum_premise_width, span4.maximum_premise_width)
        self.assertLess(span8.root_round, span4.root_round)
        self.assertGreater(span8.full_closure_rounds, span4.full_closure_rounds)

    def test_full_resource_frontier_keeps_incomparable_readout_and_continuation_points(self):
        frontier = and_tree_resource_frontier(8)
        spans = {point.span for point in frontier}
        self.assertIn(1, spans)
        self.assertIn(4, spans)
        self.assertIn(8, spans)
        for left in frontier:
            for right in frontier:
                if left == right:
                    continue
                # By construction no point on the full five-axis frontier can
                # weakly dominate another on all stored/fan-in/depth resources.
                resources_left = (
                    left.total_rule_count,
                    left.total_premise_literals,
                    left.maximum_premise_width,
                    left.root_round,
                    left.full_closure_rounds,
                )
                resources_right = (
                    right.total_rule_count,
                    right.total_premise_literals,
                    right.maximum_premise_width,
                    right.root_round,
                    right.full_closure_rounds,
                )
                self.assertFalse(
                    all(a <= b for a, b in zip(resources_left, resources_right, strict=True))
                    and any(a < b for a, b in zip(resources_left, resources_right, strict=True))
                )

    def test_resource_table_has_one_point_per_span(self):
        for height in range(1, 10):
            table = and_tree_resource_table(height)
            self.assertEqual(tuple(point.span for point in table), tuple(range(1, height + 1)))

    def test_validation(self):
        tree = balanced_binary_and_tree(3)
        with self.assertRaises(ValueError):
            root_frontier_premises(tree, 4)
        with self.assertRaises(ValueError):
            and_tree_resource_point(4, 5)


if __name__ == "__main__":
    unittest.main()
