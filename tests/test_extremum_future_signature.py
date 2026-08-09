import unittest
from itertools import combinations, product

from enterprise_math.extremum_future_signature import (
    compile_extremum_future_signature,
    delete_extremum_label,
    extremum_after_deletions,
    insert_extremum_value,
    worst_case_labeled_candidate_count,
)


def direct_extremum(values, removed, maximize):
    remaining = [value for label, value in values.items() if label not in removed]
    return max(remaining) if maximize else min(remaining)


def full_future_signature(values, horizon, maximize):
    labels = tuple(sorted(values))
    return tuple(
        (removed, direct_extremum(values, frozenset(removed), maximize))
        for count in range(horizon + 1)
        for removed in combinations(labels, count)
    )


class ExtremumFutureSignatureTests(unittest.TestCase):
    def test_compact_signature_evaluates_every_allowed_deletion_exactly(self):
        values = {0: 9, 1: 9, 2: 7, 3: 4, 4: 1}
        for horizon in range(5):
            for maximize in (True, False):
                signature = compile_extremum_future_signature(
                    values, horizon, maximize
                )
                for count in range(horizon + 1):
                    for removed in combinations(values, count):
                        self.assertEqual(
                            extremum_after_deletions(signature, removed),
                            direct_extremum(values, frozenset(removed), maximize),
                        )

    def test_large_top_tie_needs_only_guard_value_for_max_future(self):
        values = {0: 10, 1: 10, 2: 10, 3: 5, 4: 1}
        signature = compile_extremum_future_signature(values, 2, maximize=True)
        self.assertEqual(signature.exposed_levels, ())
        self.assertEqual(signature.guard_value, 10)
        for removed in combinations(values, 2):
            self.assertEqual(extremum_after_deletions(signature, removed), 10)

    def test_strict_order_retains_h_exposed_labels_plus_unlabeled_guard_value(self):
        values = {0: 50, 1: 40, 2: 30, 3: 20, 4: 10}
        signature = compile_extremum_future_signature(values, 2, maximize=True)
        self.assertEqual(
            tuple((level.value, level.labels) for level in signature.exposed_levels),
            ((50, (0,)), (40, (1,))),
        )
        self.assertEqual(signature.guard_value, 30)
        self.assertEqual(
            sum(len(level.labels) for level in signature.exposed_levels),
            worst_case_labeled_candidate_count(2),
        )
        self.assertEqual(extremum_after_deletions(signature, (0, 1)), 30)

    def test_minimum_future_uses_the_same_level_logic_in_reverse_order(self):
        values = {0: -5, 1: -5, 2: 0, 3: 4, 4: 9}
        signature = compile_extremum_future_signature(values, 2, maximize=False)
        self.assertEqual(
            tuple((level.value, level.labels) for level in signature.exposed_levels),
            ((-5, (0, 1)),),
        )
        self.assertEqual(signature.guard_value, 0)
        self.assertEqual(extremum_after_deletions(signature, (0,)), -5)
        self.assertEqual(extremum_after_deletions(signature, (0, 1)), 0)

    def test_compact_signature_partition_equals_complete_future_partition_on_small_domains(self):
        # This regression checks both sufficiency and coarseness by comparing
        # equivalence classes induced by compact vs complete deletion futures.
        for label_count in range(2, 6):
            labels = tuple(range(label_count))
            for horizon in range(label_count):
                for maximize in (True, False):
                    compact_to_full = {}
                    full_to_compact = {}
                    for assignment in product(range(4), repeat=label_count):
                        values = dict(zip(labels, assignment, strict=True))
                        compact = compile_extremum_future_signature(
                            values, horizon, maximize
                        )
                        full = full_future_signature(values, horizon, maximize)
                        compact_to_full.setdefault(compact, set()).add(full)
                        full_to_compact.setdefault(full, set()).add(compact)
                    self.assertTrue(
                        all(len(outputs) == 1 for outputs in compact_to_full.values())
                    )
                    self.assertTrue(
                        all(len(signatures) == 1 for signatures in full_to_compact.values())
                    )

    def test_online_insertion_matches_fresh_recompile_on_small_domains(self):
        labels = (0, 1, 2)
        new_label = 3
        for assignment in product(range(4), repeat=len(labels)):
            values = dict(zip(labels, assignment, strict=True))
            for horizon in range(len(labels)):
                for maximize in (True, False):
                    signature = compile_extremum_future_signature(
                        values, horizon, maximize
                    )
                    for new_value in range(4):
                        updated = insert_extremum_value(
                            signature, new_label, new_value
                        )
                        expected_values = dict(values)
                        expected_values[new_label] = new_value
                        expected = compile_extremum_future_signature(
                            expected_values, horizon, maximize
                        )
                        self.assertEqual(updated, expected)

    def test_online_deletion_matches_fresh_recompile_on_small_domains(self):
        for label_count in range(2, 6):
            labels = tuple(range(label_count))
            for assignment in product(range(4), repeat=label_count):
                values = dict(zip(labels, assignment, strict=True))
                for horizon in range(1, label_count):
                    for maximize in (True, False):
                        signature = compile_extremum_future_signature(
                            values, horizon, maximize
                        )
                        for deleted in labels:
                            updated = delete_extremum_label(signature, deleted)
                            expected_values = {
                                label: value
                                for label, value in values.items()
                                if label != deleted
                            }
                            expected = compile_extremum_future_signature(
                                expected_values, horizon - 1, maximize
                            )
                            self.assertEqual(updated, expected)

    def test_hidden_or_guard_deletion_never_requires_recovering_lower_values(self):
        # h=1 exposes top=50 and has guard=40.  Deleting the unique guard label
        # makes the surviving known top level the new guard at horizon zero.
        values = {0: 50, 1: 40, 2: 30, 3: 20}
        signature = compile_extremum_future_signature(values, 1, maximize=True)
        self.assertEqual(signature.guard_value, 40)
        updated = delete_extremum_label(signature, 1)
        expected = compile_extremum_future_signature(
            {0: 50, 2: 30, 3: 20}, 0, maximize=True
        )
        self.assertEqual(updated, expected)
        self.assertEqual(updated.guard_value, 50)

    def test_insert_then_delete_sequence_matches_full_state_recompile(self):
        values = {0: 7, 1: 7, 2: 3, 3: 1}
        signature = compile_extremum_future_signature(values, 2, maximize=True)
        signature = insert_extremum_value(signature, 4, 9)
        values[4] = 9
        self.assertEqual(
            signature,
            compile_extremum_future_signature(values, 2, maximize=True),
        )
        signature = delete_extremum_label(signature, 0)
        del values[0]
        self.assertEqual(
            signature,
            compile_extremum_future_signature(values, 1, maximize=True),
        )
        signature = insert_extremum_value(signature, 5, 2)
        values[5] = 2
        self.assertEqual(
            signature,
            compile_extremum_future_signature(values, 1, maximize=True),
        )

    def test_invalid_horizon_or_updates_are_rejected(self):
        values = {0: 3, 1: 2}
        with self.assertRaises(ValueError):
            compile_extremum_future_signature(values, 2)
        signature = compile_extremum_future_signature(values, 1)
        with self.assertRaises(ValueError):
            extremum_after_deletions(signature, (0, 1))
        with self.assertRaises(ValueError):
            extremum_after_deletions(signature, (99,))
        with self.assertRaises(ValueError):
            insert_extremum_value(signature, 0, 9)
        with self.assertRaises(ValueError):
            delete_extremum_label(signature, 99)
        no_budget = compile_extremum_future_signature(values, 0)
        with self.assertRaises(ValueError):
            delete_extremum_label(no_budget, 0)


if __name__ == "__main__":
    unittest.main()
