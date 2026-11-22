#!/usr/bin/env python3
"""Exact rational replay of the X6 R116 triple-vertex path theorem.

All six pair observations are evaluated; no external packages required.
The finite check is intentionally separate from the analytic all-Port proof.
"""
from fractions import Fraction as Q
import json

P_LIMIT = 28
PORTS = (7, 10, 17, 21, 28)
EPSILON = Q(1, 100)
S0 = ((0, 0, 2), (0, 1, 1), (0, 1, -1))
S1 = ((1, 1, 1), (1, 0, -2), (1, 1, -1), (1, 0, 0), (1, 0, 2))
S2 = ((1, -1, -1), (1, -1, 1))
CASES = (("eight", Q(1, 2), Q(3, 5)),
         ("eight_equal", Q(1, 2), Q(8, 9)),
         ("ten", Q(1, 2), Q(1)),
         ("three_equal", Q(1), Q(4, 5)),
         ("three", Q(2), Q(1)))


def port(a):
    return max(sum(max(x, 0) for x in a), sum(max(-x, 0) for x in a))


def xyz(t, m, n):
    assert (n-m) % 2 == 0
    return (10*t - 12*m + 3*n, -5*t + 7*m - 2*n,
            t + (n - 3*m)//2)


def canonical(a):
    b = tuple(-x for x in a)
    return min(a, b)


def observation(a, w):
    x, y, z = a
    heights = (0, x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)
    return max(Q(abs(heights[i]-heights[j]), w[i]+w[j])
               for i in range(4) for j in range(i+1, 4))


def weights(r, k):
    s = Q(1,2) + EPSILON/2
    X = 4 + k*EPSILON
    Y = 18 + r*EPSILON
    return (s, 1-s, X-s, Y-s)


def predicted(r, k, p):
    bank = list(S0)
    if r < 1:
        bank += S1
        if 9*k > 2*r + 7:
            bank += S2
    return {canonical(xyz(*a)) for a in bank if port(xyz(*a)) <= p}


def oriented_data(w):
    result = []
    oriented = 0
    for x in range(-P_LIMIT, P_LIMIT+1):
        for y in range(-P_LIMIT, P_LIMIT+1):
            for z in range(-P_LIMIT, P_LIMIT+1):
                a = (x, y, z)
                p = port(a)
                if not any(a) or p > P_LIMIT:
                    continue
                oriented += 1
                if a == canonical(a):
                    result.append((p, a, observation(a, w)))
    return oriented, result


def main():
    report = {"scope": "finite exact rational replay; analytic theorem covers all p>=7 and sufficiently small epsilon",
              "epsilon": str(EPSILON), "cases": []}
    for name, r, k in CASES:
        w = weights(r, k)
        assert all(u > 0 for u in w)
        eps = EPSILON
        s = Q(1, 2) + eps/2
        X = 4 + k*eps
        Y = 18 + r*eps
        assert 1-2*s < 0 and 18-Y < 0 and 9+9*X-2*Y-18*s < 0
        oriented, records = oriented_data(w)
        assert oriented == 77196
        line = {"name": name, "r": str(r), "kappa": str(k),
                "weights": [str(x) for x in w], "oriented_checked": oriented,
                "ports": {}}
        for p in PORTS:
            allowed = [(a,score) for cost,a,score in records if cost <= p]
            eta = min(score for a,score in allowed)
            exact = Q(12, 1)/(18+(r-1)*eps)
            assert eta == exact, (name,p,eta,exact)
            near = {a for a,score in allowed if 2*score < 3*eta}
            expected = predicted(r,k,p)
            assert near == expected, (name,p,near^expected)
            line["ports"][str(p)] = {"eta": str(eta), "near_count": len(near)}
        report["cases"].append(line)
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
