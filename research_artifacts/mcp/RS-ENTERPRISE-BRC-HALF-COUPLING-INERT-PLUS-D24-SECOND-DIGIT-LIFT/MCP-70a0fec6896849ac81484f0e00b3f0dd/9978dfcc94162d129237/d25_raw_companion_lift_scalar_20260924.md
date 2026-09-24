# D25 raw d=3 companion-lift scalar decomposition — 2026-09-24

Status: `STRICT_ROUTE_REDUCTION / EXACT_SOURCE_JET_DECOMPOSITION / NOT_A_RESULT / UNREVIEWED`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Consumed canonical predecessor: the Source checkpoint at commit `7ef371a42c154b05de2e9a88e150f1f8eb44fde7`, whose current exact twist split is

`TRAW_p = tau_p - K_p (mod p)`,

with `tau_p=(2^((p-1)/2)+1)/p mod p`.

This unit does not compute `K_p`. It identifies the one-order-deeper source scalar carried by the normalized companion differential before the finite Clausen/truncation bridge.

## 1. Source differential pair and a coordinate-safe coefficient

Chisholm--Deines--Long--Nebe--Swisher, Section 5, uses the normalized de Rham pair in the form

`nu = c * partial_lambda(omega) + omega`

for an exact source scalar `c` in the coefficient ring, and states that `a(p-1)=H_{3,p-1}(t)` while `b(p-1)` is computed from the companion accordingly.

To avoid silently identifying the Gauss--Manin derivative with ordinary differentiation of the already-expanded polynomial coefficient, define instead

`J_p := coeff_{xi^(p-1) dxi}(partial_lambda omega)`

in the same untwisted normalized source chart and local parameter used to define `a(p-1), b(p-1)`. Then coefficientwise linearity gives the exact identity

`b_raw(p-1) = a_raw(p-1) + c_p J_p`.

No claim is made here that `J_p` is merely `d H_{3,p-1}/d lambda`; any local-coordinate/Gauss--Manin correction remains inside the typed source coordinate `J_p`.

## 2. Supersingular valuation and raw first digit

For the target inert classes, the accepted supersingular coefficient comparison gives one factor of p on the omega coefficient and a unit companion coefficient. Write

`a_raw(p-1) = p alpha_p   (mod p^3)`,

with `alpha_p` a p-adic unit. Quartic untwisting multiplies by units, so this valuation is unchanged.

The preceding exact twist checkpoint proved that the untwisted product has leading sign +p:

`P_raw := a_raw(p-1)b_raw(p-1) = p + p^2 TRAW_p (mod p^3)`.

Substituting `b_raw=a_raw+c_p J_p` gives

`P_raw = p^2 alpha_p^2 + p c_p alpha_p J_p (mod p^3)`.

Therefore the known first digit is equivalent to

`c_p alpha_p J_p = 1 (mod p)`.

## 3. Exact one-scalar decomposition

Because the preceding product is 1 modulo p after dividing by p, the divided lift

`Lcomp_p := (c_p alpha_p J_p - 1)/p  (mod p)`

is well-defined. Then the product identity immediately yields

`boxed: TRAW_p = alpha_p^2 + Lcomp_p (mod p)`.

Combining with the already-canonical quartic twist split gives

`boxed: K_p = tau_p - alpha_p^2 - Lcomp_p (mod p)`.

Thus the opaque raw product second digit can be replaced, without information loss at the current observer, by:

1. `alpha_p = a_raw(p-1)/p mod p`, directly attached to the exact finite coefficient `H_{3,p-1}(t)`; and
2. one normalized companion comparison digit `Lcomp_p`.

This is a source-aligned decomposition of the same one-dimensional missing product information, not a claim that `Lcomp_p` is already known.

## 4. Why the exact companion lift cannot be quotiented away

Suppose an observer retains `c_p` only modulo p. Replacing an admissible lift by

`c_p -> c_p + p eta`, `eta in F_p`,

preserves the entire first-digit relation `c_p alpha_p J_p = 1 (mod p)`, but changes

`Lcomp_p -> Lcomp_p + eta alpha_p J_p (mod p)`.

Since `alpha_p J_p` is a unit (the product with the unit `c_p` is 1 modulo p), this shift can realize every residue in F_p. Consequently `c_p mod p`, together with the first-digit comparison, is provably insufficient for D25. A successful source computation must retain the normalized companion scalar through one further p-adic digit, or retain an invariant scalar proved exactly equivalent to `Lcomp_p`.

This is an information-boundary statement; it does not say the geometric companion differential is ambiguous. The actual `nu` fixes `c_p`. It says only that a compression which forgets the first lift of the companion normalization is not faithful for the D25 second-digit observer.

## 5. Relation to the earlier Proposition-16 no-go

The earlier durable checkpoint proved that the published divided-power quotient kills a primitive p-layer that can shift the product digit. The present decomposition locates the same required precision on the concrete d=3 companion side: after the explicit quartic digit `tau_p` is removed, the raw source product requires the divided comparison scalar `Lcomp_p`.

This does not replace `K_p` by more dimensions. At the declared product observer, `K_p <-> (alpha_p, Lcomp_p)` is useful only because `alpha_p` is attached directly to the exact finite H coefficient; the genuinely new companion-side input remains one scalar.

## 6. BRC audit

Population: `p == 13 or 19 (mod 24)`.

Branch: d=3, lambda=1/2, untwisted normalized source differential pair.

Observer: the second p-adic digit of the product, equivalently D25 `K_p`.

Retained typed coordinates: `(tau_p, alpha_p, Lcomp_p)` plus the label that `J_p` is the coefficient of the Gauss--Manin derivative in the same local source chart.

Safe operation: `K_p = tau_p-alpha_p^2-Lcomp_p`.

Unsafe quotient: retain only `c_p mod p` or only the first comparison `c_p alpha_p J_p=1 mod p`; either erases an arbitrary F_p shift of the needed second digit.

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + STRICT_REDUCTION_APPLIED`.

## 7. Disposition

`RAW_PRODUCT_SECOND_DIGIT = alpha_p^2 + Lcomp_p`.

`Lcomp_p = (c_p alpha_p J_p-1)/p mod p`.

`K_p = tau_p-alpha_p^2-Lcomp_p mod p`.

`COMPANION_NORMALIZATION_MOD_P_ONLY = EXACTLY_INSUFFICIENT_FOR_D25`.

`LIFT/JT2 = OPEN`.

`NEXT_ACTION = compute alpha_p directly from the exact H_{3,p-1}(t) coefficient and compute the single divided companion scalar Lcomp_p from the exact normalized Gauss--Manin companion through one additional p-adic digit; then prove the already-required one-order-deeper finite Clausen/truncation/endpoint bridge. Do not replace J_p by an ordinary polynomial derivative unless that coordinate identification is proved.`

External source: Chisholm--Deines--Long--Nebe--Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), especially Section 3.4 and the proof of Theorems 1--2 in Section 5.
