"""Finite coarse-cell proof certificates for Enterprise Math P018 stage 3.

A low-precision state denotes a finite fiber of compatible finer integer states.
For coordinatewise monotone operations, evaluating the operation at the lower
and upper corners of that finite cell gives an exact enclosure of every value in
the cell.  A predicate whose decision boundary lies outside that enclosure is
therefore proved at the coarse precision and remains proved under all compatible
refinements.

This is a finite-state construction.  It does not interpret cells as enclosures
of hidden real numbers.
"""

from __future__ import annotations

from collections.abc import Callable

from .graded_precision import degree_project
from .precision import precision_ratio, project_precision

Certificate = str
TRUE: Certificate = "TRUE"
FALSE: Certificate = "FALSE"
UNRESOLVED: Certificate = "UNRESOLVED"


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def precision_cell(value: int, coarse: int, fine: int) -> dict[str, int]:
    """Return the finite fine-coordinate fiber containing ``value``.

    If r=fine/coarse and a=value//r, the cell is
        {r*a, ..., r*(a+1)-1}.
    """
    _require_natural("value", value)
    ratio = precision_ratio(coarse, fine)
    coarse_value = value // ratio
    lower = ratio * coarse_value
    upper = ratio * (coarse_value + 1) - 1
    if not lower <= value <= upper:
        raise AssertionError("precision cell does not contain the value")
    return {
        "ratio": ratio,
        "coarse_value": coarse_value,
        "lower": lower,
        "upper": upper,
    }


def precision_cell_nesting(
    value: int, coarse: int, middle: int, fine: int
) -> dict[str, dict[str, int]]:
    """Verify that a compatible refined cell is contained in the coarse cell."""
    precision_ratio(coarse, middle)
    precision_ratio(middle, fine)
    coarse_cell = precision_cell(value, coarse, fine)
    middle_value = project_precision(value, middle, fine)
    # Express the middle cell back in final fine coordinates.
    fine_per_middle = precision_ratio(middle, fine)
    refined_lower = fine_per_middle * middle_value
    refined_upper = fine_per_middle * (middle_value + 1) - 1
    if not (
        coarse_cell["lower"]
        <= refined_lower
        <= value
        <= refined_upper
        <= coarse_cell["upper"]
    ):
        raise AssertionError("refined precision cell is not nested")
    return {
        "coarse": coarse_cell,
        "refined": {
            "ratio": fine_per_middle,
            "coarse_value": middle_value,
            "lower": refined_lower,
            "upper": refined_upper,
        },
    }


def vector_precision_cell(
    values: list[int], coarse: int, fine: int
) -> dict[str, list[int] | int]:
    """Return lower/upper corners of a product precision cell."""
    if not values:
        raise ValueError("at least one value is required")
    cells = [precision_cell(value, coarse, fine) for value in values]
    return {
        "ratio": cells[0]["ratio"],
        "coarse_values": [cell["coarse_value"] for cell in cells],
        "lower": [cell["lower"] for cell in cells],
        "upper": [cell["upper"] for cell in cells],
    }


def monotone_cell_bounds(
    operation: Callable[[list[int]], int],
    values: list[int],
    coarse: int,
    fine: int,
) -> dict[str, int | list[int]]:
    """Evaluate a coordinatewise-monotone operation on the two cell corners.

    The caller supplies the mathematical monotonicity contract.  The returned
    bounds are exact consequences of that contract on this finite cell.
    """
    cell = vector_precision_cell(values, coarse, fine)
    lower_args = list(cell["lower"])
    upper_args = list(cell["upper"])
    actual = operation(values)
    lower = operation(lower_args)
    upper = operation(upper_args)
    for name, value in (("operation lower", lower), ("operation upper", upper), ("operation actual", actual)):
        _require_natural(name, value)
    if lower > actual or actual > upper:
        raise ValueError(
            "operation violated the coordinatewise-monotone contract on this cell"
        )
    return {
        **cell,
        "image_lower": lower,
        "image_upper": upper,
        "actual": actual,
    }


def strict_less_threshold_certificate(
    image_lower: int, image_upper: int, threshold: int
) -> Certificate:
    """Certify F(x)<threshold on an entire finite image interval when possible."""
    _require_natural("image_lower", image_lower)
    _require_natural("image_upper", image_upper)
    _require_natural("threshold", threshold)
    if image_lower > image_upper:
        raise ValueError("image_lower must not exceed image_upper")
    if image_upper < threshold:
        return TRUE
    if image_lower >= threshold:
        return FALSE
    return UNRESOLVED


def equality_threshold_certificate(
    image_lower: int, image_upper: int, target: int
) -> Certificate:
    """Certify F(x)=target on a whole finite image interval when possible."""
    _require_natural("image_lower", image_lower)
    _require_natural("image_upper", image_upper)
    _require_natural("target", target)
    if image_lower > image_upper:
        raise ValueError("image_lower must not exceed image_upper")
    if image_lower == image_upper == target:
        return TRUE
    if target < image_lower or target > image_upper:
        return FALSE
    return UNRESOLVED


def monotone_threshold_certificate(
    operation: Callable[[list[int]], int],
    values: list[int],
    coarse: int,
    fine: int,
    threshold: int,
) -> dict[str, int | list[int] | Certificate]:
    """Return a coarse certificate for the predicate operation(values)<threshold."""
    bounds = monotone_cell_bounds(operation, values, coarse, fine)
    status = strict_less_threshold_certificate(
        int(bounds["image_lower"]), int(bounds["image_upper"]), threshold
    )
    return {**bounds, "threshold": threshold, "certificate": status}


def threshold_certificate_profile(
    operation: Callable[[list[int]], int],
    finest_values: list[int],
    threshold: int,
    scales: list[int],
) -> list[Certificate]:
    """Return certificates along an increasing divisibility refinement chain.

    Once TRUE or FALSE is obtained it may never return to UNRESOLVED or switch
    truth value, because each later cell is a subset of the earlier cell.
    """
    if not scales:
        raise ValueError("at least one scale is required")
    finest_scale = scales[-1]
    previous = scales[0]
    statuses: list[Certificate] = []
    decided: Certificate | None = None
    for scale in scales:
        precision_ratio(previous, scale)
        precision_ratio(scale, finest_scale)
        current_values = [
            project_precision(value, scale, finest_scale)
            for value in finest_values
        ]
        data = monotone_threshold_certificate(
            operation, current_values, scale, scale, threshold
        )
        # The previous call uses the current states as exact states.  To retain
        # the unresolved finer possibilities relative to the final precision,
        # compute the cell directly in final coordinates.
        final_bounds = monotone_cell_bounds(
            operation, finest_values, scale, finest_scale
        )
        status = strict_less_threshold_certificate(
            int(final_bounds["image_lower"]),
            int(final_bounds["image_upper"]),
            threshold,
        )
        _ = data
        if decided is not None and status != decided:
            raise AssertionError("a coarse proof certificate was overturned")
        if status != UNRESOLVED:
            decided = status
        statuses.append(status)
        previous = scale
    return statuses


def order_cell_certificate(
    left: int, right: int, coarse: int, fine: int
) -> Certificate:
    """Certify x<y for every pair in the two coarse fibers when possible."""
    left_cell = precision_cell(left, coarse, fine)
    right_cell = precision_cell(right, coarse, fine)
    if left_cell["upper"] < right_cell["lower"]:
        return TRUE
    if left_cell["lower"] >= right_cell["upper"]:
        return FALSE
    return UNRESOLVED


def homogeneous_operation_defect(
    operation: Callable[[list[int]], int],
    fine_values: list[int],
    coarse: int,
    fine: int,
    degree: int,
) -> dict[str, int | list[int]]:
    """Return the finite naturality defect of a monotone q-homogeneous operation.

    Required mathematical contract:
      * operation is coordinatewise nondecreasing on N^m;
      * operation(r*x)=r^q operation(x) for positive integer r.

    Under this contract the defect is bounded by one coarse output-cell image
    width.  The implementation checks the resulting inequalities on the supplied
    finite cell and raises if they fail.
    """
    if not fine_values:
        raise ValueError("at least one input value is required")
    _require_natural("degree", degree)
    if degree <= 0:
        raise ValueError("degree must be positive")
    ratio = precision_ratio(coarse, fine)
    coarse_values = [
        project_precision(value, coarse, fine) for value in fine_values
    ]
    coarse_output = operation(coarse_values)
    fine_output = operation(fine_values)
    upper_corner = [value + 1 for value in coarse_values]
    upper_output = operation(upper_corner)
    for name, value in (
        ("coarse output", coarse_output),
        ("fine output", fine_output),
        ("upper output", upper_output),
    ):
        _require_natural(name, value)

    transported_lower = ratio**degree * coarse_output
    transported_upper = ratio**degree * upper_output
    if fine_output < transported_lower or fine_output > transported_upper:
        raise ValueError(
            "operation violated its monotone homogeneous cell bounds"
        )

    recovered = fine_output // ratio**degree
    defect = recovered - coarse_output
    defect_bound = upper_output - coarse_output
    if not 0 <= defect <= defect_bound:
        raise AssertionError("homogeneous operation defect escaped its cell bound")
    output_detail = fine_output % ratio**degree
    return {
        "ratio": ratio,
        "degree": degree,
        "coarse_values": coarse_values,
        "coarse_output": coarse_output,
        "upper_output": upper_output,
        "recovered": recovered,
        "defect": defect,
        "defect_bound": defect_bound,
        "output_detail": output_detail,
    }


def zero_defect_certificate(
    operation: Callable[[list[int]], int],
    fine_values: list[int],
    coarse: int,
    fine: int,
    degree: int,
) -> bool:
    """Return the exact no-cell-crossing criterion for a homogeneous operation."""
    data = homogeneous_operation_defect(
        operation, fine_values, coarse, fine, degree
    )
    ratio = int(data["ratio"])
    fine_output = operation(fine_values)
    boundary = ratio**degree * (int(data["coarse_output"]) + 1)
    criterion = fine_output < boundary
    if criterion != (int(data["defect"]) == 0):
        raise AssertionError("zero-defect criterion failed")
    return criterion


def homogeneous_operation_recovery_profile(
    operation: Callable[[list[int]], int],
    finest_values: list[int],
    degree: int,
    base_scale: int,
    scales: list[int],
) -> list[int]:
    """Return the monotone base-scale recovery of a monotone q-homogeneous map."""
    _require_positive("base_scale", base_scale)
    _require_natural("degree", degree)
    if degree <= 0:
        raise ValueError("degree must be positive")
    if not scales or scales[0] != base_scale:
        raise ValueError("scales must start at base_scale")
    if not finest_values:
        raise ValueError("at least one value is required")

    finest_scale = scales[-1]
    previous_scale = base_scale
    profile: list[int] = []
    last: int | None = None
    for scale in scales:
        precision_ratio(previous_scale, scale)
        precision_ratio(scale, finest_scale)
        current_values = [
            project_precision(value, scale, finest_scale)
            for value in finest_values
        ]
        current_output = operation(current_values)
        _require_natural("operation output", current_output)
        recovered = degree_project(
            current_output, base_scale, scale, degree
        )
        if last is not None and recovered < last:
            raise ValueError(
                "operation violated monotone homogeneous recovery on the chain"
            )
        profile.append(recovered)
        last = recovered
        previous_scale = scale
    return profile
