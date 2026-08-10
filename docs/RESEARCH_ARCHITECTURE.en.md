# Enterprise Math Research Architecture v2

Status: `ACTIVE / CANONICAL ARCHITECTURE CONTRACT`  
Effective: 2026-08-09  
Stabilized: 2026-08-10

This document defines the stable research architecture. It is **not** a live branch inventory, migration dashboard, scheduler snapshot, or current-PR list. Live executor assignment and current branch/runtime state belong to the scheduling/owner-control surfaces only when the current action actually needs them. Historical branch ledgers and migration classifications remain provenance/snapshots, not live authority.

Where a migration-era example or older wording conflicts with later canonical owner-isolation, scheduling, or GitHub-liveness contracts, the later narrow contract controls its domain.

## 1. Two-axis architecture

Enterprise Math uses two independent but consistent organizational axes:

1. **Mathematical ownership A0–A5** — who maintains the most general proved statement;
2. **Git lifecycle L0–L5** — where current work happens and when a branch leaves the active surface.

P/E identifiers remain research-program and provenance identities; they are not permanent homes for every mother theorem discovered there.

Governing rule:

> Preserve discovery provenance forever; maintain the most general proved statement once; treat branches as short-lived working pointers.

Vocabulary similarity is never enough to unify structures. Ownership changes require an explicit relationship classification: `same / strict generalization / specialization / independent / conflict`.

---

## 2. Mathematical ownership axis

### A0 — Primitive Discrete State Algebra

Primary sources: P001–P009.

Objects include integer roots, perfect-power collapse, exact quotient/remainder, signed-state distinctions, total scale factors, typed transitions, order adjunctions, composition, commutation, and fixed points.

Many A0 results are already canonical on main. Exact resolved scope remains controlled by `PROBLEM_STATUS`.

### A1 — Functional Dynamics / Kernel / Stabilization

Primary sources: P010, P011, canonical P019, P020, with links to P018.

Objects include deterministic functions, functional kernels/fibers, strict history merge, collision spectra, eventual coalescence, and finite stabilization. The project-wide generic functional-kernel / declared-future-signature language is canonicalized in `FOUNDATIONS` through FQ-004.

A function graph may later be recognized as a special case of a broader relation theory, but A1 remains the canonical home for the single-valued theory.

### A2 — Observation / Future-Compatible Quotient

Primary sources: P018 and P023, with applications in E001/E002/P017/P021.

Objects include:

- observation equivalence;
- operation factorization / congruence;
- finite predictive/contextual closure;
- minimum exact repair;
- reusable interface;
- future-language sufficiency;
- exact bounded future-action language results such as the canonical P018↔P023 quotient-root power-free action basis.

Ownership discipline:

- **P023/core A2** is the candidate owner for the most general operation-language/future-compatible quotient mother theorems;
- **P018** keeps precision-specific interpretation, defect/response, context depth, transport, and arithmetic instances;
- E/P applications keep domain specializations only.

### A3 — Structured Relation-State Algebra

Historical source: `research/core/relation-quotient`; current reusable executable assets are routed through `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json`.

The core object is a structured weighted integer state, for example

`Z_ij = m_j c_i - m_i c_j`,

not an arbitrary binary relation.

The first canonical executable core is already on `main` (`weighted_relation_field.py`, `relation_lattice.py`, `relation_scale.py`). Broader candidate theorem families include partition quotient, kernel, relation rank/scale, guard-image lattice, refinement memory, and task-derived exact relation precision. Each theorem keeps its actual canonical/WIP status; executable presence does not upgrade an unpromoted theorem.

A3 receives no new P number yet and is not a Foundation. Further reusable mathematics must be stated under weakest proved hypotheses and audited against prior art before canonical promotion.

### A4 — Admissible Support / Correspondence Algebra

Historical source: E001 relational-collapse work and its admissible-support continuation; the first canonical executable core is already on `main` (`admissible_support.py`, `relational_spectrum.py`).

Core object: a finite multivalued correspondence `R ⊆ X×Y`.

Candidate theorem families include:

- functional versus relational collapse;
- admissible support families;
- relation composition/common targets;
- split-completeness boundaries;
- MAY/MUST support semantics;
- witness/event spectra;
- exact degeneration back to P011 on total-function graphs.

A4 and A3 remain sibling cores. Sharing the word “relation” is not evidence of mathematical identity. Canonical executable assets are reusable immediately; broader theorem statements retain their own proof/promotion status.

### A3↔A4 Bridge

Only statements of the following form belong to the bridge:

- conditions under which an A3 state generates an A4 support family;
- conditions under which an A4 observable factors through an A3 quotient;
- A3 internal relations that must be retained for a declared A4 future query;
- counterexamples proving strict non-equivalence.

The first executable bridge slice `a3_a4_support_bridge.py` is canonical on `main`. That does not collapse A3 and A4 into one owner or promote every historical bridge theorem. If a bridge theorem becomes generally reusable independently of the two endpoint semantics, it must move up to an explicit core owner.

### A5 — Intrinsic Discrete Geometry

Primary sources: P012 and P022.

Objects include primitive adjacency, integer shortest-path metrics, lattice/root-lattice models, balls/shells, radial/quadratic observations, distance carry, and geometry-specific contraction.

Preferred dependency direction:

`primitive geometry -> admissible supports -> observations -> future-compatible precision -> application decision`.

Geometry may consume A2/A3/A4. Generic relation algebra must not remain trapped inside P022 merely because it was discovered on a geometry branch.

---

## 3. Program / Application axis

Representative program/application identities include:

- P017 — Legendre / consecutive-square pressure test;
- P018 — finite precision calculus;
- P021 — causal horizon / focusing;
- P022 — minimum-precision geometry;
- P023 — composition-safe / future-compatible quotient;
- E001 — collision/material engineering probes;
- E002 — precision-native control / actuation / task observables;
- P016 — physical falsification contract.

Programs may discover mother theorems, but reusable mathematics must be lifted to the appropriate A0–A5 owner. Program branches retain specializations, experimental semantics, counterexamples, benchmarks, and provenance.

---

## 4. Confirmed cross-route ownership

### P017 → P018/A2

Square-basin quotient/root transport that no longer needs a prime hypothesis belongs in the precision/quotient layer; P017 keeps least-factor and lower-band applications.

### P018 ↔ P023

Unary predictive closure and operation-family quotient safety are different scopes of the same mother problem. General operation-language closure should be maintained once; P018 keeps precision interpretation and defect/transport consequences. The bounded quotient-root power-free action basis is a canonical shared specialization and must remain discoverable to both routes.

### P021 → A2 / witness algebra

Direction transport showed that cardinality shadows do not automatically preserve future composability. The general rule “discard witness identity only after proving future compositional sufficiency” should not become a second general theory inside P021.

### P011 → A4

Multivalued support may generalize collision/witness spectra, but total-function graphs must explicitly degenerate back to P011, and single-valued monotonicity must not be imported when it fails for relations.

### E001/E002 → A2

Contact/action-family/gcd/semigroup results that are really future-language minimal-quotient theorems belong in A2/P023. Contact/material/collision specializations remain engineering-owned. Canonical E001 executable specializations may still be shared as pressure tests/tools without becoming universal physical laws.

### P022 ↔ A3/A4/A2

Geometry-only results remain P022. Structured relation-state mathematics moves to A3; support/correspondence moves to A4; future-safe erasure conditions move to A2.

---

## 5. Theorem lifting protocol

When a program or bridge discovers reusable mathematics:

1. freeze the exact source branch/commit/result payload and provenance;
2. remove domain assumptions one by one to identify weakest proved hypotheses;
3. search lineage, Relay, common surface, and existing theorem families as required by the concrete ownership question;
4. classify the relation as `same / strict generalization / specialization / independent / conflict`;
5. choose exactly one mother-statement owner;
6. keep a corollary plus provenance in the source program;
7. when promotion begins, create or reconcile one L4 integration against a current `main` snapshot while keeping the frozen source-result identity;
8. replay theorem, implementation, tests, Lean, bilingual prose, lineage, prior-art, and the shared theorem/tool surface;
9. if `main` advances during validation, inspect only the actual intervening delta; unrelated movement does not generate a new replay generation;
10. pass repository gates, including the shared-surface integrity gate where applicable, then perform one final current-main combination gate and merge;
11. move historical branches to `ABSORBED/PROVENANCE` according to the lifecycle contract.

Highly diverged mathematical ownership is never resolved merely by merge or rebase. Canonical promotion is incomplete if a reusable result enters `main` but cannot be discovered through `docs/RESEARCH_COMMON_SURFACE.*` / `research_common_surface.json`.

Remote reads/writes used by this protocol remain subject to `docs/GITHUB_INTERACTION_BUDGET.md`; theorem lifting does not create a standing requirement to poll, chase moving `main`, or keep owner branches continuously synchronized.

---

## 6. Binding to Git lifecycle and live control surfaces

Mathematical ownership and branch lifecycle must agree:

- canonical A0/A1 results normally live directly on main;
- active A2/A3/A4/A5 mother theorems live on L1 core-owner branches;
- P/E frontiers live on L2 program-owner branches;
- bridge theorems live on L3;
- promotion to main goes only through one-shot L4 canonical integration;
- historical branches/PRs/checkpoints end in L5.

Stable lifecycle semantics, thresholds, and naming are defined in `RESEARCH_BRANCH_LIFECYCLE.*`. Live executor/frontier assignment is governed by `RESEARCH_SCHEDULING_PROTOCOL.*` and its current owner/scheduler/runtime surfaces only when dispatch state is materially needed. Owner isolation is governed by `RESEARCH_OWNER_ISOLATION.*`; remote interaction by `GITHUB_INTERACTION_BUDGET.md`.

`RESEARCH_BRANCH_LEDGER.*` and migration-era branch classifications are historical snapshots/provenance. They MUST NOT be treated as live executor assignment, a startup gate, or authority that can freeze a current L1/L2/L3 frontier.

---

## 7. Migration provenance, not live routing

Architecture v2 was introduced through a one-time migration that froze several highly diverged historical trees and replayed selected payloads into new owner/integration lines. Those exact 2026-08-09 classifications remain recoverable from Git history, PRs, branch ledgers, and migration/stall-audit records.

They are intentionally **not embedded here as current branch truth**.

A historical `REPLAY_REQUIRED`, `FROZEN`, `ABSORBED`, or similar classification constrains the identified historical tree and preserves provenance. It does not by itself classify the current owner generation, block new mathematics, require current-main reconciliation, or require waiting for another PR.

When a current branch classification is actually needed for promotion, cleanup, or scope-drift recovery, perform the bounded semantic/lifecycle check required by the current action. Do not run a repository-wide branch census merely to begin research.

---

## 8. Research Relay

Cross-route reusable theorems, strict generalizations, important counterexamples, and new precision obligations continue through the Research Relay.

Relay is a discovery/consumption bus, not a theorem owner and not canonical truth by itself.

Each reusable theorem should record at least:

- source commit;
- exact statement;
- weakest known hypotheses;
- relationship class;
- intended owner;
- affected consumers;
- requested downstream action.

Canonical promotion must then move reusable results from Relay-only discoverability into the common human/machine surface.

---

## 9. Compression success criteria

A researcher entering the repository should quickly determine:

1. the current canonical main when current-main identity is actually material;
2. which P/E programs are active for the selected task;
3. which A-layer owner maintains each general theorem family;
4. that the long-lived writable surface remains intentionally small; the historical 8–12 target is a compression heuristic, not a startup, dispatch, or cleanup gate;
5. why an integration/agent branch exists and when it exits;
6. how historical results are recovered from PR/tag/lineage;
7. where every canonical reusable theorem, root formalization, tool family, negative boundary, and active foundation alert is discoverable.

If a result can only be found by remembering a 300-commit historical branch or a past Relay comment, the architecture is not yet compressed enough. If research must wait for a ledger refresh, branch census, CI status, replay queue, or moving-main synchronization before a mathematically independent next step, the architecture has regressed.
