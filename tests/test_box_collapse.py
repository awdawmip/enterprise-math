import unittest
from itertools import combinations

from enterprise_math.box_collapse import (
    LabeledIntegerBox,
    box_helly_equivalence,
    deletion_safe_intersection_certificate,
    extremal_intersection_certificate,
    intersect_boxes,
    pairwise_intersection_clique,
    pairwise_multiplicity_signature,
    reconstruct_bounds_after_deletions,
)


class BoxCollapseTests(unittest.TestCase):
    def test_pairwise_clique_implies_whole_family_intersection(self):
        boxes = (
            LabeledIntegerBox(0, (-1, -1), (1, 1)),
            LabeledIntegerBox(1, (0, -1), (2, 1)),
            LabeledIntegerBox(2, (1, -1), (3, 1)),
        )
        self.assertTrue(pairwise_intersection_clique(boxes))
        self.assertTrue(box_helly_equivalence(boxes))
        common = intersect_boxes(boxes)
        self.assertEqual(common.lows, (1, -1))
        self.assertEqual(common.highs, (1, 1))
        self.assertEqual(common.cardinality, 3)

    def test_pairwise_multiplicity_matrix_does_not_determine_triple_multiplicity(self):
        first = (
            LabeledIntegerBox(0, (-3, -3), (-1, -1)),
            LabeledIntegerBox(1, (-3, -2), (-1, 0)),
            LabeledIntegerBox(2, (-3, -2), (1, 2)),
        )
        second = (
            LabeledIntegerBox(0, (-3, -3), (-1, -1)),
            LabeledIntegerBox(1, (-4, -2), (0, 2)),
            LabeledIntegerBox(2, (-2, -4), (2, 0)),
        )
        first_pair = tuple(value for _left, _right, value in pairwise_multiplicity_signature(first))
        second_pair = tuple(value for _left, _right, value in pairwise_multiplicity_signature(second))
        self.assertEqual(first_pair, (6, 6, 9))
        self.assertEqual(second_pair, (6, 6, 9))
        self.assertEqual(intersect_boxes(first).cardinality, 6)
        self.assertEqual(intersect_boxes(second).cardinality, 4)

    def test_2n_extremal_facets_reconstruct_exact_common_box(self):
        boxes = (
            LabeledIntegerBox(9, (-9, -5), (1, 5)),
            LabeledIntegerBox(2, (-3, -2), (5, 6)),
            LabeledIntegerBox(7, (-6, -9), (6, 3)),
            LabeledIntegerBox(5, (-3, -5), (7, 5)),
            LabeledIntegerBox(1, (-8, -6), (6, 8)),
        )
        certificate = extremal_intersection_certificate(boxes)
        common = intersect_boxes(boxes)
        self.assertEqual(certificate.common_box.lows, common.lows)
        self.assertEqual(certificate.common_box.highs, common.highs)
        self.assertEqual(len(certificate.facets), 4)
        self.assertLessEqual(len({facet.label for facet in certificate.facets}), 4)

    def test_h_plus_one_candidates_reconstruct_every_allowed_deletion(self):
        boxes = (
            LabeledIntegerBox(0, (-9, -5), (1, 5)),
            LabeledIntegerBox(1, (-5, -4), (3, 7)),
            LabeledIntegerBox(2, (-2, -7), (6, 4)),
            LabeledIntegerBox(3, (0, -2), (7, 9)),
            LabeledIntegerBox(4, (2, -1), (10, 10)),
            LabeledIntegerBox(5, (-4, -9), (8, 2)),
        )
        labels = [box.label for box in boxes]
        for horizon in range(0, 4):
            certificate = deletion_safe_intersection_certificate(boxes, horizon)
            self.assertEqual(len(certificate.candidates), 4 * (horizon + 1))
            for removed_count in range(horizon + 1):
                for removed in combinations(labels, removed_count):
                    remaining = [box for box in boxes if box.label not in removed]
                    direct_lows = tuple(
                        max(box.lows[axis] for box in remaining)
                        for axis in range(2)
                    )
                    direct_highs = tuple(
                        min(box.highs[axis] for box in remaining)
                        for axis in range(2)
                    )
                    self.assertEqual(
                        reconstruct_bounds_after_deletions(certificate, removed),
                        (direct_lows, direct_highs),
                    )

    def test_current_extrema_are_not_one_deletion_future_sufficient(self):
        first = (
            LabeledIntegerBox(0, (3, -2), (7, 2)),
            LabeledIntegerBox(1, (2, -2), (6, 2)),
            LabeledIntegerBox(2, (-6, -5), (4, 5)),
        )
        second = (
            LabeledIntegerBox(0, (3, -2), (7, 2)),
            LabeledIntegerBox(1, (1, -2), (5, 2)),
            LabeledIntegerBox(2, (-6, -5), (4, 5)),
        )
        self.assertEqual(intersect_boxes(first).lows, intersect_boxes(second).lows)
        self.assertEqual(intersect_boxes(first).highs, intersect_boxes(second).highs)
        self.assertEqual(intersect_boxes(first).lows, (3, -2))
        self.assertEqual(intersect_boxes(first).highs, (4, 2))

        first_h1 = deletion_safe_intersection_certificate(first, 1)
        second_h1 = deletion_safe_intersection_certificate(second, 1)
        self.assertEqual(
            reconstruct_bounds_after_deletions(first_h1, (0,))[0][0],
            2,
        )
        self.assertEqual(
            reconstruct_bounds_after_deletions(second_h1, (0,))[0][0],
            1,
        )

    def test_bounded_box_families_satisfy_helly_equivalence(self):
        library = []
        label = 0
        for lo_x in (-2, -1, 0):
            for lo_y in (-1, 0):
                for width in (1, 2):
                    library.append(
                        LabeledIntegerBox(
                            label,
                            (lo_x, lo_y),
                            (lo_x + width, lo_y + width),
                        )
                    )
                    label += 1
        for indices in list(combinations(range(len(library)), 3))[::11]:
            family = tuple(library[index] for index in indices)
            self.assertTrue(box_helly_equivalence(family), family)

    def test_invalid_families_are_rejected(self):
        with self.assertRaises(ValueError):
            intersect_boxes((LabeledIntegerBox(0, (0,), (1,)),))
        with self.assertRaises(ValueError):
            intersect_boxes(
                (
                    LabeledIntegerBox(0, (0,), (1,)),
                    LabeledIntegerBox(0, (0,), (2,)),
                )
            )
        with self.assertRaises(ValueError):
            deletion_safe_intersection_certificate(
                (
                    LabeledIntegerBox(0, (0,), (1,)),
                    LabeledIntegerBox(1, (0,), (2,)),
                ),
                2,
            )


if __name__ == "__main__":
    unittest.main()
