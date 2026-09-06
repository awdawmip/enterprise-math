#!/usr/bin/env python3
"""Exact finite checker for the X6 concrete-path dagger-category correction and
truncated noncommutative tensor path jets.

Main finite theorem on one shortest six-edge triadic frame cycle:
  order 1 jet -> 1 class
  order 2 jet -> 27 classes
  order 3 jet -> 64 classes (lossless on all branch words)

The order-2 quotient remembers only the OUTER counts on the three antipodal
macro-edge pairs.  Order 3 is the first lossless jet order on this population.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRIAD_PATH = (
    ROOT
    / "experiments"
    / "x6_triadic_rotation_v1_20260906"
    / "check_triadic_rotation.py"
)
spec = spec_from_file_location("x6_triadic_rotation_v1", TRIAD_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load existing triadic rotation checker")
tri = module_from_spec(spec)
spec.loader.exec_module(tri)

DIM = tri.N
INNER = 0
OUTER = 1


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def kron(a, b):
    return tuple(x * y for x in a for y in b)


def tensor_index(indices):
    out = 0
    for index in indices:
        out = DIM * out + index
    return out


def reverse_tensor_factors(tensor, degree):
    if degree <= 1:
        return tensor
    out = [0] * len(tensor)
    for indices in product(range(DIM), repeat=degree):
        src = tensor_index(indices)
        dst = tensor_index(tuple(reversed(indices)))
        out[dst] = tensor[src]
    return tuple(out)


def path_jet(steps, order=3):
    """S_k=sum_{r1<...<rk} s_r1 tensor ... tensor s_rk, S_0=1."""
    levels = [(1,)]
    for degree in range(1, order + 1):
        levels.append((0,) * (DIM**degree))

    # Descending update makes each primitive step appear at most once in each
    # strictly increasing subsequence.
    for step in steps:
        for degree in range(order, 0, -1):
            levels[degree] = tadd(
                levels[degree], kron(levels[degree - 1], step)
            )
    return tuple(levels)


def jet_product(left, right, order=3):
    out = [(1,)]
    for degree in range(1, order + 1):
        value = (0,) * (DIM**degree)
        for p in range(degree + 1):
            q = degree - p
            value = tadd(value, kron(left[p], right[q]))
        out.append(value)
    return tuple(out)


def reverse_steps(steps):
    return tuple(tuple(-x for x in step) for step in reversed(steps))


def phases_for(S):
    q = tri.q_triad(S)
    phases = [tri.unit(S[0])]
    for _ in range(5):
        phases.append(tri.act(q, phases[-1]))
    assert tri.act(q, phases[-1]) == phases[0]
    return tuple(phases)


def branch_steps(a, b, bit):
    minus_a = tuple(-x for x in a)
    if bit == INNER:
        return (minus_a, b)       # a -> 0 -> b
    return (b, minus_a)           # a -> a+b -> b


def cycle_steps(S, word):
    phases = phases_for(S)
    out = []
    for r, bit in enumerate(word):
        out.extend(branch_steps(phases[r], phases[(r + 1) % 6], bit))
    return tuple(out)


def jet_key(steps, order):
    jet = path_jet(steps, order)
    return tuple(jet[k] for k in range(1, order + 1))


def permutation_sign(p):
    inversions = sum(
        p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))
    )
    return -1 if inversions % 2 else 1


def determinant(matrix):
    n = len(matrix)
    total = 0
    for p in permutations(range(n)):
        term = permutation_sign(p)
        for row in range(n):
            term *= matrix[row][p[row]]
        total += term
    return total


def check_concrete_paths_are_dagger_category_not_raw_groupoid():
    S = (0, 1, 2)
    phases = phases_for(S)
    gamma = branch_steps(phases[0], phases[1], OUTER)
    dagger = reverse_steps(gamma)
    retrace = gamma + dagger

    assert len(gamma) == 2
    assert len(retrace) == 4
    assert retrace != ()

    # Raw concatenation therefore does not make dagger a categorical inverse:
    # gamma ; gamma^dagger is a nonempty concrete path, not the empty identity.
    assert gamma + dagger != ()

    # Dagger is nevertheless an exact involution.
    assert reverse_steps(dagger) == gamma


def check_jet_composition_and_dagger():
    words = tuple(product((INNER, OUTER), repeat=6))
    S = (0, 1, 2)
    for word in words:
        steps = cycle_steps(S, word)
        whole = path_jet(steps, 3)

        for cut in range(len(steps) + 1):
            left = path_jet(steps[:cut], 3)
            right = path_jet(steps[cut:], 3)
            assert jet_product(left, right, 3) == whole

        rev = path_jet(reverse_steps(steps), 3)
        for degree in range(1, 4):
            expected = tuple(
                ((-1) ** degree) * x
                for x in reverse_tensor_factors(whole[degree], degree)
            )
            assert rev[degree] == expected


def check_first_lossless_order_all_20():
    words = tuple(product((INNER, OUTER), repeat=6))
    expected_counts = {1: 1, 2: 27, 3: 64}

    for S in combinations(range(DIM), 3):
        for order, expected in expected_counts.items():
            classes = {
                jet_key(cycle_steps(S, word), order)
                for word in words
            }
            assert len(classes) == expected


def check_order2_is_exact_antipodal_pair_count_quotient():
    S = (0, 1, 2)
    words = tuple(product((INNER, OUTER), repeat=6))
    by_counts = {}
    by_s2 = {}

    for word in words:
        counts = (word[0] + word[3], word[1] + word[4], word[2] + word[5])
        s2 = path_jet(cycle_steps(S, word), 2)[2]
        by_counts.setdefault(counts, set()).add(s2)
        by_s2.setdefault(s2, set()).add(counts)

    assert len(by_counts) == 27
    assert len(by_s2) == 27
    assert all(len(values) == 1 for values in by_counts.values())
    assert all(len(values) == 1 for values in by_s2.values())

    # Matched-fiber witness: one OUTER on edge 0 vs its antipodal edge 3.
    w0 = (OUTER, INNER, INNER, INNER, INNER, INNER)
    w3 = (INNER, INNER, INNER, OUTER, INNER, INNER)
    j0_2 = path_jet(cycle_steps(S, w0), 2)
    j3_2 = path_jet(cycle_steps(S, w3), 2)
    assert j0_2[1] == j3_2[1]
    assert j0_2[2] == j3_2[2]
    assert path_jet(cycle_steps(S, w0), 3)[3] != path_jet(cycle_steps(S, w3), 3)[3]


def check_order3_linear_independence_certificate():
    # S3 is affine-linear in the six branch bits because each macro block has
    # only two primitive steps.  Use six explicit tensor coordinates to show
    # the six single-bit contribution vectors have nonzero determinant.
    S = (0, 1, 2)
    baseline_word = (INNER,) * 6
    baseline_s3 = path_jet(cycle_steps(S, baseline_word), 3)[3]

    contributions = []
    for r in range(6):
        word = [INNER] * 6
        word[r] = OUTER
        s3 = path_jet(cycle_steps(S, tuple(word)), 3)[3]
        contributions.append(tsub(s3, baseline_s3))

    coordinates = (
        (0, 0, 1),
        (0, 0, 2),
        (0, 1, 0),
        (0, 1, 2),
        (0, 2, 0),
        (1, 1, 2),
    )
    matrix = [
        [contributions[column][tensor_index(indices)] for column in range(6)]
        for indices in coordinates
    ]
    assert determinant(matrix) == 8


def check_inner_outer_and_loop_signatures():
    S = (0, 1, 2)
    phases = phases_for(S)

    inner = branch_steps(phases[0], phases[1], INNER)
    outer = branch_steps(phases[0], phases[1], OUTER)
    ji = path_jet(inner, 2)
    jo = path_jet(outer, 2)
    assert ji[1] == jo[1]
    assert ji[2] != jo[2]

    # Exact retracing is still nonempty in the concrete path category.  Even
    # if an antisymmetric area projection cancels, the full tensor jet plus
    # path grade can distinguish it from the empty path.
    retrace = outer + reverse_steps(outer)
    assert len(retrace) == 4
    jr = path_jet(retrace, 3)
    je = path_jet((), 3)
    assert jr != je


def main():
    check_concrete_paths_are_dagger_category_not_raw_groupoid()
    check_jet_composition_and_dagger()
    check_first_lossless_order_all_20()
    check_order2_is_exact_antipodal_pair_count_quotient()
    check_order3_linear_independence_certificate()
    check_inner_outer_and_loop_signatures()

    print("PASS: X6 concrete-path tensor jet")
    print("source_type", "FREE PATH CATEGORY WITH DAGGER, NOT RAW CONCATENATION GROUPOID")
    print("Q_cycle_branch_words", 64)
    print("jet_order_1_classes", 1)
    print("jet_order_2_classes", 27)
    print("jet_order_3_classes", 64)
    print("order2_exact_state", "three antipodal OUTER counts in {0,1,2}^3")
    print("order3_single-bit_certificate_det", 8)
    print("first_lossless_jet_order_on_shortest_Q_cycle", 3)


if __name__ == "__main__":
    main()
