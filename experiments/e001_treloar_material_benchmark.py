"""E001 real-material loading benchmark against classic Treloar rubber data.

The experimental points are the Steinmann transcription of Treloar's classic
vulcanized-rubber data exposed by the public ``llamm-de/thermalCANN`` benchmark
repository.  Values are stored here as exact centi-units, matching the published
CSV decimal precision.

The Enterprise Math candidate is fitted entirely with integer arithmetic.  The
Neo-Hooke, Mooney-Rivlin and Yeoh calculations below are external continuous
least-squares baselines only; they are not imported into the project core.
"""

from __future__ import annotations

from math import sqrt

from enterprise_math.material_fit import search_root_basin_material_fit


STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)


def _rmse(targets: tuple[float, ...], predictions: tuple[float, ...]) -> float:
    return sqrt(sum((t - p) ** 2 for t, p in zip(targets, predictions, strict=True)) / len(targets))


def _r2(targets: tuple[float, ...], predictions: tuple[float, ...]) -> float:
    mean = sum(targets) / len(targets)
    residual = sum((t - p) ** 2 for t, p in zip(targets, predictions, strict=True))
    total = sum((t - mean) ** 2 for t in targets)
    return 1.0 - residual / total


def _least_squares(columns: tuple[tuple[float, ...], ...], targets: tuple[float, ...]) -> tuple[float, ...]:
    """Solve a tiny full-rank least-squares system through normal equations."""
    width = len(columns)
    gram = [[sum(columns[i][k] * columns[j][k] for k in range(len(targets))) for j in range(width)] for i in range(width)]
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


def _linear_model(columns: tuple[tuple[float, ...], ...], targets: tuple[float, ...]) -> tuple[tuple[float, ...], tuple[float, ...]]:
    coefficients = _least_squares(columns, targets)
    predictions = tuple(
        sum(coefficients[j] * columns[j][i] for j in range(len(columns)))
        for i in range(len(targets))
    )
    return coefficients, predictions


def continuous_baselines() -> None:
    stretches = tuple(value / 100.0 for value in STRETCH_CENTI)
    targets = tuple(value / 100.0 for value in PK1_CENTI)
    f = tuple(stretch - stretch ** -2 for stretch in stretches)

    neo_coeff, neo_pred = _linear_model((f,), targets)
    print(
        "neo_hooke "
        f"params=1 coeff={neo_coeff} rmse={_rmse(targets, neo_pred):.6f} "
        f"r2={_r2(targets, neo_pred):.6f}"
    )

    mooney_columns = (
        tuple(2.0 * value for value in f),
        tuple(2.0 * f[i] / stretches[i] for i in range(len(f))),
    )
    mooney_coeff, mooney_pred = _linear_model(mooney_columns, targets)
    print(
        "mooney_rivlin "
        f"params=2 coeff={mooney_coeff} rmse={_rmse(targets, mooney_pred):.6f} "
        f"r2={_r2(targets, mooney_pred):.6f}"
    )

    invariant = tuple(stretch * stretch + 2.0 / stretch - 3.0 for stretch in stretches)
    yeoh_columns = (
        tuple(2.0 * f[i] for i in range(len(f))),
        tuple(4.0 * f[i] * invariant[i] for i in range(len(f))),
        tuple(6.0 * f[i] * invariant[i] ** 2 for i in range(len(f))),
    )
    for terms in (1, 2, 3):
        coeff, pred = _linear_model(yeoh_columns[:terms], targets)
        print(
            f"yeoh_{terms} params={terms} coeff={coeff} "
            f"rmse={_rmse(targets, pred):.6f} r2={_r2(targets, pred):.6f}"
        )


def integer_precision_sweep() -> None:
    targets_float = tuple(value / 100.0 for value in PK1_CENTI)
    for amplitude in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        fit = search_root_basin_material_fit(
            STRETCH_CENTI,
            PK1_CENTI,
            amplitude=amplitude,
            max_input_root_power=12,
            max_output_hardening_power=6,
            max_output_scale=800,
        )
        predictions = tuple(value / 100.0 for value in fit.predictions)
        print(
            "enterprise_integer "
            f"A={amplitude} shape=(G{fit.input_root_power},H{fit.output_hardening_power}) "
            f"output_scale={fit.output_scale} params=3 "
            f"rmse={_rmse(targets_float, predictions):.6f} "
            f"r2={_r2(targets_float, predictions):.6f} "
            f"max_abs_error={fit.max_absolute_error / 100.0:.6f}"
        )


def main() -> None:
    print(f"treloar_points={len(STRETCH_CENTI)}")
    print("continuous_baselines")
    continuous_baselines()
    print("integer_precision_sweep")
    integer_precision_sweep()


if __name__ == "__main__":
    main()
