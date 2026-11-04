# D25 — original-216 middle-band second-digit carry and two-port compensation

2026-11-04 (+08). **AUTHOR-DERIVED / ALGEBRAICALLY-PROVED-IN-DECLARED-SCOPE / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is author-side portable mathematical evidence, not a native Source checkpoint or Result.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This result derives from the previous original-216 high Chebyshev–Hadamard observer and does not change that pin.

## Theorem: middle-band p-adic first jet

Let p=6r+1 be prime, p>=7, and a_k=(2k)!(3k)!/((k!)^5 216^k). Put k_s=2r+1+s for 0<=s<r. Each a_(k_s) has exact p-valuation 1. Define Y_s=a_(k_s)/p in Z_(p) and the p-unit

    gamma_p=Y_0=[(4r+2)! ((p+2)!/p)]/[((2r+1)!)^5 216^(2r+1)] in Z_(p)^*.

Let K_0=1 and for 0<=s<r-1 let

    K_(s+1)/K_s= 3(6s+7)(s+1)(3s+4) / [4(3s+5)^3] =: R0(s).

Let D_0=0 and D_(s+1)=D_s+d_s for 0<=s<r-1, where

    d_s= 2/(6s+7)+1/[3(s+1)]+1/(3s+4)-3/(3s+5).

All denominators are p-units on the stated ranges. Then

    Y_s = gamma_p K_s (1+p D_s) (mod p^2),  0<=s<r.         (MID-JET)

**Proof.** The exact factorial recurrence is

    a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3].

With k=2r+1+s and p=6r+1 this becomes the exact rational identity

    Y_(s+1)/Y_s =
      (1/2)(s+7/6+p/3)(s+1+p/3)(s+4/3+p/3)/
             (s+5/3+p/3)^3.

For s<r-1 each constant term in the four linear factors is a p-unit. The first-order product expansion modulo p^2 gives

    Y_(s+1)/Y_s = R0(s)[1+p d_s] (mod p^2).

Multiplication from s=0 proves (MID-JET). For k=2r+1,...,3r, 2k<p and p<=3k<2p, proving the exact valuation 1 and the gamma seed formula. QED.

## Source-preserving signed two-port interface

Define the middle contribution B_mid=sum_(s=0)^(r-1)(6k_s+1)a_(k_s). Since 6k_s+1=2p+5+6s, define

    A_p = sum_(s=0)^(r-1) (5+6s) K_s   in Z_(p)/p^2,
    E_p = sum_(s=0)^(r-1) [2K_s+(5+6s)K_s D_s] in F_p.

The theorem yields, modulo p^2,

    B_mid/p = gamma_p [A_p+p E_p].                         (MID-PORT)

For the target primes p mod 24 in {13,19}, keep the *separate* original 216 low band L_low=sum_(k=0)^(2r)(6k+1)a_k, the earlier original high band H_high=sum_(k=3r+1)^(4r)(6k+1)a_k, and the original quartic half sum V_half=sum_(k=0)^((p-1)/2)(8k+1)(4k)!/((k!)^4 2304^k).

The accepted frozen first-digit result and published Guo–Zudilin quartic-half theorem imply L_low−V_half belongs to p Z_(p); hence T_low=(L_low−V_half)/p is defined p-adically. With Hbar=H_high/p^2 mod p, the **exact source-typed scalar identity** is

    (W_216(p-1)-V_half)/p
      = T_low + gamma_p(A_p+p E_p) + p Hbar     (mod p^2),   (TWO-PORT)

and therefore W_216(p-1)=p (mod p^3) if and only if the right side vanishes mod p^2 for these classes. This is an equivalent obligation, not an all-prime proof of the required cancellation and not an independently verified D24 Delta_p-R_p bridge.

The prior high-band Chebyshev–Hadamard theorem supplies Hbar. The new information is the *separate* middle p-adic carry E_p, restoring a previously aggregated second-digit source. The remaining decisive observer is T_low mod p^2 and its relation to the two specified corrections. BRC reuse: typed integer coefficients, source band, p-valuation, signed weights and observer-before-quotient are preserved; no native X6 geometric inference is claimed.

## Actual finite exact check

Python standard-library integer modular arithmetic independently evaluated the original factorial coefficients, prime-free factorial units, quartic-half source, and the rational MID-JET kernel. **PASS** for every one of 148 primes p=6r+1, 7<=p<=2000, all 22,952 middle-band positions, p^2 coefficient comparisons, weighted MID-PORT comparisons; and 77 primes in the frozen target classes for the source-preserving TWO-PORT identity.

    p   gamma mod p^2   A mod p^2  E mod p  mid/p mod p^2   T_low mod p^2   Hbar mod p
    13        28            42       6         149               59          10
    19       337            86       6         254              297           9
   373     93197         11471     269      103721            75319         266

Each of these three rows has T_low+(mid/p)+p Hbar = 0 modulo p^2; this is finite evidence, not the general target proof. The script reproduces the quoted rows and checks.

## Next exact scientific action

Construct a low-band vs quartic-half p^2 transport/finite WZ identity giving T_low modulo p^2 and its first-order cancellation against gamma A; then combine gamma pE with the known high Chebyshev Hbar in a source/endpoint-accurate second-digit certificate. Test p=13,19,373 at each boundary before generalizing. Preserve the exact frozen D24 LIFT observer Delta_p-R_p until an exact bridge has been proved.

Native source status on the last checked service version: Gateway 0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and active jobs=5/5. No new native session, claim, authorized run, native checkpoint, Result, review, admission or 373 experiment is claimed. Old staging and the maintenance conversation remain untouched. Control support route: issue #1558; experiment support: issue #1559.
