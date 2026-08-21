<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R063-STAGE2-MULTIPLICATIVE-PATH-NORM-ROOT-PROVENANCE-ALGEBRA",
  "title": "R063 Stage 2 — Multiplicative Path-Norm-Root Provenance Algebra",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_TOWER_CLASSIFICATION",
  "next_action": "Freeze the Stage 2 semantic claim ledger, define the provenance/root/trace/path tower, and prove or falsify exact multiplication descent before making any path-level lift claim.",
  "dependencies": [
    "RS-R063-STAGE1-GENERAL-NON-SQUARE-PATH-NORM-ROOT-DISCOVERY"
  ],
  "source_refs": [
    "research/r063-stage1-general-path-norm-root@65f4e98cd707c634d805f2a9ec7c41f24ab06185",
    "driver_reviews/R063_STAGE1_GENERAL_PATH_NORM_ROOT_DRIVER_REVIEW_20260821.md@fb2331b0602e74cae506ebac49c4582e7147479d"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "R063",
    "path-norm-root",
    "Gaussian",
    "provenance",
    "multiplication",
    "trace",
    "path-fiber"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R063S2",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5683a6782b9af905fb74e78425be8b1b6373977856368b52c46710b439fb4467",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R063 Stage 2 — Multiplicative Path-Norm-Root Provenance Algebra

Task-ID: `RS-R063-STAGE2-MULTIPLICATIVE-PATH-NORM-ROOT-PROVENANCE-ALGEBRA`

Driver: `EM-DVR-R63A21 / CONTROL_PLANE`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity lane: `R063S2`

Intended owner branch:

`research/r063-stage2-multiplicative-provenance-algebra`

## 0. Read first / frozen inputs

Read and treat as frozen inputs:

1. `driver_reviews/R063_STAGE1_GENERAL_PATH_NORM_ROOT_DRIVER_REVIEW_20260821.md` at acceptance commit `fb2331b0602e74cae506ebac49c4582e7147479d`;
2. R063 Stage 1 frozen owner payload `research/r063-stage1-general-path-norm-root@65f4e98cd707c634d805f2a9ec7c41f24ab06185`;
3. `research_tasks/R063_STAGE1_GENERAL_NON_SQUARE_PATH_NORM_ROOT_DISCOVERY_20260821.md` source `6a3c104f5e3a46125ccec6d591de6b824cf8dae9`;
4. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
5. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`;
6. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`;
7. current `native_semantics_admissibility.json`.

Freeze from Stage 1:

- for every positive integer `N`, integer-addressed component roots are constructively generated from integer factorization and Gaussian prime allocation;
- support is nonempty iff every prime `q == 3 mod 4` has even exponent;
- the signed Gaussian norm-root generator is complete;
- ordered nonnegative component roots are the Stage 1 return fiber;
- every component root `(a,b)` pathifies to the frozen R061 trace with exact cardinality `binom(a+b,a)`;
- native path multiplicity and algebraic derivation multiplicity are distinct;
- BRC is downstream only;
- Stage 1 is accepted only at the frozen R061 sector-local semantic strength.

Do not reopen R061, R062, R063 Stage 0 or R063 Stage 1 unless an exact contradiction is found under the same premises.

## 1. Hard objective

Classify the multiplicative structure exposed by the Stage 1 Gaussian factorization layer and determine exactly how far it descends through:

`factorization provenance -> signed Gaussian root -> unit-orbit component root -> native trace -> native path fiber -> N multiplicity -> Boolean support`.

Hard target:

`MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_TOWER_CLASSIFIED`.

The stage must not assume that a multiplication law at one layer automatically induces a canonical multiplication law at every lower-information layer.

## 2. Semantic-scope gate — mandatory before theorem promotion

Before using `native`, `intrinsic`, `canonical`, `root algebra`, or equivalent strong language in the final classification, create a machine-readable claim ledger.

At minimum type:

- integer input and factorization data;
- `Z[J]` / Gaussian factorization carrier;
- split-prime exponent-allocation provenance;
- units and conjugation;
- ordered nonnegative component-root representatives;
- frozen R061 trace identity;
- native path fiber;
- radical scalar `sqrt(N)`;
- R062 enriched/Boolean projections.

The Stage 2 theorem scope is initially frozen as:

`FROZEN_R061_SECTOR_LOCAL_PYTHAGOREAN_TRACE_SEMANTICS`.

The Gaussian carrier is a sector-local factorization/component algebra for this stage. It is not automatically a global full-plane native multiplication law.

The unresolved authority difference between the project-level undirected-axis formulation and the later three-positive-ray local foundation is a declared scope boundary. Do not resolve it by silently editing either ontology inside this task.

Required ledger verdicts must distinguish at least:

- `NATIVE_ADMISSIBLE`;
- `CONDITIONAL_DERIVED`;
- `READOUT_ONLY`;
- `SEMANTIC_MISMATCH`;
- `UNRESOLVED`.

## 3. Define the multiplicative tower exactly

Construct precise typed objects and maps. A recommended minimum tower is:

`Prov(N) -> SRoot(N) -> URoot(N) -> GRoot_E(N) -> Trace_E(N) -> Path_E(N)`.

### 3.1 Provenance carrier

Define `Prov(N)` so that one element records enough exact factorization data to reproduce one signed Gaussian root channel, including:

- integer prime exponents of `N`;
- fixed ramified contribution from `2`;
- fixed inert contribution for `q == 3 mod 4` when supported;
- for every split prime `p == 1 mod 4`, the allocation of exponent between `pi_p` and `conjugate(pi_p)`;
- the Gaussian unit.

Define exact evaluation

`ev_N : Prov(N) -> SRoot(N)`.

### 3.2 Signed root carrier

Define

`SRoot(N)={z in Z[J] : Norm(z)=N}`.

Retain the Stage 1 completeness theorem as a frozen input rather than reproving it from brute enumeration.

### 3.3 Unit-orbit root carrier

Let `U={1,J,-1,-J}`.

Define the quotient

`URoot(N)=SRoot(N)/U`.

Classify whether the canonical first-quadrant representative gives an exact bijection from `URoot(N)` to the Stage 1 ordered-nonnegative component-root fiber.

Important boundary:

**quotient by units only unless a stronger quotient is separately proved and declared.**

Do not silently quotient by conjugation or component swap. In general `(a,b)` and `(b,a)` remain distinct Stage 1 ordered component roots.

### 3.4 Trace and path carriers

Map each ordered component root to the frozen sector trace

`T_{a,b}^{(ij)}`

and its path fiber

`Sh_{a,b}(X_i,X_j)`.

Preserve the distinction:

`TRACE_IDENTITY != PATH_REPRESENTATIVE`.

## 4. Provenance multiplication

For supported positive integers `A,B`, construct an exact multiplication operation

`mu_Prov : Prov(A) x Prov(B) -> Prov(AB)`

by combining prime exponents, split-prime allocations and units.

Prove or falsify, with exact counterexamples if required:

1. evaluation multiplicativity:
   `ev_AB(mu_Prov(P,Q)) = ev_A(P) * ev_B(Q)`;
2. associativity;
3. commutativity at the appropriate typed/equivalence level;
4. the identity object at norm `1`;
5. surjectivity onto every valid `Prov(AB)` / signed-root channel under the exact chosen provenance definition;
6. compatibility with the norm grading:
   `Norm(zw)=Norm(z)Norm(w)`.

If raw provenance retains ordered factor-origin labels, distinguish strict commutativity from commutativity only after a declared provenance relabeling.

## 5. Exact multiplicative provenance-fiber count

For a split prime `p == 1 mod 4`, let

`alpha=v_p(A)`,

`beta=v_p(B)`,

and let a target `AB` Gaussian channel allocate total exponent `t` to `pi_p`.

Prove or falsify the local preimage-count candidate

`m_p(alpha,beta;t)`

`= max(0, min(alpha,t)-max(0,t-beta)+1)`.

This counts solutions of

`i+j=t`,

`0<=i<=alpha`,

`0<=j<=beta`.

Then prove or falsify the global fixed-signed-target candidate

`PreimageCount(A,B,target)`

`= 4 * product_{p == 1 mod 4} m_p(v_p(A),v_p(B);t_p)`

under the exact unit convention adopted by the stage.

The factor `4` is a theorem candidate, not a free assumption. If unit normalization, axis cases or target representative conventions modify it, preserve the smallest counterexample and replace it by the weakest exact corrected formula.

Required output: an exact primewise certificate explaining every factor in the final formula.

## 6. Component-root multiplication after unit quotient

Determine whether Gaussian multiplication descends canonically to `URoot`:

`[z]_U star [w]_U = [zw]_U`.

If yes, prove:

- well-definedness independent of unit representatives;
- associativity;
- commutativity;
- norm-1 identity;
- norm grading `URoot(A) x URoot(B) -> URoot(AB)`;
- exact relationship to canonical first-quadrant ordered component representatives.

Write the representative-level component formula explicitly. For

`z=a+bJ`, `w=c+dJ`,

the raw product is

`(ac-bd)+(ad+bc)J`.

The canonical ordered-nonnegative representative must be obtained only through the proved unit action, not by an untyped absolute-value shortcut if that shortcut changes the quotient semantics.

Conjugation/component swap remains a separate involution unless explicitly quotiented.

## 7. Trace product classification

If the unit-orbit component product is exact, define and classify a sector-local trace product

`T_r odot T_s = T_{r star s}`

with grading

`Trace_E(A) x Trace_E(B) -> Trace_E(AB)`.

Prove whether this product is well defined on frozen R061 component-trace identity.

Do not identify this trace product with concatenation of path words. Multiplying component roots and concatenating native movement words are different operations unless a theorem connects them.

## 8. Central discriminator: does multiplication lift canonically to native paths?

This is the main Stage 2 research question.

Given component roots

`r in GRoot_E(A)`, `s in GRoot_E(B)`,

and product root

`r star s in GRoot_E(AB)`,

classify whether there exists any **canonical, non-arbitrary, typed** multiplication/lift

`Path_E(r) x Path_E(s) -> Path_E(r star s)`

or an exact relation/functor with a clearly declared codomain and information loss.

Investigate at least:

- direct word concatenation;
- shuffle/interleaving constructions;
- tensor or Cartesian-product provenance followed by a deterministic readout;
- substitution/transducer constructions induced by the component product;
- provenance-labelled path products before forgetting provenance;
- quotient/relation-valued lifts when no single-valued map is canonical.

No construction is accepted merely because its cardinalities fit on selected examples.

A valid lift must state:

- domain and codomain;
- dependence on factorization provenance, units, component orientation and path order;
- associativity/commutativity status;
- whether it respects trace projection;
- whether it is choice-independent under the declared semantics.

## 9. Mandatory path-multiplicity no-go gate

The frozen Stage 1 witness must be used as a theorem discriminator:

`A=2`, `B=2`, `AB=4`.

At the component-root level, the relevant product reaches `(0,2)` after unit normalization.

The Stage 1 audit has:

`multiplicative derivation pair count = 4`,

while

`native path multiplicity of (0,2) = binom(2,0)=1`.

Therefore prove explicitly:

`NATIVE_PATH_MULTIPLICITY_IS_NOT_MULTIPLICATIVE_UNDER_ROOT_PRODUCT`.

Also test the broader naive candidate

`|Path(r star s)| = |Path(r)| * |Path(s)|`.

Preserve the smallest exact counterexample if it is even smaller under the final conventions.

This negative result does **not** by itself kill a many-to-one or provenance-enriched path product. It only forbids identifying multiplicative derivation multiplicity with native shuffle multiplicity.

## 10. Separate every multiplicity layer

Maintain distinct fields for at least:

1. `GAUSSIAN_CHANNEL_MULTIPLICITY`;
2. `MULTIPLICATIVE_FACTOR_PAIR_PREIMAGE_MULTIPLICITY`;
3. `UNIT_ORBIT_MULTIPLICITY`;
4. `ORDERED_COMPONENT_ROOT_COUNT`;
5. `TRACE_IDENTITY_COUNT`;
6. `NATIVE_PATH_MULTIPLICITY=binom(a+b,a)`;
7. R062 `N_BRC` multiplicity;
8. R062 Boolean support.

Search for accidental equalities between these counts, but do not promote coincidence to a law.

For every proposed equality, preserve the smallest counterexample if false.

## 11. R062 compatibility — downstream only

Only after the Stage 2 root/trace/path product classification is fixed may R062 be applied.

Where a lawful path-level multiplication or relation exists, determine whether the projections

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

commute with the Stage 2 product in any exact sense.

If no canonical native path multiplication exists, classify the strongest exact surviving diagram at the provenance, trace, multiplicity or Boolean-support level instead of inventing a path product.

BRC must not be used to choose Gaussian roots, define unit normalization or manufacture path multiplication.

## 12. Deterministic checker — mandatory

Create an executable exact-arithmetic checker, preferably:

`scripts/r063_stage2_validate_multiplicative_provenance_algebra.py`.

The checker must:

- consume/replay the frozen Stage 1 generator rather than duplicating a divergent root-discovery theory;
- use exact integer/Gaussian arithmetic only for theorem decisions;
- construct provenance multiplication independently of brute factor-pair target lookup;
- verify evaluation multiplicativity;
- verify the unit quotient/product laws on the tested domain;
- verify the primewise preimage-count formula or preserve the smallest counterexample;
- keep every multiplicity field separate;
- test every proposed path-level lift against exact trace projection and cardinality constraints;
- preserve smallest counterexamples for every rejected multiplication law;
- return nonzero on any unclassified mismatch.

## 13. Regression scope

Mandatory base set:

`B={1,2,5,13,17,25,65}`.

Audit every ordered pair `(A,B)` from this set.

Then run an exhaustive exact pair regression over at least

`1<=A,B<=128`.

If comfortably feasible, extend to

`1<=A,B<=256`.

Also use a deterministic sparse suite of supported and unsupported factors whose products reach at least the `10^12` scale, while avoiding any float-based classification.

For every tested pair, record:

- factorization of `A`, `B`, `AB`;
- support status;
- signed-root channel counts;
- provenance-product image and preimage counts;
- unit-orbit component roots;
- trace products;
- relevant path cardinalities;
- all rejected-law counterexamples.

## 14. Required outputs

At minimum produce:

1. `scripts/r063_stage2_validate_multiplicative_provenance_algebra.py`;
2. `research_results/R063_STAGE2/R063_STAGE2_SEMANTIC_SCOPE_CLAIM_LEDGER.json`;
3. `R063_STAGE2_PROVENANCE_ALGEBRA_THEOREM.md`;
4. `R063_STAGE2_PROVENANCE_FIBER_COUNT_CERTIFICATE.json`;
5. `R063_STAGE2_UNIT_QUOTIENT_COMPONENT_ROOT_MONOID.md`;
6. `R063_STAGE2_TRACE_PRODUCT_CLASSIFICATION.md`;
7. `R063_STAGE2_PATH_MULTIPLICATIVE_LIFT_OR_NO_GO.md`;
8. `R063_STAGE2_MULTIPLICITY_SEPARATION_CERTIFICATE.json`;
9. `R063_STAGE2_BRC_COMPATIBILITY_DIAGRAM.md`;
10. `R063_STAGE2_REGRESSION.json`;
11. `R063_STAGE2_MISMATCHES.json`;
12. `R063_STAGE2_REPRODUCIBILITY_PROOF.md`;
13. `R063_STAGE2_FINAL_CLASSIFICATION.md`.

The result directory may contain additional compact certificates when needed, but the listed outputs are mandatory.

## 15. Acceptance gates

Stage 2 passes only if every applicable gate is classified:

1. `SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE`;
2. `R063_STAGE1_FROZEN_DEPENDENCY_REPLAY_INTACT`;
3. `PROVENANCE_MULTIPLICATION_EXACT_OR_FALSIFIED`;
4. `PROVENANCE_ASSOCIATIVITY_COMMUTATIVITY_UNIT_CLASSIFIED`;
5. `EVALUATION_MULTIPLICATIVITY_AND_SIGNED_ROOT_SURJECTIVITY_CLASSIFIED`;
6. `PROVENANCE_FIBER_COUNT_FORMULA_EXACT_OR_MINIMAL_COUNTEREXAMPLE_WITH_CORRECTED_STATEMENT`;
7. `UNIT_QUOTIENT_COMPONENT_ROOT_MULTIPLICATION_WELL_DEFINED_OR_FALSIFIED`;
8. `TRACE_PRODUCT_CLASSIFIED`;
9. `CANONICAL_PATH_MULTIPLICATIVE_LIFT_OR_STRONGEST_NO_GO_CLASSIFIED`;
10. `NATIVE_PATH_MULTIPLICITY_NONMULTIPLICATIVITY_PROVED`;
11. `ALL_MULTIPLICITY_LAYERS_SEPARATED`;
12. `BRC_DOWNSTREAM_COMPATIBILITY_OR_NO_GO_CLASSIFIED`;
13. `NO_GLOBAL_FULL_PLANE_MULTIPLICATION_OVERCLAIM`;
14. `DETERMINISTIC_CHECKER_PASS_OR_MINIMAL_UNCLASSIFIED_COUNTEREXAMPLE_PRESERVED`.

## 16. Final classification options

Use the strongest result actually proved. Examples:

- `MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_TOWER_CLASSIFIED_WITH_UNIT_QUOTIENT_MONOID_AND_CANONICAL_PATH_LIFT`;
- `MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_TOWER_CLASSIFIED_WITH_UNIT_QUOTIENT_MONOID_AND_PATH_LIFT_NO_GO`;
- `SIGNED_GAUSSIAN_PROVENANCE_AND_COMPONENT_ROOT_MULTIPLICATION_COMPLETE_BUT_PATH_MULTIPLICATION_NONCANONICAL`;
- `MULTIPLICATIVE_PROVENANCE_EXTENSION_PARTIAL_WITH_MINIMAL_COUNTEREXAMPLE`;
- another strictly evidenced classification of equal or greater precision.

Finite regression cannot by itself promote a theorem. The ordinary mathematical proof and the deterministic evidence must agree.

## 17. Stop rule

After all Stage 2 evidence and the final classification are committed on the owner line, stop for Driver review.

Do not open R063 Stage 3.
