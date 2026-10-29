# D25 LIFT: uniform first carry from accepted inputs; a single mod-p residue remains

Date: 2026-10-30 Asia/Hong_Kong.
Status: AUTHOR-SIDE / PROVED SOURCE-COMPOSED REDUCTION / EXECUTED FINITE REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923 (distinct from control maintenance).

## Original weighted carriers and admitted inputs

Let p be a prime congruent to 13 or 19 mod 24. Work in the p-local rational ring, with the exact n=0,...,p-1 cutoff:

a_n = binom(2n,n)^2 binom(3n,n)/216^n,
b_n = binom(2n,n)^2 binom(4n,2n)/2304^n,
A_p = sum (6n+1)a_n, B_p = sum (8n+1)b_n.

The *unweighted* coefficient valuations are v_p(a_n)=floor(2n/p)+floor(3n/p), v_p(b_n)=floor(4n/p). Let A_p^(j),B_p^(j) denote signed sums over coefficient valuation j, for j=0,1,2,3, keeping original n and weight. Set

C_0 = A_p^(0)-2B_p^(0)+p,
C_j = A_p^(j)-2B_p^(j) (j=1,2,3).

These add EXACTLY to A_p-2B_p+p. Valuations give C_j in p^j Z_(p) for j>=1. No unsigned mass or surrogate model is introduced.

Two existing theorems are imported, not reproved:

* ACCEPTED D24 supersingular UR/JT0 first digit (RR-AC9B3BA5BD277CE043F5, reviewed DR-610CB297F3195E8F2D9E): A_p congruent p mod p^2 for every target prime. Source: research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY/MCP-e6cc623799404ca09be0012f8654712c/0f0be0d17d5eb48c835b/d24_ur_jt0_result_20260924.md (Git blob de2466e9f6484090a8cf6b1242c7180209e89927).
* Guo–Zudilin, A q-microscope for supercongruences, Advances in Mathematics 346 (2019) 329–358, Theorem 1.1: original weighted 2304 sum B_p congruent p*(-3/p) mod p^3 for p>3; here (-3/p)=1, so B_p congruent p mod p^3. Primary reference https://arxiv.org/abs/1803.01830 . This theorem concerns B2304, NOT the original A216 target.

## Theorem 1 (PROVED all target primes): first carry is already discharged

C_0+C_1 congruent 0 mod p^2.

Proof: exact partition gives C_0+C_1=(A_p-2B_p+p)-(C_2+C_3). The first bracket is p-2p+p=0 mod p^2 by the two imported theorems; the second belongs to p^2 Z_(p). Consequently C_0+C_1 belongs to p^2 Z_(p). In particular, C_0 belongs to p Z_(p) and the first carry (C_0/p+C_1/p) mod p is zero. Individual C_0/p, C_1/p need not vanish: at p=13 their residues are 11 and 2.

This corrects the preceding author note 20261029_onhour_d25_original_signed_tier01_three_carry.md, which left all-prime Carry1 as an open finite-WZ/CM obligation. It was already a consequence of accepted UR plus the published B theorem. Nothing here reclaims those inputs as an original theorem.

## Theorem 2 (exact strict reduction): only one mod-p obstruction remains

Define the *now proven integral* quotients in Z_(p):

J_p := (C_0+C_1)/p^2,    Q_p := C_2/p^2.

Since C_3 belongs to p^3 Z_(p), the original sources satisfy

A_p-2B_p+p congruent p^2(J_p+Q_p) mod p^3.

By B_p congruent p mod p^3 and A_p congruent p mod p^2, we have the justified divided congruence

(A_p-p)/p^2 congruent J_p+Q_p mod p.   (∗)

Now use the existing frozen finite Clausen cutoff bridge, not a newly invented operator: s_n=(1/6)_n(1/3)_n/(2^n(n!)^2), g=sum_{n<p}s_n, h=sum_{n<p}(12n+1)s_n, G_p=g/p, and its separately proved cutoff-reflection scalar R_p (different from the theta tail Theta_p). The accepted input gives p|g and

A_p congruent gh-p^2 R_p mod p^3.

Dividing the already proven cutoff identity (A_p-p)=p(G_p*h-1)-p^2*R_p by p^2 (integrality from accepted UR) gives the **EXACT SAME-OBSERVER DEFECT IDENTITY**

  Delta_p - R_p = (G_p*h-1)/p - R_p
                congruent (A_p-p)/p^2
                congruent J_p+Q_p  (mod p).    (DEFECT-ID)

It follows, preserving the actual signed p-adic defect rather than merely its zero set, that

  LIFT: Delta_p congruent R_p mod p
  iff A_p congruent p mod p^3
  iff J_p+Q_p congruent 0 mod p.   (LIFT-ONE-DIGIT)

Thus the frozen D25 goal reduces to precisely ONE original signed, source-labeled mod-p cancellation. This is a *strict* reduction: the first carry is proved, C_3/third carry is irrelevant to frozen LIFT (only to the optional stronger p^4 conjecture), and the observer needs only C_0+C_1 and C_2 mod p^3. There is NO universal proof yet of the remaining J_p+Q_p=0 mod p.

## Executed exact evidence, distinct from a proof

A standard-library exact modular script tested all 166 target-class primes p<5000 (83 of each class) on both original recurrences; direct integer binomial recomputation independently cross-checks p=13,19,373. All source/valuation, imported-congruence regression and bridge-equivalence assertions passed; all 166 samples also have J+Q=0 modp. This is a finite falsification scan only.

p=13: J mod p^2=94, Q mod p^2=166; modp ports 3+10=13.
p=19: J=238, Q=294; modp ports 10+9=19.
p=373: J=90746, Q=33463; modp ports 107+266=373.

Validator: research_notes/portable_direct/d25_lift_low_tier_strict_reduction_guard_20261030.py . Its p^4 internal arithmetic is solely for comparison with the predecessor's three-carry evidence; the new theorem needs no fourth digit.

## BRC, boundaries, continuation

BRC reuse: COMPOSE_APPLIED. The carrier retains (A/B source, exact original n, unweighted valuation tier, original signed observer, cutoff, p-local order, theorem provenance). Operation order: preserve signed streams -> import UR and B2304 to PROVE first divisibility -> form J as a legitimate integral quotient -> combine J with Q -> compare to the SAME frozen Delta_p-R_p through the already proved cutoff R_p. Nonzero low-tier residuals are retained until their certified joint cancellation; R_p is not substituted by the distinct Theta_p. This scalar reduction is NOT a claim about physical/native X6, H0/B0 or its native Frobenius.

Next smallest SCIENTIFIC ACTION: prove or refute uniformly J_p=-Q_p mod p for p in the two target classes using exact finite WZ/CM/character-source evaluation at the ORIGINAL signed model and proven valuation-two reflection; do not redo the settled first carry, CM0, UR, factorial tails, or optional fourth-digit Carry3.

Native scientific #1559: as read 2026-10-30, OPEN with no assigned evaluator. The original same-class p373 H0/B0 divided-power [X]U mod139129, actual module rank, real semilinear Frobenius and eta, odd signed Green/Hesse, kappa and Delta-R plus independent acceptance remain PENDING_OWNER / NOT_EXECUTED. Scalar portable mathematics does not satisfy this benchmark.

Site authority snapshot at 2026-10-30: research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false; em_checkpoint_list returned ACCESS_DENIED. Own Source session/claim/run/request/recovery state is UNKNOWN, not an empty queue; on a future lawful real Research-lane continuation first reconcile actual old request IDs and Source owner before dispatch or claim. No Source checkpoint, Result, native experiment, review, maintenance role or scheduler mutation is claimed here.
