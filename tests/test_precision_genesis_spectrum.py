import unittest
from itertools import product

from enterprise_math.precision_genesis_spectrum import (
    collision_growth_decomposition,
    collision_growth_is_strict,
    merge_growth_decomposition,
    merge_growth_is_strict,
)


class PrecisionGenesisSpectrumTests(unittest.TestCase):
    def test_branch_copy_only(self):
        n = {0: 2}
        relation = frozenset({(0, "a"), (0, "b")})
        report = collision_growth_decomposition(n, relation, 2)
        self.assertEqual(
            (report.total_growth, report.branch_copy_growth, report.cross_source_growth),
            (1, 1, 0),
        )
        merge = merge_growth_decomposition(n, relation)
        self.assertEqual(
            (merge.total_growth, merge.branch_copy_growth, merge.cross_source_growth),
            (1, 1, 0),
        )

    def test_cross_source_only(self):
        n = {0: 1, 1: 1}
        relation = frozenset({(0, "a"), (1, "a")})
        report = collision_growth_decomposition(n, relation, 2)
        self.assertEqual(
            (report.total_growth, report.branch_copy_growth, report.cross_source_growth),
            (1, 0, 1),
        )
        merge = merge_growth_decomposition(n, relation)
        self.assertEqual(
            (merge.total_growth, merge.branch_copy_growth, merge.cross_source_growth),
            (1, 0, 1),
        )

    def test_mixed_growth(self):
        n = {0: 2, 1: 1}
        relation = frozenset({(0, "a"), (0, "b"), (1, "b")})
        report = collision_growth_decomposition(n, relation, 2)
        self.assertEqual(
            (report.total_growth, report.branch_copy_growth, report.cross_source_growth),
            (3, 1, 2),
        )
        merge = merge_growth_decomposition(n, relation)
        self.assertEqual(
            (merge.total_growth, merge.branch_copy_growth, merge.cross_source_growth),
            (2, 1, 1),
        )

    def test_exact_equality_when_neither_mechanism_is_present(self):
        n = {0: 2, 1: 1}
        relation = frozenset({(0, "a"), (1, "b")})
        self.assertFalse(collision_growth_is_strict(n, relation, 2))
        self.assertFalse(merge_growth_is_strict(n, relation))

    def test_exhaustive_small_exact_decomposition(self):
        targets = (0, 1, 2)
        supports = [
            frozenset(
                target
                for index, target in enumerate(targets)
                if mask & (1 << index)
            )
            for mask in range(1, 8)
        ]
        checked = 0
        for left, right in product(supports, repeat=2):
            relation = frozenset(
                [(0, target) for target in left]
                + [(1, target) for target in right]
            )
            for n0, n1 in product(range(4), repeat=2):
                if n0 == n1 == 0:
                    continue
                n = {0: n0, 1: n1}
                for order in (1, 2, 3, 4):
                    report = collision_growth_decomposition(n, relation, order)
                    self.assertGreaterEqual(report.branch_copy_growth, 0)
                    self.assertGreaterEqual(report.cross_source_growth, 0)
                    self.assertEqual(
                        report.total_growth,
                        report.branch_copy_growth + report.cross_source_growth,
                    )
                merge = merge_growth_decomposition(n, relation)
                self.assertGreaterEqual(merge.branch_copy_growth, 0)
                self.assertGreaterEqual(merge.cross_source_growth, 0)
                self.assertEqual(
                    merge.total_growth,
                    merge.branch_copy_growth + merge.cross_source_growth,
                )
                checked += 1
        self.assertEqual(checked, 735)


if __name__ == "__main__":
    unittest.main()
