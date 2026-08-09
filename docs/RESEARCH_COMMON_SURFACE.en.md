# Enterprise Math Common Research Surface

Status: `ACTIVE / REQUIRED PREFLIGHT`  
Effective: 2026-08-09

Purpose: give every research route one compact shared view of reusable mathematics, canonical executable/formal assets, negative boundaries, active interface alerts, and live routing. This is a router, not a substitute for exact theorem documents or proofs.

## 1. Mandatory preflight

Before substantive L1/L2/L3 research:

1. read this file and `research_common_surface.json`;
2. read `docs/RESEARCH_SCHEDULING_PROTOCOL.*`, `research_scheduler.json`, and live Dispatch Board Issue #240;
3. read `docs/RESEARCH_OWNER_ISOLATION.*`;
4. read `docs/PROBLEM_STATUS.*` and the relevant canonical theorem/result documents;
5. read the latest relevant Research Relay Issue #82 entries;
6. inspect overlapping Python/tests and root-imported Lean modules before inventing a parallel theorem or tool;
7. for foundation-facing work, read `docs/FOUNDATION_STEWARD_PROTOCOL.*` and relevant Foundation Problem Set Issue #164 `FQ-*` entries.

Use selective retrieval. Absence from the current branch does not mean absence from the project.

## 2. Status discipline

Keep these distinct:

- `CANONICAL_MAIN` — proved result integrated on `main` at its stated scope;
- `LEAN_CHECKED_MAIN` — canonical statement actually covered by the root warning-fatal Lean build;
- `PROVED_WIP_RELAY` — branch-proved result with provenance but not yet canonical;
- `EXECUTABLE_CHECKED` — exact executable/finite validation, not proof by itself;
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY` — reusable failure/impossibility result;
- `CONJECTURAL` — research target only.

A source/test module entering `main` does not automatically make every mathematical or physical interpretation of that module a theorem. Scheduler claims/leases coordinate work; they never certify truth.

## 3. Canonical knowledge channels

- `docs/THEOREMS.*` — compact original theorem catalogue;
- `docs/PROBLEM_STATUS.*` — authoritative numbered-problem router;
- canonical `docs/Pxxx_*.{en,zh-CN}.md` — exact modern theorem statements and hypotheses;
- `EnterpriseMath.lean` and its imported `EnterpriseMath/**.lean` — root Lean-checked subset;
- `research_common_surface.json` — machine-readable theorem/tool/formalization router;
- Research Relay Issue #82 — cross-route WIP results, negative boundaries, and canonical consumption notices;
- Foundation Problem Set Issue #164 — verified unresolved foundation questions;
- `research_scheduler.json` + Issue #240 — dispatch/lease/handoff only.

## 4. Shared mathematical homes

### A0 — primitive discrete state algebra

Roots/collapse, basin/gap coordinates, quotient/remainder, scale lattice, signed state, typed descent, adjoints, commutation and fixed points. Main entry: P001–P009 plus `docs/THEOREMS.*`.

Canonical conventions:

- `N = N_0 = {0,1,2,...}`;
- positive integers are `N_{>0}`;
- nontrivial primitive root/collapse uses `p >= 2`;
- positive-exponent algebra uses `p >= 1` with `R_1 = C_1 = id`.

### A1 — deterministic dynamics and functional kernels

History merge, fibers/kernel multiplicity, collision spectra, coalescence and stabilization. Canonical time:

`F_0=id`, `F_{t+1}=T_t o F_t`, hence `F_t=T_{t-1} o ... o T_0` for `t>=1`.

FQ-004 canonicalizes the generic functional layer. For deterministic `f:X->Y`,

`x ~_f y iff f(x)=f(y)`, and `ker(f) subseteq ker(g o f)`.

A State Pair is ordinary `X x X`, not a new primitive.

### A2 — observation and future-compatible quotient

Observation kernels, factorization, declared future signatures, predictive closure, operation-family compatibility, minimal repair and task-relative precision. P018/P023/P024 are the main owners/consumers.

For a declared deterministic future language `W`, package required outputs as `Sigma_W:X->S_W`; future-safe equality for that language is `ker(Sigma_W)`. If current observation `O` is included,

`exact equality subseteq ker(Sigma_W) subseteq ker(O)`.

A Difference/defect/critical-grid or other compressed coordinate replaces state information only after the required current/future outputs factor through it.

#### P018↔P023 bounded quotient-root action basis — `LEAN_CHECKED_MAIN`

PR #249 / `main@c9b39069917c32b8a02a1bbdf6297ca5e43c9438`.

For `O_a(q)=R_r(floor(q/a))` on exact states `0,...,N`, a positive action set separates every exact state iff it contains every positive `r`-power-free `b<=N`; those actions are the unique least separating set under inclusion. Locally,

`O_a(q-1) != O_a(q) iff q=a*t^r`

for some positive `t`.

Canonical assets:

- `EnterpriseMath/Quotient/RootAdjacentBoundary.lean`
- `EnterpriseMath/Quotient/PowerFreeActionBasis.lean`
- `src/enterprise_math/p018_p023_power_free_action_basis.py`
- `tests/test_p018_p023_power_free_action_basis.py`
- `docs/PRIOR_ART_P018_P023_POWER_FREE_ACTION_BASIS.en.md`
- `docs/PRIOR_ART_P018_P023_POWER_FREE_ACTION_BASIS.zh-CN.md`
- dedicated source/lineage sidecars.

Boundary: power-free arithmetic and generic distinguishing/Test-Cover/minimal-language machinery are prior mathematics; exact-package historical novelty remains unverified. **Future-safe state precision and minimum future-action-language complexity are distinct resources.**

#### P018 centered-prime-radius layer — `CANONICAL_MAIN + EXECUTABLE_CHECKED`

PR #270 / `main@b48019603c3c39332be97a5769e811f33d884296`.

Assets:

- `src/enterprise_math/centered_prime_radius.py`
- `tests/test_centered_prime_radius.py`

This is an elementary centered-coordinate re-expression of the already-established P018 Stage-8 near-diagonal factor-proof slack. Under its explicit left-prime and size-range hypotheses, the relevant minimal positive symmetric prime radius is `proof_slack+1` and the shell state is localized by a difference of squares. It does **not** assert a symmetric prime pair for every center and does not prove a Goldbach-type statement.

### A3 — structured relation-state algebra

Core object: `Z_ij=m_j*c_i-m_i*c_j`, with partition quotient/kernel, relation scale/rank and refinement structure.

Canonical executable core:

- `src/enterprise_math/weighted_relation_field.py`
- `src/enterprise_math/relation_lattice.py`
- `src/enterprise_math/relation_scale.py`

These are reusable executable specifications. Broader historical A3 theorem claims retain their actual WIP/canonical status. A3 is richer than ordinary functional-kernel membership unless an explicit reduction theorem proves otherwise.

### A4 — admissible support / correspondence algebra

Finite multivalued relations, composition/converse, common-target structure, split-completeness, MAY/MUST support and witness/group spectra.

Canonical executable core:

- `src/enterprise_math/admissible_support.py`
- `src/enterprise_math/relational_spectrum.py`
- `src/enterprise_math/a3_a4_support_bridge.py` for the first executable A3→A4 bridge slice.

A4 multivalued correspondence is not silently identified with one deterministic functional kernel.

### A5 — intrinsic discrete geometry

P012 supplies the ordinary metric foundation on **connected undirected simple graphs**. P022 remains `OPEN / ACTIVE RESEARCH`; canonical executable geometry does not close the broader program.

Canonical P022 families:

- `src/enterprise_math/lattice_geometry.py` + `tests/test_lattice_geometry.py` — exact `A_p`/root-lattice graph distance, quadratic separation, radial collapse, shell/ball counts and distance-carry probes;
- PR #262 / `main@fc81a15a0fc7a76d1d2b44e7d9a41b699863ef22`:
  - `src/enterprise_math/p022_geodesic_multiplicity.py`
  - `tests/test_p022_geodesic_multiplicity.py`
  - `src/enterprise_math/p022_hcp_geometry.py`
  - `tests/test_p022_hcp_geometry.py`
- PR #288 / `main@aec7f625e48eb8f93ba701ba57686a9e225efd17`:
  - `src/enterprise_math/p022_barlow_stacking.py`
  - `tests/test_p022_barlow_stacking.py`.

PR #262 gives exact finite/combinatorial geodesic-multiplicity observables for `A_p` and simple-cubic geometry plus an integer-coordinate ABAB HCP contact graph with degree 12, exact graph distance/shells, and independently cross-checked shortest-path counts. Generic nonnegative witness-count/correspondence algebra belongs to A4/A2; P022 owns the geometry specialization. No floating-point Euclidean sphere-center model is assumed.

PR #288 generalizes the close-packed executable layer to periodic Barlow stacking: periodic contact graphs, exact graph distance/geodesic multiplicity, FCC/HCP reconstruction, and the root-to-target-layer **cumulative interface-sign-count** compression for those declared queries. The compression is task-relative; Barlow precision, periodic-growth, coordination-observable and observation-history theories are not part of the promoted slice.

**Active interface alert — FQ-20260809-005:** stable exported `geometry.graph_distance` accepts general adjacency mappings, while P012 ordinary metric theorems assume connected undirected simple graphs. Until the research answer is steward-verified, do not cite P012 metric symmetry for asymmetric adjacency inputs.

### P021 — causal-boundary specialization

Canonical executable core:

- `src/enterprise_math/causal_boundary.py`
- `tests/test_causal_boundary.py`

It consumes P018 observation/refinement machinery and owns the finite-graph + integer-expansion causal-boundary specialization. Broader causal focusing, witness/direction composition and physical interpretation remain open.

## 5. Shared E001 application tools and boundaries

### Finite material-impulse world

Canonical executable family:

- `src/enterprise_math/material_impulse_accounting.py`
- `src/enterprise_math/material_impulse_world_1d.py`
- `src/enterprise_math/material_impulse_tick_order.py`
- `src/enterprise_math/material_impulse_wall_world_1d.py`
- their four regression files.

Reusable for retained-detail impulse accounting, momentum drift, tick-order comparison and wall-world tests. It is not a general mechanics/material theorem. In particular, `OUTWARD` momentum is not automatically physical `REBOUND`.

### Exact measured-polyline refinement

PR #264 canonical assets:

- `src/enterprise_math/material_measurement_area_refinement.py`
- `src/enterprise_math/material_measurement_refinement_variation.py`
- `tests/test_material_measurement_area_refinement.py`
- `tests/test_material_measurement_refinement_variation.py`

These quantify exactly what changes when a **new measured point** is added to a declared integer stress-strain polyline. They do not interpolate missing samples or recover an unknown continuum constitutive curve.

### Residual result-conservation slice

PR #274 / `main@12500185f4c222ae49816e7b844e36a82e3ac8fe` canonicalized:

- `src/enterprise_math/material_alias_stability.py` + `tests/test_material_alias_stability.py` — finite permanent response/anisotropy alias horizon; pre-horizon visibility can be nonmonotone;
- `src/enterprise_math/material_boundary_shell_growth.py` + `tests/test_material_boundary_shell_growth.py` — for fixed depth `K`, `R_{n,K}(d)=d^n-(d-K)^n` has exact discrete degree `n-1`, while the full coarse box has degree `n`;
- `src/enterprise_math/material_phase_saturation.py` + `tests/test_material_phase_saturation.py` — once endpoint-clearance sum `C>=2d-1`, interaction phases saturate at `2(d-1)` and further displacement contributes transmission phases only;
- `src/enterprise_math/material_layered_kinematics.py` + `tests/test_material_layered_kinematics.py` — **COMPARATOR-NEGATIVE**: two staged finite projections can differ by order by at most one returned-budget quantum even when the undeformed rational product commutes.

These are finite integer/application results, not probability laws, hidden-continuum claims, laminate constitutive laws or universal material physics.

## 6. High-value negative boundaries

All routes must remember:

- exact state equality, current observational equality and declared-future-safe equality are different unless hypotheses identify them;
- compressed coordinates are not dynamically complete without factorization/sufficiency;
- future-safe state precision != minimum future-action-language complexity;
- coarse equality/support/cardinality need not preserve later composition or witness identity;
- A3 signed relation data may cancel under quotient;
- geometry-only collision/contact facts may not determine unique response;
- a quotient safe for one future language can fail for a richer one;
- ordinary metric claims require the P012 graph hypotheses;
- finite measured-polyline refinement does not reveal an unmeasured continuum;
- canonical engineering code does not become a universal physical law merely by entering `main`;
- Git ancestry/file-name equality is not proof of new mathematics or semantic absorption;
- function kernels, Galois connections, semigroups, automata distinguishability, Test Cover, power-free arithmetic, numerical semigroups and partition refinement remain prior art.

## 7. Root Lean import index

`EnterpriseMath.lean` is the canonical root build. The machine index must match these imports exactly:

- `EnterpriseMath/Arithmetic/CollapseCommutation.lean`
- `EnterpriseMath/Arithmetic/CollapseGap.lean`
- `EnterpriseMath/Arithmetic/IntegerRoot.lean`
- `EnterpriseMath/Arithmetic/RootMultiplicativity.lean`
- `EnterpriseMath/Dynamics/HistoryMerge.lean`
- `EnterpriseMath/Order/ReductiveCompositionStabilization.lean`
- `EnterpriseMath/Order/WellFoundedStabilization.lean`
- `EnterpriseMath/Precision/Carry.lean`
- `EnterpriseMath/Precision/CompositionSafeCollapse.lean`
- `EnterpriseMath/Precision/QuotientBasin.lean`
- `EnterpriseMath/Precision/QuotientCoalescence.lean`
- `EnterpriseMath/Quotient/OperationCongruence.lean`
- `EnterpriseMath/Quotient/PowerFreeActionBasis.lean`
- `EnterpriseMath/Quotient/RootAdjacentBoundary.lean`
- `EnterpriseMath/Quotient/RootFutureClosure.lean`
- `EnterpriseMath/Scale/Compatibility.lean`
- `EnterpriseMath/State/CriticalGrid.lean`

Claim `LEAN_CHECKED_MAIN` only for statements actually covered by these modules.

## 8. Repository operational tools

Every `tools/*.py` file is shared operational infrastructure and must remain machine/human indexed:

- `tools/audit_branch_lifecycle.py`
- `tools/check_bilingual_pairs.py`
- `tools/check_references.py`
- `tools/check_research_common_surface.py`
- `tools/research_scheduler.py`

`tools/check_research_common_surface.py` is mechanical only. It checks declared-path existence, exact root-Lean imports, exact repository-tool membership, active-FQ agreement, and active-alert validity. It does not prove mathematics or decide semantic reusability.

`tests/` support regression/counterexample checking; `experiments/` support bounded pressure tests. Neither automatically upgrades a claim to `PROVED`.

## 9. Propagation and canonical-promotion contract

When a reusable result appears:

1. Relay it with source, weakest assumptions, relation class, owner and one downstream action: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
2. keep research parallel unless a complete `HARD_BLOCK` exists;
3. at canonical L4 promotion, update `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json`, or explicitly justify shared-surface delta `N/A`;
4. register reusable executable-family paths;
5. root `EnterpriseMath.lean` import changes and `tools/*.py` membership changes must update the exact machine/human indexes in the same PR;
6. use one current-main final combination gate; unrelated movement of `main` during validation does not create a replay generation.

`tools/check_research_common_surface.py` enforces the objective part of this contract; semantic scope still requires steward/reviewer judgment.

## 10. Foundation stewardship

FQ-001 through FQ-004 are canonicalized foundation conventions. The only currently active foundation question is:

- `FQ-20260809-005` — stable `graph_distance` API domain versus the P012 ordinary-metric theorem domain.

The steward fixes mechanical drift directly, but does not choose unresolved research answers. Returned FQ answers require steward verification before canonicalization.
