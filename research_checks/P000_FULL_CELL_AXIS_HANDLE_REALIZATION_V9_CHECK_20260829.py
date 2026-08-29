#!/usr/bin/env python3
"""Deterministic obstruction certificate for P000 full-Cell axis-handle Gen9.

The finite countermodel is intentionally native/relational: Cells are opaque,
adjacency is primitive, PF-10 channels carry only I/O/M passage data, and no
channel is identified with an axis or with an FCC carrier line.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

AXES = ("E1", "E2", "E3", "E4", "E5", "E6")
CHANNELS = tuple(range(6))
JA = ("E1", "E2", "E3")
JB = ("E1", "E4", "E5")
B = {"E1": "E1", "E2": "E4", "E3": "E5", "E4": "E2", "E5": "E3", "E6": "E6"}
JA_RIGHT = frozenset({("E1", "E2"), ("E2", "E3"), ("E3", "E1")})
CONTACT = frozenset({frozenset(("E2", "E4")), frozenset(("E3", "E5"))})


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def symmetric_pf10_state():
    ingress = {c: 1 for c in CHANNELS}
    egress = {c: 1 for c in CHANNELS}
    passage = {(a, b): (1 if a == b else 0) for a in CHANNELS for b in CHANNELS}
    return ingress, egress, passage


def pf10_relabel_automorphisms():
    ingress, egress, passage = symmetric_pf10_state()
    out = set()
    for vals in itertools.permutations(CHANNELS):
        p = dict(zip(CHANNELS, vals))
        if not all(ingress[p[c]] == ingress[c] for c in CHANNELS):
            continue
        if not all(egress[p[c]] == egress[c] for c in CHANNELS):
            continue
        if not all(passage[p[a], p[b]] == passage[a, b] for a in CHANNELS for b in CHANNELS):
            continue
        out.add(vals)
    return out


def anchor_stabilizer_order(autos, k: int) -> int:
    """Fix k distinct axis->channel anchor incidences, axes pointwise named."""
    fixed_channels = set(CHANNELS[:k])
    count = 0
    for vals in autos:
        p = dict(zip(CHANNELS, vals))
        if all(p[c] == c for c in fixed_channels):
            count += 1
    return count


def gen8_axis_skeleton_automorphisms():
    tau = {"E1": "E1", "E2": "E4", "E3": "E5"}
    jb_right = frozenset((tau[a], tau[b]) for a, b in JA_RIGHT)
    cycle_union = JA_RIGHT | jb_right
    out = set()
    for vals in itertools.permutations(AXES):
        p = dict(zip(AXES, vals))
        if p["E1"] != "E1" or p["E6"] != "E6":
            continue
        if frozenset((p[a], p[b]) for a, b in cycle_union) != cycle_union:
            continue
        if frozenset(frozenset(p[x] for x in edge) for edge in CONTACT) != CONTACT:
            continue
        out.add(vals)
    return out


def gen7_block_pure_wreath():
    left, right = AXES[:3], AXES[3:]
    swap = {left[i]: right[i] for i in range(3)} | {right[i]: left[i] for i in range(3)}
    out = set()
    for p_left in itertools.permutations(left):
        for p_right in itertools.permutations(right):
            p0 = dict(zip(left, p_left)) | dict(zip(right, p_right))
            out.add(tuple(p0[a] for a in AXES))
            p1 = {a: swap[p0[a]] for a in AXES}
            out.add(tuple(p1[a] for a in AXES))
    return out


def repository_inventory(root: Path) -> None:
    pinned = {
        "research_tasks/P000_FULL_CELL_AXIS_HANDLE_REALIZATION_V9_20260829.md": "d610329b797908ce396587281050ee747447faa0",
        "p000_reality_foundation.json": "2eb853aa6bd2ff7e9f19b5eb4f231cec00a31900",
        "definitions/00_CURRENT_NATIVE_FOUNDATION.md": "3304733317b53069b0a8cee92e59018c3c0e9f5f",
        "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md": "b84ea850151386dae04e2798b20430381afb8786",
        "PACKET_PATH_FOUNDATION.md": "e725a95fd1be00f99233586311bc6d0e95888e7b",
        "research_returns/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_RETURN_20260829.md": "659a70074998f1d24c413934076e3a1018a13ce9",
        "driver_reviews/P000_NATIVE_AXIS_REFINED_BMIX_V8_DRIVER_REVIEW_20260829.md": "d22d30161c76cab5d2102ff32b1132cd73acab5c",
    }
    for rel, expected in pinned.items():
        path = root / rel
        assert path.exists(), rel
        assert git_blob_sha1(path) == expected, (rel, git_blob_sha1(path), expected)

    p000 = (root / "p000_reality_foundation.json").read_text(encoding="utf-8")
    router = (root / "definitions/00_CURRENT_NATIVE_FOUNDATION.md").read_text(encoding="utf-8")
    carrier = (root / "definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md").read_text(encoding="utf-8")
    packet = (root / "PACKET_PATH_FOUNDATION.md").read_text(encoding="utf-8")
    gen8 = (root / "research_returns/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_RETURN_20260829.md").read_text(encoding="utf-8")
    review = (root / "driver_reviews/P000_NATIVE_AXIS_REFINED_BMIX_V8_DRIVER_REVIEW_20260829.md").read_text(encoding="utf-8")

    assert '"ENTERPRISE_SPACE_DIMENSION": 6' in p000
    assert '"ENTERPRISE_TIME_DIMENSION": 1' in p000
    assert '"ENTERPRISE_SPACE_KIND": "DISCRETE_CELL_SPACE"' in p000
    assert "OMITTED_CELL_COORDINATE!=ZERO_COORDINATE" in router
    assert "native six-dimensional rotation group remain research targets" in router
    assert "exact bridge `E_i <-> L_j + chart orientation/transition` remain to be completed" in carrier
    assert "PF-04 — ADJACENCY IS THE ONLY REQUIRED LOCAL RELATION FOR PATH" in packet
    assert "PF-10 — IDEAL CHANNEL STATES ARE ADDITIONAL RELATIONAL STRUCTURE" in packet
    assert "M_x[a,b]" in packet
    assert "No channel pair is automatically named straight, turn, angle, curvature, or opposite." in packet
    assert "no authorized bridge from them to native axes `E_1,...,E_6`" in gen8
    assert "AXIS_HANDLE_ATTACHMENT_TO_CURRENT_FULL_P000_CELL_NOT_CANONICALLY_DERIVED" in gen8
    assert "current canonical full P000 Cell substrate does not yet derive this attachment" in review


def main() -> None:
    # Current primitive countermodel: two opaque adjacent Cells, identical symmetric
    # PF-10 local states, no cross-sort axis/channel relation and no channel gluing.
    cells = ("x0", "x1")
    adjacency = {frozenset(cells)}
    assert len(adjacency) == 1

    autos = pf10_relabel_automorphisms()
    assert len(autos) == math.factorial(6) == 720

    # Any unique axis-handle map must be invariant under primitive-preserving
    # channel reindexings. The symmetric model has no globally fixed channel.
    for c in CHANNELS:
        assert any(vals[c] != c for vals in autos)

    # With no cross-Cell channel transport relation, every permutation is an
    # observationally admissible gluing from the six slots of x0 to x1.
    gluing_choices = len(autos)
    assert gluing_choices == 720

    # Exact lower bound for explicit anchor payload in the worst symmetric Cell.
    stabilizers = {k: anchor_stabilizer_order(autos, k) for k in range(7)}
    assert stabilizers == {0: 720, 1: 120, 2: 24, 3: 6, 4: 2, 5: 1, 6: 1}
    assert all(stabilizers[k] == math.factorial(6 - k) for k in range(7))
    minimum_anchors = min(k for k in range(6) if stabilizers[k] == 1)
    assert minimum_anchors == 5

    # The allowed symmetric PF-10 model contains no off-diagonal passage, so
    # CONTACT_MATCH_b cannot be forced from current adjacency/path/channel axioms.
    _, _, passage = symmetric_pf10_state()
    assert passage[1, 3] == passage[3, 1] == 0
    assert passage[2, 4] == passage[4, 2] == 0

    # Gen8 and Gen7 regressions stay frozen and separate from the new channel
    # ambiguity. 720 channel relabelings are NOT 720 native rotations.
    gen8_autos = gen8_axis_skeleton_automorphisms()
    b = tuple(B[a] for a in AXES)
    assert gen8_autos == {AXES, b}
    assert len(gen8_autos) == 2
    W = gen7_block_pure_wreath()
    assert len(W) == 72
    assert b not in W

    # Native identity is not a carrier/readout quotient.
    s1 = ("CELL-OPAQUE-001", "same-readout")
    s2 = ("CELL-OPAQUE-002", "same-readout")
    assert s1[0] != s2[0] and s1[1] == s2[1] and s1 != s2

    # Omission remains typed absence, never inserted numeric zero.
    omitted = object()
    observation = {a: (f"payload:{a}" if a in JA else omitted) for a in AXES}
    assert observation["E4"] is omitted and observation["E5"] is omitted and observation["E6"] is omitted
    assert 0 not in observation.values()

    root = Path(__file__).resolve().parents[1]
    repository_inventory(root)

    cert = json.loads((root / "research_artifacts/P000_FULL_CELL_AXIS_HANDLE_REALIZATION_V9/MODEL_CERTIFICATE.json").read_text(encoding="utf-8"))
    assert cert["terminal_class"] == "EXACT_FULL_CELL_AXIS_HANDLE_BRIDGE_OBSTRUCTION_PROVED"
    assert cert["finite_results"]["pf10_channel_relabel_automorphism_order"] == 720
    assert cert["finite_results"]["minimum_independent_axis_channel_anchors_for_unique_bijection_in_symmetric_case"] == 5
    assert cert["minimal_extension"]["relation_type"] == "AXIS_CHANNEL_FRAME(x,E,c)"
    assert cert["promotion_guards"]["full_P000_native_b_promoted"] is False
    assert cert["promotion_guards"]["arbitrary_S6_native_rotation_promoted"] is False

    print("PASS P000_FULL_CELL_AXIS_HANDLE_REALIZATION_V9_CHECK")
    print("terminal_class=EXACT_FULL_CELL_AXIS_HANDLE_BRIDGE_OBSTRUCTION_PROVED")
    print("pf10_channel_relabel_automorphism_order=720")
    print("cross_cell_channel_gluing_choices=720")
    print("minimum_axis_channel_anchors_for_unique_frame=5")
    print("gen8_axis_skeleton_automorphism_order=2")
    print("gen7_block_pure_wreath_order=72")
    print("full_P000_native_b_promoted=false")
    print("native_state_quotient_used=false")


if __name__ == "__main__":
    main()
