import unittest

from enterprise_math.material_fit import project_interval_nearest
from enterprise_math.material_runtime import compile_root_basin_material_curve
from enterprise_math.material_runtime_compressed import (
    compress_monotone_material_curve,
    lookup_run_material_cell,
    lookup_run_material_deformation,
    pack_run_material_curve_little_endian,
)


class MaterialRuntimeCompressedTests(unittest.TestCase):
    def test_run_encoding_is_lossless_for_every_normalized_cell(self):
        dense = compile_root_basin_material_curve(100, 761, 128, 4, 2, 672)
        compressed = compress_monotone_material_curve(dense)
        self.assertEqual(compressed.run_count, 47)
        for cell, expected in enumerate(dense.values):
            self.assertEqual(lookup_run_material_cell(compressed, cell), expected)

    def test_high_precision_treloar_curve_compresses_to_expected_size(self):
        cases = (
            (64, 1, 1, 678, 39, 117),
            (128, 4, 2, 672, 47, 141),
            (512, 4, 2, 663, 180, 720),
            (1024, 4, 2, 659, 292, 1168),
            (2048, 8, 3, 663, 309, 1236),
            (4096, 8, 3, 661, 410, 1640),
            (8192, 8, 3, 661, 498, 1992),
        )
        for amplitude, root_power, hard_power, scale, runs, packed_bytes in cases:
            dense = compile_root_basin_material_curve(
                100, 761, amplitude, root_power, hard_power, scale
            )
            compressed = compress_monotone_material_curve(dense)
            self.assertEqual(compressed.run_count, runs)
            self.assertEqual(compressed.packed_size_bytes, packed_bytes)
            self.assertEqual(len(pack_run_material_curve_little_endian(compressed)), packed_bytes)
            self.assertLessEqual(compressed.packed_size_bytes, dense.packed_size_bytes)

    def test_physical_lookup_matches_dense_table(self):
        dense = compile_root_basin_material_curve(100, 761, 2048, 8, 3, 663)
        compressed = compress_monotone_material_curve(dense)
        for deformation in range(100, 762):
            cell = project_interval_nearest(deformation, 100, 761, 2048)
            self.assertEqual(
                lookup_run_material_deformation(compressed, deformation),
                dense.values[cell],
            )

    def test_nonmonotone_curve_is_rejected(self):
        dense = compile_root_basin_material_curve(0, 10, 16, 2, 2, 100)
        broken_values = dense.values[:10] + (0,) + dense.values[11:]
        self.assertGreater(dense.values[9], broken_values[10])
        broken = type(dense)(
            lower_deformation=dense.lower_deformation,
            upper_deformation=dense.upper_deformation,
            amplitude=dense.amplitude,
            input_root_power=dense.input_root_power,
            output_hardening_power=dense.output_hardening_power,
            output_scale=dense.output_scale,
            values=broken_values,
            bytes_per_value=dense.bytes_per_value,
        )
        with self.assertRaises(ValueError):
            compress_monotone_material_curve(broken)


if __name__ == "__main__":
    unittest.main()
