#!/usr/bin/env python3
"""Exact integer checker for the X6 universal Cell completion research candidate.

This checker validates the endpoint algebra only. It does not promote the model to
P000 and it does not quotient Path-formal BRC witnesses.
"""
from itertools import combinations, permutations, product
from math import gcd

VERTICES = tuple(range(4))
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
EDGE_NAMES = ("AB", "AC", "AD", "BC", "BD", "CD")
STARS = {v: tuple(i for i, e in enumerate(EDGES) if v in e) for v in VERTICES}
FACES = {v: tuple(i for i, e in enumerate(EDGES) if v not in e) for v in VERTICES}

# Normal form for G6^cell ~= Z^2 x Z/2.
# State is (u, v, epsilon) with epsilon reduced mod 2.
AXIS = (
    (1, 0, 0),    # AB
    (0, 1, 0),    # AC
    (-1, -1, 0),  # AD
    (-1, -1, 1),  # BC
    (0, 1, 1),    # BD
    (1, 0, 1),    # CD
)
T = (0, 0, 1)
ZERO = (0, 0, 0)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1], (x[2] + y[2]) & 1)


def neg(x):
    return (-x[0], -x[1], x[2] & 1)


def scale(k, x):
    return (k * x[0], k * x[1], (k * x[2]) & 1)


def endpoint(exponents):
    if len(exponents) != 6 or any(type(k) is not int for k in exponents):
        raise ValueError("expected six integer net axis exponents")
    out = ZERO
    for k, g in zip(exponents, AXIS):
        out = add(out, scale(k, g))
    return out


def edge_action(g, i):
    a, b = EDGES[i]
    e = tuple(sorted((g[a], g[b])))
    return EDGE_INDEX[e]


def compose(g, h):
    return tuple(g[h[v]] for v in VERTICES)


def rotate_state(x, g):
    # x = u*AB + v*AC + eps*T.  T is the unique nonzero torsion element.
    image_ab = AXIS[edge_action(g, 0)]
    image_ac = AXIS[edge_action(g, 1)]
    return add(add(scale(x[0], image_ab), scale(x[1], image_ac)), scale(x[2], T))


def slice_parity(x, vertex):
    # lambda_v(generator)=0 on the star of v and 1 on the opposite face.
    la = int(vertex not in EDGES[0])
    lb = int(vertex not in EDGES[1])
    return (x[0] * la + x[1] * lb + x[2]) & 1


def visible_slice_state(x, vertex):
    # Canonical projection to the local slice complement of <T>.
    return add(x, scale(slice_parity(x, vertex), T))


def matching_sums(z):
    return (z[0] + z[5], z[1] + z[4], z[2] + z[3])


def face_parity_abc(z):
    return (z[0] + z[1] + z[3]) & 1


def return_certificate(z):
    s = matching_sums(z)
    return s[0] == s[1] == s[2] and face_parity_abc(z) == 0


def star_coefficients(z):
    """Recover integer star coefficients when the exact return certificate holds."""
    if not return_certificate(z):
        raise ValueError("path does not satisfy the return certificate")
    a, b, c, d, e, f = z
    k_a = (a + b - d) // 2
    k_b = a - k_a
    k_c = b - k_a
    k_d = c - k_a
    ks = (k_a, k_b, k_c, k_d)
    rebuilt = [0] * 6
    for vertex, k in enumerate(ks):
        for i in STARS[vertex]:
            rebuilt[i] += k
    if tuple(rebuilt) != tuple(z):
        raise AssertionError("return certificate reconstruction mismatch")
    return ks


def det_int(mat):
    """Bareiss determinant over Z."""
    n = len(mat)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in mat]
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) // prev
        prev = p
    return sign * a[-1][-1]


def main():
    counts = {
        "star_relations": 0,
        "face_torsion_relations": 0,
        "opposite_edge_relations": 0,
        "s4_axis_checks": 0,
        "s4_composition_checks": 0,
        "slice_projection_checks": 0,
        "visible_kernel_states_checked": 0,
        "return_vectors_checked": 0,
        "return_reconstructions": 0,
        "snf_minor_checks": 0,
        "brc_type_regressions": 0,
    }

    # Four star loops return; four face triangles are the same nonzero order-2 class.
    for vertex in VERTICES:
        s = ZERO
        for i in STARS[vertex]:
            s = add(s, AXIS[i])
        assert s == ZERO
        counts["star_relations"] += 1

        f = ZERO
        for i in FACES[vertex]:
            f = add(f, AXIS[i])
        assert f == T
        counts["face_torsion_relations"] += 1
    assert add(T, T) == ZERO and T != ZERO

    # K4 opposite edges differ by T and agree after doubling.
    for i, j in ((0, 5), (1, 4), (2, 3)):
        assert add(AXIS[i], T) == AXIS[j]
        assert scale(2, AXIS[i]) == scale(2, AXIS[j])
        counts["opposite_edge_relations"] += 1

    # Six axes and their immediate reversals give 12 distinct directed neighbours.
    neighbours = list(AXIS) + [neg(g) for g in AXIS]
    assert len(set(neighbours)) == 12

    # Exact S4 transport of the K4 atlas.
    perms = tuple(permutations(VERTICES))
    for g in perms:
        assert rotate_state(T, g) == T
        for i in range(6):
            assert rotate_state(AXIS[i], g) == AXIS[edge_action(g, i)]
            counts["s4_axis_checks"] += 1
    probes = (ZERO, (2, -3, 1), (5, 7, 0), (-4, 2, 1))
    for g in perms:
        for h in perms:
            gh = compose(g, h)
            for x in probes:
                assert rotate_state(rotate_state(x, h), g) == rotate_state(x, gh)
                counts["s4_composition_checks"] += 1

    # Slice quotient bit and visible projection.
    for vertex in VERTICES:
        assert slice_parity(T, vertex) == 1
        for i, edge in enumerate(EDGES):
            assert slice_parity(AXIS[i], vertex) == int(vertex not in edge)
            counts["slice_projection_checks"] += 1
        for x in (ZERO, (1, 2, 0), (-3, 4, 1), (10, -9, 1)):
            assert visible_slice_state(add(x, T), vertex) == visible_slice_state(x, vertex)
            assert slice_parity(visible_slice_state(x, vertex), vertex) == 0
            counts["slice_projection_checks"] += 2

    # Common kernel of all ordinary slice-visible projections is exactly {0,T}.
    kernel = []
    for u in range(-4, 5):
        for v in range(-4, 5):
            for eps in (0, 1):
                x = (u, v, eps)
                counts["visible_kernel_states_checked"] += 1
                if all(visible_slice_state(x, w) == ZERO for w in VERTICES):
                    kernel.append(x)
    assert set(kernel) == {ZERO, T}

    # Exact return certificate over a complete [-2,2]^6 box.
    for z in product(range(-2, 3), repeat=6):
        is_return = endpoint(z) == ZERO
        assert is_return == return_certificate(z)
        counts["return_vectors_checked"] += 1
        if is_return:
            star_coefficients(z)
            counts["return_reconstructions"] += 1

    # Smith determinantal divisors: 1,1,1,2 => SNF (1,1,1,2), free rank 2.
    rel = [[1 if vertex in edge else 0 for edge in EDGES] for vertex in VERTICES]
    determinantal_divisors = []
    for k in range(1, 5):
        d = 0
        for rows in combinations(range(4), k):
            for cols in combinations(range(6), k):
                minor = [[rel[r][c] for c in cols] for r in rows]
                d = gcd(d, abs(det_int(minor)))
                counts["snf_minor_checks"] += 1
        determinantal_divisors.append(d)
    assert determinantal_divisors == [1, 1, 1, 2]

    # BRC / endpoint observer regressions: same endpoint is not same history/trace.
    assert endpoint((1, 1, 1, 0, 0, 0)) == ZERO  # nonempty A-star loop
    counts["brc_type_regressions"] += 1
    face_abc = (1, 1, 0, 1, 0, 0)
    assert endpoint(face_abc) == T
    assert endpoint(tuple(2 * x for x in face_abc)) == ZERO
    counts["brc_type_regressions"] += 2
    ab_twice = (2, 0, 0, 0, 0, 0)
    cd_twice = (0, 0, 0, 0, 0, 2)
    assert endpoint(ab_twice) == endpoint(cd_twice) and ab_twice != cd_twice
    counts["brc_type_regressions"] += 1

    total = sum(counts.values())
    print("PASS_X6_UNIVERSAL_CELL_COMPLETION_V2")
    print("determinantal_divisors=", determinantal_divisors)
    print("normal_form=Z^2 x Z/2")
    print("common_visible_kernel={0,T}")
    print("assertions_counted=", total)
    for key in sorted(counts):
        print(f"{key}={counts[key]}")


if __name__ == "__main__":
    main()
