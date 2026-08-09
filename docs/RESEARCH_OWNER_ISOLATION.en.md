# Enterprise Math Research Owner Isolation Contract

Status: `ACTIVE / CANONICAL GOVERNANCE CONTRACT`  
Effective: 2026-08-09  
Scope: L1 core owners, L2 program owners, L3 bridges/probes, and L4 integration replays.

This contract sharpens Architecture v2 after live multi-agent migration exposed a recurring failure mode: synchronizing whole moving `main` trees into research owners makes unrelated mathematics appear as owner-local PR changes and recreates the branch entanglement that semantic replay is meant to remove.

Where an older migration note can be read as requiring an owner branch to continuously absorb `main`, this contract controls.

## 1. Core invariant

> **Owners research; integrations transport.**

L1/L2/L3 branches own a bounded mathematical frontier. They are allowed to be behind `main`.

L4 branches are the only branches that are expected to start from the latest canonical `main` for promotion.

Therefore:

- an L1/L2/L3 owner MUST NOT merge, rebase onto, or otherwise copy the whole current `main` merely to stay current;
- an owner MAY consume a specific canonical theorem/module as an explicit dependency when the research genuinely needs it;
- unrelated canonical changes are not owner-local changes and must not become part of the owner's PR surface;
- moving `main` is not a reason to rebuild a proved owner result.

## 2. Owner generations

An owner branch is a research generation with a fixed semantic payload, not a rolling mirror of the repository.

A healthy generation should be describable by:

```text
owner: <A/P/E home>
base_seen: <main SHA or common-surface revision>
frontier: <bounded mathematical question>
owned_assets: <theorem/docs/code/tests/Lean/lineage created or changed by this owner>
hard_block: NONE | <explicit HARD_BLOCK>
```

The owner may continue research while `main` advances elsewhere.

If a newly canonical result matters, consume that theorem semantically. Do not import every unrelated file that happened to enter `main` beside it.

## 3. Promotion protocol

Canonical promotion is a separate L4 operation.

For a validated owner payload:

1. freeze the exact source commit/blobs/theorem statements;
2. create a **new L4 integration branch from then-current `main`**;
3. replay only the owner-owned payload plus required canonical registration/provenance updates;
4. declare `NO NEW MATHEMATICS` on the integration PR;
5. run the applicable final combination gates on that exact integration state;
6. merge the L4 branch to `main`;
7. leave the owner/source history intact for provenance;
8. if the research line continues, start the next owner generation from the appropriate fresh canonical state or from a deliberately recorded owner dependency—not by periodically syncing the previous owner with all of `main`.

This makes final-state compatibility the requirement while preventing continuous integration livelock.

## 4. Scope purity

Every L1/L2/L3 owner has a theorem home. Its PR/change surface should contain only:

- owner mathematics;
- owner-specific tests/formalization/prose/provenance;
- minimal explicit dependency changes genuinely required by that owner.

A branch has **scope drift** when its changed-file surface contains unrelated theorem homes merely because another branch or `main` was synchronized into it.

Examples of scope drift include:

- A3 relation-state PR suddenly carrying P017 Legendre supplements;
- A4 correspondence PR carrying A2 quotient formalization;
- A2 generic quotient PR carrying P024/E001 material-specialization code;
- an L4 lifecycle-tooling PR carrying any new mathematical theorem family.

Scope drift is a governance defect even when every imported theorem is correct.

## 5. Recovery from scope drift

Recovery is non-destructive:

1. preserve every existing commit as provenance;
2. identify the intended owner-local asset set;
3. construct the current branch tree from the proper canonical base plus only those owner-local assets;
4. create a new descendant commit that restores scope purity;
5. never force-delete or pretend the polluted history did not happen;
6. ensure any off-owner asset still has its real owner/source route before removal from the current tree.

The goal is semantic ownership clarity, not history rewriting.

## 6. Bridges

L3 bridges obey the same isolation rule.

A bridge may depend on two owners, but it may contain only the theorem(s) whose weakest hypotheses genuinely mention both endpoint structures. It must not synchronize either owner's whole tree.

If a bridge result becomes independent of one endpoint, rehome it to the appropriate L1/L2 owner.

## 7. Integration branches

L4 is stricter than owners:

- must start from latest `main` at promotion time;
- must state `NO NEW MATHEMATICS`;
- must contain only replay/registration/conflict-resolution work;
- must not become a temporary omnibus branch for several owner payloads unless the integration is explicitly a reviewed multi-owner release and every payload was already independently validated;
- normally exits immediately after merge.

An L4 branch that accumulates owner mathematics is invalid and must be reduced back to transport-only scope before merge.

## 8. Scope-drift audit

Branch governance tooling should eventually report two independent dimensions:

1. **ancestry state** — ahead/behind, absorbed/replay-required, semantic override;
2. **scope state** — whether changed files remain within the declared owner/integration asset set.

`ahead/behind` cannot detect scope drift. A branch can be close to `main` and still mix five theorem homes.

Recommended machine-readable owner metadata:

```json
{
  "owner": "A3_STRUCTURED_RELATION_STATE",
  "allowed_assets": [
    "src/enterprise_math/weighted_relation_field.py",
    "src/enterprise_math/relation_lattice.py"
  ],
  "allowed_prefixes": [],
  "forbidden_owner_classes": ["P017", "A4", "P021"]
}
```

Exact schemas may evolve; the semantic invariant does not.

## 9. Relationship to other canonical governance

This contract complements:

- `RESEARCH_ARCHITECTURE`: unique mathematical ownership;
- `RESEARCH_BRANCH_LIFECYCLE`: L0–L5 lifecycle;
- `RESEARCH_SCHEDULING_PROTOCOL`: parallel research, serialized canonical promotion;
- `RESEARCH_COMMON_SURFACE`: shared knowledge without whole-repository synchronization.

Together they imply:

> **Share knowledge globally, isolate research ownership locally, replay canonically only at the integration boundary.**

## 10. Migration evidence

This rule was added after live Architecture-v2 migration repeatedly reproduced the same defect on otherwise clean branches: A2, A3, A4 and the lifecycle-auditor integration each acquired unrelated P017/P024/material/core assets through whole-tree synchronization. Restoring the intended tree removed no mathematical provenance but dramatically reduced each PR's semantic surface.

This operational evidence is governance provenance, not a mathematical theorem.
