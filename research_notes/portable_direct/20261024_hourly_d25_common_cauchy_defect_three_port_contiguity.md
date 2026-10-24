# D25/LIFT — Exact HIGH Cauchy bridge defect, closed three-port rank transport, and rational-Gosper pole-orbit obstruction

2026-10-24 | TASK_RESEARCH | EXACT ALL-m RATIONAL PROOFS / LOCAL EXACT FRACTION SELF-CHECK / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** is not changed. Author logical Research lane: **chatgpt-research-hourly-enterprise-math-20260923**; not the maintenance lane or the distinct onhour Research lane. This is portable author research, not an authorized Source CLAIM/run, an admitted theorem, a native experiment, or an independent review.

## 1. Exact source coefficients and a newly identified bridge defect

The onhour lane's 20261024_onhour_d25_common_low_high_cauchy_carrier.md (commit 68514582c760f562c76043d64eb85f2887858273) proved the correct common carrier for LOW residues and HIGH-A samples and identified the rational forcing shift. Its proposed **all-m exact** expression for the *source-fixed* HIGH-B sector, however, omits a rank-dependent coefficient and parameter-shift defect. The correct precise statement is a congruence modulo the original p, not an exact equality; this note identifies and proves the missing term instead of modifying another author's evidence silently.

For every integer m >= 1 let p_m=6m+1 (primality is needed only when taking p-adic reductions), and put

\[
Q_m(t)=\frac{m!}{t(t+1)\cdots(t+m)},\qquad
h_m(t)=2^{-t}Q_m(t),\qquad
D_m=\frac{2^m(2m)!}{m!(m-1)!}.
\]

The source-fixed A/B sector coefficients and forcing are

\[
a_{m,t}=D_mh_m(t),\quad
c_{m,s}=2^{1-s}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!},
\]
\[
k_s^A=\frac{4(1-2s)(3s+1)}{(2s+1)(6s+1)},\quad
k_s^B=\frac{(2-3s)(6s+1)}{3s(3s+1)},\quad
\kappa(t)=-2+\frac{2/3}{t+1/6}+\frac{1}{t+1/2}.
\]

Keep the genuine separate HIGH-B coefficient **-1/24**, not a fitted 1/3:

\[
Z_m^{\mathrm{src}}
=\sum_{t=1}^{m-1}a_{m,t}k_t^A
-\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}k_s^B.
\]

Define the **auxiliary proposed common-carrier scalar** (not presumed source-exact)

\[
Z_m^{\mathrm{car}}=
D_m\left[\sum_{t=1}^{m-1}h_m(t)\kappa(t)
+\frac13\sum_{t=m+1}^{3m-1}h_m(t)\kappa(t)\right].
\]

**Theorem A (exact defect identity for every integer m >= 1).** With t=m+s,

\[
\boxed{Z_m^{\mathrm{src}}=Z_m^{\mathrm{car}}+p_m\mathcal E_m,}
\]

where the entirely explicit rational correction is

\[
\boxed{\begin{aligned}
\mathcal E_m=D_m\sum_{s=1}^{2m-1}h_m(m+s)\bigg[
&\frac{1}{27s(m+s+1/6)}
+\frac{1}{18(s+1/3)(m+s+1/2)}\\
&-\frac{k_s^B}{12m}\bigg].
\end{aligned}}
\]

In particular, for **every prime p=6m+1 >= 7**, \(\mathcal E_m\in\mathbb Z_{(p)}\) and

\[
Z_m^{\mathrm{src}}\equiv Z_m^{\mathrm{car}}\pmod p.
\]

There is **no general exact equality or congruence modulo p²**. This is important whenever the old mod-p HIGH description is raised one digit or transported in the cutoff rank.

**Proof.** There are three exact rational identities (no modular substitution):

\[
\frac{c_{m,s}}{a_{m,m+s}}=\frac{2(2m+1)}m,\quad
-\frac{c_{m,s}}{24a_{m,m+s}}
=-\frac{2m+1}{12m}=\frac13-\frac{p_m}{12m},
\]

\[
k_t^A=\kappa(t),\qquad
k_s^B=\kappa(m+s-p_m/6).
\]

For t=m+s and d=p_m/6,

\[
\kappa(t-d)-\kappa(t)
=\frac{p_m}{6}\left[
\frac{2/3}{s(t+1/6)}
+\frac1{(s+1/3)(t+1/2)}
\right].
\]

Replace the B branch in \(Z_m^{\mathrm{src}}\) by
\(D_mh_m(m+s)[(1/3-p_m/(12m))\kappa(m+s-p_m/6)]\).
Subtract the auxiliary B branch \(D_mh_m(m+s)\kappa(m+s)/3\), apply the last displayed difference formula, and collect exactly \(p_m\mathcal E_m\). The A branches agree exactly and cancel. All operations are in \(\mathbb Q\).

For target primes, each factor in the formula for \(\mathcal E_m\) is a p-unit: \(1\le s\le2m-1\), \(3s+1<p\), \(m+s+1/6=(p+6s)/6\), \(m+s+1/2=(2m+2s+1)/2\), and \(2m+2s+1<p\). Also \(m,D_m,h_m(m+s)\in\mathbb Z_{(p)}\), with all relevant factorial arguments less than p. Therefore \(\mathcal E_m\in\mathbb Z_{(p)}\). QED.

**Unambiguous counterexample to the previously claimed rational equality.** At m=1, p=7, the actual source HIGH value is \(Z_1^{src}=7/288\), whereas the auxiliary carrier gives \(Z_1^{car}=-14/195\). Their difference is \(7(257/18720)\ne0\). Furthermore \(\mathcal E_1\equiv6\pmod7\). At p=13,m=2, \(\mathcal E_2\equiv1\pmod{13}\), so replacing the source HIGH by the auxiliary carrier also changes its second digit. These are **source-coefficient mismatch witnesses**, not counterexamples to original LIFT.

For a **fixed original p=6m+1** and an auxiliary cutoff rank shift, the exact correction at the successor rank carries \(p_{m+1}=p+6\), not p:

\[
\boxed{
Z_{m+1}^{src}-Z_m^{src}
=(Z_{m+1}^{car}-Z_m^{car})+(p+6)\mathcal E_{m+1}-p\mathcal E_m.
}
\]

One must not discard \(6\mathcal E_{m+1}\), and \(\mathcal E_{m+1}\) is not automatically p-integral at the **previous** prime p. The predecessor's source-fixed \(-82/p\) cutoff theorem concerns \(Z^{src}\), not the uncorrected \(Z^{car}\).

## 2. New exact closed three-port contiguous transport for the auxiliary HIGH carrier

For integers \(1\le a\le b\), define the finite, labeled ports

\[
S_m[a,b]=\sum_{t=a}^{b}h_m(t),\qquad
M_{m,\alpha}[a,b]=\sum_{t=a}^{b}\frac{h_m(t)}{t+\alpha},
\quad\alpha\in\{1/6,1/2\}.
\]
Let \(U_m[a,b]=-2S_m[a,b]+(2/3)M_{m,1/6}[a,b]+M_{m,1/2}[a,b]\), retaining the three distinct port labels. Empty adjacent intervals have zero ports.

**Theorem B (closed 3-port exact rank recurrence).** Define the explicit boundary flux
\(e_m[a,b]=2(h_m(a)-h_m(b+1))\). Then

\[
\boxed{
S_{m+1}[a,b]=-S_m[a,b]+e_m[a,b],
}
\]

\[
\boxed{
(m+1-\alpha)M_{m+1,\alpha}[a,b]
=(m+1)M_{m,\alpha}[a,b]-S_{m+1}[a,b],
\quad\alpha=1/6,1/2.
}
\]

Thus the rank step closes on exactly the displayed three rational ports and a two-endpoint flux. It introduces **no untracked moving Cauchy moment**.

**Proof.** The rational carrier shift gives
\(Q_m(t+1)=tQ_m(t)/(t+m+1)\) and
\(Q_{m+1}(t)=(m+1)Q_m(t)/(t+m+1)\). Including the literal 2-power weight,

\[
h_{m+1}(t)=h_m(t)-2h_m(t+1).
\]

Summing between a and b gives the first formula with the explicit endpoints. Also,

\[
\frac{m+1}{(t+m+1)(t+\alpha)}
=\frac{m+1}{m+1-\alpha}
\left(\frac1{t+\alpha}-\frac1{t+m+1}\right).
\]

The sum of \((m+1)h_m(t)/(t+m+1)\) is \(S_{m+1}\); multiplication by \(m+1-\alpha\) gives the second formula. QED.

**Exact source-preserving moving-window reconstruction.** Write \(A_m=[1,m-1]\), \(B_m=[m+1,3m-1]\) (with empty adjacent A at m=1). The current *auxiliary carrier* obeys \(Z_m^{car}=D_m(U_m[A_m]+U_m[B_m]/3)\), \(D_{m+1}/D_m=4(2m+1)/m\). Compute \(U_{m+1}[A_m]\) and \(U_{m+1}[B_m]\) by Theorem B, then restore every changed endpoint:

\[
\boxed{\begin{aligned}
\frac{Z_{m+1}^{car}}{D_{m+1}}
={}&U_{m+1}[A_m]+\frac13U_{m+1}[B_m]
+h_{m+1}(m)\kappa(m)\\
&+\frac13\left[
-h_{m+1}(m+1)\kappa(m+1)
+\sum_{j=0}^2h_{m+1}(3m+j)\kappa(3m+j)
\right].
\end{aligned}}
\]

These are the real added/removed interval endpoints; the original 1/3 splice is untouched. To obtain **the actual source** \(Z_{m+1}^{src}\), add \((6m+7)\mathcal E_{m+1}\) as proved in Theorem A. Consequently the source-fixed cutoff has an exact rank-transport representation with a **closed 3-port auxiliary state, explicit endpoints, and exact defect restoration**. This is not a claim that the truncated rank m+1 is a new original-prime LIFT instance.

## 3. Exact rational-Gosper obstruction and limits of the conclusion

Let \(\mathcal L_mR(t)=\frac{t}{2(t+m+1)}R(t+1)-R(t)\) on \(\mathbb Q(t)\). The two rational functions \(1/(t+1/6)\) and \(1/(t+1/2)\) represent **linearly independent nonzero classes** in \(\mathbb Q(t)/\mathcal L_m\mathbb Q(t)\), for each fixed m>=1.

**Proof (pole-orbit certificate).** In a nonintegral shift orbit \(\beta+\mathbb Z\), the coefficient \(t/[2(t+m+1)]\) is finite and nonzero. If rational R has no poles in that orbit, neither does \(\mathcal L_mR\). If it has finitely many, let \(\beta+j_{\min}\) and \(\beta+j_{\max}\) be the least and greatest pole positions. At \(\beta+j_{\min}-1\) only the shifted R contributes a pole; at \(\beta+j_{\max}\) only the unshifted R contributes a pole. They are distinct, so the image has **at least two poles in the orbit**, never exactly one. The two fractions above have exactly one pole in their separate nonintegral orbits \(-1/6+\mathbb Z\) and \(-1/2+\mathbb Z\); no nonzero linear combination can be in the image. QED.

Hence **no rational G(t)** can satisfy the unrestricted exact single-stream Gosper identity
\(h_m(t+1)G(t+1)-h_m(t)G(t)=h_m(t)\kappa(t)\) for all admissible t. The inherited LOW ratio \((n-m)/(2(n+1))\) similarly cannot rationally telescope its fixed forcing \(k(n)=-2+(2/3)/(n+1/3)+1/(n+2/3)\): its two nonintegral pole orbits are likewise isolated. This obstruction applies only to a universal single-index rational antidifference; it does **not** rule out finite interpolation, the original full R_n Gosper identity, a compensated coupled WZ/creative telescoper in m and t, or a Cauchy-port extended state. Theorem B supplies a valid exact extension to advance.

## 4. Executed verification, scope and exact next action

An author-side Python Fraction reconstruction **directly compared the original independently labeled a/kA and c/kB sums**, not merely two restatements of the auxiliary carrier. Theorem A and p-integrality were checked for **all 25 primes p=6m+1 below 250**; sample residues \(\mathcal E_m\bmod p\) are 7:6, 13:1, 19:17, 31:15, 37:20, 43:1, 61:5, 67:8, 73:37, 211:56. Theorem B's fixed-window recurrences passed **120 exact rational cases**. Its moving-window identity, independently evaluated against \(Z_{m+1}^{src}\) **after** exact defect restoration, passed for m=1,...,10 and 35 (11 cases). The infinite-m claims have elementary rational proofs above; finite tests are author regression checks, **not** mathematical admission, independent review or native benchmarking.

**BRC: REUSE_APPLIED / COMPOSE_APPLIED.** Carrier retains residue/sample observer distinction; signed HIGH-A and HIGH-B origin; the 1/3 splice only as an *auxiliary congruence*; the exact \(p\mathcal E\) repair coordinate; m/t rank and endpoint labels; and the original p-adic valuation. The prior all-m HIGH-B exact identification erased the defect and is now explicitly distinguished from the valid mod-p readout. No X6/native physical theorem or Foundation promotion is asserted.

**Critical do-not-repeat/correction:** do not use \(Z_m^{car}=Z_m^{src}\) as a rational equality, or as a mod-p² substitution. This corrects the **strength** of a cross-lane portable claim without changing that lane's immutable original evidence; use \(Z_m^{src}=Z_m^{car}+p\mathcal E_m\). The earlier -82/p theorem and original finite obstruction refer to \(Z^{src}\) and remain separate.

**Smallest new unit:** insert the exact correction into the three-port rank transport and the existing two-digit LOW/HIGH Laurent finite part, then derive a corrected coupled finite-difference/WZ certificate for the *original* \(\mathcal D_m^{finite}\) and its exact fixed-rank seam/terminal. If it cannot close, keep the two independent fractional Cauchy ports and the p-divided coefficient defect rather than dropping them. The native Task additionally awaits Source-specific divided-power/CM representative class, map direction/semilinearity, ordinary \(\omega+6\nabla_\lambda\omega\) comparison, exact leading normalization and same-class kappa bridge. Parent LIFT remains OPEN. No native CLAIM/run/checkpoint/Result/review, scheduler or notification mutation is claimed.
