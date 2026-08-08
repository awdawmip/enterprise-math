#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC_RE = re.compile(r"\[(SRC-[A-Z0-9-]+)\]")

REQUIRED_SOURCE_FIELDS = {
    "id", "title", "authors", "year", "kind", "primary_url",
    "role", "enterprise_use", "not_claimed", "verified_at"
}


def registry_files(stem: str) -> list[pathlib.Path]:
    base = ROOT / f"{stem}.json"
    shards = sorted(ROOT.glob(f"{stem}_*.json"))
    return [base, *shards]


def prior_art_files(suffix: str) -> list[pathlib.Path]:
    return sorted(DOCS.glob(f"PRIOR_ART*{suffix}"))


def load_registry(paths: list[pathlib.Path]) -> list[dict]:
    records = []
    for path in paths:
        if not path.exists():
            continue
        records.append(json.loads(path.read_text(encoding="utf-8")))
    return records


def main() -> int:
    errors = []
    source_registries = load_registry(registry_files("sources"))
    lineage_registries = load_registry(registry_files("lineage"))

    source_ids = set()
    for registry in source_registries:
        for source in registry.get("sources", []):
            missing = REQUIRED_SOURCE_FIELDS - set(source)
            if missing:
                errors.append(f"{source.get('id', '<unknown>')}: missing fields {sorted(missing)}")
            sid = source.get("id")
            if not isinstance(sid, str) or not sid.startswith("SRC-"):
                errors.append(f"invalid source id: {sid!r}")
                continue
            if sid in source_ids:
                errors.append(f"duplicate source id across registries: {sid}")
            source_ids.add(sid)
            if not source.get("primary_url"):
                errors.append(f"{sid}: missing primary_url")
            if not source.get("authors"):
                errors.append(f"{sid}: missing authors")
            if not source.get("role"):
                errors.append(f"{sid}: missing role")

    relation_types = set()
    novelty_statuses = set()
    for registry in lineage_registries:
        relation_types.update(registry.get("relation_types", []))
        novelty_statuses.update(registry.get("novelty_statuses", []))

    # Shards may omit the vocabulary and inherit it from the base lineage registry.
    component_ids = set()
    for registry in lineage_registries:
        for comp in registry.get("components", []):
            cid = comp.get("id")
            if cid in component_ids:
                errors.append(f"duplicate component id across registries: {cid}")
            component_ids.add(cid)
            if comp.get("novelty_status") not in novelty_statuses:
                errors.append(f"{cid}: unknown novelty_status {comp.get('novelty_status')}")
            for rel in comp.get("source_relations", []):
                sid = rel.get("source_id")
                if sid not in source_ids:
                    errors.append(f"{cid}: unknown source_id {sid}")
                if rel.get("relation") not in relation_types:
                    errors.append(f"{cid}: unknown relation {rel.get('relation')}")

    overall_claims = [r.get("overall_novelty_claim") for r in lineage_registries if r.get("overall_novelty_claim")]
    if not overall_claims:
        errors.append("missing overall novelty claim")
    for overall in overall_claims:
        if overall.get("status") not in novelty_statuses:
            errors.append(f"unknown overall novelty status: {overall.get('status')}")

    prose_files = [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CONTRIBUTING.zh-CN.md",
        *sorted(DOCS.glob("*.md")),
    ]
    for path in prose_files:
        if not path.exists():
            continue
        for sid in SRC_RE.findall(path.read_text(encoding="utf-8")):
            if sid not in source_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown citation [{sid}]")

    # The canonical prior-art map may be split into bilingual appendices as it grows.
    # Each language corpus must still cite every registered source at least once.
    for label, suffix in (("English", ".en.md"), ("Chinese", ".zh-CN.md")):
        paths = prior_art_files(suffix)
        if not paths:
            errors.append(f"missing {label} prior-art corpus")
            continue
        cited = set()
        for path in paths:
            cited.update(SRC_RE.findall(path.read_text(encoding="utf-8")))
        missing = sorted(source_ids - cited)
        if missing:
            errors.append(f"{label} prior-art corpus: registered sources absent from lineage prose: {missing}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print(
        f"PASS: {len(source_ids)} sources and {len(component_ids)} lineage components "
        f"across {len(source_registries)} source registry file(s) and "
        f"{len(lineage_registries)} lineage registry file(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
