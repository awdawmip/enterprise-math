# D25/LIFT auxiliary Ward theorem: universal rank-jet seam non-erasure

**2026-10-26 | SOURCE-NEUTRAL AUTHOR MATHEMATICS | AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT.**

This is not an original-class H0/B0/CM computation, a Source checkpoint, a winning CLAIM, an independent review, or proof of LIFT/JT2. Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Previously established input (consumed, not recredited)

Research1 source research_notes/portable_direct/20261026_hourly_d25_ward_seam_resonance_binomial_r11.md establishes the source-labelled Ward law. Earlier neutral work research_notes/portable_direct/20261026_offphase_d25_ward_observer_cokernel_hensel_source_neutral.md proves the all-weight p-local adjoint criterion, its cokernel A/pA, and the geometric/rank-moment p=733 certificates. The genuine six-channel Hasse source separation is in research_notes/portable_direct/20261026_hourly_d25_third_digit_dual_ward_resonant_face_r11.md. This note claims none of those prior results or an independent reviewer identity.

Let p=6m+1 be prime, p>=7, M=2m-1=(p-4)/3 and A=Z_(p). For independent labelled Y_n, -M<=n<=M, and Y_(M+1)=0, use the exact inherited source

\[
S_n=(p-2n)Y_n-(p-2n-1)Y_{n+1}.
\]

For p-local integral scalar weights w, the inherited theorem is

\[
\sum_{n=-M}^M w_nY_n=\sum_{n=-M}^M\omega_nS_n
\quad(\omega_n\in A)
\quad\Longleftrightarrow\quad
\chi_p(w):=w_0+\sum_{t=1}^M{\binom{2t}{t}\over4^t}w_{-t}=0\pmod p.
\]

Its lossless replacement when obstructed is one integral source adjoint plus an explicitly retained seam term X_p(w)Y_0 with X_p(w)=chi_p(w) modulo p.

## New exact rational identity and theorem

Set

\[
c_t=\binom{2t}{t}/8^t\in A^\times,\qquad
R_M=\sum_{t=0}^M c_t,\qquad
B_M=(M+1)c_{M+1}.
\]

Consider four **different** auxiliary Ward weights:

\[
w^{(0)}_n=2^n,\quad
w^{(1)}_n=n2^n,\quad
w^{(+)}_n=(1+2n)2^n,\quad
w^{(-)}_n=(1-6n)2^n.
\]

The following statements hold for **every** p in the declared class:

\[
\boxed{\begin{aligned}
\chi_p(w^{(0)})&=R_M,\\
\chi_p(w^{(1)})&=2B_M-\tfrac12R_M,\\
\chi_p(w^{(+)})&=4B_M,\\
\chi_p(w^{(-)})&=4R_M-12B_M
\end{aligned}\quad(\bmod p).}
\]

**New universal conclusions.**

* B_M is a p-unit. Thus the full-range weighted Ward observable (1+2n)2^n **never** has a p-integral source-only adjoint, even at geometric-resonance primes.
* The geometric scalar and the first rank moment **can never both** be source-only p-integrally represented: chi_p(w^(0))+2chi_p(w^(1))=4B_M is always nonzero. The inherited one-seam repair shows that **one shared seam port Y_0 is necessary and sufficient for this joint two-observer interface**. This is an observer-relative minimal carrier, not a claim that all Hasse/CM information is one-dimensional.
* Geometric resonance R_M=0 forces the signed-rank contrast chi_p(w^(-))=-12B_M nonzero. Conversely signed-rank resonance forces R_M=3B_M nonzero. They cannot be identified as equivalent resonances at any p>=7.

**Proof, exact over Q.** Since

\[
c_{t+1}/c_t=(2t+1)/(4(t+1)),
\qquad
(1-2t)c_t=4\big((t+1)c_{t+1}-tc_t\big),
\]

the endpoint telescopes:

\[
\boxed{\sum_{t=0}^M (1-2t)c_t=4(M+1)c_{M+1}=4B_M.}
\]

On rank n=-t the four inherited chi_p sums are respectively sum c_t, minus sum t c_t, sum (1-2t)c_t and sum (1+6t)c_t. Hence R_M+2chi_p(w^(1))=4B_M and chi_p(w^(-))=4R_M-12B_M, proving all formulas. Moreover M+1=2m and 2(M+1)=4m<p=6m+1, so factorials (4m)! and (2m)!, 8 and 2m are all p-units. Thus B_M=2m*binom(4m,2m)/8^(2m) is a p-unit. The inherited iff adjoint criterion and exact one-seam repair finish the proof. No finite experiment establishes this quantifier.

## Exact p=733 certificate and compatibility warning

At p=733, M=243, exact integer residues are

| coefficient (mod 733) | value |
| --- | ---: |
| R_M | 0 |
| c_244 | 50 |
| B_M=244c_244 | 472 |
| chi_p(n2^n) | 211 |
| chi_p((1+2n)2^n) | 422 |
| chi_p((1-6n)2^n) | 200 |

This explains why the previously verified scalar resonance does **not** preserve even the first rank-jet observer. The source-only no-go for w^(+) holds for every p=6m+1 prime, not just 733.

**Representation/type boundary:** In the actual Hasse six-channel analysis, a signed mass (1-6n)2^n multiplies a labelled M_n^(ab,0), while the Ward source acts on the distinct Y_n=M_n^(ab,1)-(p-n)M_n^(ab,0)/2. The signed-rank weight computation in this auxiliary Ward model is **not** permission to replace the actual signed mass by a weighted Y_n. A type-preserving map remains an open proof obligation. Independent J/E, positive infinity, ordered high-high and native Frobenius sources are not collapsed. Rank n is an external summation coordinate, not a native X6 spatial direction. This result narrows a tempting but invalid source-only quotient route; it does not establish an original-class supercongruence.

## Author-side validation and provenance

Exact standard-library Python checks over **all 330** primes p=6m+1 with p<5000 verified the rational-binomial formulas reduced modulo p and p-unit boundary. There were **115** further direct Ward-weight/seam checks and **967** independent finite-Gauss coefficient recurrence comparisons; exact rational Fraction checks at M=1,3,5. Every check PASSED. These are author checks, not independent review. The full checker, raw JSON and expanded proof are retained in this conversation's /mnt/data/em_research files:
- 20261026_offphase_d25_rank_jet_universal_seam_LOCAL_UNPUBLISHED.md (local full proof)
- d25_ward_rank_jet_unimodular_seam_checker_20261026.py
- d25_ward_rank_jet_unimodular_seam_author_check_20261026.json

BRC T0 (typed observed output) and T6 (operation-safe quotient): COMPOSE_APPLIED to the joint rank-jet and compulsory seam repair. T1 p-unit valuation: REUSE_APPLIED. Earlier source-labelled Ward law: COMPOSE_APPLIED, without new contribution credit. Signed observers are not positive BRC mass.

## Native recovery and next exact action

The present Site's direct em_status returned 0.6.11 and research_authority_granted=false, its read-only continuation returned CONTROL_QUOTA, and the Site remained static_machine_readonly / write_relay_enabled=false. Existing verified historical recovery (bridge issue #6524) has no authority for a new Site identity; ownership/predecessor repair remains tracked by enterprise-math issue #1558. No new native CLAIM, OPEN, Source checkpoint, Result, review or activity registration is asserted by this neutral proof storage. If a current-input continuation seed is encountered, its input_artifacts are **inputs**, frontier_notes.completed_units=[], not completed predecessor mathematics.

UR V2 four-file original bundle remains **not byte-recovered**: target SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76, historical 94,687 bytes. Two related corrected uploads previously traced were source_published=false, not interchangeable with the bundle. Earlier UR math is not redone.

**Next scientific unit:** derive and check a type-preserving map (or an exact counterexample to such a map) from original-class D25/LIFT Hasse/Frobenius ports to a *fixed permitted Ward observer*, preserving signed J/E, infinity, ordered high-high and rank moments, then test whether its residual is strictly equivalent to Delta_p-R_p. Native publication of any such evidence still requires genuine winning claim/writer authorization and readback; this neutral note does not change the frozen Source pin or another researcher's ownership.
