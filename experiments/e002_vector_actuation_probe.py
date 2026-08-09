#!/usr/bin/env python3
"""Deterministic E002 vector-actuation pressure probe."""

from enterprise_math.precision_vector_actuation import (
    reachable_vector_residues,
    reachable_vector_subgroup,
    single_vector_action_horizon_class_count,
    single_vector_action_subgroup_order,
    vector_correlation_expansion_factor,
    vector_horizon_class_count,
    vector_stable_class_count,
    vector_stable_widths,
)


def main() -> None:
    widths = (3, 3)
    diagonal = ((1, 1),)
    print(f"widths={widths}")
    print(f"actions={diagonal}")
    print(f"h2_residue_vectors={reachable_vector_residues(widths, diagonal, 2)}")
    print(f"h2_residue_count={len(reachable_vector_residues(widths, diagonal, 2))}")
    print(f"h2_future_classes={vector_horizon_class_count(widths, diagonal, 2)}")
    print(f"stable_subgroup_size={len(reachable_vector_subgroup(widths, diagonal))}")
    print(f"stable_future_classes={vector_stable_class_count(widths, diagonal)}")
    print(f"correlation_expansion={vector_correlation_expansion_factor(widths, diagonal)}")

    widths3 = (5, 5, 5)
    action3 = (1, 1, 1)
    print(f"widths3={widths3}")
    print(f"action3={action3}")
    print(
        "horizon_classes3="
        + str(
            tuple(
                single_vector_action_horizon_class_count(widths3, action3, horizon)
                for horizon in range(6)
            )
        )
    )
    print(f"subgroup_order3={single_vector_action_subgroup_order(widths3, action3)}")
    print(f"stable_classes3={vector_stable_class_count(widths3, (action3,))}")
    print(f"correlation_expansion3={vector_correlation_expansion_factor(widths3, (action3,))}")

    mixed_widths = (9, 15)
    mixed_actions = ((6, 10), (12, -5))
    print(f"mixed_widths={mixed_widths}")
    print(f"mixed_actions={mixed_actions}")
    print(f"mixed_stable_widths={vector_stable_widths(mixed_widths, mixed_actions)}")
    print(f"mixed_stable_classes={vector_stable_class_count(mixed_widths, mixed_actions)}")
    print(f"mixed_subgroup_size={len(reachable_vector_subgroup(mixed_widths, mixed_actions))}")
    print(f"mixed_correlation_expansion={vector_correlation_expansion_factor(mixed_widths, mixed_actions)}")


if __name__ == "__main__":
    main()
