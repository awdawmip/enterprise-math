#!/usr/bin/env python3
"""R284AX one scalar determinant with simultaneous independent star-edge strengths.
Standard-library exact integer verification, deterministic and reproducible.
"""
from itertools import combinations, product
from math import factorial
from random import Random
from hashlib import sha256
import json
from pathlib import Path


def det_bareiss(matrix):
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prior = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                val = a[i][j] * pivot - a[i][k] * a[k][j]
                assert val % prior == 0
                a[i][j] = val // prior
            a[i][k] = 0
        prior = pivot
    return sign * a[-1][-1]


def separating_weights(n):
    # Each k-subset sum, k=1,2,3, is unique. R284AU greedy construction.
    ws = []
    for t in range(n):
        forbidden = set()
        for k in (1, 2, 3):
            if k <= t:
                for aa in combinations(ws, k - 1):
                    for bb in combinations(ws, k):
                        forbidden.add(sum(bb) - sum(aa))
        w = ws[-1] + 1 if ws else 1
        while w in forbidden:
            w += 1
        ws.append(w)
    for k in (1, 2, 3):
        s = [sum(ss) for ss in combinations(ws, k)]
        assert len(s) == len(set(s))
    return ws


def balanced_digits(y, b):
    out = {}
    pos = 0
    while y:
        y, rem = divmod(y, b)
        if rem >= b // 2:
            rem -= b
            y += 1
        if rem:
            out[pos] = rem
        pos += 1
    return out


def recover_from_one_read(C, H):
    n = len(C)
    assert n >= 2 and H >= 1
    assert all(len(row) == n for row in C)
    assert all(1 <= int(x) <= H for row in C for x in row)
    w = separating_weights(n)
    W = 1 + sum(w)
    def exponent(present):
        return len(present) * W + sum(w[i] for i in present)
    E = exponent(range(n))
    R = E + 1
    A = (2**n) * factorial(n) * H**n
    B = 1 << (2 * A).bit_length()
    assert B > 2 * A
    D = [B ** (W + w_i) for w_i in w]
    Z = [0] + [B ** (v * R) for v in range(1, n)]
    X = [[(D[i] if i == j else 0) - C[i][j]
          - (Z[j] if i == 0 and j != 0 else 0)
          for j in range(n)] for i in range(n)]
    y = det_bareiss(X)
    digits = balanced_digits(y, B)
    # Block 0 is F(D), block v>=1 is G_v(D): no baselines measured separately.
    def coefficient(block, absent):
        present = tuple(i for i in range(n) if i not in absent)
        return digits.get(block * R + exponent(present), 0)
    a = [-coefficient(0, {i}) for i in range(n)]
    P = {(i,j): a[i] * a[j] - coefficient(0, {i, j})
         for i in range(n) for j in range(i + 1, n)}
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        out[i][i] = a[i]
    for v in range(1, n):
        c_v0 = -coefficient(v, {0, v})
        assert c_v0 > 0 and P[0, v] % c_v0 == 0
        out[v][0], out[0][v] = c_v0, P[0, v] // c_v0
    for i in range(1, n):
        for j in range(i + 1, n):
            numerator = a[j] * out[i][0] - coefficient(i, {0, i, j})
            assert out[j][0] > 0 and numerator % out[j][0] == 0
            cij = numerator // out[j][0]
            assert cij > 0 and P[i, j] % cij == 0
            out[i][j], out[j][i] = cij, P[i, j] // cij
    assert out == C
    return dict(n=n, H=H, readings=1,
                max_diagonal_bits=max(d.bit_length() for d in D),
                max_star_strength_bits=max(z.bit_length() for z in Z),
                output_bits=y.bit_length(),
                radix_bits=B.bit_length() - 1, separator=R,
                digest=sha256(y.to_bytes(max(1, (y.bit_length()+8)//8), "big", signed=True)).hexdigest())


def check_affine_row_identity(C, H):
    n = len(C)
    d = [i + 3 for i in range(n)]
    def calc(strengths):
        return det_bareiss([[d[i] * (i == j) - C[i][j]
                             - (strengths[j] if i == 0 and j > 0 else 0)
                             for j in range(n)] for i in range(n)])
    baseline = calc([0] * n)
    effects = []
    for v in range(1, n):
        zz = [0] * n
        zz[v] = 1
        effects.append(calc(zz) - baseline)
    strengths = [0] + [(-1)**v * (v + 2) for v in range(1, n)]
    assert calc(strengths) == baseline + sum(strengths[v] * effects[v - 1] for v in range(1, n))


def main():
    rng = Random(2842824)
    cases = []
    affine_checks = 0
    for n, count in ((2, 15), (3, 20), (4, 16), (5, 10), (6, 3)):
        for _ in range(count):
            H = rng.randint(1, 4)
            C = [[rng.randint(1, H) for _ in range(n)] for _ in range(n)]
            cases.append(recover_from_one_read(C, H))
            check_affine_row_identity(C, H)
            affine_checks += 1
    for arr in product((1, 2), repeat=9):
        C = [list(arr[i*3:i*3+3]) for i in range(3)]
        cases.append(recover_from_one_read(C, 2))
    for _ in range(30):
        C = [[rng.randrange(1,4) for _ in range(3)] for _ in range(3)]
        cases.append(recover_from_one_read(C, 3))
    report = {
        'research_unit': 'R284AX',
        'status': 'PASS',
        'seed': 2842824,
        'measurement_model': 'single determinant, simultaneous n-1 nonnegative integer strengths on row-0 star, known H',
        'exact_integer_reconstructions': len(cases),
        'binary_3x3_exhaustive': 512,
        'ternary_3x3_sample': 30,
        'random_other_instances': 64,
        'independent_row_affinity_checks': affine_checks,
        'max_output_bits': max(x['output_bits'] for x in cases),
        'max_diagonal_bits': max(x['max_diagonal_bits'] for x in cases),
        'max_star_strength_bits': max(x['max_star_strength_bits'] for x in cases),
        'sample': cases[0],
        'finite_test_scope': 'n=2..6; exact integer computations, deterministic seed, no independent peer review',
        'general_theorem_basis': 'separate algebraic proof in accompanying note',
        'review': 'NOT_REVIEWED',
    }
    file = Path(__file__).with_name('R284AX_simultaneous_star_single_read_verification.json')
    file.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
