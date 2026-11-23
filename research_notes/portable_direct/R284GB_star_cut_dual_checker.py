#!/usr/bin/env python3
"""R284GB: exact rational Farkas certificates for the global two-heavy premise.

SciPy/HiGHS is only a candidate finder. Every certificate is independently
checked using Python's Fraction arithmetic against the complete branch LP.
No solver status is accepted as proof without an exact identity.
"""
from fractions import Fraction
from itertools import combinations, product
from scipy.optimize import linprog
import numpy as np

PAIRS = tuple(combinations(range(4), 2))
STAR = ((0, 1), (0, 2), (0, 3))
ADJ = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
        for p in range(1, 8)}
LAST = {(p, i): next(e for e in ((i - 1 - t) % 4 for t in range(4))
                      if BITS[p][e] != BITS[p][(e + 1) % 4])
        for p in range(1, 8) for i in range(4)}
DIST, CUTS = {}, {}
for pair in PAIRS:
    i, j = pair
    edges = [(p, LAST[p, i], 4 + LAST[p, j]) for p in range(1, 8)
             if BITS[p][i] != BITS[p][j]]
    DIST[pair] = tuple(p for p, _, _ in edges)
    minimal = {}
    for vertices in range(1, 256):
        mask = tuple(p for p, a, b in edges
                     if (vertices >> a) & 1 and (vertices >> b) & 1)
        if mask:
            minimal[mask] = min(minimal.get(mask, 9), vertices.bit_count())
    CUTS[pair] = tuple(minimal.items())
assert tuple(len(CUTS[pair]) for pair in STAR) == (7, 9, 7)


def branch_rows(cuts, allowed):
    """Inequalities A (x1,...,x7,q)^T <= b for n=4q+9, q>=5.

    Two of x3,x5,x6 are <=2q+1; allowed is the possibly heavy type.
    Equality total n=4q+9 is represented by its two directions.
    """
    A, b = [], []
    def row(coeff, rhs):
        A.append(tuple(coeff))
        b.append(int(rhs))
    for pair in PAIRS:
        row([-int(p in DIST[pair]) for p in range(1, 8)] + [2],
            -(5 if pair in ADJ else 3))
    for mask, m in cuts:
        row([-int(p in mask) for p in range(1, 8)] + [m], -3)
    for p in (3, 5, 6):
        if p != allowed:
            row([int(i == p) for i in range(1, 8)] + [-2], 1)
    for p in range(1, 8):
        row([-int(i == p) for i in range(1, 8)] + [0], 0)
    row([0] * 7 + [-1], -5)
    row([1] * 7 + [-4], 9)
    row([-1] * 7 + [4], -9)
    assert len(A) == 21
    return A, b


def exact_dual_proof(cuts, allowed):
    A, b = branch_rows(cuts, allowed)
    # A^T lambda = 0, b^T lambda = -1, lambda >= 0:
    # the branch would imply 0 <= -1, a contradiction.
    equal = np.vstack((np.asarray(A, dtype=float).T,
                       np.asarray(b, dtype=float)))
    rhs = [0.] * 8 + [-1.]
    candidate = linprog(np.zeros(len(A)), A_eq=equal, b_eq=rhs,
                        bounds=(0, None), method='highs')
    if candidate.status != 0:
        raise AssertionError(('NO_DUAL_CANDIDATE', cuts, allowed,
                              candidate.status))
    lam = tuple(Fraction(float(t)).limit_denominator(5000)
                for t in candidate.x)
    assert all(v >= 0 for v in lam)
    assert all(sum(lam[r] * A[r][col] for r in range(len(A))) == 0
               for col in range(8)), (cuts, allowed, 'nonzero coefficient')
    assert sum(lam[r] * b[r] for r in range(len(A))) == -1, (
        cuts, allowed, 'invalid dual bound')
    return max(v.denominator for v in lam)


def main():
    count, max_denominator = 0, 0
    for cuts in product(*(CUTS[pair] for pair in STAR)):
        for allowed in (3, 5, 6):
            max_denominator = max(max_denominator,
                                  exact_dual_proof(cuts, allowed))
            count += 1
    assert count == 7 * 9 * 7 * 3 == 1323
    print('PASS: star cuts alone + six nominal distances force two-heavy')
    print('q>=5, n=4q+9: %d/%d exact rational Farkas contradictions' %
          (count, count))
    print('maximum exact dual coefficient denominator:', max_denominator)
    print('n=4q+8 follows by padding type-1 count to n=4q+9')
    print('Combining R284GA: full stable census 7 and 66 for all q>=5')


if __name__ == '__main__':
    main()
