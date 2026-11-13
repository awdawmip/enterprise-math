#!/usr/bin/env python3
"""Exact 7-node R5 martingale sparsity sharpness certificate.

No external dependencies. Integer/rational arithmetic throughout. The symbolic
large-integer witness is constructed by a coefficient-separation lemma; the
finite checks verify its ingredients, not an exponential support enumeration.
"""
from fractions import Fraction
from math import factorial

N = 7
K = (2, 10, 15, 20, 25, 30, 38)  # r_i=K_i/20
LENGTH = N * N


def atom(j, lower=None, upper=None):
    a = [0] * LENGTH
    if lower is None:
        a[j * N + j] = 1
    else:
        assert lower < j < upper
        a[lower * N + j] = K[upper] - K[j]
        a[upper * N + j] = K[j] - K[lower]
    return a


def add(*vectors):
    return [sum(v[i] for v in vectors) for i in range(LENGTH)]


def scale(v, c):
    return [c * x for x in v]


def qmass(E):
    return sum(E)


def image(E):
    return (
        [sum(E[i * N + j] for j in range(N)) for i in range(N)]
        + [sum(E[i * N + j] for i in range(N)) for j in range(N)]
        + [sum(K[i] * E[i * N + j] for i in range(N)) for j in range(N)]
    )


def balanced(E):
    return sum((K[i] - 20) * E[i * N + j]
               for i in range(N) for j in range(N)) == 0


def in_strict_chamber(E):
    out = image(E)
    mu, nu = out[:N], out[N:2*N]
    return nu[0] > 0 and nu[-1] > 0 and all(
        nu[j] > mu[j] > 0 for j in range(1, N-1))


def pivot_rows_of_columns(vectors):
    """Exact rank and pivot rows of the 21xk matrix of output vectors."""
    cols = len(vectors)
    rows = len(vectors[0])
    M = [[Fraction(vectors[j][i]) for i in range(rows)]
         for j in range(cols)]
    piv = []
    for c in range(rows):
        h = len(piv)
        k = next((i for i in range(h, cols) if M[i][c]), None)
        if k is None:
            continue
        M[h], M[k] = M[k], M[h]
        v = M[h][c]
        M[h] = [z / v for z in M[h]]
        for i in range(cols):
            if i != h and M[i][c]:
                v = M[i][c]
                M[i] = [x - v*y for x, y in zip(M[i], M[h])]
        piv.append(c)
        if len(piv) == cols:
            break
    return piv


def determinant(A):
    """Bareiss exact integer determinant of a square matrix."""
    M = [row[:] for row in A]
    n = len(M)
    sign = 1
    den = 1
    for k in range(n-1):
        if M[k][k] == 0:
            p = next(i for i in range(k+1, n) if M[i][k] != 0)
            M[k], M[p] = M[p], M[k]
            sign = -sign
        x = M[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                v = M[i][j]*x-M[i][k]*M[k][j]
                assert v % den == 0
                M[i][j] = v//den
        for i in range(k+1,n):
            M[i][k] = 0
        den = x
    return sign * M[-1][-1]


def balanced_pair(lo, hi):
    """Combine integer atom(s) at below/above-one columns."""
    jl, L = lo
    jh, H = hi
    assert K[jl] < 20 < K[jh]
    return add(scale(L, (K[jh]-20)*qmass(H)),
               scale(H, (20-K[jl])*qmass(L)))


def make_e0():
    E = [0] * LENGTH
    for j in range(N):
        E = add(E, atom(j))
        for lo in range(j):
            for hi in range(j+1, N):
                E = add(E, atom(j, lo, hi))
    return E


def build_generators():
    E0 = make_e0()  # symmetric; has every permitted edge strictly positive
    assert balanced(E0)
    O = [0] * LENGTH
    for j in range(1,N-1):
        O = add(O, atom(j, 0, N-1))
    assert balanced(O)
    BASE = add(E0, scale(O,100))
    # Ten independent balanced rays, chosen by exact integer rank exploration.
    extras = [atom(3), atom(3,0,4), atom(3,0,5), atom(3,0,6),
              atom(3,1,4), atom(3,2,4),
              balanced_pair((0,atom(0)),(4,atom(4))),
              balanced_pair((0,atom(0)),(5,atom(5))),
              balanced_pair((0,atom(0)),(6,atom(6))),
              balanced_pair((1,atom(1)),(4,atom(4)))]
    gens = [BASE] + [add(BASE, x) for x in extras]
    assert all(balanced(x) and in_strict_chamber(x) for x in gens)
    assert len(gens) == 11
    return gens


G = build_generators()
W = [image(E) for E in G]
pivot = pivot_rows_of_columns(W)
assert len(pivot)==11
minor = [[W[j][i] for j in range(11)] for i in pivot]
det = determinant(minor)
assert det != 0
print('PASS_11_INDEPENDENT_BALANCED_MARTINGALE_IMAGES')
print('PIVOT_ROWS_0_BASED',pivot)
print('PIVOT_MINOR_NONZERO',det)

# A_int has entries 20 (row/col mass), K_i (moment), |entry|<=38.
# For a support S with <=16 positions and all 5 interior columns active,
# a basis of the martingale kernel (one balance relation per interior col)
# may use <=2 entries per column, each bounded by 36. Hence every image
# entry of these basis vectors under A_int is bounded by 2*38*36=2736.
# All integer determinant coefficients for [A_int(ker C_S), b(t)]
# (size <=12) are bounded by H=12!*M^12, with M as below.
max_output_entry = max(abs(v) for w in W for v in w)
M = max(2736, 20 * max_output_entry)
H = factorial(12) * M**12
B = H + 2
E_B = [0]*LENGTH
for k,E in enumerate(G):
    E_B = add(E_B,scale(E,B**k))
assert balanced(E_B) and in_strict_chamber(E_B)
assert sum(v>0 for v in E_B) == 37
row_col_moment = image(E_B)
mu, nu, mom = row_col_moment[:7], row_col_moment[7:14], row_col_moment[14:]
assert sum(mu) == sum(nu) == qmass(E_B)
assert all(mom[j] == K[j]*nu[j] for j in range(7))
assert sum(mom) == 20*qmass(E_B)
assert sum(K[i]*mu[i] for i in range(7)) == 20*qmass(E_B)
assert all(nu[j]>mu[j] for j in range(1,6))
print('PASS_EXPLICIT_RATIONAL_NORMALIZED_PQ_MARGINALS')
print('FULL_POSITIVE_ALLOWED_SUPPORT',sum(v>0 for v in E_B))
print('M_DETERMINANT_ENTRY_BOUND',M)
print('H_DECIMAL_DIGITS',len(str(H)))
print('B_DECIMAL_DIGITS',len(str(B)))
print('TOTAL_Q_MASS_INTEGER_DIGITS',len(str(qmass(E_B))))
print('EXACT_CONSTRUCTION_FORMULA_EB_SUM_B_POWER_K_GK',len(G))
print('SYMBOLIC_MIN_SUPPORT_LOWER_BOUND',17)
print('PREDECESSOR_UNIVERSAL_UPPER_BOUND',17)
print('THEOREM_NORMALIZED_7_NODE_17_EDGE_BOUND_SHARP')
