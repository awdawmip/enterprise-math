# Conjecture Registry Storage

Status: `ACTIVE_CANONICAL_STORAGE_RULE`
Effective: `2026-09-07`

## Canonical logical view

Beginning with G3, the conjecture registry is read through `conjecture_registry_manifest.json`.

The current logical registry is the ordered union of:

1. the historical consolidated base `conjecture_registry.json` through `BACKFILL-20260906-G2`; and
2. every shard listed in `ordered_generation_shards` in manifest order.

This changes storage, not epistemic semantics. `docs/CONJECTURE_ASSET_GOVERNANCE.md` and `conjecture_asset_contract.json` continue to govern what a conjecture means and how it may be used.

## Why sharding is required

A permanently monolithic registry would require whole-file replacement for every scan generation. That creates avoidable overwrite risk while concurrent Enterprise Math research is active. Generation shards make new registration append-only and auditable.

## Invariants

- Asset IDs are globally unique and never reused.
- A later shard may add a new asset or an explicit transition for an old asset; it may not silently redefine an earlier asset.
- An explicit state transition must cite the prior ID/version and evidence supporting the transition.
- Readers must use the manifest logical view, not assume the G2 base snapshot is current.
- A compaction may produce a new consolidated base only after an equivalence audit confirms that no asset, transition, exclusion classification or provenance reference was lost.
- After compaction, the manifest must point to the new base and retain historical generation provenance.

## Scanner rule

`conjecture_scanner_policy.json` is authoritative for scan intake and dependency propagation and points to this manifest-based logical registry.
