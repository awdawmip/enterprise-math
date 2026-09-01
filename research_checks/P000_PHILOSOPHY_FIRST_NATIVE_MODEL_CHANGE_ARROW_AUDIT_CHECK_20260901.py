#!/usr/bin/env python3
"""Deterministic regression for P000 Q24 native model-change-arrow audit.

The finite computation is deliberately modest.  It does not define the missing
bare-P000 6D rotation law.  It checks the language-audit certificate and gives a
finite-resolution countermodel showing that a declared three-axis observation
can erase Full-Cell distinctions.
"""
from __future__ import annotations

import itertools
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CERT = ROOT / "research_artifacts" / "P000_PHILOSOPHY_FIRST_NATIVE_MODEL_CHANGE_ARROW_AUDIT" / "P000_Q24_NATIVE_MODEL_CHANGE_ARROW_AUDIT_CERTIFICATE_V1.json"

ALLOWED = {
    "AUTOMORPHISM",
    "ISOMORPHISM_BETWEEN_MODELS",
    "NONINVERTIBLE_MODEL_CHANGE_ARROW",
    "OBSERVATION_NOT_MODEL_ARROW",
    "ILLEGAL_OR_UNDERDEFINED",
}

def fail(message: str) -> None:
    raise AssertionError(message)

def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    if data.get("schema") != "P000_Q24_NATIVE_MODEL_CHANGE_ARROW_AUDIT_CERTIFICATE_V1":
        fail("unexpected certificate schema")

    candidates = data["candidates"]
    ids = [item["id"] for item in candidates]
    if len(ids) != len(set(ids)):
        fail("duplicate candidate id")
    if not candidates:
        fail("empty candidate audit")

    for item in candidates:
        if item["classification"] not in ALLOWED:
            fail(f"invalid classification for {item['id']}")

    classes = {item["id"]: item["classification"] for item in candidates}
    expected = {
        "Q18_Q21_PRIMITIVE_CHANGE": "AUTOMORPHISM",
        "Q10_PRIMITIVE_PRESERVING_MORPHISM": "ISOMORPHISM_BETWEEN_MODELS",
        "BARE_P000_PRIMARY_ROTATION": "ILLEGAL_OR_UNDERDEFINED",
        "SELECT_SLICE_OBSERVE": "OBSERVATION_NOT_MODEL_ARROW",
        "FRAME_CHANGE": "ISOMORPHISM_BETWEEN_MODELS",
        "PRIMITIVE_RELABELING": "AUTOMORPHISM",
        "LOCAL_RESTRICTION_OR_FORGETTING_AS_READOUT": "OBSERVATION_NOT_MODEL_ARROW",
        "LOCAL_RESTRICTION_OR_FORGETTING_AS_FULL_MODEL_ARROW": "ILLEGAL_OR_UNDERDEFINED",
        "TIME_ORDERED_STATE_CHANGE": "ILLEGAL_OR_UNDERDEFINED",
    }
    if classes != expected:
        fail("candidate classification table drifted")

    # Strong gate: no currently classified candidate is a genuine noninvertible
    # Full-Cell model-change arrow.
    genuine = [
        item for item in candidates
        if item["classification"] == "NONINVERTIBLE_MODEL_CHANGE_ARROW"
    ]
    if genuine:
        fail("unexpected native noninvertible model-change arrow")

    # Exact P000-compatible finite-resolution countermodel.
    states = list(itertools.product((0, 1), repeat=6))
    projection = lambda x: x[:3]
    fibers: dict[tuple[int, int, int], list[tuple[int, ...]]] = {}
    for state in states:
        fibers.setdefault(projection(state), []).append(state)

    if len(states) != 64:
        fail("full-state count")
    if len(fibers) != 8:
        fail("slice observation count")
    if {len(v) for v in fibers.values()} != {8}:
        fail("slice fiber sizes")
    collision_pairs = sum(math.comb(len(v), 2) for v in fibers.values())
    if collision_pairs != 224:
        fail("slice collision-pair count")
    if not any(x != y and projection(x) == projection(y)
               for values in fibers.values()
               for x in values for y in values):
        fail("missing same-observation distinct-full-state witness")

    frozen = data["finite_countermodel"]
    observed = {
        "full_state_count": len(states),
        "slice_observation_count": len(fibers),
        "uniform_fiber_size": next(iter({len(v) for v in fibers.values()})),
        "unordered_same_observation_collision_pairs": collision_pairs,
    }
    for key, value in observed.items():
        if frozen[key] != value:
            fail(f"frozen finite countermodel mismatch: {key}")

    # Gate consistency: every legal current full-model arrow is invertible and
    # presentation-equivalent; every noninvertible current operation is typed
    # as observation/reduct rather than as a Full-Cell model arrow.
    for item in candidates:
        if item["full_model_source"] and item["full_model_target"] and item["typed_operation_defined"]:
            if item["classification"] in {"AUTOMORPHISM", "ISOMORPHISM_BETWEEN_MODELS"}:
                if item["invertible"] is not True:
                    fail(f"legal equivalence must be invertible: {item['id']}")
        if item["classification"] == "OBSERVATION_NOT_MODEL_ARROW":
            if not item["observation_or_reduct_only"]:
                fail(f"observation classification without observation/reduct typing: {item['id']}")

    terminal = data["terminal"]
    required = {
        "NO_NATIVE_NONAUTOMORPHISM_MODEL_CHANGE_ARROW_IN_CURRENT_P000_LANGUAGE",
        "SLICE_OBSERVATION_MAP_IS_NOT_A_MODEL_CHANGE_ARROW_AND_TRANSPORT_LINE_CLOSED",
    }
    if set(terminal["disposition"]) != required:
        fail("terminal disposition drifted")

    print(
        "PASS P000_Q24_NATIVE_MODEL_CHANGE_ARROW_AUDIT "
        f"candidates={len(candidates)} full_states={len(states)} "
        f"slice_states={len(fibers)} fiber=8 collisions=224 "
        "native_nonautomorphism_model_change_arrows=0"
    )

if __name__ == "__main__":
    main()
