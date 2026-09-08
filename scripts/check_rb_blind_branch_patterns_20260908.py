"""Blind, integer-only finite branch-assignment certificate.

This enumerates combinatorial candidates, not elliptic maps or ODE solutions.
No rational, quotient, remainder, root, or legacy mathematics evaluator is used.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_REL = "research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908"
SOURCE_BINDING_SHA256 = "516400d46ae5dd5a8aa2d25520021ee3a57dc839538746a550ad2a7bfae2a473"
BRANCH_LABELS = ("O", "T0", "Tplus", "Tminus", "Pplus", "Pminus")
TARGET_LABELS = ("0", "1", "lambda", "infinity")
IDENTITY = tuple(range(6))
FLIP = (0, 1, 2, 3, 5, 4)
V4 = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))
S4 = tuple(itertools.permutations(range(4)))


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def perfect_matchings(points: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], ...]:
    if not points:
        return ((),)
    first = points[0]
    result = []
    for partner in points[1:]:
        remaining = tuple(x for x in points if x != first and x != partner)
        for tail in perfect_matchings(remaining):
            result.append(((first, partner),) + tail)
    return tuple(result)


def assignments(pattern: str) -> set[tuple[int, ...]]:
    result = set()
    if pattern == "4+2+0+0":
        for pair in itertools.combinations(range(6), 2):
            for four_label, pair_label in itertools.permutations(range(4), 2):
                result.add(tuple(pair_label if x in pair else four_label for x in range(6)))
    elif pattern == "2+2+2+0":
        for matching in perfect_matchings(tuple(range(6))):
            for labels in itertools.permutations(range(4), 3):
                row = [-1] * 6
                for pair, label in zip(matching, labels):
                    for point in pair:
                        row[point] = label
                result.add(tuple(row))
    else:
        raise ValueError("unknown branch pattern")
    return result


def orbit_partition(rows: set[tuple[int, ...]], targets: tuple[tuple[int, ...], ...],
                    sources: tuple[tuple[int, ...], ...]) -> list[dict]:
    unseen = set(rows)
    result = []
    while unseen:
        representative = min(unseen)
        members = {tuple(target[representative[source[i]]] for i in range(6))
                   for target in targets for source in sources}
        if not members <= unseen:
            raise AssertionError("action is not a disjoint, closed group partition")
        unseen.difference_update(members)
        result.append({"representative": representative, "orbit_size": len(members),
                       "members_sha256": hashlib.sha256(canonical_bytes(sorted(members))).hexdigest()})
    if sum(row["orbit_size"] for row in result) != len(rows):
        raise AssertionError("orbit coverage failed")
    return result


def build_certificate(root: Path) -> dict:
    source_bytes = root.joinpath(ARTIFACT_REL, "source_binding.json").read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != SOURCE_BINDING_SHA256:
        raise ValueError("source binding changed")
    patterns = {}
    for pattern, raw_count, fixed_count, cover_count, unlabelled_count, coarse_count in (
        ("4+2+0+0", 180, 45, 33, 15, 11),
        ("2+2+2+0", 360, 90, 54, 15, 9),
    ):
        rows = assignments(pattern)
        independent_rows = {row for row in itertools.product(range(4), repeat=6)
                            if sorted(row.count(i) for i in range(4)) ==
                            ([0, 0, 2, 4] if pattern == "4+2+0+0" else [0, 2, 2, 2])}
        if rows != independent_rows or len(rows) != raw_count:
            raise AssertionError("independent assignment completeness failed")
        partitions = {
            "fixed_lambda_fixed_k_V4": orbit_partition(rows, V4, (IDENTITY,)),
            "cover_only_V4_and_source_flip": orbit_partition(rows, V4, (IDENTITY, FLIP)),
            "label_transport_S4": orbit_partition(rows, S4, (IDENTITY,)),
            "cover_only_S4_and_source_flip": orbit_partition(rows, S4, (IDENTITY, FLIP)),
        }
        expected = (fixed_count, cover_count, unlabelled_count, coarse_count)
        if tuple(len(value) for value in partitions.values()) != expected:
            raise AssertionError("orbit count mismatch")
        patterns[pattern] = {"raw_assignments": raw_count,
                             "raw_assignments_sha256": hashlib.sha256(canonical_bytes(sorted(rows))).hexdigest(),
                             "partitions": partitions}
    return {"schema": "RB_BLIND_BRANCH_ASSIGNMENT_CERTIFICATE_V1",
            "phase": "BLIND_FORWARD_PROGRESS_NOT_FINAL_RAW_FREEZE",
            "branch_labels": BRANCH_LABELS, "target_labels": TARGET_LABELS,
            "source_binding_sha256": SOURCE_BINDING_SHA256,
            "arithmetic": {"integer_enumeration_only": True, "division_evaluations": 0,
                           "root_evaluations": 0, "brc_calls": 0},
            "scope": "Assignment coverage only; no RR, square-class, ODE, map, period or terminal theorem verdict.",
            "symmetry_limit": "Source flip is cover-only: fixed k ODE retains both partners. S4 transports lambda labels; fixed lambda uses only V4. No semilinear quotient is taken.",
            "patterns": patterns}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    result = build_certificate(args.root)
    output = args.root.joinpath(ARTIFACT_REL, "branch_assignment_classification.json")
    data = canonical_bytes(result)
    if args.write:
        output.write_bytes(data)
    elif output.read_bytes() != data:
        raise SystemExit("BLIND_BRANCH_ASSIGNMENTS: FAIL (certificate bytes differ)")
    counts = {pattern: {"raw": row["raw_assignments"], **{
        name: len(partition) for name, partition in row["partitions"].items()}}
        for pattern, row in result["patterns"].items()}
    print(json.dumps({"status": "PASS", "counts": counts,
                      "certificate_sha256": hashlib.sha256(data).hexdigest()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
