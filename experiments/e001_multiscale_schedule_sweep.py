"""E001.2 deterministic schedule sweep: semantics fixed, acceleration work variable."""

from enterprise_math.engineering_collision import Body2D
from enterprise_math.multiscale_collapse import multiscale_common_collapse


def powers_to_one(start: int) -> tuple[int, ...]:
    values = []
    value = start
    while value >= 1:
        values.append(value)
        value //= 2
    return tuple(values)


def build_small_field(side: int = 80) -> list[Body2D]:
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


def build_large_domain_field(side: int = 20) -> list[Body2D]:
    bodies: list[Body2D] = []
    body_id = 0
    radius = 128
    for y in range(side):
        for x in range(side):
            bodies.append(
                Body2D(
                    body_id,
                    300 * x + (y % 3) * 7,
                    300 * y + (x % 2) * 5,
                    radius,
                )
            )
            body_id += 1
    bodies.append(Body2D(body_id, 150, 150, radius))
    body_id += 1
    bodies.append(Body2D(body_id, 200, 200, radius))
    return bodies


def sweep(name: str, bodies: list[Body2D], starts: tuple[int, ...]) -> None:
    expected = None
    print(f"[{name}]")
    for start in starts:
        report = multiscale_common_collapse(bodies, powers_to_one(start))
        if expected is None:
            expected = report.collision_pairs
        elif report.collision_pairs != expected:
            raise SystemExit("collision semantics changed with acceleration schedule")
        print(
            f"start={start} memberships={report.emitted_memberships} "
            f"shared_cells={report.visited_shared_cells} "
            f"collisions={len(report.collision_pairs)}"
        )


def main() -> None:
    sweep("small-target", build_small_field(), (2, 4, 8, 16, 32, 64, 128))
    sweep("large-target", build_large_domain_field(), (128, 256, 512, 1024))


if __name__ == "__main__":
    main()
