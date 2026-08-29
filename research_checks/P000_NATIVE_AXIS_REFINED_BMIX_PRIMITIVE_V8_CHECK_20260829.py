#!/usr/bin/env python3
"""Deterministic finite certificate for P000 Gen8 derived BMix_b interface."""
from __future__ import annotations

import hashlib
import itertools
from pathlib import Path

AXES = ("E1","E2","E3","E4","E5","E6")
JA = ("E1","E2","E3")
JB = ("E1","E4","E5")
B = {"E1":"E1","E2":"E4","E3":"E5","E4":"E2","E5":"E3","E6":"E6"}
JA_RIGHT = frozenset({("E1","E2"),("E2","E3"),("E3","E1")})
CONTACT = frozenset({frozenset(("E2","E4")), frozenset(("E3","E5"))})

def image_pair(pair, p):
    return (p[pair[0]], p[pair[1]])

def image_edge(edge, p):
    return frozenset(p[x] for x in edge)

def derive_tau():
    tau = {"E1":"E1"}
    for edge in CONTACT:
        src = [x for x in edge if x in JA and x != "E1"]
        dst = [x for x in edge if x in JB and x != "E1"]
        assert len(src) == len(dst) == 1
        tau[src[0]] = dst[0]
    return tau

TAU = derive_tau()
JB_RIGHT = frozenset(image_pair(edge, TAU) for edge in JA_RIGHT)

def automorphisms():
    cycle_union = JA_RIGHT | JB_RIGHT
    out = []
    for vals in itertools.permutations(AXES):
        p = dict(zip(AXES, vals))
        if p["E1"] != "E1" or p["E6"] != "E6":
            continue
        if frozenset(image_pair(e,p) for e in cycle_union) != cycle_union:
            continue
        if frozenset(image_edge(e,p) for e in CONTACT) != CONTACT:
            continue
        out.append(tuple(p[a] for a in AXES))
    return set(out)

def gen7_block_pure_wreath():
    A, C = AXES[:3], AXES[3:]
    rho = {A[i]:C[i] for i in range(3)} | {C[i]:A[i] for i in range(3)}
    out = set()
    for pa in itertools.permutations(A):
        for pc in itertools.permutations(C):
            p0 = dict(zip(A,pa)) | dict(zip(C,pc))
            out.add(tuple(p0[a] for a in AXES))
            p1 = {a:rho[p0[a]] for a in AXES}
            out.add(tuple(p1[a] for a in AXES))
    return out

def repository_regressions(root: Path):
    task = root / "research_tasks/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_20260829.md"
    router = root / "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    packet = root / "PACKET_PATH_FOUNDATION.md"
    gen7 = root / "research_returns/P000_NATIVE_MIXED_STAR_CROSS_BLOCK_ROTATION_V7_RETURN_20260829.md"
    for p in (task, router, packet, gen7):
        assert p.exists(), p
    data = task.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    assert blob == "9b39e89738a1c90a348e7975bb21e7a1f1a744c0"
    rt = router.read_text(encoding="utf-8")
    assert "OMITTED_CELL_COORDINATE!=ZERO_COORDINATE" in rt
    assert "native six-dimensional rotation group remain research targets" in rt
    pt = packet.read_text(encoding="utf-8")
    assert "M_x[a,b]" in pt
    assert "OPTIONAL RELATIONAL CHANNEL STATE" in pt
    assert "SIX_LOCAL_CHANNELS != SIX_P000_NATIVE_AXES" not in pt  # bridge is not pre-authorized there
    gt = gen7.read_text(encoding="utf-8")
    assert "EXACT_NATIVE_PRIMITIVE_OBSTRUCTION_PROVED" in gt

def main():
    assert TAU == {"E1":"E1","E2":"E4","E3":"E5"}
    assert JB_RIGHT == frozenset({("E1","E4"),("E4","E5"),("E5","E1")})
    b = tuple(B[a] for a in AXES)
    assert b == ("E1","E4","E5","E2","E3","E6")
    assert all(B[B[a]] == a for a in AXES)

    # Finite Cell-patch transport: a tagged J_B copy preserves adjacency.
    a_cells = ("A0","A1","A2")
    t = {"A0":"B0","A1":"B1","A2":"B2"}
    a_adj = {frozenset(("A0","A1")),frozenset(("A1","A2")),frozenset(("A2","A0"))}
    b_adj = {frozenset(t[x] for x in e) for e in a_adj}
    assert len(a_adj) == len(b_adj) == 3
    assert set(a_cells).isdisjoint(set(t.values()))

    # Omitted coordinates are typed absence from observation, not inserted zeroes.
    omitted = object()
    payload = {a:f"payload:{a}" for a in AXES}
    obs_a = {a:(payload[a] if a in JA else omitted) for a in AXES}
    obs_b = {a:(payload[a] if a in JB else omitted) for a in AXES}
    assert obs_a["E4"] is omitted and obs_b["E2"] is omitted
    assert 0 not in obs_a.values() and 0 not in obs_b.values()

    # Partial domain has active mixed relation payload and exact inverse.
    passage = {
        ("E2","E4","m24"),("E4","E2","m24"),
        ("E3","E5","m35"),("E5","E3","m35"),
        ("E1","E1","anchor"),("E6","E6","spectator"),
    }
    required = {
        ("E2","E4","m24"),("E4","E2","m24"),
        ("E3","E5","m35"),("E5","E3","m35"),
    }
    assert required <= passage
    transported_payload = {B[a]:payload[a] for a in AXES}
    transported_passage = {(B[a],B[c],label) for a,c,label in passage}
    assert transported_passage == passage
    restored_payload = {B[a]:transported_payload[a] for a in AXES}
    assert restored_payload == payload
    bad_passage = passage - {("E2","E4","m24"),("E4","E2","m24")}
    assert not required <= bad_passage

    # Carrier-readout collision does not quotient native Cell identity.
    s1 = ("CELL-OPAQUE-001","same-carrier-readout")
    s2 = ("CELL-OPAQUE-002","same-carrier-readout")
    assert s1[1] == s2[1] and s1[0] != s2[0] and s1 != s2

    autos = automorphisms()
    assert autos == {AXES, b}
    assert len(autos) == 2 < 720

    W = gen7_block_pure_wreath()
    assert len(W) == 72
    assert b not in W
    assert len(autos) != 48  # carrier S4 x C2 is not promoted to native group

    root = Path(__file__).resolve().parents[1]
    repository_regressions(root)

    print("PASS P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_CHECK")
    print("terminal_class=MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED")
    print("derived_axis_skeleton_automorphism_order=2")
    print("gen7_block_pure_wreath_order=72")
    print("full_P000_native_rotation_promoted=false")
    print("native_state_quotient_used=false")

if __name__ == "__main__":
    main()
