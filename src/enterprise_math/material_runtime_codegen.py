"""Emit small no-floating-point C headers for compiled E001 material curves.

Code generation and lookup-table deployment are established engineering
techniques.  This module exists so the E001 pressure test can cross the boundary
from Python reference mathematics into an auditable embedded/runtime artifact.
The generated lookup consumes an already-normalized finite deformation cell;
normalization belongs to the surrounding world/physics engine.
"""

from __future__ import annotations

import re

from .material_runtime_compressed import MonotoneRunMaterialCurve

_SYMBOL_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _unsigned_c_type(byte_width: int) -> str:
    if byte_width <= 1:
        return "uint8_t"
    if byte_width <= 2:
        return "uint16_t"
    if byte_width <= 4:
        return "uint32_t"
    if byte_width <= 8:
        return "uint64_t"
    raise ValueError("generated C runtime supports at most 64-bit unsigned fields")


def emit_c_run_material_header(
    curve: MonotoneRunMaterialCurve,
    symbol: str,
) -> str:
    """Return a self-contained C header for exact compressed-cell lookup."""
    if not isinstance(symbol, str) or not _SYMBOL_RE.fullmatch(symbol):
        raise ValueError("symbol must be a valid C identifier")
    if curve.run_count <= 0:
        raise ValueError("curve must contain at least one run")

    cell_type = _unsigned_c_type(curve.cell_bytes)
    value_type = _unsigned_c_type(curve.value_bytes)
    upper_symbol = symbol.upper()
    ends = ", ".join(str(value) for value in curve.run_ends)
    values = ", ".join(str(value) for value in curve.run_values)

    return f"""#ifndef {upper_symbol}_MATERIAL_H
#define {upper_symbol}_MATERIAL_H

#include <stddef.h>
#include <stdint.h>

#define {upper_symbol}_MATERIAL_AMPLITUDE {curve.amplitude}u
#define {upper_symbol}_MATERIAL_RUN_COUNT {curve.run_count}u
#define {upper_symbol}_MATERIAL_PACKED_DATA_BYTES {curve.packed_size_bytes}u

static const {cell_type} {symbol}_run_ends[{curve.run_count}] = {{{ends}}};
static const {value_type} {symbol}_run_values[{curve.run_count}] = {{{values}}};

static inline {value_type} {symbol}_material_lookup_cell({cell_type} cell) {{
    size_t lo = 0u;
    size_t hi = {curve.run_count}u;
    if (cell > ({cell_type}){curve.amplitude}u) {{
        cell = ({cell_type}){curve.amplitude}u;
    }}
    while (lo < hi) {{
        const size_t mid = lo + (hi - lo) / 2u;
        if (cell <= {symbol}_run_ends[mid]) {{
            hi = mid;
        }} else {{
            lo = mid + 1u;
        }}
    }}
    return {symbol}_run_values[lo];
}}

#endif
"""
