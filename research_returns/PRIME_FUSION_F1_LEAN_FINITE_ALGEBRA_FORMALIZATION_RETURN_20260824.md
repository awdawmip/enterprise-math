# Prime Fusion F1 — Lean Finite-Algebra Formalization Return

Status: `FROZEN / LEAN_CHECKED_WIP / DRIVER_REVIEW_REQUIRED`

Researcher-ID: `EM-PFF1-6DA3FD`

Task-ID: `RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION`

Owner branch: `formalization/prime-fusion-f1-finite-algebra`

Taskbook: `research_tasks/PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_20260824.md`

Taskbook source: `6da3fd713a10e4ceab5e4819330168882cb67c88`

Hard target: `PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED_NO_SORRY_PINNED_BUILD_PASS`

This return freezes only the Driver-accepted Prime Fusion finite-algebra Lean slice. No new theorem row, no T9/T12–T15 extension, and no silent theorem weakening was introduced.

## 1. Exact source refs consumed

Authoritative/frozen inputs used by this F1 formalization:

- Driver review: `driver_reviews/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_DRIVER_REVIEW_20260824.md@86df3a53417ddc810b3c51ac906288b54bef5e63`;
- corrected theorem package: `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md#blob=055bdaaca81c5ac7ab350a71acf3b69fe5e564a9` on `integration/prime-fusion-evidence-typed-package`;
- frozen dependency graph: `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md#blob=54d1fbb8c3fb657ac55f556c982501386a8eaf25`;
- final evidence matrix: `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv#blob=3c9f6fa670f9405eebbab6eae5d5374c2de4a037`;
- package manifest: `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json#blob=6b388f3b17eddf1443de12ec6cf9f6db3e6999c2`;
- formalization queue handoff: `driver_handoffs/PROJECT_RESULT_LEVELS_AND_FORMALIZATION_QUEUE_20260823.md@a404d271bd30a713218d38838ef3d063d1afcadf`;
- task-start root/toolchain baseline: `EnterpriseMath.lean@28da4d402864923269df6af56f8ef2c487ee4be2`, `lakefile.toml@28da4d402864923269df6af56f8ef2c487ee4be2`, `lean-toolchain@28da4d402864923269df6af56f8ef2c487ee4be2`.

Implementation head validated immediately before this freeze:

`cd546cfbd32c159b773d6d77475f433fa6117119`

PR: `#619` (`Prime Fusion F1 Lean finite-algebra formalization`).

## 2. Module/file list

Proof-bearing Prime Fusion files:

1. `EnterpriseMath/PrimeFusion/Channels.lean`
2. `EnterpriseMath/PrimeFusion/FusionAlgebra.lean`
3. `EnterpriseMath/PrimeFusion/ArithmeticSplit.lean`
4. `EnterpriseMath/PrimeFusion/MixedLocus.lean`
5. `EnterpriseMath/PrimeFusion/PhaseReadout.lean`
6. `EnterpriseMath/PrimeFusion/PointedQuotient.lean`
7. `EnterpriseMath/PrimeFusion/PointedRecovery.lean`
8. `EnterpriseMath/PrimeFusion.lean` — single root aggregator plus core `#print axioms` audit
9. `EnterpriseMath.lean` — imports `EnterpriseMath.PrimeFusion`

Mechanical shared-root registration updated consistently in:

- `research_common_surface.json`;
- `docs/RESEARCH_COMMON_SURFACE.en.md`;
- `docs/RESEARCH_COMMON_SURFACE.zh-CN.md`.

No competing general algebra library was introduced.

## 3. PF-F1-L01..L10 declaration map

| Lane | Required content | Lean declarations / evidence |
|---|---|---|
| `PF-F1-L01` | `N,C,u,v` and four exact T1 identities | `N`, `C`, `u`, `v`; `two_mul_N_eq_u_sq_add_v_sq`; `four_mul_C_eq_u_sq_add_three_v_sq`; `u_sq_eq_three_N_sub_two_C`; `v_sq_eq_two_C_sub_N` in `Channels.lean` |
| `PF-F1-L02` | exact T2 gcd law and primitive channel coprimality | `channel_gcd_exact`; `primitive_channels_isCoprime` in `Channels.lean` |
| `PF-F1-L03` | `f=X^2+1`, `g=X^2+X+1`, `F=f*g`, integral Bezout/comaximality and CRT | `gaussianPoly`; `eisensteinPoly`; `fusionPoly`; `fusion_bezout`; `fusionFactors_isCoprime`; `fusionIdeal_eq_inf`; `fusionIdeal_eq_iInf`; `fusionCRT` in `FusionAlgebra.lean` |
| `PF-F1-L04` | primitive pointed cyclic quotient maps, exact kernels, sizes, CRT `H=N*C`, `r=-ab⁻¹` | `channelResidueMap`; `mem_ker_channelResidueMap_iff`; `channelResidueMap_surjective`; `gaussianQuotientMap`; `eisensteinQuotientMap`; `gaussianQuotientMap_kernel`; `eisensteinQuotientMap_kernel`; `gaussianQuotientMap_surjective`; `eisensteinQuotientMap_surjective`; `gaussianCarrier_card`; `eisensteinCarrier_card`; `fusedCarrier_card`; `Hmodulus_eq_mul`; `primitive_moduli_coprime`; `pointedCRT`; `primitive_b_N_isCoprime`; `primitive_b_C_isCoprime`; `primitive_b_H_isCoprime`; `pointedResidue`; `pointedResidue_spec`; `pointedResidue_fusion_root` in `PointedQuotient.lean` |
| `PF-F1-L05` | pointed `N/C` gcd recovery with exact no-leakage | generic `eval_bezout`, `eval_isCoprime`, `gcd_recover_left[_local]`, `gcd_recover_right[_local]`, `exact_channel_recovery` in `ArithmeticSplit.lean`; pointed `pointedLift`, `pointedLift_linear_dvd`, `pointed_factor_divisibilities_of_linear`, `pointed_factor_divisibilities`, `pointed_channel_recovery` in `PointedRecovery.lean` |
| `PF-F1-L06` | automatic unit, reciprocal trace, idempotent split, pointed `N/C` specialization | `reciprocalCandidate`; `fusion_root_mul_reciprocal`; `fusion_root_reciprocal_mul`; `fusionRootUnit`; `rootIdempotent`; `rootIdempotent_eq_unit_trace`; `rootIdempotent_isIdempotent`; `idempotent_gcd_partition` in `ArithmeticSplit.lean`; `rootIdempotent_eq_polynomial` in `PhaseReadout.lean`; `pointedIdempotentInt`; `pointedIdempotentLift`; `pointed_idempotent_factor_divisibilities`; `pointed_idempotent_congruence`; `pointed_idempotent_partition`; `pointed_idempotent_channel_recovery`; `pointedIdempotentLift_cast`; `pointed_rootIdempotent_isIdempotent` in `PointedRecovery.lean` |
| `PF-F1-L07` | corrected channel-oriented `M_{p,q}`, local orders 4/3, global 12, four phases, inverse pair, `H=91` guard | `MixedCarrier`; `MixedLocus`; `gaussian_root_order`; `eisenstein_root_order`; `mixed_locus_order_twelve`; `mixed_locus_four_orbit`; `mixed_orbit_inverse_only_eleven`; finite `orientedRoots91`, `fusedRoots91`, `orientedRoots91_exact`, `fusedRoots91_exact`, `orientedRoots91_ne_fusedRoots91` in `MixedLocus.lean` |
| `PF-F1-L08` | sixth-power local signs, dual-prime gcd readout, `x^6=2e-1` | `gaussian_root_pow_six`; `eisenstein_root_pow_six`; `mixed_sixth_eq_two_idempotent_sub_one` in `MixedLocus.lean`; `gaussian_sixth_add_one_dvd`; `eisenstein_sixth_sub_one_dvd`; `dualPrime_sixth_gcd_readout`; `mixed_sixth_eq_two_rootIdempotent_sub_one` in `PhaseReadout.lean` |
| `PF-F1-L09` | minimal later interfaces only | T1 reconstruction identities from L01; ordered channel-product interface `Hmodulus_eq_mul`; `primitive_moduli_coprime`; `pointedCRT`; channel labels remain explicit. No full T7/T8 or later theorem rows were added. |
| `PF-F1-L10` | finite sanity, no placeholders/custom axioms, exact warnings-fatal full build | `H=91` finite regressions above use `native_decide` only for finite sets; static PR-diff audit; core `#print axioms` block in `EnterpriseMath/PrimeFusion.lean`; successful exact build recorded below. |

### Corrected T10 universe integrity

The Lean universe is explicitly channel-oriented:

`MixedCarrier p q = ZMod p × ZMod q`

with

`MixedLocus x := (x.1^2 + 1 = 0) ∧ (x.2^2 + x.2 + 1 = 0)`.

The four-phase theorem is therefore about this oriented mixed locus, not the whole fused-root universe.

The `H=91=13*7` guard distinguishes:

- oriented locus: `{18, 44, 60, 86}` — 4 residues;
- all fused roots: `{9, 16, 18, 44, 60, 74, 81, 86}` — 8 residues.

`orientedRoots91_ne_fusedRoots91` is a finite regression theorem. It is not used as proof of the general four-phase theorem.

Thus the corrected T10 `M_{p,q}` universe and the `H=91` regression boundary are preserved exactly; no claim that the four oriented phases exhaust all roots of `F mod p*q` appears in the proof-bearing slice.

## 4. Exact toolchain / mathlib revisions

Pinned build environment actually resolved by CI:

- Lean toolchain: `leanprover/lean4:v4.33.0-rc2`;
- Lean version: `4.33.0-rc2`, Lean commit `d8b18978322de05a8f3dba51ef03cf5461676c17`;
- Lake: `5.0.0-src+d8b1897`;
- mathlib revision: `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`.

These match the taskbook-pinned environment.

## 5. Exact full-build result

Required command actually executed:

```text
lake build --wfail -KCI EnterpriseMath
```

Validated implementation head:

`cd546cfbd32c159b773d6d77475f433fa6117119`

GitHub Actions Lean run / job:

- run: `32804166003`;
- job: `97670881895`;
- checked PR merge ref: `c345b171c7acaec62cfe8697e060eea819add960`;
- merge ref composition shown by checkout: owner head `cd546cfbd32c159b773d6d77475f433fa6117119` merged into base `c617ed64738660c02dda458336d1bd1091d1c58f`.

Result:

`Build completed successfully (8731 jobs).`

The log explicitly built, in order, all seven internal Prime Fusion modules, the `EnterpriseMath.PrimeFusion` aggregator, and the top-level `EnterpriseMath` target under `--wfail`.

Additional non-mathematical integration gates already green on the same implementation head before freeze:

- `reference-integrity` run `32804166075`: `success`;
- `bilingual-sync` run `32804166079`: `success`.

The repository-wide Python `quality` workflow is not part of the taskbook's F1 Lean hard gate; no classification below relies on it.

## 6. Static placeholder audit

The complete PR patch for `#619` was searched at the validated implementation head.

Results:

- token `sorry`: no match;
- token `admit`: no match;
- custom declaration form `axiom ...`: no match;
- no theorem target is commented out and represented as completed proof;
- `native_decide` is confined to explicitly finite regression facts, notably the `H=91` oriented/full-root sets, and is not used to prove an unbounded theorem.

The textual occurrences of `#print axioms` are audit commands, not custom axiom declarations.

Static audit verdict:

`PASS / NO_SORRY / NO_ADMIT / NO_CUSTOM_AXIOM`

## 7. Core axiom report

`EnterpriseMath/PrimeFusion.lean` runs `#print axioms` for the L02–L08 core. The successful warnings-fatal build emitted:

| Declaration | Reported axioms |
|---|---|
| `EnterpriseMath.PrimeFusion.channel_gcd_exact` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.fusionCRT` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.pointedCRT` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.pointedResidue_fusion_root` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.pointed_channel_recovery` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.pointed_idempotent_channel_recovery` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.mixed_locus_order_twelve` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.mixed_locus_four_orbit` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.mixed_orbit_inverse_only_eleven` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.dualPrime_sixth_gcd_readout` | `[propext, Classical.choice, Quot.sound]` |
| `EnterpriseMath.PrimeFusion.mixed_sixth_eq_two_rootIdempotent_sub_one` | `[propext, Quot.sound]` |

No `sorryAx` and no new project/custom axiom appears. Only standard Lean/mathlib foundations allowed by the taskbook are present.

Axiom audit verdict:

`PASS / STANDARD_FOUNDATIONS_ONLY`

## 8. Theorem-spec / API obstruction report

Final obstruction status:

`NONE`

During implementation, Lean exposed representation/API proof-script issues, not mathematical statement failures. They were closed without changing theorem strength:

- the pointed quotient used the correct current `ZMod` integer-divisibility API shape;
- a redundant cast rewrite was removed after normalization had already closed the cast shape;
- `pointedResidue` retained the primitivity hypothesis in its API while marking the definition-level argument unused; theorems deriving its unit/invertibility properties still consume the hypothesis;
- the missing source-facing pointed T5/T6 specializations were added as `PointedRecovery.lean` rather than treating generic lemmas as sufficient evidence;
- the axiom audit was moved to the Prime Fusion aggregator so `fusionCRT` is in scope; this changed only audit placement, not theorem content.

No frozen target was weakened, no new mathematical hypothesis was added, and no corrected T10 universe was changed.

Therefore:

- theorem-spec mismatch: `NO`;
- library-interface blocker: `NO`;
- silent weakening: `NO`.

## 9. Explicitly deferred / outside this F1 slice

The following remain outside this frozen return by taskbook design:

- full T7/T8 theorem statements and their later dedicated formalization slice;
- T9;
- T12–T15;
- optional named `ℤ[i]` / `ℤ[ω]` packaging and discriminant-12 conveniences not needed for the required integral CRT;
- optional stronger Smith-normal-form packaging beyond the exact primitive quotient maps already proved;
- optional composite-parity strengthening beyond the retained dual-prime T11 theorem;
- any publication/performance/arithmetic-distribution work.

Nothing in this list weakens PF-F1-L01..L10 as frozen above.

## 10. Final classification

`PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED`

Hard-target status:

`PRIME_FUSION_F1_FINITE_ALGEBRA_LEAN_CHECKED_NO_SORRY_PINNED_BUILD_PASS = ACHIEVED`

Formalization status remains `LEAN_CHECKED_WIP` until Driver review/canonical promotion; this return does not self-promote it to `LEAN_CHECKED_MAIN`.

Stop condition applies now: do not open or execute a later T7/T8, arithmetic-distribution, publication, or performance formalization task from this execution.