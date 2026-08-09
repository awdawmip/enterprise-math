# Enterprise Math Research Architecture v2

Status: `PROPOSED / MIGRATION IN PROGRESS`  
Baseline: `main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
Date: 2026-08-09

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

Objects include deterministic functions, fibers/kernels, strict history merge, collision spectra, eventual coalescence, and finite stabilization.

A function graph may later be recognized as a special case of a broader relation theory, but A1 remains the canonical home for the single-valued theory.

### A2 — Observation / Future-Compatible Quotient

Primary sources: P018 and P023, with applications in E001/E002/P017/P021.

Objects include:

- observation equivalence;
- operation factorization / congruence;
- finite predictive/contextual closure;
- minimum exact repair;
- reusable interface;
- future-language sufficiency.

Ownership discipline:

- **P023/core A2** is the candidate owner for the most general operation-language/future-compatible quotient mother theorems;
- **P018** keeps precision-specific interpretation, defect/response, context depth, transport, and arithmetic instances;
- E/P applications keep domain specializations only.

### A3 — Structured Relation-State Algebra

Historical source: `research/core/relation-quotient`.

The core object is a structured weighted integer state, for example

`Z_ij = m_j c_i - m_i c_j`,

not an arbitrary binary relation.

Candidate contents include partition quotient, kernel, relation rank/scale, guard-image lattice, refinement memory, and task-derived exact relation precision.

A3 receives no new P number yet and is not a Foundation. It must first be cleanly replayed, audited against prior art, and stated under weakest proved hypotheses.

### A4 — Admissible Support / Correspondence Algebra

Historical source: E001 relational-collapse work and its admissible-support continuation.

Core object: a finite multivalued correspondence `R ⊆ X×Y`.

Candidate contents include:

- functional versus relational collapse;
- admissible support families;
- relation composition/common targets;
- split-completeness boundaries;
- MAY/MUST support semantics;
- witness/event spectra;
- exact degeneration back to P011 on total-function graphs.

A4 and A3 remain sibling cores. Sharing the word “relation” is not evidence of mathematical identity.

### A3↔A4 Bridge

Only statements of the following form belong to the bridge:

- conditions under which an A3 state generates an A4 support family;
- conditions under which an A4 observable factors through an A3 quotient;
- A3 internal relations that must be retained for a declared A4 future query;
- counterexamples proving strict non-equivalence.

If a bridge theorem becomes generally reusable independently of the two endpoint semantics, it must move up to an explicit core owner.

### A5 — Intrinsic Discrete Geometry

Primary sources: P012 and P022.

Objects include primitive adjacency, integer shortest-path metrics, lattice/root-lattice models, balls/shells, radial/quadratic observations, distance carry, and geometry-specific contraction.

Preferred dependency direction:

`primitive geometry -> admissible supports -> observations -> future-compatible precision -> application decision`.

Geometry may consume A2/A3/A4. Generic relation algebra must not remain trapped inside P022 merely because it was discovered on a geometry branch.

---

## 3. Program / Application axis

Current major programs include:

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

Unary predictive closure and operation-family quotient safety are different scopes of the same mother problem. General operation-language closure should be maintained once; P018 keeps precision interpretation and defect/transport consequences.

### P021 → A2 / witness algebra

Direction transport showed that cardinality shadows do not automatically preserve future composability. The general rule “discard witness identity only after proving future compositional sufficiency” should not become a second general theory inside P021.

### P011 → A4

Multivalued support may generalize collision/witness spectra, but total-function graphs must explicitly degenerate back to P011, and single-valued monotonicity must not be imported when it fails for relations.

### E001/E002 → A2

Contact/action-family/gcd/semigroup results that are really future-language minimal-quotient theorems belong in A2/P023. Contact/material/collision specializations remain engineering-owned.

### P022 ↔ A3/A4/A2

Geometry-only results remain P022. Structured relation-state mathematics moves to A3; support/correspondence moves to A4; future-safe erasure conditions move to A2.

---

## 5. Theorem lifting protocol

When a program or bridge discovers reusable mathematics:

1. fix the source branch and commit;
2. remove domain assumptions one by one to identify weakest proved hypotheses;
3. search lineage, Relay, and existing theorem families;
4. classify the relation as `same / strict generalization / specialization / independent / conflict`;
5. choose exactly one mother-statement owner;
6. keep a corollary plus provenance in the source program;
7. create an integration replay from **latest main**;
8. replay theorem, implementation, tests, Lean, bilingual prose, lineage, and prior-art records;
9. pass repository gates and merge to main;
10. move historical branches to `ABSORBED/PROVENANCE` according to the lifecycle contract.

Highly diverged mathematical ownership is never resolved merely by merge or rebase.

---

## 6. Binding to Git lifecycle

Mathematical ownership and branch lifecycle must agree:

- canonical A0/A1 results normally live directly on main;
- active A2/A3/A4/A5 mother theorems live on L1 core-owner branches;
- P/E frontiers live on L2 program-owner branches;
- bridge theorems live on L3;
- promotion to main goes only through L4 clean integration;
- historical branches/PRs/checkpoints end in L5.

Exact lifecycle states, thresholds, naming, and the current migration batch are defined in `RESEARCH_BRANCH_LIFECYCLE.*` and `RESEARCH_BRANCH_LEDGER.*`.

---

## 7. Trees frozen for semantic replay

The following historical trees must not be expanded by appending new theorem families:

- `agent/p018-critical-grid` / PR #68;
- `research/core/relation-quotient`;
- `research/core/relation-support-bridge` / PR #83.

They are semantic-replay sources, not future canonical owners.

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

---

## 9. Compression success criteria

A researcher entering the repository should quickly determine:

1. the current canonical main;
2. which P/E programs are active;
3. which A-layer owner maintains each general theorem family;
4. that long-lived writable branches stay near 8–12;
5. why an integration/agent branch exists and when it exits;
6. how historical results are recovered from PR/tag/lineage.

If a result can only be found by remembering a 300-commit historical branch, the architecture is not yet compressed enough.
