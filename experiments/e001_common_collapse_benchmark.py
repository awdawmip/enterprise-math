"""E001.1 smoke benchmark for exact collision via shared terminal collapse targets."""

from time import perf_counter

from enterprise_math.common_collapse import common_collapse_pairs
from enterprise_math.engineering_collision import (
    Body2D,
    broad_phase_candidates,
    exact_collision,
)


def build_field(side: int = 80) -> list[Body2D]:
    bodies: list[Body2D] = []
    body_id = 0
    for y in range(side):
        for x in range(side):
            bodies.append(Body2D(body_id, 11 * x + (y % 5), 11 * y + (x % 3), 1))
            body_id += 1
    for x, y in ((30, 30), (31, 31), (300, 220), (301, 221), (-8, -8), (-7, -7)):
        bodies.append(Body2D(body_id, x, y, 1))
        body_id += 1
    return bodies


def main() -> None:
    bodies = build_field()
    by_id = {body.body_id: body for body in bodies}
    target_emissions = sum((2 * body.radius + 1) ** 2 for body in bodies)

    start = perf_counter()
    common_pairs = common_collapse_pairs(bodies)
    common_seconds = perf_counter() - start

    start = perf_counter()
    candidates = broad_phase_candidates(bodies, 64)
    fixed_pairs = tuple(
        pair
        for pair in candidates
        if exact_collision(by_id[pair[0]], by_id[pair[1]])
    )
    fixed_seconds = perf_counter() - start

    if common_pairs != fixed_pairs:
        raise SystemExit("E001.1 common-collapse result disagrees with exact terminal collision")

    print(f"bodies={len(bodies)}")
    print(f"collapse_target_emissions={target_emissions}")
    print(f"broad_phase_candidates={len(candidates)}")
    print(f"collisions={len(common_pairs)}")
    print(f"common_collapse_seconds={common_seconds:.6f}")
    print(f"fixed_bucket_plus_terminal_seconds={fixed_seconds:.6f}")


if __name__ == "__main__":
    main()
