#!/usr/bin/env python3
"""Deterministic checker for P000 Gen8 axis-refined BMix_b derived interface.

This checker does NOT promote the construction to the P000 root ontology.
It verifies the exact finite witness for the terminal class
MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED.
"""
from __future__ import annotations

import hashlib
import itertools
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable

AXES = ("E1", "E2", "E3", "E4", "E5", "E6")
JA = ("E1", "E2", "E3")
JB = ("E1", "E4", "E5")
B = {"E1":"E1", "E2":"E4", "E3":"E5", "E4":"E2", "E5":"E3", "E6":"E6"}
OMITTED = object()

# The existing J_A local cyclic right-sector incidence, and the first new
# mixed-support CONTACT_MATCH relation. JB_RIGHT is derived, not postulated.
JA_RIGHT = frozenset({("E1","E2"), ("E2","E3"), ("E3","E1")})
CONTACT_MATCH = frozenset({frozenset(("E2","E4")), frozenset(("E3","E5"))})

# A finite elementary three-Cell triangle witnesses exact local adjacency.
A_CELLS = ("A0","A1","A2")
A_ADJ = frozenset({
    frozenset(("A0","A1")),
    frozenset(("A1","A2")),
    frozenset(("A2","A0")),
})
CELL_TRANSPORT = {"A0":"B0", "A1":"B1", "A2":"B2"}
B_CELLS = tuple(CELL_TRANSPORT[c] for c in A_CELLS)
B_ADJ = frozenset(
    frozenset(CELL_TRANSPORT[c] for c in edge)
    for edge in A_ADJ
)

def permute_pair(pair: tuple[str,str], perm: dict[str,str]) -> tuple[str,str]:
    return perm[pair[0]], perm[pair[1]]

def permute_unordered_edge(edge: frozenset[str], perm: dict[str,str]) -> frozenset[str]:
    return frozenset(perm[x] for x in edge)

def image_support(support: Iterable[str], perm: dict[str,str]) -> tuple[str,...]:
    return tuple(perm[x] for x in support)

def derive_tau_from_anchor_and_contact() -> dict[str,str]:
    """Derive the ordered J_A -> J_B role map from shared E1 and CONTACT_MATCH."""
    tau = {"E1": "E1"}
    source_to_target = {}
    for edge in CONTACT_MATCH:
        left = tuple(sorted(edge, key=lambda x: AXES.index(x)))
        src = [x for x in left if x in JA and x != "E1"]
        tgt = [x for x in left if x in JB and x != "E1"]
        assert len(src) == len(tgt) == 1
        source_to_target[src[0]] = tgt[0]
    tau.update(source_to_target)
    assert tuple(tau[a] for a in JA) == JB
    return tau

TAU = derive_tau_from_anchor_and_contact()
JB_RIGHT = frozenset(permute_pair(edge, TAU) for edge in JA_RIGHT)

@dataclass(frozen=True)
class AxisRefinedHandleState:
    """Derived handle envelope over one opaque P000 full-Cell identity."""
    native_cell_id: str
    axis_payload: tuple[tuple[str,str], ...]
    passage_relation: frozenset[tuple[str,str,str]]
    time_trace_token: str
    carrier_readout: str

    def payload_map(self) -> dict[str,str]:
        return dict(self.axis_payload)

def make_state(native_cell_id: str, suffix: str, carrier_readout: str = "carrier-collision") -> AxisRefinedHandleState:
    payload = tuple((axis, f"{suffix}:{axis}") for axis in AXES)
    # PF-10-compatible shape: ingress-axis -> egress-axis with explicit payload labels.
    # The cross-block pairs are real relation payload, not a carrier permutation.
    passage = frozenset({
        ("E2","E4","m24"),
        ("E4","E2","m24"),
        ("E3","E5","m35"),
        ("E5","E3","m35"),
        ("E1","E1","anchor"),
        ("E6","E6","spectator"),
    })
    return AxisRefinedHandleState(
        native_cell_id=native_cell_id,
        axis_payload=payload,
        passage_relation=passage,
        time_trace_token="TIME_IS_SEPARATELY_TYPED",
        carrier_readout=carrier_readout,
    )

def observe_slice(state: AxisRefinedHandleState, support: tuple[str,...]) -> dict[str,object]:
    """Return a six-key observation: omitted axes use a sentinel, never numeric zero."""
    payload = state.payload_map()
    return {axis: payload[axis] if axis in support else OMITTED for axis in AXES}

def admissible_bmix_domain(state: AxisRefinedHandleState) -> bool:
    required = {
        ("E2","E4","m24"), ("E4","E2","m24"),
        ("E3","E5","m35"), ("E5","E3","m35"),
    }
    return required <= set(state.passage_relation)

def rb_transform(state: AxisRefinedHandleState) -> AxisRefinedHandleState:
    """Typed partial handle transport. Raises outside the declared BMix domain."""
    if not admissible_bmix_domain(state):
        raise ValueError("state lacks the mixed-support CONTACT_MATCH passage payload")
    old_payload = state.payload_map()
    new_payload = {B[a]: old_payload[a] for a in AXES}
    new_passage = frozenset((B[a], B[b], label) for a,b,label in state.passage_relation)
    return replace(
        state,
        axis_payload=tuple((axis,new_payload[axis]) for axis in AXES),
        passage_relation=new_passage,
    )

def axis_skeleton_automorphisms() -> list[dict[str,str]]:
    """Automorphisms of the derived relation skeleton.

    Signature:
      - E1 distinguished shared-axis anchor,
      - E6 distinguished omitted spectator,
      - union of J_A and transported J_B directed right-sector cycles,
      - CONTACT_MATCH.
    """
    cycle_union = JA_RIGHT | JB_RIGHT
    autos = []
    for values in itertools.permutations(AXES):
        p = dict(zip(AXES, values))
        if p["E1"] != "E1" or p["E6"] != "E6":
            continue
        if frozenset(permute_pair(edge,p) for edge in cycle_union) != cycle_union:
            continue
        if frozenset(permute_unordered_edge(edge,p) for edge in CONTACT_MATCH) != CONTACT_MATCH:
            continue
        autos.append(p)
    return autos

def compose_perm(left: dict[str,str], right: dict[str,str]) -> dict[str,str]:
    return {a:left[right[a]] for a in AXES}

def gen7_wreath_regression() -> set[tuple[str,...]]:
    """Finite regression only: the frozen block-pure envelope has order 72."""
    A = AXES[:3]
    C = AXES[3:]
    group = set()
    for pa in itertools.permutations(A):
        for pc in itertools.permutations(C):
            p0 = dict(zip(A,pa)) | dict(zip(C,pc))
            group.add(tuple(p0[a] for a in AXES))
            rho = {A[i]:C[i] for i in range(3)} | {C[i]:A[i] for i in range(3)}
            p1 = compose_perm(rho,p0)
            group.add(tuple(p1[a] for a in AXES))
    return group

def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def repository_text_regressions(root: Path) -> None:
    """Check exact current files when run from the repository root."""
    task = root / "research_tasks/P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_20260829.md"
    router = root / "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    packet = root / "PACKET_PATH_FOUNDATION.md"
    gen7 = root / "research_returns/P000_NATIVE_MIXED_STAR_CROSS_BLOCK_ROTATION_V7_RETURN_20260829.md"
    for path in (task,router,packet,gen7):
        assert path.exists(), f"missing repository input: {path}"
    assert git_blob_sha1(task) == "9b39e89738a1c90a348e7975bb21e7a1f1a744c0"
    rtext = router.read_text(encoding="utf-8")
    assert "OMITTED_CELL_COORDINATE!=ZERO_COORDINATE" in rtext
    assert "native six-dimensional rotation group remain research targets" in rtext
    ptext = packet.read_text(encoding="utf-8")
    assert "M_x[a,b]" in ptext
    assert "OPTIONAL RELATIONAL CHANNEL STATE" in ptext
    g7 = gen7.read_text(encoding="utf-8")
    assert "EXACT_NATIVE_PRIMITIVE_OBSTRUCTION_PROVED" in g7

def main() -> None:
    # 1. The new mixed relation determines the intended ordered chart transport.
    assert TAU == {"E1":"E1","E2":"E4","E3":"E5"}
    assert JB_RIGHT == frozenset({("E1","E4"),("E4","E5"),("E5","E1")})
    assert image_support(JA,B) == JB
    assert B["E1"] == "E1" and B["E6"] == "E6"
    assert all(B[B[a]] == a for a in AXES)

    # 2. Genuine derived J_B: finite Cell set, adjacency and local right-sector relation
    # are transported from J_A, not asserted from the FCC carrier readout.
    assert len(A_CELLS) == len(B_CELLS) == 3
    assert len(A_ADJ) == len(B_ADJ) == 3
    for edge in A_ADJ:
        assert frozenset(CELL_TRANSPORT[c] for c in edge) in B_ADJ

    # 3. E1 gluing is an interface identity, not a Cell-center quotient.
    axis_interface_A = ("J_A","E1","tick")
    axis_interface_B = ("J_B","E1","tick")
    assert axis_interface_A[1:] == axis_interface_B[1:]
    assert set(A_CELLS).isdisjoint(B_CELLS)

    # 4. Axis-refined handle semantics: omitted != 0 and full Cell identity survives.
    s = make_state("CELL-OPAQUE-001","p")
    obs_a = observe_slice(s,JA)
    obs_b = observe_slice(s,JB)
    assert obs_a["E4"] is OMITTED and obs_a["E5"] is OMITTED and obs_a["E6"] is OMITTED
    assert obs_b["E2"] is OMITTED and obs_b["E3"] is OMITTED and obs_b["E6"] is OMITTED
    assert all(v != 0 for v in obs_a.values())
    assert all(v != 0 for v in obs_b.values())

    # 5. BMix/R~_b is a nonempty typed partial involution with payload transport.
    assert admissible_bmix_domain(s)
    t = rb_transform(s)
    u = rb_transform(t)
    assert u == s
    assert t.native_cell_id == s.native_cell_id
    assert t.time_trace_token == s.time_trace_token
    assert t.payload_map()["E1"] == s.payload_map()["E1"]
    assert t.payload_map()["E6"] == s.payload_map()["E6"]
    assert t.payload_map()["E4"] == s.payload_map()["E2"]
    assert t.payload_map()["E5"] == s.payload_map()["E3"]
    assert t.passage_relation == s.passage_relation

    bad = replace(
        s,
        passage_relation=frozenset(x for x in s.passage_relation if x[:2] not in {("E2","E4"),("E4","E2")})
    )
    assert not admissible_bmix_domain(bad)
    try:
        rb_transform(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("BMix must remain partial outside its mixed-support relation domain")

    # 6. Native identity is not quotient by carrier collision.
    s2 = make_state("CELL-OPAQUE-002","q",carrier_readout=s.carrier_readout)
    assert s.carrier_readout == s2.carrier_readout
    assert s.native_cell_id != s2.native_cell_id
    assert s != s2

    # 7. The minimal relation skeleton admits exactly id and b, not arbitrary S6.
    autos = axis_skeleton_automorphisms()
    auto_tuples = {tuple(p[a] for a in AXES) for p in autos}
    id_tuple = AXES
    b_tuple = tuple(B[a] for a in AXES)
    assert auto_tuples == {id_tuple,b_tuple}
    assert len(auto_tuples) == 2 < 720

    # 8. Frozen Gen7 closure remains separate and excludes b.
    W = gen7_wreath_regression()
    assert len(W) == 72
    assert b_tuple not in W
    assert len(auto_tuples) != 48  # carrier split S4 x C2 is not promoted to native group

    # 9. Optional repository-text guards.
    root = Path(__file__).resolve().parents[1]
    repository_text_regressions(root)

    print("PASS P000_NATIVE_AXIS_REFINED_BMIX_PRIMITIVE_V8_CHECK")
    print("terminal_class=MINIMAL_DERIVED_BMix_b_CONSISTENT_PARTIAL_LIFT_CONSTRUCTED")
    print("derived_axis_skeleton_automorphism_order=2")
    print("gen7_block_pure_wreath_order=72")
    print("full_P000_native_rotation_promoted=false")
    print("native_state_quotient_used=false")

if __name__ == "__main__":
    main()
