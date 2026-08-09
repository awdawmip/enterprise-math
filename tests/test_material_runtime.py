import unittest

from enterprise_math.material_fit import predict_scaled_basis, root_basin_versine_basis
from enterprise_math.material_response import material_curve_profile
from enterprise_math.material_runtime import (
    LOADING,
    RETURNING,
    compile_material_profile_branch,
    compile_material_samples,
    compile_root_basin_material_curve,
    lookup_material_cell,
    lookup_material_deformation,
    minimum_unsigned_byte_width,
    pack_material_curve_little_endian,
)


TRELOAR_STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)


class MaterialRuntimeTests(unittest.TestCase):
    def test_compiled_cells_match_direct_integer_curve_exactly(self):
        amplitude = 128
        curve = compile_root_basin_material_curve(100, 761, amplitude, 4, 2, 672)
        cells = tuple(range(amplitude + 1))
        direct_basis = root_basin_versine_basis(cells, amplitude, 4, 2)
        direct_values = predict_scaled_basis(direct_basis, amplitude, 672)
        self.assertEqual(curve.values, direct_values)
        self.assertEqual(curve.max_cell, amplitude)
        for cell, expected in enumerate(direct_values):
            self.assertEqual(lookup_material_cell(curve, cell), expected)

    def test_physical_deformation_lookup_uses_same_finite_projection(self):
        curve = compile_root_basin_material_curve(100, 761, 128, 4, 2, 672)
        observed = tuple(lookup_material_deformation(curve, value) for value in TRELOAR_STRETCH_CENTI)
        basis = root_basin_versine_basis(TRELOAR_STRETCH_CENTI, 128, 4, 2)
        expected = predict_scaled_basis(basis, 128, 672)
        self.assertEqual(observed, expected)

    def test_profile_response_amplitude_is_not_runtime_input_cell_count(self):
        profile = material_curve_profile(
            (0, 25, 50, 75, 100),
            amplitude=100,
            loading_power=2,
            return_power=1,
            return_retention=50,
        )
        loading = compile_material_profile_branch(profile, 0, 400, LOADING)
        returning = compile_material_profile_branch(profile, 0, 400, RETURNING)
        self.assertEqual(profile.amplitude, 100)
        self.assertEqual(loading.max_cell, 4)
        self.assertEqual(returning.max_cell, 4)
        self.assertEqual(loading.values, profile.loading)
        self.assertEqual(returning.values, profile.returning)
        self.assertEqual(lookup_material_deformation(loading, 200), profile.loading[2])
        self.assertEqual(lookup_material_deformation(returning, 200), profile.returning[2])

    def test_explicit_branch_compiler_accepts_single_cell_without_fake_amplitude(self):
        curve = compile_material_samples(10, 20, (7,), source_kind="CONSTANT")
        self.assertEqual(curve.max_cell, 0)
        self.assertEqual(curve.entry_count, 1)
        for deformation in (10, 15, 20):
            self.assertEqual(lookup_material_deformation(curve, deformation), 7)

    def test_treloar_precision_controls_exact_packed_table_size(self):
        cases = (
            (64, 1, 1, 678, 130),
            (128, 4, 2, 672, 258),
            (512, 4, 2, 663, 1026),
            (1024, 4, 2, 659, 2050),
            (2048, 8, 3, 663, 4098),
        )
        for amplitude, root_power, hard_power, scale, expected_bytes in cases:
            curve = compile_root_basin_material_curve(
                100, 761, amplitude, root_power, hard_power, scale
            )
            self.assertEqual(curve.entry_count, amplitude + 1)
            self.assertEqual(curve.max_cell, amplitude)
            self.assertEqual(curve.bytes_per_value, 2)
            self.assertEqual(curve.packed_size_bytes, expected_bytes)
            self.assertEqual(len(pack_material_curve_little_endian(curve)), expected_bytes)

    def test_minimum_byte_width_tracks_output_range(self):
        self.assertEqual(minimum_unsigned_byte_width(0), 1)
        self.assertEqual(minimum_unsigned_byte_width(255), 1)
        self.assertEqual(minimum_unsigned_byte_width(256), 2)
        self.assertEqual(minimum_unsigned_byte_width(65535), 2)
        self.assertEqual(minimum_unsigned_byte_width(65536), 3)

    def test_invalid_runtime_queries_are_rejected(self):
        curve = compile_root_basin_material_curve(0, 10, 16, 2, 2, 100)
        with self.assertRaises(ValueError):
            lookup_material_cell(curve, 17)
        with self.assertRaises(ValueError):
            lookup_material_deformation(curve, 11)
        with self.assertRaises(ValueError):
            minimum_unsigned_byte_width(-1)
        with self.assertRaises(ValueError):
            compile_material_samples(0, 10, (), source_kind="EMPTY")
        with self.assertRaises(ValueError):
            compile_material_profile_branch(
                material_curve_profile((0, 1), 1), 0, 1, "UNKNOWN"
            )


if __name__ == "__main__":
    unittest.main()
