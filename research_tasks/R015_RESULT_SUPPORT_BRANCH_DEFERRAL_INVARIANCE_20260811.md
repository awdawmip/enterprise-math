<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE",
  "title": "R015 Result-Support Branch Deferral Invariance",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Prove or kill the proposed result-only branch-deferral semantics: when path/history has been consumed and only final reachable result support matters, determine exactly when eager branching with intermediate coalescence and lazy preservation of unresolved possibilities followed by later branching produce the same future-support matrix for every finite future composition. Characterize the boundary by union preservation / relational lifting, build exhaustive finite oracles, and produce an impact map for P023/R009 without yet changing the canonical collapse law.",
  "next_action": "Freeze result-support semantics; prove the relational direct-image union/composition theorems and an iff characterization of branch-deferral invariance by union preservation; construct minimal counterexamples outside the contract; exhaustively compare eager, lazy, and Boolean-matrix engines on bounded finite systems; then return a Driver-grade PASS/KILL decision and exact downstream rewrite obligations. Do not decide the separate question whether the unresolved p-th-power collapse state should be the two-neighbour set {a^p,(a+1)^p}.",
  "dependencies": [
    {"target": "P023 composition-safe collapse", "action": "PRESSURE_TEST", "satisfied": true},
    {"target": "R009 deterministic downward collapse formalization", "action": "IMPACT_ONLY_DO_NOT_MODIFY", "satisfied": true},
    {"target": "R013 result/effectivity methodology", "action": "INFORM", "satisfied": true},
    {"target": "R014 exact semantic fibre/resource separation", "action": "INFORM", "satisfied": true},
    {"target": "user correction: paths are consumed; only results matter", "action": "AUTHORITATIVE_SEMANTIC_INPUT", "satisfied": true}
  ],
  "source_refs": [
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "EnterpriseMath/R009/* formalization targets",
    "GLOBAL_KNOWLEDGE journal checkpoint cb980467a70a2ce3312559bb77f5cb7c6bec4d4c"
  ],
  "evidence_status": "FOUNDATION_SEMANTICS_GATE",
  "last_progress_ref": "Driver derivation of union-preservation criterion and bounded Boolean-matrix sanity check",
  "last_progress_at": "2026-08-11T11:02:00+08:00",
  "hard_block": null,
  "tags": ["R015", "collapse", "branching", "result-support", "future-matrix", "powerset", "relation", "union-preservation", "Boolean-matrix", "P023", "R009", "foundation-gate"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R015"
}
-->

# R015 — Result-Support Branch Deferral Invariance

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / FOUNDATION SEMANTICS GATE / NOT CANONICAL`

## 0. Why this task exists

A proposed change to Enterprise Math collapse semantics is under consideration:

- do **not** force an unresolved state to choose a direction immediately;
- retain a set/support of currently possible results;
- allow future operations to split that support when they actually distinguish possibilities;
- allow branches that reach the same current state to coalesce because their path/history has been consumed.

The user has explicitly corrected the semantic target:

> **paths are consumed; what matters is the result.**

Therefore this task is **not** about witness/path identity. It is about exact preservation of final reachable-result support.

This is a foundation gate. Do not modify R009/P023 canonical semantics merely because bounded examples look good.

---

# 1. Frozen semantic contract

Work first in pure result-support semantics.

For sets `X,Y` and a future relation

`R subseteq X x Y`, define its support transformer

`Phi_R : P(X) -> P(Y)`

by

`Phi_R(A) = { y in Y | exists x in A, x R y }`.

Interpretation:

- `A` is the set of currently possible states/results;
- branch multiplicity is discarded;
- path identity/provenance is discarded after arrival at the current state;
- duplicate branches coalesce by set idempotence;
- only membership in the final reachable support is observable.

**Current-state sufficiency requirement:** every fact that may alter future evolution must already be encoded in the current state. If a supposedly consumed history can still change the future, the state space is underspecified and the result-support contract is violated rather than the theorem disproved.

Out of scope for the positive theorem unless separately typed:

- path counts / multiplicity;
- probabilities or normalized weights;
- costs accumulated along paths;
- provenance/history queries;
- quantum amplitudes/interference;
- any nonlinear global rule that reads the whole support in a way not represented by a relation on current states.

These out-of-scope semantics must be used as negative pressure tests, not silently folded into Boolean support.

---

# 2. Core theorem targets

Use ordinary mathematical language first. Do not claim novelty merely because the consequences are important to Enterprise Math.

## R015-T01 — arbitrary union preservation of relational lifting

For every family `(A_i)`, prove

`Phi_R(union_i A_i) = union_i Phi_R(A_i)`.

Include empty-family behavior where the chosen formalism permits it.

This is the algebraic statement that branch coalescence/materialization order does not matter for one future step.

## R015-T02 — composition/functoriality

For relations `R subseteq X x Y` and `S subseteq Y x Z`, prove

`Phi_{S o R} = Phi_S o Phi_R`.

State orientation conventions explicitly and test them.

## R015-T03 — finite-horizon eager/lazy invariance

For every finite future sequence `R_1,...,R_n` and every family of initial possibilities `(A_i)`, prove

`Phi_{R_n} ... Phi_{R_1}(union_i A_i)
 = union_i (Phi_{R_n} ... Phi_{R_1})(A_i)`.

Interpret this as exact equivalence of:

1. eager branch materialization with arbitrary intermediate support coalescence;
2. lazy unresolved-support preservation followed by later materialization;
3. direct execution of the composed future relation.

The result must hold for **all** finite horizons, not only the `2x2` examples that motivated the task.

## R015-T04 — characterization / converse

Let `T : P(X) -> P(Y)` be an arbitrary result transformer.

Prove the strongest correct iff statement of the form:

`branch-deferral invariance for all families  <=>  T preserves unions`.

Then pressure-test the representation theorem:

> a transformer preserving the required unions is exactly the relational direct-image transformer generated by its singleton behavior,
>
> `R_T(x,y) iff y in T({x})`.

Be precise about whether arbitrary unions, finite unions plus `T(empty)=empty`, or finiteness of `X` is required.

A weaker theorem is acceptable only if accompanied by a counterexample killing the stronger form.

## R015-T05 — Boolean future-matrix equivalence

For finite state sets, encode each relation as a Boolean adjacency matrix and support as a Boolean vector.

Prove that relational composition and support propagation agree with Boolean-semiring matrix multiplication, and that

`(v_1 OR v_2) M = (v_1 M) OR (v_2 M)`.

Extend to arbitrary finite OR and arbitrary finite matrix products.

The phrase **future matrix is identical** in this task means equality of the final Boolean reachable-result support for every initial support under the same composed future relation.

Do **not** substitute path-count matrix equality.

## R015-T06 — coalescence idempotence

Prove explicitly that duplicate branches may coalesce without changing result-support semantics:

`A union A = A`,

and that repeated arrival at one state does not alter any future support under the frozen relational contract.

This theorem is elementary but semantically important because it separates result support from multiplicity.

---

# 3. Necessary-boundary / kill tests

The task must try to break the theorem by changing exactly one semantic assumption at a time.

Produce minimal finite counterexamples for at least:

1. **hidden-history future:** two histories share one visible/current state but later evolution differs because history was not actually consumed;
2. **multiplicity-sensitive readout:** two branches arriving at one result differ from one branch;
3. **support-global nonlinear transformer:** e.g. an operation whose output depends on cardinality or simultaneous presence of multiple support states and therefore is not union-preserving;
4. **weighted/probabilistic semantics with discarded weights**;
5. **signed/amplitude semantics with cancellation/interference** or another exact example showing Boolean support cannot represent destructive combination.

For each failure classify:

- theorem failure;
- semantic-contract violation;
- wrong state type;
- need for a richer semiring/module/state carrier.

The goal is to know exactly what `paths are consumed; results matter` permits and forbids.

---

# 4. Strongest characterization target

Attempt to prove the following conceptual classification without overclaiming novelty:

`RESULT_SUPPORT_SAFE_FUTURES`

are precisely the current-state transformers whose powerset action is a complete join/union homomorphism, equivalently relational direct-image dynamics under the correct hypotheses.

Pressure-test this against established mathematics including:

- relational composition/direct image;
- nondeterministic transition systems and automata;
- Boolean-semiring reachability;
- powerset/Kleisli-style relational semantics;
- complete join-homomorphisms / union-preserving maps.

Expected generic-mathematics status is likely `ROOTING_SUCCESS / PRIOR_ART`; that does **not** reduce the importance of the Enterprise Math semantic consequence.

Novelty is not a success criterion here. Correctness and impact are.

---

# 5. Mandatory executable oracle

Build one small exact reference module, integer/Boolean only. No floating point.

It must implement three independent engines:

1. `eager_support_engine` — materialize branch support after every step and deduplicate;
2. `lazy_support_engine` — retain unresolved initial support and apply the composed relation at the end;
3. `boolean_matrix_engine` — propagate support through Boolean adjacency matrices.

All three must produce identical final support under the positive contract.

## 5.1 Exhaustive tests

At minimum:

- exhaust all relations on a 2-state set for future lengths through at least 4;
- exhaust all initial supports;
- exhaust all branch groupings/coalescence schedules that are distinct in representation but equal as set unions;
- exhaust arbitrary transformers `T : P(X)->P(Y)` for a tractable bounded case such as `|X|<=3, |Y|<=2`, and verify the union-preservation iff relational-representation classification;
- automatically search for and minimize counterexamples to each negative boundary.

The researcher may choose stronger bounds if practical but must report exact enumeration counts.

## 5.2 Property tests

Add randomized/property tests on larger finite state sets and longer horizons. These supplement but never replace the exhaustive bounded core.

## 5.3 Mutation tests

Deliberately introduce non-union-preserving transformers and verify that the oracle detects eager/lazy divergence rather than passing vacuously.

---

# 6. Impact test against current Enterprise Math

Do not modify canonical owners in this task. Produce an exact impact matrix only.

## P023

Current P023 calls a quotient unsafe when deterministic single-valued descent fails.

Determine whether the correct split is:

- `FUNCTIONAL_SAFE`: one coarse state has one coarse successor;
- `SUPPORT_SAFE`: one coarse state may have a set of possible successors, with exact result-support semantics;
- `SUPPORT_UNSAFE`: even the result-support contract fails because the future transformer is not union-preserving/current-state sufficient.

Identify exactly which P023 theorems remain true unchanged and which become special cases.

## R009

Do **not** replace downward `collapse` in this task.

Only identify what would have to change if a later task approves an unresolved/two-sided collapse carrier.

The separate proposition

`a^p < n < (a+1)^p  =>  unresolved collapse state = {a^p,(a+1)^p}`

is **not** part of R015 and must not be assumed.

## P018/P021/R013/R014

Map consequences narrowly:

- P018 precision projection versus support-valued projection;
- P021 result-support versus witness/multiplicity semantics;
- R013 effectivity/result contract wording;
- R014 eager materialization versus lazy symbolic support as implementation-resource alternatives only after exact semantic equivalence is established.

---

# 7. Prior-art / de-dup discipline

The generic set/relation/Boolean algebra is expected to be mature mathematics.

Return every core statement with one of:

- `ROOTING_SUCCESS / PRIOR_ART`
- `ENTERPRISE_SEMANTIC_SPECIALIZATION`
- `R015_SPECIFIC_FOUNDATION_IMPACT`
- `REJECT / COUNTEREXAMPLE`

Do not preserve novelty by renaming relational image, nondeterminism, Boolean reachability, powerset lifting, or join preservation.

The project-specific question is whether these established structures justify a **semantic rewrite of collapse execution**, not whether union preservation itself was newly discovered.

---

# 8. Deliverables

One consolidated package only:

1. `docs/R015_RESULT_SUPPORT_BRANCH_DEFERRAL_REPORT.md`
2. `experiments/r015_branch_deferral_oracle.py`
3. machine-readable theorem/counterexample matrix JSON
4. tests for the oracle
5. exact enumeration summary
6. P023/R009/P018/P021/R013/R014 impact matrix
7. final Driver routing recommendation

The report must separate:

- mathematical theorem status;
- executable evidence status;
- prior-art status;
- Enterprise semantic impact;
- canonical status.

---

# 9. Success / kill criteria

## PASS gate

Return

`RESULT_SUPPORT_BRANCH_DEFERRAL_PROVED / EXECUTABLE_EXHAUSTIVE_PASS / FOUNDATION_REWRITE_CANDIDATE / NOT_CANONICAL`

only if all of the following hold:

1. T01–T03 are proved for arbitrary finite future length / families under a clean relational/current-state contract;
2. the strongest correct T04 characterization is proved with assumptions explicit;
3. Boolean future-matrix equivalence T05 is proved;
4. executable engines agree exhaustively on the declared bounded universe;
5. mutation/negative tests find the expected divergences outside the contract;
6. no path/provenance assumption is smuggled back into result-only semantics;
7. the impact matrix identifies a coherent P023 rewrite without yet changing R009 collapse direction.

## KILL / FREEZE gate

Return

`RESULT_SUPPORT_BRANCH_DEFERRAL_KILLED / FOUNDATION_REWRITE_ABORT`

if a counterexample exists **inside the declared result-only, current-state-sufficient relational contract** such that eager and lazy branching produce different final support.

A counterexample that requires hidden history, multiplicity, probability, amplitude, or another excluded observable does not kill the theorem; it defines the semantic boundary.

---

# 10. Governance

- This task may prove, disprove, compute, browse prior art, and produce proposal diffs.
- It may **not** modify canonical R009/P023 semantics or promote a new collapse law.
- Do not create child taskbooks.
- Any proposal to change the actual collapse carrier is returned to the Driver as a non-dispatchable next-step candidate.
- CI: `CI_NOT_REQUIRED_FOR_RESEARCH`; local/exact executable evidence is required, but do not poll unrelated workflows.
