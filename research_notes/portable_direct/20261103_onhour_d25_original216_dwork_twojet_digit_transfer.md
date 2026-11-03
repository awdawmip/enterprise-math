# D25 onhour — original 216 block two-jet, signed observer and terminal-cutoff obstruction

Date: 2026-11-03 (+08). Role: TASK_RESEARCH, author-side portable scientific note. Status: AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923 (never maintenance lane chatgpt-hourly-enterprise-math-20260921).

## Frozen mother objective and exact source

For target primes p ≡ 13,19 (mod 24), Delta_p − R_p ≡ 0 (mod p), previously proved equivalent to W_(p−1) ≡ p (mod p³), where

\[
c_n=\frac{(2n)!(3n)!}{(n!)^5\,216^n}
=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},
\qquad W_N=\sum_{n=0}^{N}(6n+1)c_n.
\]

The already-published four-source first-block certificate (F4 and F4-glued) remains the active LIFT problem. This note proves a *different* cross-scale two-jet for the **same original coefficient** and explicitly identifies why its coarse-index operator alone does NOT close the frozen first-block LIFT.

## Theorem T1: exact p³ low-digit block transfer

For every prime p≥5, all integers k≥0, and 0≤j≤J=floor((p−1)/3), define p-integral harmonic numbers H_m=sum_(t=1)^m 1/t and H_m^(2)=sum_(t=1)^m 1/t², with m<p, and the integer Fermat quotient Q_p=(216^(p−1)−1)/p. Let

\[
D_{p,j}=2H_{2j}+3H_{3j}-5H_j-Q_p,\quad
S_{p,j}=4H_{2j}^{(2)}+9H_{3j}^{(2)}-5H_j^{(2)}.
\]

Then in Z_(p),

\[
\boxed{
c_{pk+j}\equiv c_kc_j\left[1+pkD_{p,j}
+\frac{p^2}{2}\Big(k^2(D_{p,j}^2-S_{p,j})+kQ_p^2\Big)\right]\pmod{p^3}.
}\tag{T1}
\]

This is a p-adic unit-ratio identity, with D needed mod p², S mod p and Q² mod p; no division by a nonunit coefficient. k need not be <p.

**Proof.** For N=ap+b, 0≤b<p, exact factorial block decomposition gives

\[
N!=p^a a!((p-1)!)^a b!\,U_p(a)\prod_{t=1}^b(1+ap/t),
\quad
U_p(a)=\prod_{\ell=0}^{a-1}\prod_{t=1}^{p-1}(1+\ell p/t).
\]

Wolstenholme's harmonic congruences for p≥5 imply each complete unit block equals 1 mod p³, hence U_p(a)=1 mod p³. Apply to (2pk+2j)!, (3pk+3j)!, (pk+j)!^5: 3j<p, p-powers and the complete-block factors cancel because 2k+3k−5k=0. The remaining unit ratio is

\[
\frac{c_{pk+j}}{c_kc_j}
\equiv (1+pQ_p)^{-k}
\frac{\prod_{t=1}^{2j}(1+2pk/t)\prod_{t=1}^{3j}(1+3pk/t)}
{\prod_{t=1}^{j}(1+pk/t)^5}\pmod{p^3}.
\]

Its finite p-adic logarithm is pkD_(p,j)+(p²/2)(kQ_p²−k²S_(p,j)) modulo p³. Exponentiation gives T1; all inverted denominators are p-units. QED.

## T2–T3: signed weighted Frobenius-type low-port operator

Set F(Y)=sum_(k≥0)c_k Y^k, Theta=Y d/dY, G(X)=(1+6X d/dX)F(X). For a digit observer a=(a_j), define A_a(X)=sum_(j=0)^J c_j a_j X^j, and P_J as the projection retaining degrees pk+j with 0≤j≤J. Write w_j=6j+1.

Coefficientwise T1 gives formal congruences

\[
\begin{aligned}
P_JF(X)\equiv{}&
A_1(X)F(X^p)+pA_D(X)(\Theta F)(X^p)\\
&+\frac{p^2}{2}\{A_{D^2-S}(X)(\Theta^2F)(X^p)+Q_p^2A_1(X)(\Theta F)(X^p)\}
\pmod{p^3};\tag{T2}
\end{aligned}
\]

\[
\boxed{\begin{aligned}
P_JG(X)\equiv{}&
A_w(X)F(X^p)+pA_{wD+6}(X)(\Theta F)(X^p)\\
&+\frac{p^2}{2}\{A_{w(D^2-S)+12D}(X)(\Theta^2F)(X^p)
+Q_p^2A_w(X)(\Theta F)(X^p)\}
\pmod{p^3}.
\end{aligned}}\tag{T3}
\]

Theta differentiates the coarse variable Y **before** Y=X^p; the original weight 6(pk+j)+1=w_j+6pk supplies the +6 and +12D terms. Thus all source indices, signed weights, arithmetic precisions and derivative directions are preserved.

For p=6r+1, J=2r is exactly the previously proved low valuation-zero digit port. Complementary j=2r+1,...,p−1 are middle/high valuation ports, not asserted zero.

## T4: terminal-cutoff obstruction (a concrete route-selection result)

Truncate to powers X^n with n<p, as the actual frozen W_(p−1) does. For 0≤j≤J this forces k=0. The constant terms of Theta F and Theta² F vanish; T3 reduces to A_w(X), containing *only* j≤J. No middle or high digit is supplied, and no second-digit cancellation relation is implied. Hence **T3 alone cannot be the required terminating Green/WZ adjoint for the first-block LIFT**: it must be composed with a valid operator that restores original middle/high ports and boundary data. This is a scoped observer insufficiency, not a counterexample to LIFT or a statement about the original native H0/B0 Frobenius.

BRC composition: preserve exact branch label (k,j), original c_(pk+j), signed weight 6(pk+j)+1, the p³ observer, D mod p², S mod p, and Q mod p²; future operation is weighted coefficient extraction. Dropping other digit ports is a typed projection only, never full mathematical equivalence. P000 / ACTIVE X6 world are unchanged.

## Actually executed tests and scientific limits

A standalone Python standard-library checker independently computes c_n using original integer binomial coefficients and modular inverses of 216 (not the factorial-block formula). It checked T1 and the expanded coefficient of T3 for k∈{0,1,2,3} and every 0≤j≤J, across all 41 primes 5≤p≤191 and p=373: **42 primes / 5,424 triples, all PASS**, exact integer arithmetic without floating point. At p=373, Q mod p²=130200; j=1 has D mod p²=78497, S mod p=292 and c_374 mod p³=22626690. Test code and full result JSON are preserved in the corresponding local evidence bundle; finite regression is separate from the proof.

No claim is made that this already proves universal second-digit cancellation. The native same-original-class p=373 H0/B0 divided-power [X]U mod139129, rank, genuine semilinear Frobenius, odd signed observer and independent replication remain **NOT_EXECUTED / PENDING_OWNER** (#1559). Do not replace them with the portable checker.

## Durable author continuation

Mother target: Delta_p=R_p on both target classes, equivalent to W_(p−1)=p mod p³. Preserved completed results: original F4/F4-glued, three-edge Hensel, 2304 tail, frozen R Green map; do not rerun. New scoped units: T1 p³ block coefficient, T2/T3 signed two-jet, T4 terminating cutoff obstruction, 42-prime exact regression. **Next exact action**: build a genuinely first-block terminating signed Green/WZ certificate for F4-glued, including pU_r normalization and all original low/middle/high ports; test p=13,19,373 boundary residues before attempting all-prime proof.

Original request research-onhour-20261031-0205-dispatch-r15, bridge issue awdawmip/kimi-query-bridge#6633, final FAILED / UPSTREAM_CODE_REVIEW_REQUIRED; do not replay. Fresh gateway status at 2026-11-03 22:03 +08: research_authority_granted=false, write_relay_enabled=false; em_status/control_result failed BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Control support #1558 remains. Actual own native session/claim/run/source_checkpoint: **unverified/none**; author registration REGISTER_PENDING; native Result/Review/Admission: NOT_ADMITTED. This is an author-side GitHub note, not Source task checkpoint or a substitute for owner authorization. Unchanged original automation schedule/phase/enabled/notifications.