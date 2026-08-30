#!/usr/bin/env python3
"""Exact regression checker for RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

TASK_ID = "RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS"
PUBLICATION_ID = "TP2-0A8F9C3170B9CBABDBC9"
CLAIM_ID = "chatgpt-p000cmf1-20260830-1742-sol"
RESEARCHER_ID = "EM-P000CMF1-3C9565"
EXECUTION_RECORD_ID = "ER-881EFB1D2A33C79E25E5"
TABLE_REL = "research_output/RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS/common_mode_forgetful_semantics_classification_v1.json"
RETURN_REL = "research_returns/P000_THREE_AXIS_COMMON_MODE_FORGETFUL_SEMANTICS_CLASSIFICATION_RETURN_20260830.md"
CHECKER_REL = "research_checks/RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS/check_common_mode_forgetful_semantics.py"
EXEC_REL = "research_execution_records/RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS/ER-881EFB1D2A33C79E25E5.json"
RESULT_DIR_REL = "research_result_records/RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS"


def q(p: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = p
    return (x - y, y - z, z - x)


def shift(p: tuple[int, int, int], t: int) -> tuple[int, int, int]:
    x, y, z = p
    return (x + t, y + t, z + t)


def cycle(p: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = p
    return (z, x, y)


def rho(d: tuple[int, int, int]) -> tuple[int, int, int]:
    u, v, w = d
    return (w, u, v)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_sha1(value: str) -> str:
    return value.lower().removeprefix("sha1:")


def check_exact_algebra() -> None:
    vals = range(-3, 4)
    triples = [(x, y, z) for x in vals for y in vals for z in vals]

    for p in triples:
        d = q(p)
        assert sum(d) == 0
        assert q(cycle(p)) == rho(d)
        for t in vals:
            assert q(shift(p, t)) == d

    # Finite exact regression for the fiber theorem.
    for p in triples:
        for p2 in triples:
            same_q = q(p) == q(p2)
            dx = p2[0] - p[0]
            diagonal = (p2[1] - p[1] == dx and p2[2] - p[2] == dx)
            assert same_q == diagonal

    # Surjectivity regression on a finite window of D, using the exact section
    # s(u,v,w)=(u+v,v,0), valid whenever u+v+w=0.
    for u in vals:
        for v in vals:
            w = -u - v
            p = (u + v, v, 0)
            assert q(p) == (u, v, w)

    assert q((1, 1, 1)) == q((2, 2, 2)) == (0, 0, 0)


def check_classification(root: Path) -> None:
    table = json.loads((root / TABLE_REL).read_text(encoding="utf-8"))
    assert table["task_id"] == TASK_ID
    assert table["publication_id"] == PUBLICATION_ID
    assert table["claim_id"] == CLAIM_ID
    assert table["researcher_id"] == RESEARCHER_ID
    assert table["inventory_scope"]["additional_declared_weaker_three_axis_observable_families_found"] is False

    rows = {row["candidate"]: row for row in table["classification"]}
    assert set(rows) == {"J_A_DECLARED_FRAMED_PF10_SLICE", "Q_DIFFERENCE_READOUT"}
    assert rows["J_A_DECLARED_FRAMED_PF10_SLICE"]["g0_typed_equivalence"] == "NOT_DERIVED"
    assert rows["J_A_DECLARED_FRAMED_PF10_SLICE"]["g0_admissible_closure"] == "NOT_DERIVED"
    assert rows["J_A_DECLARED_FRAMED_PF10_SLICE"]["g0_retained_factorisation"] == "NOT_DERIVED"
    assert rows["J_A_DECLARED_FRAMED_PF10_SLICE"]["passes_all_three_g0_obligations"] is False

    qrow = rows["Q_DIFFERENCE_READOUT"]
    assert qrow["native_common_mode_descent"] == "YES_AT_AMBIENT_REPRESENTATION_LEVEL_ONLY"
    assert qrow["passes_all_three_g0_obligations"] is False
    assert table["terminal_classification"]["verdict"] == "EXACT_CURRENT_NO_MATCH"
    assert table["terminal_classification"]["observable_level_survivor_found"] is False
    assert table["terminal_classification"]["algebraic_only_survivor_found"] is True


def check_result_chain_if_present(root: Path) -> None:
    exec_path = root / EXEC_REL
    if not exec_path.exists():
        return
    execution = json.loads(exec_path.read_text(encoding="utf-8"))
    assert execution["execution_record_id"] == EXECUTION_RECORD_ID
    assert execution["task_id"] == TASK_ID
    assert execution["publication_id"] == PUBLICATION_ID
    assert execution["claim_id"] == CLAIM_ID
    assert execution["researcher_id"] == RESEARCHER_ID

    result_dir = root / RESULT_DIR_REL
    if not result_dir.exists():
        return
    matches = []
    for path in result_dir.glob("*.json"):
        value = json.loads(path.read_text(encoding="utf-8"))
        if value.get("claim_id") == CLAIM_ID:
            matches.append((path, value))
    if not matches:
        return
    assert len(matches) == 1
    _, result = matches[0]
    assert result["execution_record_id"] == EXECUTION_RECORD_ID
    assert result["terminal_verdict"] == "SUCCESS"
    manifest = {row["path"]: row for row in result["output_manifest"]}
    expected = {RETURN_REL, TABLE_REL, CHECKER_REL, EXEC_REL}
    assert set(manifest) == expected
    for rel in expected:
        path = root / rel
        assert path.exists()
        assert normalize_sha1(manifest[rel]["git_blob_sha1"]) == normalize_sha1(git_blob_sha1(path))
        assert manifest[rel]["sha256"] == sha256(path)
    assert normalize_sha1(result["return_blob_sha1"]) == normalize_sha1(git_blob_sha1(root / RETURN_REL))
    assert result["return_sha256"] == sha256(root / RETURN_REL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    check_exact_algebra()
    check_classification(root)
    check_result_chain_if_present(root)
    print("PASS: exact algebra, finite classification, and available result-chain pins are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
