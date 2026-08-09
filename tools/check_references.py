#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC_RE = re.compile(r"\[(SRC-[A-Z0-9-]+)\]")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

REQUIRED_SOURCE_FIELDS = {
    "id", "title", "authors", "year", "kind", "primary_url",
    "role", "enterprise_use", "not_claimed", "verified_at"
}

RESULT_CONSERVATION_SCHEMA = "ENTERPRISE_MATH_RESULT_CONSERVATION_V1"
RESULT_CONSERVATION_FATES = {
    "INTEGRATE",
    "SUPERSEDED",
    "COMPARATOR-NEGATIVE",
    "OWNER_MOVED",
    "REJECTED",
}


def registry_files(stem: str) -> list[pathlib.Path]:
    base = ROOT / f"{stem}.json"
    shards = sorted(ROOT.glob(f"{stem}_*.json"))
    return [base, *shards]


def prior_art_files(suffix: str) -> list[pathlib.Path]:
    return sorted(DOCS.glob(f"PRIOR_ART*{suffix}"))


def result_conservation_files() -> list[pathlib.Path]:
    return sorted(ROOT.glob("result_conservation_*.json"))


def load_registry(paths: list[pathlib.Path]) -> list[dict]:
    records = []
    for path in paths:
        if not path.exists():
            continue
        records.append(json.loads(path.read_text(encoding="utf-8")))
    return records


def _nonempty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def validate_result_conservation_manifest(
    manifest: dict,
    label: str = "<manifest>",
) -> list[str]:
    """Validate a semantic result-conservation closure certificate.

    This is deliberately a *closure invariant* checker, not a theorem prover and
    not an automatic inventory generator.  A researcher/reviewer must first
    establish the semantic inventory and assert ``inventory_complete=true`` for
    one frozen source snapshot.  The checker then prevents retirement with an
    unresolved result, an unrecognized fate, duplicate semantic IDs, or missing
    target/rationale/evidence.
    """
    errors: list[str] = []
    if manifest.get("schema") != RESULT_CONSERVATION_SCHEMA:
        errors.append(f"{label}: unexpected result-conservation schema")

    owner = manifest.get("source_owner")
    if not isinstance(owner, dict):
        errors.append(f"{label}: source_owner must be an object")
    else:
        if not isinstance(owner.get("id"), str) or not owner.get("id", "").strip():
            errors.append(f"{label}: source_owner.id must be a non-empty string")
        source_head = owner.get("source_head")
        if not isinstance(source_head, str) or not SHA_RE.fullmatch(source_head):
            errors.append(f"{label}: source_owner.source_head must be a 40-hex Git SHA")
        if owner.get("retirement_state") != "L5_PROVENANCE":
            errors.append(f"{label}: source_owner.retirement_state must be L5_PROVENANCE")

    if manifest.get("closure_state") != "RESOLVED":
        errors.append(f"{label}: closure_state must be RESOLVED on canonical main")
    if manifest.get("inventory_complete") is not True:
        errors.append(f"{label}: inventory_complete must be true before source retirement")
    if not _nonempty_string_list(manifest.get("inventory_basis")):
        errors.append(f"{label}: inventory_basis must be a non-empty string list")
    if not _nonempty_string_list(manifest.get("closure_evidence")):
        errors.append(f"{label}: closure_evidence must be a non-empty string list")

    unresolved = manifest.get("unresolved_results")
    if unresolved != []:
        errors.append(f"{label}: unresolved_results must be exactly [] for RESOLVED closure")

    results = manifest.get("results")
    if not isinstance(results, list) or not results:
        errors.append(f"{label}: results must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for index, result in enumerate(results):
        prefix = f"{label}: results[{index}]"
        if not isinstance(result, dict):
            errors.append(f"{prefix} must be an object")
            continue

        rid = result.get("id")
        if not isinstance(rid, str) or not rid.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        elif rid in seen_ids:
            errors.append(f"{label}: duplicate result id {rid}")
        else:
            seen_ids.add(rid)

        statement = result.get("statement")
        if not isinstance(statement, str) or not statement.strip():
            errors.append(f"{prefix}.statement must be a non-empty string")

        fate = result.get("fate")
        if fate not in RESULT_CONSERVATION_FATES:
            errors.append(
                f"{prefix}.fate must be one of {sorted(RESULT_CONSERVATION_FATES)}; "
                f"got {fate!r}"
            )

        if not _nonempty_string_list(result.get("source_evidence")):
            errors.append(f"{prefix}.source_evidence must be a non-empty string list")
        if not _nonempty_string_list(result.get("targets")):
            errors.append(f"{prefix}.targets must be a non-empty string list")
        rationale = result.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{prefix}.rationale must be a non-empty string")
        if not _nonempty_string_list(result.get("evidence")):
            errors.append(f"{prefix}.evidence must be a non-empty string list")

    return errors


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

    # Result-conservation certificates are semantic closure ledgers, not file
    # preservation manifests.  This checker does not infer that the inventory is
    # complete; it enforces the closure invariants once a human/research audit has
    # made that explicit assertion for a frozen source snapshot.
    conservation_paths = result_conservation_files()
    for path in conservation_paths:
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        errors.extend(validate_result_conservation_manifest(manifest, path.name))

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print(
        f"PASS: {len(source_ids)} sources and {len(component_ids)} lineage components "
        f"across {len(source_registries)} source registry file(s) and "
        f"{len(lineage_registries)} lineage registry file(s); "
        f"{len(conservation_paths)} resolved result-conservation certificate(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
