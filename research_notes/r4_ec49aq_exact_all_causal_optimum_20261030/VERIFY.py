"""Independent exact support-matrix enumeration for EC49AQ; no use of edge traversal.

Enumerates rank-4 original supports and rank-5 paid-boundary supports, computes
objective directly from P and Q source leaves instead of the q_z/T shortcut.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json

Z = Q(0)
ACTIONS = (1, 1, 2, 2, 0)
ALL = tuple(product(range(3), range(5)))
RHS_4 = (Q(1), Q(1), Q(1), Q(43, 16))
RHS_5 = RHS_4 + (Q(39, 16),)
LIMIT = Q(77, 688)


def solve_support(support, rhs):
    """Solve 4 or 5 equations in as many supported unknowns, over Q only."""
    n = len(rhs)
    assert len(support) == n
    matrix = []
    for w in range(3):
        matrix.append([Q(int(w0 == w)) for w0, c in support] + [rhs[w]])
    matrix.append([Q(ACTIONS[c]) for w, c in support] + [rhs[3]])
    if n == 5:
        matrix.append([Q(int(c != 4)) for w, c in support] + [rhs[4]])
    for k in range(n):
        pivot = next((i for i in range(k, n) if matrix[i][k]), None)
        if pivot is None:
            return None
        matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
        factor = matrix[k][k]
        matrix[k] = [z / factor for z in matrix[k]]
        for i in range(n):
            if i != k:
                factor = matrix[i][k]
                matrix[i] = [matrix[i][j] - factor * matrix[k][j] for j in range(n + 1)]
    values = tuple(matrix[i][-1] for i in range(n))
    if not all(v > 0 for v in values):
        return None
    arr = [[Z] * 5 for _ in range(3)]
    for (w, c), v in zip(support, values):
        arr[w][c] = v
    return tuple(tuple(row) for row in arr)


def paid_cost(x):
    return sum((x[w][c] for w, c in product(range(3), range(4))), Z) / 3


def direct_score(x):
    total = Z
    for c, u, z in product(range(4), range(2), range(3)):
        p = q = Z
        for w in range(3):
            tt = Q(1, 2) + (2 * u - 1) * (1 - w) * Q(1, 25)
            p += x[w][c] * tt * (Q(1, 6) if z == w else Q(1, 12))
            q += x[w][c] * tt / 9
        total += max(Z, p - Q(177, 172) * q)
    return total


v4 = {x for supp in combinations(ALL, 4) if (x := solve_support(supp, RHS_4)) is not None}
v5 = {x for supp in combinations(ALL, 5) if (x := solve_support(supp, RHS_5)) is not None}
assert len(v4) == 168
assert len(v5) == 144
assert all(paid_cost(x) == Q(13, 16) for x in v5)
v_high = {x for x in v4 if paid_cost(x) >= Q(13, 16)}
assert len(v_high) == 24
assert not v5.intersection(v_high)
assert len(v_high | v5) == 168
high_scores = [direct_score(x) for x in v_high]
boundary_scores = [direct_score(x) for x in v5]
assert max(high_scores) == Q(12177, 137600)
assert max(boundary_scores) == LIMIT
assert sum(s == LIMIT for s in boundary_scores) == 24
print(json.dumps({
    'schema': 'EC49AQ_INDEPENDENT_SUPPORT_ENUMERATION_V1',
    'status': 'PASS_EXACT_FRACTION_AUTHOR_CROSSCHECK',
    'enumeration': 'all 15 choose 4 and 15 choose 5 supports, exact Gaussian elimination',
    'scoring': 'direct purchased-leaf P,Q differences; no q_z/T shortcut',
    'untruncated_vertices': len(v4),
    'strict_positive_paid_boundary_supports': len(v5),
    'high_cost_original_vertices': len(v_high),
    'all_truncated_vertices': len(v_high | v5),
    'max_high_F': str(max(high_scores)),
    'max_boundary_F': str(max(boundary_scores)),
    'number_of_boundary_maximizers': sum(s == LIMIT for s in boundary_scores),
}, ensure_ascii=False, sort_keys=True, indent=2))
