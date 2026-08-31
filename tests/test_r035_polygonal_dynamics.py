import random
import unittest
from math import isqrt

from experiments.r035_polygonal_dynamics import (
    actual_value_support,
    adjacent_parent_overlap,
    discriminant,
    endpoint_support,
    eventual_two_jump_start,
    exact_hit_pell_residual,
    exact_hit_via_discriminant,
    iterate_support,
    cardinality_components,
    has_lower_self_loop,
    is_integer_interval,
    lower_jump,
    lower_index,
    lower_map,
    one_step,
    parent_children,
    polygonal,
    polygonal_gap,
    square_case_children,
    r4_children_formula,
    support_has_internal_gap,
    universal_interval_failure_witness,
    z_coordinate,
)


class R035PolygonalDynamicsTests(unittest.TestCase):
    def test_polygonal_examples(self):
        self.assertEqual([polygonal(3, k) for k in range(6)], [0, 1, 3, 6, 10, 15])
        self.assertEqual([polygonal(4, k) for k in range(6)], [0, 1, 4, 9, 16, 25])
        self.assertEqual([polygonal(5, k) for k in range(6)], [0, 1, 5, 12, 22, 35])

    def test_gap_identity(self):
        for s in range(3, 20):
            for k in range(200):
                self.assertEqual(polygonal(s, k + 1) - polygonal(s, k), polygonal_gap(s, k))

    def test_discriminant_square_on_polygonal_values(self):
        for s in range(3, 20):
            for k in range(200):
                z = z_coordinate(s, k)
                self.assertEqual(discriminant(s, polygonal(s, k)), z * z)

    def test_lower_index_exhaustive_small(self):
        for s in range(3, 13):
            for n in range(5000):
                m = lower_index(s, n)
                self.assertLessEqual(polygonal(s, m), n)
                self.assertGreater(polygonal(s, m + 1), n)

    def test_endpoint_exact_and_between(self):
        for s in range(3, 13):
            for k in range(1, 50):
                p = polygonal(s, k)
                self.assertEqual(endpoint_support(s, p), (k,))
                if polygonal_gap(s, k) > 1:
                    self.assertEqual(endpoint_support(s, p + 1), (k, k + 1))

    def test_r1_frozen(self):
        for s in range(3, 13):
            for k in range(100):
                self.assertEqual(parent_children(s, 1, k), (k,))
                self.assertEqual(iterate_support(s, 1, k, 5), ((k,),) * 6)

    def test_square_case_formula(self):
        for r in range(1, 50):
            for k in range(100):
                self.assertEqual(parent_children(4, r, k), square_case_children(r, k))

    def test_triangular_r2_pell_hit(self):
        hit, m = exact_hit_via_discriminant(3, 2, 2)
        self.assertTrue(hit)
        self.assertEqual(m, 3)
        self.assertEqual(2 * polygonal(3, 2), polygonal(3, 3))
        self.assertEqual(exact_hit_pell_residual(3, 2, 2, 3), 0)

    def test_incidence_duplicate_stats(self):
        # Search a small concrete parent support with a duplicate and verify accounting.
        found = None
        for s in range(3, 9):
            for r in (2, 3):
                for k in range(1, 100):
                    res = one_step(s, r, (k, k + 1))
                    if res.duplicate_edge_excess:
                        found = res
                        break
                if found:
                    break
            if found:
                break
        self.assertIsNotNone(found)
        self.assertEqual(found.raw_edges - found.duplicate_edge_excess, len(found.target))
        self.assertTrue(all(len(found.incidence[j]) == 2 for j in found.recoalescing_children))

    def test_actual_value_bridge(self):
        self.assertEqual(actual_value_support(5, (1, 3, 4)), (1, 12, 22))

    def test_mutation_lower_index_boundaries(self):
        # Boundary-focused mutation guard: m-1 and m+1 are not also valid lower indices.
        rng = random.Random(35035)
        for _ in range(5000):
            s = rng.randint(3, 30)
            n = rng.randint(0, 10**9)
            m = lower_index(s, n)
            self.assertLessEqual(polygonal(s, m), n)
            self.assertGreater(polygonal(s, m + 1), n)
            if m:
                self.assertLess(polygonal(s, m - 1), polygonal(s, m))

    def test_square_non_square_hit_boundary(self):
        # For s=4 and k>0, r*k^2 is square iff r is square.
        for r in range(1, 100):
            rq = isqrt(r)
            square_r = rq * rq == r
            for k in range(1, 20):
                self.assertEqual(len(parent_children(4, r, k)) == 1, square_r)

    def test_gap_detector(self):
        self.assertFalse(support_has_internal_gap((3, 4, 5)))
        self.assertTrue(support_has_internal_gap((3, 5)))

    def test_lower_map_strict_and_jump_bound(self):
        for s in range(3, 20):
            for r in range(1, 30):
                for k in range(0, 300):
                    d = lower_jump(s, r, k)
                    self.assertGreaterEqual(d, 1)
                    self.assertLessEqual(d, r)

    def test_no_recoalescence_r_ge_4(self):
        for s in range(3, 15):
            for r in range(4, 25):
                for k in range(1, 300):
                    self.assertGreaterEqual(lower_jump(s, r, k), 2)
                    res = one_step(s, r, (k, k + 1))
                    self.assertEqual(res.duplicate_edge_excess, 0)

    def test_r2_r3_singleton_orbits_are_intervals(self):
        for s in range(3, 15):
            for r in (2, 3):
                for k0 in range(0, 80):
                    for S in iterate_support(s, r, k0, 8):
                        self.assertTrue(is_integer_interval(S))

    def test_r4_closed_form(self):
        for s in range(3, 40):
            for k in range(0, 1000):
                self.assertEqual(parent_children(s, 4, k), r4_children_formula(s, k))

    def test_r4_orbit_closed_form(self):
        for k0 in range(1, 30):
            for t, S in enumerate(iterate_support(3, 4, k0, 8)):
                self.assertEqual(S, tuple(range((2**t)*k0, (2**t)*(k0+1))))
            for t, S in enumerate(iterate_support(4, 4, k0, 8)):
                self.assertEqual(S, ((2**t)*k0,))
            for s in (5, 6, 10, 25):
                for t, S in enumerate(iterate_support(s, 4, k0, 8)):
                    lo = (2**t)*(k0-1)+1
                    hi = (2**t)*k0
                    self.assertEqual(S, tuple(range(lo, hi+1)))

    def test_self_loop_classification(self):
        for s in range(3, 40):
            for r in range(2, 30):
                for k in range(1, 50):
                    expected = (k == 1 and r < s) or (k == 2 and r == 2 and s >= 4)
                    self.assertEqual(has_lower_self_loop(s, r, k), expected)

    def test_cardinality_conservation(self):
        rng = random.Random(350350)
        for _ in range(3000):
            s = rng.randint(3, 30)
            r = rng.randint(1, 40)
            support = {rng.randint(0, 200) for _ in range(rng.randint(0, 12))}
            n, hits, duplicates, nnext = cardinality_components(s, r, support)
            self.assertEqual(nnext, 2*n-hits-duplicates)

    def test_sharp_interval_threshold_witness(self):
        for r in range(1, 5):
            for s in range(3, 13):
                for k0 in range(0, 80):
                    for S in iterate_support(s, r, k0, 7):
                        self.assertTrue(is_integer_interval(S))
        self.assertEqual(iterate_support(3, 5, 1, 2)[-1], (5, 7, 8))

    def test_uniform_interval_failure_family_r_ge_5(self):
        for r in range(5, 151):
            s, k0, s1, s2 = universal_interval_failure_witness(r)
            self.assertEqual((s, k0), (r + 1, 1))
            self.assertEqual(s1, (1, 2))
            self.assertFalse(is_integer_interval(s2))
            self.assertNotIn(3, s2)
            self.assertGreaterEqual(min(x for x in s2 if x > 2), 4)

    def test_recoalescence_factor_classification_witnesses(self):
        # r=1 is identity; r>=4 has separated endpoint blocks.  r=2 and r=3
        # each have a concrete triangular adjacent-parent overlap.
        self.assertTrue(adjacent_parent_overlap(3, 2, 3))
        self.assertTrue(adjacent_parent_overlap(3, 3, 8))
        for s in range(3, 18):
            for r in [1] + list(range(4, 40)):
                for k in range(0, 100):
                    self.assertFalse(adjacent_parent_overlap(s, r, k))

    def test_positive_interval_image_r2_r3_and_origin_exception(self):
        for s in range(3, 20):
            for r in (2, 3):
                for lo in range(1, 30):
                    for width in range(0, 8):
                        src = tuple(range(lo, lo + width + 1))
                        self.assertTrue(is_integer_interval(one_step(s, r, src).target))
        # The positivity hypothesis is real: an artificial interval containing
        # zero need not remain an interval.  Default k0=0 itself is still fixed.
        self.assertEqual(one_step(3, 3, (0, 1)).target, (0, 2))
        self.assertEqual(iterate_support(3, 3, 0, 5), ((0,),) * 6)

    def test_eventual_two_jump_alphabet_certificate(self):
        for s in range(3, 45):
            for r in range(2, 100):
                K = eventual_two_jump_start(s, r)
                q = isqrt(r)
                for k in range(K, K + 120):
                    self.assertIn(lower_jump(s, r, k), (q, q + 1))


if __name__ == "__main__":
    unittest.main()
