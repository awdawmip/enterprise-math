#!/usr/bin/env python3
"""Bounded GEO6 Gen2 authority/atlas seed check (not the full current-head delta scan)."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = ROOT / "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS"
TASK = "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS"
CURRENT_GEN17 = ("RR-985AEE277DE45AFCC9D8", "DR-61B4E8C29A705FD31746")
REMOVED_GEN17 = "DR-6D2A91F4C8E3057B1246"
EXPECTED = {
    "RR-73C4AC1CB16F08C64FC4": "DR-8F7328B65924F20CE3DA",
    "RR-774CF0739BD6CD117CF6": "DR-B84D90C29024FFBB4A22",
    "RR-0C7464292459CAF82805": "DR-BFFACB80B9FC4584EB37",
    "RR-7A29C4C19E5F83B602D7": "DR-1E9A6C4B2F7D3058A4C1",
    CURRENT_GEN17[0]: CURRENT_GEN17[1],
    "RR-8A7F3C29D14E6B50C2F1": "DR-A43FBD4CE025D9DACC72",
    "RR-5137B2C5D070E4CEA95E": "DR-082CBBED2C7411D276E0",
}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def closure(n, edges):
    reach = [[False] * n for _ in range(n)]
    for i, j in edges:
        assert 0 <= i < n and 0 <= j < n and i != j
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    assert all(not reach[i][i] for i in range(n)), "cycle detected"
    return {(i,j) for i in range(n) for j in range(n) if reach[i][j]}

def main():
    atlas = load(B / "selector_atlas.json")
    source = load(B / "accepted_resolver_manifest.json")
    assert atlas["task_id"] == TASK == source["task_id"]
    assert atlas["publication_id"] == source["publication_id"] == "TP2-6866CB3F890F6563C474"
    assert source["snapshot"] == atlas["snapshot"] == "228446b2d797372b2d18503116f612ba03701184"
    selectors = atlas["selectors"]
    assert len(selectors) == 12 and len({s["id"] for s in selectors}) == 12
    assert Counter(s["status"] for s in selectors) == Counter({"P":3, "U":9})
    assert atlas["counts"] == {"R":0,"P":3,"U":9,"D":0}
    assert atlas["duplicate_pairs"] == []
    assert len(atlas["recommendations"]) <= 3
    rows = atlas["pair_matrix"]["upper_rows"]
    assert [len(row) for row in rows] == list(range(11,0,-1))
    pairs = {(i,i+k+1):label for i,row in enumerate(rows) for k,label in enumerate(row)}
    assert len(pairs) == 66 and Counter(pairs.values()) == Counter({"O":53,"D":9,"X":4})
    reach = closure(12, atlas["dependency_dag"])
    assert reach == {edge for edge, rel in pairs.items() if rel == "D"}
    assert set(range(12)) - {j for _,j in atlas["dependency_dag"]} == set(atlas["roots"]) == {0,1,2,3,4,8}
    assert {i for i,s in enumerate(selectors) if s["status"]=="P"} == {0,2,7}
    expected = EXPECTED
    observed = {row[0]:row[1] for row in source["candidates"]}
    assert observed.keys() == expected.keys()
    assert all(row[3] == "ACCEPTED" for row in source["candidates"])
    assert observed[CURRENT_GEN17[0]] == REMOVED_GEN17, "baseline's historical Gen17 reference changed"
    assert not (ROOT / "research_result_reviews" / CURRENT_GEN17[0] / f"{REMOVED_GEN17}.json").exists()
    for rr, dr in expected.items():
        p = ROOT / "research_result_reviews" / rr / f"{dr}.json"
        obj = load(p)
        assert (obj["result_id"],obj["review_id"],obj["disposition"]) == (rr,dr,"ACCEPTED")
        assert obj["terminal"] is True
    p000 = load(ROOT / "research_task_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/TP2-D6A41E9C3B705F821847.json")
    assert p000["record_state"] == "ACTIVE" and p000["publication_generation"] == 18
    assert p000["task_id"] == "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
    print("PASS GEO6_GEN2_BOUNDED_AUTHORITY_SEED")
    print("source_reviews=7 accepted=7 current_Gen17=DR-61B4E8C29A705FD31746")
    print("baseline_selector_matrix=66 (O53 D9 X4), DAG_transitive_pairs=9, roots=6; R0 P3 U9 D0")
    print("P000_L1_publication_gen18=ACTIVE")
    print("delta_scan_after_20260831=NOT_PERFORMED, Gen2_Result=NOT_FREEZABLE_BY_THIS_CHECK")

if __name__ == "__main__":
    main()
