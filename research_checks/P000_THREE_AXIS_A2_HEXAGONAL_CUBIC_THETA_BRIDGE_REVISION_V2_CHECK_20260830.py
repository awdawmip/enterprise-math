#!/usr/bin/env python3
"""Exact Gate-0 revision V2 regression and Result-manifest integrity check.

This checker deliberately does not construct A2/theta data.  It verifies:
(1) the exact algebra of the ambient scalar difference representation;
(2) the revised typing certificate, including downgrade of the numerical pair
    to representation-level status only;
(3) the complete dual-digest Result manifest for every non-Result output.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

TASK_ID = "RS-P000-THREE-AXIS-A2-HEXAGONAL-CUBIC-THETA-BRIDGE"
PUBLICATION_ID = "TP2-DABE69B97819A011CC8A"
RESULT_ID = "RR-1FE4541B394E2439AFE2"
EXECUTION_ID = "ER-E9A39D2DBC2C85E23FFB"

RETURN_PATH = "research_returns/P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_REVISION_V2_RETURN_20260830.md"
CHECKER_PATH = "research_checks/P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_REVISION_V2_CHECK_20260830.py"
ARTIFACT_PATH = "research_artifacts/P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_REVISION_V2/gate0_typing_certificate.json"
EXECUTION_PATH = "research_execution_records/RS-P000-THREE-AXIS-A2-HEXAGONAL-CUBIC-THETA-BRIDGE/ER-E9A39D2DBC2C85E23FFB.json"
RESULT_PATH = "research_result_records/RS-P000-THREE-AXIS-A2-HEXAGONAL-CUBIC-THETA-BRIDGE/RR-1FE4541B394E2439AFE2.json"

ROOT = Path(__file__).resolve().parents[1]


def difference_readout(triple):
    x, y, z = triple
    return (x - y, y - z, z - x)


def diagonal_translate(triple, t):
    return tuple(value + t for value in triple)


def a_pushforward(triple):
    x, y, z = triple
    return (z, x, y)


def git_blob_sha1(data):
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def load_json(path):
    with (ROOT / path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main():
    checks = 0

    # Exact ambient scalar algebra.  These are representation theorems only;
    # they do not assert that diagonal translation is a native P000 action.
    for triple in product(range(-3, 4), repeat=3):
        u, v, w = difference_readout(triple)
        assert u + v + w == 0
        checks += 1
        for t in range(-3, 4):
            assert difference_readout(diagonal_translate(triple, t)) == (u, v, w)
            checks += 1
        assert difference_readout(a_pushforward(triple)) == (w, u, v)
        checks += 1

    # Finite exhaustive guard for the exact fiber theorem.
    sample = list(product(range(-2, 3), repeat=3))
    for left in sample:
        for right in sample:
            if difference_readout(left) == difference_readout(right):
                delta = tuple(right[i] - left[i] for i in range(3))
                assert delta[0] == delta[1] == delta[2]
                checks += 1

    # The old numerical pair is deliberately checked only as an ambient
    # representation-level collision, never as a proved admissible PF-10 pair.
    left = (1, 1, 1)
    right = (2, 2, 2)
    assert difference_readout(left) == difference_readout(right) == (0, 0, 0)
    assert left != right
    checks += 2

    cert = load_json(ARTIFACT_PATH)
    assert cert["schema"] == "P000_A2_CUBIC_THETA_GATE0_REVISION_V2_TYPING_CERTIFICATE_V1"
    assert cert["task_id"] == TASK_ID
    assert cert["publication_id"] == PUBLICATION_ID
    assert cert["admissibility_audit"]["explicit_admissible_pf10_pair_constructed"] is False
    assert cert["admissibility_audit"]["arbitrary_ingress_reassignment_axiom_found"] is False
    assert cert["admissibility_audit"]["diagonal_shift_closure_theorem_found"] is False
    assert cert["representation_level_witness"]["status"] == "REPRESENTATION_LEVEL_ONLY"
    obligations = {item["id"]: item["status"] for item in cert["gate0_obligations"]}
    assert obligations == {
        "G0-TYPED-EQUIVALENCE": "NOT_DERIVED",
        "G0-ADMISSIBLE-CLOSURE": "NOT_DERIVED",
        "G0-RETAINED-FACTORISATION": "NOT_DERIVED",
        "G0-DIFFERENCE-ALGEBRA": "PROVED",
    }
    assert cert["terminal_conclusion"]["gate0"] == "COMMON_MODE_QUOTIENT_NOT_DERIVED"
    assert cert["terminal_conclusion"]["concrete_countermodel_claim"] is False
    assert cert["terminal_conclusion"]["gate1_open"] is False
    assert cert["terminal_conclusion"]["a2_theta_work_performed"] is False
    checks += 12

    execution = load_json(EXECUTION_PATH)
    assert execution["record_schema"] == "ENTERPRISE_MATH_RESEARCH_EXECUTION_RECORD_V1"
    assert execution["execution_record_id"] == EXECUTION_ID
    assert execution["task_id"] == TASK_ID
    assert execution["publication_id"] == PUBLICATION_ID
    checks += 4

    result = load_json(RESULT_PATH)
    assert result["record_schema"] == "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1"
    assert result["result_id"] == RESULT_ID
    assert result["execution_record_id"] == EXECUTION_ID
    assert result["task_id"] == TASK_ID
    assert result["publication_id"] == PUBLICATION_ID
    assert result["terminal_verdict"] == "SUCCESS"
    assert result["driver_review_required"] is True
    checks += 7

    expected_paths = {RETURN_PATH, CHECKER_PATH, ARTIFACT_PATH, EXECUTION_PATH}
    manifest = result["output_manifest"]
    assert len(manifest) == len(expected_paths)
    assert {entry["path"] for entry in manifest} == expected_paths
    checks += 2

    by_path = {entry["path"]: entry for entry in manifest}
    for path in sorted(expected_paths):
        data = (ROOT / path).read_bytes()
        assert by_path[path]["git_blob_sha1"] == "sha1:" + git_blob_sha1(data)
        assert by_path[path]["sha256"] == "sha256:" + sha256(data)
        checks += 2

    return_data = (ROOT / RETURN_PATH).read_bytes()
    assert result["return_path"] == RETURN_PATH
    assert result["return_blob_sha1"] == "sha1:" + git_blob_sha1(return_data)
    assert result["return_sha256"] == "sha256:" + sha256(return_data)
    checks += 3

    print("PASS P000_THREE_AXIS_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_REVISION_V2_CHECK")
    print(f"checks={checks}")
    print("p000_native_reality=6D_discrete_space_plus_1D_time")
    print("declared_slice=J_A:{E1,E2,E3}")
    print("difference_algebra=PROVED")
    print("numerical_pair_status=REPRESENTATION_LEVEL_ONLY")
    print("explicit_admissible_pf10_pair_constructed=false")
    print("gate0=COMMON_MODE_QUOTIENT_NOT_DERIVED")
    print("gate1_open=false")
    print("a2_theta_work_performed=false")
    print("result_manifest_complete=true")
    print("dual_digest_verification=PASS")


if __name__ == "__main__":
    main()
