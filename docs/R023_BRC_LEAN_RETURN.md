# R023 BRC Semantic Core Lean Return

Researcher-ID: `EM-R023-1B8D16`  
Task: `RS-R023-BRC-SEMANTIC-LEAN-CORE`  
Taskbook: `7c139bc175db2a8d809425e4c2899746393d3aa8`  
Frozen R021 input: `7c19a4aeca01319065fd731962597f1f1e6cb9d5` / Draft PR #496  
Owner branch: `agent/r023-brc-semantic-lean-core`  
Lean code candidate: `6eea57de1d30d6c2fe983121f6e209286a5c9895`  
Status: `BRC_SEMANTIC_CORE_FORMALIZED / LEAN_VALIDATION_PENDING / NOT_CANONICAL`  
Canonical status: `NOT_CANONICAL`

## 1. Return

`BRC_SEMANTIC_CORE_FORMALIZED / LEAN_VALIDATION_PENDING / NOT_CANONICAL`

R023 formalizes only the Boolean/result-support semantic core. It does **not** promote R021 representation Pareto claims, branch-budget optimization, multiplicity, provenance, probability/weights, or signed/amplitude cancellation.

No semantic repair of R021 is required by the resulting theorem boundary. Lean-level formalization sharpens the claims in three ways without adding assumptions:

1. `NO_RESURRECTION` needs only factorization of the exact target through the **complete** runtime encoder; injectivity of the encoder is unnecessary.
2. `ONE_STEP_COARSEST` is most cleanly a factorization/kernel universal property; the generic theorem is stated for arbitrary `sigma`, with a direct specialization to `coarseSuccessorSupport q R`.
3. `SUPPORT_BRANCH_INVARIANT` and `FORGETFUL_RECOALESCENCE_IFF` do not require a finite fine state type. Finiteness appears only in runtime list structure and in the concrete finite counterexamples.

The only `classical` use in the module is the convenience proof that a concrete predicate split `A ∩ P, A \ P` has union `A`; the four required semantic theorems themselves do not depend on classical logic or choice.

## 2. Formal carrier boundary

The module keeps the following objects type-distinct:

- fine point `x : X`;
- coarse observation `q : X -> Q`;
- exact support `Set X`;
- exact branch atom `ExactBranch X := Set X` (identity denotation, so no hidden free token exists inside the theorem);
- finite live branch configuration `List (Set X)` with denotation `configSupport`;
- relational direct image `relImage`;
- finite word execution `runWord`;
- final set-valued observable `observeSupport`;
- declared point/support future signatures;
- operational suffix safety `SuffixSafe` defined directly from execution, not as signature equality.

A richer observable requiring multiplicity, path identity, provenance, probability, or signed cancellation is outside the carrier. The middle-incidence witness demonstrates exactly where a carrier lift becomes necessary.

## 3. Theorem-surface audit

| R021 claim | Lean declarations | Exact assumptions | R021 relation | Logic/size dependencies | Generic vs Enterprise | Preserved observable |
|---|---|---|---|---|---|---|
| `NO_RESURRECTION` | `noResurrection`, `noResurrection_ne`, `pointSignature_noResurrection` | `Recovers encoder target`, i.e. an exact decoder/factorization through the complete runtime encoding | Equal, with weakest factorization hypothesis made explicit | no finiteness, `DecidableEq`, classical logic, or choice | generic factorization/kernel mathematics; Enterprise specialization is the charged-runtime interpretation | exact target; specialized to `V -> Set O` point future signature |
| `ONE_STEP_COARSEST` | `oneStepKey_sufficient`, `oneStepKey_recovers_of_sufficient`, `oneStepCoarsest`, `oneStepCoarseSuccessorCoarsest`, `oneStepCoarsest_kernel` | classifier can recover both `q` and `sigma`; R021 specialization takes `sigma = coarseSuccessorSupport q R` | Equal; generic statement is slightly more general | no finiteness, surjectivity, injectivity, `DecidableEq`, classical logic, or choice | generic product/factorization theorem; Enterprise specialization selects the collapse successor-support interface | current coarse observation plus next coarse successor-support |
| `SUPPORT_BRANCH_INVARIANT` | `relImage_union`, `configSupport_executeConfig`, `configSupport_exactRecoalesce`, `supportBranchInvariant`, `supportBranchObservableInvariant` | relation direct image; split policy preserves literal union; recoalescence denotes literal union | Stronger in generality, same semantic claim | `X` arbitrary; finite word/config represented by `List`; main theorem constructive | generic relational powerset/direct-image law; BRC specialization is split/execute/recoalesce typing | exact fine reachable `Set X`, hence every downstream set-valued observation |
| `FORGETFUL_RECOALESCENCE_IFF` | `SuffixSafe`, `supportSignature`, `forgetfulRecoalescence_iff`, `sameCurrentCoarse_notSuffixSafe` | operational equality for every declared remaining word and set-valued final observation | Equal; theorem actually permits arbitrary replacement `A -> H`, not only hull supersets | no finiteness, `DecidableEq`, classical logic, or choice in the iff | generic behavioral-signature packaging; Enterprise specialization is the forgetful recoalescence boundary | remaining-language final support signature `V -> Set O` |
| three-state quotient composition | `threeState_oneStep_exact`, `threeState_fine_twoStep_coarseSupport`, `threeState_quotient_twoStep_coarseSupport`, `threeState_composition_spurious_q1` | fixed three fine states, two coarse labels, frozen `q` and `f`, start from full `q=0` fibre | Equal to frozen R021 witness; no global minimality claim added | concrete finite inductives; `DecidableEq` for finite set simplification | Enterprise collapse counterexample built from generic existential quotient semantics | final Boolean coarse support |
| current coarse equality is insufficient | `singleton_current_coarse`, `hull_current_coarse`, `sameCurrentCoarse_notSuffixSafe` | frozen three-state system and one remaining `f` step | Equal | concrete finite inductives | Enterprise recoalescence counterexample | current coarse support vs remaining final coarse support |
| middle-incidence correlation | `middleIncidence_exact_empty`, `middleIncidence_coarse_spurious` | first edge uses `b1`, second edge requires distinct `b2`; middle quotient erases identity | Equal | concrete two-constructor middle type | generic relational-composition witness; Enterprise use is a carrier-lift warning | Boolean existence/support only; provenance/correlation intentionally not preserved |

## 4. `NO_RESURRECTION`

The formal hypothesis is exactly:

```text
Recovers encoder target := exists decode, forall x,
  decode (encoder x) = target x
```

Therefore equal complete runtime encodings force equal exact targets, and unequal targets force unequal complete encodings. Branch IDs, hidden coordinates, correlation tokens, or any other runtime metadata can evade the conclusion only by being omitted from `encoder`; that would violate the task's “complete runtime encoding” contract rather than refute the theorem.

This is an information boundary, not an injectivity theorem: the encoder may merge points whenever their declared exact targets agree.

## 5. `ONE_STEP_COARSEST`

For arbitrary `q : X -> Q` and `sigma : X -> S`, the key

```text
oneStepKey q sigma x = (q x, sigma x)
```

recovers both components. Conversely every classifier from which both components can be recovered also recovers the pair key. Hence its kernel is the unique coarsest equivalence/kernel among deterministic classifiers sufficient for this one-step interface, up to relabeling of classifier values.

`oneStepCoarseSuccessorCoarsest` instantiates `sigma` with the R021 relational successor-support

```text
coarseSuccessorSupport q R x = q '' relImage R {x}.
```

No partition implementation, quotient surjectivity, state finiteness, or encoder injectivity is needed.

## 6. `SUPPORT_BRANCH_INVARIANT`

The proof separates the three semantic moves:

1. exact split is represented only by the invariant `configSupport (split g cfg) = configSupport cfg`;
2. relational direct image commutes with union (`relImage_union`), so branchwise execution has the same union as executing the union;
3. exact recoalescence is the singleton branch whose denotation is literally the prior configuration union.

Induction on the finite future word gives equality of exact fine reachable supports, which is stronger than equality of any chosen final set-valued observation. No multiplicity or provenance theorem is claimed.

The module also includes `splitBy` as a concrete lossless binary split, but the main invariant accepts any exact support-preserving split policy.

## 7. `FORGETFUL_RECOALESCENCE_IFF`

`SuffixSafe` is defined operationally first: for every declared remaining word, execute from `A` and `H` and compare the resulting observable supports. The support signature independently packages those per-word outputs into a function. Functional extensionality then proves the iff.

The three-state finite witness proves the needed negative boundary:

```text
observeSupport q {x0} = observeSupport q {x0,x1} = {q0}
```

but after one remaining `f` step the supports are `{q0}` and `{q0,q1}` respectively. Equal current coarse observation is therefore insufficient for forgetful recoalescence.

## 8. Three-state composition counterexample

Frozen system:

```text
q(0)=q(1)=0, q(2)=1
f(0)=0, f(1)=2, f(2)=0
start = q^{-1}({0}) = {0,1}
```

The declarations make the one-step/two-step distinction explicit:

- exact fine one-step coarse support is `{0,1}`;
- one existential quotient step is also `{0,1}` (`threeState_oneStep_exact`);
- exact fine two-step coarse support is `{0}`;
- quotient-squared support is `{0,1}`;
- `threeState_composition_spurious_q1` isolates coarse state `1` as the spurious result.

R023 does not promote R021's bounded `n<3` exhaustive minimality result into Lean; that scope remains exactly as requested.

## 9. Middle-incidence correlation counterexample

The first relation reaches only middle witness `b1`; the second relation departs only from distinct witness `b2`. `middleIncidence_exact_empty` proves the exact composition is impossible because the existential middle witness must be the same object.

Quotienting both middle witnesses to one coarse `Unit` state retains two nonempty marginals. `middleIncidence_coarse_spurious` then proves their coarse composition exists. This does **not** invalidate Boolean relational support semantics for union/existential questions. It marks the exact boundary: a future observable depending on middle identity/correlation requires a richer carrier and charged metadata.

## 10. Correction audit

`R021_MISSING_HYPOTHESIS: NONE FOUND`.

`R021_OVERSTRONG_STATEMENT: NONE FOUND` for the four target semantic theorems under the frozen Boolean/result-support interpretation.

Formal sharpening only:

- “computed only from runtime encoding” = exact factorization through the complete encoder;
- “unique coarsest” = universal factorization/kernel property, uniqueness only up to kernel/relabeling, not literal classifier codomain identity;
- exact support branch theorem is about literal `Set X` denotations and relational direct image;
- forgetful recoalescence is language/observable-relative and permits an arbitrary replacement pair; a separate representation layer may additionally require `A ⊆ H` if it specifically calls `H` a hull.

These are precision improvements, not theorem corrections.

## 11. Validation

- Frozen Lean code candidate: `6eea57de1d30d6c2fe983121f6e209286a5c9895`.
- Temporary owner-local validation helper: first setup-only failure `8d2b55d0e4457183bfc44f519209b096eca8faef`; corrected helper commit `303d14d7596c9adefeca2c8b8e0091c013ad5bad`; helper removed from the owner branch at `be26c8f042fd03f993fca718b7ea929895b8b052` after the final permitted validation snapshot.
- Repository toolchain: Lean `v4.33.0-rc2`, pinned mathlib `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`.
- Required target declarations contain no `sorry`, `admit`, or task-local axioms.
- Independent finite semantic sanity check of the two counterexamples: PASS.
- Lean validation: `PENDING / NO LEAN PASS CLAIMED`. The first helper run failed before checkout/Lean compilation because `leanprover-community/cache-action` could not be resolved; this was a setup failure, not a theorem failure. After correction to the repository-native `lean-action -> lake update -> lake exe cache get -> lake env lean` path, owner-local run `31484321091` for source state `7a8d8ed4569f69913038cd543affde89c1f81603` entered `in_progress`. Repository no-polling/liveness policy forbids refreshing that unchanged validation object, so R023 records no Lean PASS and no Lean compiler counterexample in this return.
- Non-Lean repository checks are not theorem evidence. Any unrelated reference-integrity/common-surface registration issue belongs to later integration and does not change the R023 mathematical result.

## 12. Downstream recommendation

`KEEP_AS_RESEARCH_TOOL_ONLY`

Current validation-gated recommendation: keep this as research-only until the pinned owner-local Lean compile completes. If that compile passes without semantic correction, the intended integration is narrow:

- expose the factorization/no-resurrection boundary;
- expose the one-step successor-support universal property;
- expose exact relational support split/execute/recoalesce invariance;
- expose suffix-safe forgetful replacement and the two counterexample boundaries;
- retain explicit prior-art classification for the generic relational/factorization machinery;
- keep representation Pareto, atom dictionaries, cost models, branch-budget optimization, and richer carriers outside this shared semantic surface.

No Foundation Question has been exposed by the mathematics so far. Canonical promotion, root import registration, common-surface indexing, and any representation-layer work remain downstream actions.

The repository `reference-integrity` failure observed on the validation PR is unrelated owner/index drift: citation/lineage checking passed, while `check_research_common_surface.py` reported pre-existing missing tool-index entries for `tools/research_identity.py` and `tools/research_taskbook.py`. R023 does not modify those cross-owner surfaces.
