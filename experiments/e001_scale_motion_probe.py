"""E001.9 deterministic probe of scale-dependent endpoint hard exclusion.

This is an engineering toy-policy experiment, not a physical rebound law.
It demonstrates that coarse endpoint-collapse constraints can disappear under
spatial refinement, while primitive transition-aware constraints may persist.
"""

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_action_constraints import maximum_constraint_solutions
from enterprise_math.motion_collapse import BodyMotion2D
from enterprise_math.scale_motion_constraints import (
    sampled_endpoint_macro_constraints,
    transition_aware_macro_constraints,
)


def show(label, motions, factors):
    print(label)
    for factor in factors:
        try:
            static = sampled_endpoint_macro_constraints(motions, factor).constraints
            static_solutions = maximum_constraint_solutions(static)
        except ValueError:
            static = None
            static_solutions = "CURRENT_MACRO_CONTACT_REPAIR_REQUIRED"

        try:
            aware = transition_aware_macro_constraints(motions, factor).constraints
            aware_solutions = maximum_constraint_solutions(aware)
        except ValueError:
            aware = None
            aware_solutions = "CURRENT_MACRO_CONTACT_REPAIR_REQUIRED"

        print(f"d={factor}")
        print(f"  static_constraints={static}")
        print(f"  static_max_move_sets={static_solutions}")
        print(f"  transition_aware_constraints={aware}")
        print(f"  transition_aware_max_move_sets={aware_solutions}")


def main() -> None:
    approach = [
        BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
        BodyMotion2D(Body2D(1, 3, 0, 0), (-1, 0)),
    ]
    show("approach 0->1 and 3->2", approach, (3, 2, 1))

    swap = [
        BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
        BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
    ]
    show("point swap 0<->1", swap, (2, 1))


if __name__ == "__main__":
    main()
