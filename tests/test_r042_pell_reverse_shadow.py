import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import r042_pell_reverse_shadow as rs


class R042PellReverseShadowTests(unittest.TestCase):
    def test_closed_form_ideal_reverse_square_matches_energy_scaling(self):
        s, r, k = 7, 7, 29540
        for depth in (0, 1, 2, 5, 11):
            _, _, _, _, kappa = rs.params(s, r)
            S = rs.ideal_reverse_center_square(s, r, k, depth)
            self.assertEqual(S - kappa * kappa, rs.centered_energy(s, k) / (r ** depth))

    def test_known_revisit_paths_remain_exact(self):
        self.assertEqual(rs.reverse_path(6, 11, 65, 3), (2, 6, 20, 65))
        self.assertEqual(rs.reverse_path(6, 15, 10, 2), (1, 3, 10))
        self.assertEqual(rs.reverse_path(8, 14, 190, 3), (4, 14, 51, 190))

    def test_reduced_class_strict_descent_is_killed(self):
        self.assertTrue(rs.is_exact_hit(8, 40, 1))
        self.assertTrue(rs.is_exact_hit(8, 40, 24))
        self.assertEqual(rs.reverse_path(8, 40, 24, 2), (1, 4, 24))
        self.assertTrue(rs.same_reduced_pell_class(8, 40, 1, 24))

    def test_reduced_pair_bound(self):
        pair = rs.hit_pair(6, 15, 10)
        label = rs.reduce_positive_pell_pair(15, (pair.y, pair.z))
        self.assertEqual((label.reduced_y, label.reduced_z, label.unit_exponent), (2, 2, 2))
        self.assertTrue(rs.reduced_bound_holds(6, 15, (label.reduced_y, label.reduced_z)))

    def test_strong_shadow_alignment_does_not_imply_accessibility(self):
        s, r, h, H, depth = 5, 14, 2, 95, 3
        self.assertTrue(rs.is_exact_hit(s, r, h))
        self.assertTrue(rs.is_exact_hit(s, r, H))
        self.assertTrue(rs.certify_shadow_error_lt(s, r, h, H, depth, Fraction(1, 60)))
        self.assertIsNone(rs.predecessor(s, r, H))

    def test_integer_first_gate_explains_shadow_witness_failure(self):
        rows = rs.exact_first_reverse_gate_values(5, 14, 95)
        self.assertTrue(rows)
        self.assertFalse(any(row["passes"] for row in rows))
        self.assertIn(41, {row["D"] for row in rows})
        self.assertIn(-43, {row["D"] for row in rows})

    def test_local_gate_residual_and_weighted_identity(self):
        path = (2, 6, 20, 65)
        for parent, child in zip(path, path[1:]):
            row = rs.local_gate_residual(6, 11, parent, child)
            self.assertTrue(row["oracle"])
            self.assertTrue(row["gate"])
        lhs, rhs = rs.weighted_path_residual_identity(6, 11, path)
        self.assertEqual(lhs, rhs)
        self.assertEqual(lhs, Fraction(-399, 2))

    def test_shadow_witness_first_local_gate_fails(self):
        rows = [rs.local_gate_residual(5, 14, p, 95) for p in (25, 26)]
        self.assertEqual([row["E"] for row in rows], [-12960, 12576])
        self.assertFalse(any(row["gate"] for row in rows))
        self.assertFalse(any(row["oracle"] for row in rows))


if __name__ == "__main__":
    unittest.main()
