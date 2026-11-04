# D25 — exact dual Picard–Fuchs forcing and two-kernel terminal Fermat-quotient carry

Date: 2026-11-04 (+08). Status: AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Scope: portable author-side mathematical evidence, not a native Source checkpoint, CLAIM, Result, review or promotion.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7; immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Current Research lane logical ID requested: chatgpt-research-hourly-enterprise-math-20260923. Distinct from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921.
This construction consumes the published original-216 Picard–Fuchs four-band flux and the separate onhour D25 reciprocal middle/high observer without replacing either source.

## Theorem A: exact two-way operator forcing

For every prime p>=5, define the **original** rational coefficients and the cutoff polynomials

\[
a_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\quad
b_k=\frac{(4k)!}{(k!)^4 2304^k},\qquad
A(t)=\sum_{k=0}^{p-1}a_kt^k,\quad B(t)=\sum_{k=0}^{p-1}b_kt^k.
\]

Writing \(\theta=t\,d/dt\), define

\[
L_A=\theta^3-\frac t2(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23),\quad
L_B=\theta^3-\frac t9(\theta+\tfrac12)(\theta+\tfrac14)(\theta+\tfrac34),
\]

\[
R(\theta)=(\theta+\tfrac12)
\left[\frac7{18}\theta(\theta+1)+\frac{13}{144}\right],\quad
\delta_p=a_p-b_p,\quad D=A-B.
\]

Then the following **two exact polynomial identities over Q[t]** hold:

\[
\boxed{L_B D=tR(\theta)A-p^3\delta_p\,t^p,}\tag{A1}
\]
\[
\boxed{L_A D=tR(\theta)B-p^3\delta_p\,t^p.}\tag{A2}
\]

Proof: The factorial recurrences are exactly

\[
\frac{a_{k+1}}{a_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},\quad
\frac{b_{k+1}}{b_k}=\frac{(4k+1)(4k+2)(4k+3)}{576(k+1)^3}.
\]

Consequently, for the finite polynomials, \(L_AA=-p^3a_pt^p\) and \(L_BB=-p^3b_pt^p\), with all interior coefficients cancelling. Elementary expansion gives the **factorized mismatch**
\[
L_B-L_A=tR(\theta),
\]
because \(\tfrac12[(\theta+\tfrac13)(\theta+\tfrac23)]-
\tfrac19[(\theta+\tfrac14)(\theta+\tfrac34)]
=\tfrac7{18}\theta(\theta+1)+\tfrac{13}{144}\).
Subtract and substitute; both (A1) and (A2) follow without a hypothesized pullback or an assumed equality of the two Picard–Fuchs systems.

The original weighted scalar interface remains exactly
\[
W_{216}(p-1)-S_{2304}(p-1)
=\left[(1+6\theta)D-2\theta B\right]_{t=1}.\tag{A3}
\]
At the target classes p mod 24 in {13,19}, the published Guo–Zudilin quartic half/full congruence permits S_full to be replaced by S_half modulo p^3. Equations (A1)–(A3) are a concrete **inhomogeneous Green/WZ input** for the still-unproved scalar cancellation, not a proof of that cancellation or of the separate D24 Delta_p-R_p bridge.

## Theorem B: terminal coefficients through p^3 and exceptional endpoint valuation

For every prime p>=5, set the ordinary integer Fermat quotient \(q_p(u)=(u^{p-1}-1)/p\) for p-coprime u. In the p-local ring:

\[
\boxed{
a_p\equiv \frac1{18}\left(1-pq_p(216)+p^2q_p(216)^2\right)\pmod{p^3},
}\tag{B1}
\]
\[
\boxed{
b_p\equiv \frac1{96}\left(1-pq_p(2304)+p^2q_p(2304)^2\right)\pmod{p^3}.
}\tag{B2}
\]

Proof: The exact binomial representations are
\(a_k={2k\choose k}^2{3k\choose k}216^{-k}\) and
\(b_k={2k\choose k}^2{4k\choose2k}2304^{-k}\).
For c=1,2,3,
\({(c+1)p\choose p}=(c+1)\prod_{j=1}^{p-1}(1+cp/j)\).
The finite harmonic sums \(H_{p-1}^{(2)}\equiv0\bmod p\) and
\(H_{p-1}^{(1)}\equiv0\bmod p^2\) follow from inverse-square power summation and pairing j with p-j (p>=5). Expanding the products then gives
\({2p\choose p}\equiv2,\ {3p\choose p}\equiv3,\ {4p\choose p}\equiv4\bmod p^3\).
Since \({4p\choose2p}={4p\choose p}{3p\choose p}/{2p\choose p}\equiv6\),
the two original coefficients satisfy
\(a_p\equiv12\,216^{-p}\) and \(b_p\equiv24\,2304^{-p}\bmod p^3\).
Now \(u^{p-1}=1+pq_p(u)\) exactly; invert by the quadratic geometric expansion. This proves (B1)–(B2).

In particular
\[
\delta_p\equiv\frac{13}{288}\pmod p.
\]
Thus \(v_p(\delta_p)=0\) for all p>=5 except possibly p=13. At p=13, explicit independent small-modulus arithmetic gives
\(216^{12}\equiv92,\ 2304^{12}\equiv14\pmod{169}\);
hence \(a_{13}\equiv164,\ b_{13}\equiv21\pmod{169}\) and
\(\delta_{13}\equiv143=13\cdot11\pmod{169}\). Consequently,
\[
\boxed{
v_p(p^3\delta_p)=
\begin{cases}
4,&p=13,\\
3,&p\ge5,\ p\ne13.
\end{cases}}\tag{B3}
\]
The p=13 fourth-digit suppression is specific to the **difference** of the two terminal sources, not to either operator's separate cutoff flux.

Formulae (B1)–(B2) also determine \(p^3\delta_p\) modulo \(p^6\) in terms of two explicitly retained Fermat quotients; (A1)–(A2) are exact at every precision.

## Computation and BRC observer scope

Actual Python standard-library integer modular checker reconstructed both original factorial coefficients from stripped-p factorials, checked the two coefficient recurrences, every coefficient of both identities (A1),(A2) modulo p^4 and both terminal expansions modulo p^3. It passed **all 301 primes 5<=p<=2000**, **277045 individual coefficient positions**. At p=13: a_p=1347, b_p=2049, delta=1495 (mod 2197), delta/13=11 (mod 13). At p=19: delta=5299 (mod 6859), delta=17 (mod 19). These are finite verification observations; the all-prime claims are proved algebraically above.

BRC usage: population = individually labelled original 216/2304 coefficient sources at indices 0..p; observer = signed weighted evaluation at t=1 and differential boundary source; retained = source identity, index, p-valuation, endpoint delta and Fermat-quotient carries; operations = theta, L_A, L_B, finite cutoff, p-adic reduction. No positive-mass collapse, unverified quotient, native X6 geometric theorem, or fixed-373 semilinear experiment is asserted.

## Source-exact continuation

Mother task remains the frozen D24 \(\Delta_p-R_p\) second-digit lift plus original signed 216 scalar p^3 and the precise bridge. Consume (A1)–(A3) with the earlier source-typed low/middle/high observers and the onhour complementary reciprocal observer. **Next smallest mathematical action:** construct an explicit finite Green/creative-telescoping certificate evaluating
\([ (1+6\theta)D - 2\theta B ]_{t=1}\) modulo p^3 from the factorized forcing \(tR(\theta)B\), retaining the original p-cutoff source. Test each boundary for p=13,19,373, then prove the relevant prime-class cancellation and independently bridge to D24 Delta-R. Avoid treating the exceptionally suppressed p=13 terminal difference as a uniform result.

Native read-only Gateway 0.6.11 on this run returned research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, control state UPSTREAM_CODE_REVIEW_REQUIRED. No new native recovery/claim/run/checkpoint/Result effect is claimed. Old request #6637/#6638 and protected staging were not replayed or altered. Historical control support #1558; original fixed-373 experiment support #1559. Scientific input pin unchanged; evidence status UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.