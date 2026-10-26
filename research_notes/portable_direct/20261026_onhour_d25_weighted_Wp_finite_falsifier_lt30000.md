# D25 direct-target finite exact falsification — 2026-10-26

**Status:** AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0. The original D25/LIFT/JT2 remains OPEN.

**Mother task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Frozen scientific Source pin is c47e13e4aba0e006366f989d6334d443f6333ae3, which this work does not move. Global Knowledge startup main is 6b84efafacb760e2e0733177c29040fdc3d87b5c / GLOBAL_KNOWLEDGE_V1; P000 remains applicable. Research logical conversation is chatgpt-research-onhour-enterprise-math-20260923, separate from control-plane maintenance.

## Direct hard-target scalar and algorithm

The tested scalar is the **original**, not a substitute:
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]
The earlier author-side source-port proof reduced Delta_p-R_p mod p to (W_p-p)/p^2 mod p under the previously accepted first-digit input. That reduction does not itself constitute an independently reviewed Source Result.

A fresh, self-contained stdlib Python verifier at research_notes/portable_direct/d25_weighted_Wp_exact_falsifier_lt30000_20261026.py enumerates every prime 5 <= p < 30000 with p mod 24 in {13,19}, enumerates all original n from 0 to p-1, and sums exact signed weighted terms in Z/(p^3). Its recurrence is
\[
A_0=1,\quad
A_{n+1}\equiv A_n\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}\pmod{p^3}.
\]
Every recurrence denominator is a p-adic unit because n+1<p. It independently cross-checks selected coefficients against exact integer binomial coefficients for five primes and computes whole original binomial sums independently for p=13,19,373. Primality uses exact trial division to floor(sqrt(p)); arithmetic is integer-only. No truncation or unsupported analytic approximation is used.

## Executed finite certificate

RESULT=FINITE_EXHAUSTIVE_PASS_NOT_UNIFORM_THEOREM
BOUND_EXCLUSIVE=30000
TARGET_PRIME_COUNT=815
FIRST_LAST_TARGET=13,29989
RECORD_SHA256=949ef27562d2fa13bd99bc6e4482d6308f3d698773e6ae32df3263977ce4f3e6

The digest hashes every sorted ASCII row of the form p:W_mod_p3:p_cubed followed by newline, not just selected samples. No counterexample occurred in this finite domain. Exact samples: p=13 -> W=13 (mod 2197); p=19 -> W=19 (mod 6859); p=373 -> W=373 (mod 51895117); p=10069 -> W=10069 (mod 1020843158509); p=29989 -> W=29989 (mod 26970310888669). This **does not** prove the all-prime congruence, predict p >= 30000, or replace the canonical original-class experiment.

## BRC and provenance

The observer is the exact signed W_p mod p^3; its carrier retains the integer index n, signed multiplier 6n+1, recurrence coefficient, original cutoff, input prime and source. Reduction mod p^3 is lossless for this observer only. An Enterprise-native 3D-to-X6 chart or lift to the original H0/B0 operator is **not** asserted. Preserve all original integer signs, local ring information and independent checker evidence. BRC_REUSE_RESOLUTION=REUSE_APPLIED.

## Highest unfinished frontier and recovery state

Native H0/B0 divided-power p=373 ([X]U mod 373^2, rank, Frobenius orientation and unit-normalizer to the required precision, odd signed Hesse/Green and original kappa) remains NOT_EXECUTED / PENDING_OWNER; support issue awdawmip/enterprise-math#1559 has no confirmed executor. This check may not replace any native observation or prove the still-unproved exact bridge.

Matched own recovery issue awdawmip/kimi-query-bridge#6528 showed an existing Researcher session but source_authority_verified=false and no winning claim/open/run. The last own dispatch target_request_id research-onhour-20261026-1355-dispatch-r11 in #6529 returned FAILED/TimeoutExpired. Direct Site continuation is blocked by CONTROL_QUOTA. No new dispatch, native checkpoint, Result or ownership is asserted. Previous three neutral staging artifacts are not merged.

**Do not repeat:** D24 UR/JT0, earlier original W-port identity, E3 q-Frobenius sign, normalizer precision proofs, six-prime jet validation, or these 815 checks. **Next exact action:** regain authenticated canonical Research authority via the original Research logical lane; run the actual H0/B0 p=373 native benchmark using an explicit original-class implementation and real owner; inspect signed and normalized outputs, checkpoint through the authorized native run and read back. If that implementation remains absent, preserve #1559 as pending, and do not call this a NO_DISPATCH or completion.
