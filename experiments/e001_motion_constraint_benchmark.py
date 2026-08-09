"""E001.5 pairwise-vs-target-first binary motion constraint benchmark.

The sparse workload deliberately produces no interactions.  That makes the
engineering question sharp: how much work is spent merely proving that there
are no response constraints?

This script times the direct all-pairs oracle and the action-target inverted
builder, verifies that their exact reports agree, and prints theoretical pair
count plus finite action-target membership count.  Wall time is an engineering
measurement only; no asymptotic/physical claim is inferred from one machine.
"""

from time import perf_counter

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_action_constraints import (
    binary_motion_constraints,
    binary_motion_constraints_target_first,
)
from enterprise_math.motion_collapse import BodyMotion2D, motion_target_set


def build_sparse_field(side: int, spacing: int = 7) -> list[BodyMotion2D]:
    motions: list[BodyMotion2D] = []
    body_id = 0
    for y in range(side):
        for x in range(side):
            motions.append(
                BodyMotion2D(
                    Body2D(body_id, spacing * x, spacing * y, 1),
                    (1, 0),
                )
            )
            body_id += 1
    return motions


def run(side: int) -> None:
    motions = build_sparse_field(side)
    body_count = len(motions)
    possible_pairs = body_count * (body_count - 1) // 2
    action_target_memberships = 0
    for motion in motions:
        action_target_memberships += len(motion_target_set(motion))
        action_target_memberships += len(
            motion_target_set(BodyMotion2D(motion.body, (0, 0)))
        )

    start = perf_counter()
    target_first = binary_motion_constraints_target_first(motions)
    target_seconds = perf_counter() - start

    start = perf_counter()
    pairwise = binary_motion_constraints(motions)
    pairwise_seconds = perf_counter() - start

    if target_first != pairwise:
        raise SystemExit("target-first motion constraints disagree with pairwise oracle")

    print(f"side={side}")
    print(f"bodies={body_count}")
    print(f"possible_pairs={possible_pairs}")
    print(f"action_target_memberships={action_target_memberships}")
    print(f"forced_waits={len(target_first.forced_wait_ids)}")
    print(f"mutex_pairs={len(target_first.mutex_pairs)}")
    print(f"implications={len(target_first.implications)}")
    print(f"target_first_seconds={target_seconds:.6f}")
    print(f"pairwise_seconds={pairwise_seconds:.6f}")


def main() -> None:
    for side in (10, 20, 30):
        run(side)


if __name__ == "__main__":
    main()
