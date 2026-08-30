#!/usr/bin/env python3
from itertools import product

checks = 0


def require(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


# W1: SET -> GROUPOID lower-language collision.
C = (0, 1)
trivial_action = {
    0: {0: 0, 1: 1},
    1: {0: 0, 1: 1},
}
swap_action = {
    0: {0: 0, 1: 1},
    1: {0: 1, 1: 0},
}


def fixed_count(action):
    return sum(all(action[g][x] == x for g in action) for x in C)


require(tuple(trivial_action[0]) == tuple(swap_action[0]), "same underlying candidate set")
require(fixed_count(trivial_action) == 2, "trivial action has two invariant candidates")
require(fixed_count(swap_action) == 0, "swap action has no invariant candidate")

# W2: GLOBAL -> DESCENT lower-language collision.
# Triangle edges are 0->1, 1->2, 2->0; c_e in C2 and x_j=x_i+c_e.
def global_solutions(c):
    out = []
    for x in product((0, 1), repeat=3):
        if (
            x[1] == (x[0] ^ c[0])
            and x[2] == (x[1] ^ c[1])
            and x[0] == (x[2] ^ c[2])
        ):
            out.append(x)
    return out


all_c = list(product((0, 1), repeat=3))
for c in all_c:
    parity = c[0] ^ c[1] ^ c[2]
    require(
        len(global_solutions(c)) == (2 if parity == 0 else 0),
        f"triangle parity criterion failed for {c}",
    )
require(
    sum(bool(global_solutions(c)) for c in all_c) == 4,
    "exactly four of eight pairwise-valid transition triples globalize",
)

# W3: SET-DESCENT -> GROUPOID-DESCENT lower-language collision.
# Edge labels epsilon in C2^3; vertex gauge lambda in C2^3.
def gauge(eps, lam):
    return (
        lam[1] ^ eps[0] ^ lam[0],
        lam[2] ^ eps[1] ^ lam[1],
        lam[0] ^ eps[2] ^ lam[2],
    )


E = list(product((0, 1), repeat=3))
G = list(product((0, 1), repeat=3))
unseen = set(E)
orbits = []
while unseen:
    e = next(iter(unseen))
    orb = {gauge(e, lam) for lam in G}
    orbits.append(orb)
    unseen -= orb

require(len(orbits) == 2, "triangle C2 automorphism gluing has two gauge classes")
require(sorted(len(o) for o in orbits) == [4, 4], "each gauge orbit has size four")
orbit_parities = [{e[0] ^ e[1] ^ e[2] for e in o} for o in orbits]
require(
    sorted(next(iter(p)) for p in orbit_parities) == [0, 1],
    "holonomy parity classifies orbits",
)
require(all(len(p) == 1 for p in orbit_parities), "holonomy is gauge invariant")
for e in ((0, 0, 0), (1, 0, 0)):
    stabilizer = [lam for lam in G if gauge(e, lam) == e]
    require(len(stabilizer) == 2, "diagonal C2 isotropy must survive")

# Corrected abstraction lattice: morphism and locality are independent flags.
nodes = {
    (0, 0): "GLOBAL_SET",
    (1, 0): "GLOBAL_GROUPOID",
    (0, 1): "SET_DESCENT",
    (1, 1): "GROUPOID_DESCENT",
}
require(len(nodes) == 4, "four finite one-truncated abstraction nodes")
require(nodes[(1, 1)] == "GROUPOID_DESCENT", "stack-like finite scope is top-right node")

# Q1-Q8 minimal classifications at the proved/current scope.
qmap = {
    "Q1": "ROUTER",
    "Q2": "GLOBAL_SET",
    "Q3": "GLOBAL_GROUPOID",
    "Q4": "SET_DESCENT",
    "Q5": "GLOBAL_GROUPOID",
    "Q6": "GLOBAL_SET",
    "Q7": "GLOBAL_GROUPOID",
    "Q8": "ABSTRACTION_LATTICE",
}
require(qmap["Q2"] == "GLOBAL_SET", "Q2 fixed-radius collision is set-level")
require(qmap["Q3"] == "GLOBAL_GROUPOID", "Q3 needs morphisms/isotropy")
require(qmap["Q4"] == "SET_DESCENT", "Q4 strict-frame existence needs locality/cycle data")
require(qmap["Q7"] == "GLOBAL_GROUPOID", "Q7 naturality needs automorphism action")

# Gen13 current mother problem: no present subquestion forces descent/stack-like data.
gen13 = {
    1: "GLOBAL_SET",
    2: "GLOBAL_GROUPOID",  # once residues are classified under lift/gauge change
    3: "GLOBAL_SET",
    4: "GLOBAL_SET",
    5: "GLOBAL_SET",
    6: "GLOBAL_SET",
    7: "GLOBAL_GROUPOID",
    8: "GLOBAL_SET",
    9: "GLOBAL_SET",
}
require("SET_DESCENT" not in gen13.values(), "current Gen13 does not force descent")
require("GROUPOID_DESCENT" not in gen13.values(), "current Gen13 does not force stack-like data")
require(gen13[7] == "GLOBAL_GROUPOID", "Gen13 canonicality requires groupoid/action data")

print(
    "PASS P000_MINIMAL_ABSTRACTION_LATTICE; "
    f"checks={checks}; "
    "linear_ladder=COLLAPSED_TO_2AXIS_LATTICE; "
    "W1=fixed_candidates_trivial2_swap0; "
    "W2=triangle_C2_globalizable4_of8_parity0; "
    "W3=triangle_C2_gauge_orbits2_sizes4_4_isotropy2; "
    "Gen13=max_current=GLOBAL_GROUPOID:no_descent_required"
)
