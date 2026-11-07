# D25: restored frozen reflected R_p, streaming source observer, and complete second-digit comparison

Date: 2026-11-07 Asia/Hong_Kong. Role: TASK_RESEARCH author-side portable evidence; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical lane: chatgpt-research-hourly-enterprise-math-20260923. No claim of service session, runtime ownership, Researcher registration, native experiment, or independent review.

## Exact recovered frozen R_p

The previous D25 harmonic note left R_p as an uninstantiated frozen symbol. This run located its **independent original definition** (not inferred from Delta) at the task's frozen scientific pin:
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md, frozen blob SHA-1 c8c2423e8569a3da27b41bb7f602b4b781bb2a79, Section 3, equations (3)--(6);
- research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md, frozen blob SHA-1 3fedf7bef09b426037840721855f9a9d05558a0b.

For prime p=6m+1 with p mod 24 in {13,19}, write in Z_(p):

B_0=1,  B_(k+1)=B_k (6k+1)(3k+1)/(36(k+1)^2);
g=sum_(k=0)^(p-1) B_k;  h=sum_(k=0)^(p-1) (12k+1) B_k.
Delta_p=((g/p)h-1)/p mod p (integrality follows from pinned CM0 and accepted UR).
For 1<=r<=m, the frozen top-branch coefficient is
C_r=2^(r-1)((r-1)!)^2/[18 (5/6)_r (2/3)_r] in F_p.
The independently defined frozen target is
R_p=2 sum_(i=1)^m B_i sum_(r=1)^i (1+6(i-r)) C_r mod p.

No circular substitution R_p:=Delta_p is involved.

## Theorem A: exact one-pass reflected-tail reduction

Put b_i=binom(m,i)binom(2m,i)/2^i mod p, with b_0=1. These coincide with B_i mod p for 0<=i<=m by the pinned low-band coefficient identity.

Then C_1=1/10 and
C_(r+1) = C_r * 36r^2/[(6r+5)(3r+2)] mod p, 1<=r<m.
Define S_i=sum_(r=1)^i C_r and J_i=sum_(r=1)^i r C_r, both modulo p. Then

  R_p = 2 sum_(i=1)^m b_i[(1+6i)S_i - 6J_i] mod p.

Proof: take the ratio of the exact rising-factor expression for C_(r+1)/C_r:
2 r^2 /[(r+5/6)(r+2/3)] = 36r^2/[(6r+5)(3r+2)].
The initial C_1 = 1/[18*(5/6)*(2/3)]=1/10. Expand the inner frozen sum:
sum_(r=1)^i (1+6(i-r)) C_r=(1+6i)S_i-6J_i.
Finally the p-unit b_i recurrence is
b_i=b_(i-1)(m-i+1)(2m-i+1)/(2i^2).
All denominators are nonzero mod p for 1<=r,i<=m: 6r+5<=6m-1=p-2, 3r+2<=3m-1<p, 2i<p, and p>=13. This is an exact finite-field identity for every eligible p, not an empirically inferred equality.

Algorithmic cost: one O(m)-step finite-field streaming pass, with O(1) working carrier (b,C,S,J,R), instead of evaluating the original O(m^2) indexed pair sum; modular inversion/bit complexity is not asserted constant. Source identity (i,r), weights and high-tail provenance remain in the derivation even though a proven linear projection computes this particular R observer.

## Theorem B: complete source-resolved LIFT residual

The pinned finite Clausen identity states **exactly** W_p=gh-T_p, where
W_p=sum_(k=0)^(p-1) (6k+1) (1/2)_k(1/3)_k(2/3)_k/[2^k (k!)^3],
and the pinned reflected-tail theorem states T_p = p^2 R_p mod p^3.
Therefore in the target classes, with accepted first digit, the equivalence is
  Delta_p-R_p = (W_p-p)/p^2 (mod p).
The quotient is integral on the accepted first-digit scope. The weighted W_p coefficients have their independent recurrence
a_0=1, a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3].
The D25 harmonic-source expression from the previous note is now a **fully computable, independent-R** certificate:
  E_p=(X H0-1)/p+X J+Y H0
      -2 sum_(i=1)^m b_i[(1+6i)S_i-6J_i] (mod p).
The frozen parent equivalence and this stream reduction are proved under the pinned interface. Whether E_p vanishes for every target prime is still an OPEN arithmetic theorem (the weighted W_p supercongruence).

## Executed exact integer certificates

Companion script: research_notes/portable_direct/d25_frozen_Rp_restoration_20261107.py.
All 166 primes p<5000 with p mod24=13 or 19 were checked by integer modular B-recurrence mod p^3, independent binomial/C streaming R mod p, and separately evaluated weighted cubic W mod p^3. For each: direct Delta=R, E_p=0, and E_p=(W_p-p)/p^2 modulo p. On p<=109 an additional independent O(m^2) original tail was checked termwise, as was the direct factorial/rising-factor C_r formula. The preceding D25 independent harmonic checker was re-run for all 166 and its Delta agreed with the present integer recurrence.

Selected records (p : Delta, R_p, E_p):
13 : 0,0,0; 19 : 12,12,0; 37 : 11,11,0;
43 : 15,15,0; 109 : 50,50,0; 157 : 82,82,0;
373 : 196,196,0; 1093 : 267,267,0.
No finite range establishes universal vanishing. The exact general results here are the R stream identity and the inherited/source-instantiated equivalence; the 166 zeros are reproducible finite observations.

## BRC interface / observer audit

Carrier: labelled rational B_k, valuation bands k<=m, m<k<=2m, k>2m; reflected high-tail C_r labelled r and low-band b_i labelled i. Independent observed ports: Delta via quotient-first p^3 G*h and R via high-tail reflection. Future operation: LIFT E and W finite weighted sum. Theorem A is a certified observer-specific projection that retains the exact pairing law; it is not evidence of universal source identity recovery from scalar totals. Existing BRC finite coefficient and source-preservation results: COMPOSE_APPLIED (no new Foundation or tool-family claim).

## Immediate next frontier / recovery

Mathematics: prove or disprove the genuinely uniform weighted finite supercongruence W_p=p (mod p^3), using the now direct streaming R and harmonic Delta formulas; a precise candidate next step is a telescoping identity pairing the two source recurrences or a p-adic Frobenius/finite WZ certificate with cutoff preserved. Do not repeat the previously solved question "where is R_p?" or treat these finite tests as proof. Freeze CM0/UR and first-digit parent.

Control: em_status and both original request receipt reads still fail at preflight BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site phase CONFIGURED_NOT_LIVE_VERIFIED, backend_connected=false, research_authority_granted=false. Original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 and protected staging remain UNKNOWN. Support path awdawmip/enterprise-math#1558 (dedicated Site client and reviewed backend pin 0.6.11). No session change, claim, open, native checkpoint, freeze, independent review, or own activity registration; activity REGISTER_PENDING. Author-side evidence only. Official source-owned frontier requires successful authenticated recovery/status, current exact continuation, winning claim/open, then native checkpoint readback.
