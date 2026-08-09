import unittest
from itertools import combinations, product

from enterprise_math.box_collapse import LabeledIntegerBox
from enterprise_math.box_future_signature import (
    box_bounds_after_deletions,
    box_intersection_exists_after_deletions,
    compile_box_deletion_future_signature,
)


def direct_bounds(boxes, removed):
    remaining = [box for box in boxes if box.label not in removed]
    dimension = remaining[0].dimension
    lows = tuple(max(box.lows[axis] for box in remaining) for axis in range(dimension))
    highs = tuple(min(box.highs[axis] for box in remaining) for axis in range(dimension))
    return lows, highs


def full_bounds_future_signature(boxes, horizon):
    labels = tuple(sorted(box.label for box in boxes))
    return tuple(
        (removed, direct_bounds(boxes, frozenset(removed)))
        for count in range(horizon + 1)
        for removed in combinations(labels, count)
    )


class BoxFutureSignatureTests(unittest.TestCase):
    def test_componentwise_compact_signature_recovers_every_allowed_future_box(self):
        boxes = (
            LabeledIntegerBox(0, (-9, -5), (1, 5)),
            LabeledIntegerBox(1, (-5, -4), (3, 7)),
            LabeledIntegerBox(2, (-2, -7), (6, 4)),
            LabeledIntegerBox(3, (0, -2), (7, 9)),
            LabeledIntegerBox(4, (2, -1), (10, 10)),
            LabeledIntegerBox(5, (-4, -9), (8, 2)),
        )
        labels = [box.label for box in boxes]
        for horizon in range(4):
            signature = compile_box_deletion_future_signature(boxes, horizon)
            for count in range(horizon + 1):
                for removed in combinations(labels, count):
                    expected = direct_bounds(boxes, frozenset(removed))
                    self.assertEqual(
                        box_bounds_after_deletions(signature, removed),
                        expected,
                    )
                    lows, highs = expected
                    self.assertEqual(
                        box_intersection_exists_after_deletions(signature, removed),
                        all(lo <= hi for lo, hi in zip(lows, highs, strict=True)),
                    )

    def test_compiled_box_signature_partition_equals_complete_bounds_future_partition(self):
        # Exhaustively compare extensional quotient classes for three fixed
        # labels over a small 1D interval catalog.  This checks coarseness, not
        # merely reconstruction: compact signatures and complete future output
        # functions induce exactly the same partition of concrete box states.
        interval_shapes = ((0, 0), (0, 1), (1, 1), (1, 2))
        labels = (0, 1, 2)
        families = tuple(
            tuple(
                LabeledIntegerBox(label, (lo,), (hi,))
                for label, (lo, hi) in zip(labels, shapes, strict=True)
            )
            for shapes in product(interval_shapes, repeat=len(labels))
        )
        for horizon in range(len(labels)):
            compact_to_full = {}
            full_to_compact = {}
            for boxes in families:
                compact = compile_box_deletion_future_signature(boxes, horizon)
                full = full_bounds_future_signature(boxes, horizon)
                compact_to_full.setdefault(compact, set()).add(full)
                full_to_compact.setdefault(full, set()).add(compact)
            self.assertTrue(
                all(len(outputs) == 1 for outputs in compact_to_full.values())
            )
            self.assertTrue(
                all(len(signatures) == 1 for signatures in full_to_compact.values())
            )

    def test_ties_can_make_signature_smaller_than_uniform_h_plus_one_labels(self):
        boxes = (
            LabeledIntegerBox(0, (5, 0), (20, 10)),
            LabeledIntegerBox(1, (5, 0), (20, 10)),
            LabeledIntegerBox(2, (5, 0), (20, 10)),
            LabeledIntegerBox(3, (1, -5), (20, 15)),
            LabeledIntegerBox(4, (0, -6), (20, 16)),
        )
        signature = compile_box_deletion_future_signature(boxes, 2)
        # x-low has three tied maxima, so no x-low label is needed: value 5 is
        # already an undeletable guard under horizon 2.
        x_low = signature.lower_signatures[0]
        self.assertEqual(x_low.exposed_levels, ())
        self.assertEqual(x_low.guard_value, 5)
        for removed in combinations([0, 1, 2, 3, 4], 2):
            self.assertEqual(
                box_bounds_after_deletions(signature, removed),
                direct_bounds(boxes, frozenset(removed)),
            )

    def test_empty_to_nonempty_transition_under_deletion_is_detected(self):
        boxes = (
            LabeledIntegerBox(0, (3,), (5,)),
            LabeledIntegerBox(1, (0,), (1,)),
            LabeledIntegerBox(2, (0,), (10,)),
        )
        signature = compile_box_deletion_future_signature(boxes, 1)
        self.assertFalse(box_intersection_exists_after_deletions(signature, ()))
        self.assertTrue(box_intersection_exists_after_deletions(signature, (0,)))
        self.assertTrue(box_intersection_exists_after_deletions(signature, (1,)))

    def test_invalid_deletions_are_rejected(self):
        boxes = (
            LabeledIntegerBox(0, (0,), (2,)),
            LabeledIntegerBox(1, (1,), (3,)),
        )
        signature = compile_box_deletion_future_signature(boxes, 1)
        with self.assertRaises(ValueError):
            box_bounds_after_deletions(signature, (0, 1))
        with self.assertRaises(ValueError):
            box_bounds_after_deletions(signature, (99,))


if __name__ == "__main__":
    unittest.main()
