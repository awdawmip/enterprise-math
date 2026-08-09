"""Compile E001 finite material fits into deterministic integer lookup tables.

Lookup tables are established engineering practice and are not claimed as an
Enterprise Math invention.  This module tests a narrower project-specific
question: whether the *same declared precision* that constrains the material
representation also gives an exact bound on the compiled runtime state size.

Offline compilation may use integer roots/powers/root-basin geometry.  Runtime
lookup then uses only one finite interval projection plus one table access.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_fit import (
    predict_scaled_basis,
    project_interval_nearest,
    root_basin_versine_basis,
)


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
    """One immutable finite material table with explicit physical input bounds."""

    lower_deformation: int
    upper_deformation: int
    amplitude: int
    input_root_power: int
    output_hardening_power: int
    output_scale: int
    values: tuple[int, ...]
    bytes_per_value: int

    @property
    def entry_count(self) -> int:
        return len(self.values)

    @property
    def packed_size_bytes(self) -> int:
        return self.entry_count * self.bytes_per_value


def compile_root_basin_material_curve(
    lower_deformation: int,
    upper_deformation: int,
    amplitude: int,
    input_root_power: int,
    output_hardening_power: int,
    output_scale: int,
) -> CompiledMaterialCurve:
    """Compile every normalized deformation cell ``0..A`` into one output value."""
    _require_integer("lower_deformation", lower_deformation)
    _require_integer("upper_deformation", upper_deformation)
    _require_positive("amplitude", amplitude)
    _require_positive("input_root_power", input_root_power)
    _require_positive("output_hardening_power", output_hardening_power)
    _require_natural("output_scale", output_scale)
    if upper_deformation <= lower_deformation:
        raise ValueError("upper_deformation must be greater than lower_deformation")

    cells = tuple(range(amplitude + 1))
    basis = root_basin_versine_basis(
        cells,
        amplitude=amplitude,
        input_root_power=input_root_power,
        output_hardening_power=output_hardening_power,
    )
    values = predict_scaled_basis(basis, amplitude, output_scale)
    width = minimum_unsigned_byte_width(max(values, default=0))
    return CompiledMaterialCurve(
        lower_deformation=lower_deformation,
        upper_deformation=upper_deformation,
        amplitude=amplitude,
        input_root_power=input_root_power,
        output_hardening_power=output_hardening_power,
        output_scale=output_scale,
        values=values,
        bytes_per_value=width,
    )


def lookup_material_cell(curve: CompiledMaterialCurve, cell: int) -> int:
    """Evaluate one already-normalized deformation cell by direct table access."""
    _require_natural("cell", cell)
    if cell > curve.amplitude:
        raise ValueError("cell exceeds compiled curve amplitude")
    return curve.values[cell]


def lookup_material_deformation(curve: CompiledMaterialCurve, deformation: int) -> int:
    """Project one physical integer deformation to the compiled finite table."""
    cell = project_interval_nearest(
        deformation,
        curve.lower_deformation,
        curve.upper_deformation,
        curve.amplitude,
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
