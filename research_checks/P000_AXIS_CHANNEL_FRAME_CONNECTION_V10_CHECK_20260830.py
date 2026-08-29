#!/usr/bin/env python3
"""Deterministic finite checker for Gen10 P000 axis-channel frame/connection research.

This checker is task-local. It does not alter P000 and it does not treat local
channel-reindexing S6 as a native spatial rotation group.
"""
from itertools import permutations
from math import factorial

N = 6
PERMS = list(permutations(range(N)))
ID = tuple(range(N))


def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(N))


def inv(p):
    r = [None] * N
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)


def generated_group(gens):
    seen = {ID}
    todo = [ID]
    while todo:
        x = todo.pop()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


# b = (E2 E4)(E3 E5), using zero-based E1,...,E6 -> 0,...,5.
b = (0, 3, 4, 1, 2, 5)
assert compose(b, b) == ID

# Gen7 / total-global guard: W is the setwise stabilizer of the 3+3 partition.
B0 = {0, 1, 2}
B1 = {3, 4, 5}
W = []
for p in PERMS:
    image = {p[i] for i in B0}
    if image == B0 or image == B1:
        W.append(p)
assert len(W) == 72
assert b not in W
assert len(generated_group(W + [b])) == 720

# Gen8 relation skeleton: exactly {id,b}.
source_edges = frozenset({(0, 1), (1, 2), (2, 0)})
target_edges = frozenset({(0, 3), (3, 4), (4, 0)})
cycle_pair = {source_edges, target_edges}
matching = {frozenset({1, 3}), frozenset({2, 4})}


def image_edge_set(p, edges):
    return frozenset((p[a], p[c]) for a, c in edges)


def image_matching(p, mat):
    out = set()
    for pair in mat:
        a, c = tuple(pair)
        out.add(frozenset({p[a], p[c]}))
    return out


aut_sigma_b = []
for p in PERMS:
    if p[0] != 0 or p[5] != 5:
        continue
    if {image_edge_set(p, source_edges), image_edge_set(p, target_edges)} != cycle_pair:
        continue
    if image_matching(p, matching) != matching:
        continue
    aut_sigma_b.append(p)
assert set(aut_sigma_b) == {ID, b}

# Gen9 stabilizer law and five-anchor exact presentation.
stabilizers = []
for k in range(7):
    count = sum(all(p[i] == i for i in range(k)) for p in PERMS)
    stabilizers.append(count)
assert stabilizers == [720, 120, 24, 6, 2, 1, 1]
assert stabilizers == [factorial(6 - k) for k in range(7)]

# Injective images of E1,...,E5. The remaining channel uniquely receives E6.
five_anchor_states = list(permutations(range(N), 5))
assert len(five_anchor_states) == 720
for a in five_anchor_states:
    remaining = set(range(N)) - set(a)
    assert len(remaining) == 1
    full = tuple(a) + (remaining.pop(),)
    assert full in PERMS

# Gauge covariance and PASS invariance.
def relabel_matrix(M, g):
    gi = inv(g)
    return [[M[gi[c]][gi[d]] for d in range(N)] for c in range(N)]


def relabel_vector(V, g):
    gi = inv(g)
    return [V[gi[c]] for c in range(N)]


def pass_matrix(M, f):
    return [[M[f[i]][f[j]] for j in range(N)] for i in range(N)]


f = (2, 5, 1, 4, 0, 3)
M_probe = [[10 * i + j for j in range(N)] for i in range(N)]
P_probe = pass_matrix(M_probe, f)
for g in PERMS:
    f2 = compose(g, f)
    M2 = relabel_matrix(M_probe, g)
    assert pass_matrix(M2, f2) == P_probe

# Frame-induced connection: inverse, composition, flat loop, gauge law.
def transport_from_frames(fx, fy):
    return compose(fy, inv(fx))


def path_transport(path, transports):
    cur = ID
    for x, y in zip(path, path[1:]):
        cur = compose(transports[(x, y)], cur)
    return cur


frames = [
    ID,
    (1, 0, 2, 3, 5, 4),
    (2, 1, 0, 5, 4, 3),
    (5, 4, 3, 2, 1, 0),
]
cycle_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
T = {}
for x, y in cycle_edges:
    T[(x, y)] = transport_from_frames(frames[x], frames[y])
    T[(y, x)] = inv(T[(x, y)])

for x, y in list(T):
    assert T[(y, x)] == inv(T[(x, y)])
assert path_transport([0, 1, 2, 3, 0], T) == ID
assert path_transport([0, 1, 2], T) == transport_from_frames(frames[0], frames[2])
assert path_transport([0, 3, 2], T) == transport_from_frames(frames[0], frames[2])

gauges = [PERMS[17], PERMS[51], PERMS[203], PERMS[511]]
frames_g = [compose(g, h) for g, h in zip(gauges, frames)]
for x, y in T:
    lhs = transport_from_frames(frames_g[x], frames_g[y])
    rhs = compose(gauges[y], compose(T[(x, y)], inv(gauges[x])))
    assert lhs == rhs

# Independent connection can have nontrivial holonomy.
T_nonflat = {}
for x, y in [(0, 1), (1, 2), (2, 3)]:
    T_nonflat[(x, y)] = ID
    T_nonflat[(y, x)] = ID
T_nonflat[(3, 0)] = b
T_nonflat[(0, 3)] = b
H = path_transport([0, 1, 2, 3, 0], T_nonflat)
assert H == b and H != ID

T_nonflat_g = {}
for (x, y), t in T_nonflat.items():
    T_nonflat_g[(x, y)] = compose(gauges[y], compose(t, inv(gauges[x])))
Hg = path_transport([0, 1, 2, 3, 0], T_nonflat_g)
assert Hg == compose(gauges[0], compose(H, inv(gauges[0])))
assert Hg != ID

# Omega_b is conditional: an allowed empty model and an allowed nonempty model.
def zero_matrix():
    return [[0 for _ in range(N)] for _ in range(N)]


def omega_b(M, frame):
    P = pass_matrix(M, frame)
    p24, p42 = P[1][3], P[3][1]
    p35, p53 = P[2][4], P[4][2]
    return (p24 > 0 and p35 > 0 and p24 == p42 and p35 == p53), (p24, p42, p35, p53)


M_empty = zero_matrix()
for i in range(N):
    M_empty[i][i] = 1
empty_ok, _ = omega_b(M_empty, ID)
assert not empty_ok

M_nonempty = zero_matrix()
for i in range(N):
    M_nonempty[i][i] = 1
M_nonempty[1][3] = M_nonempty[3][1] = 2
M_nonempty[2][4] = M_nonempty[4][2] = 3
nonempty_ok, payload = omega_b(M_nonempty, ID)
assert nonempty_ok
assert payload == (2, 2, 3, 3)

# Omega_b is gauge invariant for all local S6 presentation changes.
for g in PERMS:
    fg = compose(g, ID)
    Mg = relabel_matrix(M_nonempty, g)
    ok, pay = omega_b(Mg, fg)
    assert ok and pay == payload

# Omega_b nonempty does NOT imply a local PF10 b-symmetry.
I = [1] * N
I[1] = 1
I[3] = 2
O = [1] * N
local_b_invariant = (
    relabel_vector(I, b) == I
    and relabel_vector(O, b) == O
    and relabel_matrix(M_nonempty, b) == M_nonempty
)
assert nonempty_ok
assert not local_b_invariant

# P000 / typing guards represented as explicit terminal assertions.
P000_MUTATED = False
NATIVE_S6_PROMOTED = False
NATIVE_STATE_QUOTIENT_USED = False
TIME_USED_AS_FRAME_SLOT = False
assert not P000_MUTATED
assert not NATIVE_S6_PROMOTED
assert not NATIVE_STATE_QUOTIENT_USED
assert not TIME_USED_AS_FRAME_SLOT

print("PASS P000_AXIS_CHANNEL_FRAME_CONNECTION_V10_CHECK")
print("terminal_class=FRAME_CONNECTION_CONSTRUCTED_BUT_FRAMED_BMix_DOMAIN_STRICTLY_CONDITIONAL")
print("gen9_local_channel_symmetry=720")
print("gen9_anchor_stabilizers=" + ",".join(map(str, stabilizers)))
print("five_anchor_states=720")
print("gen8_axis_skeleton_automorphism_order=2")
print("gen7_block_pure_wreath_order=72")
print("total_global_W_plus_b_group_order=720")
print("frame_induced_loop_holonomy=identity")
print("independent_connection_nontrivial_holonomy_witness=b")
print("framed_PASS_gauge_invariant=true")
print("Omega_b_forced=false")
print("Omega_b_possible=true")
print("Omega_b_nonempty_but_local_PF10_b_symmetry_can_fail=true")
print("full_P000_native_rotation_promoted=false")
print("native_state_quotient_used=false")
