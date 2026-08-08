#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources.json"
LINEAGE = ROOT / "lineage.json"
PRIOR_EN = ROOT / "docs" / "PRIOR_ART_AND_NOVELTY.en.md"
PRIOR_ZH = ROOT / "docs" / "PRIOR_ART_AND_NOVELTY.zh-CN.md"
SRC_RE = re.compile(r"\[(SRC-[A-Z0-9-]+)\]")

REQUIRED_SOURCE_FIELDS = {
    "id", "title", "authors", "year", "kind", "primary_url",
    "role", "enterprise_use", "not_claimed", "verified_at"
}

def main() -> int:
    errors = []
    sources_data = json.loads(SOURCES.read_text(encoding="utf-8"))
    lineage_data = json.loads(LINEAGE.read_text(encoding="utf-8"))

    source_ids = set()
    for source in sources_data.get("sources", []):
        missing = REQUIRED_SOURCE_FIELDS - set(source)
        if missing:
            errors.append(f"{source.get('id', '<unknown>')}: missing fields {sorted(missing)}")
        sid = source.get("id")
        if not isinstance(sid, str) or not sid.startswith("SRC-"):
            errors.append(f"invalid source id: {sid!r}")
            continue
        if sid in source_ids:
            errors.append(f"duplicate source id: {sid}")
        source_ids.add(sid)
        if not source.get("primary_url"):
            errors.append(f"{sid}: missing primary_url")
        if not source.get("authors"):
            errors.append(f"{sid}: missing authors")
        if not source.get("role"):
            errors.append(f"{sid}: missing role")

    relation_types = set(lineage_data.get("relation_types", []))
    novelty_statuses = set(lineage_data.get("novelty_statuses", []))
    component_ids = set()

    for comp in lineage_data.get("components", []):
        cid = comp.get("id")
        if cid in component_ids:
            errors.append(f"duplicate component id: {cid}")
        component_ids.add(cid)
        if comp.get("novelty_status") not in novelty_statuses:
            errors.append(f"{cid}: unknown novelty_status {comp.get('novelty_status')}")
        for rel in comp.get("source_relations", []):
            sid = rel.get("source_id")
            if sid not in source_ids:
                errors.append(f"{cid}: unknown source_id {sid}")
            if rel.get("relation") not in relation_types:
                errors.append(f"{cid}: unknown relation {rel.get('relation')}")

    overall = lineage_data.get("overall_novelty_claim", {})
    if overall.get("status") not in novelty_statuses:
        errors.append(f"unknown overall novelty status: {overall.get('status')}")

    prose_files = [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CONTRIBUTING.zh-CN.md",
        *sorted((ROOT / "docs").glob("*.md")),
    ]
    for path in prose_files:
        if not path.exists():
            continue
        for sid in SRC_RE.findall(path.read_text(encoding="utf-8")):
            if sid not in source_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown citation [{sid}]")

    for path in (PRIOR_EN, PRIOR_ZH):
        text = path.read_text(encoding="utf-8")
        cited = set(SRC_RE.findall(text))
        missing = sorted(source_ids - cited)
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: registered sources absent from main lineage map: {missing}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print(f"PASS: {len(source_ids)} sources and {len(component_ids)} lineage components form a valid citation/provenance graph.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
