#!/usr/bin/env python3
"""Re-run the six *original* R063 Stage0 files and attest their exact outputs.

This is an orchestration/acceptance wrapper, not a substitute checker. It reads
an existing authorized checkout of the frozen original branch, checks the Git
blob identities, invokes the unchanged loader, and validates its resulting
artifacts. No source mutation, Git network calls, or Actions are performed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

SOURCES = {
    "scripts/r063_stage0_validate_path_valued_sqrt_2500.py": "b4e000a6377f2858ae434eb0eecd0c25c33e8592",
    "scripts/r063_stage0_checker_parts/part00.inc": "4a69c4d698887bce56323f393cb979609ce4ab0a",
    "scripts/r063_stage0_checker_parts/part01.inc": "913078c642b8995bfc135ef0350912387a17cdb8",
    "scripts/r063_stage0_checker_parts/part02.inc": "b543e185ec415b512c0ca0421616404cc12a19a7",
    "scripts/r063_stage0_checker_parts/part03.inc": "4f1bbf72abed19dc7dc605371872ee31c501cebe",
    "scripts/r063_stage0_checker_parts/part04.inc": "a1834a4b39a9d528760e67220b5fe5f368c9e655",
}
EXPECTED_DISCOVERY_SHA = "6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d"
EXPECTED_ROWS_SHA = "51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae"
EXPECTED_SECTOR_BRC = 110695538274255714208
EXPECTED_GATES = {
    "INPUT_ONLY_DISCOVERY_NO_BRANCH_HARDCODE",
    "SCALAR_SQRT_2500_EXACT", "SECTOR_NORM_ALGEBRA_TYPED",
    "C2_UNSCALED_SQUARE_LIFT_CLASSIFIED",
    "C3_SCALED_SQUARE_LIFT_CLASSIFIED",
    "C4_GAUSSIAN_FACTOR_ROUTE_CLASSIFIED",
    "DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY",
    "NO_EXTRA_COMPONENT_ROOTS",
    "ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED",
    "PATHIFICATION_FORMULA_EXACT",
    "HUGE_PATH_FIBER_COMPRESSED_REPRESENTATION_EXACT",
    "ONE_SECTOR_TOTAL_PATH_CARDINALITY_EXACT",
    "R061_TRACE_IDENTITY_COMPATIBILITY_PASS",
    "GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED",
    "NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE",
    "NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY",
    "COMMITTED_DETERMINISTIC_CHECKER_PASS",
}
REQUIRED_OUTPUTS = [
    "R063_STAGE0_DISCOVERY_PHASE_FROZEN.json",
    "R063_STAGE0_SQRT2500_DISCOVERY_TREE.json",
    "R063_STAGE0_COMPONENT_ROOT_FIBER.json",
    "R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json",
    "R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json",
    "R063_STAGE0_GENERAL_SQUARE_REGRESSION.json",
    "R063_STAGE0_MISMATCHES.json",
    "R063_STAGE0_REPLAY_SUMMARY.json",
    "R063_STAGE0_PATH_ROOT_OPERATOR_CANDIDATE_MATRIX.md",
    "R063_STAGE0_SCALED_SQUARE_LIFT_THEOREM.md",
    "R063_STAGE0_GAUSSIAN_FACTOR_ROUTE_AUDIT.md",
    "R063_STAGE0_PATH_VALUED_SQRT_FORMULA.md",
    "R063_STAGE0_REPRODUCIBILITY_PROOF.md",
]


def file_sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_sha256(obj: object) -> str:
    return file_sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def check_sources(repo: Path) -> dict[str, dict[str, object]]:
    result = {}
    part_dir = repo / "scripts/r063_stage0_checker_parts"
    actual_part_names = sorted(p.name for p in part_dir.glob("part*.inc")) if part_dir.is_dir() else []
    if not (actual_part_names == [f"part{i:02}.inc" for i in range(5)]):
        raise AssertionError(("The original glob would load a different code set", actual_part_names))
    for name, expected in SOURCES.items():
        data = (repo / name).read_bytes()
        got = git_blob_sha1(data)
        if not (got == expected):
            raise AssertionError(f"FROZEN_SOURCE_BLOB_MISMATCH {name}: {got} != {expected}")
        result[name] = {"blob_sha1": got, "sha256": file_sha256(data), "bytes": len(data)}
    return result


def audit_outputs(out: Path, sources: dict[str, dict[str, object]]) -> dict[str, object]:
    outputs = {}
    for name in REQUIRED_OUTPUTS:
        body = (out / name).read_bytes()
        if not (body):
            raise AssertionError(f"EMPTY_OUTPUT {name}")
        outputs[name] = {"sha256": file_sha256(body), "bytes": len(body)}
    def j(name: str) -> dict:
        return json.loads((out / name).read_text(encoding="utf-8"))

    discovery = j("R063_STAGE0_DISCOVERY_PHASE_FROZEN.json")
    discovery_sha = discovery["discovery_snapshot_sha256"]
    # The original SHA covers the serialized discovery object *before* its
    # self-referential hash field is inserted.
    unsigned_discovery = dict(discovery)
    unsigned_discovery.pop("discovery_snapshot_sha256")
    if not (canonical_sha256(unsigned_discovery) == discovery_sha == EXPECTED_DISCOVERY_SHA):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_03")
    if not (discovery["input"]["N"] == 2500):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_04")

    regression = j("R063_STAGE0_GENERAL_SQUARE_REGRESSION.json")
    if not (regression["r_range"] == [1, 512]):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_05")
    if not (regression["tested_r_count"] == 512):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_06")
    if not (regression["combined_checker_mismatch_count"] == 0):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_07")
    if not (regression["C3_mismatch_count"] == regression["C4_mismatch_count"] == 0):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_08")
    if not (regression["rows_sha256"] == EXPECTED_ROWS_SHA):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_09")
    if not (regression["C2_failure_count"] == 484):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_10")

    summary = j("R063_STAGE0_REPLAY_SUMMARY.json")
    gates = summary["acceptance_gates"]
    if not (set(gates) == EXPECTED_GATES):
        raise AssertionError(f"GATE_SET_MISMATCH {set(gates) ^ EXPECTED_GATES}")
    if not (len(gates) == 17 and all(v is True for v in gates.values())):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_12")
    if not (summary["N"] == 2500 and summary["r"] == 50):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_13")
    if not (summary["discovery_snapshot_sha256"] == discovery_sha):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_14")
    if not (summary["ordered_nonnegative_component_root_count"] == 6):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_15")
    if not (summary["one_sector_total_path_cardinality"] == EXPECTED_SECTOR_BRC):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_16")
    if not (summary["general_regression"]["r_range"] == [1, 512]):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_17")
    if not (summary["general_regression"]["rows_sha256"] == EXPECTED_ROWS_SHA):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_18")
    if not (summary["general_regression"]["combined_checker_mismatch_count"] == 0):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_19")
    core = dict(summary)
    core.pop("summary_core_sha256")
    if not (canonical_sha256(core) == summary["summary_core_sha256"]):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_20")

    mismatch = j("R063_STAGE0_MISMATCHES.json")
    if not (mismatch["mismatch_count"] == 0):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_21")
    fiber = j("R063_STAGE0_COMPONENT_ROOT_FIBER.json")
    if not (fiber["root_count"] == 6 and fiber["C3_exact"] is True and fiber["C4_exact"] is True):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_22")
    pathcert = j("R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json")
    if not (pathcert["one_sector_total_path_cardinality"] == EXPECTED_SECTOR_BRC):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_23")
    if not (sum(int(x["cardinality"]) for x in pathcert["branches"]) == EXPECTED_SECTOR_BRC):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_24")
    graph = j("R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json")
    if not (graph["node_id_uniqueness"] is True):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_25")
    return {
        "schema": "X6_R063_EXACT_ORIGINAL_STAGE0_REPLAY_ATTESTATION_V1",
        "status": "ORIGINAL_SAME_OBJECT_REPLAY_VERIFIED",
        "frozen_original_blob_sources": sources,
        "inputs": {"N": 2500, "regression_r_range": [1, 512]},
        "discovery_sha256": discovery_sha,
        "original_512_rows_sha256": regression["rows_sha256"],
        "acceptance_gate_count": len(gates),
        "acceptance_gates": gates,
        "outputs": outputs,
        "native_scope": "R063_FROZEN_TWO_GENERATOR_SECTOR_NOT_FULL_SIGNED_X6",
        "review": "AUTHOR_SIDE_EXECUTION_ATTESTATION_NOT_INDEPENDENT_DRIVER_ADMISSION",
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True, help="Authorized original repository checkout")
    p.add_argument("--evidence-dir", type=Path, required=True, help="Must not already exist")
    args = p.parse_args()
    repo = args.repo.resolve()
    dest = args.evidence_dir.resolve()
    # An explicitly new empty directory avoids ever overwriting frozen results.
    if dest.exists():
        raise SystemExit(f"Refusing existing evidence directory: {dest}")
    sources = check_sources(repo)
    dest.mkdir(parents=True)
    original_out = dest / "original_output"
    loader = repo / "scripts/r063_stage0_validate_path_valued_sqrt_2500.py"
    cmd = [sys.executable, str(loader), "--N", "2500", "--regression-max-r", "512", "--out", str(original_out)]
    process = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, check=False)
    (dest / "original_stdout.txt").write_text(process.stdout, encoding="utf-8")
    (dest / "original_stderr.txt").write_text(process.stderr, encoding="utf-8")
    if not (process.returncode == 0):
        raise AssertionError(f"ORIGINAL_EXIT_NONZERO {process.returncode}")
    if not (json.loads(process.stdout.strip().splitlines()[-1])["status"] == "PASS"):
        raise AssertionError("R063_REPLAY_CHECK_FAILED_27")
    result = audit_outputs(original_out, sources)
    result["original_process_exit_code"] = process.returncode
    result["original_command"] = ["python3", *cmd[1:]]
    result["original_loader_preserved"] = True
    (dest / "replay_attestation.json").write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS_ORIGINAL_R063_SAME_OBJECT_17_GATES_512", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
