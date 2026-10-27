#!/usr/bin/env python3
"""Exact unrestricted eight-leaf BRC fan-in support certificate (Fraction only)."""
from fractions import Fraction as F
from itertools import product

Z = F(0)
Q1 = {"A": F(1, 2), "B": F(1, 2)}
R1 = {"A": F(1, 2), "B": F(3, 2)}
Q2 = {"A": {"U": F(1, 3), "V": F(2, 3)},
      "B": {"U": F(1, 2), "V": F(1, 2)}}
M2 = {"A": {"U": F(2), "V": F(1, 2)},
      "B": {"U": F(2, 3), "V": F(4, 3)}}
R3 = {("A", "U"): (F(1, 4), F(7, 4)),
      ("A", "V"): (F(1, 2), F(3, 2)),
      ("B", "U"): (F(1, 2), F(3, 2)),
      ("B", "V"): (F(1, 2), F(3, 2))}
q, p = {}, {}
for h in "AB":
    q[h,] = Q1[h]
    p[h,] = Q1[h] * R1[h]
    assert sum(Q2[h].values(), Z) == 1
    assert sum(Q2[h][k] * M2[h][k] for k in "UV") == 1
    for k in "UV":
        q[h, k] = q[h,] * Q2[h][k]
        p[h, k] = p[h,] * Q2[h][k] * M2[h][k]
        assert sum(R3[h, k], Z) / 2 == 1
        for j in (0, 1):
            q[h, k, j] = q[h, k] / 2
            p[h, k, j] = p[h, k] * R3[h, k][j] / 2
leaves = list(product("AB", "UV", (0, 1)))
assert len(leaves) == 8
assert sum((q[h] for h in leaves), Z) == 1
assert sum((p[h] for h in leaves), Z) == 1
assert all(q[h] > 0 and p[h] > 0 for h in leaves)
assert p["A", "U"] / q["A", "U"] == p["B", "U"] / q["B", "U"] == 1
assert len({p[h] / q[h] for h in leaves}) == 8

zero = (Z,) * 4

def add(*xs):
    return tuple(sum(parts, Z) for parts in zip(*xs)) if xs else zero

def stop(h, time, decision):
    assert decision in "PQ"
    return (p[h] if decision == "Q" else Z,
            q[h] if decision == "P" else Z,
            time * p[h], time * q[h])

def dot(coefs, values):
    return sum((a * b for a, b in zip(coefs, values)), Z)

def t2_options(h, k):
    prefix = (h, k)
    return [stop(prefix, 2, a) for a in "PQ"] + [
        add(stop(prefix + (0,), 3, a), stop(prefix + (1,), 3, b))
        for a, b in product("PQ", repeat=2)]

t2 = {(h, k): t2_options(h, k) for h in "AB" for k in "UV"}
root_stops = {h: [stop((h,), 1, a) for a in "PQ"] for h in "AB"}
full_A = root_stops["A"] + [add(x, y) for x, y in product(t2["A", "U"], t2["A", "V"])]
full_B = root_stops["B"] + [add(x, y) for x, y in product(t2["B", "U"], t2["B", "V"])]
full_effective = [add(x, y) for x, y in product(full_A, full_B)]
shared = [(t2["A", "U"][j], t2["B", "U"][j]) for j in (0, 1)]
shared += list(product(t2["A", "U"][2:], t2["B", "U"][2:]))
lr_effective = []
for au, bu in shared:
    choices_A = root_stops["A"] + [add(au, av) for av in t2["A", "V"]]
    choices_B = root_stops["B"] + [add(bu, bv) for bv in t2["B", "V"]]
    lr_effective += [add(a, b) for a, b in product(choices_A, choices_B)]
assert len(full_effective) == 38 * 38 == 1444
assert len(lr_effective) == 18 * 8 * 8 == 1152
full, lr = set(full_effective), set(lr_effective)
assert len(full) == 1402 and len(lr) == 754
assert lr <= full
assert 3**6 * 2**8 == 186624
assert 3**5 * 2**8 == 62208

lam = (F(-20), F(-10), F(-2), F(3))
full_min = min(map(lambda o: dot(lam, o), full))
lr_min = min(map(lambda o: dot(lam, o), lr))
assert (full_min, lr_min, lr_min - full_min) == (F(-121, 6), F(-239, 12), F(1, 4))

def local_cost(prefix, time, decision):
    return dot(lam, stop(prefix, time, decision))

def terminal_best(prefix):
    return min(local_cost(prefix, 3, a) for a in "PQ")

def t2_values(h, k):
    prefix = (h, k)
    return (local_cost(prefix, 2, "P"), local_cost(prefix, 2, "Q"),
            sum((terminal_best(prefix + (j,)) for j in (0, 1)), Z))

values = {(h, k): t2_values(h, k) for h in "AB" for k in "UV"}
full_root = {}
for h in "AB":
    c = min(values[h, "U"]) + min(values[h, "V"])
    full_root[h] = min(local_cost((h,), 1, "P"), local_cost((h,), 1, "Q"), c)
assert sum(full_root.values(), Z) == full_min
shared_root_costs = []
for j in range(3):
    root_by_branch = {}
    for h in "AB":
        c = values[h, "U"][j] + min(values[h, "V"])
        root_by_branch[h] = min(local_cost((h,), 1, "P"),
                                local_cost((h,), 1, "Q"), c)
    shared_root_costs.append(sum(root_by_branch.values(), Z))
assert shared_root_costs == [F(-19), F(-239, 12), F(-239, 12)]
assert min(shared_root_costs) == lr_min

full_witness = add(
    stop(("A", "U", 0), 3, "P"), stop(("A", "U", 1), 3, "Q"),
    stop(("A", "V"), 2, "P"), stop(("B", "U"), 2, "Q"),
    stop(("B", "V", 0), 3, "Q"), stop(("B", "V", 1), 3, "Q"))
assert full_witness == (F(43, 48), F(5, 12), F(8, 3), F(29, 12))
assert dot(lam, full_witness) == full_min
lr_witness = add(stop(("A", "U"), 2, "Q"), stop(("A", "V"), 2, "P"),
                 stop(("B", "U"), 2, "Q"),
                 stop(("B", "V", 0), 3, "Q"), stop(("B", "V", 1), 3, "Q"))
assert lr_witness == (F(11, 12), F(1, 3), F(5, 2), F(9, 4))
assert dot(lam, lr_witness) == lr_min
assert full_witness in full and lr_witness in lr
print("SOURCE: 8 strictly positive P,Q terminal leaves; all 8 terminal LRs unique")
print("STATE COLLISION: t2 AU=BU=1; t1 A=1/2 B=3/2")
print("RAW POLICY TABLES: full=186624, LR=62208")
print("REACHABILITY-REDUCED TABLES: full=1444, LR=1152")
print("DISTINCT FOUR-VECTORS: full=1402, LR=754")
print("ALL LR VECTORS ARE FULL VECTORS:", lr <= full)
print("SIGNED LAMBDA:", lam)
for h in "AB":
    print("NODE t1", h, "stop P,Q", local_cost((h,), 1, "P"),
          local_cost((h,), 1, "Q"), "full optimal", full_root[h])
for h in "AB":
    for k in "UV":
        print("NODE t2", h+k, "stopP stopQ continue", *values[h, k])
print("SHARED GATE LR MIN BY ACTION P,Q,C:", *shared_root_costs)
print("FULL WITNESS:", full_witness)
print("LR WITNESS:", lr_witness)
print("FULL MIN:", full_min, "LR MIN:", lr_min, "GAP:", lr_min - full_min)
print("EXHAUSTIVE DETERMINISTIC ENUMERATION AND BELLMAN EXACTLY AGREE")
print("ALL EXACT CHECKS PASSED")
