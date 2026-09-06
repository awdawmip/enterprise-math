# Global Knowledge import manifest — 2026-09-06

Status: `PROJECT-KNOWLEDGE IMPORT / NO THEOREM PROMOTION / NO FOUNDATION CHANGE`
Target project: `awdawmip/enterprise-math`
Source repository: `awdawmip/chatgpt-global-knowledge`
Initial source snapshot: `main@6e70948745cff137e1c64ea09bf7898980377187`
First tail catch-up source snapshot: `main@de4267a9f5b51492c91a98e1cd5d6280081f693c`
Second tail catch-up source snapshot: `main@5c6d2303749fac3f25ba48cbfdc927c90aea4114`
Final bounded source cutoff for this transaction: `main@3fb88e2f62f6ea51fc558df3da68267cc35cf22e`
Initial target base snapshot: `main@ff1aeaf6befb9c72b4e59f7dec6b018671633e3a`
First import merged at target: `main@bd00d2b409b78b83cc8e461bf382170aeee66bfe`
Second import merged at target: `main@687a44dec5ffbf2901629af458261ba6a849ae21`
Third import merged at target: `main@9bc95577902f14e1539b1849ed9c4e31a155fa54`

## Purpose

This directory preserves recent Enterprise Math material that existed durably in the account-level GLOBAL_KNOWLEDGE_V1 repository but had no equivalent durable source in the Enterprise Math repository at the migration snapshots.

The import is intentionally non-promotional:

- imported `RESEARCH_FRONTIER` material remains research frontier material;
- `NOT_MILLENNIUM_PROOF` remains binding where stated;
- `HYPOTHESIS / TESTING` remains hypothesis/testing and is not promoted by co-location with verified reductions;
- imported terminal archives and progress events remain archives/progress events, not accepted theorem ledgers;
- imported `VERIFIED` theorem adapters remain adapters/compositions over existing Enterprise tool families unless separately admitted through the source project's normal tool/Foundation process;
- no Driver review, Foundation admission, Working Truth, task publication, claim, or canonical theorem status is created by this import;
- current source `p000_reality_foundation.json` and current control authority remain authoritative over stale provenance text embedded in imported records.

## Imported material

1. `BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md`
   - direct-user account-wide BRC method-priority contract;
   - imported because no equivalent policy file was present in the source project at the migration snapshot;
   - records the policy without rewriting theorem ledgers or machine-control JSON.

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
   - RSA-270 BRC add/sub cost-field and coordinate-geometrization progress event;
   - preserves the quantified no-go refinement and exact ridge/cost identities without claiming a factor.

6. `20260906T202000+0800-rsa270-round7-minimax-j-sieve-9d4c2e.md`
   - multiplier-lattice cost-field minimax and forced-mod-72 endpoint sieve;
   - closes the single-direction route at an infeasible quantified budget; no factor obtained.

7. `20260906T205500+0800-rsa270-round8-combined-strategy-table-5b8f1a.md`
   - complete direction table for combined cost × endpoint sieve;
   - marks the branch family as quantitatively closed; no factor obtained.

8. `nt-rh-ground-state-feshbach-leakage-20260905.md`
   - verified exact rank-one / finite-low-mode Feshbach reduction, including the 2026-09-06 correction that rank one is not a robust predictive-complete state for the tested Weil square-shell propagation;
   - explicitly not an RH proof.

9. `nt-rh-landau-widom-critical-repair-band-20260906.md`
   - `HYPOTHESIS / TESTING` record proposing a growing repair-band scale near `4 L exp(2L)` / `4 n^2 log n` from three floating pressure tests plus Landau-Widom/Shannon structure;
   - numerical structural hypothesis only, not a theorem and not an RH proof.

10. `nt-tool-spectral-tail-feshbach-certificate-20260906.md`
    - verified reusable theorem adapter over existing T2/T4/T6 machinery;
    - gives exact/coarse high-tail response certificates and observer-relative minimal future-safe repair rank;
    - explicitly not a new top-level T-family.

11. `nt-tool-response-optimal-svd-repair-20260906.md`
    - verified response-optimal SVD repair adapter;
    - identifies the dominant left singular subspace of the normalized future-response operator as the optimal rank-constrained repair carrier;
    - defines response-effective rank as future-observer relative and does not itself prove block positivity.

12. `nt-tool-response-inertia-threshold-certificate-20260906.md`
    - verified block-inertia threshold adapter for response singular-value counts;
    - certifies the number of normalized response singular values above a threshold via the negative inertia of `[[eta^2 A,B],[B*,D]]`, avoiding explicit inverse square roots;
    - finite numerical inertia is not proof without rigorous enclosures, and this remains a composition of existing T2/T4/T6 machinery.

13. `nt-tool-response-model-transfer-capacity-20260906.md`
    - verified normalized-response model-transfer adapter using operator-norm or Hilbert-Schmidt defect control;
    - converts model singular-value information plus explicit defect into a finite bound on extra threshold-crossing repair directions;
    - explicitly does not transfer RH positivity by itself and is not a new top-level tool family.

## Deliberately not reverse-imported

- Global `projects/enterprise-math/P000_REALITY_FOUNDATION.json` was not copied because the source project already had a newer P000 revision at the migration snapshot.
- PCF7FIX/BRC re-verification handoff material was not copied back because it already referenced durable Enterprise Math source artifacts and was a source-to-global handoff, not a source gap.
- `journal/enterprise-math/2026-09-06/20260906T134800+0800-rh-green-alladi-critical-source-port.md` was not reverse-imported because it explicitly mirrors source commit `4b1c52677c5f7d07e9bd6527b6cf1a5375530e98` and source file `research_notes/RH_GREEN_ALLADI_CRITICAL_PRIMITIVE_SOURCE_PORT_20260906.md`, which remains present in Enterprise Math.
- The large 2026-09-05 number-theory tool-harvest catalog was not bulk-copied in this transaction. Enterprise Math already has a substantial canonical tool registry / invocation policy / method inventory; those harvested notes require semantic tool-by-tool dedup rather than filename mirroring. Bulk duplication would create two competing catalogs.

## Provenance rule

Paths mentioned inside imported files that begin with `knowledge/...` or `journal/...` are provenance references to the GLOBAL_KNOWLEDGE_V1 source repository unless a source-project equivalent is explicitly added later. Do not reinterpret those path strings as current Enterprise Math canonical paths.
