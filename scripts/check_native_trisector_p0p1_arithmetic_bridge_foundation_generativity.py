#!/usr/bin/env python3
"""Finite regression for the Phase-A C3 selector obstruction.

This checker is not the proof of global definability.  It exhaustively checks the
finite C3 action used by the exact hand proof and bounded canonical-address
regressions for the native origin-norm shell invariant.
"""

from itertools import product

AXES = (0, 1, 2)
ROTATIONS = (0, 1, 2)


def rho_axis(i: int, k: int = 1) -> int:
    return (i + k) % 3


def rho_address(t: tuple[int, int, int], k: int = 1) -> tuple[int, int, int]:
    a, b, c = t
    for _ in range(k % 3):
        a, b, c = c, a, b
    return a, b, c


def main() -> None:
    fixed_axes = [
        i for i in AXES if all(rho_axis(i, k) == i for k in ROTATIONS)
    ]
    assert fixed_axes == [], fixed_axes

    singleton_blocks = [frozenset((i,)) for i in AXES]
    invariant_singletons = [
        block
        for block in singleton_blocks
        if all(
            frozenset(rho_axis(i, k) for i in block) == block
            for k in ROTATIONS
        )
    ]
    assert invariant_singletons == [], invariant_singletons

    full_orbit = frozenset(AXES)
    assert all(
        frozenset(rho_axis(i, k) for i in full_orbit) == full_orbit
        for k in ROTATIONS
    )

    checked = 0
    for t in product(range(7), repeat=3):
        if min(t) != 0:
            continue
        q = sum(x * x for x in t)
        for k in ROTATIONS:
            u = rho_address(t, k)
            assert min(u) == 0
            assert sum(x * x for x in u) == q
        checked += 1

    assert checked == 127
    print(
        "PASS: C3 has no fixed pointed lane; full unpointed orbit is invariant; "
        f"native canonical-address/Q regression checked on {checked} tuples."
    )


if __name__ == "__main__":
    main()
