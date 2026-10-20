"""Finite diagnostic for the BRC horizontal/vertical multiplier coverage bridge.

The theorem-level identity is analytic.  This script only checks the finite
small-theta convergence of exact log-ratio interval unions to the leading
coefficient that underlies the existing multiplier score nu(m)^4/m.

No floating-point output is used as theorem authority.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

THETAS = (1e-2, 1e-3, 1e-4, 1e-5, 1e-6)
MAX_MULTIPLIER = 100


def same_parity_factor_pairs(multiplier: int) -> tuple[tuple[int, int], ...]:
    pairs: list[tuple[int, int]] = []
    for v in range(1, math.isqrt(multiplier) + 1):
        if multiplier % v:
            continue
        u = multiplier // v
        if u > v and (u - v) % 2 == 0:
            pairs.append((u, v))
    return tuple(pairs)


def exact_half_width(multiplier: int, theta: float) -> float:
    return 2.0 * math.acosh(1.0 + theta / math.sqrt(multiplier))


def interval_union_length(intervals: list[tuple[float, float]]) -> float:
    if not intervals:
        return 0.0
    intervals.sort()
    left, right = intervals[0]
    total = 0.0
    for next_left, next_right in intervals[1:]:
        if next_left <= right:
            right = max(right, next_right)
        else:
            total += right - left
            left, right = next_left, next_right
    return total + right - left


def exact_union_length(multiplier: int, theta: float) -> float:
    pairs = same_parity_factor_pairs(multiplier)
    if not pairs:
        return 0.0
    width = exact_half_width(multiplier, theta)
    intervals = [
        (math.log(u / v) - width, math.log(u / v) + width)
        for u, v in pairs
    ]
    return interval_union_length(intervals)


def leading_union_length(multiplier: int, theta: float) -> float:
    nu = len(same_parity_factor_pairs(multiplier))
    return 4.0 * math.sqrt(2.0 * theta) * nu * multiplier ** (-0.25)


def rows() -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for theta in THETAS:
        relative_errors: list[float] = []
        live = 0
        for multiplier in range(1, MAX_MULTIPLIER + 1):
            lead = leading_union_length(multiplier, theta)
            if lead == 0.0:
                continue
            live += 1
            exact = exact_union_length(multiplier, theta)
            relative_errors.append(abs(exact / lead - 1.0))
        output.append(
            {
                "theta": theta,
                "live_multipliers": live,
                "max_relative_error": max(relative_errors),
                "mean_relative_error": sum(relative_errors) / len(relative_errors),
            }
        )
    return output


def write_csv(path: str | Path) -> None:
    data = rows()
    output = Path(path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    target = (
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_horizontal_vertical_coverage_bridge_20260907.csv"
    )
    write_csv(target)
    print(target)
