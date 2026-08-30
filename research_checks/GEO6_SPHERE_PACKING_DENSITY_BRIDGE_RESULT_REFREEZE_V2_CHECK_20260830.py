#!/usr/bin/env python3
"""Deterministic checks for RS-GEO6-SPHERE-PACKING-DENSITY-BRIDGE.

No external packages required.
"""
from itertools import product

DIM = 6
ID = tuple(range(DIM))
# Accepted Gen12 axis readout permutations, used here only as declared model symmetries.
A = (1, 2, 0, 5, 3, 4)  # (E1 E2 E3)(E4 E6 E5)
B = (0, 3, 4, 1, 2, 5)  # (E2 E4)(E3 E5)

E6_GRAM = (
    (2, -1, 0, 0, 0, 0),
    (-1, 2, -1, 0, 0, 0),
    (0, -1, 2, -1, 0, -1),
    (0, 0, -1, 2, -1, 0),
    (0, 0, 0, -1, 2, 0),
    (0, 0, -1, 0, 0, 2),
)


def compose(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(DIM))


def ppow(p, k):
    r = ID
    for _ in range(k):
        r = compose(p, r)
    return r


def inverse_perm(p):
    inv = [0] * DIM
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def act_coords(x, p):
    # Coordinate readout law y_j=x_{p^{-1}(j)}.
    inv = inverse_perm(p)
    return tuple(x[inv[j]] for j in range(DIM))


def vertices(n):
    return product(range(n), repeat=DIM)


def neighbor(x, axis, step, n):
    y = list(x)
    y[axis] = (y[axis] + step) % n
    return tuple(y)


def parity_set(n):
    assert n % 2 == 0
    return {x for x in vertices(n) if sum(x) % 2 == 0}


def check_torus(n):
    assert n >= 4 and n % 2 == 0
    S = parity_set(n)
    N = n ** DIM
    assert len(S) * 2 == N

    # Exact lower construction: every conflict edge flips parity.
    for x in S:
        for i in range(DIM):
            for step in (-1, 1):
                assert neighbor(x, i, step, n) not in S

    # Independent upper certificate: perfect matching along E1.
    seen = set()
    pair_count = 0
    for tail in product(range(n), repeat=DIM - 1):
        for k in range(0, n, 2):
            x = (k,) + tail
            y = (k + 1,) + tail
            assert y == neighbor(x, 0, 1, n)
            assert x not in seen and y not in seen
            seen.add(x)
            seen.add(y)
            pair_count += 1
    assert len(seen) == N
    assert pair_count * 2 == N
    # One vertex at most from each matching edge gives alpha <= N/2,
    # while S has N/2 vertices, hence alpha=N/2.

    # Translation covariance: each unit translation maps S to S or complement.
    all_vertices = set(vertices(n))
    for i in range(DIM):
        shifted = {neighbor(x, i, 1, n) for x in S}
        assert shifted == all_vertices - S

    # Carrier-S4 readout generators preserve conflicts and the parity construction.
    for p in (A, B, compose(A, B)):
        mapped = {act_coords(x, p) for x in S}
        assert mapped == S
        for x in S:
            y = act_coords(x, p)
            for i in range(DIM):
                z = neighbor(x, i, 1, n)
                yz = act_coords(z, p)
                # Images still differ by one unit in exactly one coordinate.
                diffs = [((yz[j] - y[j]) % n) for j in range(DIM)]
                nonzero = [d for d in diffs if d]
                assert len(nonzero) == 1
                assert nonzero[0] in (1, n - 1)

    return N, len(S), pair_count


def check_refinement(n, k):
    """Cover-refinement q: T_{kn}->T_n by coordinate reduction mod n."""
    assert n >= 4 and n % 2 == 0 and k >= 2
    coarse = parity_set(n)
    fine_n = k * n
    preimage_count = 0
    fine_parity_count = 0
    for x in vertices(fine_n):
        qx = tuple(c % n for c in x)
        in_preimage = qx in coarse
        if in_preimage:
            preimage_count += 1
        if sum(x) % 2 == 0:
            fine_parity_count += 1
        # Because n is even, reduction mod n preserves parity.
        assert in_preimage == (sum(x) % 2 == 0)
    assert preimage_count == (k ** DIM) * len(coarse)
    assert 2 * preimage_count == fine_n ** DIM
    assert preimage_count == fine_parity_count


def parity_in_box(start, lengths):
    total = 1
    for L in lengths:
        total *= L
    occ = 0
    for offsets in product(*(range(L) for L in lengths)):
        x = tuple(start[i] + offsets[i] for i in range(DIM))
        if sum(x) % 2 == 0:
            occ += 1
    return occ, total


def matching_boundary_box(start, lengths, axis=0):
    """Count vertices whose global E_axis matching partner leaves W.

    Pair even coordinate 2k with 2k+1. This is an exact boundary certificate.
    """
    ranges = [range(start[i], start[i] + lengths[i]) for i in range(DIM)]
    W = set(product(*ranges))
    b = 0
    for x in W:
        y = list(x)
        if x[axis] % 2 == 0:
            y[axis] += 1
        else:
            y[axis] -= 1
        if tuple(y) not in W:
            b += 1
    return b


def check_boundary_cases():
    cases = [
        ((0, 0, 0, 0, 0, 0), (3, 3, 3, 3, 3, 3)),
        ((1, 0, 2, 1, 3, 4), (3, 4, 3, 2, 3, 2)),
        ((2, 1, 0, 0, 0, 0), (5, 2, 2, 2, 2, 2)),
        ((-3, 2, 1, 0, -1, 4), (1, 3, 2, 2, 2, 2)),
    ]
    for start, lengths in cases:
        occ, N = parity_in_box(start, lengths)
        b = matching_boundary_box(start, lengths, 0)
        # Complete matching pairs contribute exactly one occupied cell.
        assert abs(2 * occ - N) <= b


def det_bareiss(M):
    A0 = [list(map(int, row)) for row in M]
    n = len(A0)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A0[k][k] == 0:
            for r in range(k + 1, n):
                if A0[r][k] != 0:
                    A0[k], A0[r] = A0[r], A0[k]
                    sign *= -1
                    break
            else:
                return 0
        pivot = A0[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A0[i][j] = (A0[i][j] * pivot - A0[i][k] * A0[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A0[i][k] = 0
        for j in range(k + 1, n):
            A0[k][j] = 0
    return sign * A0[-1][-1]


def e6_q(v):
    return sum(v[i] * E6_GRAM[i][j] * v[j] for i in range(DIM) for j in range(DIM))


def check_e6():
    # Exact external benchmark: Cartan/Gram determinant 3, minimal squared norm 2.
    assert det_bareiss(E6_GRAM) == 3
    roots = []
    min_q = None
    for v in product(range(-3, 4), repeat=DIM):
        if not any(v):
            continue
        q = e6_q(v)
        if min_q is None or q < min_q:
            min_q = q
        if q == 2:
            roots.append(v)
    assert min_q == 2
    # Standard E6 root system has 72 norm-2 roots in this simple-root basis.
    assert len(roots) == 72


def main():
    assert ppow(A, 3) == ID
    assert ppow(B, 2) == ID
    assert ppow(compose(A, B), 4) == ID

    stats = []
    for n in (4, 6):
        stats.append((n,) + check_torus(n))
    check_refinement(4, 2)
    check_boundary_cases()
    check_e6()

    print("PASS GEO6 sphere-packing density bridge")
    for n, N, occ, pairs in stats:
        print(f"T_{n}: cells={N}, independent={occ}, matching_pairs={pairs}, density=1/2")
    print("refinement T_8 -> T_4: full-fiber parity lift preserves density=1/2")
    print("E6 benchmark: det(Gram)=3, min norm^2=2, norm-2 roots=72")
    print("all symmetry and adversarial boundary checks passed")


if __name__ == "__main__":
    main()
