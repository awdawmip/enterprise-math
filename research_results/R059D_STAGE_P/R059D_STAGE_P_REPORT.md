# R059D Stage P — Initial Branch Context / Symmetry Torsor / Post-Credit Identification

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `8f9028e85e527da8ef41b6779bb042bf1d3fc85b`  
Frozen parent: `c2ab05c7a101e1bebbe64306335731f7ecb35851`

## Disposition

`INITIAL_BRC_SELECTOR_REQUIRES_TAU_ODD_CONTEXT`

with simultaneous freezes:

- `BRC_SYMMETRIC_BRANCH_PAIR_IS_FREE_Z2_TORSOR`
- `TAU_FIXED_CONTEXT_CANNOT_INITIALIZE_UNIQUE_BRANCH`
- `SYMMETRY_INVARIANT_POST_CREDIT_CANNOT_BREAK_INITIAL_BRANCH_SYMMETRY`
- `SYMMETRY_INVARIANT_POST_CREDIT_INSUFFICIENT_FOR_INITIALIZATION`
- `INITIAL_BRC_SELECTION_EQUALS_EXACT_CONTEXTUAL_SINGLETON_WHEN_AVAILABLE`
- `INITIAL_BRANCH_IS_RELATIVE_CONTEXT_TORSOR`
- `INITIAL_MULTIBRANCH_IS_INTRINSIC_UNDER_FULL_SYMMETRY`
- `INITIAL_SELECTOR_STILL_NONIDENTIFIED`

The last status applies to the currently frozen fully symmetric initial state because no independent tau-odd initial context is supplied by the Stage-O input set.

## Free Z2 torsor

The branch pair is `B={0,1}` with nontrivial action `tau_B(b)=1-b`. The action is free because `1-b != b` for both Boolean values, and transitive because the unique group element `g=b0 xor b1` transports any branch to any other. Hence the branch pair is a free transitive Z2-set.

Choosing an absolute branch origin is extra structure. At a tau-fixed base state, no equivariant section can choose that origin without context.

## General contextual theorem

Let `H` carry involution `tau_H` and require

`F(tau_S(s),tau_H(h)) = 1-F(s,h)`.

At a symmetric local state `tau_S(s)=s`, any fixed context `h=tau_H(h)` would force

`F(s,h)=1-F(s,h)`,

which has no Boolean solution.

Therefore unique initialization requires a tau-nonfixed context state. In a finite context the minimum possible orbit has size two. A two-state free context is sufficient to support equivariant unique maps, but the bare torsor admits exactly two of them:

`F_plus(h)=h`

and

`F_minus(h)=1-h`.

No invariant of the bare torsor distinguishes them.

## Symmetry-invariant post-credit no-go

If all inputs and the macro supervision `Phi` are tau-invariant, exact derived initial branch structures remain flip-invariant.

- exact feasible set: `b in A iff 1-b in A`, so `A` is empty or `{0,1}`, never a singleton;
- exact residual: `R(0)=R(1)`;
- finite difference: `Delta_b R=0`;
- one-bit Mobius form `R=c0+c1 b`: flip invariance forces `c1=0`;
- rank-one straightness: the all-0 and all-1 realizations are exchanged by tau and both satisfy the same rank-one certificate.

Thus invariant post-credit cannot manufacture a first-branch asymmetry.

## Exact singleton criterion

For exact contextual constraints, reduce them to the Boolean feasible set

`A(s,h)={b in {0,1}: all exact contextual equations hold}`.

A unique initial branch is proved if and only if the full exact set is `{0}` or `{1}`. `{0,1}` remains unresolved and the empty set is inconsistent.

Two exact oriented controls are:

- `b-h=0` -> `A={h}`;
- `b+h-1=0` -> `A={1-h}`.

Both are equivariant when `h -> 1-h`. They demonstrate sufficiency of independently declared tau-odd context, not that the current symmetric state generates one.

## Context audit

Previous branch bit and previous donor relation are valid tau-odd continuation contexts, but are unavailable at a truly initial event unless a prior relation actually exists.

An exact upstream coupled constraint is a genuine positive initial-context class only if its tau-odd variable/relation exists independently before the collapse and its Boolean reduction is singleton.

Signed collapse residue is branch-conditioned: for the integer completion case `rho=1/2-b`, exchange sends `rho -> -rho`, but before selection the residue pair is `{+1/2,-1/2}`. Using the sign computed from the candidate branch to select that same branch is circular.

Finite-difference credit from invariant supervision has zero initial one-bit difference.

A predeclared donor/oriented algebraic relation can be valid initial context if it is typed before scoring and transforms under exchange.

Ingress/orientation state from earlier stages is not promoted because the authorized Stage-O input set supplies no exact transformation law for it.

Hidden coordinate order and coordinate-name preference are rejected.

## Relative torsor interpretation

For bare free two-state context torsor `H` and branch torsor `B`, the only equivariant maps are `h` and `1-h`. They are the two torsor identifications and are exchanged by the nontrivial torsor automorphism. Without an added origin/relation neither is canonical.

Therefore the initial branch is most naturally typed as a branch relative to an independently declared context torsor, not as a canonically absolute bit.

## Straight continuation replay

For fixed recipient y, the primitive branch transfers are `(0,1,-1)` and `(-1,1,0)`. They are Z-linearly independent. A nonempty transfer sequence has rank-one integer span exactly when all realized branch bits are equal.

Hence, after initialization:

`b_(k+1)=b_k`.

The previous bit becomes a valid tau-odd continuation context. This theorem does not select `b_0`.

## Scalar 5 control

For the square completion layer, `5` has legal completed neighbors `{4,9}`, so the completion-neighbor binary form transfers. But the scalar problem does not inherit the vector transverse-exchange action. Therefore the vector no-go theorem does not by itself prove scalar selector impossibility.

Freeze:

`SCALAR_5_INITIAL_SELECTOR_REMAINS_UNIDENTIFIED_BY_VECTOR_SYMMETRY_THEOREM`.

## Covariance and large backgrounds

Coordinate permutations transport recipient/donor/context relations. Global inversion transports transfer relations with the state. Transverse exchange sends branch and tau-odd context together by complement. Completion-layer affine covariance is used only when the layer is transformed with the state.

Exact symbolic backgrounds around `10^36` and completion scales `1,2,5,11` leave the torsor/context theorems unchanged. No huge enumeration is used.

## Firewalls

No nearest rounding, endpoint argmax, arbitrary reward weights, ML fitting, random tiebreak, hidden coordinate ordering, Euclidean metric/angle/norm/trig selector, path-language BRC definition, or physical probability interpretation is used.

`PHYSICAL_PROBABILITY_FROM_BRANCH_SYMMETRY = NOT_ESTABLISHED`.

## Checker

Current deterministic checker before final parent compare:

`2925/2925 PASS`

digest `5901897b9f8c69e82d273ba926c6bfedf009de70a14acf938eb2301fcf06b093`.

The checker uses symbolic finite proofs plus tiny exact oracles only. Large-background tests use closed-form integer arithmetic.

## Parent immutability

`PASS_PENDING_FINAL_GITHUB_COMPARE`

The owner branch will be compared against frozen Stage-O head before manifest/checkpoint freeze.
