# D25 d=3, lambda=1/2 quartic-twist second-digit split — 2026-09-24

Status: `STRICT_ROUTE_REDUCTION / EXACT_TWIST_DIGIT / NOT_A_RESULT / UNREVIEWED`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Consumed durable predecessor: the Source checkpoint whose current Frobenius-side carrier is

`C_p := a(p-1)b(p-1) = -p + p^2 K_p (mod p^3)`,

with

`K_p = (a(p-1)b(p-1)+p)/p^2 mod p = U^2-E_p`.

This unit does not claim to compute `K_p`. It removes one exact and previously bundled part of the bridge from the quartic-normalized Frobenius product to the untwisted d=3 coefficient product.

## 1. Source-pinned quartic coordinate factor

Chisholm--Deines--Long--Nebe--Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi* (Mathematics 1 (2013), DOI 10.3390/math1010009), Section 4.2, treats d=3 by the quartic twist

`(x,y) -> (alpha^2 X, alpha^3 Y)`,  `alpha=(1-lambda_3)^(1/4)`,

and records for d=3,4 that the local parameter satisfies

`xi_old=-x/y = xi_new / (1-lambda_d)^(1/4)`.

Section 5 later writes the Frobenius-normalized change as

`xi_tilde = Delta_d^(-1/4) xi`

and the coefficient product with the factor `Delta_d^((p-1)/2)`. Comparing the two coordinate changes for d=3 gives the exact algebraic factor

`Delta_3 = (1-lambda_3)^(-1)`.

At the frozen target `lambda_3=1/2`, therefore

`Delta_3 = 2`.

This is an exact twist normalization, not only its Legendre symbol.

## 2. The target half-Fermat lift

For every target prime `p == 13 or 19 (mod 24)`, one has `p mod 8 in {5,3}`, hence `(2/p)=-1`. Euler's criterion gives

`D_p := Delta_3^((p-1)/2) = 2^((p-1)/2) == -1 (mod p)`.

Define the exact first lifted twist digit

`tau_p := (2^((p-1)/2)+1)/p  (mod p)`.

Then

`D_p = -1 + p tau_p (mod p^2)`

and consequently

`D_p^(-1) = -1 - p tau_p (mod p^2)`.

No choice of square or fourth root enters `tau_p`; it belongs to the rational twist factor itself.

## 3. Exact second-digit split

Let the durable quartic-normalized supersingular product carrier be

`C_p = -p + p^2 K_p (mod p^3)`.

Undoing only the d=3 quartic coefficient factor means multiplying by `D_p^(-1)`. Therefore

`C_p D_p^(-1)`
`= (-p+p^2 K_p)(-1-p tau_p)  (mod p^3)`
`= p + p^2(tau_p-K_p)  (mod p^3)`.

Hence the normalized-to-untwisted product second digit splits exactly as

`boxed:  TRAW_p = tau_p - K_p  (mod p)`.

Equivalently,

`K_p = tau_p - TRAW_p  (mod p)`.

Thus the quartic twist itself contributes the explicit half-Fermat scalar `tau_p`; it is not an unknown part of the remaining Frobenius/finite-Gauss bridge.

## 4. What this does and does not close

This is a strict route reduction because one exact second-digit correction has been separated from the unresolved source coefficient product. It does **not** prove that the untwisted de Rham coefficient product equals the project weighted finite-Gauss sum `W_p` modulo `p^3`, and it does not prove LIFT/JT2. Chisholm et al. only use the product at the lower precision needed for their theorem; no mod-p^3 identification is imported from that paper.

The remaining bridge now has two sharply separated pieces:

1. compute the actual `K_p` (equivalently the untwisted second digit `TRAW_p`) from the exact d=3 coefficient `H_{3,p-1}(t)` and its normalized companion differential; and
2. prove the one-order-deeper finite Clausen/truncation/endpoint relation from that untwisted product to the frozen project carrier `[a_parent Psi-1]/p` and then to `R_p`.

The explicit twist digit `tau_p` must remain visible throughout that comparison.

## 5. BRC information audit

Population: target primes `p == 13 or 19 (mod 24)`.

Branch: d=3, `lambda=1/2`, supersingular D25 Frobenius route.

Observer: one additional p-adic digit of the coefficient product.

Retained carrier: `(K_p, tau_p)` together with the label identifying normalized versus untwisted product.

Safe operation: exact quartic untwist `C_p -> C_p D_p^(-1)` through mod `p^3`.

Unsafe quotient: replacing `D_p` by only its Legendre sign `-1`; that erases `tau_p`, exactly one p-adic digit needed by D25.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + STRICT_REDUCTION_APPLIED`.

## 6. Deterministic falsifier

The companion checker verifies the algebra over all 166 target primes below 5000, with several independent test values of `K_p` for each prime. It checks exact divisibility of `2^((p-1)/2)+1` by p and the congruence

`(-p+p^2 K_p) * 2^(-(p-1)/2) == p+p^2(tau_p-K_p) (mod p^3)`.

This finite computation is regression/falsification only; the theorem is the exact two-line expansion above.

## 7. Disposition

`D3_TARGET_QUARTIC_FACTOR = Delta_3 = 2`.

`TWIST_SECOND_DIGIT = tau_p = (2^((p-1)/2)+1)/p mod p`.

`UNTWISTED_PRODUCT_SECOND_DIGIT = tau_p-K_p mod p`.

`LIFT/JT2 = OPEN`.

`NEXT_ACTION = use the exact d=3 finite coefficient H_{3,p-1}(t) and the normalized companion differential at lambda=1/2 to compute K_p / TRAW_p at source level, then compare the untwisted product one order deeper with the finite-Gauss/Clausen carrier and endpoint correction; keep tau_p explicit and do not replace the quartic factor by its sign.`

Source: https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf , especially Section 4.2 (d=3 quartic local-parameter scaling), Proposition 16, and Section 5 (the `Delta_d^((p-1)/2)` coefficient factor).
