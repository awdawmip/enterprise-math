#!/usr/bin/env python3
"""R284BS: exact witness checker. Python 3 standard library only.

Each control is a separate diagonal or root-row entry, hence the determinant
polynomial is multiaffine in the free controls. Equality at every Boolean
control corner is equivalent to equality of the whole polynomial.
"""
import itertools
import json
from pathlib import Path

def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]

def observation(c, j, t, values):
    n = len(c)
    other_leaves = [k for k in range(1, n) if k != j]
    free_d = values[:n-1]  # d_0 followed by the n-2 unfrozen leaf diagonals
    z = values[n-1:]       # z_1,...,z_{n-1}
    diagonals = {0: free_d[0], j: t}
    diagonals.update(zip(other_leaves, free_d[1:]))
    a = [[-c[i][k] + (diagonals[i] if i == k else 0)
          for k in range(n)] for i in range(n)]
    for k in range(1, n):
        a[0][k] -= z[k - 1]
    return determinant(a)

def negative_pair(n, H, t, j=1):
    assert 1 - H * H <= t <= 0
    k = next(k for k in range(1, H + 1) if 1 <= t + H * k <= H)
    c = t + H * k
    a = [[1] * n for _ in range(n)]
    a[j][j], a[j][0] = c, H
    leaves = [i for i in range(1, n) if i != j]
    for i in leaves:
        a[i][j] = k
    u, v = leaves[:2]
    a[u][v], a[v][u] = 1, 2
    b = [row[:] for row in a]
    b[u][v], b[v][u] = 2, 1
    return a, b, {'case': 'dark-subblock-transpose', 'c': c, 'k': k, 'u': u, 'v': v}

def positive_pair(n, H, t, j=1):
    assert 1 <= t <= H * H
    a = [[1] * n for _ in range(n)]
    p = next(i for i in range(1, n) if i != j)
    if t <= H:
        a[j][j] = t
        b = [row[:] for row in a]
        for q in range(n):
            if q != j:
                b[p][q] = 2
        return a, b, {'case': 'zero-pivot-shear', 'c': t, 'p': p}
    k, c = (t - 1) // H, t - H * ((t - 1) // H)
    assert 1 <= k <= H - 1 and 1 <= c <= H
    a[j][j] = c
    for q in range(n):
        if q != j:
            a[j][q] = H
    a[p][j] = k + 1
    b = [row[:] for row in a]
    b[p][j] = 1
    for q in range(n):
        if q != j:
            b[p][q] = 2
    return a, b, {'case': 'nonzero-pivot-shear', 'c': c, 'k': k, 'p': p}

def verify():
    items = []
    for n, H in [(4, 2), (4, 3), (5, 2), (5, 3), (6, 2)]:
        for t in range(1 - H * H, H * H + 1):
            c, d, parameters = (negative_pair if t <= 0 else positive_pair)(n, H, t)
            assert c != d
            assert all(1 <= v <= H for matrix in (c, d) for row in matrix for v in row)
            count = 0
            for v in itertools.product((0, 1), repeat=2*n-2):
                observed_c = observation(c, 1, t, v)
                observed_d = observation(d, 1, t, v)
                assert observed_c == observed_d, (n, H, t, v, observed_c, observed_d)
                count += 1
            items.append({'n': n, 'H': H, 'j': 1, 't': t,
                          'construction': parameters, 'C': c, 'D': d,
                          'exact_boolean_corners': count})
    return {'schema':'R284BS_EXACT_CORNER_CERTIFICATE_V1',
            'arithmetic':'Exact integer Bareiss determinant',
            'mathematical_scope':'Complete Boolean corners for each constructed pair; multiaffinity gives polynomial identity',
            'cases':len(items), 'total_corners':sum(x['exact_boolean_corners'] for x in items),
            'cases_detail':items}

if __name__ == '__main__':
    result = verify()
    output = Path(__file__).with_name('R284BS_sharp_leaf_freeze_verification.json')
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('cases:', result['cases'], 'exact corners:', result['total_corners'])
    print('saved:', output)
