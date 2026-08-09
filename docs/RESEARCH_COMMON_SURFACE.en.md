# Enterprise Math Common Research Surface

Status: `ACTIVE / REQUIRED PREFLIGHT`  
Effective: 2026-08-09  
Purpose: give every research route the same compact view of reusable mathematics, executable tools, negative boundaries, active interface alerts, dispatch state, and live cross-route results.

This file is a router, not a replacement for proofs. Exact theorem scope remains controlled by canonical result documents; branch-proved results remain explicitly WIP until promoted. Scheduler state coordinates work but does not promote mathematical truth.

## 1. Mandatory preflight

Before starting a new L1/L2/L3 theorem line:

1. read this common surface;
2. read `docs/RESEARCH_SCHEDULING_PROTOCOL.*`;
3. read `research_scheduler.json` and the live Research Dispatch Board Issue #240;
4. read `docs/RESEARCH_OWNER_ISOLATION.*`;
5. read `docs/PROBLEM_STATUS.*` and the relevant canonical result document;
6. read the latest relevant Research Relay Issue #82 entries;
7. inspect overlapping executable specs/tests and imported Lean modules;
8. for foundational language/formula/theorem/tool-interface work, read `docs/FOUNDATION_STEWARD_PROTOCOL.*` and relevant Foundation Problem Set Issue #164 `FQ-*` entries;
9. then classify the work as a mother theorem, specialization, bridge, counterexample, tool, duplicate, or answer to a foundation question.

Use selective retrieval; do not inject the whole repository into working context.

## 2. Epistemic/status discipline

Keep these distinct:

- `CANONICAL_MAIN`: proved result integrated on `main` at its stated scope;
- `LEAN_CHECKED_MAIN`: canonical result covered by the imported/warning-fatal Lean build;
- `PROVED_WIP_RELAY`: proved branch result with source provenance, not yet canonical;
- `EXECUTABLE_CHECKED`: exact executable/finite validation, not proof by itself;
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`: reusable impossibility/failure result;
- `CONJECTURAL`: research target only.

A **canonical executable asset** is a source/test artifact integrated on `main`; its presence does not by itself promote every statement encoded by that module to `PROVED`. Likewise, a scheduler claim/lease records who is working, not what has been proved.

## 3. Canonical knowledge channels

- `docs/THEOREMS.*`: compact original theorem catalogue;
- `docs/PROBLEM_STATUS.*`: authoritative numbered-problem router;
- canonical `docs/Pxxx_*.{en,zh-CN}.md`: exact modern theorem families and hypotheses;
- `EnterpriseMath.lean` plus imported `EnterpriseMath/**.lean`: Lean-checked subset;
- Research Relay Issue #82: proved WIP results/counterexamples with source commit and relation class;
- Foundation Problem Set Issue #164: verified bottom-layer questions needing research;
- `research_scheduler.json` plus Issue #240: live dispatch/lease/handoff coordination only.

Never infer “unknown” merely because a result or tool is absent from the current branch.

## 4. Shared reusable mathematical homes

### A0 — primitive discrete state algebra

Roots/collapse, basin/gap coordinates, quotient/remainder, scale factors and gcd/lcm lattice, signed state, typed descent, adjoints, commutation and fixed points. Canonical entry: P001–P009 plus `docs/THEOREMS.*`.

Canonical interface conventions:

- `N = N_0 = {0,1,2,...}`; positive integers are `N_{>0}`;
- nontrivial primitive root/collapse uses `p >= 2`;
- exact positive-exponent algebra uses `p >= 1` with `R_1 = C_1 = id`.

### A1 — dynamics, functional kernels, collision and stabilization

Deterministic history merge, fiber/kernel multiplicity, collision spectra, coalescence and well-founded stabilization. Canonical time interface:

`F_0 = id`, `F_{t+1} = T_t o F_t`, equivalently `F_t = T_{t-1} o ... o T_0` for `t >= 1`.

FQ-004 also fixes the project-wide generic **functional-kernel layer**. For a typed carrier `X` and deterministic `f:X->Y`, current equality after `f` is `ker(f)`, not exact state equality unless `f` is injective. Deterministic postcomposition satisfies

`ker(f) subseteq ker(g o f)`.

A state pair is ordinary product notation `X x X`, not a separate primitive.

Primary entry: `docs/FOUNDATIONS.*`, T012/P010, P011, P019, P020.

### A2 — observation and future-compatible quotient

Observation factorization, predictive/future closure, finite operation-family compatibility, minimal repair and task-relative precision. P018/P023/P024 are primary entry points. The finite-arity quotient operation-congruence extension is canonical and Lean-routed through `EnterpriseMath/Quotient/OperationCongruence.lean` when imported by the root build.

For a declared future language `W`, package the required future outputs as `Sigma_W:X->S_W`. Its kernel is the future-safe equality for **that declared language**. If current observation `O` is included in the signature, then

`exact equality subseteq ker(Sigma_W) subseteq ker(O)`.

A Difference/defect/critical-grid or other compressed coordinate may replace state information only after the required current/future observable factors through it. P023 owns the factorization/coarsest-repair theory; P024 owns the exact translation-language specialization. These generic kernel/factorization/distinguishability ideas are classical prior mathematics, not Enterprise Math novelty.

### A3 — structured relation-state algebra

Core object: `Z_ij = m_j*c_i - m_i*c_j`, with partition coarsening `Z' = A Z A^T`, relation scale/rank and refinement structure.

Canonical executable core on `main`:

- `weighted_relation_field.py`;
- `relation_lattice.py`;
- `relation_scale.py`;
- their canonical regression suites.

These modules are shared executable specifications. Any theorem statement still living only in a research branch/Relay keeps its WIP status until separately canonicalized. FQ-004 explicitly preserves A3 as an extension richer than ordinary functional-kernel membership unless an owner proves an exact reduction.

### A4 — admissible support / correspondence algebra

Finite multivalued relations, converse/composition, common-target structure, radius-indexed support, split-completeness boundaries, MAY/MUST semantics and witness/group spectra.

Canonical executable core on `main`:

- `admissible_support.py`;
- `relational_spectrum.py`;
- their canonical regression suites.

The A3→A4 executable bridge `a3_a4_support_bridge.py` is also canonical on `main`; theorem/proof status remains controlled by canonical result/Relay provenance rather than module presence. FQ-004 does not collapse multivalued correspondence semantics into one deterministic kernel.

### A5 — intrinsic discrete geometry

P012 supplies the canonical ordinary metric foundation on connected undirected simple graphs. Canonical tools include `geometry.py` and the P022 `A_p` / root-lattice executable core `lattice_geometry.py` with its regression suite.

P022 remains `OPEN / ACTIVE RESEARCH`; the canonical executable slice covers integer `A_p` graph distance, quadratic separation, collapsed radial distance, shell/ball counts and distance-carry probes. Broader lattice candidates, HCP/Barlow and cross-owner interfaces remain open.

**Active interface alert:** `FQ-20260809-005` asks whether stable exported `geometry.graph_distance` should enforce the P012 undirected metric domain or be explicitly layered from a more general directed shortest-walk helper. Until resolved, do not cite P012 metric symmetry for asymmetric adjacency inputs.

### P021 — causal-boundary specialization

Canonical executable core on `main`:

- `causal_boundary.py`;
- `test_causal_boundary.py`.

It consumes P018 observation/refinement machinery and owns the finite graph + integer expansion boundary specialization. Broader causal focusing, direction/witness composition and physical interpretation remain open.

### E001 — finite material-impulse application specialization

The following eight-file slice is canonical executable application machinery on `main`:

- `material_impulse_accounting.py` + regression;
- `material_impulse_world_1d.py` + regression;
- `material_impulse_tick_order.py` + regression;
- `material_impulse_wall_world_1d.py` + regression.

This slice is reusable for exact retained-detail impulse accounting, discrete momentum drift, explicit tick-order comparison, and contact/wall-world experiments. It is **not** a general mechanics/material theorem and does not by itself validate a physical model. In particular, `OUTWARD` momentum is not silently identified with a physical `REBOUND`; contact history/transmission state remains part of the richer event semantics.

## 5. High-value negative boundaries

- exact state equality, current observational equality and declared-future-safe equality must not be silently identified;
- a Difference/defect/critical-grid coordinate is not dynamically complete without a factorization/sufficiency theorem;
- coarse equality/support/cardinality does not automatically preserve later composition;
- A3 signed relation data can cancel under quotient, so coarse support does not certify universal fine support;
- pairwise/common-target cardinality can lose witness identity needed by multi-step composition;
- geometry-only contact/collision facts may be insufficient to select a unique response;
- a quotient safe for one future language can fail for a richer language;
- ordinary metric claims require their graph/weight hypotheses; directed/asymmetric structures must not silently inherit symmetry;
- an E001 engineering transition/result must not be promoted to a universal physical law merely because its executable slice is canonical;
- file-name equality, Git ancestry or `ahead(main)>0` is not proof of new mathematics;
- established machinery such as function kernels, Galois connections, semigroups, automata distinguishability, numerical semigroups and partition refinement remains prior art.

## 6. Shared executable tool surface

All routes may reuse canonical executable assets; discovery branch does not create exclusive ownership.

Python roots under `src/enterprise_math/` include:

- A0/A5 primitives: `core.py`, `division.py`, `scale_algebra.py`, `signed.py`, `typed_scale.py`, `geometry.py`, `lattice_geometry.py`;
- A2: `composition_safe_collapse.py`, precision/predictive/future-signature modules, action-language/clearance/guard/boundary specializations;
- A3: `weighted_relation_field.py`, `relation_lattice.py`, `relation_scale.py`;
- A4: `admissible_support.py`, `relational_spectrum.py`;
- A3→A4: `a3_a4_support_bridge.py`;
- P021: `causal_boundary.py`;
- P017: mirror/cofactor/Legendre pressure-test modules;
- E001 application: `material_impulse_accounting.py`, `material_impulse_world_1d.py`, `material_impulse_tick_order.py`, `material_impulse_wall_world_1d.py` and their tests.

No new Python/Lean subsystem is required by FQ-004: the canonical functional-kernel layer is a language/interface clarification backed by existing theorem owners.

`src/enterprise_math/__init__.py` exports only a compact stable subset. A non-exported module may still be a canonical internal executable specification; check scope/provenance before treating it as a stable API.

Lean:

- `EnterpriseMath.lean` is the root import surface;
- `EnterpriseMath/**.lean` contains formalization assets;
- claim `LEAN_CHECKED_MAIN` only for statements actually covered by the imported/warning-fatal build.

Validation/reconstruction/governance tools:

- `tests/`: exact regression/counterexample suites;
- `experiments/`: bounded pressure tests and engineering probes;
- `tools/check_bilingual_pairs.py`: bilingual gate;
- `tools/check_references.py`: reference-integrity gate;
- `tools/research_scheduler.py`: live dispatch/lease/handoff state-machine helper; it coordinates execution and does not certify theorem truth.

Executable checks support discovery/falsification/regression; they do not independently upgrade a claim to `PROVED`.

## 7. Propagation, dispatch and nonblocking rules

When a reusable result appears:

1. Relay it if another active route may benefit;
2. classify downstream action as `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
3. identify mother-theorem owner/relation class;
4. after canonical promotion, update status/result routing and this surface as needed;
5. register reusable executable tool families here;
6. never wait for consumer ACK unless a complete `HARD_BLOCK` exists.

Research is parallel; canonical promotion is serialized. `defer` is routing, not blocking. Claims on Issue #240 are renewable execution leases; unfinished sessions must hand the route back rather than silently leaving it unstaffed. Scheduler events (`CLAIM`, `HEARTBEAT`, `PROGRESS`, `HANDOFF`, `HARD_BLOCK`, `UNBLOCK`, `DONE`, `SUPERSEDE`) coordinate execution only.

## 8. Foundation stewardship

Mechanical or already-determined bottom-layer drift is fixed directly. Genuine unresolved mathematical/interface choices are minimally verified and escalated to Issue #164, then handed to another researcher.

Canonicalized foundation questions FQ-001 through FQ-004 now establish:

- positive-exponent primitive/algebra scope;
- `N=N_0` including zero;
- zero-based cumulative time;
- the minimal classical functional-kernel / declared-future-signature layering described above.

Current active foundation question:

- `FQ-20260809-005` — stable `graph_distance` API domain versus the P012 ordinary metric theorem domain.
