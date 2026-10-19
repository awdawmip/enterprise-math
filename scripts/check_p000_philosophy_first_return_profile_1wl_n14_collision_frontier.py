#!/usr/bin/env python3
"""Q30 n=14 durable recovery audit.

This checker verifies the persisted recovery certificate's exact arithmetic and
provenance invariants. It is not a replacement for the pinned graph-level
enumeration/replay at source commit b90378c3....
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

TASK_ID = "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER"
PUBLICATION_ID = "TP2-8969646E7FF5FB8A9F5D"
OBSERVABLE = "FROZEN_Q22_Q25_Q27_Q28_Q29_PRIMITIVE_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_UNCHANGED"
TERMINAL = "RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N14"
SOURCE_COMMIT = "b90378c332e0dbf80aad0c09d363047abb2ee2f3"
CERT_BLOB = "9ed536a327dda4d9d6e3a21d31bb90383bf7ddc9"
EXPECTED_R = [2, 4, 6, 8, 10, 12, 14]
EXPECTED_TOTALS = {
    "kernel_types": 1267,
    "representatives": 56972,
    "normalized_connected": 26406647416800,
    "stable_packets": 56972,
    "collision_fibers": 0,
}
DEFAULT_AUDIT = Path(
    "research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/"
    "P000_Q30_N14_RECOVERY_AUDIT_20260907.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("audit", nargs="?", type=Path, default=DEFAULT_AUDIT)
    args = ap.parse_args()

    data = json.loads(args.audit.read_text(encoding="utf-8"))
    require(data["schema"] == "P000_Q30_N14_RECOVERY_AUDIT_V1", "schema")
    require(data["task_id"] == TASK_ID, "task_id")
    require(data["publication_id"] == PUBLICATION_ID, "publication_id")
    require(data["n"] == 14, "n")
    require(data["observable"] == OBSERVABLE, "observable changed")
    require(data["terminal_state"] == TERMINAL, "terminal_state")
    require(data["source_pin"]["commit"] == SOURCE_COMMIT, "source commit")
    require(data["source_pin"]["certificate_git_blob_sha1"] == CERT_BLOB, "certificate blob")
    require("Exact packet equality" in data["method_contract"]["identity_policy"], "exact packet identity policy")
    require("hashes are integrity pins only" in data["method_contract"]["identity_policy"], "hash policy")

    sectors = data["sectors"]
    require(sorted(map(int, sectors)) == EXPECTED_R, "sector set")
    for r in EXPECTED_R:
        sec = sectors[str(r)]
        hist = {int(a): int(c) for a, c in sec["expected_aut_hist"].items()}
        reps = int(sec["expected_representatives"])
        packets = int(sec["expected_stable_packets"])
        require(sum(hist.values()) == reps, f"r={r}: automorphism histogram count")
        require(reps == packets, f"r={r}: representative/packet count")
        orbit_sum = sum(
            count * math.factorial(r) * math.factorial(14 - r) // aut
            for aut, count in hist.items()
        )
        require(orbit_sum == int(sec["expected_normalized_connected"]), f"r={r}: orbit sum {orbit_sum}")

    totals = data["totals"]
    for key, value in EXPECTED_TOTALS.items():
        require(int(totals[key]) == value, f"total {key}")
    require(sum(int(sectors[str(r)]["expected_representatives"]) for r in EXPECTED_R) == EXPECTED_TOTALS["representatives"], "summed representatives")
    require(sum(int(sectors[str(r)]["expected_normalized_connected"]) for r in EXPECTED_R) == EXPECTED_TOTALS["normalized_connected"], "summed normalized connected")
    require(sum(int(sectors[str(r)]["kernel_type_count"]) for r in EXPECTED_R) == EXPECTED_TOTALS["kernel_types"], "summed kernel types")

    repair = data["r14_reference_repair"]
    require(repair["legacy_reference"] == "P000_Q30_N14_KERNELS_R14_V1.json", "legacy r14 pointer")
    require(repair["legacy_status"] == "SUPERSEDED", "legacy r14 status")
    require(len(repair["replacement_shards"]) == 5, "r14 replacement shard count")
    require(sum(int(x["count"]) for x in repair["replacement_shards"]) == 509, "r14 replacement representatives")
    supplement = repair["replacement_supplement"]
    require(int(supplement["representatives"]) == 509, "r14 supplement representatives")
    require(int(supplement["stable_packets"]) == 509, "r14 supplement packets")
    require(int(supplement["collision_fibers"]) == 0, "r14 supplement collisions")
    require(int(supplement["orbit_sum"]) == 19491385914000, "r14 orbit sum")
    require(int(supplement["independent_connected_labeled_cubic_count"]) == 19491385914000, "r14 independent count")
    require(data["audit_status"] == "PASS", "audit status")

    print(
        "PASS Q30 n=14 recovery audit: "
        "representatives=56972 normalized_connected=26406647416800 "
        "stable_packets=56972 collision=0; legacy_r14_pointer=SUPERSEDED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
