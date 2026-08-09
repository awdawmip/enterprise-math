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
8. for foundational language/formula/theorem/tool-interface work, a flagged contradiction, or a mature result that may feed back into the common bottom layer, read `docs/FOUNDATION_STEWARD_PROTOCOL.*`, `docs/FOUNDATION_BACKFLOW_LOOP.*`, `foundation_backflow.json`, and relevant Foundation Problem Set Issue #164 `FQ-*` entries;
9. then classify the work as a mother theorem, specialization, bridge, counterexample, tool, duplicate, answer to a foundation question, or Foundation Feedback Packet.

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

For foundation backflow, keep four additional boundaries explicit: Relay `PROVED` is not canonical main; scheduler `DONE` is not theorem proof or canonical promotion; an FQ `ANSWERED` result is not steward acceptance; steward `ACCEPTED` is still not canonical until a gated latest-main integration enters `main`.

## 3. Canonical knowledge channels

- `docs/THEOREMS.*`: compact original theorem catalogue;
- `docs/PROBLEM_STATUS.*`: authoritative numbered-problem router;
- canonical `docs/Pxxx_*.{en,zh-CN}.md`: exact modern theorem families and hypotheses;
- `EnterpriseMath.lean` plus imported `EnterpriseMath/**.lean`: Lean-checked subset;
- Research Relay Issue #82: proved WIP results/counterexamples with source commit and relation class;
- Foundation Problem Set Issue #164: verified bottom-layer questions needing research and returned answers awaiting steward verification;
- `research_scheduler.json` plus Issue #240: live dispatch/lease/handoff coordination only;
- `foundation_backflow.json`: semantic links among research findings, FQs, scheduler tasks, steward verification, integration, and post-merge propagation.

Never infer “unknown” merely because a result or tool is absent from the current branch.

## 4. Shared reusable mathematical homes

### A0 — primitive discrete state algebra

Roots/collapse, basin/gap coordinates, quotient/remainder, scale factors and gcd/lcm lattice, signed state, typed descent, adjoints, commutation and fixed points. Canonical entry: P001–P009 plus `docs/THEOREMS.*`.

Canonical interface conventions:

- `N = N_0 = {0,1,2,...}`; positive integers are `N_{>0}`;
- nontrivial primitive root/collapse uses `p >= 2`;
- exact positive-exponent algebra uses `p >= 1` with `R_1 = C_1 = id`.

### A1 — dynamics, functional kernels, collision and stabilization

Deterministic history merge, functional kernels, fiber multiplicity, collision spectra, coalescence and well-founded stabilization. For any deterministic `f:X->Y`, the generic functional kernel is `x ~_f y iff f(x)=f(y)`, and deterministic postcomposition satisfies `ker(f) subseteq ker(g o f)`.

Canonical time interface:

`F_0 = id`, `F_{t+1} = T_t o F_t`, equivalently `F_t = T_{t-1} o ... o T_0` for `t >= 1`.

A State Pair is the derived product carrier `X x X` used to query such relations; it is not a separate primitive Foundation object.

Primary entry: `docs/FOUNDATIONS.*`, P010, P011, P019, P020.

### A2 — observation, future signatures and future-compatible quotient

Current observational equality is `ker(O)` and is not exact state equality unless `O` is injective. A declared deterministic future experiment/operation language may be packaged as a signature `Sigma_W`; its future-safe equivalence is `ker(Sigma_W)`. If the current observation is included in the signature, the relation-inclusion chain is

`Delta_X subseteq ker(Sigma_W) subseteq ker(O)`.

P018/P023/P024 provide observation factorization, predictive/future closure, finite operation-family compatibility, minimal repair and task-relative precision. The finite-arity quotient operation-congruence extension is canonical and Lean-routed through `EnterpriseMath/Quotient/OperationCongruence.lean` when imported by the root build.

A Difference/defect/other coordinate is complete for a current or future task only after the required observation/future signature is proved to factor through that coordinate. P023 retains generic factorization/minimal-repair/future-refinement ownership; P024 retains integer action-language specialization.

### A3 — structured relation-state algebra

Core object: `Z_ij = m_j*c_i - m_i*c_j`, with partition coarsening `Z' = A Z A^T`, relation scale/rank and refinement structure.

Canonical executable core on `main`:

- `weighted_relation_field.py`;
- `relation_lattice.py`;
- `relation_scale.py`;
- their canonical regression suites.

These modules are shared executable specifications. Any theorem statement still living only in a research branch/Relay keeps its WIP status until separately canonicalized. A3 structured relation-state may retain information beyond membership in one functional equivalence relation and is not identified with the A1/A2 functional-kernel layer.

### A4 — admissible support / correspondence algebra

Finite multivalued relations, converse/composition, common-target structure, radius-indexed support, split-completeness boundaries, MAY/MUST semantics and witness/group spectra.

Canonical executable core on `main`:

- `admissible_support.py`;
- `relational_spectrum.py`;
- their canonical regression suites.

The A3→A4 executable bridge `a3_a4_support_bridge.py` is also canonical on `main`; theorem/proof status remains controlled by canonical result/Relay provenance rather than module presence. A multivalued correspondence can admit several future images and is not identified with the kernel of one deterministic function.

### A5 — intrinsic discrete geometry

P012 supplies the canonical ordinary metric foundation on connected undirected simple graphs. Canonical tools include `geometry.py` and the P022 `A_p` / root-lattice executable core `lattice_geometry.py` with its regression suite.

P022 remains `OPEN / ACTIVE RESEARCH`; the canonical executable slice covers integer `A_p` graph distance, quadratic separation, collapsed radial distance, shell/ball counts and distance-carry probes. Broader lattice candidates, HCP/Barlow and cross-owner interfaces remain open.

**Active interface alert:** `FQ-20260809-005` asks whether stable exported `geometry.graph_distance` should enforce the P012 undirected metric domain or be explicitly layered from a more general directed shortest-walk helper. Until resolved, do not cite P012 metric symmetry for asymmetric adjacency inputs. `foundation_backflow.json` routes this research to the P022 geometry owner rather than to the steward.

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

- coarse equality/support/cardinality does not automatically preserve later composition;
- Difference/defect coordinates are not automatically complete state; current/future sufficiency requires an explicit factorization theorem;
- A3 signed relation data can cancel under quotient, so coarse support does not certify universal fine support;
- pairwise/common-target cardinality can lose witness identity needed by multi-step composition;
- functional kernels, A3 structured relation-state and A4 multivalued support are distinct layers and must not be collapsed merely because all use relation language;
- geometry-only contact/collision facts may be insufficient to select a unique response;
- a quotient safe for one future language can fail for a richer language;
- ordinary metric claims require their graph/weight hypotheses; directed/asymmetric structures must not silently inherit symmetry;
- an E001 engineering transition/result must not be promoted to a universal physical law merely because its executable slice is canonical;
- file-name equality, Git ancestry or `ahead(main)>0` is not proof of new mathematics;
- established machinery such as functional kernels, quotient/congruence, factorization/semiconjugacy, behavioral equivalence, partition refinement, Galois connections, semigroups and numerical semigroups remains prior art.

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
- `tools/research_scheduler.py`: live dispatch/lease/handoff state-machine helper; it coordinates execution and does not certify theorem truth;
- `tools/foundation_backflow.py`: validates the static FQ↔scheduler/backflow authority links and role boundaries.

Executable checks support discovery/falsification/regression; they do not independently upgrade a claim to `PROVED`.

## 7. Propagation, dispatch and nonblocking rules

When a reusable result appears:

1. Relay it if another active route may benefit;
2. classify downstream action as `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
3. identify mother-theorem owner/relation class;
4. ask whether the result exposes a minimal sufficient state, minimal repair/extension, cross-route invariant, negative boundary, reusable tool, or layering law; if so, create or route a Foundation Feedback Packet rather than leaving the structure only in the program branch;
5. after canonical promotion, update status/result routing and this surface as needed;
6. register reusable executable tool families here;
7. never wait for consumer or steward ACK unless a complete `HARD_BLOCK` exists.

Research is parallel; canonical promotion is serialized. `defer` is routing, not blocking. Claims on Issue #240 are renewable execution leases; unfinished sessions must hand the route back rather than silently leaving it unstaffed. Scheduler events (`CLAIM`, `HEARTBEAT`, `PROGRESS`, `HANDOFF`, `HARD_BLOCK`, `UNBLOCK`, `DONE`, `SUPERSEDE`) coordinate execution only.

## 8. Foundation stewardship and backflow

The bottom layer is governed by `docs/FOUNDATION_STEWARD_PROTOCOL.*`, `docs/FOUNDATION_BACKFLOW_LOOP.*`, `foundation_steward.json`, and `foundation_backflow.json`.

Mechanical or already-determined bottom-layer drift is fixed directly. A mature result that may feed back is compressed into a Foundation Feedback Packet and classified as `DIRECT_FOUNDATION_MAINTENANCE`, `FOUNDATION_QUESTION`, or `APPLICATION_LOCAL_OR_NOT_READY`. Genuine unresolved mathematical/interface choices are minimally verified and escalated to Issue #164, then linked to an appropriate #240 scheduler task. Mathematical FQ research uses `RESEARCH`; steward verification/integration uses `GOVERNANCE`.

`FQ-20260809-004` has a returned research answer that the steward accepted only at the narrow integration scope `typed state -> deterministic/observation functional kernel -> declared future-signature kernel`. It remains noncanonical until its latest-main integration passes applicable gates and enters `main`. `FQ-20260809-005` remains an active interface question routed to P022 geometry research.

Resolved canonical conventions currently on main remain FQ-001 through FQ-003. After FQ-004's resolving integration actually enters `main`, the minimal functional-kernel layer becomes the fourth canonical interface; the integration must not wholesale-promote P018/P023/P024/A3/A4 owner-specific mathematics.

The stable loop is:

`shared-surface preflight -> cross-route result extraction -> Foundation Feedback Packet -> direct maintenance OR FQ -> scheduler-linked research -> RETURN -> steward verification -> latest-main integration -> gates -> canonical main -> common-surface/tool/global-knowledge propagation -> later research pressure-test`.

If any stage can be recovered only from one conversation's memory, the loop is incomplete.
