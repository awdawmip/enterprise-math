# R283 — Resonance-stratified finite-grid certificates for BRC Port observers

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED**.
Science input pin retained: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Direct predecessor: R282 at `ea9d315ceaab0e29cc963de8c31b9b008388e5a5`, `research_notes/portable_direct/R282_FINITE_GRID_PORT_OBSERVER_EQUIVALENCE_20261118.md`.
This is a result about the typed, finite, strictly stable, nonnegative-rational, labeled BRC Port subsystem with *matched additive edge edits*. It does not change P000 or assert an unconstructed map into native X6 dynamics.

## 1. Problem and exact notation

R282 proved that, for `m` matched named rank-one edge edits, equality of each declared rational response on a three-point-per-coordinate grid implies rational-function equality. Its finite-modulus version assumed p-integral coefficient presentations and unit denominators. This note derives a finite-digit certificate across nonunit denominator (resonance) strata, including the p=2 interpolation penalty, and identifies a sharp obstruction to a uniform unstratified finite-digit claim.

Let `W_h(x)=W_h+sum_{i=1}^m x_i E_i`, `h=1,2`, be two finite nonnegative rational matrices. The `E_i=e_{u_i}e_{v_i}^T` are the *same, named, unit-weight additive edit matrices* for both models. On a shared set `Omega` of admissible rational edits, all row sums are strictly less than 1. For one declared matched output pair `(a,b)`, let
`F_h(x)=[(I-W_h(x))^{-1}]_{ab}=N_h(x)/D_h(x)`.
Determinant/cofactor presentations can be chosen with `N_h,D_h` multiaffine in every `x_i`. Multiply each pair by any suitable nonzero rational scalar so all its coefficients lie in `Z_(p)`. Define the cross-product
`P(x)=N_1(x)D_2(x)-N_2(x)D_1(x)`.
It has degree at most 2 in each coordinate. Write `v_p(0)=+infinity`. All inputs of the modular theorem are in `Z_(p)^m`, denominators at the test/target points are *nonzero* (but need not be p-adic units).

For each edit coordinate choose three distinct p-integral rational test weights `T_i={t_i0,t_i1,t_i2}`; assume their full tensor grid `G=product_i T_i` is physically admissible to both models. Define the explicitly computable interpolation loss
`kappa_i=max_{j=0,1,2} sum_{l != j} v_p(t_ij-t_il)` and `kappa=sum_i kappa_i`.
Because all three nodes are p-integral, `kappa_i>=0`.

## 2. Theorem R283-A: nonunit-denominator grid transfer

**Statement.** For any such pair of response presentations, with `s(u)=v_p(D_1(u))+v_p(D_2(u))` at any `u` where both denominators are nonzero, and any integer `M`, the finite conditions

`v_p(F_1(u)-F_2(u)) >= M+kappa-s(u) ` for **every** `u in G`

imply that **every coefficient of `P` has p-adic valuation at least `M`**. Thus for any p-integral admissible target `x` with `D_1(x)D_2(x) != 0`,

`v_p(F_1(x)-F_2(x)) >= M-s(x)`.

In particular, fix an integer observation precision `k>=1` and a target resonance stratum
`Omega_T={x in Omega intersect Z_(p)^m : s(x)<=T}`, where `T` is an integer. If the grid differences satisfy

`v_p(F_1(u)-F_2(u)) >= k+T+kappa-s(u)` for all `u in G`,

then **`F_1(x) == F_2(x) (mod p^k)` for every `x in Omega_T`**. The integer `T` is a declared target-stratum bound, not necessarily global.

**Proof.** Each degree-at-most-two polynomial over `Q` is recovered by three-point Lagrange interpolation. Let
`L_ij(X)=product_{l != j}(X-t_il)/(t_ij-t_il)`.
All numerator coefficients are p-integral; the denominator has valuation `sum_{l != j}v_p(t_ij-t_il)<=kappa_i`. Hence coefficients of `L_ij` belong to `p^(-kappa_i)Z_(p)`. Tensor-product interpolation gives

`P(x)=sum_{u in G} P(u) product_i L_i,j_i(x_i)`.

The sampled inequality yields `v_p(P(u))=v_p(F_1(u)-F_2(u))+s(u)>=M+kappa`. Each basis-product coefficient has valuation at least `-kappa`; therefore each coefficient of `P` has valuation at least `M`. For p-integral `x`, `v_p(P(x))>=M`, and division by the two nonzero denominators gives the target bound. Set `M=k+T` for the stratum claim. QED.

This theorem extends verbatim to any finite declared collection of outputs, using each output's own `N_h,D_h,P,s`, and the same grid. It controls both final observations and all intermediate reads obtained after admissible prefixes of additive edits, since every prefix corresponds to another allowed edit vector.

## 3. Theorem R283-B: p=2 interpolation penalty is unavoidable

For primes `p>=3`, choose three pairwise distinct residues modulo p in each coordinate: then `kappa_i=0`, recovering R282's unit-difference interpolation with no loss even when observation denominators have positive valuation. For `p=2`, any three p-integral nodes contain two with equal residue, so at least one Lagrange denominator is even and `kappa_i>=1`. This lower bound is achieved, with all values in `[0,1)`, by `T_i={0,1/5,2/5}` (`kappa_i=1`).

The `m`-digit tensor penalty is attained for the **general coordinatewise-quadratic interpolation class**: the polynomial
`P_m(x)=product_{i=1}^m x_i(1/5-x_i)`
has a unit leading coefficient, but its values on `{0,1/5,2/5}^m` are all zero except at the all-`2/5` corner, where the value is `(-2/25)^m`, divisible by `2^m`. Thus `m` lost digits cannot be improved for arbitrary separately quadratic polynomials without additional structure.

A **typed BRC cross-product** already realizes the one-coordinate loss. On Ports 0,1,2 take baseline edges `0->1=a`, `2->0=b`, `2->1=gamma`, edit `1->2` by the same `x`, and read output (0,0). Then `F(x)=(1-gamma*x)/(1-(gamma+a*b)x)`. Model 1 uses `(a,b,gamma)=(1/4,1/4,0)`; model 2 uses `(1/4,6/25,1/5)`. Their responses are

`F_1(x)=1/(1-x/16)`, `F_2(x)=(1-x/5)/(1-13x/50)`.

Both are strictly stable at the three nodes `0,1/5,2/5`; they agree at the first two and differ at the third (`40/39` versus `115/112`). Using p=2 integral presentations `(N_1,D_1)=(16,16-x)`, `(N_2,D_2)=(2-2x/5,2-13x/25)`, the cross product is

`P(x)=N_1D_2-N_2D_1=(2/5)x(1/5-x)`.

Every coefficient has valuation >=1 and one has exactly 1; its grid values have minimum valuation **2**. Hence the loss `kappa=1` is attained by an actual matched-edge BRC Port response pair, not only by arbitrary polynomials. No assertion about the universal m-coordinate sharpness *within BRC response pairs* is needed for this theorem.

## 4. Theorem R283-C: no uniform finite-digit grid without resonance control

There is a direct counterexample even for one named editable self-loop, p=13 and strictly stable positive-rational models. Fix any finite set `G_0` of p-integral test weights with `0<=x<1/2`, and any desired sample agreement precision `H`. For sufficiently large integer `N>=1`, set

`delta_N=13^N/(1+13^(2N))`, `w_1=1/2`, `w_2=1/2+delta_N`, and `F_h(x)=1/(1-w_h-x)`.

All points in the fixed grid remain admissible when `N` is sufficiently large. At any fixed test point, put `d=v_13(1/2-x)`. If `N>d`, then `v_13(1/2-delta_N-x)=d`, and

`v_13(F_2(x)-F_1(x))=N-2d`.

Choosing `N` larger than the finitely many `H+2d` makes the two observers agree modulo `13^H` at every fixed test point.

But for every integer `t>N`, take `epsilon_t=13^t/(1+4*13^t)` and the *same legal edge edit* `x_t=1/2-epsilon_t`. We have `0<delta_N<epsilon_t<1/2`, hence both models stay strictly stable. Yet

`v_13(1-w_1-x_t)=t`, `v_13(1-w_2-x_t)=N`, and

`v_13(F_2(x_t)-F_1(x_t))=N-t-N=-t`.

Thus arbitrarily accurate finite-grid p-adic agreement cannot establish a *global, unbounded-resonance* finite-digit equivalence. A declared resonance-depth bound or an exact-rational equality certificate is logically necessary for the requested uniform conclusion. The construction shows that the p-adic resonance depth can increase without nearing the real instability boundary: `x_t` approaches `1/4` in the ordinary real metric.

## 5. Execution, provenance, and remaining questions

Checker: `R283_stratified_port_grid_checker.py`, Python standard-library `fractions.Fraction`. Exact checks: 124 nonzero quadratic coefficient triples each for p=2 and 13 (248); 4 p=13 resonance pairs `(N,t)=(1,2),(2,3),(4,7),(6,10)`; p=2 BRC sharpness with three exact rational outputs, and tensor examples m=1..4. Saved result: `R283_verification.json` (PASS). These finite tests support only the displayed examples; universal statements above follow from the Lagrange and valuation proofs.

Scientific scope: auxiliary typed labeled Port algebra; P000/native X6, source identity, branching history and physical interpretation remain governed by their separate contracts. New work has no formal CLAIM, Result, independent review, or automatic main admission.

**Next discriminating question:** Identify which BRC Port transfer graphs force the cross-product coefficients into a smaller interpolation module so that fewer than `3^m` test points or fewer than `m` binary interpolation-loss digits suffice. For native X6 transfer, first construct the provenance-preserving Port map and test its update naturality; do not infer it from auxiliary rational identities alone.
