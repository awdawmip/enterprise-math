# D25 — Clausen signed cutoff: two-prefix scalar certificate

**Date:** 2026-11-05. **Status:** AUTHOR-SIDE EXACT SCOPED PROOF / FINITE INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE H0/B0 NOT_RUN.
**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen science pin:** c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical label chatgpt-research-onhour-enterprise-math-20260923, not the maintenance conversation.

## Exact theorem — rank-two running prefixes

Consume the already-published signed finite Clausen cutoff theorem (research_notes/portable_direct/20261105_onhour_d25_clausen_p3_convolution_boundary.md). For prime p=6n+1>=7 let

\[
 b_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2},\
 g=\sum_{k=0}^{p-1}b_k,\
 h=\sum_{k=0}^{p-1}(12k+1)b_k,
\]
\[
 W_p=\sum_{k=0}^{p-1}(6k+1)\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3},\
 W_p\equiv gh-B_p\pmod{p^3},\quad p^2\mid B_p.
\]

Define
\[
 C_p=\frac{(1/6)_{p-1}(1/3)_{p-1}}{p^2((p-1)!)^2}\pmod p,\quad
 R_1=1,\quad
 R_{r+1}=R_r\frac{18r^2}{(6r+5)(3r+2)}\pmod p.
\]
C_p is a nonzero unit, and denominators are p-units on the used index range. Retain the signed two-index contribution, but evaluate its designated scalar observer by
\[
 A_0=J_0=0,\quad A_i=A_{i-1}+2^iR_i,\quad J_i=J_{i-1}+i2^iR_i\quad (1\le i\le n).
\]
Then the **all-prime exact identity**
\[
 \boxed{\ T_p:=B_p/p^2
 =C_p\sum_{i=1}^n b_i\big[(6i+1)A_i-6J_i\big]\pmod p\ } \tag{1}
\]
follows by expanding the already-proved signed boundary
\[
 T_p=2C_p\sum_{1\le r\le i\le n}(6(i-r)+1)q_i2^{-(1+i-r)}R_r,\quad q_i=2^i b_i
\]
and using the **termwise** identity
\[
 \sum_{r=1}^i(6(i-r)+1)2^rR_r=(6i+1)A_i-6J_i.
\]
The R recurrence follows from the existing reverse quotient \(R_r=((r-1)!)^2/[(11/6)_{r-1}(5/3)_{r-1}]\). Every contributing ordered pair is preserved algebraically for this readout. No p-adic cancellation, sign, weight or valuation is discarded. Computing (1) takes O(n) field operations and O(1) streaming working memory; g,h,C_p take O(p) additional operations.

## Direct connection to the frozen second digit

For target primes p≡13,19 (mod 24), consume accepted CM0/UR first-digit facts p|g and gh≡p (mod p²). Define the genuine frozen scalar
\[
 \Delta_p=(gh-p)/p^2\bmod p.
\]
The original signed Clausen identity yields **exactly**
\[
 \boxed{\ \Delta_p-T_p=(W_p-p)/p^2\pmod p.\ } \tag{2}
\]
The source-frozen R_p is a separate observer; **this note does not silently define R_p:=T_p**. The remaining mother obligation is source-typed comparison Delta_p=R_p, or a uniform p-dependent terminating certificate for W_p=p mod p³ with the original interface. (1) reduces the explicit signed boundary work, not the unresolved mathematical equality.

## Executed exact verification

The accompanying standard-library checker streams 2F1 g,h and computes the original 216 3F2 W by a **separate** modular recurrence, then verifies (1) against (gh-W)/p² modulo p. All 611 primes 7<=p<=10000, p≡1 (mod6), pass. The original triangular double-sum is evaluated independently for the 25 primes <=250 and matches exactly. Of those 611, there are 312 target-class primes and all 312 numerically satisfy Delta_p=T_p; 611/611 also happen to satisfy W_p=p mod p³. These are **finite exact observations**, not full all-prime proofs.

| p | n | C_p | T_p | Delta_p if target |
|---:|---:|---:|---:|---:|
| 7 | 1 | 5 | 3 | n/a |
| 13 | 2 | 4 | 0 | 0 |
| 19 | 3 | 2 | 12 | 12 |
| 139 | 23 | 14 | 91 | 91 |
| 373 | 62 | 112 | 196 | 196 |

Script: research_notes/portable_direct/d25_terminal_boundary_rank2_checker_20261105.py. Run with standard Python 3 and no dependencies. This is not the p373 native H0/B0 crystalline test.

## BRC observer and continuation

Original carrier: ordered (i,r), signed weight 6(i-r)+1, original 216 and Clausen source, low-valuation i-layer and high-valuation (p-r)-layer. The pair of moments (A_i,J_i) is proved sufficient **only** for the fixed scalar B_p/p² readout and its displayed operations; it is not a lossless replacement for pair provenance, future weights, mod p⁴, or native Frobenius/kappa. Preserve the original formula for those operations. BRC reuse: COMPOSE_APPLIED (prior signed Clausen theorem and p-adic branch/valuation observer); no new general-purpose BRC family claim.

NEXT: read the exact frozen definition of R_p and source-typed compare to this T_p; seek a p-dependent terminal proof of the unclosed second digit. Existing issue #1559 is the distinct original-class p373 H0/B0 [X]U mod139129, rank, sigma-Frobenius, eta, kappa, signed branch observer, independent replica: NOT_RUN / UNASSIGNED. This scalar proof does not satisfy that native object.

Source continuation onhour11-20261105-1300-d25-cont: SUCCEEDED, observed 2026-11-05T05:02:27.824721+00:00, execution_authorized=false. No current own native CLAIM/open/run/Source checkpoint, no formal Result/admission; no other conversation's authority assumed.