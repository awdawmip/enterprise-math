#!/usr/bin/env python3
"""Executable pressure tests for QRF-R3 independent foundation verification.

This script is regression evidence only. Infinite claims are proved in the
companion Markdown report.
"""

from itertools import permutations, product


VERTICES = (0, 1, 2)


def rotations(cycle):
    cycle = tuple(cycle)
    return [cycle[i:] + cycle[:i] for i in range(3)]


def orientation_class(cycle):
    """Canonical representative of a cyclic order modulo cyclic rotation."""
    return min(rotations(tuple(cycle)))


def permutation_parity(p):
    inversions = sum(
        p[i] > p[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return 1 if inversions % 2 == 0 else -1


def act_on_orientation(p, orientation):
    return orientation_class(tuple(p[i] for i in orientation))


def directed_edges(orientation):
    orientation = tuple(orientation)
    return tuple(
        (orientation[i], orientation[(i + 1) % 3])
        for i in range(3)
    )


# Abstract triangular carrier presentation:
# e1=(1,0), e2=(0,1), e3=(-1,-1).
# This realizes only the additive carrier relation e1+e2+e3=0.
def phi(z):
    a, b, c = z
    return (a - c, b - c)


def normalize(z):
    m = min(z)
    return tuple(x - m for x in z)


def is_min_zero(z):
    return all(x >= 0 for x in z) and min(z) == 0


def permute_coordinates(p, z):
    return tuple(z[p[i]] for i in range(3))


def complement_min_zero(a):
    """Normal form after reversing all three positive generators."""
    M = max(a)
    return tuple(M - x for x in a)


def main():
    # A. Two cyclic orientations and exact S3/A3 action.
    orientations = sorted(
        {orientation_class(p) for p in permutations(VERTICES)}
    )
    assert len(orientations) == 2
    o0, o1 = orientations

    for p in permutations(VERTICES):
        image0 = act_on_orientation(p, o0)
        image1 = act_on_orientation(p, o1)
        if permutation_parity(p) == 1:
            assert image0 == o0
            assert image1 == o1
        else:
            assert image0 == o1
            assert image1 == o0

    assert not all(
        act_on_orientation(p, o0) == o0
        for p in permutations(VERTICES)
    )
    assert not all(
        act_on_orientation(p, o1) == o1
        for p in permutations(VERTICES)
    )

    # B. Cyclic representative does not choose a base edge.
    base_edge_set = set(directed_edges(o0))
    for representative in rotations(o0):
        assert set(directed_edges(representative)) == base_edge_set

    # The opposite sheet reverses all directed edges.
    reversed_edge_set = {(b, a) for (a, b) in base_edge_set}
    assert set(directed_edges(o1)) == reversed_edge_set

    # D. Min-zero normal form pressure test.
    bound = 5
    representative_count = 0
    for z in product(range(-bound, bound + 1), repeat=3):
        representative_count += 1
        nz = normalize(z)
        assert is_min_zero(nz)
        assert phi(nz) == phi(z)

        # Carrier diagonal shifts leave displacement and normal form unchanged.
        for k in range(-3, 4):
            zk = tuple(x + k for x in z)
            assert phi(zk) == phi(z)
            assert normalize(zk) == nz

    # Bounded uniqueness among valid min-zero addresses.
    seen = {}
    for z in product(range(0, 2 * bound + 2), repeat=3):
        if not is_min_zero(z):
            continue
        displacement = phi(z)
        if displacement in seen:
            assert seen[displacement] == z
        else:
            seen[displacement] = z

    # Gauge equivariance: normalization commutes with coordinate permutation.
    for p in permutations(range(3)):
        for z in product(range(-2, 3), repeat=3):
            lhs = normalize(permute_coordinates(p, z))
            rhs = permute_coordinates(p, normalize(z))
            assert lhs == rhs

    # Native-slice firewall: every nonzero diagonal shift leaves A_E.
    for a in product(range(0, 6), repeat=3):
        if not is_min_zero(a):
            continue
        for k in range(-3, 4):
            if k == 0:
                continue
            shifted = tuple(x + k for x in a)
            assert not is_min_zero(shifted)

    # Switching the same displacement to the globally reversed generator triple
    # yields the complement normal form (up to whichever gauge permutation is used).
    for a in product(range(0, 6), repeat=3):
        if is_min_zero(a):
            assert normalize(tuple(-x for x in a)) == complement_min_zero(a)

    print(
        {
            "orientation_classes": orientations,
            "s3_action_factors_through_parity": True,
            "full_s3_fixed_orientation": False,
            "carrier_representatives_checked": representative_count,
            "bounded_unique_min_zero_displacements": len(seen),
            "coordinate_permutation_equivariance": True,
            "native_diagonal_shift_firewall": True,
            "opposite_orientation_complement_law": True,
        }
    )


if __name__ == "__main__":
    main()
