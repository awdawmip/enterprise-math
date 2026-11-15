#!/usr/bin/env python3
"""Independent exact finite W2 source-histogram rank check.

The frozen Stage3 formula is transcribed as arithmetic over finite cell posets.
This is NOT the frozen R063 Stage0 17-gate/512-case native benchmark
and is NOT a rerun of the original Stage3 whole checker.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
import json


def words(a, b):
    return ["".join("i" if j in pos else "j" for j in range(a+b))
            for pos in combinations(range(a+b), a)]


def hist(p, q):
    groups = {j: [] for j in range(4)}
    for r, x in enumerate(p):
        for s, y in enumerate(q):
            phase = (int(x == 'j') + int(y == 'j')) % 4
            groups[phase].append((r, s, phase))
    remnants = [()]
    for a, b in ((0, 2), (1, 3)):
        A, B = groups[a], groups[b]
        pool = A if len(A) >= len(B) else B
        extras = list(combinations(pool, abs(len(A)-len(B))))
        remnants = [base + extra for base in remnants for extra in extras]
    result = Counter()
    for rem in remnants:
        rem = tuple(sorted(rem))
        preds = [frozenset(j for j, d in enumerate(rem)
                            if d[0] <= c[0] and d[1] <= c[1]
                            and (d[0] < c[0] or d[1] < c[1]))
                 for c in rem]
        def visit(mask, word):
            if mask == (1 << len(rem)) - 1:
                result[word] += 1
                return
            for i, c in enumerate(rem):
                if not (mask & (1 << i)) and all(mask & (1 << j) for j in preds[i]):
                    assert c[2] in (0, 1), (p, q, c)
                    visit(mask | (1 << i), word + ('i' if c[2] == 0 else 'j'))
        visit(0, '')
    return result


def det_bareiss(mat):
    a = [[int(x) for x in r] for r in mat]
    n = len(a)
    prev = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        for i in range(k+1, n):
            for j in range(k+1, n):
                val = a[i][j]*a[k][k] - a[i][k]*a[k][j]
                assert val % prev == 0
                a[i][j] = val // prev
            a[i][k] = 0
        prev = a[k][k]
    return sign*a[-1][-1]


def rank_gauss(mat):
    a = [[Fraction(v) for v in r] for r in mat]
    k = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(k, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        leading = a[k][col]
        a[k] = [v/leading for v in a[k]]
        for r in range(len(a)):
            if r != k and a[r][col]:
                scale = a[r][col]
                a[r] = [u-scale*v for u, v in zip(a[r], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def tensor3_signature(p, q, r):
    return tuple(sorted((i, j, k, (int(x == 'j') + int(y == 'j') + int(z == 'j')) % 4)
                        for i, x in enumerate(p) for j, y in enumerate(q) for k, z in enumerate(r)))


def main():
    src = words(2,1)
    target = words(3,4)
    pairs = list(product(src, repeat=2))
    H = [hist(*pq) for pq in pairs]
    rows = [[r.get(w, 0) for w in target] for r in H]
    assert len(src) == 3 and len(target) == 35 and len(rows) == 9
    assert all(H[3*i+j] == H[3*j+i] for i in range(3) for j in range(3))
    assert [sum(r.values()) for r in H] == [102,54,26,54,52,54,26,54,102]
    unique = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    rowids = [3*i+j for i,j in unique]
    chosen = ['iiijjjj','iijijjj','ijijijj','jiijijj','jiijjij','jjijiji']
    cols = [target.index(w) for w in chosen]
    minor = [[rows[i][j] for j in cols] for i in rowids]
    expected_minor = [[36,30,8,0,0,0],[0,2,5,2,4,0],[0,0,0,2,1,0],
                      [0,0,4,0,0,4],[0,0,0,0,2,5],[0,0,0,0,0,8]]
    assert minor == expected_minor
    determinant = det_bareiss(minor)
    assert determinant == -9216
    assert rank_gauss(rows) == rank_gauss([rows[i] for i in rowids]) == 6
    assert sum(sum(row) for row in rows) == 524
    assert len(set().union(*[set(v) for v in H])) == 31
    # Explicit kernel basis, and independently verified six-dimensional image.
    kernel_basis = []
    for i,j in [(0,1),(0,2),(1,2)]:
        vec = [0]*9
        vec[3*i+j],vec[3*j+i] = 1,-1
        assert all(sum(vec[k]*rows[k][c] for k in range(9))==0 for c in range(35))
        kernel_basis.append(vec)
    assert len(kernel_basis)==9-rank_gauss(rows)
    # Nonnegative input witnesses: same exact output histogram, different source-order observer.
    assert H[1] == H[3] and pairs[1] != pairs[3]
    left = tensor3_signature('iij', 'iji', 'ij')
    right = tensor3_signature('iji', 'iij', 'ij')
    assert len(left) == len(right) == 18
    triple_diff = [(x, y) for x, y in zip(left, right) if x != y]
    assert len(triple_diff) == 12
    assert triple_diff[0] == ((0, 1, 0, 1), (0, 1, 0, 0))
    output = dict(source_words=src, triple_source_order_changed_cells=len(triple_diff), target_word_count=len(target), source_ordered_pairs=9,
                  unique_unordered_source_types=6, source_pair_formal_witness_totals=[sum(r.values()) for r in H],
                  histogram_matrix_rank_Q=6, kernel_dimension_Q=3,
                  kernel_basis=kernel_basis, minor_column_words=chosen,
                  minor_determinant=determinant, formal_witness_sum=524,
                  native_endpoint_full_fibre_count=35, original_stage3_union_support_size=31,
                  ordered_pair_collision_example=['iij×iji','iji×iij'])
    print(json.dumps(output,ensure_ascii=False,sort_keys=True,separators=(',',':')))
    print('PASS_X6_R063_STAGE3_W2_SOURCE_HISTOGRAM_RANK6')


if __name__ == '__main__':
    main()
