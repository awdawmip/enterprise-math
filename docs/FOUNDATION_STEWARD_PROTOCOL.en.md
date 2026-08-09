# Enterprise Math Foundation Steward Protocol

Status: `ACTIVE / P0 MAINTENANCE CONTRACT`  
Effective: 2026-08-09  
Foundation problem set: GitHub Issue #164

## 1. Role

Enterprise Math maintains one dedicated **foundation steward** for the common bottom layer of the project.

The steward is responsible for maintaining and verifying:

- mathematical language, terminology and notation;
- primitive definitions and domain/type/scale conventions;
- formula statements and cross-document formula consistency;
- theorem statements, hypotheses, status labels and canonical ownership pointers;
- prose ↔ executable specification ↔ test ↔ Lean consistency;
- the project-wide shared theorem/tool surface;
- reusable Python/Lean/reference tools and their declared scope;
- cross-route foundational invariants and boundary language;
- canonical routing needed so every research route can discover proved results and tools;
- **active research-to-foundation backflow: extracting verified reusable tools, minimal state requirements, minimal repairs, repeated mechanisms and negative boundaries from existing research and using them to pressure-test the common foundation.**

The steward is a **maintainer and verifier**, not another competing research route.

## 2. Primary operating distinction

The steward performs maintenance work directly when the answer is mechanically or already mathematically determined by established canonical evidence.

Examples:

- spelling/formatting/bilingual synchronization;
- broken references;
- an obviously stale status pointer after an already-canonical merge;
- exact formula transcription errors where the intended theorem is unambiguous from proof/Lean/source;
- registering an already-canonical tool in the shared surface;
- removing ambiguous wording when no mathematical choice is involved.

But when maintenance or research backflow exposes a genuine unresolved mathematical choice, contradiction risk, missing hypothesis, cross-route incompatibility, new structural pattern, prior-art uncertainty, or tool/theorem sufficiency question, the steward **must not become the primary investigator**.

Instead:

1. verify that the concern is real enough to deserve research attention;
2. minimize the statement and separate verified facts from unknowns;
3. record exact evidence and affected surfaces;
4. post it to Foundation Problem Set Issue #164 using an `FQ-*` ID;
5. stop researching that item and return to foundation maintenance;
6. later verify researcher results before canonicalizing any resulting change.

## 3. Verification threshold before escalation

The steward must not flood the problem set with first impressions.

Before opening an `FQ-*` item, check the relevant subset of:

- `docs/FOUNDATIONS.*`;
- `docs/THEOREMS.*` and `docs/PROBLEM_STATUS.*`;
- the exact canonical P/E theorem/result documents;
- `docs/RESEARCH_COMMON_SURFACE.*`;
- Research Relay Issue #82;
- Python reference implementation and tests;
- imported Lean statements when formalization is relevant;
- source commit/PR provenance;
- prior-art/lineage records when the concern is novelty or theorem ownership.

The verification goal is not to solve the research problem. It is to establish that the discrepancy/question survives basic reconciliation.

## 4. Foundation surfaces under stewardship

### 4.1 Language and notation

Maintain one coherent meaning for recurring terms and symbols. Important examples include:

- state-space notation (`N_0`, positive naturals, signed states);
- exponent/domain conventions;
- time/iteration indexing;
- scale/precision/resolution vocabulary;
- quotient, collapse, projection, observation, kernel, relation, support, witness and state terminology;
- the distinction between representation precision and future-safe precision;
- the distinction between mathematical definitions/results and physical/ontological hypotheses.

If two existing canonical uses cannot be reconciled without a mathematical choice, escalate to #164 rather than choosing silently.

### 4.2 Formula integrity

For a formula to be canonical, the steward checks as applicable:

- domain and codomain;
- parameter ranges;
- quantifier scope;
- index origin and endpoint conventions;
- integer/floor/quotient semantics;
- scale units and typed-state interpretation;
- whether equality, equivalence, inclusion or implication is intended;
- whether a claimed inverse/factorization/composition law is one-sided or two-sided;
- whether a formula is theorem, definition, specialization, diagnostic, conjecture or physical hypothesis.

### 4.3 Theorem integrity

The steward maintains the boundary among:

- `CANONICAL_MAIN`;
- `LEAN_CHECKED_MAIN`;
- `PROVED_WIP_RELAY`;
- `EXECUTABLE_CHECKED`;
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`;
- `CONJECTURAL`.

A theorem statement should have a discoverable path from common surface → status/router → exact statement/proof provenance → executable/Lean assets when present.

The steward may repair presentation/status drift, but any disputed theorem scope or missing mathematical argument is escalated to #164.

### 4.4 Tool integrity

Reusable tools are project-wide assets rather than property of the branch that discovered them.

The steward maintains a map from mathematical role to available tool families under:

- `src/enterprise_math/`;
- `EnterpriseMath/` and `EnterpriseMath.lean`;
- `tests/`;
- `experiments/`;
- repository validation tools.

Before accepting a new shared tool, check:

- what exact mathematical object it represents;
- input/output domain and precision semantics;
- whether it is oracle, executable specification, heuristic, benchmark or production implementation;
- tests/counterexamples;
- theorem/status provenance;
- overlap with existing tools;
- whether its name/API claims more than the proved scope.

Research-level uncertainty about tool sufficiency or equivalence is sent to #164.

### 4.5 Research-to-foundation backflow integrity

Existing research routes are also pressure tests of the foundation. The steward must not only route foundation knowledge outward; the steward must also inspect mature cross-route results for structures that should change the common bottom layer.

The preferred extraction targets are:

1. **minimal sufficient state** — the weakest state object actually required by a theorem or exact computation;
2. **minimal repair / extension data** — the least carry, remainder, witness, history, relation coordinate, or other detail needed when a quotient/collapse loses the declared closure property;
3. **cross-route invariant** — the same structural law recurring independently in different mathematical or engineering routes;
4. **negative boundary** — a reusable counterexample, no-go theorem, or precise failure of an attractive generalization;
5. **reusable tool** — an exact oracle, executable specification, Lean interface, counterexample generator, or finite compiler useful outside its source route;
6. **layering law** — evidence that one object should be primitive while another is only a coordinate, observation, response law, or application semantics.

A potential backflow result should be compressed into a **Foundation Feedback Packet** containing, when applicable:

- `candidate_object_or_tool`;
- `weakest_scope_hypotheses`;
- `minimal_state`;
- `minimal_repair_or_extension`;
- `negative_boundary`;
- `cross_route_evidence`;
- `proof_status`;
- `tool_surface`;
- `prior_art_and_owner`;
- `foundation_destination`.

This packet is a compression format, not a new global barrier. A route does not wait for steward acknowledgement unless a separately valid `HARD_BLOCK` exists.

Every backflow candidate is classified into exactly one handling class:

- `DIRECT_FOUNDATION_MAINTENANCE` — existing canonical evidence already determines the change, so the steward may repair language, interfaces, routing, or an omitted proved layering directly;
- `FOUNDATION_QUESTION` — the candidate could change primitives, layering, theorem interfaces, or a cross-route mother structure but still requires real research; create an `FQ-*` entry in #164 and hand it off;
- `APPLICATION_LOCAL_OR_NOT_READY` — the candidate remains route-specific, testing/conjectural, tied to a special physical response law, or lacks cross-route necessity; keep it above the foundation.

A useful application result is therefore **not** promoted merely because it is elegant. In particular, WIP structures, physical interpretations, or one-route response rules remain outside the canonical foundation until their required proof/status boundary is satisfied.

## 5. P0 Foundation Problem Set

Canonical escalation surface: **GitHub Issue #164 — `[P0] Foundation Steward Problem Set`**.

Each finding receives a stable `FQ-YYYYMMDD-NNN` ID with:

- priority;
- status;
- kind;
- minimal statement;
- evidence;
- verified-so-far boundary;
- unknowns;
- affected routes/surfaces;
- risk/value;
- constraints;
- suggested research owner;
- resolution bar.

Priority classes:

- `P0-C` — contradiction/unsoundness risk;
- `P0-I` — foundational interface/invariant risk;
- `P1-R` — high-value research lead;
- `P2-A` — important audit/debt.

The queue is high priority but is **not a global stop barrier**. Research scheduling still follows `RESEARCH_SCHEDULING_PROTOCOL`; only a complete explicit `HARD_BLOCK` can stop a route.

## 6. Research handoff and return path

Researchers claim an `FQ-*` item in #164 and investigate on an appropriate L1/L2/L3 route.

A returned answer should include:

- proof, counterexample, or exact tool evidence;
- weakest scope/hypotheses;
- source branch/commit/PR;
- relation to existing theorem families;
- prior-art boundary when relevant;
- explicit recommendation for canonical language/formula/tool changes.

The steward then verifies the answer independently enough to decide whether to:

- canonicalize a maintenance change;
- request a narrower proof/scope;
- mark the issue rejected;
- keep it open;
- relay reusable results through Issue #82.

The steward does not treat a researcher's assertion as canonical merely because it answers an `FQ-*` item.

## 7. Continuous maintenance loop

The steady-state loop is:

`shared-surface preflight -> cross-route result extraction -> foundation-candidate classification -> mechanical maintenance OR FQ escalation -> researcher investigation -> steward verification -> canonical language/formula/theorem/tool update -> common-surface propagation -> later research pressure-tests the revised foundation`.

The desired outcome is that every research route can rely on a stable common mathematical language, discover the strongest currently justified theorem/tool interface, and return reusable structural discoveries to the bottom layer without requiring the steward to conduct the research itself.