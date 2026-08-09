"""Losslessly compress monotone compiled E001 material branches into finite runs.

Run-end compression is standard engineering practice.  This module operates on
the generic compiled branch interface, so compression is independent of whether
the samples came from a real-data fit, an intrinsic oscillator profile, or an
ordered material program.
"""

from __future__ import annotations

from bisect import bisect_left
from dataclasses import dataclass

from .material_fit import project_interval_nearest
from .material_runtime import CompiledMaterialCurve, minimum_unsigned_byte_width


@dataclass(frozen=True)
class MonotoneRunMaterialCurve:
    """Lossless run-end encoding of one non-decreasing material branch."""

    lower_deformation: int
    upper_deformation: int
    max_cell: int
    run_ends: tuple[int, ...]
    run_values: tuple[int, ...]
    cell_bytes: int
    value_bytes: int
    source_kind: str

    @property
    def run_count(self) -> int:
        return len(self.run_values)

    @property
    def packed_size_bytes(self) -> int:
        return self.run_count * (self.cell_bytes + self.value_bytes)


def compress_monotone_material_curve(
    curve: CompiledMaterialCurve,
) -> MonotoneRunMaterialCurve:
    """Compress equal-output plateaus; reject non-monotone runtime branches."""
    values = curve.values
    if not values:
        raise ValueError("compiled curve must contain at least one value")
    if tuple(sorted(values)) != values:
        raise ValueError("run compression currently requires a non-decreasing curve")

    run_ends: list[int] = []
    run_values: list[int] = []
    current = values[0]
    for cell in range(1, len(values)):
        if values[cell] != current:
            run_ends.append(cell - 1)
            run_values.append(current)
            current = values[cell]
    run_ends.append(len(values) - 1)
    run_values.append(current)

    if run_ends[-1] != curve.max_cell:
        raise AssertionError("compressed run coverage does not end at max_cell")
    return MonotoneRunMaterialCurve(
        lower_deformation=curve.lower_deformation,
        upper_deformation=curve.upper_deformation,
        max_cell=curve.max_cell,
        run_ends=tuple(run_ends),
        run_values=tuple(run_values),
        cell_bytes=minimum_unsigned_byte_width(curve.max_cell),
        value_bytes=minimum_unsigned_byte_width(max(run_values)),
        source_kind=curve.source_kind,
    )


def lookup_run_material_cell(curve: MonotoneRunMaterialCurve, cell: int) -> int:
    """Evaluate a normalized cell through binary search over finite run ends."""
    if isinstance(cell, bool) or not isinstance(cell, int) or cell < 0:
        raise ValueError("cell must be a non-negative integer")
    if cell > curve.max_cell:
        raise ValueError("cell exceeds compressed curve domain")
    index = bisect_left(curve.run_ends, cell)
    if index >= curve.run_count:
        raise AssertionError("compressed material lookup escaped its run partition")
    return curve.run_values[index]


def lookup_run_material_deformation(
    curve: MonotoneRunMaterialCurve, deformation: int
) -> int:
    """Project a physical deformation and evaluate the lossless run encoding."""
    if isinstance(deformation, bool) or not isinstance(deformation, int):
        raise ValueError("deformation must be an integer")
    if deformation < curve.lower_deformation or deformation > curve.upper_deformation:
        raise ValueError("deformation lies outside compressed physical bounds")
    if curve.max_cell == 0:
        return curve.run_values[0]
    cell = project_interval_nearest(
        deformation,
        curve.lower_deformation,
        curve.upper_deformation,
        curve.max_cell,
    )
    return lookup_run_material_cell(curve, cell)


def pack_run_material_curve_little_endian(curve: MonotoneRunMaterialCurve) -> bytes:
    """Serialize ``(run_end,run_value)`` pairs using certified minimal widths."""
    payload = bytearray()
    for run_end, value in zip(curve.run_ends, curve.run_values, strict=True):
        payload.extend(run_end.to_bytes(curve.cell_bytes, "little", signed=False))
        payload.extend(value.to_bytes(curve.value_bytes, "little", signed=False))
    if len(payload) != curve.packed_size_bytes:
        raise AssertionError("compressed payload disagrees with size certificate")
    return bytes(payload)
