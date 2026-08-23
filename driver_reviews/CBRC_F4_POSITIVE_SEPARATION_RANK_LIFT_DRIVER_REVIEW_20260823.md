# CBRC F4 Positive-Separation Rank-Lift — Driver Review

Status: `ACCEPTED_WITH_NEGATIVE_RANK_LIFT_RESULT`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F4-POSITIVE-SEPARATION-RANK-LIFT-CLASSIFICATION`
Accepted owner head: `f0a0edc9ef5d8e0ea1b21727f5a7c92f681e09a5`

## 0. Driver verdict

`F4_ACCEPTED`

Primary research verdict accepted:

`F4_RANK_ONE_SURVIVOR_EXISTS`.

Hard target:

`GLOBAL_ZERO_SEPARATION_RANK_ONE_EXTENSION_CLASSIFIED = ACCEPTED`.

F4 does **not** prove a torsion-free-rank lift to two. This is a valid completion because the issued taskbook explicitly allowed the rank-one-survivor outcome.

## 1. Accepted theorem-level results

### 1.1 General rank-one normal form

For every finitely generated conservative carrier of torsion-free rank one with primitive signed generator and retraction,

`C ~= Z e ⊕ T`

with finite abelian `T`.

Every two-slot additive automorphism has free/torsion block form

`(v,s) -> (A v, R v + P s)`

with `A in GL_2(Z)`, `P in Aut(T^2)`, and `R` arbitrary.

### 1.2 Finite-torsion minimum-envelope theorem

For any conserved marked scalar `q`, the finite-fiber minimum

`f(n)=min_{t in T} q(n,t)`

obeys the induced free conservation equation. Under `GLOBAL_ZERO_SEPARATION`,

`f(n)>0` for every nonzero integer `n`.

The F4 report correctly refutes the stronger requested subclaim `f(1)=1`: the issued axioms normalize `q(e)=1`, not the entire torsion fiber over free coordinate one.

### 1.3 Uniform free-block obstruction

For arbitrary finite `T`, if the induced free block `A in GL_2(Z)` is not a signed permutation, mixed-difference identities plus nonnegativity force a nonzero period of `f`. This contradicts envelope zero separation.

Accepted theorem:

`GLOBAL_ZERO_SEPARATION + RANK_ONE + CONSERVATION => FREE_QUOTIENT_BLOCK_IS_SIGNED_PERMUTATION`.

### 1.4 Exact rank-one torsion loophole

The report gives an exact survivor on

`C = Z e ⊕ Z/2`

with globally zero-separating scalar and involutive cross-slot torsion mixing. Its free block is `I_2`, while the full operation is not a product of unary slot maps and sends `(e,0)` to two nonzero balanced coefficient states.

A strengthening on

`Z e ⊕ Z/3 ⊕ Z/2`

preserves the previously frozen `R,J,S` scalar invariances. Therefore the loophole is not obtained merely by deleting the accepted order-three torsion semantics.

### 1.5 Rank conclusion

The strongest accepted conclusion is:

- torsion-free rank one remains possible;
- `GLOBAL_ZERO_SEPARATION` kills every genuinely non-signed-permutation **free-quotient** mixing in rank one;
- finite torsion can still mediate genuine full-carrier cross-slot mixing while the free quotient is a signed permutation;
- no rank-two lower bound is derivable from the issued F4 conditions alone.

## 2. Driver interpretation

The F4 counterexample identifies the exact semantic loophole:

an output marked branch may be nonzero only in a newly added finite torsion direction while its projection to the old signed occurrence coordinate is zero.

For the minimal survivor,

`M(e,0)=((1,1),(0,1))` on `Z ⊕ Z/2`.

The second output is nonzero in the enriched carrier but disappears under the old signed projection.

This is mathematically legal under the F4 packet as issued. It must not be rejected by retroactively redefining `genuine mixing` to mean non-signed-permutation on the free quotient.

Whether such a pure-enrichment output should count as a native refined branch is a **new semantic question**, not an F4 theorem.

## 3. Acceptance gates

Accepted:

- `F4_RANK_ONE_CARRIER_AND_AUTOMORPHISM_NORMAL_FORM_CLASSIFIED`
- `F4_FINITE_TORSION_MIN_ENVELOPE_CLASSIFIED`
- `F4_RANK_ONE_POSITIVE_SEPARATION_MIXING_CLASSIFIED`
- `F4_MINIMUM_TORSION_FREE_RANK_LOWER_BOUND_CLASSIFIED`
- `F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED`
- `TARGET_LEAK_AUDIT_PASS`
- deterministic checker digest `be9a6cf62635ad6689510c1e4da94755a42838976921a5f66a29012f36aba12a`

No Foundation promotion is authorized.

## 4. Successor routing

Do **not** open a rank-two carrier search yet.

The next load-bearing question is semantic:

> If one native Path-formal occurrence is refined into two retained marked alternatives, must each refined alternative remain nonzero after forgetting only the new coefficient enrichment back to the old signed occurrence layer?

Candidate condition:

`FORGETFUL_BRANCH_NONDEGENERACY`:

if `M(e,0)=(x,y)` is an elementary two-branch refinement and `pi:C->Z e` is the conservative forgetful retraction, then

`pi(x) != 0` and `pi(y) != 0`.

This condition must **not** be assumed merely because it yields rank lift. A successor stage must decide whether it follows from native Path-formal/refinement typing or is a genuinely new axiom, and only then classify its rank consequence.

Driver closure note:

`F4 POSITIVE-SEPARATION CLASSIFIED; RANK-LIFT FAILED BECAUSE PURE-TORSION BRANCHES REMAIN LEGAL UNDER ISSUED SEMANTICS.`
