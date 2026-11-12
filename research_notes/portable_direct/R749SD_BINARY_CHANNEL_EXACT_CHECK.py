#!/usr/bin/env python3
"""Exact rational checks for R749SD; independent 3-class step kernel.

The 960-edge source-graph partition (1,1,14) is a pinned R749SA
premise, not re-enumerated here. No native Cell/Link/Port event is simulated.
"""
from fractions import Fraction as F
from math import comb
import json


def q(p):
    return (1 + 15 * p) / 16


def r(p):
    return (1 - p) / 16


def a(p):
    return (1 + 7 * p) / 8


def law(m, t):
    return [F(comb(m, k)) * t**k * (1 - t)**(m - k)
            for k in range(m + 1)]


def tv(m, t0, t1):
    return sum((abs(x-y) for x, y in zip(law(m, t0),
                                           law(m, t1))), F()) / 2


def exact_joint(m, p):
    # J exact signed completions, U unsigned-only completions, O others.
    result = {}
    for j in range(m + 1):
        for u in range(m - j + 1):
            o = m - j - u
            mass = F(comb(m, j) * comb(m - j, u)) * q(p)**j * r(p)**u * (14*r(p))**o
            result[j, u, o] = mass
    assert sum(result.values(), F()) == 1
    for k in range(m + 1):
        exact_k = sum((v for (j,u,o),v in result.items() if j + u == k), F())
        assert exact_k == law(m, a(p))[k]
    for j in range(m + 1):
        exact_j = sum((v for (x,u,o),v in result.items() if x == j), F())
        assert exact_j == law(m, q(p))[j]
    return result


p0, p1 = F(0), F(1,2)
assert (q(p0), q(p1), a(p0), a(p1)) == (F(1,16), F(17,32), F(1,8), F(9,16))
assert a(p0) == q(p0) + (1-q(p0))/15
assert a(p1) == q(p1) + (1-q(p1))/15
for p in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
    assert q(p) + 15*r(p) == 1
    assert q(p) + r(p) == a(p)
    for m in range(0, 9):
        exact_joint(m, p)

rows=[]
for m in range(1,7):
    signed=tv(m, q(p0), q(p1))
    unsigned=tv(m, a(p0), a(p1))
    assert signed > unsigned
    rows.append({"m":m,"tv_signed":str(signed),"tv_unsigned":str(unsigned),
                 "bayes_error_signed":str((1-signed)/2),
                 "bayes_error_unsigned":str((1-unsigned)/2)})
assert rows[1] == {"m":2,"tv_signed":"675/1024", "tv_unsigned":"147/256",
                  "bayes_error_signed":"349/2048", "bayes_error_unsigned":"109/512"}
# At p=1, Y=1 a.s.; any parameter-independent reverse B(Y->X)
# reproducing p=1 must have B(X=1|Y=1)=1. At p=0,
# Pr(Y=1)=1/8 > Pr(X=1)=1/16: reverse is impossible.
assert a(F(1)) == q(F(1)) == 1 and a(F(0)) > q(F(0))

print(json.dumps({"status":"PASS", "model":"R749SA_FINITE_OBSERVER_KERNEL_ONLY",
                  "parameter_grid":["0","1/4","1/2","3/4","1"],
                  "joint_multinomial_horizons":"m=0..8",
                  "binary_testing_horizons":"m=1..6",
                  "p0":"0", "p1":"1/2", "rows":rows,
                  "native_event_permission":False},indent=2))
