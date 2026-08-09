"""Exact area shells under finite stress-strain measurement refinement.

This E001 empirical module studies what changes when a *new measured point* is
inserted into an already declared integer polyline.  It does not interpolate or
claim to recover the unknown continuum curve between samples.

For adjacent measured endpoints ``P0=(e0,s0)``, ``P2=(e2,s2)`` with ``e0<e2``
and a newly measured interior point ``P1=(e1,s1)``, ``e0<e1<e2``, the change in
the exact doubled trapezoid coordinate is

    delta = (e2-e0)*s1 - (e2-e1)*s0 - (e1-e0)*s2
          = (e2-e0)*(s1-s0) - (e1-e0)*(s2-s0).

Thus ``delta`` is an integer oriented-triangle determinant.  It vanishes exactly
when the new point lies on the old chord, using cross multiplication only.

The shell is translation invariant and transforms under positive integer axis
rescaling ``e -> a*e+b``, ``s -> c*s+d`` by

    delta' = a*c*delta.

For any sequence of genuine point insertions, local shells telescope exactly:

    sum local_delta = area2(final polyline) - area2(initial polyline).

Hence the *total* area refinement defect is endpoint/path independent once the
final measured point set is fixed, while the local shell witness decomposition
can depend on insertion order and can contain cancellations.  This is another
finite example of the project-wide distinction between compressed final values
and refinement/history witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass

MeasurementPoint = tuple[int, int]


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_point(point: MeasurementPoint, name: str) -> None:
    if not isinstance(point, tuple) or len(point) != 2:
        raise ValueError(f"{name} must be an (deformation,response) integer pair")
    _require_integer(f"{name}.deformation", point[0])
    _require_integer(f"{name}.response", point[1])


def _require_increasing_polyline(points: tuple[MeasurementPoint, ...]) -> None:
    if len(points) < 2:
        raise ValueError("polyline requires at least two measured points")
    for index, point in enumerate(points):
        _require_point(point, f"points[{index}]")
    if not all(left[0] < right[0] for left, right in zip(points, points[1:])):
        raise ValueError("measurement deformation counts must be strictly increasing")


def measured_polyline_doubled_area(
    points: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
) -> int:
    """Exact doubled trapezoid coordinate of an increasing measured polyline."""
    values = tuple(points)
    _require_increasing_polyline(values)
    return sum(
        (right[0] - left[0]) * (left[1] + right[1])
        for left, right in zip(values, values[1:])
    )


def trapezoid_refinement_shell(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
) -> int:
    """Return exact ``area2(refined)-area2(coarse)`` for one new measured point."""
    _require_point(left, "left")
    _require_point(inserted, "inserted")
    _require_point(right, "right")
    e0, s0 = left
    e1, s1 = inserted
    e2, s2 = right
    if not e0 < e1 < e2:
        raise ValueError("inserted deformation must lie strictly between endpoint counts")
    return (e2 - e0) * s1 - (e2 - e1) * s0 - (e1 - e0) * s2


def measured_point_lies_on_chord(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
) -> bool:
    """Exact integer collinearity criterion for the old measurement chord."""
    return trapezoid_refinement_shell(left, inserted, right) == 0


@dataclass(frozen=True)
class MeasurementRefinementStep:
    before: tuple[MeasurementPoint, ...]
    inserted: MeasurementPoint
    containing_left_index: int
    containing_interval: tuple[MeasurementPoint, MeasurementPoint]
    local_area_shell: int
    area2_before: int
    area2_after: int
    after: tuple[MeasurementPoint, ...]


def insert_measured_point(
    points: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    inserted: MeasurementPoint,
) -> MeasurementRefinementStep:
    """Insert one genuinely new measured point and expose its exact local shell."""
    before = tuple(points)
    _require_increasing_polyline(before)
    _require_point(inserted, "inserted")
    if any(point[0] == inserted[0] for point in before):
        raise ValueError("inserted deformation count already exists in the measured polyline")
    if not before[0][0] < inserted[0] < before[-1][0]:
        raise ValueError("inserted point must refine an existing interior interval")

    left_index = next(
        index
        for index, (left, right) in enumerate(zip(before, before[1:]))
        if left[0] < inserted[0] < right[0]
    )
    left = before[left_index]
    right = before[left_index + 1]
    shell = trapezoid_refinement_shell(left, inserted, right)
    after = before[: left_index + 1] + (inserted,) + before[left_index + 1 :]
    area_before = measured_polyline_doubled_area(before)
    area_after = measured_polyline_doubled_area(after)
    if area_after - area_before != shell:
        raise AssertionError("local trapezoid shell disagrees with full polyline area change")
    return MeasurementRefinementStep(
        before=before,
        inserted=inserted,
        containing_left_index=left_index,
        containing_interval=(left, right),
        local_area_shell=shell,
        area2_before=area_before,
        area2_after=area_after,
        after=after,
    )


@dataclass(frozen=True)
class MeasurementRefinementTrace:
    initial: tuple[MeasurementPoint, ...]
    insertion_order: tuple[MeasurementPoint, ...]
    steps: tuple[MeasurementRefinementStep, ...]
    final: tuple[MeasurementPoint, ...]
    local_area_shells: tuple[int, ...]
    total_area_shell: int
    endpoint_area_difference: int


def trace_measurement_refinement(
    initial: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    insertion_order: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
) -> MeasurementRefinementTrace:
    """Insert measured points sequentially and verify exact shell telescoping."""
    start = tuple(initial)
    _require_increasing_polyline(start)
    current = start
    steps: list[MeasurementRefinementStep] = []
    for point in tuple(insertion_order):
        step = insert_measured_point(current, point)
        steps.append(step)
        current = step.after
    local = tuple(step.local_area_shell for step in steps)
    total = sum(local)
    endpoint = measured_polyline_doubled_area(current) - measured_polyline_doubled_area(start)
    if total != endpoint:
        raise AssertionError("measurement area shells failed exact refinement telescope")
    return MeasurementRefinementTrace(
        initial=start,
        insertion_order=tuple(insertion_order),
        steps=tuple(steps),
        final=current,
        local_area_shells=local,
        total_area_shell=total,
        endpoint_area_difference=endpoint,
    )


@dataclass(frozen=True)
class RefinementOrderComparison:
    first: MeasurementRefinementTrace
    second: MeasurementRefinementTrace
    same_final_polyline: bool
    same_total_area_shell: bool
    same_local_shell_sequence: bool


def compare_refinement_orders(
    initial: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    first_order: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
    second_order: tuple[MeasurementPoint, ...] | list[MeasurementPoint],
) -> RefinementOrderComparison:
    """Compare two insertion histories that may reach the same final measured set."""
    first = trace_measurement_refinement(initial, first_order)
    second = trace_measurement_refinement(initial, second_order)
    same_final = first.final == second.final
    same_total = first.total_area_shell == second.total_area_shell
    if same_final and not same_total:
        raise AssertionError("same final measured polyline changed total refinement area shell")
    return RefinementOrderComparison(
        first=first,
        second=second,
        same_final_polyline=same_final,
        same_total_area_shell=same_total,
        same_local_shell_sequence=(first.local_area_shells == second.local_area_shells),
    )


def affine_transform_point(
    point: MeasurementPoint,
    deformation_scale: int,
    deformation_shift: int,
    response_scale: int,
    response_shift: int,
) -> MeasurementPoint:
    """Apply a positive-scale integer affine change of the two measurement axes."""
    _require_point(point, "point")
    for name, value in (
        ("deformation_scale", deformation_scale),
        ("deformation_shift", deformation_shift),
        ("response_scale", response_scale),
        ("response_shift", response_shift),
    ):
        _require_integer(name, value)
    if deformation_scale <= 0 or response_scale <= 0:
        raise ValueError("measurement axis scales must be positive integers")
    return (
        deformation_scale * point[0] + deformation_shift,
        response_scale * point[1] + response_shift,
    )


def verify_refinement_shell_affine_covariance(
    left: MeasurementPoint,
    inserted: MeasurementPoint,
    right: MeasurementPoint,
    deformation_scale: int,
    deformation_shift: int,
    response_scale: int,
    response_shift: int,
) -> bool:
    """Verify ``delta' = deformation_scale*response_scale*delta`` exactly."""
    original = trapezoid_refinement_shell(left, inserted, right)
    transformed = tuple(
        affine_transform_point(
            point,
            deformation_scale,
            deformation_shift,
            response_scale,
            response_shift,
        )
        for point in (left, inserted, right)
    )
    changed = trapezoid_refinement_shell(*transformed)
    expected = deformation_scale * response_scale * original
    if changed != expected:
        raise AssertionError("measurement area shell lost affine covariance")
    return True
