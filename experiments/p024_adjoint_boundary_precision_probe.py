#!/usr/bin/env python3
"""Deterministic probe for P024 adjoint boundary pullback."""

from enterprise_math.adjoint_boundary_precision import (
    boundary_orbit,
    dilation_action,
    floor_division_action,
    natural_collapse_action,
    natural_quotient_action,
    natural_root_action,
    stabilize_boundary_orbit,
    translation_action,
)


def foundational_actions() -> None:
    root = natural_root_action(2)
    quotient = natural_quotient_action(3)
    collapse = natural_collapse_action(2)
    print("root_boundary_7", root.pullback_cut(7))
    print("quotient_boundary_7", quotient.pullback_cut(7))
    print("collapse_boundary_7", collapse.pullback_cut(7))
    print("collapse_boundary_9", collapse.pullback_cut(9))


def translation_recovery() -> None:
    actions = (translation_action(-2), translation_action(3))
    print("translation_boundary_orbit_h3", boundary_orbit((0,), actions, 3))


def coarse_fine_reversal() -> None:
    division = floor_division_action(2)
    dilation = dilation_action(2)
    print("floor_division_boundary_orbit_h6", boundary_orbit((1,), (division,), 6))
    stable = stabilize_boundary_orbit((17, -9, 0), (dilation,), 10)
    print("dilation_stabilized", stable.stabilized, stable.horizon)
    print("dilation_boundary_orbit", stable.cuts)


def main() -> None:
    foundational_actions()
    translation_recovery()
    coarse_fine_reversal()


if __name__ == "__main__":
    main()
