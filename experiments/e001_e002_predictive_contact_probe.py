#!/usr/bin/env python3
"""Deterministic E001/E002 Boolean-contact predictive-state probe."""

from enterprise_math.predictive_contact import (
    contact_horizon_class_count,
    separated_shell_horizon_class_count,
    stable_contact_class_count,
    stable_separated_shell_class_count,
)


def main() -> None:
    precision = 15
    step = 4
    print(f"contact_precision={precision}")
    print(f"separating_or_closing_step={step}")
    print(
        "contact_horizon_classes="
        + str(tuple(contact_horizon_class_count(precision, step, h) for h in range(8)))
    )
    print(f"contact_stable_classes={stable_contact_class_count(precision, step)}")
    print(f"contact_fine_gap_states={precision}")

    shell_width = 17
    print(f"separated_shell_width={shell_width}")
    print(
        "separated_horizon_classes="
        + str(
            tuple(
                separated_shell_horizon_class_count(shell_width, step, h)
                for h in range(8)
            )
        )
    )
    print(
        "separated_stable_classes="
        + str(stable_separated_shell_class_count(shell_width, step))
    )
    print(f"separated_fine_gap_states={shell_width}")


if __name__ == "__main__":
    main()
