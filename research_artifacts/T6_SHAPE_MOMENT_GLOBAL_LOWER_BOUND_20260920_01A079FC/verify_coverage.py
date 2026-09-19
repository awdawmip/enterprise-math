"""Bind interval metadata; independent mathematical validation replays the runs."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    input_sha = digest(root.joinpath("input.json"))
    source_sha = digest(root.joinpath("p19_order9.py"))
    ranges = [(0, 25), (25, 2025), (2025, 8124)]
    files = ["run_0000_0025.json", "run_0025_2025.json", "run_2025_8124.json"]
    primitive = cancelled = 0
    ledger = []
    for name, interval in zip(files, ranges):
        path = root.joinpath(name)
        data = json.loads(path.read_text())
        assert data["status"] == "EXACT_INTERVAL_CLEAR" and data["kernel"] is None
        assert data["requested_rows"] == list(interval) == data["completed_rows"]
        assert data["state_counts"] == [8124, 8506]
        assert data["input_sha256"] == input_sha and data["source_sha256"] == source_sha
        assert sum(data["rejection_depth_counts"]) == data["primitive_cosets_checked"]
        assert data["primitive_cosets_checked"] + data["cancelled_pairs"] == (interval[1] - interval[0]) * 8506
        primitive += data["primitive_cosets_checked"]
        cancelled += data["cancelled_pairs"]
        ledger.append({"path": name, "sha256": digest(path), "rows": list(interval),
                       "primitive_cosets": data["primitive_cosets_checked"]})
    assert primitive + cancelled == 8124 * 8506
    output = {"schema": "T6_P19_ORDER9_45_COMPLETE_COVERAGE_V1",
              "status": "COVERAGE_METADATA_PASS", "split": [4, 5],
              "rows_covered": [0, 8124], "state_pairs": 8124 * 8506,
              "primitive_cosets": primitive, "shared_atom_pairs": cancelled,
              "input_sha256": input_sha, "core_source_sha256": source_sha,
              "intervals": ledger,
              "scope": "Complete primitive (4,5) coverage only; (3,6) review gap and global T6 remain",
              "independent_mathematical_execution_check": "Replay p19_order9.py for the three named intervals"}
    (root.joinpath("coverage_4_5.json")).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(output))


if __name__ == "__main__":
    main()
