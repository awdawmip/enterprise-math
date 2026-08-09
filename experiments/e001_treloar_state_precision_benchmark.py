"""Compare Treloar predictive error with P024 material-aware state cost.

This experiment deliberately reports two independent axes:

1. constitutive held-out error from the existing leakage-resistant Treloar folds;
2. finite future-state complexity induced by the fitted discrete response branch.

The second axis is not a physical-fit score.  A model can require fewer world
states simply because its represented response has larger plateaus, while still
predicting the held-out material data worse.

For each fold, the fitted root-basin parameters are evaluated on every integer
deformation in the already-declared fixed benchmark domain [100, 761].  The
resulting 662-sample branch is interpreted only for this experiment through the
explicit depth convention

    material_depth = deformation_centi - 100.

Thus collapse_factor=662 gives positive clearance depths 1..661 exactly the
same represented depth range.  No material amplitude, measurement scale, or
spatial factor is silently identified with another quantity.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from enterprise_math.clearance_horizon_precision import (
    isotropic_named_horizon_class_count,
)
from enterprise_math.material_fit import predict_scaled_basis
from enterprise_math.material_future_precision import material_future_class_count
from enterprise_math.material_validation import (
    FixedDomainMaterialFit,
    cross_validate_fixed_domain_material_fit,
    fixed_domain_basis,
)

STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)

DOMAIN_LOWER = 100
DOMAIN_UPPER = 761
DENSE_DEFORMATIONS = tuple(range(DOMAIN_LOWER, DOMAIN_UPPER + 1))
COLLAPSE_FACTOR = len(DENSE_DEFORMATIONS)


@dataclass(frozen=True)
class FoldStateCost:
    amplitude: int
    fold_index: int
    input_root_power: int
    output_hardening_power: int
    output_scale: int
    test_count: int
    test_sse: int
    dense_response_levels: int
    adjacent_plateau_steps: int
    dimension: int
    horizon: int
    raw_future_classes: int
    material_future_classes: int

    @property
    def test_rmse(self) -> float:
        return sqrt(self.test_sse / self.test_count) / 100.0

    @property
    def compression_ratio(self) -> float:
        return self.material_future_classes / self.raw_future_classes


def dense_response_branch(fit: FixedDomainMaterialFit) -> tuple[int, ...]:
    """Evaluate one already-fitted fold model on every integer domain state."""
    basis = fixed_domain_basis(
        DENSE_DEFORMATIONS,
        fit.lower_deformation,
        fit.upper_deformation,
        fit.amplitude,
        fit.input_root_power,
        fit.output_hardening_power,
    )
    return predict_scaled_basis(basis, fit.amplitude, fit.output_scale)


def fold_state_cost(
    *,
    amplitude: int,
    fold_index: int,
    fit: FixedDomainMaterialFit,
    test_count: int,
    test_sse: int,
    dimension: int,
    horizon: int,
) -> FoldStateCost:
    response = dense_response_branch(fit)
    if len(response) != COLLAPSE_FACTOR:
        raise AssertionError("dense response branch no longer matches the declared depth domain")
    raw = isotropic_named_horizon_class_count(
        dimension, COLLAPSE_FACTOR, horizon
    )
    material = material_future_class_count(
        dimension, COLLAPSE_FACTOR, response, horizon
    )
    if material > raw:
        raise AssertionError("coarser material observable produced more classes than raw depth")
    return FoldStateCost(
        amplitude=amplitude,
        fold_index=fold_index,
        input_root_power=fit.input_root_power,
        output_hardening_power=fit.output_hardening_power,
        output_scale=fit.output_scale,
        test_count=test_count,
        test_sse=test_sse,
        dense_response_levels=len(set(response)),
        adjacent_plateau_steps=sum(
            left == right for left, right in zip(response, response[1:], strict=False)
        ),
        dimension=dimension,
        horizon=horizon,
        raw_future_classes=raw,
        material_future_classes=material,
    )


def benchmark_amplitude(
    amplitude: int,
    dimensions: tuple[int, ...] = (2, 3),
    horizons: tuple[int, ...] = (0, 1, 2, 4, 8, 16, 32),
) -> tuple[FoldStateCost, ...]:
    cv = cross_validate_fixed_domain_material_fit(
        STRETCH_CENTI,
        PK1_CENTI,
        DOMAIN_LOWER,
        DOMAIN_UPPER,
        amplitude,
        5,
        12,
        6,
        800,
    )
    rows = []
    for fold in cv.folds:
        for dimension in dimensions:
            for horizon in horizons:
                rows.append(
                    fold_state_cost(
                        amplitude=amplitude,
                        fold_index=fold.fold_index,
                        fit=fold.fit,
                        test_count=fold.test_error.count,
                        test_sse=fold.test_error.sse,
                        dimension=dimension,
                        horizon=horizon,
                    )
                )
    return tuple(rows)


def main() -> None:
    print(
        "metric_boundary=held_out_prediction_error_vs_future_state_complexity "
        f"dense_depth_domain=[0,{COLLAPSE_FACTOR - 1}] "
        "depth_convention=deformation_centi-100"
    )
    for amplitude in (128, 2048, 8192):
        rows = benchmark_amplitude(amplitude)
        for row in rows:
            print(
                f"A={row.amplitude} fold={row.fold_index} "
                f"shape=(G{row.input_root_power},H{row.output_hardening_power},"
                f"{row.output_scale}) "
                f"test_rmse={row.test_rmse:.6f} "
                f"levels={row.dense_response_levels} "
                f"plateau_steps={row.adjacent_plateau_steps} "
                f"n={row.dimension} h={row.horizon} "
                f"raw_classes={row.raw_future_classes} "
                f"material_classes={row.material_future_classes} "
                f"class_ratio={row.compression_ratio:.6f}"
            )


if __name__ == "__main__":
    main()
