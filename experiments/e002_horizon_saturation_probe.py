#!/usr/bin/env python3
"""Deterministic E002 stage-3 probe for finite horizon and saturation."""

from enterprise_math.precision_horizon_saturation import (
    finite_horizon_class_count,
    horizon_stabilization_depth,
    reachable_action_residues,
    saturation_range_collapses,
    saturated_translation_descends,
    single_action_horizon_class_count,
)
from enterprise_math.precision_locked_actuation import precision_cell_width


def main() -> None:
    precision = 8
    width = precision_cell_width(precision)
    print(f"precision={precision}")
    print(f"cell_width={width}")

    single = (6,)
    print(f"single_action={single}")
    print(
        "single_counts="
        + str(
            tuple(
                single_action_horizon_class_count(precision, single[0], horizon)
                for horizon in range(8)
            )
        )
    )

    families = ((6, 10), (4, 6, 8), (-6, 9, 12))
    for actions in families:
        counts = tuple(
            finite_horizon_class_count(precision, actions, horizon)
            for horizon in range(8)
        )
        print(f"actions={actions}")
        print(f"class_counts={counts}")
        print(f"stabilization_depth={horizon_stabilization_depth(precision, actions)}")
        print(
            "stable_residues="
            + str(
                reachable_action_residues(
                    width,
                    actions,
                    horizon_stabilization_depth(precision, actions),
                )
            )
        )

    aligned_increment = 30
    misaligned_increment = 4
    nontrivial_bounds = (-30, 30)
    one_cell_bounds = (-3, 3)
    print(f"aligned_increment={aligned_increment}")
    print(
        "aligned_nontrivial_saturation_descends="
        + str(
            saturated_translation_descends(
                precision,
                aligned_increment,
                *nontrivial_bounds,
            )
        )
    )
    print(f"misaligned_increment={misaligned_increment}")
    print(
        "misaligned_nontrivial_saturation_descends="
        + str(
            saturated_translation_descends(
                precision,
                misaligned_increment,
                *nontrivial_bounds,
            )
        )
    )
    print(
        "one_cell_saturation_collapses="
        + str(saturation_range_collapses(precision, *one_cell_bounds))
    )
    print(
        "misaligned_one_cell_saturation_descends="
        + str(
            saturated_translation_descends(
                precision,
                misaligned_increment,
                *one_cell_bounds,
            )
        )
    )


if __name__ == "__main__":
    main()
