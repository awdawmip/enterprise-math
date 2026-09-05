#!/usr/bin/env python3
"""Regression checker for the reusable X6 universal Cell prototype."""
from itertools import permutations, product

from x6_cell import (
    COMPANION,
    EDGE_NAMES,
    ORIGIN_CELL,
    VERTEX_NAMES,
    CellState,
    axis_generator,
    change_slice_chart,
    endpoint_from_exponents,
    from_slice_chart,
    return_certificate,
    rotate_state,
    slice_address,
    slice_sheet_bit,
    step,
)


def main():
    checks = 0

    # Immediate reversal and 12 distinct directed neighbours.
    neighbours = set()
    for axis in EDGE_NAMES:
        forward = step(ORIGIN_CELL, axis, +1)
        backward = step(ORIGIN_CELL, axis, -1)
        assert step(forward, axis, -1) == ORIGIN_CELL
        assert step(backward, axis, +1) == ORIGIN_CELL
        neighbours.add(forward)
        neighbours.add(backward)
        checks += 4
    assert len(neighbours) == 12
    checks += 1

    # Four local star loops close at the Cell endpoint; the four face triangles
    # reach the same nonzero order-two companion.
    star_words = (
        ("AB", "AC", "AD"),
        ("AB", "BC", "BD"),
        ("AC", "BC", "CD"),
        ("AD", "BD", "CD"),
    )
    face_words = (
        ("BC", "BD", "CD"),
        ("AC", "AD", "CD"),
        ("AB", "AD", "BD"),
        ("AB", "AC", "BC"),
    )
    for word in star_words:
        state = ORIGIN_CELL
        for axis in word:
            state = step(state, axis)
        assert state == ORIGIN_CELL
        checks += 1
    for word in face_words:
        state = ORIGIN_CELL
        for axis in word:
            state = step(state, axis)
        assert state == COMPANION
        assert state.then_displacement(COMPANION) == ORIGIN_CELL
        checks += 2

    # Every full state in a large exact box is losslessly encoded by any one
    # existing-style min-zero three-axis address plus one binary sheet bit.
    for u in range(-12, 13):
        for v in range(-12, 13):
            for sheet in (0, 1):
                state = CellState(u, v, sheet)
                for source in VERTEX_NAMES:
                    address = slice_address(state, source)
                    bit = slice_sheet_bit(state, source)
                    assert from_slice_chart(source, address, bit) == state
                    checks += 1
                    for target in VERTEX_NAMES:
                        target_address, target_bit = change_slice_chart(source, address, bit, target)
                        assert from_slice_chart(target, target_address, target_bit) == state
                        checks += 1

    # S4 rotations preserve endpoint structure and the unique companion.
    perms = tuple(permutations(range(4)))
    probes = (
        ORIGIN_CELL,
        COMPANION,
        CellState(3, -5, 0),
        CellState(-7, 4, 1),
    )
    for perm in perms:
        assert rotate_state(COMPANION, perm) == COMPANION
        checks += 1
        for probe in probes:
            # A permutation followed by its inverse recovers the state.
            inv = tuple(perm.index(i) for i in range(4))
            assert rotate_state(rotate_state(probe, perm), inv) == probe
            checks += 1

    # Exact return criterion on the complete [-2,2]^6 box.
    returns = 0
    for z in product(range(-2, 3), repeat=6):
        is_return = endpoint_from_exponents(z) == ORIGIN_CELL
        assert is_return == return_certificate(z)
        returns += int(is_return)
        checks += 1
    assert returns == 165
    checks += 1

    # Opposite-axis doubled traces have the same endpoint but remain different
    # component traces, so endpoint quotient must not replace Path-formal BRC.
    assert endpoint_from_exponents((2, 0, 0, 0, 0, 0)) == endpoint_from_exponents((0, 0, 0, 0, 0, 2))
    checks += 1

    # The older context-dependent four-step candidate loop is NOT forced by the
    # accepted shared-axis endpoint relations.  Its net trace is -2*AC.
    old_context_loop = (0, -2, 0, 0, 0, 0)
    assert endpoint_from_exponents(old_context_loop) != ORIGIN_CELL
    checks += 1

    print("PASS_X6_CELL_MODULE_V2")
    print("checks=", checks)
    print("return_vectors_in_box=", returns)
    print("chart_roundtrip=ONE_SLICE_MINZERO_ADDRESS_PLUS_ONE_BIT")
    print("old_context_four_step_loop=NOT_FORCED_RETURN")


if __name__ == "__main__":
    main()
