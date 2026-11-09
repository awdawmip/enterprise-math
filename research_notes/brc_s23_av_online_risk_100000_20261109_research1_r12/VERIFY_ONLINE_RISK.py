#!/usr/bin/env python3
"""Stdlib, integer-exact O(N log N) certificate for frozen S23/AV R(128,L).

Run: python VERIFY_ONLINE_RISK.py [max_horizon]
All decisions are made with the integer endpoints of a strict rational theta
bracket. Reported affine expressions are exact for every theta in that bracket.
"""
from heapq import heappush, heappop
from fractions import Fraction
import sys

P = 262204504569236716045286
Q = 10**24
M = 128


def ev(e, end=P):
    return Q * e[0] + end * e[1]


def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])


def minus(a, b):
    return (a[0] - b[0], a[1] - b[1])




def certify_theta():
    """Two-sided rational log certificates, no floating-point comparisons."""
    def log_bounds(z, terms=160):
        acc = Fraction(0)
        term = z
        for k in range(terms):
            acc += 2 * term / (2*k+1)
            term *= z*z
        return acc, acc + 2*term / ((2*terms+1) * (1-z*z))
    a, b = log_bounds(Fraction(3,4))       # ln 7
    c, d = log_bounds(Fraction(3,17))      # ln(10/7)
    rlo, rhi = a/d, b/c
    assert 79*rlo > 431
    def theta(r):
        return 79 * (2074774 - 380295*r) / (79*r-431) - 46
    # Strictly decreasing in r, since d theta / dr = -79/(79r-431)^2.
    assert Fraction(P,Q) < theta(rhi) < theta(rlo) < Fraction(P+1,Q)
    print('CERTIFIED_THETA_FROM_160_TERM_LOG_BOUNDS')


def independent_partition_risk(n, ph):
    """Reference formula independently recomputed from complete partition P_n."""
    order = sorted(range(n), key=lambda j: ev(ph[j]))
    best = {}
    parent = None
    for k,j in enumerate(order):
        if j < M:
            parent = j
        if parent is None:
            # The initial circular segment is owned by the last anchor.
            parent = next(i for i in reversed(order) if i<M)
        t = order[(k + 1) % n]
        g = gap(ph[j], ph[t])
        if parent not in best or ev(g)>ev(best[parent]):
            best[parent]=g
    assert len(best)==M
    # Different linear expressions might cross: check that winners remain
    # the same at the other strict interval endpoint.
    parent = None
    for k,j in enumerate(order):
        if j<M:parent=j
        if parent is None:
            parent=next(i for i in reversed(order) if i<M)
        g=gap(ph[j],ph[order[(k+1)%n]])
        assert ev(best[parent], P+1)>=ev(g,P+1)
    return minus((1,0), (sum(e[0] for e in best.values()),
                           sum(e[1] for e in best.values())))

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        self.topbit = 1 << (n.bit_length() - 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def prefix(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        assert 1 <= k <= self.prefix(self.n)
        idx = 0
        bit = self.topbit
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit //= 2
        return idx + 1


def phase(j):
    if j == 0:
        return (0, 0)
    left = j * P // Q
    right = j * (P + 1) // Q
    assert left == right, ('ambiguous floor', j)
    p = (left + 1, -j)
    assert min(ev(p, P), ev(p, P+1)) > 0
    assert max(ev(p, P), ev(p, P+1)) < Q
    return p


def gap(x, y):
    e = minus(y, x)
    if ev(e) <= 0:
        e = plus(e, (1, 0))
    assert ev(e, P) > 0 and ev(e, P + 1) > 0
    return e


def run(n):
    assert n >= 1
    certify_theta()
    size = M + n
    ph = [phase(j) for j in range(size)]
    # One *offline* sort for the declared finite horizon.
    order = sorted(range(size), key=lambda j: ev(ph[j]))
    for a, b in zip(order, order[1:]):
        assert ev(ph[a], P) < ev(ph[b], P)
        assert ev(ph[a], P+1) < ev(ph[b], P+1)
    rank = [0] * size
    vals = [None] * (size + 1)
    for i, j in enumerate(order, start=1):
        rank[j] = i
        vals[i] = ph[j]

    ft = Fenwick(size)
    for j in range(M):
        ft.add(rank[j], 1)
    old_order = sorted(rank[:M])
    heaps = [[[], []] for _ in range(M)]
    gaps = {}
    live = {}
    serial = 0

    def store(a, b, parent):
        nonlocal serial
        e = gap(vals[a], vals[b])
        serial += 1
        live[serial] = True
        gaps[a] = (serial, parent, e)
        heappush(heaps[parent][0], (-ev(e, P), serial, e))
        heappush(heaps[parent][1], (-ev(e, P + 1), serial, e))

    def winner(parent):
        tops = []
        for h in heaps[parent]:
            while not live[h[0][1]]:
                heappop(h)
            tops.append(h[0][2])
        assert tops[0] == tops[1], ('interval max mismatch', parent, tops)
        return tops[0]

    for parent, r in enumerate(old_order):
        t = old_order[(parent + 1) % M]
        store(r, t, parent)
    assert sum(ev(winner(i)) for i in range(M)) == Q
    risk = (0, 0)
    blocks = []
    prev = None
    first = 1
    selected = {0: (0, 0)}
    for L in range(1, n + 1):
        r = rank[M + L - 1]
        s = ft.prefix(r - 1)
        current = M + L - 1
        a = ft.kth(s if s else current)
        b = ft.kth(s + 1 if s < current else 1)
        ident, parent, old = gaps[a]
        left, right = gap(vals[a], vals[r]), gap(vals[r], vals[b])
        assert plus(left, right) == old
        was = winner(parent)
        live[ident] = False
        ft.add(r, 1)
        store(a, r, parent)
        store(r, b, parent)
        now = winner(parent)
        d = minus(was, now)
        assert min(ev(d, P), ev(d, P + 1)) >= 0
        risk = plus(risk, d)
        assert 0 <= min(ev(risk, P), ev(risk, P + 1))
        assert max(ev(risk, P), ev(risk, P + 1)) <= Q
        if d != prev:
            if prev is not None:
                blocks.append((first, L - 1, prev))
            first, prev = L, d
        if L in (36, 37, 1142, 10000, n):
            selected[L] = risk
    blocks.append((first, n, prev))
    for h in (1142, 10000, 100000):
        if h <= n:
            direct = independent_partition_risk(M+h, ph)
            assert selected[h] == direct, ('direct risk mismatch', h)
            print('INDEPENDENT_PARTITION_MATCH',h,direct[0],direct[1])
    if n >= 1142:
        assert selected[1142] == (-18559, 70784)
    if n >= 10000:
        assert selected[10000] == (-151935, 579456)
    if n >= 100000:
        assert selected[100000] == (-2769919, 10563968)
    assert sum(end - begin + 1 for begin, end, _ in blocks) == n
    assert sum((end - begin + 1) * d[0] for begin, end, d in blocks) == risk[0]
    assert sum((end - begin + 1) * d[1] for begin, end, d in blocks) == risk[1]
    print('CERTIFIED_UNIFORM_INTERVAL', P, P + 1, Q)
    print('M', M, 'LMAX', n, 'CUTS', size, 'BLOCKS', len(blocks))
    for begin, end, d in blocks:
        print('BLOCK', begin, end, d[0], d[1])
    for L in sorted(selected):
        print('R', L, selected[L][0], selected[L][1])
    print('PASS_ONLINE_EXACT_RISK')
    return blocks

if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 100000)
