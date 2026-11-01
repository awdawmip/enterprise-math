# D25/LIFT: complementary Gauss / Clausen reciprocal prime-index mirrors

Date: 2026-10-31 (Asia/Hong_Kong). Research logical lane: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Source grading: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE_LOCKED unchanged. These are external p-adic identities, not native Enterprise X6 claims.

## New theorem G: complementary Gauss reciprocal mirror

For every prime p=6m+1 >=7, let

\[
b_n={(1/6)_n(1/3)_n\over 2^n(n!)^2},
\quad
c_n={(5/6)_n(2/3)_n\over 2^n(n!)^2}.
\]

For every 1<=k<=4m, the coefficient c_k is a p-unit and b_{p-k} has valuation exactly two, and

\[
\boxed{36k^2 c_k\,{b_{p-k}\over p^2}\equiv1\pmod p.}\tag{G}
\]

Proof: the exact forward ratios are
b_{n+1}/b_n=(6n+1)(3n+1)/[36(n+1)^2] and
c_k/c_{k-1}=(6k-1)(3k-1)/(36k^2).
With v_k=b_{p-k}/p^2 mod p, reversal gives
v_{k-1}/v_k=(6k-1)(3k-1)/[36(k-1)^2] for 2<=k<=4m.
It follows that k^2 c_k v_k is constant. The previously proved and checked Wilson endpoint v_1=1/10 and c_1=5/18 fixes this constant at 1/36. The denominators are p-units throughout the indicated range. This is algebraic for all primes in the class, not inferred from samples.

For p mod24 in {13,19}, retain GH-166/GH-178's **original frozen signed projection** (not the separate reflected R_p(9)):

\[
R_p=2\sum_{i=1}^{m}b_i\sum_{k=1}^{i}
[1+6(i-k)]\,{b_{p-k}\over p^2}\pmod p.
\]

The mirror proves the new exact complementary low-index expression

\[
\boxed{R_p\equiv {1\over18}\sum_{i=1}^m b_i
  \sum_{k=1}^i {1+6(i-k)\over k^2c_k}\pmod p.}\tag{G-R}
\]

With P_i=sum_{k=1}^i 1/(k^2 c_k), J_i=sum_{k=1}^i 1/(k c_k),
this is also

\[
\boxed{R_p\equiv {1\over18}\sum_{i=1}^m b_i
[(1+6i)P_i-6J_i]\pmod p.}\tag{G-R2}
\]

No individual reciprocal moment is asserted zero. This maps the high-index p^2-normalized signed tail to a pair of low-index complementary Gauss moments, with all indices and signs preserved. Complementary parameters also occur in the separately authored onhour Euler–Clausen three-factor port decomposition; that source is consumed at its author-side status, not independently reviewed or recredited here.

## New theorem C: Clausen reciprocal mirror and independent p^4 tail observer

Let

\[
a_n={(1/2)_n(1/3)_n(2/3)_n\over2^n(n!)^3}
={\binom{2n}{n}^2\binom{3n}{n}\over216^n}.
\]

For the same p=6m+1 and 1<=k<=2m, a_k is a p-unit and a_{p-k} has valuation three. One has

\[
\boxed{18 k^3 a_k\,{a_{p-k}\over p^3}\equiv-1\pmod p.}\tag{C}
\]

Proof: a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/[36(n+1)^3].
If u_k=a_{p-k}/p^3 mod p, then
u_{k-1}/u_k=(2k-1)(3k-1)(3k-2)/[36(k-1)^3].
Thus k^3 a_k u_k is constant. The previously established Wilson endpoint a_{p-1}/p^3=-1 and a_1=1/18 set it equal to -1/18. The relevant recurrence denominators are units.

Write A_p(1)=sum_{n=0}^{p-1}(6n+1)a_n and the previously established minimal p^3-safe cutoff A_p^short(1)=sum_{n=0}^{4m}(6n+1)a_n. The **auxiliary p^4** normalized omitted tail Q_p=[A_p(1)-A_p^short(1)]/p^3 modp is exactly

\[
\boxed{Q_p\equiv\sum_{k=1}^{2m}{6k-1\over18k^3a_k}\pmod p.}\tag{C-Q}
\]

This is a distinct reciprocal-prefix representation for an existing observer, not a new universal p^3 LIFT proof and not a new census. It recovers the earlier known Q_373=278 and Q_1327=0 without changing the frozen X=1 parameter.

## Execution / mathematical evidence

Companion executed Python stdlib integer program d25_gauss_clausen_mirror_check.py independently iterated the **original** Gauss recurrence modulo p^3, complementary Gauss prefix modulo p, and **original** Clausen recurrence modulo p^4. It checked every k of (G),(C) for every prime 7<=p<5000 with p mod6=1, compared original signed high-index R with (G-R2) for both frozen target residue classes, and checked the original direct high-index p^4 weighted tail against (C-Q).

Result: 330 primes; 166 target-class primes; 514860 Gauss mirror pair checks and 257430 Clausen pair checks, all PASS. Original signed R anchors: p=13 -> 0, 19 -> 12, 37 -> 11, 157 -> 82, 373 -> 196 (mod p); Q_373=278, Q_1327=0. Exact terminal marker PASS_D25_COMPLEMENTARY_GAUSS_AND_CLAUSEN_MIRRORS_EXACT. No floating point, external runtime, Lean checker or independent mathematical review.

BRC COMPOSE_APPLIED: carrier Z_(p) rational hypergeometric sequences with source family, original index, reversed index, valuation, normalization, signed weight and original-source provenance. Operations: reverse n to p-k, normalize at proven valuation, take original signed weighted prefix, read fixed-X=1 mod p^3; Q is a separate p^4 observer. The reciprocal low-index pair (P_i,J_i) is sufficient for the stated signed-projection readout but not automatically sufficient for native H0/B0 or p-adic higher-digit observers. No native six-axis transfer is claimed.

Consume, do not duplicate: GH-166/167 original signed tail; GH-170–175 valuation/tail endpoints; GH-178/179 parameter jets; the same Research lane's exact harmonic jet blocks and rational one-term Gosper obstruction; the onhour Euler eleven-source port work.

The fixed-X LIFT target is **OPEN** for all p mod24 in {13,19}: A_p(1) ?= p (mod p^3). Next smallest scientific question: combine (G-R2) with the existing complete carry + parameter-jets – original-R connection, and find an actual two-parameter WZ, CM or Gauss–Manin signed **joint** evaluation, not one-term Gosper (already obstructed) and not separate assumptions that each port vanishes. D25 native H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius/eta, signed Green/Hesse and actual native p=373 remain separately due.

Control status observed during this author-side unit: Enterprise Math Gateway 0.6.11 research_authority_granted=false; executor_binding_configured=false; active_jobs=5/5; CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Native recovery_status was advertised in a contract but not a callable entrypoint here. No new session, claim/open, Source checkpoint, formal Result, review or authorized experiment. The old service session/staging and maintenance conversation remain unchanged. Existing responsible tickets enterprise-math #1558 (control) and #1559 (native experiment). GitHub author-side persistence is separate from Source durable frontier or mathematical admission.
