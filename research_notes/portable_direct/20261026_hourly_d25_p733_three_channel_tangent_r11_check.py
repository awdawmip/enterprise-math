#!/usr/bin/env python3
"""Non-native finite-ring corrected-Clausen three-channel Ward check.
Original-class crystalline Frobenius / H0/B0 experiments are NOT performed.
"""
from functools import lru_cache
from pathlib import Path
from runpy import run_path

_helper = run_path(str(Path(__file__).with_name(
    '20261026_hourly_d25_ward_adjoint_two_digit_tangent_r11_check.py')))
direct_adjoint = _helper['direct_adjoint']
expansion = _helper['expansion']
CHANNELS = ((0, 2), (1, 2), (0, 3))


def check(p):
    assert (p - 1) % 6 == 0
    m = (p - 1) // 6
    N = 2 * m - 1
    L = -N
    q = p * p
    inv2 = pow(2, -1, q)
    inv = lambda x: pow(x % q, -1, q)
    u = [[0] * p for _ in range(4)]
    u[0][0] = 1
    for a in range(4):
        for r in range(1, p):
            take = lambda b, s: u[b][s] if b >= 0 and s >= 0 else 0
            numerator = ((r - 1 - m) * (r - 1 - 2 * m) * take(a, r - 1)
                         + 3 * r * take(a - 1, r)
                         - (3 * (r - 1) - 4 * m) * take(a - 1, r - 1)
                         + 2 * take(a - 2, r - 1))
            u[a][r] = numerator * inv(r * (r - p * inv2)) % q

    def scalar(a, r):
        return u[a][r] if a >= 0 and 0 <= r < p else 0

    @lru_cache(None)
    def M(a, b, n, s=0):
        if a < 0 or b < 0:
            return 0
        ans = 0
        for j in range(max(1, 1 - n), min(2 * m, 2 * m - n) + 1):
            ell = j + n
            ans += pow(j, s, q) * scalar(a, j) * scalar(b, p - ell)
        return ans % q

    def source(a, b, n):
        J = (3 * M(a - 1, b, n, 1) - 3 * M(a - 1, b, n + 1, 1)
             + 4 * m * M(a - 1, b, n + 1) + 2 * M(a - 2, b, n + 1)
             - 3 * ((p - n) * M(a, b - 1, n) - M(a, b - 1, n, 1))
             + (14 * m - 3 * n) * M(a, b - 1, n + 1)
             - 3 * M(a, b - 1, n + 1, 1) - 2 * M(a, b - 2, n + 1))
        if n >= 0:
            E = ((2 * m * m * (a == 0) + 4 * m * (a == 1) + 2 * (a == 2))
                 * scalar(b, p - n - 1)
                 + scalar(a, 2 * m - n) *
                 (-6 * m * m * scalar(b, 4 * m) +
                  8 * m * scalar(b - 1, 4 * m) -
                  2 * scalar(b - 2, 4 * m)))
        else:
            E = (scalar(a, -n) *
                 (20 * m * m * scalar(b, p - 1) -
                  14 * m * scalar(b - 1, p - 1) +
                  2 * scalar(b - 2, p - 1))
                 + scalar(b, p - (2 * m + n + 1)) *
                 (2 * m * scalar(a - 1, 2 * m) -
                  2 * scalar(a - 2, 2 * m)))
        return (J + E) % q

    def Y(a, b, n):
        return (M(a, b, n, 1) - (p - n) * inv2 * M(a, b, n)) % q

    lam = {0: 0}
    for k in range(0, L, -1):
        neg_power = inv(pow(2, -k, q))
        lam[k - 1] = ((p - 2 * k) * lam[k] - neg_power) * inv(p - 2 * k + 1) % q
    direct, delta = direct_adjoint(p, q)
    assert all(lam[-t] == direct[t] for t in range(N + 1))
    _, delta2, d0, d1, _ = expansion(p, q)
    assert delta == delta2 == (inv(pow(2, N, q)) - (p + 2 * N) * lam[L]) % q

    records = []
    total_ward = 0
    for a, b in CHANNELS:
        for n in range(L, 2 * m):
            assert ((p - 2 * n) * Y(a, b, n)
                    - (p - 2 * n - 1) * Y(a, b, n + 1)
                    - source(a, b, n)) % q == 0, (p, a, b, n, 'WARD')
            total_ward += 1
        w = lambda n: pow(2, n, q) if n >= 0 else inv(pow(2, -n, q))
        U = sum(w(n) * M(a, b, n) for n in range(L, 1)) % q
        T = sum(w(n) * (1 - 6 * n) * M(a, b, n) for n in range(L, 1)) % q
        K = sum(w(n) * M(a, b, n, 1) for n in range(L, 1)) % q
        R = sum(w(n) * Y(a, b, n) for n in range(L, 1)) % q
        source_adj = sum(lam[n] * source(a, b, n) for n in range(L, 0)) % q
        edge_adj = delta * Y(a, b, L) % q
        assert R == (source_adj + edge_adj) % q, (p, a, b, 'ADJOINT')
        assert T == ((1 - 6 * p) * U + 12 * K - 12 * R) % q, (p, a, b, 'T')
        records.append({
            'channel': (a, b), 'U': U, 'T': T, 'K': K, 'R': R,
            'J_E_adjoint': source_adj, 'left_face_adjoint': edge_adj,
            'raw_left_face': Y(a, b, L), 'delta': delta
        })
    if p == 13:
        assert [[x[k] for k in ('U', 'T', 'K', 'R', 'J_E_adjoint',
                                'left_face_adjoint')] for x in records] == [
            [138, 130, 99, 104, 104, 0],
            [80, 41, 154, 102, 30, 72],
            [69, 113, 13, 96, 96, 0],
        ]
    if p == 733:
        assert delta == 176653 and d0 == 142202 and d1 % p == 47
        middle = next(x for x in records if x['channel'] == (1, 2))
        assert middle['raw_left_face'] % p == 610
        assert middle['left_face_adjoint'] == p * 410
        assert records[0]['left_face_adjoint'] == 0
        assert records[2]['left_face_adjoint'] == 0
        assert [[x[k] for k in ('U', 'T', 'K', 'R', 'J_E_adjoint',
                                'left_face_adjoint', 'raw_left_face')]
                for x in records] == [
            [194980, 14284, 492593, 506918, 506918, 0, 0],
            [225095, 108012, 109186, 140261, 377020, 300530, 268155],
            [400749, 526050, 300290, 229559, 229559, 0, 0],
        ]
    print('PASS', p, 'Ward cells', total_ward,
          'adjoint and T-port checks', 2 * len(CHANNELS),
          'records=', records)
    return records


if __name__ == '__main__':
    check(13)
    check(733)
