#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS"
TASK = "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS"
PUB = "TP2-C9A47F3D1E805B62A4C7"
SNAP = "c95d2767f0d6f24977db46c24990a27319199021"
P000_TASK = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
P000_HEAD = "TP2-E5B7C19A3D604F821583"
STALE_REVIEW = "DR-6D2A91F4C8E3057B1246"
CANON_G17 = ("RR-985AEE277DE45AFCC9D8", "DR-61B4E8C29A705FD31746")

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def require(cond: bool, msg: str):
    if not cond:
        raise AssertionError(msg)

atlas = load(ART / "selector_atlas_v2.json")
resolver = load(ART / "accepted_resolver_manifest_v2.json")
delta = load(ART / "current_head_delta_manifest_v2.json")

for obj, schema in [
    (atlas, "GEO6_OBJECTIVE_SEMANTIC_SELECTOR_ATLAS_V2"),
    (resolver, "GEO6_ACCEPTED_RESOLVER_MANIFEST_V2"),
    (delta, "GEO6_CURRENT_HEAD_DELTA_MANIFEST_V2"),
]:
    require(obj["schema"] == schema, f"wrong schema: {schema}")
    require(obj["task_id"] == TASK, "task mismatch")
    require(obj["publication_id"] == PUB, "publication mismatch")

require(atlas["execution_snapshot"] == SNAP, "atlas snapshot drift")
require(resolver["execution_snapshot"] == SNAP, "resolver snapshot drift")
require(delta["scan"]["execution_snapshot"] == SNAP, "delta snapshot drift")

selectors = atlas["selectors"]
require(len(selectors) == 12, "selector count != 12")
ids = [row["id"] for row in selectors]
require(len(set(ids)) == 12, "duplicate selector id")
counts = Counter(row["status"] for row in selectors)
require(dict(atlas["counts"]) == {"R": 0, "P": 3, "U": 9, "D": 0}, "atlas count drift")
require(counts == Counter({"U": 9, "P": 3}), "selector status drift")

rows = atlas["pair_matrix"]["upper_rows"]
require(len(rows) == 11, "pair matrix row count drift")
require([len(row) for row in rows] == list(range(11, 0, -1)), "pair matrix shape drift")
require(sum(map(len, rows)) == 66, "pair count != 66")
require(all(ch in "ODXSU" for row in rows for ch in row), "unknown pair code")
require(all("S" not in row for row in rows), "SAME_SELECTOR introduced")
require(atlas["duplicate_pairs"] == [], "duplicate selector introduced")

edges = [tuple(edge) for edge in atlas["dependency_dag"]]
require(edges == [(3,5),(1,6),(6,7),(8,9),(8,10),(8,11),(6,11)], "dependency DAG drift")
adj = defaultdict(list)
indeg = [0] * 12
for a, b in edges:
    adj[a].append(b)
    indeg[b] += 1
q = deque(i for i, d in enumerate(indeg) if d == 0)
seen = 0
while q:
    u = q.popleft()
    seen += 1
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
require(seen == 12, "dependency DAG cycle")
require(atlas["roots"] == [0,1,2,3,4,8], "root set drift")
require(len(atlas["recommendations"]) == 3 <= 3, "recommendation cap violated")
require(atlas["revalidation"]["semantic_drift"] is False, "semantic drift unexpectedly true")

candidate_pairs = {(row[0], row[1]) for row in resolver["candidates"]}
require(CANON_G17 in candidate_pairs, "canonical Gen17 authority missing")
require(all(row[1] != STALE_REVIEW for row in resolver["candidates"]), "stale Gen17 review retained")
require(resolver["canonical_review_repair"]["current_canonical_review_id"] == CANON_G17[1], "Gen17 canonical review mismatch")
require(resolver["canonical_review_repair"]["stale_review_id"] == STALE_REVIEW, "Gen17 stale review mismatch")
require(resolver["full_resolvers"] == [], "unexpected full resolver")
require(resolver["partial_bindings"] == {
    "0": ["RR-7A29C4C19E5F83B602D7"],
    "2": ["RR-774CF0739BD6CD117CF6","RR-0C7464292459CAF82805","RR-985AEE277DE45AFCC9D8"],
    "7": ["RR-0C7464292459CAF82805","RR-7A29C4C19E5F83B602D7"],
}, "partial binding drift")

for result_id, review_id, _label, disposition, _impacts in resolver["candidates"]:
    path = ROOT / "research_result_reviews" / result_id / f"{review_id}.json"
    require(path.is_file(), f"review missing: {review_id}")
    review = load(path)
    require(review["review_id"] == review_id, f"review id mismatch: {review_id}")
    require(review["result_id"] == result_id, f"result binding mismatch: {review_id}")
    require(review["disposition"] == disposition == "ACCEPTED", f"non-accepted resolver: {review_id}")

stale_path = ROOT / "research_result_reviews" / CANON_G17[0] / f"{STALE_REVIEW}.json"
require(not stale_path.exists(), "superseded Gen17 review path still present as current file")

excluded = resolver["excluded_nonaccepted"]
require(len(excluded) == 1 and excluded[0]["review_id"] == "DR-C5539B165E52AAAA3C6A", "nonaccepted exclusion drift")
p11 = load(ROOT / "research_result_reviews" / "RR-C3E71A9D4B6052F88E21" / "DR-C5539B165E52AAAA3C6A.json")
require(p11["disposition"] == "REQUEST_REVISION", "P11 nonterminal review changed")

pdir = ROOT / "research_task_records" / P000_TASK
records = [load(path) for path in pdir.glob("*.json")]
active = [row for row in records if row.get("record_state") == "ACTIVE"]
require(active, "no active P000-L1 publications")
max_gen = max(int(row.get("publication_generation", -1)) for row in active)
require(max_gen == 19, f"unexpected P000-L1 max generation: {max_gen}")
gen19 = [row for row in active if int(row.get("publication_generation", -1)) == 19]
require(len(gen19) == 1 and gen19[0]["publication_id"] == P000_HEAD, "P000-L1 current Gen19 head mismatch")
head = gen19[0]
require(head["supersedes_publication_id"] == "TP2-D6A41E9C3B705F821847", "P000-L1 supersession mismatch")
require(head.get("concurrent_duplicate_publication_ids_resolved") == ["TP2-D4A7C19E5B306F821472"], "P000-L1 duplicate resolution mismatch")
require(atlas["external_gate"]["current_publication_id"] == P000_HEAD, "atlas P000 gate head mismatch")
require(atlas["external_gate"]["state"] == "ACTIVE_NO_DUPLICATE_GATE", "P000 no-duplicate gate lost")

require(delta["before"]["counts"] == delta["after"]["counts"] == {"R":0,"P":3,"U":9,"D":0}, "before/after status drift")
require(delta["before"]["roots"] == delta["after"]["roots"] == 6, "root count drift")
require(delta["before"]["recommendations"] == delta["after"]["recommendations"] == 3, "recommendation drift")
require(delta["after"]["p000_l1_publication"] == P000_HEAD, "delta P000 head mismatch")
require(delta["after"]["g17_review"] == CANON_G17[1], "delta Gen17 authority mismatch")
require(delta["terminal"]["semantic_drift"] is False, "delta semantic drift true")
require(delta["terminal"]["authority_drift"] is True, "authority drift not recorded")
require(delta["terminal"]["routing_drift"] is True, "routing drift not recorded")

delta_by_result = {row["result_id"]: row for row in delta["rows"]}
require(delta_by_result["RR-7FED4A83F3922D37319D"]["disposition"] == "CONTEXT_ONLY", "Gen18 semantic scope overstated")
for rr in ["RR-AC29BC88CA7CB2AFBA21","RR-7E4C19A2D6B3058F14C7","RR-A03013D3867717461674"]:
    require(delta_by_result[rr]["disposition"] == "TYPE_MAP_REJECTED", f"type-map rejection lost: {rr}")
require(all(row["semantic_delta"] is False for row in delta["rows"]), "unexplained semantic delta")

print("PASS GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_CURRENT_HEAD_REVALIDATION_V2")
print("selectors=12 pairs=66 resolved=0 partial=3 unresolved=9 duplicate=0 roots=6 recommendations=3")
print(f"snapshot={SNAP} p000_l1_head={P000_HEAD} g17_review={CANON_G17[1]}")
