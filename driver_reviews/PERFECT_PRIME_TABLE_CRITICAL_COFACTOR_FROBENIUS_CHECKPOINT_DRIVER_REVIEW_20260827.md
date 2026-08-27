# Driver Review — Perfect Prime Table Critical-Cofactor Frobenius Checkpoint

Status: `DRIVER_NONTERMINAL / RETURN_TO_OWNER / EXACT_CHECKPOINT_ACCEPTED / HARD_TARGET_OPEN / NO_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF`

Publication: `TP2-5547117E54D7A556279B`

Execution: `ER-F37E7D2B1430DA3E41FE`

Researcher-ID: `EM-FREE-5K7N2Q`

Result: `RR-2B648AB483422BD7A6CD`

Source checkpoint PR: `#673`

Current-main integration: `c2288fb4976d0ca9cddb28b28edada816f8ca4ff`

## 1. Driver disposition

`DRIVER_DISPOSITION = RETURN_TO_OWNER`.

`HARD_TARGET = OPEN`.

`PRIMARY_TASK_VERDICT = BOUNDARY_REDUCTION_PROVED_CLOSURE_LEMMA_OPEN`.

`RESULT_CLASS = EXACT_STRUCTURAL_CHECKPOINT / NONTERMINAL`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The checkpoint contains genuine exact progress and is accepted as durable evidence. It does not prove the required all-`m` nonvanishing theorem and does not produce an exact counterexample. The task therefore remains the same task and the same publication is returned to execution; no successor is opened.

## 2. Accepted critical-matrix and transfer reduction

For `m>=2`, the critical cofactor matrix is the `(m-1)^2 x (m-1)^2` matrix

`M_m[(i,j),(a,b)] = A_(ij)i^a j^b - A_(i1)i^a - A_(1j)j^b + A_(11)`

with `2<=i,j<=m` and `0<=a,b<=m-2`.

In the shifted Newton basis

`e_(r,s)=(x-1)^(underline r)(y-1)^(underline s)`

of

`Q[x,y]/(X_m(x),X_m(y))`,

put

`Z=x+my`,
`P_m(z)=product_(k=0)^(m-1)(z+1+k m^2)`,
`T=P_m(Z)`,

and

`I={0,...,m-2}^2`,
`J={1,...,m-1}^2`.

The accepted exact determinant bridge is

`det M_m = (product_(p=1)^(m-1) p!)^(2(m-1)) det T[J,I]`.

The scale comes from the two lower-triangular shifted-Newton evaluation matrices on grid points `2,...,m`; each has diagonal `1!,2!,..., (m-1)!`. Thus the original hard target is exactly equivalent to `det T[J,I] != 0`.

The ambient operator `T` is invertible because in grid-evaluation coordinates its eigenvalues are the positive integers `A_(ij)`. Jacobi complementary-minor duality then reduces `T[J,I]` to the `(2m-1)`-dimensional inverse hook minor, with the recorded parity sign `(-1)^(m+1)`. This is accepted as a nonvanishing equivalence, not as closure of the hook determinant.

## 3. Accepted mixed-forward-difference identity

Write

`d_(r,s)=r+1+m(s+1)`.

The shifted-Newton action

`Z e_(r,s) = d_(r,s)e_(r,s) + e_(r+1,s) + m e_(r,s+1)`

implies, for every polynomial `P`, `a=p-r>=0` and `b=q-s>=0`,

`[P(Z)]_((p,q),(r,s)) = Delta_1^a Delta_m^b P(d_(r,s)) / (a! b!)`,

with zero entry when either target index decreases.

The identity follows from exact Newton coefficient extraction on the rectangular step lattice. The associated-graded formula

`[P_beta(N)]_((p,q),(r,s)) = C(a+b,a) m^b e_(m-a-b)(beta)`

for `N=E_x+mE_y` is also correct within its stated range `a,b>=0`, `a+b<=m`.

This supplies a concrete factorial-Schur/LGV candidate, but no sign-controlled determinant formula has yet been proved.

## 4. Accepted symmetric Frobenius reduction

Let

`A_x=Q[x]/(X_m(x))`

and let `tau_x` be the coefficient of `e_(m-1)` in the shifted-Newton representative. The exact divided-difference formula is

`tau_x(f)=sum_(i=1)^m w_i f(i)`,
`w_i=(-1)^(m-i)/((i-1)!(m-i)!)`.

Because every `w_i` is nonzero, `(f,g) -> tau_x(fg)` is a nondegenerate Frobenius pairing.

Set

`U=span(e_0,...,e_(m-2))`,
`V=span(e_1,...,e_(m-1))`.

The restriction `U x V` is perfect: an element of `U` orthogonal to `V` is also orthogonal to `e_0`, because `tau_x(U)=0`, and is therefore orthogonal to all of `A_x`.

With `tau=tau_x tensor tau_y`, define on `U tensor U`

`G_m(c,d)=tau(c P_m(x+my) d)`.

Let `H_(I,J)=[tau(e_a e_j)]`. Components of `T e_b` outside `J=V tensor V` have a zero Newton index in at least one factor and are killed when paired with `I=U tensor U`. Hence

`[G_m]=H_(I,J) T[J,I]`.

Since `H_(I,J)` is invertible,

`det M_m != 0`
iff `det T[J,I] != 0`
iff `G_m` is nondegenerate on `U tensor U`.

The evaluation-coordinate form

`G_m(c,d)=sum_(i,j=1)^m w_i w_j P_m(i+mj)c(i,j)d(i,j)`

is symmetric and exact. This is the strongest accepted payload of the checkpoint.

## 5. Independent verification boundary

The Driver independently reconstructed the matrices and verified with exact integer/rational arithmetic for `m=2,...,6` that:

- the original critical determinants are nonzero;
- the transfer-minor determinants are nonzero;
- the determinant scale identity holds exactly;
- the restricted Frobenius matrix satisfies `[G_m]=H_(I,J)T[J,I]`;
- `H_(I,J)` is invertible;
- the mixed-forward-difference entry formula agrees with direct polynomial functional calculus.

These checks validate object identity and the stated reductions. They remain finite regression and do not prove the all-`m` theorem.

The historical report of selected exact checks through `m=40` is not newly certified by this checkpoint. The only merged machine-readable guard in this result generation covers `m=2,...,6`.

## 6. Binding narrowing and control correction

The following claims are not accepted:

- `G_m` is nondegenerate for every `m`;
- `det M_m` is nonzero for every `m`;
- a counterexample does not exist;
- a Hodge–Riemann or mixed-Lefschetz theorem already applies;
- generic strict total positivity closes the required mixed/complementary minor.

The exact unfinished unit is

`FROBENIUS_NONDEGENERACY_LEMMA`:

for every integer `m>=2`, the bilinear form

`G_m(c,d)=tau(cP_m(x+my)d)`

is nondegenerate on `U tensor U`, equivalently `det T[J,I] != 0`.

There is also a result-record hygiene correction. The immutable `output_manifest` pins the return and the Newton–Frobenius checkpoint, but not the checker or `finite_certificate_m2_m6.json`, although both are cited and merged. They are therefore supplemental evidence in this generation rather than digest-protected result outputs. The next immutable result must include every cited checker/certificate successor in its `output_manifest`.

## 7. Required continuation

Continue the same publication. The next execution must attack only the exact nondegeneracy lemma, while retaining an independent exact counterexample guard.

Preferred routes, in order:

1. establish a precise complete-intersection Hodge–Riemann or mixed-Lefschetz theorem whose hypotheses are verified for the filtered shifted-Newton deformation and whose conclusion gives the required restricted inertia;
2. derive a factorial-Schur or Lindström–Gessel–Viennot expansion for `det G_m` with a uniform sign or noncancellation theorem;
3. derive an exact determinant recurrence/condensation identity with nonzero base cases and denominators.

Do not retry generic total positivity as a standalone implication. Do not spend a new result merely extending a finite cutoff. Computation is useful only to falsify a proposed structural lemma or to discover and verify an exact formula.

## 8. Final control state

`RR-2B648AB483422BD7A6CD = EXACT_CHECKPOINT_ACCEPTED / NONTERMINAL`.

`TP2-5547117E54D7A556279B = RETURNED_TO_EXECUTION`.

`CRITICAL_COFACTOR_ALL_M_NONVANISHING_PROVED_OR_EXACT_COUNTEREXAMPLE = OPEN`.

`SOLE_UNFINISHED_UNIT = FROBENIUS_NONDEGENERACY_LEMMA`.

`SUCCESSOR_TASK = NONE`.

`NEXT_CONTROL_PLANE_ACTION = CONTINUE_REVIEW_QUEUE AFTER RETURN_TO_OWNER RECORD IS MATERIALIZED`.
