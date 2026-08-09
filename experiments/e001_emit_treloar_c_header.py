"""Print one no-float embedded C header for the A=128 Treloar loading fit."""

from enterprise_math.material_runtime import compile_root_basin_material_curve
from enterprise_math.material_runtime_codegen import emit_c_run_material_header
from enterprise_math.material_runtime_compressed import compress_monotone_material_curve


def main() -> None:
    dense = compile_root_basin_material_curve(100, 761, 128, 4, 2, 672)
    compressed = compress_monotone_material_curve(dense)
    print(emit_c_run_material_header(compressed, "treloar_a128"))


if __name__ == "__main__":
    main()
