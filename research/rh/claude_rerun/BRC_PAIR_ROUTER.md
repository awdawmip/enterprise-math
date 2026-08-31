# BRC_PAIR_ROUTER — exact conjugate-pair routing and spectral causal cone

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Parent head: `88c05f9452db11441054f7c65b51c31007a1555c`

Status:

`EXACT_RECTANGULAR_PAIR_ROUTER / FINITE_SPECTRAL_CAUSAL_CONE / THIN_UNSAFE_BRANCH_CONE / RH_NOT_CLOSED`

## 1. Zero alphabet and rectangular observable

For the normalized genus-zero Xi generating function

`G(z)=sum_{n>=0} a_n z^n = G(0) product_j (1+alpha_j z)`,

the coefficient sequence is the elementary-symmetric specialization `a_n=e_n(alpha)`. The consecutive Toeplitz minor therefore has the dual Jacobi–Trudi form

`D_{r,k}=det[e_{k+j-i}]_{i,j=0}^{r-1}=s_(r^k)(alpha)`,

where `(r^k)` is the rectangle with `k` rows and width `r`.

For a hypothetical off-line zeta zero pair, keep the conjugate alphabet

`Y={R exp(i theta), R exp(-i theta)}`

as one BRC atom.

## 2. Exact one-pair router

Let `X` be any remaining alphabet, `k>=2`, and `lambda=(r^k)`. The rectangular complement identity gives

`boxed: s_(r^k)(X union Y) = sum_{0<=b<=a<=r} s_(r^(k-2), r-b, r-a)(X) * s_(a,b)(Y)`.

There are exactly `(r+1)(r+2)/2` router states before any sign recoalescence.

Proof: start from the standard branching identity

`s_lambda(X union Y)=sum_mu s_mu(X) s_(lambda/mu)(Y)`.

Because `Y` has two variables, only complement partitions with at most two rows survive. For a rectangle the nonzero complement is uniquely `nu=(a,b)` and

`mu=(r^(k-2), r-b, r-a)`,

with coefficient one. Equivalently this is rectangular duality for `det^r` tensored with the dual representation. No generic LR multiplicity is present in this one-pair routing step.

## 3. Exact pair observable

For `nu=(a,b)`, `a>=b>=0`, put `m=a-b+1`. The two-variable Weyl formula gives

`s_(a,b)(Y)=R^(a+b) sin(m theta)/sin(theta)`.

Thus the router needs only `(R,theta,a,b)` for the pair-local future sign/amplitude observable.

## 4. Thin unsafe branch cone

Assume `0<|theta|<pi`. A negative pair factor requires

`sin(m|theta|)<0`,

and therefore necessarily

`m|theta|>pi`.

Let

`T(theta)=floor(pi/|theta|)`.

Since `m=a-b+1`, a potentially negative router state must satisfy

`a-b >= T(theta)`.

Hence the total number of potentially unsafe states is at most

`B_unsafe(r,theta)=((r-T+1)(r-T+2))/2`

when `r>=T`, and zero otherwise.

Near the first unsafe rank `r=T+h`, the active negative-support branch count is only `O(h^2)` rather than `O(r^2)`. All other pair-router states may recoalesce to `NONNEGATIVE` for a terminal sign query.

## 5. Spectral causal cone

For a zeta zero `rho=1/2+delta+i gamma`, the Xi zero variable satisfies

`|theta|=2 atan(|delta|/|gamma|) <= 1/|gamma|`

using only `|delta|<1/2` in the critical strip.

Every router state has `m<=r+1`. Therefore if

`|gamma| >= (r+1)/pi`,

then

`m|theta| <= (r+1)/|gamma| <= pi`,

so every two-row branch of that conjugate pair is nonnegative.

Consequently:

`boxed: a negative-support witness for rank r can involve an unsafe conjugate zero pair only at height |gamma| < (r+1)/pi.`

This is an exact **spectral causal cone**. For a fixed finite rank, the potentially sign-dangerous unresolved zero universe is finite. Higher zero pairs may be represented by recoalesced safe-support tokens for the sign observable; their exact magnitudes remain relevant only if a later nonterminal observable requires them.

## 6. Verified-prefix specialization

If all zeta zeros through height `H` are verified on the critical line, then every unverified pair satisfies `|gamma|>H`. Thus all rank-r pair routers are safe whenever

`r+1 <= pi H`.

This recovers the classical Schoenberg/verified-zero low-rank strip but now as a branch-local RCC statement. Beyond that strip the entire tail does not become unsafe: only pairs in the finite window

`H < |gamma| < (r+1)/pi`

require sign-sensitive refinement.

## 7. Relation to R021/R022

- R021 `NO_RESURRECTION`: do not collapse an active pair to a sign token if later propagation needs `(R,theta)` or branch allocation `(a,b)`.
- R022 RCC: the conjugate pair is an exact router atom because all pair-local futures factor through `(R,theta,a,b)`.
- R022 NCC: `a-b>=T(theta)` is the exact entry condition for the potentially negative branch cone.
- Branch accounting is explicit: full one-pair router size is triangular in `r`; unsafe width is triangular only in the excess above the pair threshold.

## 8. What this does and does not solve

This theorem removes infinite-zero-set branching from a fixed-rank sign query: negative support has a finite height horizon. It does **not** prove that the remaining finite unsafe branches sum to less than the positive safe mass, and it does not prove RH.

The next target remains `PAIR_CLUSTER_DOMINATION`, now sharpened to the finite causal window and the thin unsafe branch cone.
