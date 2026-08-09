#!/usr/bin/env python3
"""Deterministic E002 stage-2 probe for actuation/precision compatibility."""

from __future__ import annotations

from itertools import product

from enterprise_math.precision_locked_actuation import (
    admissible_precision_widths,
    centered_precision_state,
    precision_cell_width,
    shared_exact_action_unit,
    stable_action_cell_width,
    stable_action_precision,
)


def future_q_signature(error: int, precision: int, word: tuple[int, ...]) -> tuple[int, ...]:
    values = [centered_precision_state(error, precision).quotient]
    current = error
    for action in word:
        current += action
        values.append(centered_precision_state(current, precision).quotient)
    return tuple(values)


def cell_signature_count(
    precision: int,
    actions: tuple[int, ...],
    horizon: int,
) -> int:
    width = precision_cell_width(precision)
    center = (width - 1) // 2
    errors = tuple(detail - center for detail in range(width))
    signatures = set()
    for error in errors:
        per_state = tuple(
            future_q_signature(error, precision, word)
            for word in product(actions, repeat=horizon)
        )
        signatures.add(per_state)
    return len(signatures)


def main() -> None:
    precision = 8
    width = precision_cell_width(precision)
    scenarios = (
        ("matched", (-30, 0, 45, 60)),
        ("partial", (-6, 0, 9, 12)),
        ("coprime", (-4, 0, 6, 8)),
    )

    print(f"precision={precision}")
    print(f"cell_width={width}")
    for name, actions in scenarios:
        stable_width = stable_action_cell_width(precision, actions)
        repair_classes = width // stable_width
        print(f"scenario={name}")
        print(f"actions={actions}")
        print(f"stable_width={stable_width}")
        print(f"stable_precision={stable_action_precision(precision, actions)}")
        print(f"repair_classes={repair_classes}")
        print(f"horizon3_distinguishable_classes={cell_signature_count(precision, actions, 3)}")

    requested_precisions = (2, 3, 4)
    print(f"adaptive_precisions={requested_precisions}")
    print(f"adaptive_widths={tuple(precision_cell_width(p) for p in requested_precisions)}")
    print(f"minimum_shared_exact_action={shared_exact_action_unit(requested_precisions)}")

    action_family = (90, -150, 210)
    print(f"action_family={action_family}")
    print(f"admissible_widths={admissible_precision_widths(action_family)}")


if __name__ == "__main__":
    main()
