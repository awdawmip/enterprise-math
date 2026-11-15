# R749SQR — Exact six-phase source quasipolynomials and minimal shift-faithful residual

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**.

Frozen independent auxiliary Walsh source model: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Continues R749SQQ, PR #2519 @3dfef5ca3ae9352e2cecafe3a36d735a89a07b92. This is a positive labeled-source observer theorem, not an asserted native signed X6 Cell/Port or BRC computational lift.

## Exact population

Take seven distinct labeled sources with weights
\[
s=(1,1,1,2,2,3,3), \quad
\Omega_r=\{k\in\mathbb Z_{\ge0}^7:\sum_i s_i k_i\le r-1\}.
\]
Write \(C_r=|\Omega_r|\) and \(T_{h,r}=h\sum_{k\in\Omega_r}k_{j(h)}\), where \(j(h)\) marks the first weight-\(h\) source for \(h=1,2,3\). Let \(E_{h,r}=T_{h,r}/(r C_r)\) for integers \(r\ge1\); \(C_0=T_{h,0}=0\).

## Theorem A — all-precision exact quasipolynomial reconstruction

For each \(a\in\{0,\ldots,5\}\), the values \(C_{a+6n}\) are polynomials in \(n\ge0\) of degree at most 7. For each marked weight \(h\), \(T_{h,a+6n}\) has degree at most 8. Thus the following identities hold for every nonnegative integer \(n\):
\[
\boxed{C_{a+6n}=\sum_{j=0}^7\binom nj\Delta_6^j C_a,\qquad
T_{h,a+6n}=\sum_{j=0}^8\binom nj\Delta_6^j T_{h,a}.}
\]
Here \(\Delta_6 u_r=u_{r+6}-u_r\). Initial counts through \(r=53\) reconstruct **all** integer numerators and denominators, and hence all \(E_{h,r}\).

**Proof.** With the strict-prefix bound \(r-1\), the exact generating functions are
\[
F(z)=\sum_{r\ge0}C_rz^r=
\frac{z}{(1-z)^4(1-z^2)^2(1-z^3)^2},\quad
N_h(z)=\sum_{r\ge0}T_{h,r}z^r=
F(z)\frac{h z^h}{1-z^h}.
\]
Both are proper rational functions. Their only poles lie at 1, -1, and the two primitive third roots, all sixth roots of unity. The pole at 1 has order 8 for \(F\), 9 for \(N_h\); the others have order at most 2 for \(F\), 3 for \(N_h\). Exact partial fractions therefore give coefficients as finite sums of \(P_\zeta(r)\zeta^{-r}\), with polynomial degree at most 7 or 8 respectively, for **every** \(r\ge0\). There is no polynomial-part transient because the functions are proper. Since each \(\zeta^{-r}\) is constant when \(r=a+6n\), restriction to a class yields a polynomial of the asserted degree. Newton forward interpolation proves the boxed identities for all \(n\). QED.

An independent combinatorial identity is
\[
\boxed{\frac{T_{h,r}}h=\sum_{\ell\ge1} C_{r-\ell h},\qquad C_t=0\ (t\le0).}
\]
Count a marked occurrence \(k_{j(h)}\) by its \(k_{j(h)}\) positive thresholds; deleting \(\ell\) copies leaves precisely the population at budget \(r-\ell h\). Thus \(M_{h,r}=T_{h,r}/h=C_{r-h}+M_{h,r-h}\).

## Theorem B — simultaneous cyclotomic phase at order six

Set \(\rho_3(r)=2\) for \(r\equiv0\pmod3\), and \(\rho_3(r)=-1\) otherwise. Let \(H_{h,6}(r)=\sum_{j=0}^6 a_{h,j}r^{-j}\) be the smooth \(z=1\) contribution to the mean, with exact coefficients:

| Marked h | a0, a1, a2, a3, a4, a5, a6 |
|---|---|
| 1 | 1/8, 1/4, -77/48, 77/8, -7189/96, 10479/16, -1179983/192 |
| 2 | 1/8, -1/4, 7/48, -7/8, 959/96, -1869/16, 259693/192 |
| 3 | 1/8, -3/4, 49/16, -147/8, 4473/32, -19089/16, 700091/64 |

Then, uniformly as integers \(r\to\infty\),
\[
\boxed{
E_{h,r}=H_{h,6}(r)+
\frac{P_h(-1)^r+Q_h\rho_3(r)}{r^6}+O(r^{-7}),
}
\]
where
\[
(P_1,P_2,P_3)=\frac{2835}{32}(1,-3,1),\qquad
(Q_1,Q_2,Q_3)=\frac{280}{3}(1,1,-3).
\]

**Proof.** For the two sources of each weight 2 and 3, the pole multiplicity at -1 and each primitive third root is \(m=2\), while \(d=7\) and \(W=\prod_i s_i=36\). The strict-prefix Laurent constants are
\[
A_{-1}=-\frac{1}{2(2\cdot2)2^5}=-\frac1{256},\quad
A_\omega=A_{\omega^2}=
\frac{\omega}{9(1-\omega)^4(1-\omega^2)^2}
=-\frac1{243}.
\]
The second identity uses \(1+\omega+\omega^2=0\) and \((1-\omega)(1-\omega^2)=3\). By the proved leading-pole coefficient formula of R749SQQ, a marked source whose weight is **not** divisible by the root order has coefficient \(-7! W A_\zeta/(8\cdot1!)=-22680A_\zeta\). If the marked weight **is** divisible, its coefficient is \(7!W A_\zeta(8-2)/(8\cdot2!)=3\cdot22680A_\zeta\), exactly -3 times the former. This gives parity amplitude \(22680/256=2835/32\), and cubic amplitude \(22680/243=280/3\) per root. The two primitive roots sum to \(\omega^{-r}+\omega^{-2r}=\rho_3(r)\). Rational partial fractions yield the uniform remainder and the displayed coefficients follow by rational Taylor expansion, coefficient extraction, and series division at \(z=1\). QED.

## Four instantaneous phase values; six states with one future shift

For the marked unit source let \(f(r)=P_1(-1)^r+Q_1\rho_3(r)\). Its exact values on \(r\bmod 6=0,\ldots,5\) are
\[
\boxed{(f(0),f(1),f(2),f(3),f(4),f(5))
=\frac1{96}(26425,-17465,-455,9415,-455,-17465).}
\]
These are **four** distinct instantaneous outputs: classes 1 and 5 coincide; classes 2 and 4 coincide. However the pairs \((f(r),f(r+1))\) are
\((a,b),(b,c),(c,d),(d,c),(c,b),(b,a)\), where \(a,b,c,d\) denote the four distinct values. All six pairs are different. Thus **one subsequent unit budget increment is enough to distinguish all six phase classes**. The minimal deterministic quotient preserving the observer under every future \(r\mapsto r+1\) is therefore \(\mathbb Z/6\mathbb Z\). It is not the four-class instantaneous quotient. This future shift is an auxiliary budget operation, not a heartbeat time update.

The three marked observations have periodic vector
\[
\frac1{r^6}\left[
\frac{2835}{32}(-1)^r(1,-3,1)
+\frac{280}{3}\rho_3(r)(1,1,-3)
\right].
\]
Hence observer-specific linear combinations compress differently **at order six**, after subtracting their corresponding smooth expansions:
- \(E_1+E_2/3\): parity cancels; nonzero least period 3.
- \(E_1+E_3/3\): cubic part cancels; nonzero least period 2.
- \(2E_1+E_2+E_3\): both order-six cyclic contributions cancel. In this particular linear combination, **all-order** cancellation is established by Theorem C below.

This supplies a constructive separation between the minimal carrier for one immediate read and the minimal carrier for a declared family of future operations. It does not assert native spatial dimension, signed-force cancellation, or an implementation of typed BRC.

## Theorem C — Exact all-order slack-source conservation

The sixth-order cancellation above is the shadow of a substantially stronger identity: for **every** integer \(r\ge1\),

\[
\boxed{4T_{1,r}+2T_{2,r}+2T_{3,r}=(r-1)C_r,\qquad
2E_{1,r}+E_{2,r}+E_{3,r}=\frac{r-1}{2r}.}
\]

**Combinatorial proof.** Adjoin the uniquely determined nonnegative slack variable
\(q=r-1-\sum_i s_i k_i\). The resulting configurations satisfy exactly
\[
q+k_1+k_2+k_3+2(k_4+k_5)+3(k_6+k_7)=r-1.
\]
This equation is symmetric under permutations of the **four** weight-one variables \(q,k_1,k_2,k_3\). Their total first moments are therefore identical. The two weight-two variables have equal first moments, as do the two weight-three variables. Summing the displayed equation over every configuration gives \((r-1)C_r=4T_{1,r}+2T_{2,r}+2T_{3,r}\). Division by \(2rC_r\) yields the mean identity for all \(r\ge1\), including the boundary \(r=1\). QED.

**General form.** For any finite labeled positive-integer source alphabet with \(m_1\ge1\) weight-one labels and \(m_w\) labels of each other weight \(w\), choose one marked source of each distinct weight and set \(T_{w,r}=w\sum_{\Omega_r}k_{j(w)}\). The same slack-variable symmetry gives the exact invariant
\[
\boxed{(m_1+1)T_{1,r}+\sum_{w>1}m_w T_{w,r}=(r-1)C_r.}
\]
It follows directly from conservation of weighted budget; no analytic asymptotics, special multiplicities or cyclotomic expansions are needed.

The composite observer \(2E_1+E_2+E_3\) is consequently an exact function of \(r\) alone and has **no** periodic source residual at any order. Individual marked observers still have the nonzero independent order-2 and order-3 root phases of Theorem B. This establishes an exact, constructive distinction between information lost in a selected observer and information retained by a richer observer family.

## Computational certificate and limits

Run R749SQR_SIX_PHASE_SOURCE_OBSERVER_CERT.py with Python 3.10+ (standard library only). Exact integer/Fraction arithmetic returns PASS for the full grid \(0\le r\le8005\), 24,015 marked-deletion identities, 8,005 exact slack-source conservation identities, 60 independently enumerated populations, 32,024 Newton reconstruction equalities, 21 rational smooth-coefficient checks, two amplitude equalities and four phase-class checks. The companion JSON includes reconstruction coefficients and scaled exact rational samples displayed to nine decimal places. Finite tests corroborate the derivation; the **all-r** assertions follow from the preceding partial-fraction proof.

**Next:** classify **all** independent all-precision linear conservation relations among marked-source observers for general weights; generalize minimal shift-faithful states to arbitrary allowed future-operation semigroups and marked observer families; determine whether any typed BRC-provenance-preserving lift exists.

Current mathematical status: AUTHOR_EXACT_NOT_REVIEWED. No shared X6 CLAIM, Result, review or native Port correspondence is asserted.