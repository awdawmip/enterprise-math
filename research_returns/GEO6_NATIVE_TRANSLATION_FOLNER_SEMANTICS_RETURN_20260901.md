# GEO6 Native Translation and Følner Semantics — Research Return

Researcher-ID: `EM-G6TRANSFOL-9D7E05`
Task: `RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS`
Publication: `TP2-2DACFDB1816BE0DEB532`
Claim: `chatgpt-g6transfol-20260901-2059-4a7c12`
Execution: `ER-F8A9F149D2416118F8A7`
Execution branch base: `3418f4fdf52b2f62d9d8a47405d550ecd6632009`

## Terminal verdict

`NEGATIVE_BOUNDARY / CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`.

At the frozen accepted evidence cut, current P000/Full-Cell semantics does not determine or type a native translation/amenable action. Native period, window, boundary and Følner-density semantics therefore are not presently derivable. This is an exact current-language authorization/underdetermination boundary, not a theorem that no P000-compatible translation extension can exist.

Hard target:

`GEO6_NATIVE_TRANSLATION_ACTION_AND_FOLNER_DENSITY_INTERFACE_TYPED_OR_EXACTLY_OBSTRUCTED / PROVED / CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`.

## Frozen accepted evidence

The semantic conclusion uses only canonical accepted authority.

- `research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas_v2.json`, blob `sha1:120b71b74dc07edd9a3c78474b51752676c6dae3`: `TRANSLATION_ACTION_SELECTOR=UNRESOLVED`, resolver list empty; `TRANSLATION_FOLNER_SELECTOR=UNRESOLVED`; dependency `TRANSLATION_ACTION_SELECTOR -> TRANSLATION_FOLNER_SELECTOR`.
- `driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_V2_DRIVER_REVIEW_20260901.md`, blob `sha1:510ed84f6ee0913eaee90372e2b591a30ebfa601`, disposition `ACCEPTED`: after the Q24 current-head delta, both translation selectors remain unresolved. Accepted P000 exposes exact equivalence/automorphism and observation/reduct structure, but no reviewed result promotes comparison translation into native P000 semantics.

Q25/Q26 and the concurrently executing GEO6 relation/refinement successors are not consumed as axioms.

## Candidate action classification

| Candidate | Classification | Exact failure |
|---|---|---|
| Accepted Cell/Full-Cell equivalences and automorphisms | `PRESENTATION_EQUIVALENCE_ONLY` | No accepted translation-label sort, displacement semantics, or period/window law distinguishes a subgroup as translation. |
| Observation/reduct/slice maps | `TYPE_MAP_REJECTED` | Not a total same-sort action with identity/composition. |
| Named carrier/rotation symmetries | `PRESENTATION_EQUIVALENCE_ONLY` | Named symmetry is not a translation action; no translation resolver follows. |
| Comparison-model `Z^6` coordinate shifts | `COMPARISON_ONLY` | Classical after external coordinates are declared; no accepted native type map. |
| Finite carrier permutations, quotient covers, graph symmetries | `TYPE_MAP_REJECTED` | Permutation/cover structure does not type spatial translation labels or native windows. |

Current count: `NATIVE_ACTION=0`; density-capable `PARTIAL_ACTION=0`.

A finite permutation group is amenable as an abstract finite group, but that fact cannot authorize the missing native action. On a finite carrier it yields only finite orbit averaging unless an independently typed spatial action/window system is supplied.

## Current-P000 authorization no-go

A native translation layer sufficient for density requires all of:

1. a native translation-label group `G`;
2. total actions `tau_Cell : G x Cell -> Cell` and `tau_Full : G x FullCell -> FullCell`;
3. identity/composition laws;
4. a semantic designation separating translation from generic presentation symmetry without importing comparison coordinates;
5. action-compatible period/window/boundary typing.

No current accepted datum supplies all five. The accepted selector census has no resolver for the action selector, and every candidate above fails at least one clause. Because the Følner selector has a strict accepted dependency on the action selector, native Følner density is currently blocked.

## Minimum missing primitive

Freeze the exact missing interface as an extension candidate only:

`NATIVE_TRANSLATION_LABEL_GROUP_AND_TYPED_CELL_FULLCELL_ACTION`.

Minimum contract:

- native group `G=(G,e,mul,inv)`, semantically independent of comparison coordinates;
- total `tau_Cell` and `tau_Full`;
- `tau(e,x)=x` and `tau(gh,x)=tau(g,tau(h,x))`;
- a nonidentity/nondegeneracy witness;
- for every accepted readout/locality map `rho : FullCell -> Cell` placed in scope,
  `rho(tau_Full(g,x)) = tau_Cell(g,rho(x))`.

If a native Cell relation `R` is later accepted, require diagonal equivariance
`R(c,c') iff R(tau_Cell(g,c),tau_Cell(g,c'))`.
If a typed Cell×Support incidence `I` is later accepted, require an explicitly typed support action/transport `tau_S` with
`I(c,s) iff I(tau_Cell(g,c),tau_S(g,s))`.
No relation/support structure is inferred here.

## Finite same-readout countermodels

These witnesses refute reconstruction of a unique translation action from the observable/fiber fragment. They are not claimed to realize all P000 axioms; the project-level no-go additionally uses the accepted no-resolver census.

Let `X={0,1}^3` with `rho(b,u,v)=b`; each readout fiber has four states. Put `i=2u+v mod 4`.

### Same group, incompatible actions

Take label group `C4`.

- `A_g(b,i)=(b,i+g mod 4)` on both fibers.
- `B_g(0,i)=(0,i+g mod 4)`; `B_g(1,i)=(1,i)`.

Both are total faithful `C4` actions and preserve `rho`. The generator has `0` fixed points under `A` and `4` under `B`. Exhaustion of all `4! * 4! = 576` readout-preserving bijections gives `0` action conjugacies. Thus even fixing the group and readout does not determine the action.

### Same readout, torsor strength, incompatible groups

Compare the regular `C4` action `A` with the regular `V4=(Z/2Z)^2` XOR action
`(a,c).(b,u,v)=(b,u xor a,v xor c)`.

Both are faithful, readout-preserving, free and transitive on every readout fiber. Yet `C4` contains elements of order `4`, while `V4` has exponent `2`. Hence even the stronger condition that every readout fiber is a translation torsor does not reconstruct the translation-label group.

## Conditional Følner/density reuse interface

No native Følner structure is granted now. Classical results become reusable only after the native action contract is accepted and one also specifies:

- finite nonempty windows `F_n subset G`;
- for every fixed `g in G`, `|gF_n triangle F_n|/|F_n| -> 0`;
- for periodic reuse, a typed finite-index period subgroup `H <= G` and an `H`-periodic bounded/local observable.

For finite probe `K`, one may set `partial_K F = KF triangle F`.

For a finite-index normal `H`, an `H`-periodic `f:G->R`, and a declared left Følner sequence, the normalized averages over `F_n` converge to the uniform mean on `G/H`. Proof: push normalized counting measure to the finite quotient; Følner invariance makes each subsequential limit translation-invariant, and the only invariant probability on the transitive finite quotient is uniform. This is classical reuse after typing, not evidence for the missing native action.

## Regression guards

Reject all shortcuts:

- coordinate shift `!=` native translation by notation;
- exact automorphism `!=` translation without a type map;
- observation/reduct `!=` action;
- finite quotient cover `!=` global translation;
- finite carrier permutation `!=` native Følner authorization;
- classical Følner averaging `!=` construction of the missing action.

## Deterministic verification

Checker: `research_checks/GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS_CHECK_20260901.py`

Certificate: `research_artifacts/GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS/certificate_20260901.json`

Frozen output:

`PASS GEO6_TRANSLATION_FOLNER states=8 fibers=2 fiber_size=4 c4A_faithful=1 c4B_faithful=1 c4A_fiber_regular=1 c4B_fiber_regular=0 generator_fixed_A=0 generator_fixed_B=4 obs_bijections=576 obs_conjugacies=0 v4_fiber_regular=1 native_action_count=0 terminal=CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`

## Driver handoff

Unresolved residue: one semantically native translation-label group, typed Cell/FullCell actions, and the required equivariance laws. Once independently accepted, classical periodic/Følner averaging may be reused under the conditional interface above. Until then, global density remains comparison-conditional.

This Researcher return publishes no successor and grants no Working Truth, Foundation authority, canonical/native-geometry promotion, or novelty certificate.
