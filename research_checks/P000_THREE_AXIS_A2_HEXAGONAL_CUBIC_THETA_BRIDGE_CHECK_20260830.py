#!/usr/bin/env python3
"""Exact Gate-0 regression for the P000 three-axis A2/cubic-theta bridge.

This checker deliberately stops before any A2/theta matching.  It verifies that
the diagonal/common-mode quotient preserves differences but does not preserve the
retained PF-10 ingress triple on the declared J_A={E1,E2,E3} slice.
"""
from itertools import product

J_A = ("E1", "E2", "E3")


def difference_readout(triple):
    x, y, z = triple
    return (x - y, y - z, z - x)


def diagonal_translate(triple, t):
    return tuple(value + t for value in triple)


def a_pushforward(triple):
    # a_xi=(E1 E2 E3).  Push values forward along axis labels.
    x, y, z = triple
    return (z, x, y)


def main():
    checks = 0

    # Exact algebraic regressions over a finite integer window.
    for triple in product(range(-3, 4), repeat=3):
        u, v, w = difference_readout(triple)
        assert u + v + w == 0
        checks += 1

        for t in range(-3, 4):
            assert difference_readout(diagonal_translate(triple, t)) == (u, v, w)
            checks += 1

        # The frozen a_xi cycle acts compatibly on the difference readout.
        assert difference_readout(a_pushforward(triple)) == (w, u, v)
        checks += 1

    # Fiber theorem regression: equal full difference readout iff the two
    # integer triples differ by one common diagonal translation.
    sample = list(product(range(-2, 3), repeat=3))
    for left in sample:
        for right in sample:
            if difference_readout(left) == difference_readout(right):
                delta = tuple(right[i] - left[i] for i in range(3))
                assert delta[0] == delta[1] == delta[2]
                checks += 1

    # Minimal retained-observable obstruction.
    p = (1, 1, 1)
    q = (2, 2, 2)
    assert difference_readout(p) == difference_readout(q) == (0, 0, 0)
    assert p != q  # full PF-10 ingress restriction distinguishes the states
    assert sum(p) != sum(q)  # even the aggregate common mode distinguishes them
    checks += 3

    print("PASS P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_CHECK")
    print(f"checks={checks}")
    print("declared_slice=J_A:{E1,E2,E3}")
    print("difference_readout_diagonal_invariant=true")
    print("difference_fibers=diagonal_translation_orbits")
    print("frozen_a_cycle_difference_equivariant=true")
    print("retained_full_PF10_ingress_constant_on_fibers=false")
    print("gate0=FAIL")
    print("terminal_class=COMMON_MODE_QUOTIENT_NOT_DERIVED")
    print("gate1_attempted=false")


if __name__ == "__main__":
    main()
