"""E001 deployment frontier for compiled Treloar loading curves.

This probe reports an exact packed-table memory certificate beside the observed
Treloar loading error for several representation precisions.  It intentionally
does not claim CPU superiority over floating constitutive models: the runtime
path is structurally one integer interval projection plus one table access, but
hardware timings belong to a later implementation benchmark.
"""

from __future__ import annotations

from math import sqrt

from enterprise_math.material_fit import search_root_basin_material_fit
from enterprise_math.material_runtime import compile_root_basin_material_curve


STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)


def main() -> None:
    print("A shape scale packed_bytes rmse max_abs")
    for amplitude in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        fit = search_root_basin_material_fit(
            STRETCH_CENTI,
            PK1_CENTI,
            amplitude=amplitude,
            max_input_root_power=12,
            max_output_hardening_power=6,
            max_output_scale=800,
        )
        curve = compile_root_basin_material_curve(
            STRETCH_CENTI[0],
            STRETCH_CENTI[-1],
            amplitude,
            fit.input_root_power,
            fit.output_hardening_power,
            fit.output_scale,
        )
        rmse = sqrt(fit.sse / len(PK1_CENTI)) / 100.0
        print(
            f"{amplitude} G{fit.input_root_power}/H{fit.output_hardening_power} "
            f"{fit.output_scale} {curve.packed_size_bytes} "
            f"{rmse:.6f} {fit.max_absolute_error / 100.0:.6f}"
        )


if __name__ == "__main__":
    main()
