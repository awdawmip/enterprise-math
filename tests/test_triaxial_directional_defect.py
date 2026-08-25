import random
import unittest
from fractions import Fraction

from enterprise_math.triaxial_directional_defect import (
    convolve_kernels, declare_frame, diff1_kernel, eight_state_trace_cube,
    euler_phi, exposed_vertex_sampling_matrix, family_width,
    finite_support_left_inverse_possible, frame_census_law, gram_factor_kernel,
    gram_matrix, hex_box, hive_bridge_values, kernel_matrix,
    laplacian_product_kernel, matmul, primitive_frame_census, rank_mod, rank_q,
    rhombus2_kernel, six_point_endpoint_stencil, triple_defect_kernel,
    xray_kernel_cert, xray_matrix, y_delta_is_additive_counterexample,
    y_delta_triangle_conductances,
)


def reverse_seed(seed):
    m = max(seed)
    return tuple(m - x for x in seed)


class TriaxialDirectionalDefectTests(unittest.TestCase):
    def test_frame_covariance_orientation_and_bridge(self):
        for seed in ((1, 0, 0), (2, 1, 0), (3, 1, 0), (4, 3, 0)):
            frame = declare_frame(seed)
            rotated = declare_frame((seed[2], seed[0], seed[1]))
            self.assertEqual(triple_defect_kernel(frame), triple_defect_kernel(rotated))
            reversed_frame = declare_frame(reverse_seed(seed))
            self.assertEqual(triple_defect_kernel(reversed_frame), {u: -c for u, c in triple_defect_kernel(frame).items()})
            d1, d2, d3 = frame.directions
            g = triple_defect_kernel(frame)
            self.assertEqual(convolve_kernels(diff1_kernel(d1), rhombus2_kernel(d2, d3)), g)
            self.assertEqual(convolve_kernels(diff1_kernel(d2), rhombus2_kernel(d3, d1)), g)
            self.assertEqual(convolve_kernels(diff1_kernel(d3), rhombus2_kernel(d1, d2)), g)

    def test_eight_trace_states_collapse_only_at_endpoints(self):
        frame = declare_frame((2, 1, 0))
        cube = eight_state_trace_cube(frame)
        self.assertEqual(len(cube), 8)
        zeros = [row for row in cube if row[1] == (0, 0)]
        self.assertEqual(len(zeros), 2)
        self.assertEqual(sum(row[2] for row in zeros), 0)
        stencil = six_point_endpoint_stencil(frame)
        self.assertEqual(len(stencil), 6)
        self.assertTrue(all(abs(c) == 1 for c in stencil.values()))

    def _assert_exact_tomography(self, seeds, radius):
        x, points = xray_matrix(seeds, radius)
        p, domain, codomain = kernel_matrix(seeds, radius)
        self.assertEqual(points, codomain)
        xp = matmul(x, p) if p and x else []
        self.assertTrue(all(v == 0 for row in xp for v in row))
        expected = len(hex_box(radius - family_width(seeds)))
        self.assertEqual(len(points) - rank_q(x), expected)
        self.assertEqual(rank_q(p), len(domain))
        for prime in (2, 3, 5, 7):
            self.assertEqual(len(points) - rank_mod(x, prime), expected)
            self.assertEqual(rank_mod(p, prime), len(domain))

    def test_base_frame_tomography_exact_kernel_and_uniqueness(self):
        for seed in ((1, 0, 0), (2, 1, 0), (3, 1, 0)):
            width = max(seed)
            for radius in range(max(0, width - 1), width + 3):
                self._assert_exact_tomography((seed,), radius)
            x_small, pts_small = xray_matrix((seed,), width - 1)
            self.assertEqual(len(pts_small) - rank_q(x_small), 0)
            x_equal, pts_equal = xray_matrix((seed,), width)
            self.assertEqual(len(pts_equal) - rank_q(x_equal), 1)

    def test_mixed_multiframe_tomography_and_random_regression(self):
        self._assert_exact_tomography(((1, 0, 0), (2, 1, 0)), 4)
        rng = random.Random(79114)
        candidates = list(primitive_frame_census(3, oriented=False))
        rng.shuffle(candidates)
        self._assert_exact_tomography(((2, 1, 0), candidates[0]), 6)

    def test_constructive_kernel_certificate_line_sums(self):
        seeds = ((1, 0, 0), (2, 1, 0))
        amplitude = {p: 3 * p[0] - 2 * p[1] + 5 for p in hex_box(1)}
        self.assertTrue(xray_kernel_cert(amplitude, seeds))

    def test_primitive_frame_euler_phi_census(self):
        for width in range(1, 17):
            unoriented, oriented = frame_census_law(width)
            self.assertEqual(unoriented, euler_phi(width))
            self.assertEqual(oriented, 2 * euler_phi(width))

    def test_exposed_vertex_sampling_is_unimodular_triangular(self):
        for seeds, radius in ((((1, 0, 0),), 4), (((2, 1, 0),), 5), (((1, 0, 0), (2, 1, 0)), 5)):
            m, domain, _, _ = exposed_vertex_sampling_matrix(seeds, radius)
            for i, row in enumerate(m):
                self.assertIn(row[i], (-1, 1))
                self.assertTrue(all(row[j] == 0 for j in range(i + 1, len(row))))
            self.assertEqual(rank_q(m), len(domain))
            for prime in (2, 3, 5, 7):
                self.assertEqual(rank_mod(m, prime), len(domain))

    def test_gram_laplacian_factorization_and_characteristic_boundaries(self):
        frame = declare_frame((1, 0, 0))
        self.assertEqual(gram_factor_kernel(frame), laplacian_product_kernel(frame))
        gram1, _ = gram_matrix(((1, 0, 0),), 1)
        self.assertEqual(gram1, [[6]])
        self.assertEqual((rank_mod(gram1, 2), rank_mod(gram1, 3)), (0, 0))
        gram2, domain2 = gram_matrix(((1, 0, 0),), 2)
        self.assertEqual(rank_q(gram2), len(domain2))
        self.assertLess(rank_mod(gram2, 5), len(domain2))
        gram3, domain3 = gram_matrix(((1, 0, 0),), 3)
        self.assertEqual(rank_q(gram3), len(domain3))
        self.assertLess(rank_mod(gram3, 7), len(domain3))

    def test_hive_rhombus_reuses_same_operator(self):
        frame = declare_frame((1, 0, 0))
        field = {p: p[0] * p[1] * (p[0] + p[1]) for p in hex_box(5)}
        a, b, c, g = hive_bridge_values(field, frame)
        self.assertEqual(a, g)
        self.assertEqual(b, g)
        self.assertEqual(c, g)
        self.assertTrue(any(v != 0 for v in g.values()))

    def test_no_finite_support_translation_invariant_deghosting(self):
        for seed in ((1, 0, 0), (2, 1, 0), (3, 2, 0)):
            self.assertFalse(finite_support_left_inverse_possible(triple_defect_kernel(declare_frame(seed))))

    def test_y_delta_is_negative_discriminator(self):
        self.assertTrue(y_delta_is_additive_counterexample())
        self.assertEqual(y_delta_triangle_conductances(Fraction(1), Fraction(1), Fraction(1)), (Fraction(1, 3),) * 3)


if __name__ == "__main__":
    unittest.main()
