# D25 / SECOND-DIGIT-LIFT — proven 2304 prior art reduces original second-digit proof to minimal p³ bridge

At: 2026-10-30 Asia/Hong_Kong. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923; not maintenance lane chatgpt-hourly-enterprise-math-20260921.
Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains frozen.
Classification: AUTHOR-SIDE / EXTERNAL PROVED THEOREM CONSUMED / EXACT CONDITIONAL REDUCTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

## Precise previously proved input

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, **Advances in Mathematics 346 (2019), 329–358**, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830 (updated 2019-02-13). The paper's stated theorem at truncation p−1 proves for **every prime p>3**:

\[
 B_p=\sum_{n=0}^{p-1}(8n+1)\frac{\binom{4n}{2n}\binom{2n}{n}^{2}}{2304^n}
 \equiv p\chi_p\pmod {p^3},\quad \chi_p=\left(\frac{-3}{p}\right).
 \tag{B_GZ}
\]

Primary citable source: https://arxiv.org/abs/1803.01830 ; publisher DOI https://doi.org/10.1016/j.aim.2019.02.008 . In the paper, denominator 2^(8n)3^(2n) equals 2304^n **exactly**, numerator and weight match B_p, and the proved truncation is p−1 (it also separately gives the half truncation). This proof is **credited to Guo–Zudilin, not to the current author**. The research source from 2026-10-30 on the p^5 sharpness of A216/B2304 already defined the bridge D_p, but did not use the 2019 published B theorem as a formal all-prime input.

## Source-faithful exact reduction of the unfinished original LIFT

Retain the other unchanged original weighted model

\[
 A_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},
\]
and its existing signed bridge
\[
 D_p=A_p-2B_p+p\chi_p.
\]

From (B_GZ), for **every prime p>3**, directly:

\[
 \boxed{D_p\equiv A_p-p\chi_p\pmod {p^3}.}\tag{1}
\]

In the frozen target classes p≡13,19 (mod24), \(\chi_p=+1\), so

\[
 \boxed{A_p\equiv p\pmod {p^3}\ \Longleftrightarrow\
 D_p\equiv0\pmod {p^3}.}\tag{2}
\]

This is an unconditional *equivalence derived from an existing proved external theorem*, not an unconditional proof that D_p vanishes. Previous accepted D24 first digit gives A_p≡p (mod p²) on those target classes; (B_GZ) then gives p²|D_p. The earlier exact original Clausen port alignment proved \((A_p-p)/p²≡\Delta_p-R_p\pmod p\) for target primes. Consequently:

\[
 \boxed{\frac{D_p}{p^2}\equiv\Delta_p-R_p\pmod p.}\tag{3}
\]

All quotients here are taken in Z_(p) before reduction. Equations (1)–(3) preserve the exact original model labels, signs, p-local observer, and source provenance. Equation (3) makes the **minimal proof target** a mod-p³ bridge, rather than the *stronger* p⁴ bridge empirically observed in earlier author-side 667-prime computations. The p⁴ bridge and its p⁵ counterexamples are distinct statements: finite evidence for p⁴ cannot be promoted to an all-prime theorem and is not a mandatory condition to prove LIFT.

The earlier author's p⁵ bridge/source-carry artifact (immutable reference):
https://github.com/awdawmip/enterprise-math/blob/5d5b1d8b07ccc807c71e7d8c11f2a2f65edb8aec/research_notes/portable_direct/20261030_onhour_d25_original_A216_B2304_p5_sharpness_source_carry.md .
The earlier original \(\Delta-R\)/Clausen equivalence:
https://github.com/awdawmip/enterprise-math/blob/2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be/research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md .

## BRC provenance/observer and next precise action

BRC resolution: COMPOSE_APPLIED. Keep ordered index n, two *distinct* 216 and 2304 model origins, signed weights 6n+1 and 8n+1, exactly invertible p-local denominators, quadratic character \(\chi_p\), and target observer \(\Delta_p-R_p\) modulo p. The allowed source-typed operation is signed difference \(D=A-2B+p\chi\); the external B theorem is a proved theorem dependency with its own attribution and domain, not an identification of individual n-term coefficients or a positive-mass BRC collapse.

**Next smallest scientific unit:** prove or refute the *original exact* bridge \(A_p-2B_p+p\chi_p\equiv0\pmod{p^3}\) uniformly for both frozen residue classes, using a finite hypergeometric transformation with p-adic remainder or a coupled source-preserving certificate. Reuse the existing higher-resolution 667-prime bridge checks as test data, but do not make their stronger p⁴ hypothesis an unjustified proof premise. In parallel, the unchanged original fixed-p373 **native** H0/B0 divided-power Frobenius/Green/Hesse/κ experiment must be executed by an authorized native owner under issue https://github.com/awdawmip/enterprise-math/issues/1559 .

This note is **external theorem consumption and exact algebraic reduction**, no new all-prime proof of the bridge and no H0/B0 execution. GitHub author-side persistence does not grant canonical Source role, checkpoint, Result, independent review or admission. 2026-10-30 06:02 UTC the Site reported research_authority_granted=false and write_relay_enabled=false; own checkpoint list read ACCESS_DENIED. Own-lane formal continuation awaits lawful recovery/authorization, with original request receipts reconciled before any dispatch; no maintenance session/claim borrowed.
