#!/usr/bin/env python3
"""
RSA-270 continuation checkpoint:
1) multiplier/Fermat exact identities and generalized Plucker determinant;
2) reproducible N-only first-layer predictor benchmark;
3) BRC profile moment <-> odd divisor-sum bridge.

Researcher-ID: EM-DIRECT-66DE45
No RSA-270 factor is used or produced.
"""
from math import isqrt
from statistics import mean


def divisors(n):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def ceil_sqrt(n):
    r = isqrt(n)
    return r if r * r == n else r + 1


def profile(n):
    assert n % 2 == 1
    P = {}
    for d in divisors(n):
        s = (d + n // d + 2) // 2
        for j in range(s - 1):
            e = 2 - s + 2 * j
            P[e] = P.get(e, 0) + 1
    return P


def sigma(n, k):
    return sum(d ** k for d in divisors(n))


def mu_closed(n):
    s1, s3, s5, s7 = (sigma(n, k) for k in (1, 3, 5, 7))
    mu0 = s1
    num2 = s3 + (3 * n - 4) * s1
    assert num2 % 12 == 0
    mu2 = num2 // 12
    num4 = 3 * s5 + (15 * n - 40) * s3 + (30 * n * n - 120 * n + 112) * s1
    assert num4 % 240 == 0
    mu4 = num4 // 240
    num6 = (
        3 * s7
        + (21 * n - 84) * s5
        + (63 * n * n - 420 * n + 784) * s3
        + (105 * n ** 3 - 840 * n * n + 2352 * n - 1984) * s1
    )
    assert num6 % 1344 == 0
    mu6 = num6 // 1344
    return (mu0, mu2, mu4, mu6)


def check_moments():
    tests = [15, 35, 45, 105, 143, 225, 315]
    for n in tests:
        P = profile(n)
        direct = tuple(sum((e ** r) * c for e, c in P.items()) for r in (0, 2, 4, 6))
        assert direct == mu_closed(n), (n, direct, mu_closed(n))
    return len(tests)


def check_multiplier():
    samples = [
        (711649, 971639, [(1, 1), (3, 1), (5, 3), (13, 11), (29, 25)]),
        (8943811, 13689397, [(1, 1), (7, 5), (15, 11), (65, 47)]),
        (46559, 49003, [(1, 1), (5, 3), (9, 7), (17, 15)]),
    ]
    count = 0
    for p, q, abs_ in samples:
        N = p * q
        for a, b in abs_:
            x = a * p + b * q
            y = abs(a * p - b * q)
            k = a * b
            assert x * x - y * y == 4 * k * N
            x0 = ceil_sqrt(4 * k * N)
            j = x - x0
            assert j >= 0
            c, d = b, a + 2
            x2 = c * p + d * q
            Delta = a * d - b * c
            assert (d * x - b * x2) * (a * x2 - c * x) == Delta * Delta * N
            count += 1
    return count


def ranks(vals):
    order = sorted(range(len(vals)), key=lambda i: vals[i])
    out = [0.0] * len(vals)
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and vals[order[j]] == vals[order[i]]:
            j += 1
        r = ((i + j - 1) / 2.0) + 1.0
        for t in range(i, j):
            out[order[t]] = r
        i = j
    return out


def spearman(xs, ys):
    rx, ry = ranks(xs), ranks(ys)
    mx, my = mean(rx), mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def k_rows(p, q, K=1000):
    N = p * q
    rows = []
    for k in range(1, K + 1, 2):
        x0 = ceil_sqrt(4 * k * N)
        d0 = x0 * x0 - 4 * k * N
        width = 2 * x0 - 1
        rho = d0 / width
        rd = isqrt(d0)
        if d0 == 0:
            sqnorm = 0.0
        else:
            sqerr = min(d0 - rd * rd, (rd + 1) * (rd + 1) - d0)
            sqnorm = sqerr / (2 * rd + 1) if rd else 0.0
        best = None
        for a in divisors(k):
            b = k // a
            j = a * p + b * q - x0
            if j >= 0 and (best is None or j < best):
                best = j
        rows.append((k, best, rho, sqnorm))
    return rows


DATA = {
    16: [
        (46559, 49003), (36847, 45077), (47623, 54877), (41113, 48299),
        (46307, 62773), (43853, 58601), (54331, 63473), (45377, 59107),
        (44269, 49031), (57329, 64187), (34123, 60077), (36017, 56393),
    ],
    20: [
        (711649, 971639), (577531, 738743), (568231, 607769), (619867, 849523),
        (619111, 951497), (705113, 829811), (569659, 740087), (572549, 811667),
        (542599, 785249), (710473, 789221), (847507, 948659), (573673, 837503),
    ],
    24: [
        (8943811, 13689397), (14884873, 15917791), (12926219, 16566527),
        (10418647, 15879449), (11635297, 15997571), (10504933, 13825193),
        (8809627, 12267953), (9188783, 10002397), (10875181, 16663511),
        (8626099, 10844651), (14141707, 16582099), (11091011, 16083061),
    ],
}


def predictor_benchmark():
    out = {}
    for bits, pairs in DATA.items():
        cors = {"rho": [], "sqnorm": []}
        ovs = {"rho": [], "sqnorm": []}
        for p, q in pairs:
            rows = k_rows(p, q)
            import math
            logj = [math.log1p(r[1]) for r in rows]
            for name, idx in (("rho", 2), ("sqnorm", 3)):
                vals = [r[idx] for r in rows]
                cors[name].append(spearman(vals, logj))
                m = max(1, len(rows) // 20)
                good = {r[0] for r in sorted(rows, key=lambda x: x[1])[:m]}
                pred = {r[0] for r in sorted(rows, key=lambda x: x[idx])[:m]}
                ovs[name].append(len(good & pred) / m)
        out[bits] = {name: (mean(cors[name]), mean(ovs[name])) for name in cors}
    return out


if __name__ == "__main__":
    print("multiplier identities:", check_multiplier(), "PASS")
    print("moment bridge:", check_moments(), "odd composites PASS")
    b = predictor_benchmark()
    for bits in sorted(b):
        print(bits, b[bits])
    assert abs(b[24]["rho"][0]) < 0.03
    assert abs(b[24]["sqnorm"][0]) < 0.03
    assert 0.03 <= b[24]["rho"][1] <= 0.07
    assert 0.03 <= b[24]["sqnorm"][1] <= 0.07
    print("ALL PASS")
