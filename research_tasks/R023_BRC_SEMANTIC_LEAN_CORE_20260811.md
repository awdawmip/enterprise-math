<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R023-BRC-SEMANTIC-LEAN-CORE",
  "title": "R023 BRC Semantic Core Lean Formalization and Minimal Counterexample Gate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_FORMALIZATION",
  "frontier": "Formalize the narrow semantic core that survived R021: no-resurrection, unique coarsest one-step repair, exact Boolean support branch invariance, suffix-safe forgetful recoalescence, and the two minimal composition/correlation counterexamples, without elevating the representation Pareto layer into a foundation primitive.",
  "next_action": "Translate the frozen R021 statements into minimal Lean definitions, prove or sharply correct the four core theorems, encode the two finite counterexamples, and return the exact weakest-assumption theorem surface suitable for later integration.",
  "dependencies": [
    {
      "target": "RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS",
      "action": "CONSUME_FROZEN_R021_SEMANTIC_CORE_AT_7c19a4aeca01319065fd731962597f1f1e6cb9d5",
      "satisfied": true
    },
    {
      "target": "R015/R016 relational result-support core",
      "action": "REUSE_UNION_PRESERVING_RELATIONAL_SEMANTICS_WHERE_COMPATIBLE",
      "satisfied": true
    },
    {
      "target": "P023 deterministic future-safe theorem family",
      "action": "PRESERVE_DETERMINISTIC_BASELINE_AND_AVOID_SEMANTIC_REDEFINITION",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R021 owner checkpoint 7c19a4aeca01319065fd731962597f1f1e6cb9d5",
    "R021 Draft PR #496",
    "docs/R021_BRANCHING_COLLAPSE_REPORT.md at R021 owner checkpoint",
    "experiments/r021_theorem_counterexample_matrix.json at R021 owner checkpoint",
    "R021 oracle/test evidence: 16/16 focused tests PASS"
  ],
  "evidence_status": "BRC_SEMANTIC_LEAN_FORMALIZATION_GATE",
  "last_progress_ref": "R021 complete return accepted for narrow formalization review",
  "last_progress_at": "2026-08-11T18:16:00+08:00",
  "hard_block": null,
  "tags": [
    "R023",
    "BRC",
    "branch-recoalescence-collapse",
    "Lean",
    "no-resurrection",
    "support-semantics",
    "recoalescence",
    "counterexample"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R023",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R023 — BRC Semantic Core Lean Formalization and Minimal Counterexample Gate

Status: `READY / P0 / FOUNDATIONAL_FORMALIZATION / NOT CANONICAL`

## 1. Mother question

R021 found a real but sharply scoped Branch-Recoalescence Collapse regime. The next question is not whether the whole R021 report can be encoded in Lean. It is:

> can the smallest semantic theorem package that separates exact pointwise information from exact Boolean/result-support branching be stated with clean types, proved with weak assumptions, and accompanied by machine-checked minimal counterexamples?

The target is a narrow theorem surface. Representation-size Pareto claims, engineering heuristics, branch-budget optimization, cryptanalytic source structure, multiplicity, provenance, probability weights, and signed/amplitude cancellation are outside this gate.

## 2. Frozen semantic distinctions

Preserve the following type distinctions throughout:

- fine point `x : X`;
- coarse observation `q x`;
- exact support `A ⊆ X`;
- branch atom/token with an explicit denotation into `Set X` or equivalent exact carrier;
- live branch configuration whose meaning is the union of branch denotations;
- final observable support;
- future language as finite words of deterministic maps or relations.

Do not model a coarse cell label as though it were automatically the exact full-fibre support. Do not use an uncharged hidden token to recover erased point identity.

For the positive branch theorem, the default observable is Boolean/set-valued final support and the transition semantics must preserve unions.

## 3. R023-T01 — minimal formal definitions

Build only the definitions needed by the theorem package. Prefer factorization/kernel formulations over a large partition library when they express the same mathematics more directly.

At minimum provide formal objects for:

1. declared future signature of a fine point;
2. one-step coarse successor-support signature;
3. complete runtime encoder for a pointwise computation;
4. exact branch denotation and configuration union;
5. relational direct image / finite-word execution;
6. remaining-suffix support signature;
7. operational notion of a support replacement being safe for a remaining language.

Definitions must be reusable independently of the R021 Python oracle.

## 4. R023-T02 — NO_RESURRECTION

Formalize and prove the information boundary:

If all exact pointwise answers for the declared future language are computed only from a complete runtime encoding `e x`, then

`e x = e y -> Sigma_U x = Sigma_U y`.

Also expose the contrapositive/corollary form:

`Sigma_U x != Sigma_U y -> e x != e y`.

The theorem must quantify over the complete runtime encoding, so branch IDs, correlation IDs, hidden coordinates, or other metadata cannot sit outside the charged information object.

A proof that assumes injectivity of `e` is too strong and misses the point. Seek the weakest factorization hypothesis actually needed.

## 5. R023-T03 — ONE_STEP_COARSEST

Formalize the unique coarsest one-step deterministic repair of a coarse observation.

For one generator/relation `g`, define the one-step key

`K_g(x) = (q(x), sigma_g(x))`

where `sigma_g` is the next coarse successor-support.

Prove both directions of the universal property:

1. `K_g` itself is sufficient to recover `q` and the next coarse successor-support;
2. every deterministic classifier/refinement from which both are recoverable must refine the kernel of `K_g`.

The preferred statement is a factorization/kernel theorem rather than an implementation-specific partition theorem.

If a genuinely weaker assumption than R021's prose statement is discovered, use it and record the change precisely.

Optional only if it reuses the same infrastructure with little extra machinery: the analogous static declared-future key `(q, Sigma_U)`. Do not let this optional theorem delay the required gate.

## 6. R023-T04 — SUPPORT_BRANCH_INVARIANT

Formalize the positive BRC support theorem.

For exact branch denotations and union-preserving relational execution, prove that:

- splitting a support into exact sub-supports does not change its union;
- relational direct image commutes with union;
- replacing several exact branches by an exact token denoting their literal union does not change the represented support;
- by induction over a finite future word, split / execute / lossless-union recoalescence returns exactly the same reachable fine support as direct fine support execution.

The theorem must not claim multiplicity, provenance, probability, or signed cancellation preservation.

Prefer a theorem whose core union-preservation statement does not require finiteness of `X` if Lean permits it cleanly; finite executable examples may remain finite.

## 7. R023-T05 — FORGETFUL_RECOALESCENCE_IFF

Formalize the lossy/hull replacement boundary without making the theorem true merely by definition.

Define operational suffix-safety first:

A replacement `A -> H` is safe for remaining language `V` when every declared suffix produces the same final observable support from `A` and `H`.

Then define the corresponding remaining support signature and prove:

`safe_V(A,H) <-> Sigma_V^P(A) = Sigma_V^P(H)`.

Add a concrete machine-checked example showing that equality of the current coarse observation alone does not imply suffix-safety.

## 8. R023-T06 — three-state quotient-composition counterexample

Encode the frozen R021 witness with three fine states:

`q(0)=q(1)=0`, `q(2)=1`;
`f(0)=0`, `f(1)=2`, `f(2)=0`.

Starting from the full fibre over coarse state `0`, prove in Lean that exact two-step fine execution has final coarse support `{0}`, while two repeated applications of the naive existential quotient relation admit `{0,1}`.

The artifact must make the distinction between one-step exactness and repeated coarse composition explicit.

Do not claim global minimality from Lean alone. The bounded `n<3` minimality evidence remains the R021 exhaustive oracle result unless this task separately formalizes the enumeration.

## 9. R023-T07 — middle-incidence correlation counterexample

Encode a smallest finite composition example in which:

- the first relation reaches middle witness `b1`;
- the second relation departs from a different middle witness `b2`;
- coarse/nonempty middle marginals appear compatible;
- exact relational composition is empty.

Prove that erasing middle identity/correlation can introduce a spurious composite result.

Use this only as the carrier-lift warning: result-support semantics is exact for union/existential questions, but future observables that require middle identity or provenance need a richer carrier.

## 10. R023-T08 — theorem-surface audit

For every theorem, record:

- Lean declaration name;
- exact assumptions;
- whether the statement is stronger, equal, or weaker than the R021 prose claim;
- dependence on finiteness, decidable equality, classical logic, or choice;
- whether the theorem belongs to generic mathematics/prior art or is an Enterprise collapse specialization;
- the exact semantic observable preserved.

Reject any proof that succeeds only because an intended semantic distinction was collapsed by the formal definitions.

The final target declarations must contain no `sorry`, `admit`, or task-local axioms standing in for a required R023 theorem.

## 11. Required artifacts

Return a compact package containing:

1. one or more Lean modules for the theorem package;
2. a concise `R023_BRC_LEAN_RETURN.md`;
3. a theorem-status table mapping R021 claim IDs to Lean declaration names;
4. the two finite counterexamples as checked declarations/examples;
5. any focused tests or small executable helpers genuinely required by the formalization.

Do not formalize the R021 representation Pareto table in this gate.

## 12. PASS / CORRECTION / KILL criteria

Preferred PASS:

`BRC_SEMANTIC_CORE_LEAN_CHECKED / NO_RESURRECTION_CHECKED / ONE_STEP_COARSEST_CHECKED / SUPPORT_BRANCH_INVARIANT_CHECKED / FORGETFUL_RECOALESCENCE_CHECKED / COUNTEREXAMPLES_CHECKED / NOT_CANONICAL`

A mathematically useful correction is also a successful return when Lean exposes a missing hypothesis or an overstrong R021 statement. Return:

`BRC_FORMALIZATION_CORRECTION_FOUND`

with the weakest corrected theorem and a precise explanation of what changed.

Return a negative result if any target theorem is false under the intended definitions. Provide the smallest counterexample or missing assumption rather than weakening definitions until the statement becomes tautological.

## 13. Downstream decision requested from the researcher

At return, recommend exactly one of:

- `READY_FOR_NARROW_SHARED_SURFACE_INTEGRATION`;
- `KEEP_AS_RESEARCH_TOOL_ONLY`;
- `FOUNDATION_QUESTION_REQUIRED`.

The recommendation must be based on the formal theorem boundary, not on the attractiveness of the BRC terminology.
