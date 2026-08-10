import unittest

from enterprise_math.precision_typed_relation_compiler import (
    coarsest_relation_stable_refinement,
    common_refinement,
    count_channel,
    label_set_channel,
    may_channel,
    partition_refines,
    relation_partition_is_stable,
    stabilized_common_refinement,
)


class PrecisionTypedRelationCompilerTests(unittest.TestCase):
    def test_may_count_label_semantics_form_partial_information_order(self):
        states = ("x", "y", "z", "a", "b")
        initial = (states,)
        witnesses = (
            ("x", "a", "p"),
            ("x", "b", "q"),
            ("y", "a", "p"),
            ("y", "b", "p"),
            ("z", "a", "p"),
        )
        may = may_channel("may", ((source, target) for source, target, _ in witnesses))
        count = count_channel("count", witnesses)
        labels = label_set_channel("labels", witnesses)

        may_partition = coarsest_relation_stable_refinement(
            states, initial, (may,)
        ).partition
        count_partition = coarsest_relation_stable_refinement(
            states, initial, (count,)
        ).partition
        label_partition = coarsest_relation_stable_refinement(
            states, initial, (labels,)
        ).partition
        joint_partition = coarsest_relation_stable_refinement(
            states, initial, (count, labels)
        ).partition

        self.assertEqual(may_partition, (("x", "y", "z"), ("a", "b")))
        self.assertEqual(count_partition, (("x", "y"), ("z",), ("a", "b")))
        self.assertEqual(label_partition, (("x",), ("y", "z"), ("a", "b")))
        self.assertEqual(
            joint_partition, (("x",), ("y",), ("z",), ("a", "b"))
        )
        self.assertTrue(partition_refines(states, count_partition, may_partition))
        self.assertTrue(partition_refines(states, label_partition, may_partition))
        self.assertFalse(partition_refines(states, count_partition, label_partition))
        self.assertFalse(partition_refines(states, label_partition, count_partition))
        self.assertEqual(len(count_partition), len(label_partition))

    def test_cross_channel_activation_cascade_needs_second_repair_round(self):
        states = (0, 1, 2)
        initial = (states,)
        channel_a = count_channel("A", ((0, 1, "a"),))
        channel_b = count_channel(
            "B", ((0, 1, "b0"), (1, 2, "b1"), (2, 0, "b2"))
        )

        only_a = coarsest_relation_stable_refinement(
            states, initial, (channel_a,)
        ).partition
        only_b = coarsest_relation_stable_refinement(
            states, initial, (channel_b,)
        ).partition
        raw = common_refinement(states, (only_a, only_b))
        joint = coarsest_relation_stable_refinement(
            states, initial, (channel_a, channel_b)
        )

        self.assertEqual(only_a, ((0,), (1, 2)))
        self.assertEqual(only_b, ((0, 1, 2),))
        self.assertEqual(raw, ((0,), (1, 2)))
        self.assertFalse(
            relation_partition_is_stable(states, raw, (channel_a, channel_b))
        )
        self.assertEqual(joint.partition, ((0,), (1,), (2,)))
        self.assertEqual(joint.class_counts, (1, 2, 3))
        self.assertEqual(joint.strict_rounds, 2)

    def test_same_channel_raw_common_refinement_can_be_unstable(self):
        states = (0, 1, 2, 3, 4)
        edges = (
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 1),
            (4, 0),
            (4, 1),
        )
        channel = count_channel(
            "count",
            tuple((source, target, index) for index, (source, target) in enumerate(edges)),
        )
        left = ((0, 2, 4), (1, 3))
        right = ((0, 3, 4), (1, 2))
        raw = common_refinement(states, (left, right))

        self.assertTrue(relation_partition_is_stable(states, left, (channel,)))
        self.assertTrue(relation_partition_is_stable(states, right, (channel,)))
        self.assertEqual(raw, ((0, 4), (1,), (2,), (3,)))
        self.assertFalse(relation_partition_is_stable(states, raw, (channel,)))

        repaired = stabilized_common_refinement(
            states, (left, right), (channel,)
        )
        self.assertEqual(repaired.partition, ((0,), (1,), (2,), (3,), (4,)))
        self.assertEqual(repaired.class_counts, (4, 5))

    def test_strict_round_count_is_bounded_by_available_splits(self):
        states = (0, 1, 2)
        initial = (states,)
        channel_a = count_channel("A", ((0, 1, "a"),))
        channel_b = count_channel(
            "B", ((0, 1, "b0"), (1, 2, "b1"), (2, 0, "b2"))
        )
        result = coarsest_relation_stable_refinement(
            states, initial, (channel_a, channel_b)
        )
        self.assertLessEqual(result.strict_rounds, len(states) - len(initial))

    def test_invalid_partition_and_empty_channel_language_fail_closed(self):
        states = (0, 1)
        channel = may_channel("may", ((0, 1),))
        with self.assertRaises(ValueError):
            coarsest_relation_stable_refinement(states, ((0,),), (channel,))
        with self.assertRaises(ValueError):
            coarsest_relation_stable_refinement(states, (states,), ())


if __name__ == "__main__":
    unittest.main()
