#!/usr/bin/env python3
from __future__ import annotations
import itertools
import json
from collections import Counter, deque

MOD = 3
ID8 = tuple(range(8))
ID4 = tuple(range(4))

# Certificate coordinates only. Primitive data are the opaque 8-point ternary
# relation BALANCE3 and the typed Hidden-to-Axis bridge.
H = tuple((a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0))
HIDX = {v: i for i, v in enumerate(H)}
LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
LIDX = {v: i for i, v in enumerate(LINES)}


def add3(x, y, z):
    return ((x[0] + y[0] + z[0]) % 3, (x[1] + y[1] + z[1]) % 3)


def norm(v):
    x, y = v
    if x % 3:
        inv = 1 if x % 3 == 1 else 2
        return ((x * inv) % 3, (y * inv) % 3)
    return (0, 1)


FIBER = tuple(LIDX[norm(v)] for v in H)
FIBERS = tuple(tuple(i for i in range(8) if FIBER[i] == s) for s in range(4))
assert sorted(map(len, FIBERS)) == [2, 2, 2, 2]

BALANCE3 = frozenset(
    tuple(sorted((HIDX[x], HIDX[y], HIDX[z])))
    for x, y, z in itertools.combinations(H, 3)
    if add3(x, y, z) == (0, 0)
)
assert len(BALANCE3) == 8

# Q10 CarrierStar3 certificate: four stars, six pair-intersection AxisTypes.
AXES = tuple(itertools.combinations(range(4), 2))
STARS = tuple(frozenset(i for i, e in enumerate(AXES) if s in e) for s in range(4))
assert all(len(J) == 3 for J in STARS)
assert all(len(STARS[i] & STARS[j]) == 1 for i in range(4) for j in range(i + 1, 4))
HIDDEN_AXIS_INC = frozenset((h, e) for h in range(8) for e in STARS[FIBER[h]])
assert len(HIDDEN_AXIS_INC) == 24


def pc(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def ppow(p, n):
    r = tuple(range(len(p)))
    for _ in range(n):
        r = pc(r, p)
    return r


def pord(p):
    one = tuple(range(len(p)))
    r = one
    for n in range(1, 100):
        r = pc(r, p)
        if r == one:
            return n
    raise AssertionError("order bound")


def pgen(gs):
    one = tuple(range(len(gs[0])))
    seen = {one}
    q = deque([one])
    while q:
        x = q.popleft()
        for g in gs:
            y = pc(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def image_triple(p, t):
    return tuple(sorted(p[i] for i in t))


def preserves_rel(p, rel):
    return frozenset(image_triple(p, t) for t in rel) == rel


# Opposite/sign pairing is derived: it is exactly pair codegree zero.
pair_codegree = {}
for i, j in itertools.combinations(range(8), 2):
    pair_codegree[(i, j)] = sum(i in t and j in t for t in BALANCE3)
assert Counter(pair_codegree.values()) == Counter({1: 24, 0: 4})
DERIVED_OPP_PAIRS = frozenset(
    frozenset(pair) for pair, c in pair_codegree.items() if c == 0
)
BRIDGE_PAIRS = frozenset(frozenset(F) for F in FIBERS)
assert DERIVED_OPP_PAIRS == BRIDGE_PAIRS

# Exact primitive automorphism census.
AUT_BAL = tuple(
    p for p in itertools.permutations(range(8)) if preserves_rel(p, BALANCE3)
)
assert len(AUT_BAL) == 48


def star_action(p):
    out = []
    for s in range(4):
        image = {FIBER[p[i]] for i in FIBERS[s]}
        if len(image) != 1:
            return None
        out.append(next(iter(image)))
    return tuple(out)


BAL_ACTIONS = {star_action(p) for p in AUT_BAL}
assert None not in BAL_ACTIONS
assert len(BAL_ACTIONS) == 24
BAL_KERNEL = tuple(p for p in AUT_BAL if star_action(p) == ID4)
assert len(BAL_KERNEL) == 2

# Identify the derived group with GL(2,3); matrices are certificate-only.
def det(A):
    return (A[0] * A[3] - A[1] * A[2]) % 3


def act(A, v):
    return (
        (A[0] * v[0] + A[1] * v[1]) % 3,
        (A[2] * v[0] + A[3] * v[1]) % 3,
    )


GL23 = tuple(A for A in itertools.product(range(3), repeat=4) if det(A))
assert len(GL23) == 48


def matrix_perm(A):
    return tuple(HIDX[act(A, v)] for v in H)


GL_PERMS = {matrix_perm(A) for A in GL23}
assert GL_PERMS == set(AUT_BAL)
Z = tuple(HIDX[((-v[0]) % 3, (-v[1]) % 3)] for v in H)
assert set(BAL_KERNEL) == {ID8, Z}
assert ppow(Z, 2) == ID8

# Structural upper-bound certificate: 8*6 ordered non-antipodal pairs.
ordered_bases = [
    (i, j)
    for i in range(8)
    for j in range(8)
    if i != j and frozenset((i, j)) not in DERIVED_OPP_PAIRS
]
assert len(ordered_bases) == 48
for i, j in ordered_bases:
    assert len({(p[i], p[j]) for p in AUT_BAL}) == 48

# The eight Balance3 tuples form one Aut orbit. Removing one loses S4 surjectivity.
seed_edge = next(iter(BALANCE3))
edge_orbit = {image_triple(p, seed_edge) for p in AUT_BAL}
assert edge_orbit == BALANCE3
deleted = frozenset(set(BALANCE3) - {seed_edge})
AUT_DELETE_ONE_EDGE = tuple(
    p for p in itertools.permutations(range(8)) if preserves_rel(p, deleted)
)
assert len(AUT_DELETE_ONE_EDGE) == 6
assert len({star_action(p) for p in AUT_DELETE_ONE_EDGE if star_action(p) is not None}) == 6

# Nonsplitting via the accepted S4 (3,2,4) presentation type.
S4 = set(BAL_ACTIONS)
qpairs = [
    (a, b)
    for a in S4
    for b in S4
    if pord(a) == 3
    and pord(b) == 2
    and pord(pc(a, b)) == 4
    and len(pgen((a, b))) == 24
]
assert len(qpairs) == 24
fibres = {q: tuple(p for p in AUT_BAL if star_action(p) == q) for q in S4}
assert all(len(v) == 2 for v in fibres.values())
residues = Counter()
for a, b in qpairs:
    for A in fibres[a]:
        for B in fibres[b]:
            residues[ppow(pc(A, B), 4)] += 1
assert residues == Counter({Z: 96})
SECTION_EXISTS_NONSPLIT = False

# Split regression under the SAME signature: a sign-blind coarse interpretation.
COARSE_BALANCE3 = frozenset(
    t
    for t in itertools.combinations(range(8), 3)
    if len({FIBER[i] for i in t}) == 3
)
assert len(COARSE_BALANCE3) == 32
AUT_COARSE = tuple(
    p for p in itertools.permutations(range(8)) if preserves_rel(p, COARSE_BALANCE3)
)
assert len(AUT_COARSE) == 384
assert {star_action(p) for p in AUT_COARSE} == set(itertools.permutations(range(4)))
COARSE_KERNEL = tuple(p for p in AUT_COARSE if star_action(p) == ID4)
assert len(COARSE_KERNEL) == 16


def split_lift(q):
    p = [None] * 8
    for s in range(4):
        for bit, i in enumerate(FIBERS[s]):
            p[i] = FIBERS[q[s]][bit]
    return tuple(p)


for q in itertools.permutations(range(4)):
    L = split_lift(q)
    assert L in AUT_COARSE
    assert star_action(L) == q
for q1 in itertools.permutations(range(4)):
    for q2 in itertools.permutations(range(4)):
        assert split_lift(pc(q1, q2)) == pc(split_lift(q1), split_lift(q2))
SECTION_EXISTS_SPLIT = True

# No-lift regression under the SAME signature: exact Hidden witness + P4 NativeAdj.
P4_EDGES = frozenset(((0, 1), (1, 2), (2, 3)))


def preserves_p4(q):
    return frozenset(tuple(sorted((q[i], q[j]))) for i, j in P4_EDGES) == P4_EDGES


P4_AUT = {q for q in itertools.permutations(range(4)) if preserves_p4(q)}
assert len(P4_AUT) == 2
AUT_NOLIFT = tuple(p for p in AUT_BAL if star_action(p) in P4_AUT)
assert len(AUT_NOLIFT) == 4
assert {star_action(p) for p in AUT_NOLIFT} == P4_AUT

# Deletion audit.
AUT_BRIDGE_ONLY = tuple(
    p for p in itertools.permutations(range(8)) if star_action(p) is not None
)
assert len(AUT_BRIDGE_ONLY) == 384
assert len({star_action(p) for p in AUT_BRIDGE_ONLY}) == 24
assert len([p for p in AUT_BRIDGE_ONLY if star_action(p) == ID4]) == 16
for q in itertools.permutations(range(4)):
    assert split_lift(q) in AUT_BRIDGE_ONLY

# Delete bridge: Hidden GL(2,3) and Q10 carrier S4 decouple.
AUT_NO_BRIDGE_ORDER = len(AUT_BAL) * 24
assert AUT_NO_BRIDGE_ORDER == 1152
# Delete Hidden entirely: Q10 Gen12 base remains S4 -> S4.
AUT_NO_HIDDEN_ORDER = 24

# Q12 is reused as a derived observable: untwisted induced holonomy equals residue.
DERIVED_RESIDUE = Z
DERIVED_UNTWISTED_HOLONOMY = Z
assert DERIVED_RESIDUE == DERIVED_UNTWISTED_HOLONOMY != ID8

report = {
    "schema": "P000_Q15_HIDDEN_KERNEL_MODEL_SIGNATURE_CHECK_V1",
    "status": "PASS",
    "hard_target": "P000_HIDDEN_KERNEL_NONSPLIT_MODEL_SIGNATURE_MINIMALITY_CLASSIFIED",
    "terminal_class": "MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND",
    "primitive_extension": {
        "sorts_added": ["HiddenPhase"],
        "relations_added": [
            "HiddenBalance3(HiddenPhase^3)",
            "HiddenAxisInc(HiddenPhase,AxisType)",
        ],
        "forbidden_as_primitives_and_derived_instead": [
            "Opposite/sign involution",
            "projective 4-block quotient",
            "C2 kernel",
            "GL(2,3) group action",
            "section obstruction",
            "relation residue",
        ],
    },
    "nonsplit_witness": {
        "hidden_points": 8,
        "balance_triples": len(BALANCE3),
        "derived_opposite_pairs": len(DERIVED_OPP_PAIRS),
        "aut_primitive_order": len(AUT_BAL),
        "certificate_identification": "Aut(HiddenBalance3)=GL(2,3)",
        "carrier_image_order": len(BAL_ACTIONS),
        "kernel_order": len(BAL_KERNEL),
        "kernel_nontrivial_generator": "derived global antipode z",
        "quotient_generator_pairs": len(qpairs),
        "lifted_pairs_checked": sum(residues.values()),
        "relation_residue": "(AB)^4=z for all 96 lifted (3,2,4) pairs",
        "section_exists": SECTION_EXISTS_NONSPLIT,
    },
    "same_signature_regressions": {
        "split": {
            "hidden_relation": "coarse sign-blind Balance3",
            "aut_order": len(AUT_COARSE),
            "kernel_order": len(COARSE_KERNEL),
            "carrier_image_order": 24,
            "section_exists": SECTION_EXISTS_SPLIT,
        },
        "no_lift": {
            "hidden_relation": "exact 8-edge Balance3 witness",
            "native_adj": "P4 on four star-anchored Cells",
            "aut_order": len(AUT_NOLIFT),
            "carrier_image_order": len(P4_AUT),
            "section_exists": False,
        },
    },
    "deletion_audit": {
        "delete_HiddenBalance3": {
            "aut_order": len(AUT_BRIDGE_ONLY),
            "kernel_order": 16,
            "carrier_image_order": 24,
            "effect": "split wreath C2^4 semidirect S4; nonsplit obstruction disappears",
        },
        "delete_HiddenAxisInc": {
            "aut_order": AUT_NO_BRIDGE_ORDER,
            "effect": "Hidden GL(2,3) decouples from Q10 carrier S4; pure-carrier section appears",
        },
        "delete_HiddenPhase": {
            "aut_order": AUT_NO_HIDDEN_ORDER,
            "effect": "returns to split Gen12 Q10 base",
        },
        "delete_one_Balance3_tuple": {
            "aut_order": len(AUT_DELETE_ONE_EDGE),
            "carrier_image_order": 6,
            "effect": "full S4 carrier surjectivity is lost; all 8 tuples form one orbit",
        },
    },
    "q12_derived_observable": {
        "kernel_element": "z=unique nonidentity element of ker(rho)",
        "relation_residue": "R=(AB)^4=z",
        "induced_connection_holonomy": "H_ind=R=z",
        "independent_twist_rule_reused": "H=R*D (Q12/T9), not added to Q15 primitives",
    },
    "minimality_scope": (
        "deletion-minimal and relation-role-minimal under typed semantic discipline: "
        "one cross-sort carrier bridge plus one intra-Hidden coupling relation; "
        "no claim against artificial single-symbol arity fusion"
    ),
    "method_reuse": [
        "T7_FINITE_SYMMETRY_EQUIVARIANCE",
        "T9_HOLONOMY_COCOYCLE_GLUING",
        "T2_BLOCK_FINITE_CERTIFICATE",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
