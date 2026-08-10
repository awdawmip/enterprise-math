"""Two-task scheduling for P017 least-prime and cofactor-root precision.

The conditional asymmetry of L064 does not determine the globally cheaper first
task because the first task itself has a class-count cost.  This module applies
P023-S14 exactly to the two partitions P (least-prime shell) and R (cofactor
root) on one square basin.
"""

from __future__ import annotations

from .p017_directional_root_factor_precision import (
    factor_partition,
    root_factor_tagged_states,
    root_partition,
)
from .precision_incidence_geometry import (
    block_count,
    directed_repair_factor,
    integer_symbol_depth,
    realized_product_class_count,
)


def root_factor_two_task_schedule(k: int, base: int = 2) -> dict[str, int | str]:
    """Return exact costs of P->R and R->P schedules for one square basin."""

    states = root_factor_tagged_states(k)
    factor = factor_partition(states)
    root = root_partition(states)

    factor_classes = block_count(states, factor)
    root_classes = block_count(states, root)
    joint_classes = realized_product_class_count(states, factor, root)

    factor_to_root = directed_repair_factor(states, factor, root)
    root_to_factor = directed_repair_factor(states, root, factor)

    factor_first = integer_symbol_depth(factor_classes, base) + integer_symbol_depth(
        factor_to_root, base
    )
    root_first = integer_symbol_depth(root_classes, base) + integer_symbol_depth(
        root_to_factor, base
    )
    lower_bound = integer_symbol_depth(joint_classes, base)

    if factor_first < root_first:
        preferred = "FACTOR_FIRST"
    elif root_first < factor_first:
        preferred = "ROOT_FIRST"
    else:
        preferred = "TIE"

    return {
        "factor_classes": factor_classes,
        "root_classes": root_classes,
        "joint_classes": joint_classes,
        "factor_to_root_factor": factor_to_root,
        "root_to_factor_factor": root_to_factor,
        "factor_first_depth": factor_first,
        "root_first_depth": root_first,
        "joint_lower_bound_depth": lower_bound,
        "preferred": preferred,
    }
