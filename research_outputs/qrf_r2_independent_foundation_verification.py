#!/usr/bin/env python3
"""Executable witnesses for RS-QRF-R2-INDEPENDENT-FOUNDATION-VERIFICATION."""

from __future__ import annotations

import json
from typing import Callable

ScalarField = Callable[[int, int], int]


def mixed_defect(q: ScalarField, a: int, b: int) -> int:
    return q(a + 1, b + 1) - q(a + 1, b) - q(a, b + 1) + q(a, b)


def all_zero_defects(q: ScalarField, a_max: int, b_max: int) -> bool:
    return all(mixed_defect(q, a, b) == 0 for a in range(a_max) for b in range(b_max))


def rectangle_defect(q: ScalarField, a0: int, a1: int, b0: int, b1: int) -> int:
    return q(a1, b1) - q(a1, b0) - q(a0, b1) + q(a0, b0)


def q_tau(tau: int) -> ScalarField:
    return lambda a, b: a * a + tau * a * b + b * b


def q_separable(a: int, b: int) -> int:
    return a**3 - 7 * b + 11


def q_target(a: int, b: int) -> int:
    return a * a + b * b


def q_shear(u: int, v: int) -> int:
    return q_target(u, u + v)


def finite_mixing_relabel(a: int, b: int) -> tuple[int, int]:
    if (a, b) == (1, 0):
        return (2, 0)
    if (a, b) == (2, 0):
        return (1, 0)
    return (a, b)


def q_mixed_relabel(a: int, b: int) -> int:
    x, y = finite_mixing_relabel(a, b)
    return q_target(x, y)


def q_reconstructed_from_axes(a: int, b: int) -> int:
    q_a0 = a * a
    q_0b = b * b
    q_00 = 0
    return q_a0 + q_0b - q_00


def main() -> None:
    tau_defects = {
        str(tau): sorted({mixed_defect(q_tau(tau), a, b) for a in range(8) for b in range(8)})
        for tau in (-1, 0, 1)
    }
    assert tau_defects == {"-1": [-1], "0": [0], "1": [1]}

    assert all_zero_defects(q_separable, 8, 8)
    assert rectangle_defect(q_separable, 1, 7, 2, 6) == 0

    assert all(
        q_reconstructed_from_axes(a, b) == q_target(a, b)
        for a in range(12)
        for b in range(12)
    )

    shear_defects = sorted({mixed_defect(q_shear, u, v) for u in range(8) for v in range(8)})
    assert shear_defects == [2]

    finite_relabel_origin_defect = mixed_defect(q_mixed_relabel, 0, 0)
    assert finite_relabel_origin_defect == -3

    output = {
        "verdict_support": "VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL",
        "tau_defects": tau_defects,
        "separable_non_target_zero_defect": True,
        "axis_reconstruction_matches_sum_of_squares_on_12x12": True,
        "shear_defects": shear_defects,
        "finite_channel_mixing_relabel_origin_defect": finite_relabel_origin_defect,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
