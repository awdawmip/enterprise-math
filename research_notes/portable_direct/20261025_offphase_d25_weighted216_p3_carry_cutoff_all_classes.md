# D25/LIFT — exact 216-series carry valuation ports and p^3 cutoff

2026-10-25. Portable TASK_RESEARCH author derivation and exact finite checking. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NONBLIND / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**. No native Source progress, new owner, reviewer or canonical acceptance claimed.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Historically relevant Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; **frozen scientific Source** c47e13e4aba0e006366f989d6334d443f6333ae3. Prior Clausen-cutoff/Rp bridge: research_notes/portable_direct/20261025_offphase_d25_frozen_Rp_cutoff_identification_all_6m_plus_1.md. Existing proofs are consumed, not re-claimed.

## Proven, all primes p>3: integer carry/valuation and sharp truncation

For integer 0<=k<p, let

\[
d_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},
\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)d_k.
\]

Then the following **exact p-adic valuation identity** holds:

\[
\boxed{v_p(d_k)=\left\lfloor\frac{2k}{p}\right\rfloor+
\left\lfloor\frac{3k}{p}\right\rfloor.}\tag{1}
\]

Proof: k<p and 3k<p²; hence by Legendre's exact factorial formula, v_p(C(2k,k))=floor(2k/p) and v_p(C(3k,k))=floor(3k/p)-floor(2k/p). The denominator 216^k is a p-unit. Adding valuations proves (1), for every p>3.

This is a four-port exact filtration, with valuations 0,1,2,3 on successive k intervals
[0,ceil(p/3)), [ceil(p/3),ceil(p/2)),
[ceil(p/2),ceil(2p/3)),
[ceil(2p/3),p).
The extra weight v_p(6k+1) is nonzero at exactly one k in [0,p): k=(p-1)/6 for p=1 mod6; k=(5p-1)/6 for p=5 mod6. It is 1 there, except p=5,k=4 where it is 2. This distinct signed weight port is retained, not erased.

It follows **for all p>3, unconditionally** that with N_p=floor((2p-1)/3),

\[
\boxed{W_p\equiv
\sum_{k=0}^{N_p}(6k+1)
\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k}
\pmod{p^3}.}\tag{2}
\]

The terms above N_p have valuation at least 3. For p=6m+1, N_p=4m; for p=6m+5, N_p=4m+3. This truncation is a proof, not a conjectured congruence to a closed-form answer.

## Exact finite evidence; all-prime supercongruence NOT established

The companion checker (standard library, original hypergeometric recurrence plus independent factorial-binomial reconstruction) tested **all 667 primes 5<=p<5000**. It found

\[
W_p\equiv p\left(\frac{-3}{p}\right)\pmod{p^3}
\]

**for each tested p only**. The 330 cases p=1 mod6 reproduce existing author-side target evidence; the additional 337 cases p=5 mod6 are the new finite complementary coverage and give -p mod p³. For all 667, full and theorem-truncated sums match. The 44 primes p<200 are independently recalculated using integer binomial coefficients rather than the recurrence. The exact recurrence is

\[
d_{k+1}/d_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3).
\]

The factor **36** is essential (not 18); all inverted factors are p-units for k<p-1. Samples (p,N_p,W_p mod p³): (5,3,120), (7,4,7), (11,7,1320), (13,8,13), (19,12,19), (31,20,31). Neither enumeration nor this p-adic cutoff proof establishes the unbounded congruence.

The frozen target still requires, for **all p≡13,19 mod24**, the weighted Sun A14(ii) second-digit step W_p≡p mod p³, which the earlier Clausen-Rp theorem reduces LIFT to under accepted UR. The other residue classes were tested only to clarify the sign/provenance port; they do not change the mother Task or close the native CM/DP correspondence.

## BRC and recovery boundaries

BRC: COMPOSE_APPLIED to the integer binomial-carry/valuation carrier; the independent k-index, weight anomaly and order-mod-p³ observation are preserved. Removing the final band is proved safe only for this scalar sum at this precision, not arbitrary future operations, higher precision or native X6 physics. No custom axiom or native formal proof asserted.

Do not repeat prior accepted UR mathematics, WZ seams, frozen Rp identification, previous 330 target-prime tests, another stream's inert self-Green no-go or Research1 J1/J2 work. The UR V2 94,687-byte four-file historical bundle with required SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 is still unverified; bounded GitHub and Drive-manifest searches found no identical hash, not proof of nonexistence. Only missing writer/provenance remains authorized for that prior UR work; do not regenerate the old proof.

This conversation has no executable typed recovery_status tool, though em_status describes it; checkpoint_list returned ACCESS_DENIED. Sites gateway reports static_machine_readonly/write_relay_enabled=false/research_authority_granted=false. No own authenticated session/claim/run, original target_request_id or current winning claim was available. No dispatch, identity borrowing, retry of a refused mutation or native source write was performed. This note is portable GitHub evidence, **not** a canonical Source checkpoint or predecessor completed research. If Source returns CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, exact readback is required and frontier_notes.completed_units=[].

Next research action: prove or refute the original target-class all-prime W_p=p mod p³ by an independent WZ/CM argument without duplicating prior Jacobi or Clausen work. Next Source action when properly authorized: recover own real request IDs/receipts, reconcile uncertain effects, read exact continuation and winning claim, and publish/checkpoint this already derived unit with source-backed provenance, not an invented claim.
