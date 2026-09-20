"""Exact coverage/binding ledger for the six remaining primitive p19 blocks."""
import hashlib
import json
from pathlib import Path

import p19_order9 as arithmetic
import verify_coverage


def main():
    verify_coverage.main()
    root = Path(__file__).resolve().parent
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    input_hash = digest(root.joinpath("input.json"))
    core_hash = digest(root.joinpath("p19_order9.py"))
    ledger = []
    for a, b, na, nb in [(4, 6, 8124, 262), (5, 5, 8506, 8506),
                          (5, 6, 8506, 262), (6, 6, 262, 262)]:
        path = root.joinpath(f"block_{a}_{b}.json")
        data = json.loads(path.read_text())
        assert data["status"] == "EXACT_INTERVAL_CLEAR" and data["kernel"] is None
        assert data["split"] == [a, b] and data["state_counts"] == [na, nb]
        assert data["requested_rows"] == [0, na] == data["completed_rows"]
        assert data["input_sha256"] == input_hash and data["core_source_sha256"] == core_hash
        assert data["consumer_source_sha256"] == digest(root.joinpath("higher_orders.py"))
        expected = arithmetic.exact(na * (na - 1), 2) if a == b else na * nb
        assert data["oriented_pairs"] == expected
        assert data["primitive_cosets_checked"] + data["shared_atom_pairs"] == expected
        assert sum(data["rejection_depth_counts"]) == data["primitive_cosets_checked"]
        ledger.append({"split": [a, b], "path": path.name, "sha256": digest(path),
                       "primitive_instances": data["primitive_cosets_checked"]})
    path = root.joinpath("audit_3_6.json")
    data = json.loads(path.read_text())
    assert data["status"] == "OLD_BOUNDED_CLAIM_INDEPENDENTLY_ESTABLISHED" and data["kernel"] is None
    assert data["completed_rows"] == [0, 1482]
    assert data["input_sha256"] == input_hash and data["core_source_sha256"] == core_hash
    assert data["audit_source_sha256"] == digest(root.joinpath("audit_prior_3_6.py"))
    assert data["primitive_cosets_checked"] == 335374
    assert data["primitive_cosets_checked"] + data["shared_atom_pairs"] == 1482 * 262
    assert sum(data["rejection_depth_counts"]) == 335374
    ledger.append({"split": [3, 6], "path": path.name, "sha256": digest(path),
                   "primitive_instances": 335374})
    path = root.joinpath("coverage_4_5.json")
    data = json.loads(path.read_text())
    ledger.append({"split": [4, 5], "path": path.name, "sha256": digest(path),
                   "primitive_instances": data["primitive_cosets"]})
    total = sum(row["primitive_instances"] for row in ledger)
    assert total == 70285694
    result = {"schema": "T6_P19_ORDER9_12_COVERAGE_LEDGER_V1", "status": "COVERAGE_METADATA_PASS",
              "remaining_primitive_blocks": ledger, "total_primitive_instances": total,
              "all_recorded_kernels": None, "input_sha256": input_hash,
              "core_source_sha256": core_hash,
              "frozen_prior_input": "Task-authorized global p19 orders0..8, consumed without replay",
              "mathematical_conclusion_after_proof_and_execution_review": "Entire maximal-p19 layer excluded below side mass2332",
              "next_research_unit": "p17 vertical order1; p17 q0 independently checked by verify_p17_q0.py",
              "strength": "Researcher proof and exact computation; no Driver or Foundation acceptance",
              "count_semantics": "Pattern-indexed affine-coset instances, not asserted distinct quotient classes"}
    root.joinpath("coverage_p19.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
