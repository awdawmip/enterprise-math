# R062 Stage 0 — BRC Provenance and Type Recovery

Researcher-ID: `EM-R062-7C4A91`  
Task: `RS-R062-STAGE0-BRC-MULTIPATH-ENRICHMENT-BRIDGE-VALIDATION`  
Taskbook source: `bde65a479108b8a906d287fb1728d004f25178af`  
Status: `AUTHORITATIVE_PRIOR_BRC_RECOVERED`

## 1. Recovery verdict

The repository contains an authoritative prior BRC. `BRC` expands to **Branch-Recoalescence Collapse**. The authoritative semantic core is the R023 Boolean/result-support core, now registered as `CANONICAL_MAIN + LEAN_CHECKED_MAIN` and implemented by:

`EnterpriseMath/Relation/BranchRecoalescence.lean`.

The taskbook-opening observation that a literal BRC definition had not yet been found is therefore superseded by this recovery. No provisional `BRC_CANDIDATE_V0` is needed.

Provenance chain:

1. R021 owner checkpoint `7c19a4aeca01319065fd731962597f1f1e6cb9d5`, `docs/R021_BRANCHING_COLLAPSE_REPORT.md`;
2. R023 taskbook `7c139bc175db2a8d809425e4c2899746393d3aa8`;
3. R023 owner head `0b72b9e549e1469567764fbe89f9f2baa8b55453`, `docs/R023_BRC_LEAN_RETURN.md`;
4. canonicalization commit `3bbddc4661647537834953cfd64264fc965be292`;
5. canonical Lean module `EnterpriseMath/Relation/BranchRecoalescence.lean`.

## 2. Exact canonical type surface

For a fine-state type `X`:

- relation: `Rel X := X -> X -> Prop`;
- exact support: `Set X`;
- exact branch: `ExactBranch X := Set X`;
- branch configuration: `BranchConfig X := List (Set X)`;
- relation execution: `relImage R A = { y | exists x, x in A and R x y }`;
- word execution: `runWord step w A`, left-to-right relational direct image;
- configuration denotation: literal union of branch supports;
- exact recoalescence: replace a configuration by the singleton branch denoting that literal union;
- relation composition: `relComp R S a c := exists b, R a b and S b c`.

In a finite presentation this is exactly Boolean relation/matrix semantics:

- merge/addition = OR / set union;
- composition/multiplication = existential shared-middle composition / Boolean matrix multiplication;
- zero = empty relation/support;
- unit = identity relation.

The identity relation is standard for relation composition but is not introduced as a specially named R023 declaration.

## 3. Recoalescence semantics

R023's positive exact theorem is support-level:

`split -> relational direct image -> literal-union recoalescence`

preserves exact reachable **support**. R021/R023 explicitly exclude from this carrier:

- path multiplicity;
- path identity;
- provenance/correlation identity;
- probability or general weights;
- signed/amplitude cancellation.

Accordingly, the historical BRC is already a Boolean shadow. Enriching it to natural multiplicities or path witnesses is an R062 carrier lift, not a recovered hidden prior definition.

## 4. Relabeling semantics

The canonical Lean module has no primitive declaration named `relabel`, `Equiv`, or an automorphism transport operator. Its definitions are polymorphic in state/generator types.

For an exact state bijection `phi : X ~= X'`, define transport by:

`(phi_* R)(x',y') <-> R(phi^-1 x', phi^-1 y')`

and `phi_* A` by direct image. Then directly from existential relational image:

`phi_*(relImage R A) = relImage (phi_*R) (phi_*A)`.

Thus union, support, exact recoalescence, finite-word execution and relational composition are covariant under bijective renaming. Generator relabeling is handled by the corresponding bijection on the `G` index of `step : G -> Rel X`.

This is exact transport of the canonical semantics; it must not be confused with a prior named BRC relabeling primitive.

## 5. R061 bridge typing

For translated native sector `S_ij(P)`, instantiate BRC on the component-typed transition skeleton:

- state carries at least `(P, sector, local cell address)`;
- generators are the distinct native components `X_i`, `X_j`;
- one-step relations are `R_i`, `R_j`;
- typed start incidence is `Sigma_P^(ij)`;
- trace context carries `(P, sector, a,b)`.

This typing is essential. Erasing component labels creates an independent semantic failure at the reverse-third shortcut, even before multiplicity is considered.

Machine-readable signature: `R062_STAGE0_BRC_TYPE_SIGNATURE.json`.
