"""Treloar validation benchmark with deterministic held-out folds."""

from __future__ import annotations

from math import sqrt

from enterprise_math.material_fit import search_root_basin_material_fit
from enterprise_math.material_validation import cross_validate_fixed_domain_material_fit

STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)


def _least_squares(
    columns: tuple[tuple[float, ...], ...], targets: tuple[float, ...]
) -> tuple[float, ...]:
    width = len(columns)
    gram = [
        [sum(columns[i][k] * columns[j][k] for k in range(len(targets))) for j in range(width)]
        for i in range(width)
    ]
    rhs = [sum(columns[i][k] * targets[k] for k in range(len(targets))) for i in range(width)]
    augmented = [gram[i] + [rhs[i]] for i in range(width)]
    for pivot in range(width):
        row = max(range(pivot, width), key=lambda index: abs(augmented[index][pivot]))
        augmented[pivot], augmented[row] = augmented[row], augmented[pivot]
        divisor = augmented[pivot][pivot]
        if abs(divisor) < 1e-15:
            raise ValueError("baseline least-squares system is singular")
        for column in range(pivot, width + 1):
            augmented[pivot][column] /= divisor
        for row_index in range(width):
            if row_index == pivot:
                continue
            factor = augmented[row_index][pivot]
            for column in range(pivot, width + 1):
                augmented[row_index][column] -= factor * augmented[pivot][column]
    return tuple(augmented[i][-1] for i in range(width))


def _baseline_columns() -> dict[str, tuple[tuple[float, ...], ...]]:
    stretches = tuple(value / 100.0 for value in STRETCH_CENTI)
    f = tuple(stretch - stretch ** -2 for stretch in stretches)
    invariant = tuple(stretch * stretch + 2.0 / stretch - 3.0 for stretch in stretches)
    return {
        "neo_hooke": (f,),
        "mooney_rivlin": (
            tuple(2.0 * value for value in f),
            tuple(2.0 * f[i] / stretches[i] for i in range(len(f))),
        ),
        "yeoh_2": (
            tuple(2.0 * f[i] for i in range(len(f))),
            tuple(4.0 * f[i] * invariant[i] for i in range(len(f))),
        ),
        "yeoh_3": (
            tuple(2.0 * f[i] for i in range(len(f))),
            tuple(4.0 * f[i] * invariant[i] for i in range(len(f))),
            tuple(6.0 * f[i] * invariant[i] ** 2 for i in range(len(f))),
        ),
    }


def _continuous_five_fold_rmse(columns: tuple[tuple[float, ...], ...]) -> float:
    targets = tuple(value / 100.0 for value in PK1_CENTI)
    total_sse = 0.0
    for fold in range(5):
        test = tuple(index for index in range(len(targets)) if index % 5 == fold)
        train = tuple(index for index in range(len(targets)) if index % 5 != fold)
        train_columns = tuple(
            tuple(column[index] for index in train) for column in columns
        )
        coefficients = _least_squares(
            train_columns, tuple(targets[index] for index in train)
        )
        for index in test:
            prediction = sum(
                coefficients[j] * columns[j][index] for j in range(len(columns))
            )
            total_sse += (targets[index] - prediction) ** 2
    return sqrt(total_sse / len(targets))


def print_integer_validation(amplitude: int) -> None:
    full = search_root_basin_material_fit(
        STRETCH_CENTI, PK1_CENTI, amplitude, 12, 6, 800
    )
    cv = cross_validate_fixed_domain_material_fit(
        STRETCH_CENTI,
        PK1_CENTI,
        100,
        761,
        amplitude,
        5,
        12,
        6,
        800,
    )
    full_rmse = sqrt(full.sse / len(STRETCH_CENTI)) / 100.0
    cv_rmse = sqrt(cv.aggregate_test_error.sse / cv.aggregate_test_error.count) / 100.0
    shapes = tuple(
        (fold.fit.input_root_power, fold.fit.output_hardening_power, fold.fit.output_scale)
        for fold in cv.folds
    )
    print(
        f"enterprise_integer A={amplitude} "
        f"full_shape=(G{full.input_root_power},H{full.output_hardening_power},{full.output_scale}) "
        f"full_rmse={full_rmse:.6f} cv5_rmse={cv_rmse:.6f} fold_shapes={shapes}"
    )


def main() -> None:
    print(f"treloar_points={len(STRETCH_CENTI)} split=index_mod_5 fixed_domain=[100,761]")
    for name, columns in _baseline_columns().items():
        print(f"continuous {name} cv5_rmse={_continuous_five_fold_rmse(columns):.6f}")
    for amplitude in (128, 2048, 8192):
        print_integer_validation(amplitude)


if __name__ == "__main__":
    main()
