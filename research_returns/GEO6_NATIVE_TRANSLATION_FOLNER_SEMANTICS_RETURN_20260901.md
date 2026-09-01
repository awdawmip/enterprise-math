# GEO6 Native Translation and Følner Semantics — Research Return

Researcher-ID: `EM-G6TRANSFOL-9D7E05`  
Task: `RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS`  
Publication: `TP2-2DACFDB1816BE0DEB532`  
Claim: `chatgpt-g6transfol-20260901-2059-4a7c12`  
Execution: `ER-F8A9F149D2416118F8A7`  
Execution branch base: `3418f4fdf52b2f62d9d8a47405d550ecd6632009`  
Hard target: `GEO6_NATIVE_TRANSLATION_ACTION_AND_FOLNER_DENSITY_INTERFACE_TYPED_OR_EXACTLY_OBSTRUCTED`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`.

At the frozen accepted evidence cut, current P000/Full-Cell semantics does **not** determine or type a native translation/amenable action. Consequently native period, window, boundary and Følner-density semantics are not presently derivable.

This is deliberately narrower than a global impossibility theorem. It is an exact **current-language authorization and underdetermination boundary**: a P000-compatible translation extension may exist, but it must add and justify a typed native action primitive rather than relabel comparison coordinates or presentation symmetries.

The hard target is therefore met by exact obstruction.

## 2. Frozen accepted evidence

Only canonical accepted authority is used for the semantic conclusion.

1. `research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas_v2.json`
   - blob `sha1:120b71b74dc07edd9a3c78474b51752676c6dae3`;
   - `TRANSLATION_ACTION_SELECTOR` is `UNRESOLVED`;
   - its resolver list is empty;
   - `TRANSLATION_FOLNER_SELECTOR` is `UNRESOLVED`;
   - the accepted dependency DAG contains `TRANSLATION_ACTION_SELECTOR -> TRANSLATION_FOLNER_SELECTOR`.

2. `driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_V2_DRIVER_REVIEW_20260901.md`
   - blob `sha1:510ed84f6ee0913eaee90372e2b591a30ebfa601`;
   - disposition `ACCEPTED`;
   - after the current-head Q24 delta, both translation selectors remain unresolved;
   - accepted P000 currently has exact equivalence/automorphism and observation/reduct structure, but no reviewed result promotes comparison translation into native P000 semantics.

Q25/Q26 and the two concurrently executing GEO6 successor tasks are not consumed as axioms.

## 3. Candidate action inventory

| Candidate currently visible at the accepted cut | Exact type status | Reason |
|---|---|---|
| Exact Cell/Full-Cell equivalences and automorphisms | `PRESENTATION_EQUIVALENCE_ONLY` | They are same-sort invertible symmetries, but no accepted translation-label sort, displacement semantics, or period/window law distinguishes a subgroup as translation. |
| Observation/reduct/slice maps | `TYPE_MAP_REJECTED` | They are observational/forgetful maps, not a total same-sort action with identity/composition. |
| Named carrier/rotation symmetries | `PRESENTATION_EQUIVALENCE_ONLY` | A named symmetry is not a translation action. Immediate native rotation typing is separately owned and supplies no translation resolver at this cut. |
| External comparison-model `Z^6` coordinate shifts | `COMPARISON_ONLY` | They are a classical translation action after comparison coordinates are declared, but no accepted type map makes them native P000. |
| Finite carrier permutations, quotient covers, graph symmetries | `TYPE_MAP_REJECTED` | Permutation/cover data alone does not supply a spatial translation label or native window/boundary semantics. |

Thus there are `0` current `NATIVE_ACTION` candidates and `0` current `PARTIAL_ACTION` candidates strong enough to authorize the density interface.

A finite permutation group being amenable as an abstract finite group is irrelevant to this authorization question: without a native action semantics it is only presentation symmetry, and on a finite state carrier its Følner averaging degenerates to a finite orbit average rather than the global-density layer sought here.

## 4. Exact current-P000 obstruction

### Theorem — current P000 translation authorization no-go

At the frozen accepted evidence cut, no current accepted datum supplies all of:

1. a native translation-label sort/group `G`;
2. a total action on native `Cell` or `FullCell` states;
3. identity and composition laws for that action;
4. a semantic designation that separates translation from generic automorphism/presentation equivalence without importing comparison coordinates;
5. an action-compatible period/window/boundary interface.

The accepted selector census records no resolver for `TRANSLATION_ACTION_SELECTOR`, and every currently visible candidate above fails at least one required typing clause. Since `TRANSLATION_FOLNER_SELECTOR` has an accepted strict dependency on `TRANSLATION_ACTION_SELECTOR`, native Følner-density semantics is blocked as a consequence.

This theorem is an authorization theorem about the frozen language/evidence set. It does **not** assert that no future P000 extension can carry a translation action.

## 5. Minimum missing primitive contract

The minimum density-capable extension candidate is:

`NATIVE_TRANSLATION_LABEL_GROUP_AND_TYPED_CELL_FULLCELL_ACTION`.

A legal candidate must provide, at minimum:

- a native group `G=(G,e,·,^{-1})` whose semantics is declared independently of comparison coordinates;
- `tau_Cell : G × Cell -> Cell`;
- `tau_Full : G × FullCell -> FullCell`;
- `tau(e,x)=x` and `tau(gh,x)=tau(g,tau(h,x))`;
- a nondegeneracy witness showing the action is not merely identity presentation;
- for every accepted readout/locality map `rho : FullCell -> Cell` placed in scope, `rho(tau_Full(g,x)) = tau_Cell(g,rho(x))`.

This is a **minimum missing interface**, not an accepted P000 primitive and not a successor publication.

### Relation-core compatibility

The concurrently executing native-relation task need not finish before this classification. Compatibility is conditional:

- if a native Cell relation `R` is later accepted, require `R(c,c') iff R(tau_Cell(g,c),tau_Cell(g,c'))`;
- if a typed Cell×Support incidence `I` is later accepted, a support action/transport `tau_S` must be explicitly supplied with `I(c,s) iff I(tau_Cell(g,c),tau_S(g,s))`.

No contact/exclusion/support relation is inferred here.

## 6. Finite same-readout countermodels

These witnesses establish underdetermination of the action from the observable/fiber-equivalence fragment. They are **not** claimed to model every P000 axiom; the current-P000 conclusion also uses the accepted no-resolver census above.

Let

`X = {0,1}^3 = {(b,u,v)}`

with readout `rho(b,u,v)=b`. Each readout fiber contains four states; write `i=2u+v in Z/4Z`.

### Witness A/B — same group, same readout, inequivalent actions

Use the same label group `C4`.

- `A_g(b,i)=(b,i+g mod 4)` on both fibers.
- `B_g(0,i)=(0,i+g mod 4)` and `B_g(1,i)=(1,i)`.

Both are exact total `C4` actions, globally faithful, and preserve `rho`.

But the generator has:

- `0` fixed points under `A`;
- `4` fixed points under `B`.

The checker exhausts all `4!·4!=576` readout-preserving bijections of `X` and finds **zero** conjugacies from `A` to `B` with the `C4` labels fixed. Hence even fixing the group and the readout does not determine the action.

### Witness A/V — same readout and fiberwise torsor strength, different label groups

Compare:

- the regular `C4` action `A` above;
- the regular `V4=(Z/2Z)^2` XOR action `(a,c)·(b,u,v)=(b,u xor a,v xor c)`.

Both actions are faithful, readout-preserving, free, and transitive on **every** readout fiber.

Nevertheless their translation-label groups are nonisomorphic: `C4` contains elements of order `4`, while every nonidentity element of `V4` has order `2`.

Therefore even the stronger requirement “every readout fiber is a translation torsor” does not reconstruct a unique translation group from the readout structure.

## 7. Conditional native Følner/density interface

No native Følner structure is granted now. The exact interface under which classical results become reusable is:

1. the native action contract in §5;
2. finite nonempty windows `F_n subset G`;
3. the left Følner condition `|g F_n triangle F_n| / |F_n| -> 0` for every fixed `g in G`;
4. for periodic reuse, an explicitly typed finite-index period subgroup `H <= G`;
5. an `H`-periodic bounded/local observable.

For a finite probe set `K`, one may use the boundary `partial_K F = K F triangle F`; a Følner sequence makes its normalized size vanish for every fixed finite `K`.

### Reuse lemma for periodic observables

Assume the native interface above and, for simplicity, a finite-index normal period subgroup `H normal G`. Let `f:G->R` be `H`-periodic. Then along any declared left Følner sequence `F_n`,

`(1/|F_n|) sum_{g in F_n} f(g) -> (1/|G/H|) sum_{q in G/H} f(q)`.

Proof: push the normalized counting measure of `F_n` to the finite quotient `G/H`. The Følner condition makes every translated quotient measure asymptotically equal. Every subsequential limit is therefore translation invariant on the finite transitive `G/H`-set, hence uniform. The displayed convergence follows.

This is a standard classical consequence **after** the native action/window/period types are supplied. It is not evidence that those types already exist in P000.

## 8. Regression separation

The following identifications are rejected and are regression guards for downstream work:

- coordinate shift `!=` native translation by notation;
- exact automorphism `!=` translation without a native translation type map;
- observation/reduct `!=` action;
- finite quotient cover `!=` global translation;
- finite carrier permutation `!=` authorization of a native Følner layer;
- classical Følner averaging `!=` construction of the missing action.

Only after the action selector is resolved may the classical density theorem be reused.

## 9. Deterministic verification

Checker:

`research_checks/GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS_CHECK_20260901.py`

Certificate:

`research_artifacts/GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS/certificate_20260901.json`

Frozen local execution:

`PASS GEO6_TRANSLATION_FOLNER states=8 fibers=2 fiber_size=4 c4A_faithful=1 c4B_faithful=1 c4A_fiber_regular=1 c4B_fiber_regular=0 generator_fixed_A=0 generator_fixed_B=4 obs_bijections=576 obs_conjugacies=0 v4_fiber_regular=1 native_action_count=0 terminal=CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`

## 10. Hard-target disposition and Driver handoff

Hard target:

`GEO6_NATIVE_TRANSLATION_ACTION_AND_FOLNER_DENSITY_INTERFACE_TYPED_OR_EXACTLY_OBSTRUCTED / PROVED / CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION`.

The exact unresolved residue is one semantically native translation-label group plus typed `Cell`/`FullCell` actions and equivariance laws. Once such an interface is independently accepted, classical periodic/Følner averaging may be reused under §7. Until then, global density remains comparison-conditional.

Driver review should decide whether this current-language obstruction and the minimum missing primitive contract are accepted. This Researcher return publishes no successor and grants no Working Truth, Foundation authority, canonical/native-geometry promotion, or novelty certificate.
