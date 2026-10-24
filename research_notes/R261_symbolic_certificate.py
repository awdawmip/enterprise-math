"""R261: exact Laurent-linear Hankel certificate for the fixed R256--R260 model.
This is an author-side symbolic computation, NOT a native heartbeat simulation.
Requires Python 3 and SymPy; all arithmetic is exact.
"""
import json
import sympy as sp

STATES = ((0, 0), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
EDGE = {
    0: ((2, -1, -1), (2, +1, -1)),
    1: ((0, -1, -1), (0, +1, -1)),
    2: ((1, +1, +1), (2, +1, -1)),
}

def monitor(r, a):
    return ((1, 2, 2) if a == 0 else (0, 0, 2))[r]

def matrices(x):
    index = {state: i for i, state in enumerate(STATES)}
    A = sp.zeros(14)
    for src, (q, r) in enumerate(STATES):
        for a in (0, 1):
            q1, eta, b = EDGE[q][a]
            dest = index[(q1, monitor(r, a))]
            swap = sp.eye(2) if eta == 1 else sp.Matrix([[0, 1], [1, 0]])
            effect = sp.diag(x**b, x**(-b)) * swap
            for i in (0, 1):
                for j in (0, 1):
                    A[2 * dest + i, 2 * src + j] += effect[i, j]
    C = sp.zeros(12, 14)
    for src, (q, r) in enumerate(STATES):
        for parity in (0, 1):
            C[2 * (2 * q + int(r == 2)) + parity, 2 * src + parity] = 1
    v = sp.zeros(14, 1)
    v[0] = 1
    return A, C, v

def main():
    x = sp.Symbol('x', nonzero=True)
    z = sp.Symbol('z')
    A, C, v = matrices(x)
    expected_char = -z**2 * (z**2 + 1) * (x**2 - x*z + 1) * (
        x**2 - x*z**3 - x*z + 1
    ) * (x**2*z**5 - x*z**6 - 2*x*z**2 + x + z**5) / x**3
    assert sp.cancel(A.charpoly(z).as_expr() - expected_char) == 0
    p = sp.Poly(sp.cancel(expected_char / z), z)
    assert p.degree() == 13 and p.LC() == 1
    residual = sp.zeros(14)
    for coefficient in p.all_coeffs():
        residual = (residual * A + coefficient * sp.eye(14)).applyfunc(sp.cancel)
    assert residual == sp.zeros(14), 'p13(A) is not zero'
    assert A.rank() == 12 and (A * A).rank() == 12
    A2 = A.subs(x, sp.Integer(2))
    v2 = v.copy()
    seq = []
    for n in range(25):
        seq.append((C * v2)[2])  # terminal q=0, contains 00, parity +
        v2 = A2 * v2
    hankel = sp.Matrix(13, 13, lambda i, j: seq[i + j])
    determinant = hankel.det()
    exact = sp.Rational(163341851565859597265625, 1099511627776)
    assert determinant == exact and determinant != 0
    # Coarser observer x=1 forgets the translation k while retaining eps.
    A1 = A.subs(x, sp.Integer(1))
    p11 = sp.Poly(z * (z - 2) * (z - 1) * (z**2 + 1) *
                   (z**2 - z - 1) * (z**2 + z + 1) *
                   (z**2 + z + 2), z)
    assert p11.degree() == 11 and p11.LC() == 1
    annihilate_start = v.copy() * 0
    for coefficient in p11.all_coeffs():
        annihilate_start = A1 * annihilate_start + coefficient * v
    assert annihilate_start == sp.zeros(14, 1)
    v1 = v.copy()
    seq1 = []
    for _ in range(21):
        seq1.append((C * v1)[2])
        v1 = A1 * v1
    H11 = sp.Matrix(11, 11, lambda i, j: seq1[i + j])
    assert H11.det() == 151782400
    report = {
        'status': 'PASS',
        'classification': 'AUTHOR_SIDE_EXACT_SYMBOLIC_CERTIFICATE',
        'source_model': 'R260 formal 3-control, 2-choice, 7-reachable-monitor-state BRC',
        'lifted_dimension': 14,
        'minimal_laurent_linear_dimension_over_Qx': 13,
        'charpoly_factored': str(sp.factor(expected_char)),
        'annihilator_degree': p.degree(),
        'annihilator_matrix_identity': True,
        'rank_A_over_Qx': 12,
        'rank_A2_over_Qx': 12,
        'specialization': 'x=2',
        'hankel_order': 13,
        'hankel_det_numerator': str(sp.numer(determinant)),
        'hankel_det_denominator': str(sp.denom(determinant)),
        'forget_translation_x1_minimal_order': 11,
        'forget_translation_x1_hankel_11_det': '151782400',
        'forget_translation_x1_annihilator': str(sp.factor(p11.as_expr())),
        'seq_first_16': [str(v) for v in seq[:16]],
        'scope': 'one repeated summed packet, complete formal affine-effect/query output, NOT native heartbeat or original R193'
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
