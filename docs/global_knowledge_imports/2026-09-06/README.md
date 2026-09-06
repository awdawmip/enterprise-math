# Global Knowledge import manifest — 2026-09-06

Status: `PROJECT-KNOWLEDGE IMPORT / NO THEOREM PROMOTION / NO FOUNDATION CHANGE`
Target project: `awdawmip/enterprise-math`
Source repository: `awdawmip/chatgpt-global-knowledge`
Source snapshot used for imported bytes: `main@6e70948745cff137e1c64ea09bf7898980377187`
Target base snapshot before branch creation: `main@ff1aeaf6befb9c72b4e59f7dec6b018671633e3a`

## Purpose

This directory preserves recent Enterprise Math material that existed durably in the account-level GLOBAL_KNOWLEDGE_V1 repository but had no equivalent durable source in the Enterprise Math repository at the migration snapshot.

The import is intentionally non-promotional:

- imported `RESEARCH_FRONTIER` material remains research frontier material;
- `NOT_MILLENNIUM_PROOF` remains binding where stated;
- imported terminal archives remain archives, not accepted theorem ledgers;
- no Driver review, Foundation admission, Working Truth, task publication, claim, or canonical theorem status is created by this import;
- current source `p000_reality_foundation.json` and current control authority remain authoritative over stale provenance text embedded in imported records.

## Imported material

1. `BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md`
   - direct-user account-wide BRC method-priority contract;
   - imported because no equivalent policy file was present in the source project at the migration snapshot;
   - this file records the policy; it does not itself rewrite theorem ledgers or machine-control JSON.

2. `pde-critical-helicity-double-null-20260906.md`
   - Navier–Stokes critical helicity double-null / FCC shell-coherence frontier;
   - status preserved as conditional/frontier work, not a Millennium proof.

3. `pde-minority-helicity-L3-criterion-20260906.md`
   - scale-critical minority-helicity `L^3` conditional regularity criterion;
   - status preserved as conditional/frontier work, not a Millennium proof.

4. `rsa270-enterprise-reformulation-terminal-archive-20260906.md`
   - durable terminal archive of the factor-blind RSA-270 Enterprise/BRC reformulation line;
   - explicitly records that RSA-270 was not factored.

5. `20260906T194000+0800-rsa270-cost-field-geometrization-7e3b5d.md`
   - later RSA-270 BRC add/sub cost-field and coordinate-geometrization progress event;
   - preserves the quantified no-go refinement and the exact ridge/cost identities without claiming a factor.

## Deliberately not reverse-imported

- Global `projects/enterprise-math/P000_REALITY_FOUNDATION.json` was not copied because the source project already had a newer P000 revision at the migration snapshot.
- PCF7FIX/BRC re-verification handoff material was not copied back because it already referenced durable Enterprise Math source artifacts and was a source-to-global handoff, not a source gap.
- The large 2026-09-05 number-theory tool-harvest catalog was not bulk-copied in this transaction. Enterprise Math already has a substantial canonical tool registry / invocation policy / method inventory; those harvested notes require semantic tool-by-tool dedup rather than filename mirroring. Bulk duplication would create two competing catalogs.

## Provenance rule

Paths mentioned inside imported files that begin with `knowledge/...` or `journal/...` are provenance references to the GLOBAL_KNOWLEDGE_V1 source repository unless a source-project equivalent is explicitly added later. Do not reinterpret those path strings as current Enterprise Math canonical paths.
