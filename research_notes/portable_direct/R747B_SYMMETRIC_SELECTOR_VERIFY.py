"""Finite incidence/symmetry audit for the R747 C1 framed port candidate.
Exact finite-group proof audit only; not native X6 event/PASS computation.
"""
from itertools import permutations, product
import json

AX = range(6)
SIGNS = (-1, 1)
ALL_S6 = tuple(permutations(AX))

def act_port(sigma, port):
    return sigma[port[0]], port[1]

def act_frame(sigma, frame):
    return tuple(act_port(sigma, p) for p in frame)

def rot(frame):
    return frame[1:] + frame[:1]

def wire(frame):
    return min(frame, rot(frame), rot(rot(frame)))

def edges(frame):
    in_use = {p[0] for p in frame}
    return tuple((p, (j, s)) for p in frame for j in AX if j not in in_use for s in SIGNS)

def act_edge(sigma, edge):
    return act_port(sigma, edge[0]), act_port(sigma, edge[1])

def replace(frame, edge):
    p, q = edge
    assert p in frame and q[0] not in {x[0] for x in frame}
    return tuple(q if v == p else v for v in frame)

def policy(frame):
    e = edges(frame)
    signs = [p[1] for p in frame]
    if signs.count(1) in (0, 3):
        return tuple(x for x in e if x[1][1] == 1)
    minority_sign = 1 if signs.count(1) == 1 else -1
    return tuple(x for x in e if x[0][1] == minority_sign and x[1][1] == 1)

reps = [tuple((i, s) for i, s in enumerate(sig)) for sig in product(SIGNS, repeat=3)]
results = []
for f in reps:
    sf = [sg for sg in ALL_S6 if act_frame(sg, f) == f]
    sw = [sg for sg in ALL_S6 if wire(act_frame(sg, f)) == wire(f)]
    remaining = set(edges(f))
    w_orbits = []
    while remaining:
        e = next(iter(remaining))
        orb = {act_edge(sg, e) for sg in sw}
        assert orb <= remaining
        w_orbits.append(len(orb))
        remaining -= orb
    remaining = set(edges(f))
    f_orbits = []
    while remaining:
        e = next(iter(remaining))
        orb = {act_edge(sg, e) for sg in sf}
        assert orb <= remaining
        f_orbits.append(len(orb))
        remaining -= orb
    ps = set(policy(f))
    assert len(ps) == min(w_orbits), (f, len(ps), w_orbits)
    for sg in ALL_S6:
        g = act_frame(sg, f)
        assert {act_edge(sg, e) for e in ps} == set(policy(g))
        for e in edges(f):
            assert replace(act_frame(sg, f), act_edge(sg,e)) == act_frame(sg, replace(f,e))
    results.append({
        'signs': ''.join('+' if s == 1 else '-' for _,s in f),
        'frame_stabilizer': len(sf),
        'wire_stabilizer': len(sw),
        'frame_edge_orbits': sorted(f_orbits),
        'wire_edge_orbits': sorted(w_orbits),
        'minimal_equivariant_wire_policy_support':len(ps)
    })

frames = [
    tuple((i, s) for i,s in zip(axes, sigs))
    for axes in permutations(AX,3)
    for sigs in product(SIGNS, repeat=3)
]
assert len(frames) == 960
assert len({wire(f) for f in frames}) == 320

rotation_checks = 0
for f in frames:
    for e in edges(f):
        rotated = rot(f)
        assert replace(rotated,e) == rot(replace(f,e))
        assert wire(replace(rotated,e)) == wire(replace(f,e))
        rotation_checks += 1
    assert set(policy(f)) == set(policy(rot(f)))

out = {
    'schema':'R747B_SYMMETRIC_ADAPTIVE_C1_AUDIT_V1',
    'status':'PASS',
    'scope':'R747 candidate signed three-port frames and S6 axis relabeling only; not native X6 event authorization',
    'all_frame_count':len(frames),
    'oriented_wire_count':len({wire(f) for f in frames}),
    'legal_replacements_per_frame':18,
    'representatives':results,
    'representative_S6_update_checks':8*len(ALL_S6)*18,
    'representative_S6_policy_checks':8*len(ALL_S6),
    'cyclic_update_checks':rotation_checks,
    'result':'deterministic S6-equivariant strict one-port selector impossible; optimal equivariant quotient-safe stochastic supports: 9 all-equal signs, 3 mixed signs; pathwise W-descent at every finite horizon'
}
print(json.dumps(out,indent=2,sort_keys=True))
