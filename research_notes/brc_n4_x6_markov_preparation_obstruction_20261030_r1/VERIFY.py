"""Exact positive-mass BRC 16-branch checker; external finite law, no native physical evolution."""
from fractions import Fraction as F
from itertools import product

SIGNS = {"AU": (1, 1), "AV": (1, -1), "BU": (-1, 1), "BV": (-1, -1)}
Q = {"AU": 10, "AV": 20, "BU": 15, "BV": 15}
P = {"AU": (9, 11), "AV": (5, 5), "BU": (3, 27), "BV": (30, 30)}
LEAVES = [dict(s=s, j=j, k=k, bits=SIGNS[s] + (1 if j == 0 else -1, 1 if k == 0 else -1),
               P=F(P[s][j], 240), Q=F(Q[s], 240))
          for s, j, k in product(SIGNS, range(2), range(2))]
assert len(LEAVES) == 16
for law in "PQ":
    assert sum((leaf[law] for leaf in LEAVES), F(0)) == 1
    assert all(leaf[law] > 0 for leaf in LEAVES)

def mass(law, prefix):
    return sum((leaf[law] if law != "M" else (leaf["P"]+leaf["Q"])/2
                for leaf in LEAVES if leaf["bits"][:len(prefix)] == prefix), F(0))

def tv(depth):
    prefixes = {leaf["bits"][:depth] for leaf in LEAVES}
    return sum((abs(mass("P", h)-mass("Q", h)) for h in prefixes), F(0))/2

for law in ("P", "Q", "M"):
    for leaf in LEAVES:
        weight, h = F(1), ()
        for step in leaf["bits"]:
            assert mass(law, h) > 0
            weight *= mass(law, h+(step,))/mass(law, h)
            h += (step,)
        assert weight == mass(law, h)
        x = [0]*6
        for axis, step in enumerate(h):
            prev = x[:]
            x[axis] += step
            assert sum(a != b for a,b in zip(x,prev)) == 1
        assert tuple(x[:4]) == h and tuple(x[4:]) == (0, 0)

assert [tv(m) for m in range(5)] == [F(0), F(1,4), F(1,4), F(43,120), F(43,120)]
midpoint_error = sum((abs(leaf["P"]-mass("M", leaf["bits"])) for leaf in LEAVES), F(0))/2
assert midpoint_error == F(43, 240)
assert sum((abs(leaf["Q"]-mass("M", leaf["bits"])) for leaf in LEAVES), F(0))/2 == midpoint_error

classes = {}
for s, signs in SIGNS.items():
    p = mass("P", signs+(1,))/mass("P", signs)
    q = mass("Q", signs+(1,))/mass("Q", signs)
    classes[s] = (str(p), str(q), p != q)
assert classes == {"AU": ("9/20", "1/2", True), "AV": ("1/2", "1/2", False),
                   "BU": ("1/10", "1/2", True), "BV": ("1/2", "1/2", False)}
assert sum(2 if row[2] else 1 for row in classes.values()) == 6
for law, s, j in product("PQ", SIGNS, range(2)):
    h = SIGNS[s]+(1 if j == 0 else -1,)
    assert mass(law, h+(1,))/mass(law, h) == F(1, 2)
    assert mass(law, h+(-1,))/mass(law, h) == F(1, 2)
print("PASS_BRC_N4_X6_MARKOV_PREPARATION_OBSTRUCTION")
print("16 strictly-positive branches, 4 signed native X6 steps, P/Q/midpoint cylinder products: PASS")
print("PREFIX_TV=0,1/4,1/4,43/120,43/120")
print("SHARP_UNPREPARED_MINIMAX=43/240; STAGE2_POTENTIAL_FUTURE_CLASSES=6; K_FAIR=PASS")
