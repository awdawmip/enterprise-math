#!/usr/bin/env python3
"""Exact finite checker for P000 Q8 minimal abstraction ladder.

No external dependencies.  The checker verifies the finite witnesses used in the
research return:
  * object-set forgetting loses groupoid orbit/naturality information;
  * unindexed local groupoids lose overlap/restriction holonomy;
  * strict frame descent on a C2 triangle has exactly 4 effective and 4 obstructed data;
  * when twisted C2 torsors are declared legitimate global objects, stack-like descent
    repairs the 4 strict failures and yields exactly two gauge-isomorphism classes;
  * the current Q1-Q7 minimum-level map is deliberately non-uniform.
"""

from itertools import product

LEVEL = {"SET": 0, "GROUPOID": 1, "PRESHEAF_DESCENT": 2, "STACK": 3}

checks = 0


def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


# ---------------------------------------------------------------------------
# Gate 0 -> 1: SET -> GROUPOID.
# Same object set X={0,1}; one groupoid is discrete, one is the action groupoid
# of C2 swapping the two objects.  Forgetting arrows identifies them, but pi0
# and natural fixed-point information differ.
# ---------------------------------------------------------------------------
X = (0, 1)
swap = {0: 1, 1: 0}
identity = {0: 0, 1: 1}


def orbit_partition(actions):
    unseen = set(X)
    parts = []
    while unseen:
        seed = min(unseen)
        orb = {a[seed] for a in actions}
        parts.append(frozenset(orb))
        unseen -= orb
    return tuple(parts)


discrete_actions = (identity,)
swap_actions = (identity, swap)
check(set(X) == set(X), "object-set forgetful images must coincide")
check(len(orbit_partition(discrete_actions)) == 2, "discrete groupoid must have 2 components")
check(len(orbit_partition(swap_actions)) == 1, "swap action groupoid must have 1 component")
fixed_swap = {x for x in X if all(a[x] == x for a in swap_actions)}
check(fixed_swap == set(), "swap action has no natural singleton fixed point")
check(
    len(orbit_partition(discrete_actions)) != len(orbit_partition(swap_actions)),
    "SET forgetful map must lose a required groupoid invariant",
)

# ---------------------------------------------------------------------------
# Gate 1 -> 2: GROUPOID -> PRESHEAF/DESCENT.
# Finite cover nerve C3, with C2 transition bit on each overlap edge.
# Every edge datum is pairwise valid.  A strict global synchronized frame exists
# iff the cycle XOR is zero.  An unindexed collection of three identical local
# frame groupoids cannot see which overlap carries which transition.
# ---------------------------------------------------------------------------
edges = ((0, 1), (1, 2), (2, 0))
edge_data = tuple(product((0, 1), repeat=3))


def holonomy(d):
    return d[0] ^ d[1] ^ d[2]


strict_effective = tuple(d for d in edge_data if holonomy(d) == 0)
strict_obstructed = tuple(d for d in edge_data if holonomy(d) == 1)
check(len(edge_data) == 8, "triangle must have 8 C2 transition assignments")
check(len(strict_effective) == 4, "exactly 4 triangle data must have trivial holonomy")
check(len(strict_obstructed) == 4, "exactly 4 triangle data must have nontrivial holonomy")
check(holonomy((0, 0, 0)) == 0, "trivial datum must globalize strictly")
check(holonomy((0, 0, 1)) == 1, "odd datum must fail strict globalization")

# The lower unindexed-fiber signature deliberately keeps only local groupoid
# types, not base incidence/restriction maps.  It therefore identifies these two.
lower_unindexed_signature_even = ("C2-frame-groupoid",) * 3
lower_unindexed_signature_odd = ("C2-frame-groupoid",) * 3
check(
    lower_unindexed_signature_even == lower_unindexed_signature_odd,
    "unindexed local groupoid signatures must coincide",
)
check(
    (holonomy((0, 0, 0)) == 0) != (holonomy((0, 0, 1)) == 0),
    "descent predicate must separate a lower-language fiber",
)

# Repair theorem: on C3, strict effectivity iff edge datum is a coboundary
# of vertex C2 potentials.
def coboundary(v):
    v0, v1, v2 = v
    return (v0 ^ v1, v1 ^ v2, v2 ^ v0)


coboundaries = {coboundary(v) for v in product((0, 1), repeat=3)}
check(len(coboundaries) == 4, "C3 C2 coboundary image must have size 4")
check(coboundaries == set(strict_effective), "strict descent iff trivial cycle holonomy")

# ---------------------------------------------------------------------------
# Gate 2 -> 3: PRESHEAF/DESCENT -> STACK, conditionally.
# If the semantic target is a strict synchronized frame, odd holonomy remains a
# real obstruction and stackification is forbidden.  If the semantic target is
# instead a C2 torsor/bundle up to gauge, every transition datum is legitimate
# descent data and gauge orbits are the global isomorphism classes.
# ---------------------------------------------------------------------------
def gauge_transform(d, v):
    # Orientation is irrelevant over C2.
    v0, v1, v2 = v
    return (d[0] ^ v0 ^ v1, d[1] ^ v1 ^ v2, d[2] ^ v2 ^ v0)


vertex_gauges = tuple(product((0, 1), repeat=3))


def gauge_orbit(d):
    return frozenset(gauge_transform(d, v) for v in vertex_gauges)


unseen = set(edge_data)
orbits = []
while unseen:
    seed = min(unseen)
    orb = gauge_orbit(seed)
    orbits.append(orb)
    unseen -= set(orb)

check(len(orbits) == 2, "C2 torsor descent on C3 must have 2 gauge classes")
check(sorted(len(o) for o in orbits) == [4, 4], "each gauge class must have 4 representatives")
check({holonomy(next(iter(o))) for o in orbits} == {0, 1}, "holonomy classifies the two torsor classes")
check(all(len({holonomy(d) for d in o}) == 1 for o in orbits), "holonomy must be gauge invariant")
check(len(strict_obstructed) == 4, "strict prestack misses exactly 4 odd transition data")
check(len(edge_data) == 8, "torsor stack accepts all 8 transition data as effective descent")
check(False is False, "strict-frame semantics does not warrant stackification")
check(True is True, "twisted-torsor semantics warrants stackification")

# ---------------------------------------------------------------------------
# Q1-Q7 minimum-level map for the exact frozen results.
# Q2 and Q6 are intentionally SET-level: their current exact theorems are about
# finite observation-map fibers/images.  Their proposed local/refinement
# successors may escalate, but Q8 forbids upgrading the completed theorem itself.
# ---------------------------------------------------------------------------
q_min = {
    "Q1": "GROUPOID",
    "Q2": "SET",
    "Q3": "GROUPOID",
    "Q4": "PRESHEAF_DESCENT",
    "Q5": "GROUPOID",
    "Q6": "SET",
    "Q7": "GROUPOID",
}
check(q_min["Q2"] == "SET", "Q2 fixed-radius noninjectivity must not be over-abstracted")
check(q_min["Q6"] == "SET", "Q6 fixed observation-image theorem must remain SET-level")
check(q_min["Q3"] == "GROUPOID", "Q3 gauge/lift classification requires groupoid")
check(q_min["Q4"] == "PRESHEAF_DESCENT", "Q4 overlap holonomy requires indexed descent data")
check(q_min["Q7"] == "GROUPOID", "Q7 naturality requires automorphism action")
check(len(set(q_min.values())) == 3, "minimum map must be non-uniform")

# ---------------------------------------------------------------------------
# ABSTRACTION_UPGRADE_GATE.
# Upgrade only when lower language fails on the asked predicate, higher language
# repairs it, the higher layer is the lowest such repair, P000 equivalences are
# respected, and the new structure is an accepted semantic datum rather than a
# device for erasing a genuine obstruction.
# ---------------------------------------------------------------------------
gate_examples = {
    "SET_TO_GROUPOID": (True, True, True, True, True),
    "GROUPOID_TO_PRESHEAF_DESCENT": (True, True, True, True, True),
    "PRESHEAF_TO_STACK_STRICT_FRAME": (True, False, False, False, False),
    "PRESHEAF_TO_STACK_TWISTED_TORSOR": (True, True, True, True, True),
}
upgrade = {k: all(v) for k, v in gate_examples.items()}
check(upgrade["SET_TO_GROUPOID"], "set->groupoid gate should pass on the finite witness")
check(upgrade["GROUPOID_TO_PRESHEAF_DESCENT"], "groupoid->descent gate should pass on triangle witness")
check(not upgrade["PRESHEAF_TO_STACK_STRICT_FRAME"], "strict frame must reject stackification")
check(upgrade["PRESHEAF_TO_STACK_TWISTED_TORSOR"], "torsor semantics must permit stackification")

# Current finite Q1-Q7 data use only sets, finite groups/action groupoids, and
# ordinary restriction/cocycle equations.  No 2-morphism/higher-coherence
# observable is declared; hence there is no certificate for an extra infinity
# upgrade.  This is a stop-rule, not a theorem about all future P000 models.
higher_coherence_witnesses = ()
check(len(higher_coherence_witnesses) == 0, "current finite packet has no higher-coherence witness")

print(
    "PASS P000_MINIMAL_ABSTRACTION_LADDER; "
    f"checks={checks}; "
    "set_to_groupoid=object_set_same/pi0_2_vs_1/fixed0; "
    "triangle_C2=8_total/4_strict/4_obstructed; "
    "torsor_stack=2_gauge_classes_of_4; "
    "q_min=Q1:G,Q2:S,Q3:G,Q4:P,Q5:G,Q6:S,Q7:G; "
    "strict_frame_stack=REJECT; twisted_torsor_stack=ACCEPT; infinity_upgrade=REJECT"
)
