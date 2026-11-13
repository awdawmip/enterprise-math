"""Exact rational verifier for the R5 K-source vector rigidity theorem.

The analytic theorem is in RESEARCH.md; this script checks independent finite
support computations, explicit witnesses, affine rank, and real-policy
aggregation at selected rational parameters. Python stdlib only.
"""
from fractions import Fraction as F
from itertools import product, combinations

M = (F(1, 4), F(1, 4), F(1, 8), F(1, 8))
CASES = [
    (F(3, 5), F(2, 5), (F(1, 4), F(2, 3), F(5, 8), F(3, 7)),
     (F(1, 3), F(4, 5), F(2, 7), F(9, 20))),
    (F(1, 2), F(1, 3), (F(1, 3),) * 4, (F(2, 3),) * 4),
    (F(1, 4), F(2, 5), (F(1, 4), F(1, 4), F(3, 4), F(1, 4)), (F(1, 2),) * 4),
    (F(3, 4), F(1, 4), (F(2, 3),) * 4, (F(1, 4), F(1, 4), F(3, 4), F(1, 4))),
    (F(1, 5), F(4, 5), (F(1, 8), F(7, 8), F(2, 5), F(3, 5)),
     (F(5, 7), F(1, 7), F(3, 8), F(7, 8))),
    (F(7, 8), F(1, 8), (F(1, 10), F(9, 10), F(1, 10), F(9, 10)),
     (F(9, 10), F(1, 10), F(9, 10), F(1, 10))),
    (F(1, 3), F(2, 3), (F(4, 9),) * 4, (F(5, 9),) * 4),
    (F(4, 7), F(3, 7), (F(1, 3), F(2, 3), F(1, 3), F(2, 3)),
     (F(2, 3), F(1, 3), F(2, 3), F(1, 3))),
]


def observer(t, policy):
    """t=(a,b,U[4],V[4]); policy=(x,jB,jI,k[4]); exact source flow."""
    a, b, u, v = t
    x, jb, ji, *k = map(F, policy)
    db = (1 - jb) / 8
    di = (1 - x) * (1 - ji) / 8
    d = db + di
    w = (F(1, 4), (1 - x) / 4, db, di)
    c = [w[s] * (1 - k[s]) for s in range(4)]
    csum = sum(c)
    base = F(5, 2) - 3*x/4 + 2*d
    return (1 - a*d - sum(u[s]*c[s] for s in range(4)),
            b*d + sum(v[s]*c[s] for s in range(4)),
            base + 3*csum/2,
            base + 4*csum/3)


def lr_policy(x, y, z):
    return (x, y, y, z, z, z, z)


def inner(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm1(a):
    return sum(map(abs, a))


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(len(a)))


def rank4_witness(vertices):
    for inds in combinations(range(1, len(vertices)), 4):
        d = det([[vertices[i][j] - vertices[0][j] for j in range(4)]
                 for i in inds])
        if d:
            return inds, d
    return None


def support_normal(kernel, law):
    mean = sum(M[i]*kernel[i] for i in range(4))/sum(M)
    n = ((1, 0) if law == 'P' else (0, -1)) + (6*mean-32, 36-6*mean)
    return mean, n


def case_support(t, vertices_full, vertices_lr, kernel, law):
    mean, n = support_normal(kernel, law)
    a, b, _, _ = t
    baseline = 13-a/4 if law == 'P' else 12-b/4
    predicted = sum(M[i]*max(F(0), mean-kernel[i]) for i in range(4))
    # The maximizing face is x=jB=jI=0. Continue only below-mean sources.
    policy = (0, 0, 0) + tuple(0 if kernel[i] < mean else 1 for i in range(4))
    witness = observer(t, policy)
    assert max(inner(n, o) for o in vertices_lr) == baseline
    assert max(inner(n, o) for o in vertices_full) == baseline + predicted
    assert inner(n, witness) == baseline + predicted
    assert predicted == sum(M[i]*abs(mean-kernel[i]) for i in range(4))/2
    assert norm1(n) == 69-12*mean
    assert predicted >= (max(kernel)-min(kernel))/16
    return predicted, mean, n, witness, predicted/norm1(n)


checks = 0
for index, t in enumerate(CASES):
    a, b, u, v = t
    assert 0 < a < 1 and 0 < b < 1
    assert all(0 < z < 1 for z in u+v)
    full_vertices = [observer(t, p) for p in product((0, 1), repeat=7)]
    lr_vertices = [observer(t, lr_policy(*p)) for p in product((0, 1), repeat=3)]
    checks += 2
    for law, kernel in [('P', u), ('Q', v)]:
        gap, mean, n, witness, distance = case_support(t, full_vertices, lr_vertices, kernel, law)
        checks += 6
        if len(set(kernel)) == 1:
            assert gap == 0
        else:
            assert gap > 0
        checks += 1
        print('CASE', index, law, 'MEAN', mean, 'GAP', gap,
              'DIST_LINF', distance, 'NORMAL', n, 'WITNESS', witness)
    rank = rank4_witness(lr_vertices)
    print('CASE', index, 'LR_RANK4', rank)
    if index == 0:
        assert rank is not None
        checks += 1
    if len(set(u)) == len(set(v)) == 1:
        for q in range(36):
            p = [F(((7*q+11*i*i+5*i)%23)+1, 25) for i in range(7)]
            x, jb, ji, *k = p
            db = (1-jb)/8
            di = (1-x)*(1-ji)/8
            weights = (F(1, 4), (1-x)/4, db, di)
            y = (jb+(1-x)*ji)/(2-x)
            z = sum(weights[i]*k[i] for i in range(4))/sum(weights)
            assert 0 <= y <= 1 and 0 <= z <= 1
            assert observer(t, p) == observer(t, lr_policy(x, y, z))
            checks += 2

print('PASS_EXACT_R5_K_SOURCE_VECTOR_RIGIDITY', checks, 'assertions',
      len(CASES)*128, 'FULL vertices,', len(CASES)*8, 'LR vertices')
