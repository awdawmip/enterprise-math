# Enterprise Math Research Branch Lifecycle v2

Status: `PROPOSED / EXECUTABLE MIGRATION CONTRACT`  
Candidate effective date: 2026-08-09  
Baseline: `main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`

## 1. Purpose

Enterprise Math is now a multi-researcher, multi-route program. Long-term mathematical ownership, problem/application identity, and Git history must be separated.

Core rule:

> **Long-term authority lives in `main` and an explicit theorem owner; a Git branch is a short-lived pointer between research layers.**

Discovery provenance is retained by commits, PRs, tags, and lineage records. A historical branch does not need to remain active forever.

This document complements the A0–A5 mathematical ownership axis in `RESEARCH_ARCHITECTURE` with an independent Git-lifecycle axis.

---

## 2. Six Git lifecycle layers

### L0 — Canonical Main

The only canonical integration layer is `main`.

Allowed:

- results that passed applicable repository gates;
- canonical problem/status documents;
- implementations, Lean proofs, tests, lineage, and prior-art records that all downstream work may consume;
- research results already semantically replayed from historical branches.

Forbidden:

- wholesale merges of highly diverged historical research trees;
- treating branch/PR existence alone as enough to promote a problem to `RESOLVED`.

### L1 — Core Owner

Hosts reusable mother theorems shared by multiple P/E programs.

Current candidates:

- `core/a2-future-quotient` — future-compatible quotient / factorization / congruence / minimal repair;
- `core/a3-relation-state` — structured relation state / partition quotient / kernel;
- `core/a4-admissible-support` — multivalued support/correspondence / witness algebra.

Rules:

1. A theorem family has one owner.
2. The owner uses the weakest proved hypotheses.
3. P/E programs retain specializations, applications, counterexamples, and provenance instead of duplicating the mother theorem.
4. Core owners do not own application benchmarks or physical interpretations.

### L2 — Program Owner

Hosts the current frontier of a numbered problem or engineering program.

Typical branches:

- `program/p017-legendre`;
- `program/p018-precision`;
- `program/p021-causal-focusing`;
- `program/p022-geometry`;
- `engineering/e001-collision`;
- `engineering/e001-material`;
- `engineering/e002-control` only while active.

A program may discover a mother theorem, but it must relay that theorem upward to L1 and then consume the general owner version.

### L3 — Bridge / Probe

Answers one explicit question between two owners.

Examples:

- `bridge/a3-a4-*`;
- `bridge/e001-e002-contact-*`.

A bridge must stay thin. It may own factorization/specialization/reconstruction/failure theorems linking two homes, but it must not become a second owner for either side. If a bridge result becomes generally reusable, lift it to L1. Completed or failed bridges move to L5.

### L4 — Integration Replay

A one-shot transport layer created from **latest main**.

Its only jobs are:

1. semantic replay of selected theorems;
2. canonical numbering;
3. bilingual synchronization;
4. implementation/test/Lean replay;
5. lineage/prior-art updates;
6. repository gates.

Hard rule:

> **An integration branch may not create new mathematics.**

If replay exposes a new theorem, return to the appropriate L1/L2/L3 owner first. Delete the integration branch after merge; keep the PR as history.

### L5 — Provenance / Archive

Contains:

- branches fully or semantically absorbed by main;
- superseded research branches;
- historical PRs;
- immutable checkpoint tags;
- source discovery commits.

L5 accepts no new research commits.

Prefer immutable tags over new `checkpoint/*` branches. Once an `agent/*` branch is absorbed or superseded, close the PR if applicable and delete the branch ref after provenance is recorded.

---

## 3. Required branch states

Every non-main branch must be classified as exactly one of:

### `ACTIVE_OWNER`

Unique current L1/L2 owner with unabsorbed mathematics.

### `ACTIVE_BRIDGE`

Bounded bridge question with unabsorbed results.

### `INTEGRATION`

Current-main semantic replay; no new mathematics.

### `REPLAY_REQUIRED`

Semantic audit confirms mathematics still missing from main, but the branch is highly diverged or mixes multiple owners; freeze new research and replay from latest main.

Default triggers include:

- `behind(main) >= 50` and semantic audit still finds unique assets;
- more than one theorem owner in the same branch;
- a PR too large to represent one auditable research increment;
- canonical numbering or path collisions.

### `ABSORBED`

Definition: **the branch contains no semantic asset still missing from main.**

Two common proof modes:

1. **Mechanical absorption** — `ahead(main)=0`;
2. **Semantic absorption** — `ahead(main)>0`, but branch-owned theorem/doc/implementation/test/lineage assets entered main through another replay history, and exact-blob / theorem-equivalence / strict-generalization audit shows no unique content remains.

Therefore:

> `ahead(main)=0` is sufficient but not necessary for `ABSORBED`; `ahead(main)>0` is not proof that unique mathematics remains.

Action: close/annotate the PR, retain a tag if useful, then remove the branch ref.

### `PROVENANCE`

Explicitly frozen historical branch/checkpoint; not scheduled for new research.

---

## 4. Semantic absorption audit

When `ahead(main)>0`, commit ancestry alone is not enough to decide whether replay is needed.

Audit at least:

1. whether the theorem statement already exists on main as the same statement, an equivalent coordinate form, or a strict generalization;
2. whether implementation/tests are exact blobs or explicitly superseded;
3. whether prior-art/lineage still recover discovery provenance;
4. whether a path/name was later **reused for different mathematics** — identical filenames are not absorption evidence;
5. when main contains a strict generalization, whether the source specialization still has a unique application or counterexample worth retaining.

Only branches with no unique semantic assets become `ABSORBED`.

This prevents both errors:

- replaying already-absorbed mathematics merely because Git history is different;
- deleting unique mathematics merely because a later file reused the same name/number.

---

## 5. One-way lifecycle

Recommended state flow:

`ACTIVE_OWNER / ACTIVE_BRIDGE`

→ theorem audit / relay

→ `INTEGRATION`

→ `main`

→ `ABSORBED`

→ `PROVENANCE`.

`REPLAY_REQUIRED` may spawn a clean owner or integration branch, but a historical large tree must not be made current again through repeated wholesale merges.

---

## 6. Git divergence is a governance signal, not semantic truth

- `ahead=0`: mechanical absorption; default `ABSORBED`.
- `ahead>0`: perform semantic-equivalence audit before choosing `ABSORBED` or `REPLAY_REQUIRED`.
- `ahead>0, behind<20`: if unique mathematics remains, usually suitable for a short current-main owner/replay branch.
- `ahead>0, behind>=50`: if unique mathematics remains, default `REPLAY_REQUIRED`.
- `ahead>100` or changes span multiple theorem homes: distill semantically; stop expanding the old PR.

These are Git-governance triggers, not mathematical-quality judgments.

---

## 7. Immediate classification of major current trees

### P018 `agent/p018-critical-grid`

`REPLAY_REQUIRED`.

The tree spans pair/kernel, coalescence, contextual closure, operation congruence, transport/reusable-interface, and quotient-basin work and has diverged strongly from main.

Next ownership:

- general future-compatible quotient mother theorems → A2/P023 owner;
- precision-specific state/kernel/context/transport → `program/p018-precision-v2`;
- square-basin/factor/proof specializations → P018 application layer.

Freeze PR #68 as provenance; do not append further Supplements to the historical tree.

### A3 `research/core/relation-quotient`

`REPLAY_REQUIRED`.

Next owner: `core/a3-relation-state-v2`. Replay only structured relation-state / partition quotient / kernel / guard-image mathematics. Geometry, A4 correspondence, and causal applications must be routed elsewhere.

### A3/A4 `research/core/relation-support-bridge`

`REPLAY_REQUIRED`.

Next bridge: `bridge/a3-a4-v2`, containing only true bridge theorems. Semantic-shadow/equitability/witness algebra that is independently reusable must belong to a named L1 owner instead.

### E002 v2 historical branches

Most are mechanically `ahead=0`. `task-observable-v2` still shows ahead commits, but its document/implementation/tests were verified as the same blobs already on main, so it is **semantically absorbed** rather than a replay candidate. The old E002 v2 generation should therefore move to `ABSORBED/PROVENANCE`.

---

## 8. Naming

Long-lived writable owners:

- `core/<home>`
- `program/<problem>`
- `engineering/<program>`

Temporary layers:

- `bridge/<a>-<b>-<question>`
- `integration/<scope>-<stage-or-date>`
- `agent/<task>` — short-lived executor branch, never a long-term theorem owner.

Do not create new `checkpoint/*` branches; use immutable annotated tags.

---

## 9. PR rules

- L1/L2/L3 PRs may contain new mathematics.
- L4 PRs must declare `NO NEW MATHEMATICS`.
- A PR spanning multiple theorem homes must be split or marked `REPLAY_REQUIRED`.
- `ABSORBED` PRs should not remain open merely because their history matters; the closed PR is the history.
- Stacked PR chains must remain short and temporary; no long-lived dependency DAG.

---

## 10. Target active surface

The long-lived writable set should stay near 8–12 branches:

- three core owners A2/A3/A4;
- four program owners P017/P018/P021/P022;
- E001 collision/material;
- E002 while active;
- zero to two bridges.

Integration and agent branches do not count toward the long-lived surface and must exit after completion.

---

## 11. Preservation invariant

Any cleanup must preserve the ability to answer:

1. Where was the result discovered?
2. Who owns the most general proved form now?
3. Which current owner continues the research?
4. Which programs/applications consume it?

If deleting a branch ref would make any answer unrecoverable from Git/PR/tag/lineage, record provenance first.
