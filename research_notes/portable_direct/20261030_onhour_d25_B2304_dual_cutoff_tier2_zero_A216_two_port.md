# D25 / SECOND-DIGIT-LIFT: dual-cutoff B2304 cancellation and an A216-only two-port certificate

Date: 2026-10-30, Asia/Hong_Kong.
Status: AUTHOR-SIDE / PROVED SOURCE-COMPOSED COROLLARY / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research logical-lane provenance: chatgpt-research-onhour-enterprise-math-20260923. No native session/CLAIM or maintenance identity is assumed.

## 1. Exact original streams and a previously unconsumed published input

For each prime p>3 retain the separate original signed sources

\[
a_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
b_n=\frac{\binom{2n}{n}^2\binom{4n}{2n}}{2304^n},
\]
\[
A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\qquad
B_p=\sum_{n=0}^{p-1}(8n+1)b_n.
\]

Guo–Zudilin, "A q-microscope for supercongruences", Advances in Mathematics 346 (2019), 329–358, https://arxiv.org/abs/1803.01830, proved TWO congruences on the original B2304 weighted series, for all p>3:

\[
\boxed{\sum_{n=0}^{(p-1)/2}(8n+1)b_n
\equiv \sum_{n=0}^{p-1}(8n+1)b_n
\equiv p\chi_p\pmod{p^3},\quad \chi_p=\left(\frac{-3}{p}\right).}\tag{GZ-dual}
\]

The full-cutoff theorem was imported in earlier D25 work; the additional HALF-cutoff theorem is consumed here for the first time. We do not claim to have reproved the published input.

## 2. All-prime B2304 valuation-two vanishing (PROVED COROLLARY)

For 0<=n<p, v_p(b_n)=floor(4n/p). Let B_p^(j) be the sum of the ORIGINAL (8n+1)b_n at exactly that unweighted valuation j.

The difference of the two GZ-dual cutoffs is B_p^(2)+B_p^(3). Every contribution to B_p^(3) lies in p^3 Z_(p). Subtraction therefore proves, for EVERY prime p>3,

\[
\boxed{B_p^{(2)}\equiv0\pmod{p^3}.}\tag{B2-ZERO}
\]

This is cancellation of the SIGNED TIER-TWO SUM, not each summand. At p=13, the normalized term residues for n=7,8,9 are respectively 7,0,6 modulo 13.

Compose B2-ZERO with the already PROVED first-jet reflection in research_notes/portable_direct/20261029_onhour_d25_A216_B2304_p4_tier2_first_jet.md (commit d4f60a540969e9ece570c0ad3b2ba0bc52e7d1b6). For r=p-1-n, the genuine original weighted term satisfies

\[
\frac{(8n+1)b_n}{p^2}\equiv
2(8r+7)2304^r\frac{(r!)^4}{(4r+3-p)!}\pmod p,
\quad \lfloor p/4\rfloor\le r\le(p-3)/2.
\]

Hence the following explicit FINITE-FIELD IDENTITY is proved for ALL p>3:

\[
\boxed{\sum_{r=\lfloor p/4\rfloor}^{(p-3)/2}
2(8r+7)2304^r\frac{(r!)^4}{(4r+3-p)!}\equiv0\pmod p.}\tag{B-reflected-zero}
\]

All denominator factorial indices are in [0,p-1], so they are p-units.

Precision boundary: B2-ZERO does NOT extend generally to p^4. The exactly calculated B_p^(2)/p^3 mod p equals 3 for p=13, 6 for p=19, and 234 for p=373. These are exact p^4 counterexamples to dropping this tier in the OPTIONAL stronger bridge.

## 3. Strict one-model reduction of the actual frozen LIFT (PROVED EQUIVALENCE)

Now take p=6m+1 with p modulo 24 in {13,19}; chi_p=1. Define the exact ORIGINAL A216 partial sums

\[
A_{\rm low}=\sum_{n=0}^{3m}(6n+1)a_n,\qquad
A_{\rm mid}=\sum_{n=3m+1}^{4m}(6n+1)a_n.
\]

They are exactly A_p^(0)+A_p^(1) and A_p^(2). The remaining A tier has valuation at least three.

The accepted D24 UR/JT0 first-digit theorem gives A_p≡p (mod p^2); therefore (A_low-p)/p^2 is p-locally integral. By the published GZ HALF-cutoff, B_low=B_p^(0)+B_p^(1)≡p (mod p^3). By newly proved B2-ZERO, B_p^(2)≡0 (mod p^3).

For the previous D25 source-preserving, integral carriers

\[
J_p=\frac{A_{\rm low}-2B_{\rm low}+p}{p^2},
\qquad Q_p=\frac{A_{\rm mid}-2B_p^{(2)}}{p^2},
\]

we now prove the stronger source-local statements

\[
\boxed{J_p\equiv\frac{A_{\rm low}-p}{p^2}\pmod p,\qquad
Q_p\equiv\frac{A_{\rm mid}}{p^2}\pmod p.}\tag{ONE-MODEL-PORTS}
\]

Reuse the prior already-proved A216 tier-two FIRST reflection (do not count its proof again):

\[
\frac{A_{\rm mid}}{p^2}
\equiv\sum_{r=2m}^{3m-1}(6r+5)216^r
\frac{(r!)^5}{(2r+1)!(3r+2-p)!}\pmod p.\tag{A2-reflection}
\]

The preceding exact D25 reduction proved LIFT iff J_p+Q_p=0 mod p. Therefore the precise currently outstanding SCIENTIFIC TARGET is equivalently

\[
\boxed{\text{LIFT}\iff
\frac{A_{\rm low}-p}{p^2}+
\sum_{r=2m}^{3m-1}(6r+5)216^r
\frac{(r!)^5}{(2r+1)!(3r+2-p)!}
\equiv0\pmod p.}\tag{LIFT-A-TWO-PORT}
\]

This eliminates the B2304 valuation-two computation and replaces its lower contribution by the proved half-cutoff value. It preserves both original A216 index windows and their signs. It is NOT YET a proof of the low/mid A216 cancellation and is not an H0/B0 experiment. In particular, the optional fourth p-adic digit is excluded from this frozen LIFT proof obligation.

## 4. Exact executable evidence, not a universal-proof substitute

Executable source: research_notes/portable_direct/d25_20261030_dual_cutoff_b2_guard.py.
Commit: 8e336fac57c9956add7b5798bc82d042bab8292e.
Verified Git blob: 0ca26f966dbeba7bbc2ced877c05e016a19be7c6.
Local SHA-256 of executed identical script: 9a934e12a238d81c546d02d765d3539fe1e9d5560f5be6bb8bcd00e287dffdf7.

Standard-library Python actually computed both original weighted factorial coefficient streams modulo p^4 for ALL 237 primes 5<=p<1500. Unit factorial blocks explicitly retain the k! from multiples kp. The independent reflected expression matched B2304 tier two TERM BY TERM. Both Guo–Zudilin truncations, B2-ZERO and the finite-field identity passed. The target D25 two A216 ports and reflected A tier-two matched for 60 primes in the two target residue classes. Separate exact original binomial-sum cross-check was run for p=5,7,11,13,19,31,373.

    TARGET 13 J 3 A2/p2 10 B2/p3 3 B3/p3 6
    TARGET 19 J 10 A2/p2 9 B2/p3 6 B3/p3 16
    TARGET 373 J 107 A2/p2 266 B2/p3 234 B3/p3 119
    PASS_B2304_DUAL_CUTOFF_TIER2_ALL_PRIMES 237 TARGET_CLASS_PRIMES 60 B2_NONZERO_MOD_P4 236
    PASS_REFLECTED_FINITE_FIELD_IDENTITY_AND_ORIGINAL_RAW_CROSSCHECK

The mathematical all-prime B2 result rests on GZ-dual and valuations; the executable is a FINITE regression. The all-target LIFT-A-TWO-PORT cancellation remains OPEN.

## 5. BRC and canonical continuation obligations

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED. Preserve the exact branch carrier (A/B, original integer n, coefficient p-valuation, signed weight, cutoff, p-unit denominators, source theorem). Observer: the signed p-adic residue modulo p^3 followed by valid division by p^2. B2 contraction is justified by the published dual-cutoff equality, not by positive-mass aggregation. The arithmetic observer is not the P000 native Heartbeat World X6 geometry.

Native support issue #1559 still calls for an authentic fixed-p373 original H0/B0 divided-power [X]U modulo 139129, module rank, semilinear Frobenius direction/normalization eta, odd signed Green/Hesse, kappa, and independent acceptance. This run DID NOT execute it or replace it with a scalar/Hesse surrogate. Current Gateway reports research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false; exact read-only continuation failed CONTROL_QUOTA. No own session/claim/run recovery was proved and no native Source checkpoint, Result, review or maintenance role is claimed. Current external mathematical write is an AUTHOR-SIDE portable repository note, not formal research-state admission. No task schedule or notification settings changed.

Next exact scientific action: prove or find a strict counterexample for LIFT-A-TWO-PORT uniformly for p≡13,19 mod24, attempting a finite WZ/CM/character certificate for the original A216 lower-window divided residue versus the m-term reflected middle window. Do not repeat B2, accepted UR, or the previously settled first carry. Native issue #1559 remains a separate, exact mandatory experiment requiring an authorized original-class evaluator.