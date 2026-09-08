# #1162 — rooted-forest jet as a derivative-free higher inverse-spectrum carrier

Status: RESEARCH_NOTE / FINITE OBSERVER FACTORIZATION / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-forest-jet-roughness-carrier-20260908-b62d
Date: 2026-09-08

## 1. Motivation

The exact C4 counterexample shows that the Basel/m=1 nonnegative roughness defect does not extend as a one-scalar positive defect to higher inverse moments. The replacement should not be a high-order microscopic derivative. This note gives a finite combinatorial carrier instead.

## 2. Finite rooted-forest jet

Let G be any finite connected weighted graph with positive edge conductances and Laplacian L. Write

`det(L+tI)=c_1 t+c_2 t^2+...+c_N t^N`.

By the matrix-forest theorem every `c_r` is a finite positive rooted-forest sum. No spectral interpolation is needed to define it.

Let the positive Laplacian eigenvalues be `lambda_1,...,lambda_(N-1)` only as algebraic roots. Then

`det(L+tI)/t = c_1 product_i(1+t/lambda_i)`.

Therefore

`e_k := c_(k+1)/c_1`

is exactly the kth elementary symmetric polynomial of the inverse eigenvalues `lambda_i^(-1)`.

Define the order-m normalized forest jet

`J_m(G)=(e_1,...,e_m)
      =(c_2/c_1,...,c_(m+1)/c_1)`.

This is a finite combinatorial object.

## 3. Exact factorization of inverse moments

Let

`p_j=Tr[(L^+)^j]=sum_i lambda_i^(-j)`.

Newton identities give the triangular recurrence

`p_j - e_1p_(j-1)+e_2p_(j-2)-...+(-1)^j j e_j=0`.

Hence every output `p_1,...,p_m` factors exactly through `J_m(G)`.

Conversely Newton identities can be inverted recursively to recover every `e_j`, j<=m, from `p_1,...,p_j`. Thus, for the future language consisting of the first m inverse spectral moments, the normalized forest jet and the moment jet contain exactly the same algebraic information.

This is an exact observer quotient, not an approximation.

## 4. First two orders

For m=1,

`p_1=e_1=c_2/c_1`.

On a cycle the effective-resistance structure allows a further special compression to the single positive roughness defect D after scale normalization. That extra compression is Basel-order specific.

For m=2,

`p_2=e_1^2-2e_2
    =(c_2/c_1)^2-2c_3/c_1`.

The new coefficient `c_3` enters with a negative sign in the moment readout. Thus positivity of the individual forest sums does not imply a one-sided roughness response. This finite algebraic fact is consistent with the exact alternating-C4 no-go where roughness raises `p_2`.

For m=3,

`p_3=e_1^3-3e_1e_2+3e_3`.

Again only a finite additional forest layer is needed.

## 5. Roughness meaning

Changing finite edge weights changes the forest sums `c_r` by finite positive algebraic rules. The higher inverse-moment observer should therefore carry the required forest jet rather than infer behavior from the m=1 defect or from derivatives of a smooth completion.

This separates three structures:

1. positive combinatorial carrier: rooted-forest weights;
2. finite algebraic observer: Newton signed combination;
3. integer refinement: actual graph/subdivision operation.

Signs enter only at the declared readout stage. They are not silently reinterpreted as positive branch mass.

## 6. Observer-relative sufficiency and generic minimality

For the declared future outputs `(p_1,...,p_m)`, the map between `(e_1,...,e_m)` and `(p_1,...,p_m)` is triangular with nonzero diagonal coefficients. Hence neither jet can be reduced by simply dropping one coordinate while retaining all m outputs generically.

This is a finite analogue of a jet, but it is combinatorial/algebraic rather than differential: no below-resolution limit is used.

## 7. Interaction with the cycle refoundation

For the unweighted cycle, the previous rooted-forest formula

`c_r(N)=(N/r) binom(N+r-1,2r-1)`

makes the entire jet explicit and proves that every normalized inverse moment is a finite polynomial in `N^(-2)`. The stable integer-refinement projector can then quotient the finite-size modes with condition number `<2` for integer q>=2.

For rough weighted cycles, the same jet supplies the natural candidate repair hierarchy. Exact transformation laws of `J_m` under allowed subdivision rules are the next target.

## 8. BRC resolution

REUSE_APPLIED: observer/future-operation factorization. Full weighted-graph microstructure is collapsed to `J_m` only for the future language of the first m inverse moments. Rooted-forest multiplicities/weights are retained until the c_r are formed; signed Newton combinations happen only at readout.

Positive recurrent BRC machinery is NOT_APPLICABLE to the signed Newton readout itself.

## 9. Prior-art boundary

The matrix-forest theorem, elementary symmetric polynomials and Newton identities are classical. No novelty is claimed for those ingredients. The purpose here is refoundation after the derivative-stability correction: a finite forest jet replaces an inadmissible microscopic differential jet as the exact carrier for higher inverse-spectrum outputs.

## 10. Next

1. Derive the transformation of `J_2=(c_2/c_1,c_3/c_1)` under equal and unequal cycle subdivision.
2. Determine whether a lower-dimensional cycle-specific port than the generic forest jet exists for m=2.
3. Combine forest-jet transformation with cross-q finite falsifiers and honest roughness envelopes.
