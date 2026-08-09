"""E001.4 deterministic probe for finite contact, response, and primitive motion.

This experiment is intentionally small and auditable.  It demonstrates four
separate facts without assigning physical force/energy semantics:

1. overlap witness width is not a de-overlap distance under containment;
2. geometry-only pair response can remain genuinely set-valued under symmetry;
3. transition conflicts need edge targets in addition to final-state vertices;
4. the same proposed pair-conflict graph can have different future admission
   capacity, so the pair graph alone is not a future-sufficient response state.
"""

from enterprise_math.collapse_contact import collapse_contact_profile
from enterprise_math.collapse_response import balanced_pair_responses
from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_collapse import (
    BodyMotion2D,
    maximum_conflict_free_move_sets,
    maximum_conflict_free_outcomes,
    motion_conflict_pairs,
    motion_conflict_witnesses,
)


def main() -> None:
    outer = Body2D(0, 0, 0, 5)
    inner = Body2D(1, 0, 0, 1)
    contact = collapse_contact_profile(outer, inner)
    if contact is None:
        raise SystemExit("containment contact unexpectedly vanished")
    print("containment")
    print(f"shared_axis_counts={(contact.x_count, contact.y_count)}")
    print(f"shared_target_count={contact.shared_target_count}")
    print(f"minimum_separation_steps={contact.minimum_axis_separation_steps}")
    print(f"minimum_relative_corrections={contact.minimum_relative_corrections}")

    coincident_left = Body2D(0, 0, 0, 1)
    coincident_right = Body2D(1, 0, 0, 1)
    responses = balanced_pair_responses(coincident_left, coincident_right)
    print("coincident_response")
    print(f"balanced_response_count={len(responses)}")
    print(
        "balanced_relative_deltas="
        f"{tuple(sorted({response.relative_delta for response in responses}))}"
    )

    head_on = [
        BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
        BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
    ]
    converge = [
        BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0)),
        BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
    ]

    print("head_on")
    print(f"conflict_pairs={motion_conflict_pairs(head_on)}")
    print(
        "shared_transition_targets="
        f"{tuple(sorted(motion_conflict_witnesses(head_on[0], head_on[1]), key=repr))}"
    )
    print(f"maximum_move_sets={maximum_conflict_free_move_sets(head_on)}")
    print(f"after_states={maximum_conflict_free_outcomes(head_on)}")

    print("converge")
    print(f"conflict_pairs={motion_conflict_pairs(converge)}")
    print(
        "shared_transition_targets="
        f"{tuple(sorted(motion_conflict_witnesses(converge[0], converge[1]), key=repr))}"
    )
    print(f"maximum_move_sets={maximum_conflict_free_move_sets(converge)}")
    print(f"after_states={maximum_conflict_free_outcomes(converge)}")

    if motion_conflict_pairs(head_on) != motion_conflict_pairs(converge):
        raise SystemExit("probe expected identical proposed pair-conflict graphs")
    if maximum_conflict_free_move_sets(head_on) == maximum_conflict_free_move_sets(converge):
        raise SystemExit("probe failed to expose future-sufficiency counterexample")


if __name__ == "__main__":
    main()
