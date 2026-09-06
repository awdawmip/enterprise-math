# RSA-270 multiplier-endpoint Plücker rank-two theorem and geometric-coupling no-go

Status: `TASK_RESEARCH / EXACT ALGEBRAIC NO-GO AT ENDPOINT OBSERVER / NO FACTOR OBTAINED`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RSA-270 / BRC multiplier cost field / multidirection geometry / endpoint observer`

## 0. Context and BRC scope

The current multiplier-lattice branch uses coprime direction pairs `(a,b)` and the factor endpoint

`x_(a,b) = a p + b q`,

with

`x_(a,b)^2 - 4abN = (ap-bq)^2`, `N=pq`.

The add-cost coordinate is

`j_(a,b) = x_(a,b) - x0_(a,b)`,

where

`x0_(a,b)=ceil(2 sqrt(abN))`

is known from `N` and the chosen direction.

The open geometric question was whether coupling several branch directions could create a new observable beyond the single scalar `S=p+q` / factor endpoint family.

This note gives an exact redundancy certificate **only for the endpoint/cost observer**. It does not erase branch path provenance, first-step `rho_k`, intermediate square-test data, or any other observer without a separate certificate.

Reuse resolution:

- BRC first-line observer audit: `REUSE_APPLIED`;
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED` at the endpoint-linear-observer horizon only;
- joint-relation directions are preserved until the exact rank-two certificate below is proved.

## 1. Endpoint map

Choose multiplier directions

`v_i=(a_i,b_i) in Z^2`

and define

`x_i = a_i p + b_i q = v_i dot (p,q)`.

Let

`Delta_(i,j) = det(v_i,v_j)=a_i b_j-b_i a_j`.

The entire endpoint vector is therefore

`x = p a + q b`,

where `a=(a_i)_i` and `b=(b_i)_i`.

Hence every finite family of multiplier endpoints has linear rank at most two before any computation.

## 2. New theorem: exact Plücker relation for every three directions

For every triple `(i,j,k)`, one has

`boxed: Delta_(i,j) x_k - Delta_(k,j) x_i - Delta_(i,k) x_j = 0`.

### Proof

The two-dimensional row vectors satisfy the exact determinant identity

`Delta_(i,j) v_k - Delta_(k,j) v_i - Delta_(i,k) v_j = 0`.

Dot with `(p,q)`. This gives the displayed endpoint relation.

Thus every third endpoint is already constrained by any two independent direction endpoints.

If `Delta_(i,j) != 0`, then

`x_k = [Delta_(k,j) x_i + Delta_(i,k) x_j] / Delta_(i,j)`.

For a unimodular pair `|Delta_(i,j)|=1`, every other endpoint is an **integer-linear** combination of the pair.

## 3. Affine rank-two theorem for add-cost coordinates

Since

`x_i = x0_i + j_i`

with known `x0_i`, the same relation becomes

`Delta_(i,j) j_k - Delta_(k,j) j_i - Delta_(i,k) j_j`
`= -Delta_(i,j) x0_k + Delta_(k,j) x0_i + Delta_(i,k) x0_j`.

The right side is known from `N` and the chosen directions.

Therefore all exact endpoint add-cost values lie in a known affine rank-two lattice. Adding more directions does not add a third independent endpoint coordinate.

This is a scope-typed BRC redundancy certificate:

`MULTIDIRECTION ENDPOINT/COST OBSERVER -> AFFINE RANK <= 2`.

It does **not** imply that the full branch trajectories are redundant.

## 4. Two-direction determinant hyperbola

Take two directions

`v_1=(a,b)`, `v_2=(c,d)`

with

`Delta=ad-bc != 0`,

and endpoints

`x_1=ap+bq`, `x_2=cp+dq`.

Then

`d x_1 - b x_2 = Delta p`,

`a x_2 - c x_1 = Delta q`.

Multiplying gives the exact conic/hyperbola equation

`boxed: (d x_1-b x_2)(a x_2-c x_1)=Delta^2 N`.

Conversely, if an integer pair `(x_1,x_2)` satisfies this equation and the two linear factors are divisible by `Delta` with positive quotients, then

`p=(d x_1-b x_2)/Delta`,

`q=(a x_2-c x_1)/Delta`

is a factorization of `N`.

Therefore the two-endpoint geometric problem is exactly a linear coordinate transform of the original factor hyperbola.

## 5. Unimodular no-go

If

`|Delta|=1`,

the map

`(p,q) -> (x_1,x_2)`

is a `GL_2(Z)` coordinate change. It preserves the full integer-lattice information with no compression and no extra arithmetic constraint.

Hence a unimodular pair of exact multiplier endpoints is **factorization-equivalent by an integer linear change of coordinates**.

This is stronger than merely saying the endpoints determine `S`: they are literally another lattice chart on `(p,q)`.

## 6. Specialization to the current best direction `(2,1)`

Pair the Fermat direction

`v_F=(1,1)`

with the current cost-field optimum

`v_2=(2,1)`.

Their determinant is

`Delta = 1*1-1*2 = -1`.

The endpoints are

`x_F=p+q`,

`x_2=2p+q`.

Therefore

`boxed: p=x_2-x_F`

`boxed: q=2x_F-x_2`

and

`boxed: (x_2-x_F)(2x_F-x_2)=N`.

In cost coordinates, with

`x_F=x0_F+j_F`, `x_2=x0_2+j_2`,

the same identity is

`[(x0_2+j_2)-(x0_F+j_F)]`
`*[2(x0_F+j_F)-(x0_2+j_2)] = N`.

So coupling the Fermat cost field to the `(2,1)` cost field does not create a new hidden scalar: it is an affine-unimodular rewriting of factorization.

## 7. Consequence for the proposed multidirection geometric route

For any finite direction family, exact endpoint data live in rank two. Once two independent endpoints are retained, all additional endpoint values satisfy exact Plücker relations.

Therefore the previously proposed family

`geometric constraints coupling several branch directions via their exact endpoints/costs`

is now closed as a source of a genuinely new observer class:

`MORE ENDPOINT DIRECTIONS != MORE INDEPENDENT ENDPOINT INFORMATION`.

A viable continuation must use data that do **not** factor through the endpoint linear map, for example a certified pre-endpoint path/correlation observable, a new relation field, or external information. Merely adding more exact multiplier endpoints, ridges, or endpoint costs cannot escape the factor hyperbola.

## 8. Relation to the previous cost-field no-go

The previous cost-field work proved quantitatively that the best single multiplier direction under the prior RSA-270 ratio band is `(2,1)` and that even after the forced mod-72 endpoint sieve its work remains infeasible.

The present theorem closes a distinct escape attempt:

- previous no-go: **scanning one or many directions is still exponentially expensive**;
- present no-go: **even exact multidirection endpoint coupling has only rank-two information and is a factor-coordinate transform**.

Together they leave no current evidence that the multiplier-endpoint family can yield a subexponential RSA-270 factorization route.

## 9. Verification

The Plücker relation and the `(1,1)/(2,1)` product identity were checked exactly on synthetic semiprimes including `101*211`, `1009*1013`, and `10007*10009`, across direction sets `(1,1),(2,1),(3,2),(5,3),(11,5)`. All identities held exactly. The proof is symbolic and does not depend on the checks.

## 10. Hard boundaries

- `ENDPOINT RANK TWO != FULL BRANCH PROCESS RANK TWO`.
- This theorem does not prove a general lower bound for integer factorization.
- It does not exclude observables that retain trajectory/order/provenance information before endpoint collapse.
- It does not factor RSA-270.
- A nonlinear function of many endpoints can still be useful computationally, but it cannot contain more raw endpoint information than the two factor coordinates unless it imports additional non-endpoint data.

## 11. Smallest unresolved unit

Do not continue by adding more endpoint directions. The next admissible RSA step must first exhibit an observable that provably fails to factor through the affine rank-two endpoint carrier while remaining computable from `N` without already knowing `p,q`. If no such observable is produced, the multiplier branch should remain closed.
