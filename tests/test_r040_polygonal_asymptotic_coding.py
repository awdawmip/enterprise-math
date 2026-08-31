import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / "experiments" / "r040_polygonal_asymptotic_coding.py"
spec = importlib.util.spec_from_file_location("r040", MOD)
r040 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = r040
spec.loader.exec_module(r040)


class R040ExactTests(unittest.TestCase):
    def test_discriminant_inverse_against_holdout(self):
        for s in range(3, 11):
            for x in list(range(0, 200)) + [999, 10_000, 123_456]:
                self.assertEqual(r040.lower_index(s, x), r040.lower_index_holdout(s, x), (s, x))

    def test_endpoint_against_independent_holdout(self):
        for s in range(3, 10):
            for r in range(1, 18):
                for k in range(0, 120):
                    x = r * r040.polygonal(s, k)
                    self.assertEqual(r040.endpoint_children_value(s, x), r040.endpoint_children_holdout(s, x), (s, r, k))

    def test_r4_frozen_formulas(self):
        for k in range(1, 100):
            self.assertEqual(r040.endpoint_children(3, 4, k), (2*k, 2*k+1))
            self.assertEqual(r040.endpoint_children(4, 4, k), (2*k,))
            for s in range(5, 10):
                self.assertEqual(r040.endpoint_children(s, 4, k), (2*k-1, 2*k))

    def test_square_affine_offset_and_threshold(self):
        for s in [3, 5, 6, 7, 8, 10]:
            for q in [2, 3, 4, 5, 7]:
                K = r040.square_stable_threshold(s, q)
                d = r040.square_affine_offset(s, q)
                for k in range(K, K + 500):
                    self.assertEqual(r040.endpoint_children(s, q*q, k), (q*k+d, q*k+d+1), (s, q, K, d, k))
                if K > 1:
                    self.assertNotEqual(r040.endpoint_children(s, q*q, K-1), (q*(K-1)+d, q*(K-1)+d+1))

    def test_square_digit_formula_in_stable_region(self):
        for s, q in [(3, 3), (5, 3), (6, 4), (8, 5)]:
            K = r040.square_forward_invariant_threshold(s, q)
            k0 = K + 3
            layers = r040.iterate_support(s, q*q, [k0], 6)
            for t in range(0, 7):
                self.assertEqual(layers[t], r040.square_support_formula(s, q, k0, t), (s, q, t))

    def test_nonsquare_pell_strip_equivalence_after_stable_drop(self):
        cases = [(3, 10), (3, 11), (7, 6), (8, 8), (6, 11), (5, 7)]
        for s, r in cases:
            p = r040.Params(s, r)
            self.assertIsNone(p.square_q)
            for k in range(100, 20_000):
                h = r040.curvature_drop(s, r, k)
                self.assertIn(h, (0, 1), (s, r, k, h))
                N = r040.baseline_pell_norm(s, r, k)
                self.assertEqual(h == 1, 0 < N < p.B, (s, r, k, h, N, p.B))
                if r040.exact_hit(s, r, k):
                    self.assertEqual(N, p.B, (s, r, k, N, p.B))

    def test_pell_strip_endpoint_trichotomy(self):
        from math import isqrt
        for s in range(3, 10):
            if s == 4:
                continue
            for r in range(2, 20):
                if isqrt(r) ** 2 == r:
                    continue
                p = r040.Params(s, r)
                K = r040.curvature_drop_sufficient_threshold(s, r)
                for k in range(K, K + 1000):
                    G = r040.baseline_linear_floor(s, r, k)
                    N = r040.baseline_pell_norm(s, r, k)
                    ch = r040.endpoint_children(s, r, k)
                    if N < p.B:
                        self.assertEqual(ch, (G - 1, G), (s, r, k, N, p.B))
                    elif N == p.B:
                        self.assertEqual(ch, (G,), (s, r, k, N, p.B))
                    else:
                        self.assertEqual(ch, (G, G + 1), (s, r, k, N, p.B))

    def test_two_axis_coupling_witness_r10(self):
        self.assertEqual(r040.curvature_drop_sufficient_threshold(5, 10), 1)
        self.assertEqual(r040.baseline_pell_norm(3, 10, 18), 1)
        self.assertEqual(r040.endpoint_children(3, 10, 18), (57, 58))
        for k in range(1, 20_000):
            self.assertEqual(r040.curvature_drop(5, 10, k), 0)

    def test_principal_convergent_boundary_witness(self):
        sample = r040.defect_rational_sample(9, 10, 11)
        self.assertEqual(sample["N"], 169)
        self.assertEqual(sample["reduced_y_over_z"], [471, 149])
        self.assertFalse(sample["principal_convergent_within_checked_prefix"])

    def test_lower_jump_drop_identity(self):
        for s, r in [(3, 10), (3, 11), (7, 6), (8, 8)]:
            for k in range(100, 20_000):
                lhs = r040.lower_jump(s, r, k)
                rhs = r040.baseline_jump(s, r, k) + r040.curvature_drop(s, r, k) - r040.curvature_drop(s, r, k+1)
                self.assertEqual(lhs, rhs)

    def test_cardinality_loss_identity(self):
        for s in [3, 4, 5, 7]:
            for r in [2, 3, 4, 5, 9, 10]:
                layers = r040.iterate_support(s, r, [1], 5)
                for S in layers:
                    d = r040.cardinality_loss(s, r, S)
                    self.assertEqual(d["next_support"], d["identity_rhs"])

    def test_curvature_drop_threshold_and_strip_exhaustive_small_domain(self):
        from math import isqrt
        for s in range(3, 11):
            for r in range(2, 25):
                if isqrt(r) ** 2 == r or s == 4:
                    continue
                K = r040.curvature_drop_sufficient_threshold(s, r)
                p = r040.Params(s, r)
                for k in range(K, K + 3000):
                    h = r040.curvature_drop(s, r, k)
                    self.assertIn(h, (0, 1), (s, r, K, k, h))
                    N = r040.baseline_pell_norm(s, r, k)
                    self.assertEqual(h == 1, 0 < N < p.B, (s, r, K, k, h, N, p.B))
                    if r040.exact_hit(s, r, k):
                        self.assertEqual(N, p.B)

    def test_exact_sturmian_balance_counterexample(self):
        w = r040.sturmian_balance_witness(8, 8, start=1, length=200, max_factor_len=20)
        self.assertIsNotNone(w)
        self.assertEqual(w["kind"], "sturmian_balance_violation")
        self.assertEqual(w["factor_length"], 6)
        self.assertEqual({w["low_factor"], w["high_factor"]}, {"011110", "111111"})

    def test_s4_degeneracy(self):
        for q in [2, 3, 4, 5]:
            for k in range(1, 100):
                self.assertEqual(r040.endpoint_children(4, q*q, k), (q*k,))
        for r in [2, 3, 5, 6, 7, 8, 10]:
            for k in range(1, 100):
                self.assertEqual(r040.curvature_drop(4, r, k), 0)
                self.assertFalse(r040.exact_hit(4, r, k))


if __name__ == "__main__":
    unittest.main()
