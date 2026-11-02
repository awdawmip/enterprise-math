#!/usr/bin/env python3
"""Exact R5 two-law, source-conditioned P/Q terminal-delay fiber certificate.
All arithmetic uses fractions.Fraction; no floating point and no network.
"""
from fractions import Fraction as F
from itertools import product

Z, H, O = F(0), F(1, 2), F(1)
SRC = ('C', 'I', 'BJ', 'IJ')
FULL = tuple(product((Z, O), repeat=7))
LR = tuple(product((Z, O), repeat=3))
CHECKS = 0
FLOWS = 0

def check(claim, msg):
    global CHECKS
    CHECKS += 1
    if not claim:
        raise AssertionError(msg)

def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(4))

def scale(a, v):
    return tuple(a * b for b in v)

def stop(t):
    return O, Z, F(t), F(t)

def answer(t, p, q):
    return p, O - q, F(t), F(t)

def flow(p, q, x, jB, jI, kC, kI, kBJ, kIJ):
    global FLOWS
    FLOWS += 1
    def knode(source, k):
        return add(scale(k, stop(3)),
                   scale(O - k, (H, H, F(4) + p[source], F(4) + q[source])))
    def jnode(source, j, k):
        daughter = 'BJ' if source == 'B' else 'IJ'
        return add(scale(j, stop(2)),
                   scale(O - j, add(scale(H, knode(daughter, k)),
                                    scale(H, answer(3, F(3, 5), F(2, 5))))))
    i = add(scale(x, stop(1)),
            scale(O - x, add(scale(H, jnode('I', jI, kIJ)),
                             scale(H, knode('I', kI)))))
    return add(scale(H, i), scale(F(1, 4), jnode('B', jB, kBJ)),
               scale(F(1, 4), knode('C', kC)))

def lr(p, q, x, y, z):
    return flow(p, q, x, y, y, z, z, z, z)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def det4(matrix):
    a = [list(row) for row in matrix]
    det = O
    for i in range(4):
        piv = next((j for j in range(i, 4) if a[j][i]), None)
        if piv is None:
            return Z
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            det = -det
        v = a[i][i]
        det *= v
        for k in range(i + 1, 4):
            r = a[k][i] / v
            for h in range(i + 1, 4):
                a[k][h] -= r * a[i][h]
    return det

# Uniform two-coordinate answer projection, independent of all eight delays.
reference = {s: H for s in SRC}
L = [lr(reference, reference, *v) for v in LR]
V = [flow(reference, reference, *v) for v in FULL]
expected_answers = ((F(21, 40), F(21, 40)),
                    (F(9, 10), F(3, 20)),
                    (F(3, 4), F(1, 4)),
                    (O, Z), (F(61, 80), F(21, 80)),
                    (F(19, 20), F(3, 40)),
                    (F(7, 8), F(1, 8)), (O, Z))
check(tuple(v[:2] for v in L) == expected_answers, 'eight answer coordinates')
# These four halfplanes enclose exactly the LR answer quadrilateral;
# FULL corners satisfy them, so full and LR answer convex hulls coincide.
faces = ((-11, -9), (1, 1), (-1, -1), (3, 2))
heights = []
for m in faces:
    scores = [dot(m, v[:2]) for v in L]
    h = max(scores)
    heights.append(h)
    check(all(dot(m, f[:2]) <= h for f in V), f'FULL answer hull facet {m}')
check(tuple(heights) == (F(-21, 2), F(21, 20), -O, F(3, 1)),
      'answer hull halfplane constants')
check(tuple(i for i, v in enumerate(L) if dot(faces[0], v[:2]) == heights[0])
      == (0, 2), 'unique edge endpoints L0,L2')
check(tuple(heights[0] - dot(faces[0], v[:2]) for v in L) ==
      (Z, F(3, 4), Z, H, F(1, 4), F(5, 8), F(1, 4), H),
      'exact off-edge exposure slacks')

# On the exposed answer edge, the two opposite FULL corners project to
# the midpoint but acquire exactly opposite P and Q time residuals.
# Because the observer is AFFINE in every independent terminal delay,
# checking all eight delay-cube vertices gives a complete identity proof.
for bits in product((Z, O), repeat=8):
    p = dict(zip(SRC, bits[:4]))
    q = dict(zip(SRC, bits[4:]))
    l0, l2 = lr(p, q, *LR[0]), lr(p, q, *LR[2])
    middle = scale(H, add(l0, l2))
    wplus, wminus = flow(p, q, *FULL[16]), flow(p, q, *FULL[32])
    delta = ((p['BJ'] - p['IJ']) / 16, (q['BJ'] - q['IJ']) / 16)
    check(wplus[:2] == middle[:2] == wminus[:2], 'answer midpoint identity')
    check((wplus[2] - middle[2], wplus[3] - middle[3]) == delta,
          'positive FULL fiber lift')
    check((wminus[2] - middle[2], wminus[3] - middle[3]) ==
          (-delta[0], -delta[1]), 'negative FULL fiber lift')

# Construct an explicit EXACT signed normal for any nonzero BJ/IJ delay
# discrepancy under P or Q, uniformly over the other six delay values.
def separation(p, q, which):
    j = 2 if which == 'P' else 3
    d = p['BJ'] - p['IJ'] if which == 'P' else q['BJ'] - q['IJ']
    ll = [lr(p, q, *v) for v in LR]
    r = -(ll[2][j] - ll[0][j]) / (ll[2][0] - ll[0][0])
    n = (F(-1100) + r, F(-900), O if j == 2 else Z,
         O if j == 3 else Z)
    scores = [dot(n, v) for v in ll]
    h = scores[0]
    check(h == scores[2] == max(scores), 'uniform exposing normal')
    check(all(scores[k] < h for k in (1, 3, 4, 5, 6, 7)),
          'strict off-edge exposure')
    check(abs(r) <= F(160, 9) and sum(abs(a) for a in n) < 2019,
          'uniform normal one-norm bound')
    witness = flow(p, q, *(FULL[16] if d >= 0 else FULL[32]))
    check(dot(n, witness) - h == abs(d) / 16, 'exact lifted support certificate')
    return witness, n, h, abs(d) / 16

ex_p = {'C': F(1, 4), 'I': H, 'BJ': F(2, 3), 'IJ': F(1, 3)}
ex_q = {s: F(1, 3) for s in SRC}
w, normal, h, gap = separation(ex_p, ex_q, 'P')
check(w == (F(51, 80), F(31, 80), F(175, 48), F(43, 12)),
      'concrete all-Q-equal FULL witness')
check(normal == (F(-9865, 9), F(-900), O, Z), 'explicit integer-scalable normal')
check(h == F(-50107, 48) and dot(normal, w) == F(-8351, 8)
      and gap == F(1, 48), 'numerical support certificate')
LE = [lr(ex_p, ex_q, *v) for v in LR]
AE = [[LE[k][i] - LE[0][i] for k in (1, 2, 3, 4)] for i in range(4)]
check(det4(AE) == F(3, 10240), 'LR affine rank-four determinant')
base = [H] * 7
cols = []
for k in (0, 1, 2, 3):
    a = base.copy(); a[k] = O
    b = base.copy(); b[k] = Z
    av, bv = flow(ex_p, ex_q, *a), flow(ex_p, ex_q, *b)
    cols.append(tuple(av[i] - bv[i] for i in range(4)))
check(det4([[cols[k][i] for k in range(4)] for i in range(4)]) ==
      F(-1, 40960), 'FULL interior Jacobian rank-four minor')

# Additional rational, non-corner cross checks for both measures.
for a in range(90):
    vals = [F(((a * (2 * i + 3) + 11 * i + 1) % 43) + 1, 45)
            for i in range(8)]
    p = dict(zip(SRC, vals[:4])); q = dict(zip(SRC, vals[4:]))
    l0, l2 = lr(p, q, *LR[0]), lr(p, q, *LR[2])
    midpoint = scale(H, add(l0, l2))
    v1, v2 = flow(p, q, *FULL[16]), flow(p, q, *FULL[32])
    check(v1[:2] == midpoint[:2] == v2[:2], 'rational answer edge')
    d0, d1 = (p['BJ'] - p['IJ'])/16, (q['BJ'] - q['IJ'])/16
    check(v1[2:]==(midpoint[2]+d0,midpoint[3]+d1), 'rational positive fiber')
    check(v2[2:]==(midpoint[2]-d0,midpoint[3]-d1), 'rational negative fiber')
    if d0:
        separation(p,q,'P')
    if d1:
        separation(p,q,'Q')

print('ANSWER_HULL_EXACT_2D_QUADRILATERAL=TRUE')
print('UNIQUE_LR_EDGE_ANSWER_PROJECTION={0,2}; EXACT_OFF_EDGE_SLACK_MIN=1/4')
print('FIBER_LIFTS=plusminus ((pBJ-pIJ)/16,(qBJ-qIJ)/16)')
print('UNIVERSAL_NECESSARY_EQUALITY pBJ=pIJ AND qBJ=qIJ')
print('UNIFORM_HAUSDORFF_LINF_LOWER_BOUND=max(|pBJ-pIJ|,|qBJ-qIJ|)/32304')
print('EXAMPLE_P',ex_p,'EXAMPLE_Q',ex_q)
print('EXAMPLE_FULL_WITNESS',w)
print('EXAMPLE_NORMAL',normal,'LR_SUPPORT',h,'WITNESS_SUPPORT',dot(normal,w),
      'CERTIFIED_SUPPORT_GAP',gap)
print('EXAMPLE_LR_AFFINE_DET=3/10240 FULL_JACOBIAN_MINOR=-1/40960')
print('EXACT_ASSERTIONS',CHECKS,'FULL_SOURCE_FLOW_EVALUATIONS',FLOWS)
print('PASS_EXACT_R5_INDEPENDENT_PQ_EXPOSED_ANSWER_EDGE')
