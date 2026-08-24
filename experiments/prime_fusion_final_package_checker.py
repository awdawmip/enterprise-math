#!/usr/bin/env python3
"""Thin final composition checker for the frozen Prime Fusion T1–T15 package.

This file deliberately contains no theorem-checking implementation. It:
  1. materializes the four already-frozen component checker blobs from Git;
  2. verifies each blob identity before execution;
  3. executes each checker in an isolated temporary directory;
  4. checks final package metadata/evidence typing/T10 scope guards and manifest digests.

Running this script is a reproducibility audit. Finite checker success is not a
substitute for the frozen written proofs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys
import tempfile


@dataclass(frozen=True)
class Component:
    name: str
    path: str
    blob_sha: str
    review_ref: str


COMPONENTS = (
    Component(
        "source-package",
        "experiments/prime_fusion_theorem_package_checker.py",
        "07db705c1227d86df0fa021e56eb07eaddeee3c5",
        "research/prime-fusion-theorem-package-clean@e5138e17f8c4009f5e357f43326f2812c9df1359",
    ),
    Component(
        "blind-core",
        "experiments/prime_fusion_independent_replication_checker.py",
        "fc67f08f146782728b00472ee0156c64bdf7747e",
        "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    ),
    Component(
        "phase-extension",
        "experiments/prime_fusion_phase_extension_targeted_verification_checker.py",
        "f2570534c99a92e75ca55b9ba24286854bc48fff",
        "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
    ),
    Component(
        "t4-t7-t8-final-exact-closure",
        "experiments/prime_fusion_t4_t7_t8_final_exact_closure_checker.py",
        "c2319bf4092e41cc21d70ee6eb407480de0450ed",
        "driver_reviews/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_DRIVER_REVIEW_20260824.md@ed016687bcd2d75957041ce820e335678aeb1f53",
    ),
)

EXPECTED_STATUSES = {
    "T1": "INDEPENDENT_EXACT",
    "T2": "INDEPENDENT_EXACT",
    "T3": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T4": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T5": "INDEPENDENT_EQUIVALENT_EXACT",
    "T6": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T7": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T8": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T9": "INDEPENDENT_EXACT",
    "T10": "INDEPENDENT_EXACT_AFTER_SCOPE_REPAIR",
    "T11": "INDEPENDENT_EXACT_STATEMENT_EXPOSED",
    "T12": "INDEPENDENT_EXACT",
    "T13": "INDEPENDENT_EXACT",
    "T14": "INDEPENDENT_EXACT",
    "T15": "INDEPENDENT_EXACT_STRONGER_FORM",
}

PACKAGE = Path("research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md")
MATRIX = Path("research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv")
GRAPH = Path("research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md")
MANIFEST = Path("research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json")


def repo_root() -> Path:
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return Path(proc.stdout.strip())


def git_blob_hash(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def materialize_blob(root: Path, component: Component, destination: Path) -> None:
    proc = subprocess.run(
        ["git", "cat-file", "blob", component.blob_sha],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"{component.name}: frozen blob {component.blob_sha} is not present locally. "
            f"Fetch the referenced research/review history before running the composed audit."
        )
    data = proc.stdout
    actual = git_blob_hash(data)
    if actual != component.blob_sha:
        raise AssertionError(
            f"{component.name}: blob identity mismatch: expected {component.blob_sha}, got {actual}"
        )
    destination.write_bytes(data)


def run_component(root: Path, component: Component) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="prime-fusion-final-") as td:
        tmp = Path(td)
        script = tmp / Path(component.path).name
        materialize_blob(root, component, script)
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=tmp,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=600,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                f"{component.name} failed with exit code {proc.returncode}\n"
                f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
            )
        return {
            "name": component.name,
            "blob_sha": component.blob_sha,
            "review_ref": component.review_ref,
            "returncode": proc.returncode,
            "stdout_tail": proc.stdout[-2000:],
        }


def audit_final_artifacts(root: Path) -> dict[str, object]:
    package = (root / PACKAGE).read_text(encoding="utf-8")
    graph = (root / GRAPH).read_text(encoding="utf-8")
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))

    required_package_guards = (
        "T10_SCOPE = CHANNEL_ORIENTED_MIXED_LOCUS_M_PQ",
        "T10_FULL_FUSED_ROOT_SET_CLAIM = false",
        "T10_PRESSURE_WITNESS_H = 91",
        "M_{p,q}",
        "{18,44,60,86}",
        "{9,16,18,44,60,74,81,86}",
        "INDEPENDENT_AUDIT_COVERAGE = 15/15",
        "PRIME_FUSION_ALL_15_BLINDLY_REPLICATED = false",
    )
    for guard in required_package_guards:
        if guard not in package:
            raise AssertionError(f"package guard missing: {guard}")

    if "FALSE_CHAIN_REJECTED = T3 -> T6 -> T10 -> T11" not in graph:
        raise AssertionError("dependency graph did not reject the false linear chain")
    if "T10_FULL_FUSED_ROOT_SET_CLAIM = false" not in graph:
        raise AssertionError("dependency graph lost the T10 universe guard")

    with (root / MATRIX).open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 15:
        raise AssertionError(f"evidence matrix has {len(rows)} rows, expected 15")
    actual = {row["theorem"]: row["final_independent_evidence_status"] for row in rows}
    if actual != EXPECTED_STATUSES:
        raise AssertionError(f"evidence matrix mismatch: {actual!r}")
    raw_matrix = (root / MATRIX).read_text(encoding="utf-8")
    if "PARTIAL" in raw_matrix or "MISSED" in raw_matrix:
        raise AssertionError("obsolete PARTIAL/MISSED label remains in final evidence matrix")

    if manifest.get("final_classification") != "PRIME_FUSION_FINAL_PACKAGE_FROZEN":
        raise AssertionError("manifest final classification mismatch")
    if manifest.get("theorem_row_count") != 15:
        raise AssertionError("manifest theorem_row_count mismatch")
    if manifest.get("all_15_blindly_replicated") is not False:
        raise AssertionError("manifest incorrectly homogenizes evidence as 15/15 blind")

    expected_digests = manifest["artifact_git_blob_sha1"]
    for relative in (PACKAGE, MATRIX, GRAPH, Path("experiments/prime_fusion_final_package_checker.py")):
        key = relative.as_posix()
        actual_digest = git_blob_hash((root / relative).read_bytes())
        if expected_digests.get(key) != actual_digest:
            raise AssertionError(
                f"manifest digest mismatch for {key}: "
                f"{expected_digests.get(key)} != {actual_digest}"
            )

    return {
        "theorem_rows": len(rows),
        "evidence_rows_exact": True,
        "t10_scope_guard": True,
        "t10_pressure_witness_h": 91,
        "false_linear_chain_rejected": True,
        "manifest_digests": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="check final package/matrix/graph/manifest without executing component checkers",
    )
    args = parser.parse_args()

    root = repo_root()
    artifact_audit = audit_final_artifacts(root)
    component_results = []
    if not args.metadata_only:
        for component in COMPONENTS:
            component_results.append(run_component(root, component))

    print("PRIME_FUSION_FINAL_PACKAGE_CHECKER: PASS")
    print(json.dumps(
        {
            "artifact_audit": artifact_audit,
            "component_checkers_executed": not args.metadata_only,
            "component_results": component_results,
        },
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()
