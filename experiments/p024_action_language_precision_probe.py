#!/usr/bin/env python3
"""Deterministic P024 action-language precision probe."""

from enterprise_math.action_language_precision import (
    action_grain,
    cyclic_reachable_residues,
    group_completed_window_class_count,
    group_completion_overrefinement_defect,
    numerical_semigroup_profile,
    one_sided_window_class_count,
    positive_semigroup_below,
    relevant_semigroup_holes,
    signed_group_completion_grain,
    threshold_group_coordinate,
)


def main() -> None:
    one_sided = (4, 6)
    width = 7
    profile = numerical_semigroup_profile(one_sided)
    print("one_sided")
    print(f"actions={one_sided}")
    print(f"window_width={width}")
    print(f"reachable_below={positive_semigroup_below(one_sided, width)}")
    print(f"minimal_classes={one_sided_window_class_count(width, one_sided)}")
    print(
        "group_completed_classes="
        f"{group_completed_window_class_count(width, one_sided)}"
    )
    print(f"relevant_holes={relevant_semigroup_holes(width, one_sided)}")
    print(
        "group_completion_defect="
        f"{group_completion_overrefinement_defect(width, one_sided)}"
    )
    print(f"grain={profile.grain}")
    print(f"normalized_generators={profile.normalized_generators}")
    print(f"conductor={profile.conductor}")
    print(f"physical_irregular_depth={profile.physical_irregular_depth}")

    signed = (6, -10)
    grain = signed_group_completion_grain(signed)
    print("\ntwo_sided")
    print(f"actions={signed}")
    print(f"grain={grain}")
    print(
        "coordinates="
        + repr(tuple(threshold_group_coordinate(x, 7, grain) for x in range(0, 15)))
    )

    cyclic_actions = (6,)
    cyclic_width = 15
    print("\ncyclic")
    print(f"width={cyclic_width}")
    print(f"actions={cyclic_actions}")
    print(f"integer_action_grain={action_grain(cyclic_actions)}")
    print(
        "reachable_residues="
        f"{cyclic_reachable_residues(cyclic_width, cyclic_actions)}"
    )


if __name__ == "__main__":
    main()
