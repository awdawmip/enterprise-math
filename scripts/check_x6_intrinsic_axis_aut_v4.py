#!/usr/bin/env python3
"""Exact finite checker for intrinsic axis S4 and face companion matching."""
from itertools import combinations, permutations

ZERO = (0, 0, 0)
T = (0, 0, 1)
AXES = (
    (1, 0, 0),
    (0, 1, 0),
    (-1, -1, 0),
    (-1, -1, 1),
    (0, 1, 1),
    (1, 0, 1),
)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1], (x[2] + y[2]) & 1)


def sum_axes(indices):
    out = ZERO
    for i in indices:
        out = add(out, AXES[i])
    return out


def main():
    triples = tuple(combinations(range(6), 3))
    zero_triples = {frozenset(c) for c in triples if sum_axes(c) == ZERO}
    torsion_triples = {frozenset(c) for c in triples if sum_axes(c) == T}

    assert zero_triples == {
        frozenset((0, 1, 2)),
        frozenset((0, 3, 4)),
        frozenset((1, 3, 5)),
        frozenset((2, 4, 5)),
    }
    assert torsion_triples == {
        frozenset((0, 1, 3)),
        frozenset((0, 2, 4)),
        frozenset((1, 2, 5)),
        frozenset((3, 4, 5)),
    }

    # Any six-axis permutation preserving the intrinsic zero-sum star family is
    # an automorphism of the K4 star hypergraph.  Exactly 24 survive.
    axis_automorphisms = []
    for p in permutations(range(6)):
        image = {frozenset(p[i] for i in tri) for tri in zero_triples}
        if image == zero_triples:
            axis_automorphisms.append(p)
    assert len(axis_automorphisms) == 24

    # The torsion-face family is automatically preserved by the same 24 maps.
    for p in axis_automorphisms:
        image = {frozenset(p[i] for i in tri) for tri in torsion_triples}
        assert image == torsion_triples

    # Unique C2 identification t -> -1 matches every face triangle with the
    # already-derived all-negative chart connection face holonomy.
    def phi(state):
        if state == ZERO:
            return 1
        if state == T:
            return -1
        raise ValueError("phi is defined only on the companion subgroup")

    assert phi(ZERO) == 1
    assert phi(T) == -1
    for face in torsion_triples:
        assert phi(sum_axes(face)) == -1
    for star in zero_triples:
        assert phi(sum_axes(star)) == 1

    print("PASS_X6_INTRINSIC_AXIS_AUT_V4")
    print("zero_sum_star_triples=4")
    print("torsion_face_triples=4")
    print("intrinsic_positive_axis_permutation_automorphisms=24")
    print("axis_automorphism_group=S4")
    print("companion_C2_matches_face_sign_holonomy_C2")


if __name__ == "__main__":
    main()
