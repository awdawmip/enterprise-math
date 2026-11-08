# D25 — Universal 2304 grade-two tail zero from the double truncation theorem

2026-11-08 Asia/Hong_Kong. **TASK_RESEARCH author-side: a fully sourced all-prime corollary PROVED, an explicit finite hypergeometric congruence PROVED by deduction, no native H0/B0 / UNREVIEWED / NOT_ADMITTED.**

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7, frozen input enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane chatgpt-research-onhour-enterprise-math-20260923; NOT the maintenance lane.

## New verified source input: BOTH published 2304 truncations, not just the full one

Guo and Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019) 329–358; https://arxiv.org/abs/1803.01830 (Theorem 1.1, ordinary limits of equations (5) and (6)), prove, for **every prime p>3**, both

S_V(p-1) = p*(-3/p) (mod p^3),
S_V((p-1)/2) = p*(-3/p) (mod p^3),

where S_V(m) is the truncated sum of the SAME original weighted-2304 terms
v_n = (8n+1)*binom(4n,2n)*binom(2n,n)^2/2304^n.

Thus, by direct subtraction of two already-proved published congruences,

SUM_{n=(p+1)/2}^{p-1} v_n = 0 (mod p^3).   (A)

We checked the actual primary source text: the abstract and its Theorem 1.1 explicitly establish both truncations. This second theorem was not yet consumed in the previous D25 216/2304 comparison, which conservatively left V's observed grade-two tail zero unproved.

## All-prime corollary: exact grade-two aggregate vanishes

For 0<=n<p, v_p(binomial coefficient of v_n excluding 8n+1)=floor(4n/p). Let N=(p+1)/2 and L=floor((3p-1)/4). For n>=L+1 in the tail in (A), floor(4n/p)>=3, hence each such term is zero modulo p^3. Consequently

SUM_{n=N}^{L} v_n = 0 (mod p^3).  (B)

The previous exact p-free factorial reduction, which did not assume any supercongruence, established for this grade-2 interval

v_n/p^2 = 2*(8n+1)*(4n-2p)!/(n!)^4/2304^n (mod p).

All denominators are p-units. Divide (B) by p^2 in the p-local integers, then reduce modulo p. We have proved the **unconditional all-prime theorem**

T_V(p) := 2 SUM_{n=N}^{L} (8n+1)*(4n-2p)!/(n!)^4/2304^n
         = 0 (mod p), for every prime p>3.   (C)

This uses the *existing published* V truncation theorem and an exact new source-graded reduction; it is not an independent proof of Guo–Zudilin.

## Explicit derived terminating hypergeometric identity

Set R=L-N=floor((p-3)/4), and use finite Pochhammer symbols in F_p. The algebraically proved ratio identity from the previous checkpoint gives

T_V(p) = 4/[N!^4 * 2304^N] *
         SUM_{r=0}^{R} (8r+5)*(3/4)_r*(1)_r*(5/4)_r /
          [(3/2)_r^3 * 9^r] (mod p).

The prefactor is a p-unit, so (C) proves the exact congruence

**SUM_{r=0}^{floor((p-3)/4)} (8r+5)*(3/4)_r*(1)_r*(5/4)_r /
 [(3/2)_r^3 9^r] = 0 (mod p), for EVERY prime p>3.**

All denominators are units in the declared finite range. This is an explicit, source-attributed congruence deduction from the two Guo–Zudilin truncations; its first statement in this project does not establish novelty over the wider literature.

## Why this matters for frozen 216 and BRC

The observed 301-prime V grade-two vanishing is now a **proved all-prime input**, rather than a conjecture. However the original weighted-216 grade-two aggregate remains nonzero in the 77 target primes tested, with exact examples 10 (p=13), 9 (p=19), 266 (p=373). The p=13 counterexample to a diagonal grade-output scalar transfer is therefore even sharper: V grade-2 output is identically zero for all primes, and W grade-2 output at p13 is demonstrably nonzero. Any actual W/V proof that uses these grade observables must account for cross-grade source redistribution; the full original W-to-V p^3 identity is NOT proven by the V tail theorem.

The typed carrier is: original index and binomial source; two separate truncations S_V(p-1) and S_V((p-1)/2); p-adic grade; signed (8n+1) factor; grade-two output; and the future full W/Delta-R observer. Using published S_V equality to collapse its entire high-index **aggregate** is legitimate only for the total-mod-p^3 observer. It does NOT license termwise cancellation or erasure of W's independent high-grade source, or any native H0/B0 simplification. This preserves BRC/source-provenance and P000 type boundaries.

Existing exact checker research_notes/portable_direct/d25_crossmodel_band_transport_check_20261108.py independently verified (C) in 301 primes p<=2000 and verified original finite sums in eight examples. Those finite checks are corroboration, not the proof of (C).

## Required continuation

The narrow question "does V's e=2 tail vanish for all p>3?" is now answered **YES** by a fully sourced proof. Do not repeatedly re-check it or claim it as an original author theorem.

Next portable exact action: construct a source-preserving Fricke/Cartier/finite-series W-to-V transformation that necessarily mixes original grade-two and lower-grade observables, or produce a concrete defect/counterexample for a proposed formula. The mother W_p≡p (mod p^3) for p≡13,19 (mod24) and original Delta-R remain OPEN.

Original same-class p=373 native H0/B0 divided-power benchmark under https://github.com/awdawmip/enterprise-math/issues/1559 remains PENDING_OWNER / NOT_EXECUTED: [X]U mod139129, true rank, semilinear F/eta, signed Green/Hesse kappa, Delta-R and independent exact implementation, followed by p=19. No substitute accepted.

Original Source target_request_id onhour11-20261106-1400-exact-research-lane-continuation was read only and unresolved: BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false. Site is CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; native session, CLAIM, run and checkpoint NOT_VERIFIED/NOT_WRITTEN. No native mutation or maintenance identity borrowed; prior contributions and staging remain separate. The required safe configuration is the independently authorized Site-bound backend client and credential, followed by a lawful benchmark executor. Existing schedule/notifications untouched.

**Status**: AUTHOR_SIDE_SOURCE_DERIVED_ALL_PRIME_THEOREM_PROVED / EXACT_301_PRIME_CROSSCHECK_CONSUMED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
