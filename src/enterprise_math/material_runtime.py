"""Compile finite E001 material branches into deterministic integer lookup tables.

Lookup tables are established engineering practice and are not claimed as an
Enterprise Math invention.  The project-specific rule here is stricter: the
runtime layer must not conflate four distinct quantities that happen to coincide
for some root-basin fits:

* physical deformation bounds;
* number of represented deformation cells;
* material/profile response amplitude;
* experimental measurement scale.

The generic compiler therefore consumes an explicit finite branch table.  A
root-basin fit and a ``MaterialCurveProfile`` are merely two upstream adapters.
Runtime lookup uses one finite interval projection plus one table access.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_fit import (
    predict_scaled_basis,
    project_interval_nearest,
    root_basin_versine_basis,
)
from .material_response import MaterialCurveProfile

LOADING = "LOADING"
RETURNING = "RETURNING"


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_natural(name: str, value: int) -> None:
    _require_integer(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def minimum_unsigned_byte_width(max_value: int) -> int:
    """Return the minimum whole-byte width for one non-negative integer."""
    _require_natural("max_value", max_value)
    return max(1, (max_value.bit_length() + 7) // 8)


@dataclass(frozen=True)
class CompiledMaterialCurve:
    """One immutable finite material branch on an explicit physical input domain."""

    lower_deformation: int
    upper_deformation: int
    values: tuple[int, ...]
    bytes_per_value: int
    source_kind: str

    @property
    def entry_count(self) -> int:
        return len(self.values)

    @property
    def max_cell(self) -> int:
        return self.entry_count - 1

    @property
    def packed_size_bytes(self) -> int:
        return self.entry_count * self.bytes_per_value


def compile_material_samples(
    lower_deformation: int,
    upper_deformation: int,
    samples: tuple[int, ...] | list[int],
    source_kind: str = "EXPLICIT",
) -> CompiledMaterialCurve:
    """Compile one already-declared finite response branch without reinterpretation."""
    _require_integer("lower_deformation", lower_deformation)
    _require_integer("upper_deformation", upper_deformation)
    if upper_deformation <= lower_deformation:
        raise ValueError("upper_deformation must be greater than lower_deformation")
    values = tuple(samples)
    if not values:
        raise ValueError("material runtime branch must contain at least one sample")
    for value in values:
        _require_natural("material response sample", value)
    if not isinstance(source_kind, str) or not source_kind:
        raise ValueError("source_kind must be a nonempty string")
    width = minimum_unsigned_byte_width(max(values))
    return CompiledMaterialCurve(
        lower_deformation=lower_deformation,
        upper_deformation=upper_deformation,
        values=values,
        bytes_per_value=width,
        source_kind=source_kind,
    )


def compile_material_profile_branch(
    profile: MaterialCurveProfile,
    lower_deformation: int,
    upper_deformation: int,
    branch: str,
) -> CompiledMaterialCurve:
    """Compile one loading/returning branch from the shared profile interface."""
    if branch == LOADING:
        values = profile.loading
    elif branch == RETURNING:
        values = profile.returning
    else:
        raise ValueError("branch must be LOADING or RETURNING")
    return compile_material_samples(
        lower_deformation,
        upper_deformation,
        values,
        source_kind=f"PROFILE:{branch}",
    )


def compile_root_basin_material_curve(
    lower_deformation: int,
    upper_deformation: int,
    amplitude: int,
    input_root_power: int,
    output_hardening_power: int,
    output_scale: int,
) -> CompiledMaterialCurve:
    """Adapter: compile every root-basin normalized deformation cell ``0..A``."""
    _require_positive("amplitude", amplitude)
    _require_positive("input_root_power", input_root_power)
    _require_positive("output_hardening_power", output_hardening_power)
    _require_natural("output_scale", output_scale)
    cells = tuple(range(amplitude + 1))
    basis = root_basin_versine_basis(
        cells,
        amplitude=amplitude,
        input_root_power=input_root_power,
        output_hardening_power=output_hardening_power,
    )
    values = predict_scaled_basis(basis, amplitude, output_scale)
    return compile_material_samples(
        lower_deformation,
        upper_deformation,
        values,
        source_kind=(
            f"ROOT_BASIN:G{input_root_power}:H{output_hardening_power}:S{output_scale}"
        ),
    )


def lookup_material_cell(curve: CompiledMaterialCurve, cell: int) -> int:
    """Evaluate one already-normalized deformation cell by direct table access."""
    _require_natural("cell", cell)
    if cell > curve.max_cell:
        raise ValueError("cell exceeds compiled curve domain")
    return curve.values[cell]


def lookup_material_deformation(curve: CompiledMaterialCurve, deformation: int) -> int:
    """Project one physical integer deformation to the compiled finite branch."""
    _require_integer("deformation", deformation)
    if deformation < curve.lower_deformation or deformation > curve.upper_deformation:
        raise ValueError("deformation lies outside compiled physical bounds")
    if curve.max_cell == 0:
        return curve.values[0]
    cell = project_interval_nearest(
        deformation,
        curve.lower_deformation,
        curve.upper_deformation,
        curve.max_cell,
    )
    return lookup_material_cell(curve, cell)


def pack_material_curve_little_endian(curve: CompiledMaterialCurve) -> bytes:
    """Return a deterministic minimal-width unsigned binary representation."""
    payload = bytearray()
    for value in curve.values:
        payload.extend(value.to_bytes(curve.bytes_per_value, "little", signed=False))
    if len(payload) != curve.packed_size_bytes:
        raise AssertionError("packed material payload length disagrees with size certificate")
    return bytes(payload)
