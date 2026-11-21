#!/usr/bin/env python3
"""Exact rational author replication of the R97 positive-count BRC histogram theorem.

This is an algebraic model-defined BRC observer, not a simulation of native
X6 paths, signed phase, triadic forces, or physical heartbeat dynamics.
"""
from fractions import Fraction as Q
from collections import Counter

P_MAX = 26

def q(a):
    return max(sum(max(v, 0) for v in a),
               sum(max(-v, 0) for v in a))

def moments(a):
    x, y, z = a
    return x + 3*y + 6*z, 3*x + 12*y + 30*z, 7*x + 39*y + 126*z

def objective(m, S, T):
    u, v, h = m
    return max(Q(abs(u), 2), Q(abs(v), 1)/(S+1),
               Q(abs(h), 1)/(T+1), Q(abs(v-u), 1)/(S+1),
               Q(abs(h-u), 1)/(T+1), Q(abs(h-v), 1)/(S+T))

def all_directions(pmax):
    for x in range(-pmax, pmax+1):
      for y in range(-pmax, pmax+1):
       for z in range(-pmax, pmax+1):
        a = (x, y, z)
        if a == (0,0,0) or q(a)>pmax:
            continue
        first = next(v for v in a if v)
        if first < 0:  # choose one orientation for every ± pair
            continue
        yield q(a), a, moments(a)

pairs = [
    (Q(1),Q(12)), (Q(5),Q(12)), (Q(6),Q(12)), (Q(11),Q(12)),
    (Q(5),Q(23)), (Q(6),Q(23)), (Q(25,4),Q(23)),
    (Q(5),Q(30)), (Q(27,4),Q(30)), (Q(10),Q(30)),
    (Q(100),Q(30)), (Q(7),Q(25)), (Q(11),Q(25)),
    (Q(13,2),Q(15)), (Q(31,2),Q(33)),
    (Q(2),Q(100)), (Q(100),Q(100)), (Q(12),Q(100)),
    (Q(1),Q(1)), (Q(2),Q(5)), (Q(9),Q(11)), (Q(100),Q(11)),
    (Q(3),Q(3,2)), (Q(100),Q(1)),
]
ports = (11,12,15,16,20,21,22,26)
directions = list(all_directions(P_MAX))
assert len(directions) == 31031
u0 = 0
for p, a, (u,v,h) in directions:
    if u != 0:
        continue
    u0 += 1
    if v == 0:
        assert h != 0 and abs(h) >= 12
    else:
        assert h != 0 and h != v
        assert abs(v) >= 3 and abs(h) >= 6 and abs(h-v) >= 3
assert u0 == 160
comparisons = 0
for S,T in pairs:
    values = [(p,objective(m,S,T)) for p,a,m in directions]
    expected = min(Q(1,2), Q(12)/(T+1),
                   max(Q(3)/(S+1), Q(6)/(T+1)))
    for port in ports:
        actual = min(value for p,value in values if p<=port)
        assert actual == expected, (S,T,port,actual,expected)
        comparisons += sum(p<=port for p,v in values)
assert comparisons == 2411712
print({"status":"PASS", "directions":len(directions), "u_zero":u0,
       "parameter_pairs":len(pairs), "ports":len(ports),
       "cases":len(pairs)*len(ports), "exact_comparisons":comparisons})
