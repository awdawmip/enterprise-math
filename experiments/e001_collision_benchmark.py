"""Deterministic E001 engineering smoke benchmark (integer state only)."""

from enterprise_math.engineering_collision import Body2D, exact_collision_pairs, run_collision_engine


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
    schedule = (64, 32, 16, 8, 4, 2, 1)
    report = run_collision_engine(bodies, schedule)
    oracle = exact_collision_pairs(bodies)
    if report.collision_pairs != oracle:
        raise SystemExit("E001 differential validation failed")
    print(f"bodies={report.body_count}")
    print(f"possible_pairs={report.possible_pairs}")
    print(f"broad_phase_candidates={report.candidate_pairs}")
    print(f"precision_observations={report.precision_observations}")
    print(f"fixed_terminal_checks={report.candidate_pairs}")
    print(f"adaptive_terminal_checks={report.terminal_checks}")
    print(f"terminal_checks_avoided={report.candidate_pairs - report.terminal_checks}")
    print(f"collisions={len(report.collision_pairs)}")
    print(f"decisions_by_cell_size={report.decisions_by_cell_size}")


if __name__ == "__main__":
    main()
