<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION",
  "title": "Prime Fusion F1 — Lean Finite-Algebra Formalization",
  "kind": "FORMALIZATION",
  "owner": "formalization/prime-fusion-f1-finite-algebra",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED_NO_SORRY_PINNED_BUILD_PASS",
  "next_action": "Formalize the accepted Prime Fusion finite-algebra kernel in the repository-pinned Lean/mathlib environment: channel identities and gcd law, polynomial/CRT fusion algebra, pointed quotient and channel recovery, reciprocal-trace idempotent split, corrected channel-oriented mixed-locus orbit, sixth-power readout, and the minimal interfaces needed by later reconstruction/finite-quotient layers. Produce proof-bearing Lean with no sorry/admit/custom axioms, run the pinned full build, freeze exact declaration/build/axiom evidence, and stop without changing theorem content.",
  "dependencies": [
    "driver_reviews/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_DRIVER_REVIEW_20260824.md@86df3a53417ddc810b3c51ac906288b54bef5e63",
    "research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md@blob:055bdaaca81c5ac7ab350a71acf3b69fe5e564a9",
    "research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md@blob:54d1fbb8c3fb657ac55f556c982501386a8eaf25",
    "research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv@blob:3c9f6fa670f9405eebbab6eae5d5374c2de4a037",
    "EnterpriseMath.lean@28da4d402864923269df6af56f8ef2c487ee4be2",
    "lakefile.toml@28da4d402864923269df6af56f8ef2c487ee4be2",
    "lean-toolchain@28da4d402864923269df6af56f8ef2c487ee4be2"
  ],
  "source_refs": [
    "driver_reviews/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_DRIVER_REVIEW_20260824.md@86df3a53417ddc810b3c51ac906288b54bef5e63",
    "integration/prime-fusion-evidence-typed-package:research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md#blob=055bdaaca81c5ac7ab350a71acf3b69fe5e564a9",
    "integration/prime-fusion-evidence-typed-package:research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md#blob=54d1fbb8c3fb657ac55f556c982501386a8eaf25",
    "integration/prime-fusion-evidence-typed-package:research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json#blob=6b388f3b17eddf1443de12ec6cf9f6db3e6999c2",
    "driver_handoffs/PROJECT_RESULT_LEVELS_AND_FORMALIZATION_QUEUE_20260823.md@a404d271bd30a713218d38838ef3d063d1afcadf",
    "lakefile.toml@28da4d402864923269df6af56f8ef2c487ee4be2",
    "lean-toolchain@28da4d402864923269df6af56f8ef2c487ee4be2"
  ],
  "evidence_status": "F1_FORMALIZATION_ADMITTED_BY_DRIVER_ACCEPTED_PACKAGE",
  "last_progress_ref": "driver_reviews/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_DRIVER_REVIEW_20260824.md@86df3a53417ddc810b3c51ac906288b54bef5e63",
  "last_progress_at": "2026-08-24T12:58:00+08:00",
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "F1",
    "Lean",
    "formalization",
    "finite-algebra",
    "CRT",
    "ZMod",
    "idempotent",
    "mixed-locus",
    "no-sorry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFF1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE",
  "successor_gate": {
    "new_information_gap": "The corrected fifteen-theorem package is mathematically accepted and independently audited, but its finite-algebra core is not yet represented as proof-bearing Lean declarations in the project kernel. Written proofs and Python checkers do not establish elaboration, type correctness, imported-library compatibility, or axiom cleanliness of the corresponding Lean statements.",
    "why_parent_result_does_not_close_it": "The parent task froze accurate source text, evidence typing, dependency structure, and executable audit composition. It explicitly did not translate the mathematics into Lean or verify that the theorem interfaces can be expressed without hidden assumptions in the pinned Lean/mathlib environment.",
    "discriminating_outcomes": [
      "the accepted finite-algebra kernel is formalized with no sorry/admit/custom axioms and the pinned full build passes",
      "Lean exposes an exact theorem-spec/interface mismatch requiring return to Driver rather than silent hypothesis changes",
      "the mathematics remains sound but a library/API representation obstruction prevents completion and is isolated without weakening theorem statements"
    ],
    "kill_condition": "If any target can be proved only by changing the corrected T10 universe, adding an unreviewed mathematical hypothesis, replacing a retained theorem by a weaker statement, introducing a custom axiom, or treating a finite computation as proof of a general theorem, stop and return the exact obstruction.",
    "alternative_route_or_free_exploration_considered": "Publication/package review was the other user-authorized route. It remains available after formalization. F1 was selected first because its admission gate is now explicitly satisfied and a proof-kernel translation can expose statement/API defects before publication-facing polishing without reopening mathematical research.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The package-freeze task is complete and should not be reopened for implementation work. A separate formalization task preserves the distinction between accepted mathematics and machine-checked representation while providing a falsifiable build/axiom gate."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion F1 — Lean Finite-Algebra Formalization

Status: `READY / DRIVER_APPROVED / F1 FORMALIZATION / NO NEW MATHEMATICS`

Task-ID:

`RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION`

Owner branch:

`formalization/prime-fusion-f1-finite-algebra`

Hard target:

`PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED_NO_SORRY_PINNED_BUILD_PASS`

## 0. Scope

This task translates an already accepted theorem package into Lean. It is not a theorem-discovery task and must not change the mathematics to obtain a build.

The authoritative mathematical source is the corrected evidence-typed package whose Git blob is

`055bdaaca81c5ac7ab350a71acf3b69fe5e564a9`.

The authoritative dependency structure is the frozen non-linear graph whose Git blob is

`54d1fbb8c3fb657ac55f556c982501386a8eaf25`.

The repository toolchain at task start is:

- Lean `leanprover/lean4:v4.33.0-rc2`;
- mathlib revision `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`.

Use the pinned project environment. Reuse mathlib-native polynomial, quotient, CRT, `ZMod`, finite-field, gcd and order APIs where they fit transparently. Do not build a competing general algebra library merely for Prime Fusion naming.

## 1. Repository placement

Create a dedicated namespace/directory:

`EnterpriseMath/PrimeFusion/`

Preferred module split:

1. `EnterpriseMath/PrimeFusion/Channels.lean`;
2. `EnterpriseMath/PrimeFusion/FusionAlgebra.lean`;
3. `EnterpriseMath/PrimeFusion/Pointed.lean`;
4. `EnterpriseMath/PrimeFusion/Phase.lean`;
5. optional `EnterpriseMath/PrimeFusion/FiniteInterfaces.lean` if a clean T7/T8 interface layer is useful.

Import the completed F1 modules from `EnterpriseMath.lean` only when the proof-bearing slice is coherent and the full build passes.

A different narrow split is acceptable if the return maps every target below to exact declarations and does not duplicate existing project modules.

## 2. Formalization target PF-F1-L01 — channel definitions and T1 identities

Define transparent channel functions corresponding to

`N(a,b)=a^2+b^2`,

`C(a,b)=a^2-a*b+b^2`.

Provide exact declarations for the T1 diagonal identities with

`u=a+b`, `v=a-b`:

`2*N=u^2+v^2`,

`4*C=u^2+3*v^2`,

`u^2=3*N-2*C`,

`v^2=2*C-N`.

Prefer integer statements at the exact source strength where subtraction is natural. Sector-positive corollaries may then be derived separately.

## 3. PF-F1-L02 — exact gcd law and primitive coprimality

Formalize the exact T2 content, not merely a bounded instance:

`gcd(N(a,b),C(a,b)) = gcd(a,b)^2`

with the correct Lean integer/natural gcd typing.

Then derive the primitive-cell corollary that the channels are coprime.

If the cleanest theorem uses `natAbs`/`Int.gcd`, expose an audit-friendly source-facing corollary rather than hiding the statement behind conversion machinery.

## 4. PF-F1-L03 — fusion polynomial and integral CRT core

Define over `Polynomial ℤ`:

`f=X^2+1`,

`g=X^2+X+1`,

`F=f*g`.

Formalize an integral Bezout/comaximality certificate equivalent to

`(X+1)f - Xg = 1`.

Use it to obtain the quotient/product CRT equivalence

`ℤ[X]/(F) ≃+* (ℤ[X]/(f)) × (ℤ[X]/(g))`

or a definitionally equivalent transparent statement.

For F1, these quotient components may serve as the formal `Gaussian` and `Eisenstein` components. Do not force use of a specialized library type if that makes the theorem less transparent.

The discriminant-12 calculation and named `ℤ[i]`, `ℤ[omega]` equivalences are welcome if clean in the pinned library, but failure to package those names must not be confused with failure of the required finite-algebra CRT theorem. Record exact coverage in the return.

## 5. PF-F1-L04 — primitive pointed quotient core

For primitive positive sector coordinates, formalize the component quotient/cyclic carrier needed by T4.

At minimum establish proof-bearing maps with exact kernels giving the two cyclic quotients of sizes/channels `N` and `C`, and combine them through CRT to the pointed modulus `H=N*C`.

The distinguished residue must correspond to

`r = -a*b⁻¹ mod H`

under the exact invertibility hypotheses derived from primitivity.

Do not prove a quotient isomorphism from equal cardinalities alone.

If the stronger Smith-normal-form theorem is natural in Lean, retain it as a separate strengthening declaration:

component cyclicity iff `gcd(a,b)=1`.

It is not required to invent new SNF infrastructure if mathlib support makes that disproportionate; the exact source T4 quotient maps remain mandatory.

## 6. PF-F1-L05 — pointed channel recovery

Formalize the T5 recovery laws for the pointed residue:

`N = gcd(H,r^2+1)`,

`C = gcd(H,r^2+r+1)`.

Keep sign convention explicit.

Prove the no-cross-channel leakage through an exact Bezout/coprimality argument; do not replace the general theorem with sampled modular computation.

## 7. PF-F1-L06 — reciprocal trace and idempotent split

Formalize the reciprocal identity underlying T6 and the accepted strengthening:

- a modular root of `F` is automatically a unit;
- with `T=r+r⁻¹` and `e=-T`, one has `e^2=e`;
- `gcd(e,H)` and `gcd(e-1,H)` partition the prime-power factors of `H` and multiply to `H`.

For the pointed primitive cell, derive the channel specialization `N` and `C`.

Prefer general reusable lemmas for idempotents modulo a natural modulus when they already fit project/mathlib abstractions.

## 8. PF-F1-L07 — corrected T10 channel-oriented mixed locus

This is the highest formalization integrity guard.

For distinct dual-prime channels `p=N>3`, `q=C>3`, define explicitly in Lean the channel-oriented mixed locus

`M_{p,q} = {x mod p*q | x^2+1=0 mod p and x^2+x+1=0 mod q}`

using transparent reduction maps or an equivalent CRT representation.

Prove from the retained hypotheses:

- the pointed local orders are `4` modulo `p` and `3` modulo `q`;
- the global pointed order is `12`;
- the oriented locus is exactly the four phases represented by
  `r, r^5, r^7, r^11`;
- the inversion/shared-coefficient pair is `{r,r^11}` at the algebraic phase level.

Do **not** formalize the false claim that those four elements are every root of `F` modulo `p*q`.

Add a small executable or theorem-level regression example for `H=91` that distinguishes the four-element oriented locus from the eight fused roots, without using that finite example as proof of the general theorem.

## 9. PF-F1-L08 — sixth-power readout and T6/T11 cross-link

Formalize T11 directly from the two oriented local equations:

`x^6=-1 mod p`,

`x^6=+1 mod q`.

Derive the source dual-prime gcd readout:

`p=gcd(H,x^6+1)`,

`q=gcd(H,x^6-1)`.

Also formalize the accepted cross-link on the oriented locus:

`x^6 = 2*e-1 mod H`.

The proof should not depend on completeness of the T10 four-phase orbit when only the local equations are needed.

The composite-parity strengthening may be included as a separate lemma if clean; it must not replace the source dual-prime theorem.

## 10. PF-F1-L09 — interfaces for later T7/T8 formalization

Do not attempt to formalize all remaining theorem rows in this F1 slice.

Expose only the small proof-bearing interfaces naturally produced by L01–L08 that later T7/T8 work can reuse, including where clean:

- idempotent split gives `N*C=H` and channel coprimality automatically;
- T1 square identities are exported in a form suitable for exact reconstruction;
- quotient/channel labels remain distinct from an abstract unordered product of fields.

Do not add T9 or T12–T15 to this task merely because supporting lemmas become available.

## 11. PF-F1-L10 — proof-integrity and finite sanity layer

Add a small number of focused examples/tests sufficient to catch sign/order/universe regressions, including the `H=91` T10 guard.

The proof-bearing slice must contain none of:

- `sorry`;
- `admit`;
- `axiom` or custom postulates introduced to close Prime Fusion targets;
- theorem statements commented out and presented as completed evidence;
- `native_decide` used as the proof of an unbounded mathematical theorem.

`decide`/`native_decide` may be used for explicitly finite regression examples.

## 12. Build and axiom gate

Run the repository-pinned full build exactly:

```bash
lake build --wfail -KCI EnterpriseMath
```

The final returned head is not `LEAN_CHECKED` unless this command succeeds.

Also perform:

1. a static placeholder audit for `sorry`, `admit`, and custom axioms in the new Prime Fusion modules;
2. `#print axioms` or an equivalent generated axiom report for the core declarations corresponding to L02, L03, L04, L05, L06, L07 and L08.

Standard Lean/mathlib foundations are acceptable. `sorryAx` or a new project axiom is not.

## 13. Theorem-spec mismatch discipline

If Lean reveals that a frozen target is false, ill-typed at the claimed mathematical strength, or requires an omitted mathematical hypothesis:

1. do not weaken or silently patch the theorem;
2. isolate the smallest exact failing statement/counterexample if practical;
3. distinguish an API representation problem from a mathematical statement problem;
4. freeze the result as a theorem-spec/interface obstruction for Driver review.

A change of representation that is provably equivalent is allowed and must be documented in the declaration map.

## 14. Required return

Freeze one return at:

`research_returns/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_RETURN_20260824.md`

It must contain:

1. exact source refs and frozen package blob identities consumed;
2. module/file list;
3. mapping table `PF-F1-L01..L10 -> Lean declarations`;
4. exact toolchain/mathlib revisions;
5. exact full-build result;
6. static placeholder audit;
7. axiom report for core declarations;
8. any theorem-spec/API obstruction;
9. statement of what remains for later F1 extension (especially T7/T8 full statements and T9/T12–T15 outside this slice);
10. final classification.

Allowed final classifications:

- `PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED`;
- `PRIME_FUSION_F1_FORMALIZATION_PROGRESS_BUILD_NOT_CLOSED`;
- `PRIME_FUSION_F1_THEOREM_SPEC_MISMATCH`;
- `PRIME_FUSION_F1_LIBRARY_INTERFACE_BLOCKED`.

Only the first classification satisfies the hard target.

## 15. Stop condition

Stop after the F1 finite-algebra return is frozen.

Do not open a later T7/T8, arithmetic-distribution, publication, or performance formalization task from this execution. Driver review decides the next slice.
