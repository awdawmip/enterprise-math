"""E001.2 structural benchmark for terminal incidence vs multiscale collapse."""

from enterprise_math.collapse_incidence import collapse_incidence_report
from enterprise_math.engineering_collision import Body2D, exact_collision_pairs
from enterprise_math.multiscale_collapse import multiscale_common_collapse


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


def main() -> None:
    small = build_small_field()
    incidence = collapse_incidence_report(small)
    small_tree = multiscale_common_collapse(small, (64, 32, 16, 8, 4, 2, 1))
    if incidence.collision_pairs != small_tree.collision_pairs:
        raise SystemExit("E001.2 small-field incidence/tree differential validation failed")

    print("[small-target field]")
    print(f"bodies={len(small)}")
    print(f"possible_pairs={small_tree.possible_pairs}")
    print(f"terminal_incidence_memberships={incidence.emitted_memberships}")
    print(f"multiscale_memberships={small_tree.emitted_memberships}")
    print(f"visited_shared_cells={small_tree.visited_shared_cells}")
    print(f"collisions={len(small_tree.collision_pairs)}")
    print(f"decisions_by_cell_size={small_tree.decisions_by_cell_size}")
    print(f"collapse_overlap_spectrum={incidence.overlap_spectrum}")

    large = build_large_domain_field()
    large_tree = multiscale_common_collapse(
        large, (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1)
    )
    oracle = exact_collision_pairs(large)
    if large_tree.collision_pairs != oracle:
        raise SystemExit("E001.2 large-domain tree disagrees with exact terminal collision")
    terminal_memberships = sum((2 * body.radius + 1) ** 2 for body in large)

    print("[large-target field]")
    print(f"bodies={len(large)}")
    print(f"possible_pairs={large_tree.possible_pairs}")
    print(f"hypothetical_terminal_memberships={terminal_memberships}")
    print(f"multiscale_memberships={large_tree.emitted_memberships}")
    print(f"visited_shared_cells={large_tree.visited_shared_cells}")
    print(f"collisions={len(large_tree.collision_pairs)}")
    print(f"decisions_by_cell_size={large_tree.decisions_by_cell_size}")


if __name__ == "__main__":
    main()
