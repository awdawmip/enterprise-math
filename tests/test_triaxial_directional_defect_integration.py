import unittest

import enterprise_math.triaxial_directional_defect as td
from enterprise_math import _triaxial_directional_defect_core as core


def reverse_seed(seed):
    m = max(seed)
    return tuple(m - x for x in seed)


class TriaxialDirectionalDefectIntegrationTests(unittest.TestCase):
    def test_declare_frame_requires_canonical_primitive_and_exposes_unoriented_key(self):
        f = td.DECLARE_FRAME((2, 1, 0))
        self.assertTrue(f.canonical)
        self.assertTrue(f.primitive)
        self.assertEqual(len(set(f.unoriented_rays)), 3)
        with self.assertRaises(ValueError):
            td.DECLARE_FRAME((2, 0, 0))
        with self.assertRaises(ValueError):
            td.DECLARE_FRAME((2, 1, 1))

    def test_cyclic_covariance_and_reversal_sign(self):
        for seed in ((1, 0, 0), (2, 1, 0), (3, 1, 0)):
            a = td.DECLARE_FRAME(seed)
            b = td.DECLARE_FRAME((seed[2], seed[0], seed[1]))
            c = td.DECLARE_FRAME(reverse_seed(seed))
            ka = core.triple_defect_kernel(core.declare_frame(a.seed))
            kb = core.triple_defect_kernel(core.declare_frame(b.seed))
            kc = core.triple_defect_kernel(core.declare_frame(c.seed))
            self.assertEqual(ka, kb)
            self.assertEqual(kc, {u: -v for u, v in ka.items()})

    def test_second_to_third_bridge_uses_shared_operator_core(self):
        frame = td.DECLARE_FRAME((2, 1, 0))
        d1, d2, d3 = frame.directions
        g = core.triple_defect_kernel(core.declare_frame(frame.seed))
        self.assertEqual(core.convolve_kernels(core.diff1_kernel(d1), core.rhombus2_kernel(d2, d3)), g)
        self.assertEqual(core.convolve_kernels(core.diff1_kernel(d2), core.rhombus2_kernel(d3, d1)), g)
        self.assertEqual(core.convolve_kernels(core.diff1_kernel(d3), core.rhombus2_kernel(d1, d2)), g)

    def test_endpoint_stencil_is_not_trace_cube(self):
        frame = td.DECLARE_FRAME((2, 1, 0))
        cube = td.TRACE_CUBE_STATES(frame)
        stencil = td.ENDPOINT_STENCIL(frame)
        self.assertEqual(len(cube), 8)
        self.assertEqual(len(stencil), 6)
        zeros = [row for row in cube if row[1] == (0, 0)]
        self.assertEqual(len(zeros), 2)
        self.assertEqual(sum(row[2] for row in zeros), 0)

    def test_native_hex_single_frame_uniqueness_boundary(self):
        frame = td.DECLARE_FRAME((2, 1, 0))
        self.assertTrue(td.MULTIFRAME_UNIQUENESS((frame.seed,), td.NativeHexDomain(1)).unique)
        cert = td.MULTIFRAME_UNIQUENESS((frame.seed,), td.NativeHexDomain(2))
        self.assertFalse(cert.unique)
        self.assertEqual(cert.nullity, 1)

    def test_native_hex_multiframe_and_unoriented_dedup(self):
        seeds = ((1, 0, 0), (0, 1, 0), (2, 1, 0))
        cert = td.MULTIFRAME_UNIQUENESS(seeds, td.NativeHexDomain(4))
        self.assertEqual(cert.frame_count, 2)
        self.assertEqual(cert.total_width, 3)
        self.assertGreaterEqual(cert.nullity, 0)

    def test_xray_constructive_kernel_certificate(self):
        seeds = ((1, 0, 0), (2, 1, 0))
        amplitude = {p: 3 * p[0] - 2 * p[1] + 5 for p in core.hex_box(1)}
        self.assertTrue(td.XRAY_KERNEL_CERT(amplitude, seeds))

    def test_euler_phi_primitive_census(self):
        for width in range(1, 17):
            self.assertEqual(len(td.PRIMITIVE_FRAME_CENSUS(width, False)), td.EULER_PHI(width))
            self.assertEqual(len(td.PRIMITIVE_FRAME_CENSUS(width, True)), 2 * td.EULER_PHI(width))

    def test_exposed_augmentation_stays_unimodular_in_verified_characteristics(self):
        seeds = ((1, 0, 0), (2, 1, 0))
        for char in (0, 2, 3, 5, 7):
            cert = td.EXPOSED_AUGMENT(seeds, td.NativeHexDomain(5), td.CoefficientDomain(char))
            self.assertTrue(cert.unimodular_full_rank)
            self.assertEqual(cert.rank, cert.dimension)

    def test_full_adjoint_and_compressed_gram_are_distinct_typed_surfaces(self):
        frame = td.DECLARE_FRAME((1, 0, 0))
        adj = td.FULL_ADJOINT({(0, 0): 1}, frame)
        gram = td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(1))
        self.assertEqual(adj.domain, "FULL_SPARSE_FIELD")
        self.assertIsInstance(adj.field, dict)
        self.assertEqual(gram.basis, ((0, 0),))
        self.assertEqual(gram.matrix, ((6,),))
        self.assertNotEqual(type(adj), type(gram))

    def test_gram_factorization_and_small_characteristic_failure_guards(self):
        frame = td.DECLARE_FRAME((1, 0, 0))
        self.assertTrue(td.GRAM_FACTOR(frame).factorization_matches)
        self.assertTrue(td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(1), td.CoefficientDomain(0)).nonsingular)
        self.assertFalse(td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(1), td.CoefficientDomain(2)).nonsingular)
        self.assertFalse(td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(1), td.CoefficientDomain(3)).nonsingular)
        self.assertFalse(td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(2), td.CoefficientDomain(5)).nonsingular)
        self.assertFalse(td.COMPRESSED_GRAM((frame.seed,), td.NativeHexDomain(3), td.CoefficientDomain(7)).nonsingular)
        with self.assertRaises(ValueError):
            td.CoefficientDomain(11)

    def test_hive_rhombus_reuses_same_operator_core(self):
        frame = td.DECLARE_FRAME((1, 0, 0))
        field = {p: p[0] * p[1] * (p[0] + p[1]) for p in core.hex_box(5)}
        a, b, c, g = td.HIVE_BRIDGE(field, frame)
        self.assertEqual(a, g)
        self.assertEqual(b, g)
        self.assertEqual(c, g)
        self.assertTrue(any(v != 0 for v in g.values()))

    def test_y_delta_absent_and_left_inverse_negative_guard_retained(self):
        self.assertNotIn("y_delta_triangle_conductances", td.__all__)
        self.assertFalse(hasattr(td, "y_delta_triangle_conductances"))
        self.assertFalse(td.FINITE_SUPPORT_LEFT_INVERSE_POSSIBLE(td.DECLARE_FRAME((1, 0, 0))))


if __name__ == "__main__":
    unittest.main()
