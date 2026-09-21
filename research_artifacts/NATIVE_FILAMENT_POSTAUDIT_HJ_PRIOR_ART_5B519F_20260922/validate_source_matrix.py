#!/usr/bin/env python3
import json, sys, hashlib
from pathlib import Path

ALLOWED = {
    "EXACT_DUPLICATE",
    "PARTIAL_ANTECEDENT",
    "ADJACENT_METHOD",
    "NO_MATERIAL_MATCH_IN_AUDITED_SET",
}
REQUIRED_LAYERS = ["H1","H2","J1","J2","C1","C2"]

def fail(msg):
    raise SystemExit("FAIL: " + msg)

p = Path(sys.argv[1])
data = json.loads(p.read_text(encoding="utf-8"))
if data.get("schema") != "ENTERPRISE_MATH_EXTERNAL_PRIOR_ART_AUDIT_MATRIX_V1":
    fail("wrong schema")
rows = data.get("classifications")
if not isinstance(rows, list) or [r.get("layer") for r in rows] != REQUIRED_LAYERS:
    fail("layers must be exactly H1,H2,J1,J2,C1,C2 in order")
source_ids = {s.get("id") for s in data.get("sources", [])}
if len(source_ids) != len(data.get("sources", [])):
    fail("duplicate source id")
for row in rows:
    if row.get("classification") not in ALLOWED:
        fail("bad enum at " + str(row.get("layer")))
    for f in ("frozen_target","source_hypotheses","source_conclusions","boundary"):
        if not isinstance(row.get(f), str) or not row[f].strip():
            fail(f"empty {f} at {row.get('layer')}")
    ids = row.get("source_ids")
    if not isinstance(ids, list) or any(x not in source_ids for x in ids):
        fail("unknown source id at " + row["layer"])
for s in data.get("sources", []):
    for f in ("citation","url","source_role","exact_hypotheses_or_scope","exact_conclusion_or_content"):
        if not isinstance(s.get(f), str) or not s[f].strip():
            fail(f"source {s.get('id')} missing {f}")
overall = data.get("overall_disposition", {})
if overall.get("exact_duplicate_found") is not False:
    fail("exact_duplicate_found must be false for this audit")
text = json.dumps(data, ensure_ascii=False)
for phrase in ("not establish novelty", "not an exhaustive literature search", "do not infer common provenance"):
    if phrase.lower() not in text.lower():
        fail("missing caution: " + phrase)
c2 = next(r for r in rows if r["layer"]=="C2")
for phrase in ("numerical only","common provenance","causal mechanism"):
    if phrase.lower() not in c2["boundary"].lower():
        fail("C2 narrowing missing " + phrase)
h2 = next(r for r in rows if r["layer"]=="H2")
if "prime-only" not in h2["boundary"] or "odd-q" not in h2["boundary"]:
    fail("H2 odd-q narrowing missing")
h1 = next(r for r in rows if r["layer"]=="H1")
if "off-diagonal" not in h1["boundary"]:
    fail("H1 off-diagonal narrowing missing")

print(json.dumps({
    "status":"PASS",
    "schema":data["schema"],
    "layers":REQUIRED_LAYERS,
    "classifications":{r["layer"]:r["classification"] for r in rows},
    "source_count":len(data.get("sources",[])),
    "query_count":len(data.get("exact_query_ledger",[])),
    "matrix_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
}, indent=2))
