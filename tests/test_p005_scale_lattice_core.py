import math
import unittest

from enterprise_math.scale_algebra import (
    greatest_common_coarsening,
    least_common_refinement,
    project_scale_factor,
    scale_factor,
    scaled_root_factor,
)


class TestP005ScaleLatticeCore(unittest.TestCase):
    def test_base_level_representation_collapses_to_total_factor(self):
        self.assertEqual(scale_factor(4, 1), 4)
        self.assertEqual(scale_factor(2, 2), 4)
        for base in range(2, 7):
            for level in range(0, 5):
                self.assertEqual(scale_factor(base, level), base**level)

    def test_general_scale_compatibility(self):
        for exponent in range(1, 6):
            for n in range(0, 121):
                for coarse in range(1, 9):
                    for ratio in range(1, 7):
                        fine = coarse * ratio
                        fine_state = scaled_root_factor(n, exponent, fine)
                        projected = project_scale_factor(fine_state, fine, coarse)
                        self.assertEqual(projected, scaled_root_factor(n, exponent, coarse))

    def test_projection_composition(self):
        for value in range(0, 241):
            for d in range(1, 7):
                for a in range(1, 6):
                    for b in range(1, 6):
                        e = d * a
                        f = e * b
                        via = project_scale_factor(
                            project_scale_factor(value, f, e), e, d
                        )
                        direct = project_scale_factor(value, f, d)
                        self.assertEqual(via, direct)

    def test_gcd_lcm_diamond(self):
        for a in range(1, 21):
            for b in range(1, 21):
                g = greatest_common_coarsening(a, b)
                ell = least_common_refinement(a, b)
                self.assertEqual(g, math.gcd(a, b))
                self.assertEqual(ell, math.lcm(a, b))
                for value in range(0, 121):
                    via_a = project_scale_factor(
                        project_scale_factor(value, ell, a), a, g
                    )
                    via_b = project_scale_factor(
                        project_scale_factor(value, ell, b), b, g
                    )
                    direct = project_scale_factor(value, ell, g)
                    self.assertEqual(via_a, direct)
                    self.assertEqual(via_b, direct)

    def test_multibase_refinement_order_independent_from_retained_state(self):
        for exponent in range(1, 5):
            for n in range(0, 101):
                for a in range(1, 8):
                    for b in range(1, 8):
                        self.assertEqual(
                            scaled_root_factor(n, exponent, a * b),
                            scaled_root_factor(n, exponent, b * a),
                        )

    def test_coarse_root_does_not_determine_unique_fine_root(self):
        self.assertEqual(scaled_root_factor(2, 2, 1), 1)
        self.assertEqual(scaled_root_factor(3, 2, 1), 1)
        self.assertEqual(scaled_root_factor(2, 2, 10), 14)
        self.assertEqual(scaled_root_factor(3, 2, 10), 17)

    def test_incomparable_projection_is_rejected(self):
        with self.assertRaises(ValueError):
            project_scale_factor(17, 6, 4)


if __name__ == "__main__":
    unittest.main()
