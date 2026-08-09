import unittest
from itertools import combinations, product

from enterprise_math.extremum_future_signature import (
    compile_extremum_future_signature,
    extremum_after_deletions,
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

    def test_invalid_horizon_or_deletions_are_rejected(self):
        values = {0: 3, 1: 2}
        with self.assertRaises(ValueError):
            compile_extremum_future_signature(values, 2)
        signature = compile_extremum_future_signature(values, 1)
        with self.assertRaises(ValueError):
            extremum_after_deletions(signature, (0, 1))
        with self.assertRaises(ValueError):
            extremum_after_deletions(signature, (99,))


if __name__ == "__main__":
    unittest.main()
