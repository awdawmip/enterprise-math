# D25 Gauss–Manin representative gauge boundary and hypergeometric companion bridge — 2026-09-24

Status: `STRICT_ROUTE_REDUCTION / EXACT_INFORMATION_BOUNDARY / ALL_TARGET_FIRST_DIGIT_BRIDGE / LIFT_OPEN / NOT_A_RESULT / UNREVIEWED`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Consumed durable frontier: the current Source checkpoint after the exact raw-coefficient bridge `alpha_p = G_T - D_p - E_p (mod p)`, together with `TRAW_p = alpha_p^2 + Lcomp_p` and `Lcomp_p=(c_p alpha_p J_p-1)/p (mod p)` in the normalized-companion convention.

This unit does **not** reopen D24 UR/JT0 and does not claim JT2/LIFT. It audits exactly what the published Gauss–Manin source data can and cannot determine one p-adic digit deeper.

## 1. Exact source boundary

Chisholm–Deines–Long–Nebe–Swisher work in algebraic de Rham cohomology. Their Section 3.4 places `partial_lambda omega` in `H^1_DR` and constructs the CM companion eigenclass from the Gauss–Manin connection. In the proof of Theorems 1–2 they write, for the local uniformizer `xi=-x/y`, `nu = c partial_lambda omega + omega` and use the formal coefficients `a(p-1), b(p-1)`, with leading coefficients normalized to 1. Proposition 16 proves only the product congruence modulo `p^2`; it does not publish a modulo-`p^3` comparison.

This distinction matters at D25 precision. A de Rham class does not, by itself, remember an exact representative.

Let a chosen representative have local expansion `partial_lambda omega = ... + J_p xi^(p-1) dxi + ...`. Change only the representative by an exact relative differential whose primitive begins `F = eta xi^p + O(xi^(p+1))`. Then `d_rel F = p eta xi^(p-1) dxi + O(xi^p) dxi`, hence `J_p -> J_p + p eta`. The cohomology class is unchanged. The leading `xi^0 dxi` coefficient is unchanged for `p>1`. Every first-digit comparison modulo p is unchanged.

Now write the supersingular source coefficient as `a(p-1)=p alpha_p` with `alpha_p` a unit modulo p, and let the companion coefficient be `b(p-1)=a(p-1)+c_p J_p`. Whatever fixed nonzero first-digit unit is used by the chosen normalization, the product shift is exactly `Delta[a(p-1)b(p-1)] = p^2 c_p alpha_p eta (mod p^3)`. Equivalently, in the current normalized convention `c_p alpha_p J_p = 1 (mod p)`, `Lcomp_p -> Lcomp_p + c_0 alpha_0 eta (mod p)`, where `c_0, alpha_0` are reductions modulo p.

Because the first comparison makes `c_0 alpha_0` a unit, eta can change the D25 digit arbitrarily while preserving the de Rham class, leading coefficient, all modulo-p comparisons, and the published modulo-`p^2` product statement.

**Theorem (representative-gauge boundary).** The Gauss–Manin cohomology class plus leading-coefficient normalization and Proposition-16 precision do not determine `Lcomp_p`. A D25 proof must additionally pin an exact local representative through the `p xi^(p-1) dxi` layer, or supply one invariant scalar proved equal to the resulting divided companion digit. This is a route-specific information boundary, not a no-go for Gauss–Manin/Frobenius methods.

## 2. Canonical fixed-xi candidate and a source/hypergeometric distinction

For `d=3` the source family is `E_3(t): y^2 + xy + (t/27)y = x^3`. Lemma 12 expands the invariant differential in the relative coordinate `xi=-x/y`: `omega = H(xi,t) dxi = sum_{n>=1} H_{3,n-1}(t) xi^(n-1) dxi`. At the target `lambda=4t(1-t)=1/2`, choose `s^2=2`, `t=(2-s)/4`. Then `d lambda/dt = 2s` and `dt/d lambda = 1/(2s)=s/4`.

A concrete formal trivialization is therefore obtained by holding xi fixed. Its coefficient derivative is `J_p^(xi) := (s/4) partial_t H_{3,p-1}(t)`. This is an exact representative choice. It is **not** asserted to be interchangeable with an arbitrary representative of the Gauss–Manin class at D25 precision; Section 1 explains the missing exact-form datum.

## 3. All-target hypergeometric companion lemma from the accepted D24 theorem

Define `F_p(t)= sum_{k=0}^{p-1} ((1/3)_k(2/3)_k/(k!)^2) t^k` and the corresponding unweighted `3F2` polynomial `S_p(lambda)`. The published truncated Clausen lemma gives, coefficientwise, `F_p(t)^2 = S_p(lambda) (mod p^2)`, `lambda=4t(1-t)`. Differentiating this polynomial congruence preserves modulus `p^2`: `2 F_p F_p' = (d lambda/dt) S_p'(lambda) (mod p^2)`.

For the target supersingular primes, `F_p(t)=0 (mod p)`. Put `beta_p = F_p(t)/p (mod p)`, `J_p^F = (dt/dlambda) F_p'(t) = (s/4)F_p'(t) (mod p)`. The already accepted D24 all-target theorem is `W_p=(1+6 lambda d/dlambda)S_p(lambda)=p (mod p^2)`. At `lambda=1/2`, divide the differentiated Clausen identity by p after using `F_p^2=0 (mod p^2)`. This gives `W_p/p = (3s/2) beta_p F_p'(t) = 6 beta_p J_p^F (mod p)`. Therefore, for every target prime, `boxed: 6 beta_p J_p^F = 1 (mod p)`. Equation (3) is an all-target theorem because it is a formal consequence of the already accepted D24 theorem plus the published polynomial Clausen congruence. No finite scan is used as proof.

## 4. Exact correction from the period truncation to the formal coefficient

The exact formal coefficient used by Proposition 16 is `H_p := H_{3,p-1}(t)`, and the current durable checkpoint writes `alpha_p = H_p/p (mod p)`. Since Lemma 12 gives `H_p = F_p (mod p)`, the fixed-xi derivatives satisfy `J_p^(xi) = J_p^F (mod p)`. Define `C_p := (F_p(t)-H_p)/p (mod p) = beta_p-alpha_p`. Then the previous identity gives the exact first-digit bridge `boxed: 6 alpha_p J_p^(xi) = 1 - 6 C_p J_p^F (mod p)`.

Thus the period companion with coefficient 6 and the exact formal coefficient companion differ by a genuine p-layer correction. At D25 precision this correction cannot be silently absorbed into a change of notation. In particular, if the current normalized `Lcomp_p` convention requires `c_0 alpha_p J_p^(xi)=1`, then `c_0 = (alpha_p J_p^(xi))^(-1)` and replacing `c_0` by the period coefficient 6 is justified only after proving the correction term vanishes, which it generally does not.

This repairs a potential normalization shortcut in the earlier companion decomposition: `J_p` remains a typed coefficient of the exact normalized source representative; it must not be identified with the ordinary derivative of a truncated period without the representative/normalization bridge.

## 5. Deterministic regression and a sharp normalization witness

The companion checker works in `R_p=(Z/p^2 Z)[s]/(s^2-2)` and reconstructs both `H_{3,p-1}(t)` from Lemma 12 and `F_p(t)` directly. For every one of the 166 target primes `p<5000` it verifies: both are divisible by p; `J_p^(xi)=J_p^F (mod p)`; `6 beta_p J_p^F=1`; the exact correction identity; and the observed fixed-xi normalization witness `6 alpha_p J_p^(xi)=2s-1 (mod p)`. The fifth identity is reported **only as finite regression / a normalization witness**, not as an all-prime theorem. Its role is diagnostic: the correction is visibly nonzero throughout the checked target range, so quotienting the formal coefficient into the period normalization would erase real structure.

## 6. BRC audit

Population: primes `p == 13 or 19 (mod 24)`. Branch: `d=3`, `lambda=1/2`, supersingular D25 source/Frobenius lane. Observer: the divided second product digit modulo p. Retained coordinates: `(alpha_p, beta_p, C_p, J_p^(xi), J_p^F, Lcomp_p)` plus the representative label. Safe quotient: `J_p^(xi)=J_p^F (mod p)` only at the first-digit observer. Unsafe quotient: identify the Gauss–Manin class with a local differential representative one p-layer deeper; replace the source companion normalization by 6 without paying `C_p`; or use Proposition 16 modulo `p^2` as if it determined the product modulo `p^3`. `BRC_REUSE_RESOLUTION = REUSE_APPLIED + STRICT_REDUCTION_APPLIED`.

## 7. Disposition

`HYPERGEOMETRIC_FIRST_DIGIT_COMPANION = PROVED: 6 beta_p J_p^F = 1`.

`FORMAL_COEFFICIENT_CORRECTION = PROVED: 6 alpha_p J_p^(xi) = 1 - 6 C_p J_p^F`.

`GAUSS_MANIN_CLASS_PLUS_FIRST_ORDER_NORMALIZATION = EXACTLY_INSUFFICIENT_FOR_Lcomp_p`.

`MINIMUM_ADDITIONAL_SOURCE_INFORMATION = ONE_PINNED_EXACT_REPRESENTATIVE_OR_ONE_EQUIVALENT_DIVIDED_NORMALIZATION_SCALAR`.

`LIFT/JT2 = OPEN`.

Next action: use the explicit d=3 Weierstrass model and the exact CM companion eigenline to pin the actual normalized representative (or its invariant divided normalization scalar) through the p-layer, then express that single scalar in the existing finite-Gauss cutoff/endpoint carrier. Preserve the exact-form gauge and `C_p`; do not re-identify `J_p` with an ordinary derivative by convention.

External source: Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), especially Section 3.4, Lemma 12, Proposition 16, Lemma 18, and the proof of Theorems 1–2.
