"""Exact all-real q certificates for the R5 ingress-sensitive four-observer projection.

Auxiliary two-measure finite stopping model; standard-library Fraction arithmetic.
This is author-side mathematical evidence, not a native X6/BRC execution.
"""
from fractions import Fraction as Q
from itertools import product

ALPHA = (Q(1, 4), Q(1, 5))
KAPPA = (Q(3, 4), Q(1, 6))
LEAVES = ('A', 'D', 'Y', 'C', 'DH', 'YH', 'LD', 'LY', 'LC', 'L4D', 'L4Y', 'L4C')
TIME = (1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4)
RATIO = (Q(1), Q(1, 2), Q(3, 2), Q(1), Q(1, 4), Q(2),
         Q(1), Q(1), Q(1), Q(1), Q(1), Q(1))
KEY_INDEX = {key: j for j, key in enumerate(LEAVES)}


def mass(bits):
    """Twelve source/ingress-preserving terminal Q masses; bit order per source:
    A, D, Y, LD, LY, LC (1 means CONTINUE)."""
    out = [Q(0)] * len(LEAVES)
    def add(key, amount):
        out[KEY_INDEX[key]] += amount
    for i, (alpha, kappa) in enumerate(zip(ALPHA, KAPPA)):
        a, d, y, ld, ly, lc = bits[6*i:6*i+6]
        c0 = Q(1, 2) * a
        add('A', Q(1, 2) - c0)
        dm = c0 * alpha
        ym = c0 * alpha
        cm = c0 * (1 - 2*alpha)
        if d:
            add('DH', 2*dm/3)
            add('L4D' if ld else 'LD', dm/3)
        else:
            add('D', dm)
        if y:
            add('YH', ym/2)
            add('L4Y' if ly else 'LY', ym/2)
        else:
            add('Y', ym)
        add('C', cm*(1-kappa))
        add('L4C' if lc else 'LC', cm*kappa)
    assert min(out) >= 0
    assert sum(out) == sum(v*r for v, r in zip(out, RATIO)) == 1
    return tuple(out)


def reduced(flow):
    x = flow[KEY_INDEX['DH']]
    u = flow[KEY_INDEX['YH']]
    t = sum(v*tt for v, tt in zip(flow, TIME))
    y = sum(flow[KEY_INDEX[k]] for k in ('L4D', 'L4Y', 'L4C'))
    c = flow[KEY_INDEX['LC']]
    return x, u, t, y, c


def project(v, q):
    return v[:3] + (v[3] + q*v[4],)


def dot(v, w):
    return sum(a*b for a, b in zip(v, w))


def determinant(matrix):
    a = [list(row) for row in matrix]
    answer = Q(1)
    for col in range(len(a)):
        i = next((i for i in range(col, len(a)) if a[i][col]), None)
        if i is None:
            return Q(0)
        if i != col:
            a[i], a[col] = a[col], a[i]
            answer = -answer
        p = a[col][col]
        answer *= p
        for i in range(col+1, len(a)):
            ratio = a[i][col]/p
            for j in range(col, len(a)):
                a[i][j] -= ratio*a[col][j]
    return answer


def minor4(vertices, inds, q):
    p = project(vertices[inds[0]], q)
    return determinant([[project(vertices[i], q)[k]-p[k]
                         for k in range(4)] for i in inds[1:]])


# Each cert is n(q) dot (x,u,t,y+q*c) <= b(q),
# with n(q) = n0 + q*n1 and b(q) = b0 + q*b1.
CERTS = {
    'A': {'n0': (-21, -61, -19, 118), 'n1': (0, 0, 0, 0),
          'b0': -19, 'b1': 0,
          'face': (0, 9, 11, 13), 'full': 4032},
    'B': {'n0': (-891, -5544, 0, 1782), 'n1': (684, 5510, -342, 0),
          'b0': 0, 'b1': -342,
          'face': (0, 8, 11, 15), 'full': 3968},
    'C': {'n0': (3360, 4480, -2240, 2240), 'n1': (-3040, -3040, 1520, 0),
          'b0': -5012, 'b1': 3933,
          'face': (8, 10, 11, 15), 'full': 2750},
}
LEFT = Q(99, 118)
RIGHT = Q(2772, 2413)


def slack(spec, vertex, q):
    normal = tuple(a+q*b for a, b in zip(spec['n0'], spec['n1']))
    return dot(normal, project(vertex, q)) - (spec['b0']+q*spec['b1'])


def affine_slack(spec, vertex):
    a = slack(spec, vertex, Q(0))
    b = slack(spec, vertex, Q(1)) - a
    # n_s(q) is constant, hence no q^2 term.
    assert spec['n1'][3] == 0
    assert slack(spec, vertex, Q(2)) == a + 2*b
    return a, b


def main():
    assert all((1+k*(1-2*a))/a == Q(11, 2)
               for a, k in zip(ALPHA, KAPPA))
    fbits = list(product((0, 1), repeat=12))
    lbits = list(product((0, 1), repeat=4))
    full = [reduced(mass(b)) for b in fbits]
    lr = [reduced(mass((b[0], b[1], b[2], b[3], b[3], b[3])*2))
          for b in lbits]
    assert len(full) == 4096 and len(lr) == 16
    assert LEFT < RIGHT
    # 4D LR affine rank holds for every real q: the determinant is affine in q,
    # and its exact values at q=0,1 are equal and nonzero.
    rank_ids = (0, 9, 10, 13, 14)
    rank_value = Q(8019, 5120000)
    assert minor4(lr, rank_ids, Q(0)) == rank_value
    assert minor4(lr, rank_ids, Q(1)) == rank_value
    assert minor4(lr, rank_ids, Q(2)) == rank_value
    print('POLICY_COUNTS FULL=4096 LR=16; P/Q rational normalization PASS')
    print('LR_FOUR_DIM_RANK_ALL_REAL_Q minor(0,9,10,13,14)=8019/5120000')
    for name, cert in CERTS.items():
        # All four face vertices saturate the same symbolic supporting plane.
        for j in cert['face']:
            assert affine_slack(cert, lr[j]) == (Q(0), Q(0))
        for v in lr:
            a, b = affine_slack(cert, v)
            if name == 'A':
                assert b >= 0 and a+b*LEFT <= 0  # q <= LEFT
            elif name == 'B':
                assert a+b*LEFT <= 0 and a+b*RIGHT <= 0
            else:
                assert b <= 0 and a+b*RIGHT <= 0  # q >= RIGHT
        witness = full[cert['full']]
        wa, wb = affine_slack(cert, witness)
        if name == 'A':
            assert (wa, wb) == (Q(11, 2), Q(0))
        elif name == 'B':
            assert (wa, wb) == (-Q(1881, 8), Q(1517, 4))
            assert wa+wb*LEFT == Q(9801, 118) > 0
        else:
            assert (wa, wb) == (Q(0), Q(171))
            assert wa+wb*RIGHT == Q(24948, 127) > 0
        print(f'CERT_{name} LR_ALL_16_ALL_REAL_INTERVAL PASS; FULL_BITS={"".join(map(str,fbits[cert["full"]]))}; WITNESS_GAP={wa}+({wb})*q')
    print('PARAMETER_COVER (-inf,99/118] UNION [99/118,2772/2413] UNION [2772/2413,+inf)=R')
    print('THEOREM: forall q in R, rank(conv LR4)=4 and conv FULL4 != conv LR4')
    print('SCOPE auxiliary two-measure route-labelled stopping model; not native X6 theorem; independent review pending')
    print('PASS_EXACT_R5_INGRESS_Q_ALL_REAL_NO_GO')


if __name__ == '__main__':
    main()
