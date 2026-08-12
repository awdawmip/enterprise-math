# R044 — Native-Semantics Admissibility Gate Injection Backtest

Status: `DONE / RETURNED / SEMANTIC_CHECKPOINT / PASS_WITH_HARDENING_REQUIRED / NOT CANONICAL`

Researcher-ID: `EM-R044-8C2F61`  
Task: `RS-R044-NATIVE-SEMANTICS-ADMISSIBILITY-GATE-INJECTION-BACKTEST`  
Source main/taskbook: `b662cc9c9febd341eaaed94e6591abb2b75b8421`  
Audited policy digest: `sha256:8eb97ee026cbbd35f77f8bba02547d246beb86021631ab0a5257dd1f97acad19`

## 1. Verdict

R044 independently audited the active native-semantics gate, rebuilt its injection path, implemented a typed-dependency checker, attacked it with adversarial/mutation controls, and retyped representative R033–R043 claims.

`ACTIVE_GATE_CONCEPTUALLY_SOUND / INJECTION_MECHANICALLY_LIVE / CONDITIONAL_MATH_PRESERVED / MACHINE_SCHEMA_HARDENING_REQUIRED`

When faithfully applied, the active gate blocks the historical promotion pattern

`N0 graph/contact -> added root/metric/process -> readout/geometry -> therefore N0 ontology`.

It does **not** ban metric or continuum mathematics. If a task explicitly declares a metric, embedding, stochastic rule, optimization rule, or continuum structure in its N0 base, the checker accepts claims native to that enlarged task-relative world.

No new semantic stratum is needed. I0/N0/N1/N2/N3 remain sufficient, but promotion must be dependency-complete and semantic-strength-sensitive.

## 2. Type-system audit

Retained strata:

- `I0_IMPLEMENTATION_CARRIER`: labels/coordinates/bases/encodings used only to realize/check declared structure;
- `N0_NATIVE_RELATIONAL`: task-declared carrier, relations, predicates, operations;
- `N1_DERIVED_OPERATIONAL_SEMANTICS`: root/seed choices, path/metricization, propagation, optimization, stochastic/action/future language introduced after N0;
- `N2_READOUT_COLLAPSE`: quotient/scalar/shell/radius/norm/surface scalar/histogram/embedding quantity/moment/spectrum/zeta;
- `N3_CONTINUUM_CLASSICAL`: smooth/continuum/PDE/integral/coarse classical structures introduced after N0.

R044 adds a necessary distinction:

- `DECLARED_N0_PRIMITIVE`: written into the task base;
- `N0_DEFINABLE_DERIVED`: uniquely definable from N0, independently of non-N0 choices, at the semantic strength being claimed.

A definability theorem does not retroactively make a derived object an original primitive.

## 3. Weakest reliable native-promotion certificate

Promotion of a theorem-critical object `D` toward native/intrinsic status requires all of:

1. exact declared N0 base;
2. transitive coverage of every theorem-critical symbol by N0 or a typed dependency DAG;
3. construction of `D` using only N0 structure (unless extra structure is itself declared N0);
4. independence from arbitrary non-N0 root/basis/orientation/enumeration/representative/implementation choices;
5. invariance or canonical equivariance under the relevant N0 relabelings/automorphisms;
6. uniqueness/reconstruction at the **same semantic strength** being promoted;
7. evidence references for those facts.

R044 uses `SCALAR < QUOTIENT < RELATION < OBJECT < PRIMITIVE` only as a checker strength order. A scalar invariant cannot certify a full object. Omitted/dangling theorem-critical dependencies give `UNRESOLVED`, never a native pass.

## 4. Deterministic checker and adversarial results

Artifact: `tools/check_native_semantics_claims.py`.

Verdicts are driven by declared base + theorem-critical typed dependency graph + certificate strength, not keywords. Hazard words only trigger warnings.

Focused tests: `8 / 8 PASS` under Python 3.13.

Frozen fixture set: 16 cases.

- unsafe native promotions/incomplete native ledgers: `10/10` blocked or fail-closed;
- legal native tasks (including explicit metric and explicit continuum bases): `3/3` accepted;
- legal non-native readout/continuum mathematics: `3/3` preserved;
- scoped false negatives: `0`;
- scoped false positives: `0`.

Verdict distribution: `SEMANTIC_MISMATCH 9 / NATIVE_ADMISSIBLE 3 / READOUT_ONLY 2 / CONTINUUM_ONLY 1 / UNRESOLVED 1`.

The zero FP/FN count is only for this frozen adversarial set, not a guarantee over arbitrary prose.

Load-bearing negative control: an automorphism-invariant scalar does not promote a full object. Load-bearing positive controls: explicitly declared metric-base and continuum-base worlds remain admissible.

## 5. Injection backtest

### Startup injection — PASS

Current `AGENTS.md` contains the mandatory native-semantics startup gate and explicitly flags root, shortest path, radius/equidistance, embedding, propagation, optimization, Fourier/Bloch and readout promotion hazards. This catches derived structures introduced during research even if a taskbook never used ontology vocabulary.

### Taskbook-policy injection — PASS

`research_taskbook_policy.json` includes `native_semantics_admissibility.json` in `policy_inputs`.

R044 independently recomputed `tools/research_taskbook.py`'s Git-blob digest and obtained exactly:

`sha256:8eb97ee026cbbd35f77f8bba02547d246beb86021631ab0a5257dd1f97acad19`.

Thus a gate change mechanically rotates taskbook policy review stamps.

### R043 stale-stamp control — PASS

R043 still carries old digest `sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77`. Under current `audit --dispatch`, that is `TB-POLICY-STALE / ERROR`. R043 cannot be newly dispatched until Driver re-review/restamp.

Eight mutations were frozen in `R044_INJECTION_BACKTEST.json`: delete startup gate; omit N1 dependency; report N2 as N0; explicitly declare metric in base; blanket-forbid metric; blanket-forbid continuum; promote object with scalar certificate; remove gate from policy inputs. Each has an explicit detecting control.

## 6. Historical R033–R043 impact

Artifact: `research/r044_generated/R044_CLAIM_IMPACT_MATRIX.json`.

47 claims/taskbook items were typed:

- `KEEP_NATIVE`: 4;
- `KEEP_BUT_RETYPE_CONDITIONAL`: 20;
- `KEEP_AS_READOUT_ONLY`: 16;
- `RETRACT_NATIVE_INTERPRETATION`: 3;
- `RECOMPUTE_UNDER_N0`: 1;
- `UNRESOLVED_NEEDS_NEW_TASK`: 3.

The main result is **conservation**: most exact mathematics survives.

### R033

Keep contact adjacency as N0. Keep exact shortest-path/word-metric formulas as N1-conditional. Shell/ball counts, stable-norm/limit-shape geometry, exposed/Voronoi constructions and macro ratios are N2 readouts. Retract seed-as-center and propagation-independent reading of “intrinsic sphere.” No R033 formula needs recomputation solely for this correction.

### R034

Uniform NN propagation/random-walk/heat are N1; physical displacement/covariance/moments/Bloch/Fourier are N2; Brownian continuum is N3. Exact propagation and stacking-memory theorems survive conditionally. No theorem-level recomputation is triggered.

### R037

Independent replication remains valid evidence for the conditional R033/R034 mathematics, but reproduction does not confer ontology admissibility. Add semantic typing to its evidence matrix; do not rerun replicated numerics/formulas solely due retyping.

### R038 — genuine repair core

The rooted graph-zeta formulas survive as N1/N2 mathematics.

- `R038-C05`: the rooted graph-zeta H7 kill was used against a stronger metric-free N0 hypothesis. That inference must be **recomputed under N0**; the conditional zeta theorem survives.
- `R038-C06`: `NO_UNIQUE_NATIVE_PI_WITHOUT_READOUT_SEMANTICS`, if claimed as metric-free N0 nonexistence, is **unresolved**. Many inequivalent readouts do not logically exclude a different N0-definable invariant.

These are the only frozen theorem-level recompute/resolve targets for R045.

### R039

Positive control survives: `delta(C)={(u,v):u in C,v notin C,u~v}` uses declared contact+occupancy only and is N0-relational. `S=|delta|`, masks/types/histograms are N2. Addition/future languages, `SURFACE_DOWN`, fixed-horizon carriers and fixed-volume optimization are N1; Wulff/zonotope descriptions are later readouts. Exact update/counterexample mathematics remains valid at those layers.

### R041

`T_h/CT_h/B_h/M_h` are exact future/action carriers, hence N1 with N2 readout components where applicable. Their exactness does not make them N0 state ontology. Retract only the reading of “native surface horizon quotient” that promotes the horizon quotient itself to N0.

### R043

R043 cannot continue under its stale review stamp. After re-review, use this typing delta:

- contact+occupancy and unweighted relational frontier/interface: N0 or N0-definable;
- `S`, frontier weights and weighted graph summaries: N2;
- chosen addition/actions, `B_h`, recursive/Markov future semantics: N1;
- a positive `G0 -> B3` or recursive-G0 theorem is an exact future-carrier theorem, not automatically an N0 world-state theorem.

## 7. Hardening delta

Returned as research proposal only: `R044_GATE_HARDENING_DELTA.json`.

Recommended additions:

- `NSA-12-TASK-RELATIVE-BASE-PRECEDENCE`;
- `NSA-13-SEMANTIC-STRENGTH-MATCH`;
- `NSA-14-TRANSITIVE-DEPENDENCY-CLOSURE`;
- `NSA-15-DECLARED-VS-N0-DEFINABLE`.

Recommended ledger fields: `critical_symbols`, `typed_dependency_graph`, `promotion_target_strength`, `certificate_semantic_strength`, `transitive_dependency_closure_checked`, `native_basis_status`.

The active policy itself is deliberately not rewritten by this research owner; activation is a separate Driver/governance action.

## 8. Frozen R045 contract

Artifact: `research/r044_generated/R045_RERUN_GENERATION_SPEC.json`.

R045 is **not** a wholesale rerun. It must retype preserved claims without recomputation, add semantic typing to R037 evidence, audit downstream Foundation-facing consumers of the R038 native claims, and do theorem-level repair/resolve only for:

`{R038-C05, R038-C06}`.

R043 execution is outside R045 and requires its own Driver restamp first.

## 9. Answers to the taskbook questions

1. **Gate sufficiency:** `PASS_WITH_HARDENING_REQUIRED`. The policy/startup design blocks the historical promotions when faithfully applied; machine enforcement should explicitly add strength matching and dependency closure.
2. **Weakest promotion certificate:** declared N0 + complete typed dependency closure + N0-only construction + choice independence + N0 relabeling invariance/equivariance + same-strength uniqueness/reconstruction + evidence refs.
3. **Metric/continuum positive control:** the gate must and does allow such worlds when explicitly declared in N0; it forbids hidden promotion, not vocabulary.
4. **Rename/retype vs recompute:** R033/R034/R037/R039/R041 mathematics is conserved under retyping; only `R038-C05/C06` form the frozen theorem-level repair core.
5. **R043:** cannot directly continue; current stamp is stale and must be re-reviewed/restamped under `8eb97...`.
6. **Minimal R045:** historical retype + R037 semantic evidence dimension + downstream audit + theorem-level work only on `R038-C05/C06`.

## 10. Evidence and returned artifacts

Validation: checker `8/8 PASS`; 16 fixtures all matched expected verdict; policy digest exact match; 8 mutation controls; 47 historical claims/items routed. No theorem-critical floating point was used.

`CI_NOT_REQUIRED_FOR_RESEARCH` — no workflow/status query was performed.

Returned:

- `research/R044_NATIVE_SEMANTICS_GATE_REPORT.md`;
- `research/r044_generated/R044_CLAIM_IMPACT_MATRIX.json`;
- `research/r044_generated/R044_ADVERSARIAL_FIXTURES.json`;
- `research/r044_generated/R044_INJECTION_BACKTEST.json`;
- `research/r044_generated/R044_GATE_HARDENING_DELTA.json`;
- `research/r044_generated/R045_RERUN_GENERATION_SPEC.json`;
- `tools/check_native_semantics_claims.py`;
- `tests/test_check_native_semantics_claims.py`.
