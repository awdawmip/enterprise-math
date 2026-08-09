# Enterprise Math Common Research Surface

Status: `ACTIVE / REQUIRED PREFLIGHT`  
Effective: 2026-08-09  
Purpose: give every research route the same compact view of reusable proved mathematics, executable tools, negative boundaries, and live cross-route results before it starts a new theorem line.

This file is a router, not a replacement for proofs. Exact statements remain in their canonical theorem/problem documents or, for not-yet-canonical branch results, in the Research Relay with source commit provenance.

## 1. Mandatory preflight for every L1/L2/L3 research route

Before starting a new theorem line:

1. read this common surface;
2. read `docs/RESEARCH_SCHEDULING_PROTOCOL.*`;
3. read `docs/PROBLEM_STATUS.*` and the canonical result document for the relevant problem;
4. search the latest relevant entries in Research Relay Issue #82;
5. inspect the relevant executable specification/tests or Lean module when the proposed result overlaps an existing tool/theorem family;
6. only then decide whether the next step is a new mother theorem, specialization, bridge, counterexample, or duplicate.

Do not inject the whole repository into working context. The point is shared awareness plus selective retrieval.

## 2. Status classes

Every reusable result encountered through this surface belongs to one of these classes:

- `CANONICAL_MAIN`: proved result integrated on `main`; safe for all routes to consume at its stated scope.
- `LEAN_CHECKED_MAIN`: canonical result also checked by the imported Lean build.
- `PROVED_WIP_RELAY`: proved on a research branch and relayed with source commit, but not yet canonical; may be used explicitly as branch/WIP input, never silently promoted to main truth.
- `EXECUTABLE_CHECKED`: supported by exact finite/reference checks but not a substitute for proof.
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`: reusable impossibility or failure result; must be shared with the same priority as a positive theorem.
- `CONJECTURAL`: research target only.

## 3. Canonical theorem knowledge channels

All routes should know that canonical proved mathematics is not confined to `docs/THEOREMS.*`.

### Base theorem catalogue

- `docs/THEOREMS.en.md` / `docs/THEOREMS.zh-CN.md`: compact proved propositions from the original core.
- `docs/PROBLEM_STATUS.en.md` / `docs/PROBLEM_STATUS.zh-CN.md`: authoritative numbered-problem status and canonical result pointers.
- the canonical `docs/Pxxx_*.{en,zh-CN}.md` files named by `PROBLEM_STATUS`: exact modern theorem families and scope.
- `EnterpriseMath.lean` plus imported `EnterpriseMath/**.lean`: Lean-checked subset.

### Live proved-but-not-yet-canonical channel

- Research Relay Issue #82: exact cross-route theorem/counterexample statements with source branch/commit, weakest hypotheses, relation class, and requested action.

A route must never infer “unknown” merely because a result is absent from its own branch.

## 4. Shared reusable theorem families

This list is intentionally at theorem-family granularity. Use the referenced canonical documents for exact hypotheses and numbering.

### A0 — primitive discrete state algebra

Reusable tools/results include:

- integer roots and exact perfect-power collapse;
- basin characterization/cardinality and collapse gap coordinates;
- root exponent composition and commutation;
- quotient/remainder versus multiple-collapse semantics;
- total scale-factor algebra, divisibility projection, gcd/lcm scale lattice, path independence and nonunique inverse refinement;
- signed-state distinctions;
- typed strict-rank descent;
- order-adjoint/right-adjoint formulations and reductive idempotent collapse.

Primary canonical entry points: P001–P009 result docs and `docs/THEOREMS.*`.

### A1 — dynamics, kernels, collision and stabilization

Reusable tools/results include:

- deterministic history merging: merged states never split under the same later deterministic composition;
- exact collision/fiber multiplicity observables and collision spectra;
- finite/eventual coalescence structures;
- monotone reductive stabilization on well-founded orders;
- stable collapse-word behavior and lcm fixed-point structure.

Primary canonical entry points: P010, P011, P019, P020.

### A2 — observation and future-compatible quotient

Reusable tools/results include:

- factorization through a quotient iff the required observable/operation is constant on quotient fibers;
- coarsest exact repair/refinement for a declared future task;
- finite predictive/future-signature refinement and stabilization;
- finite operation-family compatibility and operation-word semantics;
- exact quotient/multiple-collapse compatibility and minimal boundary-bit repairs in arithmetic specializations;
- task-relative precision: there is no universal scalar precision independent of the future language.

Primary canonical entry points: P018 precision-state results, P023 and its canonical supplements, P024 specializations. Branch extensions are routed through Relay #82.

### A3 — structured relation-state algebra

Shared WIP/core concepts include the integer weighted relation field

`Z_ij = m_j*c_i - m_i*c_j`,

partition coarsening `Z' = A Z A^T`, partition kernels, integer relation scale/rank, refinement memory and task-derived exact relation precision.

Until canonical replay completes, consume A3 results with their explicit `PROVED_WIP_RELAY`/branch provenance rather than pretending they are main theorems.

### A4 — admissible support / correspondence algebra

Shared WIP/core concepts include finite multivalued relations, relation composition/converse, common-target structure, radius-indexed supports, split-completeness boundaries, MAY/MUST semantics, witness/group spectra, and degeneration to P011 on total-function graphs.

Again, distinguish WIP proved results from canonical-main results.

### A5 — intrinsic discrete geometry

Reusable canonical and WIP tools include primitive adjacency, graph distance, finite balls/shells, lattice/root-lattice candidates, radial/quadratic observations, distance carry and geometry-specific contraction. P012 gives the canonical metric foundation; broader P022 geometry remains active.

## 5. High-value cross-route negative boundaries everyone must know

- Coarse equality/support/cardinality does not automatically preserve later composition; future sufficiency must be proved for the declared operation language.
- A3 signed relation information can cancel under quotient, so coarse support does not certify universal fine support.
- Pairwise/common-target cardinality shadows can lose witness identity needed for multi-step composition.
- A geometry-only collision fact may be insufficient to select a unique response; additional action/material/symmetry-breaking state may be required.
- A safe quotient for one observable can fail for a richer future language.
- File-name equality, branch ancestry, or `ahead(main)>0` is not proof of new mathematical content; semantic identity controls replay.
- Established general machinery (Galois connections, semigroups, numerical semigroups, partition refinement, etc.) remains prior art even when used inside Enterprise Math.

## 6. Shared executable tool surface

All routes may reuse canonical executable assets; they are not owned by the branch where they were first discovered.

### Python exact/reference tools

Root: `src/enterprise_math/`

Important families include:

- `core.py`, `division.py`, `scale_algebra.py`, `signed.py`, `typed_scale.py`, `geometry.py` — A0/A5 primitive tools;
- `composition_safe_collapse.py` and predictive/future-signature modules — A2 quotient-safety tools;
- `action_language_precision.py`, clearance/guard/boundary precision modules — P024/A2 specializations;
- P017 mirror/cofactor/Legendre modules — square-basin pressure-test tools;
- relation/support modules when and where they are canonical or explicitly consumed from a WIP owner.

`src/enterprise_math/__init__.py` exports only a compact stable subset; non-exported modules may still be legitimate internal executable specifications. Check their theorem/provenance status before treating them as canonical APIs.

### Lean tools

- `EnterpriseMath.lean` is the root import surface.
- `EnterpriseMath/**.lean` contains the formalized subset.
- “Lean-checked” may be claimed only when the module is imported by the root build or otherwise explicitly covered by the repository's warning-fatal formalization gate.

### Tests and reconstruction tools

- `tests/`: exact regression/counterexample suites;
- `experiments/`: bounded pressure tests and engineering probes;
- `tools/check_bilingual_pairs.py`: bilingual-pair gate;
- `tools/check_references.py`: reference-integrity gate.

Executable checks support proof discovery, falsification and regression. They do not by themselves upgrade a statement from `EXECUTABLE_CHECKED` to `PROVED`.

## 7. Shared knowledge propagation rule

When any route proves or finds something reusable:

1. relay it immediately if another active route may benefit;
2. label the downstream action `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
3. identify the mother-theorem owner and relation class;
4. if it enters canonical `main`, ensure `PROBLEM_STATUS`, the canonical theorem/result doc, lineage/prior-art, and this common surface are sufficient for future routes to discover it;
5. if it creates a reusable executable method/tool, register the canonical module/tool family here at the next common-surface update;
6. do not wait for every consumer to acknowledge it.

## 8. Nonblocking rule

Knowledge sharing increases parallelism; it must never create a global barrier.

A route that discovers an upstream theorem should consume it and continue. A route that discovers an upstream gap should isolate the exact missing lemma and continue elsewhere unless it can honestly record a `HARD_BLOCK` under `RESEARCH_SCHEDULING_PROTOCOL`.