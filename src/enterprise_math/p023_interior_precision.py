"""Finite-chain audits for P023 Stage-2 interior-like precision theorems."""

from __future__ import annotations

from collections.abc import Mapping

from .core import collapse


def _chain_operation(operation: Mapping[int, int]) -> tuple[int, ...]:
    if not operation:
        raise ValueError("operation must be nonempty")
    n = len(operation)
    if set(operation) != set(range(n)):
        raise ValueError("finite chain operation must have domain 0..N-1")
    values = tuple(operation[index] for index in range(n))
    if any(value < 0 or value >= n for value in values):
        raise ValueError("operation must map the finite chain into itself")
    return values


def is_monotone_reductive_idempotent(operation: Mapping[int, int]) -> bool:
    """Check the P008 interior-like conditions on a finite integer chain."""
    values = _chain_operation(operation)
    if any(values[index] > values[index + 1] for index in range(len(values) - 1)):
        return False
    if any(values[index] > index for index in range(len(values))):
        return False
    return all(values[values[index]] == values[index] for index in range(len(values)))


def fixed_points(operation: Mapping[int, int]) -> tuple[int, ...]:
    values = _chain_operation(operation)
    return tuple(index for index, value in enumerate(values) if index == value)


def floor_precision_descends_on_chain(operation: Mapping[int, int], ratio: int) -> bool:
    """Whether Q_ratio(T(n)) is constant on every represented Q_ratio cell."""
    values = _chain_operation(operation)
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    seen: dict[int, int] = {}
    for index, value in enumerate(values):
        coarse = index // ratio
        output = value // ratio
        if coarse in seen and seen[coarse] != output:
            return False
        seen[coarse] = output
    return True


def fixed_point_alignment_on_chain(operation: Mapping[int, int], ratio: int) -> bool:
    """Whether every fixed point's represented cell-left endpoint is also fixed."""
    values = _chain_operation(operation)
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    for point in fixed_points(operation):
        boundary = ratio * (point // ratio)
        if boundary >= len(values):
            raise AssertionError("cell boundary escaped represented chain")
        if values[boundary] != boundary:
            return False
    return True


def cell_coarse_output_counts(operation: Mapping[int, int], ratio: int) -> dict[int, int]:
    """Number of distinct Q_ratio(T(n)) values inside each represented cell."""
    values = _chain_operation(operation)
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    outputs: dict[int, set[int]] = {}
    for index, value in enumerate(values):
        outputs.setdefault(index // ratio, set()).add(value // ratio)
    return {cell: len(targets) for cell, targets in outputs.items()}


def interior_alignment_theorem_holds(operation: Mapping[int, int], ratio: int) -> bool:
    """Audit fixed-point alignment iff quotient descent plus the two-output bound."""
    if not is_monotone_reductive_idempotent(operation):
        raise ValueError("operation must be monotone, reductive and idempotent")
    aligned = fixed_point_alignment_on_chain(operation, ratio)
    descends = floor_precision_descends_on_chain(operation, ratio)
    two_output = all(
        count <= 2 for count in cell_coarse_output_counts(operation, ratio).values()
    )
    return aligned == descends and two_output


def perfect_power_uniform_precision_witness(power: int, ratio: int) -> dict[str, int]:
    """Uniform witness that Q_ratio cannot carry global C_power for power,ratio>=2."""
    if power < 2 or ratio < 2:
        raise ValueError("power and ratio must be at least two")
    right = (ratio + 1) ** power
    left = right - 1
    if left // ratio != right // ratio:
        raise AssertionError("witness inputs are not in one precision fiber")
    left_collapse = collapse(left, power)
    right_collapse = collapse(right, power)
    if left_collapse // ratio == right_collapse // ratio:
        raise AssertionError("witness collapse outputs did not separate")
    return {
        "power": power,
        "ratio": ratio,
        "left": left,
        "right": right,
        "coarse_input": left // ratio,
        "left_collapse": left_collapse,
        "right_collapse": right_collapse,
        "left_coarse_output": left_collapse // ratio,
        "right_coarse_output": right_collapse // ratio,
    }


def uniform_floor_quotient_refines(finer_ratio: int, coarser_ratio: int) -> bool:
    """Exact criterion for Q_finer to refine Q_coarser on all natural states."""
    if finer_ratio <= 0 or coarser_ratio <= 0:
        raise ValueError("ratios must be positive")
    return coarser_ratio % finer_ratio == 0
