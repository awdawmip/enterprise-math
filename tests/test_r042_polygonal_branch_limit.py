import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).resolve().parents[1] / "tools" / "r042_polygonal_branch_limit.py"
spec = importlib.util.spec_from_file_location("r042", MODULE)
r042 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r042
spec.loader.exec_module(r042)


class R042ExactOracleTests(unittest.TestCase):
    def test_r040_coupling_witness(self):
        got = r042.exact_children(3, 10, 18)
        self.assertFalse(got.exact_hit)
        self.assertEqual(got.children, (57, 58))
        self.assertEqual(r042.pell_strip_norm(3, 10, 18), 1)
        self.assertEqual(r042.pell_strip_class(3, 10, 18), "INTERIOR_DEFECT")

    def test_nonconsecutive_hit_revisit_witnesses(self):
        cases = [
            (6, 11, 2, 65, [2, 6, 20, 65]),
            (6, 15, 1, 10, [1, 3, 10]),
            (7, 7, 1, 29540, [1, 2, 5, 13, 33, 86, 228, 603, 1595, 4220, 11165, 29540]),
            (8, 14, 4, 190, [4, 14, 51, 190]),
        ]
        for s, r, h0, h1, path in cases:
            self.assertTrue(r042.is_exact_hit(s, r, h0))
            self.assertTrue(r042.is_exact_hit(s, r, h1))
            self.assertEqual(r042.backward_path(s, r, h1, h0), path)
            self.assertTrue(any(not r042.is_exact_hit(s, r, k) for k in path[1:-1]))
            for u, v in zip(path, path[1:]):
                self.assertIn(v, r042.exact_children(s, r, u).children)

    def test_predecessor_unique_on_representative_ranges(self):
        for s, r in [(3, 5), (3, 10), (5, 10), (6, 11), (7, 7), (8, 14), (9, 10)]:
            levels = r042.support_levels(s, r, [1], 7)
            for lev in levels[1:]:
                for child in lev:
                    self.assertIsNotNone(r042.predecessor(s, r, child))

    def test_rational_cylinder_enclosures_shrink(self):
        s, r = 6, 11
        path = [2, 6, 20, 65]
        widths = []
        for t, k in enumerate(path):
            lo, hi = r042.cylinder_enclosure(s, r, t, k, decimal_digits=30)
            self.assertLess(lo, hi)
            widths.append(hi - lo)
        self.assertLess(widths[-1], widths[0])

    def test_support_binary_prefactor_is_positive_in_checked_prefix(self):
        for s, r, root in [(3, 5, 1), (5, 10, 1), (6, 11, 2), (6, 15, 1), (8, 14, 4)]:
            levels = r042.support_levels(s, r, [root], 12)
            ratios = [len(lev) / (2 ** t) for t, lev in enumerate(levels)]
            self.assertGreater(min(ratios), 0.0)
            self.assertLessEqual(ratios[-1], ratios[0])

    def test_bounded_scan_has_no_three_hit_ancestry_in_holdout(self):
        atlas = r042.bounded_recurrence_scan(range(3, 10), range(5, 17), 50_000)
        self.assertLessEqual(atlas["max_hits_on_one_checked_ancestry"], 2)
        witnesses = [
            w
            for cell in atlas["cells"]
            for w in cell["nonconsecutive_revisit_witnesses"]
        ]
        self.assertTrue(any(w["ancestor_hit"] == 1 and w["descendant_hit"] == 10 for w in witnesses))


if __name__ == "__main__":
    unittest.main()
