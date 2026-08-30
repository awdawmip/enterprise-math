#!/usr/bin/env python3
"""Exact finite/regression checks for P000 Axis-Channel Frame Prior-Art Audit V7."""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7"
CLAIM_MAP = ART / "claim_map.json"
SOURCE_LEDGER = ART / "source_ledger.json"

ALLOWED = {
    "EXACT_DUPLICATE",
    "PARTIAL_ANTECEDENT",
    "ADJACENT_METHOD",
    "NO_MATERIAL_MATCH",
}
EXPECTED = {
    "C01_AUTOMORPHISM_DEFINABILITY_OBSTRUCTION": "EXACT_DUPLICATE",
    "C02_S6_BASE_SIZE_FIVE_ANCHOR_LOWER_BOUND": "EXACT_DUPLICATE",
    "C03_FRAME_AS_S6_TORSOR_TRIVIALIZATION": "EXACT_DUPLICATE",
    "C04_FRAME_FIELD_VS_SEED_PLUS_EDGE_TRANSPORT": "EXACT_DUPLICATE",
    "C05_GRAPH_CONNECTION_PARALLEL_TRANSPORT_HOLONOMY": "EXACT_DUPLICATE",
    "C06_GAUGE_CHANGE_AND_HOLONOMY_CONJUGACY": "EXACT_DUPLICATE",
    "C07_FLATNESS_VS_GLOBAL_FRAME_TERMINOLOGY": "EXACT_DUPLICATE",
    "C08_PARTIAL_ACTION_GROUPOID_INVERSE_SEMIGROUP_RELATION": "PARTIAL_ANTECEDENT",
    "C09_PASS_CHANGE_OF_FRAME": "EXACT_DUPLICATE",
    "C10_P000_COMPOUND_NO_QUOTIENT_NATIVE_IDENTITY": "NO_MATERIAL_MATCH",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """p after q."""
    return tuple(p[q[i]] for i in range(6))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 6
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def main() -> None:
    claims = load(CLAIM_MAP)
    ledger = load(SOURCE_LEDGER)

    assert claims["classification_vocabulary"] == [
        "EXACT_DUPLICATE",
        "PARTIAL_ANTECEDENT",
        "ADJACENT_METHOD",
        "NO_MATERIAL_MATCH",
    ]
    rows = claims["rows"]
    assert len(rows) == 10
    by_id = {row["claim_id"]: row for row in rows}
    assert set(by_id) == set(EXPECTED)
    for cid, classification in EXPECTED.items():
        assert by_id[cid]["classification"] == classification
        assert classification in ALLOWED

    source_ids = {s["source_id"] for s in ledger["sources"]}
    assert len(source_ids) == len(ledger["sources"])
    for row in rows:
        assert set(row["sources"]) <= source_ids

    # Exact natural S6 pointwise-stabilizer counts.
    perms = list(itertools.permutations(range(6)))
    assert len(perms) == math.factorial(6) == 720
    counts = []
    for k in range(7):
        counts.append(sum(all(p[i] == i for i in range(k)) for p in perms))
    assert counts == [720, 120, 24, 6, 2, 1, 1]
    assert min(k for k, c in enumerate(counts) if c == 1) == 5

    # Five anchors + bijectivity contain exactly the same 720 choices as a full frame.
    frame5_count = 1
    for n in range(6, 1, -1):
        frame5_count *= n
    assert frame5_count == 720 == len(perms)

    # Bij(A,C) is an S6 torsor under postcomposition:
    # for every pair of frames p,q there is a unique g=q∘p^{-1}.
    sample_frames = [perms[0], perms[137], perms[-1]]
    for p in sample_frames:
        pinv = inverse(p)
        for q in sample_frames:
            g = compose(q, pinv)
            assert compose(g, p) == q
            # uniqueness is immediate because h∘p=q => h=q∘p^{-1};
            # verify no second permutation in S6 satisfies it.
            matches = sum(compose(h, p) == q for h in perms)
            assert matches == 1

    # Gauge/PASS reindexing regression with deliberately asymmetric M.
    M = [[10 * i + j + 1 for j in range(6)] for i in range(6)]
    f = perms[211]
    for g in perms:
        ginv = inverse(g)
        # M'(c',d') = M(g^{-1}c', g^{-1}d')
        Mp = [
            [M[ginv[c]][ginv[d]] for d in range(6)]
            for c in range(6)
        ]
        fp = compose(g, f)
        for i in range(6):
            for j in range(6):
                assert Mp[fp[i]][fp[j]] == M[f[i]][f[j]]

    guard = claims["terminology_guard"].lower()
    assert "flat" in guard and "trivial holonomy" in guard
    assert claims["novelty_guard"] == "NO_MATERIAL_MATCH != NOVELTY"
    assert ledger["terminology_finding"]

    print("PASS P000_AXIS_CHANNEL_FRAME_PRIOR_ART_AUDIT_V7_CHECK")
    print("S6 stabilizers:", counts)
    print("full frames:", len(perms), "five-anchor presentations:", frame5_count)
    print("claim rows:", len(rows), "source rows:", len(ledger["sources"]))


if __name__ == "__main__":
    main()
