# D25 Proposition-16 divided-power quotient visibility boundary and direct product carrier — 2026-09-24

Status: `STRICT_ROUTE_REDUCTION / EXACT_INFORMATION_BOUNDARY / NOT_A_RESULT / UNREVIEWED`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Consumed canonical predecessor checkpoint: `.../MCP-70a0fec6896849ac81484f0e00b3f0dd/c2aa8477fbeeec2526de/_checkpoint.json@0793f426a6d661b4f55d2c1676bb6e80cdc2a1ea`.

This unit does not reopen D24 UR/JT0, the finite adjoint/Green closures, or the already-proved ASD recurrence no-go. It isolates what one extra layer of the **actual Proposition-16 coefficient-comparison route** must retain.

## 1. External source boundary

Chisholm--Deines--Long--Nebe--Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi* (Mathematics 1 (2013), DOI 10.3390/math1010009), Section 5.1, defines the formal primitive representation

`sum_{n>=1} c(n-1)/n * xi^n`

and the divided-power cohomology object used in Proposition 16 as a quotient whose denominator contains every primitive in `p A[[xi]]` vanishing at the origin. Proposition 16 then obtains in the supersingular chart the first coefficient comparisons

`1 = v*b(p-1)/p (mod p)` and `1 = w*a(p-1)/p (mod p)`,

and only the product congruence modulo `p^2`. The paper does not supply the corresponding product modulo `p^3`.

## 2. Target normalization and already-owned first lift

Retain the canonical quartic-normalized supersingular notation

`u=pU,  v=pV,  w=W,  a(p-1)=pA,  b(p-1)=B`,

with `V,W,A,B` units modulo `p` and target determinant normalization `b2=p`. The Frobenius determinant gives

`VW = -1 - p U^2`.

The first comparisons define the omitted digits

`e_a=(WA-1)/p mod p`,  `e_b=(VB-1)/p mod p`,

and `E_p=e_a+e_b`. The preceding checkpoint already proved

`a(p-1)b(p-1) = -p + p^2 (U^2-E_p)  (mod p^3)`.

## 3. Exact Proposition-16 observer no-go

The next digit is invisible not only to the ASD recurrence, but also to the **specific divided-power quotient used by Proposition 16**.

Fix any `t in F_p` and change only the p-th coefficient of the formal primitive for `omega` by

`A -> A + p W^{-1} t`,

equivalently

`a(p-1) -> a(p-1) + p^2 W^{-1} t`.

Because the primitive coefficient of `xi^p` is `a(p-1)/p=A`, the change of primitive is exactly

`p W^{-1} t * xi^p`,

which lies in the denominator `p A[[xi]]` of the Proposition-16 divided-power quotient. Hence the cohomology class seen by that observer is unchanged. The first comparison `WA=1 (mod p)` is also unchanged.

But

`e_a -> e_a+t`,

so

`E_p -> E_p+t`,

and therefore the product second digit changes by

`U^2-E_p -> U^2-E_p-t`.

Thus the Proposition-16 cohomology object at exactly the precision used in the published proof cannot determine the D25 second digit. This is an observer theorem, not a claim that the actual geometric differential lacks the digit. The missing information lives precisely in the first layer killed by the quotient.

## 4. Direct source-equivalent product carrier

Individual recovery of `e_a` and `e_b` is unnecessary at the current product observer. Define

`K_p := (a(p-1)b(p-1)+p)/p^2 mod p`.

Then algebraically

`K_p = U^2-E_p`,

so, once the already-retained matrix jet `U` is fixed,

`E_p = U^2-K_p`.

Therefore the Frobenius-side next unit can be reduced from two one-order-deeper coefficient comparisons to **one quartic-normalized product comparison modulo p^3**. This is lossless for the current product-second-digit observer. It is not claimed lossless for arbitrary future observers that separately inspect the two eigen-differential coefficients.

## 5. Minimal precision extension forced by the proof

The gauge witness shows exactly what a successful deeper comparison must add. Any proof that remains entirely inside the published quotient by `p A[[xi]]` cannot distinguish the required digit. One must instead provide one of the following, with source provenance:

1. an explicit Frobenius/coefficient calculation retaining the `p A[[xi]] / p^2 A[[xi]]` layer (or an equivalent one-step-thicker object), sufficient to compute `K_p`; or
2. a direct finite/hypergeometric evaluation of `a(p-1)b(p-1) mod p^3`; or
3. another scalar proved exactly equal to `K_p` (equivalently to `E_p` together with `U`).

This does **not** introduce a custom axiom or assert a pre-existing named `H_DR(...,(p^2))` theory. It only states the information layer that cannot be quotiented away.

## 6. Why d=3 now has a concrete target

For the d=3 family the same paper gives an exact finite expression for `a(p-1)=H_{3,p-1}(t)` before reducing modulo p, while `b(p-1)` comes from the normalized companion differential `nu=c*partial_lambda omega+omega`. Hence the next source calculation is now concrete: specialize `lambda=1/2`, carry the quartic twist and the companion differential at exact precision, and compute their product through `p^3`. There is no need to increase the ASD recurrence depth or to split `E_p` artificially.

The required remaining bridge is still nontrivial: prove that this `K_p` (or its equivalent `E_p`) maps to the finite-Gauss divided product digit `[a_parent Psi-1]/p` with the already-owned endpoint correction. Until that bridge is proved, LIFT/JT2 remains open.

## 7. BRC audit

Population: target primes `p == 13 or 19 (mod 24)`.

Observer: one additional p-adic digit of the quartic-normalized supersingular de Rham product, eventually bridged to D25 LIFT.

Carrier retained: `(U, K_p)` or equivalently `(U,E_p)`, plus quartic-twist/source normalization provenance.

Safe quotient at this observer: `(e_a,e_b) -> e_a+e_b`, equivalently direct use of `K_p`.

Unsafe quotient: the Proposition-16 quotient modulo `p A[[xi]]` alone, because it kills the exact `p*xi^p` primitive layer that changes `K_p`.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + STRICT_REDUCTION_APPLIED`.

## 8. Disposition

`PROP16_P_DIVIDED_POWER_QUOTIENT_ALONE = EXACT_NO_GO_FOR_SECOND_PRODUCT_DIGIT`.

`DIRECT_PRODUCT_CARRIER = K_p=(a(p-1)b(p-1)+p)/p^2 mod p`.

`K_p = U^2-E_p`.

`MINIMUM_NEW_LAYER = retain one scalar from the first primitive layer killed by p A[[xi]]`.

`LIFT/JT2 = OPEN`.

`NEXT_ACTION = compute K_p directly for d=3, lambda=1/2 by carrying the exact H_{3,p-1}(t) coefficient and normalized companion differential through the quartic twist to mod p^3; then prove the exact bridge from K_p/E_p to [a_parent Psi-1]/p plus the endpoint correction.`

External source: https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf , especially pp. 17-20 of the manuscript (Section 5.1 and Proposition 16).
