#!/usr/bin/env python3
"""Exact rational audit for the R5 single-collision signed-cone gate.
External finite P/Q experiment, not a Heartbeat native dynamical solver.
Python standard library only. No floating point and no random samples.
"""
from fractions import Fraction as F
from itertools import product

Z = F(0)
D = {"A": (F(1, 4), F(1, 2)), "B": (F(3, 4), F(1, 2))}  # P,Q at t=1
# Second-stage conditional Q weights and child (unconditional) P/Q ratios.
SECOND = {
    "A": {"U": (F(1, 4), F(1)), "V": (F(3, 4), F(1, 3))},
    "B": {"U": (F(1, 4), F(1)), "V": (F(3, 4), F(5, 3))},
}
# Two terminal Q-equiprobable leaves; P/Q multiplier relative to stage 2.
LAST = {
    "AU": (F(1, 3), F(5, 3)),
    "AV": (F(1, 2), F(3, 2)),
    "BU": (F(2, 3), F(4, 3)),
    "BV": (F(3, 5), F(7, 5)),
}

nodes = {}
for root, (p, q) in D.items():
    nodes[root] = (p, q, 1)
    assert sum(x[0] for x in SECOND[root].values()) == 1
    assert sum(x[0] * x[1] for x in SECOND[root].values()) == p / q
    for branch, (qc, lr) in SECOND[root].items():
        h = root + branch
        p2, q2 = q * qc * lr, q * qc
        nodes[h] = (p2, q2, 2)
        assert sum(LAST[h]) == 2  # terminal multipliers have Q-mean one
        for j, mult in enumerate(LAST[h]):
            nodes[h + str(j)] = (p2 * mult / 2, q2 / 2, 3)

term = [h for h in nodes if len(h) == 3]
assert len(term) == 8
assert all(nodes[h][0] > 0 and nodes[h][1] > 0 for h in term)
assert sum(nodes[h][0] for h in term) == 1
assert sum(nodes[h][1] for h in term) == 1
assert nodes["AU"][0] / nodes["AU"][1] == nodes["BU"][0] / nodes["BU"][1] == 1
assert len({nodes[h][0] / nodes[h][1] for h in term}) == 8
assert len({nodes[h][0] / nodes[h][1] for h in ("AV", "BV")}) == 2


def plus(*vectors):
    return tuple(sum(values) for values in zip(*vectors))


def observed(h, action):
    p, q, t = nodes[h]
    assert action in ("P", "Q")
    return (p if action == "Q" else Z,
            q if action == "P" else Z, F(t) * p, F(t) * q)


def terminal_options(h):
    return [plus(observed(h + "0", a), observed(h + "1", b))
            for a, b in product("PQ", repeat=2)]


def node_options(h):
    return [observed(h, "P"), observed(h, "Q")] + terminal_options(h)


root_options = {}
for g in "AB":
    root_options[g] = [observed(g, "P"), observed(g, "Q")]
    root_options[g] += [plus(u, v) for u, v in
                        product(node_options(g + "U"), node_options(g + "V"))]
assert all(len(root_options[g]) == 38 for g in "AB")
full = {plus(a, b) for a, b in product(root_options["A"], root_options["B"])}

lr = set()
for choice in range(18):
    if choice < 2:
        act = "PQ"[choice]
        au, bu = observed("AU", act), observed("BU", act)
    else:
        k = choice - 2
        au, bu = terminal_options("AU")[k // 4], terminal_options("BU")[k % 4]
    for av, bv in product(node_options("AV"), node_options("BV")):
        for a in (observed("A", "P"), observed("A", "Q"), plus(au, av)):
            for b in (observed("B", "P"), observed("B", "Q"), plus(bu, bv)):
                lr.add(plus(a, b))
assert len(full) == 1132, len(full)
assert len(lr) == 724, len(lr)
assert lr.issubset(full)


def dot(coeff, vec):
    return sum(x * y for x, y in zip(coeff, vec))


def cost(h, action, lam):
    a, b, u, v = lam
    p, q, t = nodes[h]
    return (b * q if action == "P" else a * p) + t * (u * p + v * q)


def bellman(lam):
    # One and only t=2 shared signature: AU and BU, with P,Q,C actions.
    ku = {h: (cost(h, "P", lam), cost(h, "Q", lam),
              sum(min(cost(h + str(j), "P", lam),
                      cost(h + str(j), "Q", lam)) for j in (0, 1)))
          for h in ("AU", "BU")}
    wv = {h: min(cost(h, "P", lam), cost(h, "Q", lam),
                 sum(min(cost(h + str(j), "P", lam),
                         cost(h + str(j), "Q", lam)) for j in (0, 1)))
          for h in ("AV", "BV")}
    early = {g: min(cost(g, "P", lam), cost(g, "Q", lam)) for g in "AB"}
    gate = {g: tuple(min(early[g], wv[g + "V"] + ku[g + "U"][d])
                     for d in range(3)) for g in "AB"}
    vf = sum(min(gate[g]) for g in "AB")
    vl = min(sum(gate[g][d] for g in "AB") for d in range(3))
    return vf, vl, ku, wv, early, gate


lam = (F(-18), F(-10), F(-2), F(3))
vf, vl, ku, wv, early, gate = bellman(lam)
assert vf == F(-71, 4)
assert vl == F(-141, 8)
assert vl - vf == F(1, 8)
assert ku == {"AU": (F(-1), F(-2), F(-17, 8)),
              "BU": (F(-1), F(-2), F(-15, 8))}
assert wv == {"AV": F(-2), "BV": F(-93, 8)}
assert early == {"A": F(-4), "B": F(-27, 2)}
assert gate == {"A": (F(-4), F(-4), F(-33, 8)),
                "B": (F(-27, 2), F(-109, 8), F(-27, 2))}

assert min(dot(lam, x) for x in full) == vf
assert min(dot(lam, x) for x in lr) == vl
witness = (F(41, 48), F(7, 16), F(11, 4), F(5, 2))
assert witness in full and witness not in lr
assert dot(lam, witness) == vf
assert all(-dot(lam, x) <= F(141, 8) for x in lr)
assert -dot(lam, witness) == F(71, 4)

# Cross-check all deterministic policies versus Bellman for a finite signed sample;
# universally valid all-real conclusions are proved separately by multi-affinity.
checked = 0
for a, b, u, v in product((-3, -1, 1, 4), (-5, -1, 2, 4),
                           (-2, 0, 2), (-3, 0, 3)):
    coeff = tuple(map(F, (a, b, u, v)))
    x, y, *_ = bellman(coeff)
    assert x == min(dot(coeff, p) for p in full)
    assert y == min(dot(coeff, p) for p in lr)
    checked += 1

print("SOURCE: external finite dual-measure observation tree, exact Fraction")
print("TERMINAL_LEAF_COUNT:", len(term))
print("TERMINAL_RATIOS:", ",".join(str(nodes[h][0] / nodes[h][1]) for h in sorted(term)))
print("RAW_REDUCED_TABLES: full=1444 lr=1152")
print("DISTINCT_OBSERVATIONS: full=%d lr=%d" % (len(full), len(lr)))
print("LAMBDA:", lam)
print("BELL_A:", gate["A"], "BELL_B:", gate["B"])
print("V_FULL:", vf, "V_LR:", vl, "GAP:", vl - vf)
print("FULL_WITNESS:", witness)
print("SUPPORT_INEQUALITY: 18*eP + 10*eQ + 2*TP - 3*TQ <= 141/8")
print("WITNESS_LEFT_SIDE:", -dot(lam, witness))
print("EXHAUSTIVE_SIGNED_CROSSCHECKS:", checked)
print("ALL EXACT CHECKS PASSED")
