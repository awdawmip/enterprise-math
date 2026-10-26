#!/usr/bin/env python3
"""Exact rational N=3 collision-repair check (external two-measure BRC readout)."""
from fractions import Fraction as F
from collections import defaultdict
from random import Random
from itertools import product

# A transition is child: (Q(child|parent), P(child|parent)).
T = {
    "": {"a": (F(1, 3), F(2, 3)), "b": (F(2, 3), F(1, 3))},
    "a": {"ax": (F(1, 2), F(1, 4)), "ay": (F(1, 2), F(3, 4))},
    "b": {"bx": (F(2, 3), F(1, 3)), "by": (F(1, 3), F(2, 3))},
    "ax": {"axu": (F(16, 21), F(1, 21)), "axv": (F(5, 21), F(20, 21))},
    "ay": {"ayu": (F(1, 2), F(1, 2)), "ayv": (F(1, 2), F(1, 2))},
    "bx": {"bxu": (F(1, 2), F(1, 2)), "bxv": (F(1, 2), F(1, 2))},
    "by": {"byu": (F(1, 2), F(1, 2)), "byv": (F(1, 2), F(1, 2))},
}
DEPTH = {"": 0}
P = {"": F(1)}
Q = {"": F(1)}
for d in range(3):
    for h in [s for s in DEPTH if DEPTH[s] == d]:
        row = T[h]
        assert sum(q for q, _ in row.values()) == 1
        assert sum(p for _, p in row.values()) == 1
        for child, (qc, pc) in row.items():
            DEPTH[child] = d + 1
            Q[child] = Q[h] * qc
            P[child] = P[h] * pc
assert len([h for h in DEPTH if DEPTH[h] == 3]) == 8
assert sum(Q[h] for h in DEPTH if DEPTH[h] == 3) == 1
assert sum(P[h] for h in DEPTH if DEPTH[h] == 3) == 1
L = {h: P[h] / Q[h] for h in DEPTH}
assert (L["a"], L["b"], L["ax"], L["by"], L["ay"], L["bx"]) == (2, F(1, 2), 1, 1, 3, F(1, 4))

COST_P, COST_Q = F(389, 1344), F(-347, 1344)
def objective(o):
    return o[0] + o[1] + COST_P * o[2] + COST_Q * o[3]

def value(policy):
    """Return four observables for any full-history probabilistic action policy.
    Each node stores (Pr(continue), Pr(decide P), Pr(decide Q)).
    """
    ep = eq = tp = tq = F(0)
    def visit(h, survival):
        nonlocal ep, eq, tp, tq
        cont, decp, decq = policy[h]
        assert cont >= 0 and decp >= 0 and decq >= 0
        assert cont + decp + decq == 1
        if DEPTH[h] == 3:
            assert cont == 0
        ep += P[h] * survival * decq
        eq += Q[h] * survival * decp
        tp += P[h] * survival * cont
        tq += Q[h] * survival * cont
        if h in T:
            for child in T[h]:
                visit(child, survival * cont)
    visit("", F(1))
    return ep, eq, tp, tq

def deterministic_policy(stop_by=False):
    policy = {}
    for h in DEPTH:
        if DEPTH[h] == 3:
            policy[h] = (F(0), F(int(L[h] >= 1)), F(int(L[h] < 1)))
        elif h == "ay" or (h == "by" and stop_by):
            policy[h] = (F(0), F(1), F(0))
        else:
            policy[h] = (F(1), F(0), F(0))
    return policy

def bellman(h):
    stop = min(L[h], F(1))
    if DEPTH[h] == 3:
        return stop
    continue_cost = COST_P * L[h] + COST_Q + sum(q * bellman(child) for child, (q, _p) in T[h].items())
    return min(stop, continue_cost)

assert bellman("ax") == F(71, 224)
assert bellman("ay") == 1
assert bellman("bx") == F(115, 1792)
assert bellman("by") == 1
assert bellman("a") == F(47, 48)
assert bellman("b") == F(353, 1344)
assert bellman("") == F(179, 336)

full = value(deterministic_policy(stop_by=True))
coarse_s1 = value(deterministic_policy(stop_by=False))
assert full == (F(5, 42), F(3, 7), F(41, 18), F(47, 18))
assert coarse_s1 == (F(5, 42), F(3, 7), F(5, 2), F(17, 6))
assert objective(full) == F(179, 336)
assert objective(coarse_s1) == F(34, 63)
assert F(34, 63) - bellman("") == F(1, 144)
assert tuple(coarse_s1[i] - full[i] for i in range(4)) == (0, 0, F(2, 9), F(2, 9))
assert sum(map(abs, (F(1), F(1), COST_P, COST_Q))) == F(107, 42)
assert F(1, 144) / F(107, 42) == F(7, 2568)

# For any full behavioral policy, copy decisions at all nonterminal states using
# one bit at the sole merged pair ax/by. Terminal actions are Q-arrival-weighted
# by their exact likelihood-ratio class, so one does not retain a final bit.
def onebit_repair(full_policy):
    arrival = {}
    def reach(h, survive):
        arrival[h] = Q[h] * survive
        for child in T.get(h, {}):
            reach(child, survive * full_policy[h][0])
    reach("", F(1))
    numerator = defaultdict(F)
    denominator = defaultdict(F)
    for h in DEPTH:
        if DEPTH[h] != 3:
            continue
        ell = L[h]
        denominator[ell] += arrival[h]
        numerator[ell] += arrival[h] * full_policy[h][2]
    repaired = dict(full_policy)
    for h in DEPTH:
        if DEPTH[h] == 3:
            ell = L[h]
            pq = numerator[ell] / denominator[ell] if denominator[ell] else F(0)
            repaired[h] = (F(0), F(1) - pq, pq)
    # Nonterminal actions are addressable by (time,LR) except ax/by,
    # distinguished by a single transient bit at time 2.
    assert len({(DEPTH[h], L[h], "ax" if h == "ax" else "by" if h == "by" else "-") for h in T}) == len(T)
    assert value(repaired) == value(full_policy)
    return repaired

onebit_repair(deterministic_policy(stop_by=True))
rng = Random(271027)
for _ in range(64):
    policy = {}
    for h in DEPTH:
        if DEPTH[h] == 3:
            a, b = rng.randint(1, 9), rng.randint(1, 9)
            policy[h] = (F(0), F(a, a + b), F(b, a + b))
        else:
            a, b, c = (rng.randint(1, 9) for _ in range(3))
            policy[h] = (F(a, a + b + c), F(b, a + b + c), F(c, a + b + c))
    onebit_repair(policy)

# Deterministic quotient enumeration cross-check; all-real optimality comes
# from the cited prior algebraic inequality, not enumeration alone.
states = sorted({(DEPTH[h], L[h]) for h in DEPTH})
choices = [((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))) if t < 3
           else ((F(0), F(1), F(0)), (F(0), F(0), F(1))) for t, _l in states]
best = None
best_times = set()
count = 0
for table in product(*choices):
    indexed = dict(zip(states, table))
    ptab = {h: indexed[(DEPTH[h], L[h])] for h in DEPTH}
    o = value(ptab)
    j = objective(o)
    if best is None or j < best:
        best = j
        best_times = {(o[2], o[3])}
    elif j == best:
        best_times.add((o[2], o[3]))
    count += 1
assert count == 23328
assert best == F(34, 63)
assert best_times == {(F(13, 9), F(19, 9)), (F(5, 2), F(17, 6))}

print("TREE: 8 strictly positive rational leaves; P/Q normalized PASS")
print("L2: ax=by=1; ay=3; bx=1/4; PASS")
print("FULL_BELLMAN_MIN:", bellman(""))
print("COARSE_MIN (prior all-real certificate):", F(34, 63))
print("COARSE_DETERMINISTIC_EXHAUSTIVE:", count, "PASS; exact optimal time pairs:", sorted(best_times))
print("EXACT_SIGNED_SUPPORT_GAP:", F(1, 144))
print("FULL_OPTIMAL_VECTOR:", full)
print("COARSE_S1_VECTOR:", coarse_s1)
print("S1_MINUS_FULL:", tuple(coarse_s1[i] - full[i] for i in range(4)))
print("LINF_APPROXIMATION_OBSTRUCTION:", F(7, 2568))
print("ONEBIT_REPAIR_EXACT_RANDOM_RATIONAL_CHECKS: 64 PASS")
print("ALL REAL ONEBIT REPAIR: mathematical occupancy proof, not inferred from tests")
