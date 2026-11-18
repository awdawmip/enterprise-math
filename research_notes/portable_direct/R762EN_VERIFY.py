#!/usr/bin/env python3
"""R762EN: exact mod-prime zero-return Hankel certificate for q=9.
Only Python standard library; no stochastic data or floating-point arithmetic.
"""
from hashlib import sha256

Q = 9
SHIFTS = ((0, 0, 0), (1, 0, 0), (0, 0, 1),
          (1, 1, 0), (0, 1, 1), (1, 1, 1))
PRIMES = (1000000007, 998244353)
H = 127
SAMPLES = 320


def return_counts_mod(p):
    perms = []
    for a, b, c in SHIFTS:
        perms.append([(((x + a) % Q) * Q + (y + b) % Q) * Q + (z + c) % Q
                      for x in range(Q) for y in range(Q) for z in range(Q)])
    v = [0] * (Q ** 3)
    v[0] = 1
    ret = []
    for _ in range(SAMPLES):
        ret.append(v[0])
        w = [0] * (Q ** 3)
        for perm in perms:
            for i, j in enumerate(perm):
                w[j] += v[i]
        v = [w_i % p for w_i in w]
    return ret


def determinant_mod_hankel(seq, order, p, start=0):
    a = [[seq[start + i + j] for j in range(order)] for i in range(order)]
    d = 1
    for k in range(order):
        pivotrow = next((i for i in range(k, order) if a[i][k]), None)
        if pivotrow is None:
            return 0
        if pivotrow != k:
            a[k], a[pivotrow] = a[pivotrow], a[k]
            d = -d
        pivot = a[k][k]
        d = d * pivot % p
        inv = pow(pivot, p - 2, p)
        for i in range(k + 1, order):
            z = a[i][k] * inv % p
            if z:
                for j in range(k + 1, order):
                    a[i][j] = (a[i][j] - z * a[k][j]) % p
                a[i][k] = 0
    return d % p


def berlekamp_massey(seq, p):
    # Gives sum(C[j] * seq[n-j], j=0..L) == 0 for n >= L.
    c, b, L, m, old_delta = [1], [1], 0, 1, 1
    for n in range(len(seq)):
        delta = sum(c[j] * seq[n - j] for j in range(L + 1)) % p
        if not delta:
            m += 1
            continue
        saved = c[:]
        factor = delta * pow(old_delta, p - 2, p) % p
        if len(c) < len(b) + m:
            c += [0] * (len(b) + m - len(c))
        for j, bj in enumerate(b):
            c[j + m] = (c[j + m] - factor * bj) % p
        if 2 * L <= n:
            L, b, old_delta, m = n + 1 - L, saved, delta, 1
        else:
            m += 1
    return L, c


def main():
    assert Q == 9 and len(SHIFTS) == 6
    for p in PRIMES:
        seq = return_counts_mod(p)
        assert seq[:9] == [1] * 9 and seq[9] == 6
        h127 = determinant_mod_hankel(seq, H, p)
        h128 = determinant_mod_hankel(seq, H + 1, p)
        shifted126 = determinant_mod_hankel(seq, H - 1, p, start=1)
        shifted127 = determinant_mod_hankel(seq, H, p, start=1)
        degree, c = berlekamp_massey(seq[:2 * H], p)
        assert degree == H and h127 != 0 and h128 == 0
        assert shifted126 != 0 and shifted127 == 0
        assert all(sum(c[j] * seq[n - j] for j in range(degree + 1)) % p == 0
                   for n in range(degree, SAMPLES))
        digest = sha256(','.join(map(str, seq[:2 * H])).encode()).hexdigest()
        print({'prime': p, 'hankel_127_det_mod_p': h127,
               'hankel_128_det_mod_p': h128,
               'shifted_hankel_126_det_mod_p': shifted126,
               'shifted_hankel_127_det_mod_p': shifted127,
               'BM_degree': degree, 'samples': SAMPLES,
               'sha256_first_254_decimal_csv': digest,
               'independent_tail_check': 'PASS'})


if __name__ == '__main__':
    main()
