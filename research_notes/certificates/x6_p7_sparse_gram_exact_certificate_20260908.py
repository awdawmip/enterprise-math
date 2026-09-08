#!/usr/bin/env python3
"""Exact finite certificate for the X6 determinant-7 anisotropy lower bound.

Scope:
- no floating point;
- enumerates the finite symmetric-integral Gram region forced by Delta_6 < 68;
- proves every determinant-49 scalar Gram candidate below 68 has one canonical
  H7 (+) H7 type with Delta_6=56;
- verifies that this type has no order-7 isotropic discriminant glue;
- verifies an explicit determinant-7 transport with Delta_6=68.

This is a result-specific certificate, not a reusable top-level tool family and
not a Foundation mutation.
"""
from itertools import combinations, combinations_with_replacement, product

D = 6
P = 7
BOUND = 68
EDGES = list(combinations(range(D), 2))


def det_bareiss(mat):
    """Exact integer determinant by fraction-free Bareiss elimination."""
    a = [list(map(int, row)) for row in mat]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = None
            for r in range(k + 1, n):
                if a[r][k] != 0:
                    swap = r
                    break
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def diagonal_defect(diag):
    return sum((diag[i] - diag[j]) ** 2 for i in range(D) for j in range(i + 1, D))


def offdiag_mass(conf):
    return sum(v * v for _, v in conf)


def matrix_from(diag, conf):
    g = [[0] * D for _ in range(D)]
    for i, x in enumerate(diag):
        g[i][i] = x
    for edge_index, value in conf:
        i, j = EDGES[edge_index]
        g[i][j] = value
        g[j][i] = value
    return g


def delta_from(diag, conf):
    return diagonal_defect(diag) + 12 * offdiag_mass(conf)


def configs_by_mass():
    """All off-diagonal integer configurations with squared mass <= 5.

    Delta<68 implies M<=5. Hence entries are only 0,+/-1, with the sole
    additional possibilities one +/-2 (M=4) or one +/-2 plus one +/-1 (M=5).
    """
    out = {m: [] for m in range(6)}
    out[0].append(())
    for m in range(1, 6):
        for inds in combinations(range(len(EDGES)), m):
            for signs in product((-1, 1), repeat=m):
                out[m].append(tuple(zip(inds, signs)))
    for edge in range(len(EDGES)):
        for sign in (-2, 2):
            out[4].append(((edge, sign),))
    for edge2 in range(len(EDGES)):
        for edge1 in range(len(EDGES)):
            if edge1 == edge2:
                continue
            for sign2 in (-2, 2):
                for sign1 in (-1, 1):
                    out[5].append(((edge2, sign2), (edge1, sign1)))
    return out


CONFIGS = configs_by_mass()


def graph_components(conf):
    adj = [set() for _ in range(D)]
    for edge_index, value in conf:
        if value == 0:
            continue
        i, j = EDGES[edge_index]
        adj[i].add(j)
        adj[j].add(i)
    seen = set()
    comps = []
    for s in range(D):
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append(tuple(sorted(comp)))
    return tuple(sorted(comps, key=lambda c: (len(c), c)))


def canonical_low_candidate(diag, conf):
    """Check the only determinant-49 scalar type found below Delta=68.

    It must have diagonal multiset 2,2,2,2,3,3 and four unit edges forming
    two disconnected 3-vertex paths. Each component has diagonal multiset
    2,2,3 and the degree-2 vertex has diagonal 2. Tree signs are removable by
    signed basis switches, so their signs do not change the type.
    """
    if tuple(diag) != (2, 2, 2, 2, 3, 3):
        return False
    if offdiag_mass(conf) != 4:
        return False
    if any(abs(value) != 1 for _, value in conf):
        return False
    comps = graph_components(conf)
    nontrivial = [c for c in comps if len(c) > 1]
    if sorted(map(len, nontrivial)) != [3, 3]:
        return False
    # Rebuild degree data.
    degree = [0] * D
    for edge_index, _ in conf:
        i, j = EDGES[edge_index]
        degree[i] += 1
        degree[j] += 1
    for comp in nontrivial:
        vals = sorted(diag[i] for i in comp)
        degs = sorted(degree[i] for i in comp)
        if vals != [2, 2, 3] or degs != [1, 1, 2]:
            return False
        center = [i for i in comp if degree[i] == 2][0]
        if diag[center] != 2:
            return False
    return True


def exact_sparse_scan():
    # If Delta<68, the diagonal range is at most 4. Indeed the minimum D for
    # six integers containing both 0 and 5 is 77 (translate-invariant).
    assert diagonal_defect((0, 5, 2, 2, 2, 2)) == 77

    # If every diagonal >=3, write G=3I+E+R with R diagonal nonnegative.
    # The accompanying proof shows 3I+E is positive definite for M<=5, so
    # determinant is coordinatewise increasing in R. The finite E scan below
    # verifies min det(3I+E)=216 >49.
    min_det_at_three = None
    for mass in range(6):
        for conf in CONFIGS[mass]:
            g = matrix_from((3, 3, 3, 3, 3, 3), conf)
            det = det_bareiss(g)
            if min_det_at_three is None or det < min_det_at_three:
                min_det_at_three = det
    assert min_det_at_three == 216

    # Therefore any determinant-49 Gram below the bound must have minimum
    # diagonal 1 or 2; range<=4 gives the finite diagonal windows below.
    diagonal_patterns = []
    for minimum in (1, 2):
        for diag in combinations_with_replacement(range(minimum, minimum + 5), D):
            if diag[0] != minimum:
                continue
            dd = diagonal_defect(diag)
            if dd < BOUND:
                diagonal_patterns.append((diag, dd))

    candidates = []
    checked = 0
    for diag, dd in diagonal_patterns:
        max_mass = min(5, (BOUND - 1 - dd) // 12)
        for mass in range(max_mass + 1):
            if dd + 12 * mass >= BOUND:
                continue
            for conf in CONFIGS[mass]:
                checked += 1
                g = matrix_from(diag, conf)
                if det_bareiss(g) == P * P:
                    candidates.append((dd + 12 * mass, diag, conf))

    assert checked == 1_150_826
    assert len(candidates) == 384
    assert {c[0] for c in candidates} == {56}
    assert all(canonical_low_candidate(diag, conf) for _, diag, conf in candidates)
    return checked, len(candidates), min_det_at_three


def discriminant_glue_obstruction():
    # One canonical 3x3 determinant-7 block has discriminant coefficient 6=-1.
    h7 = [
        [2, 1, -1],
        [1, 2, 0],
        [-1, 0, 3],
    ]
    assert det_bareiss(h7) == 7
    # Cofactor (1,1) is 6, so e1^* gives a cyclic discriminant generator with
    # coefficient 6/7. Two copies would need 6x^2+6y^2=0 mod7.
    solutions = []
    for x in range(7):
        for y in range(7):
            if x == 0 and y == 0:
                continue
            if (6 * x * x + 6 * y * y) % 7 == 0:
                solutions.append((x, y))
    assert solutions == []


def explicit_upper_bound():
    a7 = [
        [0, -1, -1, 0, 0, -1],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, -1, 0, -1],
        [0, 0, 1, 0, 0, -1],
        [0, 0, 0, -1, 1, 1],
        [0, 0, 0, 1, 1, 0],
    ]
    assert abs(det_bareiss(a7)) == 7
    # Exact Gram.
    g = [[sum(a7[k][i] * a7[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
    diag = tuple(g[i][i] for i in range(D))
    conf = []
    edge_to_index = {e: idx for idx, e in enumerate(EDGES)}
    for i, j in EDGES:
        if g[i][j]:
            conf.append((edge_to_index[(i, j)], g[i][j]))
    assert det_bareiss(g) == 49
    assert delta_from(diag, tuple(conf)) == 68
    return diag, tuple(conf)


if __name__ == "__main__":
    checked, low_candidates, min_det_at_three = exact_sparse_scan()
    discriminant_glue_obstruction()
    diag, conf = explicit_upper_bound()
    print({
        "status": "EXACT_CERTIFICATE_PASSED",
        "matrices_checked_in_low_window": checked,
        "det49_scalar_candidates_below_68": low_candidates,
        "all_low_candidates_delta": 56,
        "all_low_candidates_type": "H7 direct_sum H7 (same discriminant phase)",
        "discriminant_glue": "OBSTRUCTED because x^2+y^2=0 has no nonzero solution mod 7",
        "explicit_det7_delta": 68,
        "min_det_3I_plus_E_for_M_le_5": min_det_at_three,
        "conclusion": "min_{|det A|=7} Delta_6(A)=68",
        "boundary": "Result-specific finite Gram certificate + exact discriminant-form obstruction; no Foundation promotion.",
    })
