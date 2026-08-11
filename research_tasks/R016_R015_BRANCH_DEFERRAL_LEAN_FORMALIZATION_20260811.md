<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R016-R015-BRANCH-DEFERRAL-LEAN-FORMALIZATION",
  "title": "R016 R015 Branch-Deferral Lean Formalization",
  "kind": "FORMALIZATION",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Independently formalize the frozen generic core behind R015 result-support branch deferral: relational direct-image lifting preserves unions, composes exactly, yields eager/lazy support invariance, and characterizes union-preserving powerset transformers by singleton-generated relations under explicit hypotheses. Provide a finite Boolean future-matrix bridge without changing theorem statements merely to satisfy Lean.",
  "next_action": "Create a narrow Lean module from current main; formalize the target list L01-L10 with no sorry/admit/custom axiom; add finite executable/native_decide examples where appropriate; run the repository-pinned full build `lake build --wfail -KCI EnterpriseMath`; return exact proof/build evidence and any theorem-spec mismatch. Do not modify R009/P023 semantics and do not infer the separate two-neighbour collapse law.",
  "dependencies": [
    {"target": "RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE", "action": "FORMALIZE_FROZEN_GENERIC_CORE", "satisfied": true},
    {"target": "current Enterprise Math Lean toolchain", "action": "USE_PINNED", "satisfied": true},
    {"target": "R011 formalization experience", "action": "INFORM_API_DISCIPLINE", "satisfied": true}
  ],
  "source_refs": [
    "research_tasks/R015_RESULT_SUPPORT_BRANCH_DEFERRAL_INVARIANCE_20260811.md",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "lakefile.toml / lean-toolchain / lake-manifest.json on current main"
  ],
  "evidence_status": "LEAN_FOUNDATION_GATE",
  "last_progress_ref": "Driver theorem decomposition for result-support branch deferral",
  "last_progress_at": "2026-08-11T11:02:00+08:00",
  "hard_block": null,
  "tags": ["R016", "R015", "Lean", "formalization", "relation", "powerset", "union", "branch-deferral", "Boolean-matrix", "foundation-gate"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R016"
}
-->

# R016 — R015 Branch-Deferral Lean Formalization

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / LEAN FOUNDATION GATE / NOT CANONICAL`

## 0. Role and separation

R016 is an **independent formalization task**, not a second research owner.

It must not invent or weaken the mathematics in order to obtain a green build.

The generic core below is already sufficiently precise to formalize independently of the later R015 project-impact verdict. If R015 later finds a mathematical mismatch, R016 must report the mismatch rather than silently preserving an obsolete statement.

Do not modify R009/P023 canonical semantics in this task.

Do not assume or formalize the separate future proposal

`a^p < n < (a+1)^p -> unresolved collapse = {a^p,(a+1)^p}`.

---

# 1. Lean carrier and definitions

Prefer a minimal transparent definition rather than introducing a new project abstraction.

For types `α β`, define a relation as an ordinary predicate

`R : α -> β -> Prop`.

Define result-support lifting:

```lean
def RelSupport (R : α → β → Prop) (A : Set α) : Set β :=
  {y | ∃ x ∈ A, R x y}
```

Equivalent mathlib-native definitions may be used only if the theorem statements remain transparent and easy to audit.

Define relation composition with orientation stated explicitly, e.g.

```lean
def RelComp (R : α → β → Prop) (S : β → γ → Prop) : α → γ → Prop :=
  fun x z => ∃ y, R x y ∧ S y z
```

If mathlib already provides an exact compatible definition, use it; do not duplicate a large relation framework merely for naming.

---

# 2. Mandatory theorem targets

Names may change to fit repository style, but maintain a one-to-one mapping in the return report.

## R016-L01 — empty support

Prove:

`RelSupport R ∅ = ∅`.

## R016-L02 — binary union

Prove:

`RelSupport R (A ∪ B) = RelSupport R A ∪ RelSupport R B`.

## R016-L03 — arbitrary indexed union

Prove an arbitrary-family theorem equivalent to:

`RelSupport R (⋃ i, A i) = ⋃ i, RelSupport R (A i)`.

Handle universes/index types correctly. Do not weaken to finite union merely because elaboration is easier unless a genuine theorem-level obstruction is found.

## R016-L04 — relation composition

Prove:

`RelSupport (RelComp R S) A = RelSupport S (RelSupport R A)`.

This theorem must make composition orientation unambiguous.

## R016-L05 — two-branch deferral

Prove directly:

`RelSupport R (A ∪ B) = RelSupport R A ∪ RelSupport R B` as the semantic eager/lazy bridge, with the project-facing theorem name/documentation explaining branch deferral.

L05 may reuse L02; it exists as a named semantic theorem.

## R016-L06 — composed-future deferral

For two composed relations at minimum, prove:

`RelSupport S (RelSupport R (A ∪ B))
 = RelSupport S (RelSupport R A) ∪ RelSupport S (RelSupport R B)`.

Then provide an induction-ready generic theorem for a finite same-type relation list or an equivalent formulation sufficient to establish arbitrary finite horizon without unsafe dependent-type complexity.

If varying state types make a single list theorem awkward, formalize the generic arbitrary-union theorem plus composition theorem and explain why they compose structurally; do not introduce a complicated bespoke heterogeneous list only for optics.

## R016-L07 — union-preserving transformer representation

Define an explicit property such as

```lean
def PreservesArbitraryUnions (T : Set α → Set β) : Prop := ...
```

Prove the strongest clean theorem that a union-preserving transformer is determined by singleton images:

`T A = ⋃ x : A, T {x}`

under the exact hypotheses required.

Then define

`R_T x y : Prop := y ∈ T {x}`

and prove

`T A = RelSupport R_T A`.

Conversely prove every `RelSupport R` satisfies the chosen union-preservation property.

Return the exact iff statement obtained.

Do not hide an extra `T ∅ = ∅` requirement. If the chosen definition of arbitrary-union preservation already forces it, prove that explicitly or make the convention clear.

## R016-L08 — coalescence idempotence

Provide the semantic corollary that duplicated support does not change any relational future, e.g.

`RelSupport R (A ∪ A) = RelSupport R A`.

This may be a short theorem, but it must be present and documented as result-support rather than multiplicity semantics.

## R016-L09 — finite Boolean matrix bridge

Avoid depending on a fragile `Bool` semiring instance if unnecessary.

For finite indices, a Boolean future matrix may be represented directly as

`M : Fin n -> Fin m -> Prop`.

Define Boolean support-vector propagation by existential/AND semantics and Boolean matrix composition by

`(M ⋆ N) i k := ∃ j, M i j ∧ N j k`.

Prove:

1. matrix support propagation is extensionally the same as `RelSupport`;
2. Boolean matrix composition is extensionally the same as `RelComp`;
3. propagation distributes over support OR/union;
4. two-step matrix propagation is associative/extensional in the required sense.

Do not prove path-count matrix multiplication.

## R016-L10 — finite sanity examples

Add small finite examples/tests showing:

- two branches can coalesce to one current result and later rebranch with unchanged final support;
- a non-union-preserving support-global rule cannot be represented by the relational lifting theorem.

Use `example`, `decide`, `native_decide`, or focused executable tests as appropriate without turning the module into an experiment dump.

---

# 3. Proof integrity gate

Forbidden in the proof-bearing slice:

- `sorry`
- `admit`
- `axiom` or custom postulates introduced to close R016 targets
- commented-out failed theorem statements presented as evidence
- theorem weakening solely to make Lean pass

Run a static placeholder audit and return its exact result.

For every major theorem, include `#print axioms <theorem>` or an equivalent generated audit in the evidence packet. Standard Lean/mathlib logical foundations are acceptable; `sorryAx` or a custom project axiom is not.

---

# 4. Build gate

R016 is not complete on source inspection alone.

Use the repository-pinned toolchain from the branch base and run exactly:

```bash
lake build --wfail -KCI EnterpriseMath
```

The task may use focused `lake env lean ...` commands during repair, but the final gate is the full command above.

Do not report `LEAN_CHECKED` until the exact pinned build succeeds on the returned head.

CI workflow polling is not required for research. A successful local pinned build with exact toolchain/ref evidence is sufficient for the research return; canonical promotion may later require its own integration checks.

If only GitHub Actions has the pinned environment available, create one narrow validation PR and return the exact run/job/log evidence. Do not repeatedly poll unrelated workflows.

---

# 5. Repository placement

Preferred narrow owner-neutral placement:

- `EnterpriseMath/Precision/BranchDeferral.lean` or another existing appropriate Foundation/Precision namespace;
- import it from `EnterpriseMath.lean` only if needed for the final build and repository convention;
- optional small evidence file under `experiments/` only if generated audit output is useful.

Do not modify existing R009 theorem targets merely to reuse code.

Do not duplicate P023 owner theorems under a new truth source; this module proves generic support-valued relational facts and may later be imported by a P023 rewrite if Driver approves.

---

# 6. Counterexample discipline

If Lean exposes that a frozen target is false or requires an omitted mathematical hypothesis:

1. stop trying to coerce the proof;
2. construct the smallest exact counterexample in Lean if practical;
3. mark the target `THEOREM_SPEC_MISMATCH`;
4. return it to Driver/R015;
5. do not silently add a stronger precondition without documenting the mathematical change.

API/library mismatches are formalization issues; theorem counterexamples are mathematical issues. Keep them separate.

---

# 7. Deliverables

Return one compact formalization package:

1. Lean source diff / branch / commit / PR as applicable;
2. theorem mapping table `R016-L01..L10 -> Lean declaration`;
3. exact toolchain and dependency SHAs;
4. exact `lake build --wfail -KCI EnterpriseMath` output summary;
5. static placeholder audit;
6. `#print axioms` audit for core declarations;
7. any theorem-spec mismatch/counterexample;
8. final status line.

---

# 8. Success / failure statuses

Only return

`R015_BRANCH_DEFERRAL_CORE_LEAN_CHECKED / NO_SORRY / PINNED_BUILD_PASS / NOT_CANONICAL`

if all mandatory L01-L10 targets (or an explicitly Driver-acceptable equivalent for the finite-horizon formulation in L06) are proof-bearing and the exact pinned full build succeeds.

If source progress exists but build fails, return

`FORMALIZATION_PROGRESS / LEAN_BUILD_FAILED / CONTINUE_SAME_TASK / NO_PROMOTION`.

If a theorem target is mathematically false, return

`THEOREM_SPEC_MISMATCH / RETURN_TO_R015_DRIVER_REVIEW`.

No canonical or Foundation promotion is authorized by this taskbook.

---

# 9. Governance

- `created_by_role: RESEARCH_DRIVER`
- `task_authority: DRIVER_APPROVED`
- `identity_policy: AUTO_RESOLVE_OR_ALLOCATE`
- no fixed Researcher-ID in the taskbook;
- executing conversation allocates/preserves its own R016 identity;
- no child taskbooks;
- no R009/P023 semantic rewrite during formalization.
