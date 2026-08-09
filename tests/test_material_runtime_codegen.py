import unittest

from enterprise_math.material_runtime import compile_root_basin_material_curve
from enterprise_math.material_runtime_codegen import emit_c_run_material_header
from enterprise_math.material_runtime_compressed import compress_monotone_material_curve


class MaterialRuntimeCodegenTests(unittest.TestCase):
    def test_treloar_a128_header_has_exact_state_certificate_and_no_float_types(self):
        dense = compile_root_basin_material_curve(100, 761, 128, 4, 2, 672)
        curve = compress_monotone_material_curve(dense)
        header = emit_c_run_material_header(curve, "treloar_a128")
        self.assertIn("TRELOAR_A128_MATERIAL_AMPLITUDE 128u", header)
        self.assertIn("TRELOAR_A128_MATERIAL_RUN_COUNT 47u", header)
        self.assertIn("TRELOAR_A128_MATERIAL_PACKED_DATA_BYTES 141u", header)
        self.assertIn("static const uint8_t treloar_a128_run_ends[47]", header)
        self.assertIn("static const uint16_t treloar_a128_run_values[47]", header)
        self.assertIn("treloar_a128_material_lookup_cell", header)
        self.assertNotIn("float", header)
        self.assertNotIn("double", header)

    def test_high_precision_header_uses_16_bit_cell_and_value_fields(self):
        dense = compile_root_basin_material_curve(100, 761, 8192, 8, 3, 661)
        curve = compress_monotone_material_curve(dense)
        header = emit_c_run_material_header(curve, "treloar_a8192")
        self.assertIn("TRELOAR_A8192_MATERIAL_RUN_COUNT 498u", header)
        self.assertIn("TRELOAR_A8192_MATERIAL_PACKED_DATA_BYTES 1992u", header)
        self.assertIn("static const uint16_t treloar_a8192_run_ends[498]", header)
        self.assertIn("static const uint16_t treloar_a8192_run_values[498]", header)

    def test_invalid_c_symbol_is_rejected(self):
        dense = compile_root_basin_material_curve(0, 10, 16, 2, 2, 100)
        curve = compress_monotone_material_curve(dense)
        for symbol in ("9curve", "curve-name", "curve value", ""):
            with self.assertRaises(ValueError):
                emit_c_run_material_header(curve, symbol)


if __name__ == "__main__":
    unittest.main()
