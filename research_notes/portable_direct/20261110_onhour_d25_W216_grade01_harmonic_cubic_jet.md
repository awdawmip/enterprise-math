# D25 / W216 — Fourth-digit harmonic cubic jets of original grades 0 and 1

Date: 2026-11-10 (Asia/Hong_Kong). Classification: **AUTHOR_SIDE / ALL-PRIME EXACT ALGEBRAIC REDUCTION / TEN EXACT TWO-PATH REGRESSIONS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen source `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## 1. The original indexed source and BRC carrier

For a prime `p=6m+1>=13` put
\[
 A_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\quad
 C_{p,g}(a)=A_a^{-1}\sum_{\substack{0\le b<p\\ \lfloor2b/p\rfloor+\lfloor3b/p\rfloor=g}}(6pa+6b+1)A_{pa+b}.
\]
Define \(\mathcal L(f)=f(3)-5f(2)+7f(1)-3f(0)\) and \(L_g=\mathcal L(C_{p,g})\).
Here \(\sum_{g=0}^3L_g=q_3-2q_2\) exactly, with the original signed weight and \((a,b)\) labels retained. Grade intervals are \([0,2m]\), \([2m+1,3m]\), \([3m+1,4m]\) and \([4m+1,6m]\).

The preceding author result proved
\[
 L_2\equiv-24W_2-56pJ_2,\qquad L_3\equiv-108W_3\pmod{p^4},
\]
with original weighted \(W_g\) and explicit first jet \(J_2\). The present work treats **the two remaining original grades**, not another precision scan.

All sums are p-local rationals. Let
\[
 H_n^{(r)}=\sum_{j=1}^n j^{-r},\quad Q=\frac{216^{p-1}-1}{p},
 \quad h_2=\frac{H_{p-1}^{(2)}}p\pmod p.
\]
For all denominators in these harmonic expressions, only indices \(<p\) occur; \(p\) is never inverted. \(Q\) and \(h_2\) are p-integral. The value \(Q\) is used to precision required by the final observer, not treated as a floating approximation.

## 2. Grade 1 (2m+1 <= b <= 3m): all-prime second-order p-block jet

Put \(s=3b-p\) and \(\widehat H_s^{(r)}=\sum_{j=1}^s(p+j)^{-r}\). Define
\[
 \lambda_b^{(1)}=2H_{2b}^{(1)}+3\widehat H_s^{(1)}-5H_b^{(1)}-Q,\quad
 \mu_b^{(1)}=-4H_{2b}^{(2)}-9\widehat H_s^{(2)}+5H_b^{(2)}.
\]
The exact original factorial block calculation, through relative precision \(p^3\), gives
\[
 \frac{A_{pa+b}}{A_a}\equiv A_b(3a+1)
 \Bigl[1+pa\lambda_b^{(1)}+
 p^2\Bigl(\frac{aQ^2}{2}+\frac{a^2}{2}(\mu_b^{(1)}+(\lambda_b^{(1)})^2)\Bigr)\Bigr]
 \pmod{p^4}.
\]
The factors \(3a+1\) are the **original exceptional p-factor**, since \(\lfloor3b/p\rfloor=1\) while \(\lfloor2b/p\rfloor=0\). The p-free full-block ratio is \(1\bmod p^3\), adequate here because \(p\mid A_b\).

Define **signed original-grade** quantities
\[
\begin{aligned}
 W_1&=\sum_{I_1}(6b+1)A_b,\\
 Z_1&=\sum_{I_1}A_b[6+(6b+1)\lambda_b^{(1)}],\\
 K_1&=\sum_{I_1} A_b(6b+1)Q^2/2,\\
 V_1&=\sum_{I_1}A_b[6\lambda_b^{(1)}+
       (6b+1)(\mu_b^{(1)}+(\lambda_b^{(1)})^2)/2].
\end{aligned}
\]
The signed \(6pa\) carry remains present. Since \(\mathcal L(3a+1)=0\),
\(\mathcal L(a(3a+1))=-12\), \(\mathcal L(a^2(3a+1))=-22\), we prove:
\[
 \boxed{L_1\equiv -12pZ_1-12p^2K_1-22p^2V_1\pmod{p^4}.}\tag{G1}
\]
No uniform cancellation assertion is used.

## 3. Grade 0 (0 <= b <= 2m): all-prime cubic p-block jet

Put
\[
\begin{aligned}
 \lambda_b^{(0)}&=2H_{2b}^{(1)}+3H_{3b}^{(1)}-5H_b^{(1)}-Q,\\
 \mu_b^{(0)}&=-4H_{2b}^{(2)}-9H_{3b}^{(2)}+5H_b^{(2)},\\
 \nu_b^{(0)}&=8H_{2b}^{(3)}+27H_{3b}^{(3)}-5H_b^{(3)},\\
 S_b&=\mu_b^{(0)}+(\lambda_b^{(0)})^2,\\
 N_b&=\nu_b^{(0)}/3-5h_2+
 \lambda_b^{(0)}\mu_b^{(0)}/2+(\lambda_b^{(0)})^3/6.
\end{aligned}
\]
The **full-block correction** cannot be dropped at fourth digit. For
\(D_p(t)=\prod_{j=1}^{p-1}(tp+j)\) the p-free factorial block log is
\[
 \log\frac{\prod_{t<2a}D_p(t)\prod_{t<3a}D_p(t)}
 {(\prod_{t<a}D_p(t))^5}
 \equiv -5p^3a^3h_2\pmod{p^4}.
\]
To derive it, use
\(\log D_p(t)-\log D_p(0)\equiv ptH_{p-1}^{(1)}
-\frac{p^2t^2}{2}H_{p-1}^{(2)}\pmod{p^4}\);
\(\sum t\) of the weighted 2a/3a/5a block combination is \(4a^2\);
\(\sum t^2\) is \(2a^2(5a-2)\).
Wolstenholme and pairing give \(2H_{p-1}^{(1)}\equiv-pH_{p-1}^{(2)}\pmod{p^3}\) and \(H_{p-1}^{(3)}=0\bmod p\). Substitution yields exactly \(-5p^3a^3h_2\).

Combine this with incomplete blocks and
\(216^{-a(p-1)}=(1+pQ)^{-a}\). The p-adic exponential yields
\[
\begin{aligned}
\frac{A_{pa+b}}{A_a}\equiv A_b\bigg[1+
pa\lambda_b^{(0)}+
p^2\left(\frac{aQ^2}{2}+\frac{a^2S_b}{2}\right)
+p^3\left(-\frac{aQ^3}{3}+
  \frac{a^2\lambda_b^{(0)}Q^2}{2}+a^3N_b\right)\bigg]\pmod{p^4}.
\end{aligned}
\]
Here symbols denote their p-adic rational values; for **the final \(\mathcal L\) observer only** it suffices to compute \(Q,\lambda,\mu,S\) modulo \(p^2\) and \(\nu,N,h_2\) modulo p, because the uncertain high digits occur in terms linear in a, killed by \(\mathcal L\).

Use \(\mathcal L(1)=\mathcal L(a)=0\),
\(\mathcal L(a^2)=-4\), \(\mathcal L(a^3)=-6\).
Apply the original \(6pa+6b+1\) signed weight before \(\mathcal L\). The resulting new all-prime formula is
\[
 \boxed{\begin{aligned}
 L_0\equiv \sum_{b=0}^{2m}A_b\bigg\{
 p^2[-2(6b+1)S_b-24\lambda_b^{(0)}]\\
 +p^3[-2(6b+1)\lambda_b^{(0)}Q^2
       -6(6b+1)N_b-12Q^2-18S_b]\bigg\}
 \pmod{p^4}.
 \end{aligned}}\tag{G0}
\]

## 4. Combined original-source finite-band certificate and remaining theorem

Joining (G0), (G1) to previously proved (G2), (G3), the exact scalar
\(q_3-2q_2\) equals
\[
\begin{aligned}
 \sum_{b\in I_0} A_b\{p^2[-2(6b+1)S_b-24\lambda_b^{(0)}]
     +p^3[-2(6b+1)\lambda_b^{(0)}Q^2-6(6b+1)N_b-12Q^2-18S_b]\}
\\{}-12pZ_1-12p^2K_1-22p^2V_1-24W_2-56pJ_2-108W_3
 \pmod{p^4}.
\end{aligned}
\]
This is an **unconditional explicit congruence formula**, established for all primes p=6m+1>=13 and retaining the four original signed branches and all p-adic carries. The additional assertion that its right side vanishes mod \(p^4\) is **still conjectural**. It was checked here for ten primes; it is not a full-proof result.

BRC: **COMPOSE_APPLIED** to \((a,b,\mathrm{grade}, v_p(A_b), p\text{-unit},6pa+6b+1)\); preserved original grade source and signed cancellations. The moment-projected q-combination does not reconstruct native original H0/B0, odd \(\kappa\) or arbitrary future operators.

## 5. Reproducible exact regression and next action

The companion program `d25_w216_grade01_harmonic_jet_20261110.py` independently constructs each original coefficient by (i) integer binomial factorials and (ii) p-free factorial valuation/units, compares all source coefficients through four complete p-blocks, then evaluates (G0) and (G1) against the uncompressed original band Newton sums. All **ten primes 13,19,31,37,43,61,67,73,109,373 passed**. The final column's sum vanishes for these *finite witnesses only*.

| p | L0 mod p⁴ | L1 mod p⁴ | L2 mod p⁴ | L3 mod p⁴ |
|---:|---:|---:|---:|---:|
| 13 | 4901 | 20280 | 18759 | 13182 |
| 19 | 123462 | 2527 | 100358 | 34295 |
| 37 | 1076034 | 948717 | 1520959 | 202612 |
| 373 | 6206544690 | 8485755968 | 14213279511 | 9808177113 |

The exact next mathematical action is a finite-grade reflection/shift telescoping identity for this *combined* signed sum at precision p4, or an exact source-aligned counterexample. Both residual classes p≡13,19 (mod24) are retained. The primary D25 mother target remains original \(\Delta_p-R_p=0\bmod p\) and distinct native H0/B0 \([X]U\bmod139129\), rank, signed odd branch, semilinear Frobenius \(\eta\) and \(\kappa\), independent validation **NOT_RUN / PENDING_OWNER** under existing Issue #1559.

Source control unchanged: last successful exact read `onhour11-20261110-1515-exact-cont` at `407d531b4048b4094f317eac892832f847ef621e`. Researcher's earlier session `MCP-5378d3819d8947bda9049c9428493e2d` has an unrecoverable-to-current-caller private key gap, so no current winning claim/open run or Source-native checkpoint is asserted. Original session-request receipt read this turn failed transiently `BACKEND_IDENTITY_CHECK_UNAVAILABLE; operation_sent=false`. The maintenance lane was not accessed or adopted; the old 3 staging objects remain independent provenance.
