"""EC18 finite exact integer regression; universality comes from the proof, not this test."""
from collections import defaultdict
from fractions import Fraction
from math import comb

EDGES = {
    0: {0: (2, -1, -1), 1: (2, 1, -1)},
    1: {0: (0, -1, -1), 1: (0, 1, -1)},
    2: {0: (1, 1, 1), 1: (2, 1, -1)}
}

def rows(N):
    E = []
    for n in range(N + 1):
        a = [0] * (n + 1)
        for k in range(n + 1):
            v = int(n == 0 and k == 0) - int(n == 2 and k == 1)
            if n:
                v += E[n - 1][k] if k < n else 0
                v += E[n - 1][k - 1] if k else 0
            if n >= 4 and 2 <= k <= n - 2:
                v -= 2 * E[n - 4][k - 2]
            if n >= 6 and 3 <= k <= n - 3:
                v += E[n - 6][k - 3]
            a[k] = v
        E.append(a)
    return E

def clean_dp(N):
    state = {(0, 0, 1, 0): 1}
    out = [{0: 1}]
    for n in range(1, N + 1):
        nxt = defaultdict(int)
        for (q, last_zero, e, k), mass in state.items():
            for bit in (0, 1):
                if last_zero and bit == 0:
                    continue
                qq, eta, b = EDGES[q][bit]
                ee = eta * e
                assert ee * b == e * (1 - 2 * bit)
                nxt[(qq, int(bit == 0), ee, k + int(ee * b == -1))] += mass
        state = nxt
        r = defaultdict(int)
        for (_, _, _, k), mass in state.items():
            r[k] += mass
        out.append(dict(r))
    return out

def main():
    N = 300
    E, C = rows(N), clean_dp(100)
    tested = 0
    for n in range(N + 1):
        assert E[n] == E[n][::-1]
        for k in range(1, n // 2 + 1):
            if n >= 4 * k * k:
                assert Fraction(E[n][k] - E[n][k - 1], comb(n, k - 1)) > Fraction(13, 99)
                tested += 1
        if n < len(C):
            for k in range(n + 1):
                c = E[n][k] - (E[n - 3][k - 1] if n >= 3 and 1 <= k <= n - 2 else 0)
                assert c == C[n].get(k, 0)
    assert E[10][3] ** 2 == 529 < 575 == E[10][2] * E[10][4]
    print('PASS; integer wedge checks:', tested, 'n<=', N, 'nonlogconcavity n=10')

if __name__ == '__main__':
    main()
