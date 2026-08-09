#!/usr/bin/env python3
"""Small deterministic probe for P024 lattice-guard precision."""

from enterprise_math.lattice_guard_precision import (
    IntegerGuard,
    classify_projected_action_monoid,
    guard_rank_signature,
    nonnegative_2d_semigroup_contains,
    positive_zero_relation_inverse_words,
    rank_box_sizes,
)


def parity_lattice_probe() -> None:
    guards = (
        IntegerGuard((1, 1), 2),
        IntegerGuard((1, -1), 2),
    )
    actions = ((1, 0),)
    horizon = 2
    sizes = rank_box_sizes(guards, actions, horizon)
    observed = {
        guard_rank_signature((x, y), guards, actions, horizon)
        for x in range(-8, 9)
        for y in range(-8, 9)
    }
    formal = {
        (left, right)
        for left in range(sizes[0])
        for right in range(sizes[1])
    }
    print("parity_formal_classes", len(formal))
    print("parity_realized_classes", len(observed))
    print("parity_missing_classes", sorted(formal - observed))


def directional_probe() -> None:
    actions = ((1, 1), (-1, 1))
    x_type = classify_projected_action_monoid(IntegerGuard((1, 0), 0), actions)
    y_type = classify_projected_action_monoid(IntegerGuard((0, 1), 0), actions)
    print("x_guard_action_type", x_type.kind, x_type.grain, x_type.generators)
    print("y_guard_action_type", y_type.kind, y_type.grain, y_type.generators)


def zero_relation_probe() -> None:
    actions = ((1, 0), (0, 1), (-1, -1))
    words = positive_zero_relation_inverse_words(actions, (1, 1, 1))
    print("positive_zero_inverse_words", words)


def affine_hole_probe() -> None:
    generators = ((2, 0), (0, 1), (1, 1))
    holes = [
        (x, 0)
        for x in range(16)
        if not nonnegative_2d_semigroup_contains((x, 0), generators)
    ]
    conductor_failures = [
        (x, y)
        for x in range(12)
        for y in range(1, 6)
        if not nonnegative_2d_semigroup_contains((x, y), generators)
    ]
    print("sample_boundary_holes", holes)
    print("sample_conductor_translate_failures", conductor_failures)


def main() -> None:
    parity_lattice_probe()
    directional_probe()
    zero_relation_probe()
    affine_hole_probe()


if __name__ == "__main__":
    main()
