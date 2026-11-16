# R749SRY — Exact adversarial integer-error decoding without error-cube enumeration

**Date:** 2026-11-16 (Asia/Shanghai). **Review:** AUTHOR_EXACT_NOT_REVIEWED.
**Frozen science:** Walsh auxiliary model at a72226e2430ffa4786321ac86e7f0c599d5f0389; direct continuation of R749SRX (Draft PR #2540, commit c19994d0dcd10261821c79cb29f9118187967a94).
**Scope:** Independent positive labeled-source combinatorics. The six-phase coordinate is an observer in this auxiliary model, not a Heartbeat X6 spatial or time coordinate; no native signed BRC morphism is asserted.

## Fixed model

Fix the weights \(w=(1,1,2,3,6)\), with the first labeled source marked. For integer \(r\ge1\),
\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^5:\sum_iw_ik_i\le r-1\},\quad
C_r=|\Omega_r|,\quad T_r=\sum_{k\in\Omega_r}k_1.
\]
Define
\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}+\frac{115}{6r^3}-\frac{16315}{108r^4},\quad
R(r)=r^3T_r/C_r-r^4H_4(r).
\]
Let \(P=(455,-295,-25,185,-25,-295)/36\), indexed modulo six.
For shifts \(J=(0,1,5)\), the ideal signature is \(S_a=(P_a,P_{a+1},P_{a+5})\).
With integer budget \(M\ge0\), three independent marked-count errors satisfy \(\epsilon_i\in[-M,M]\cap\mathbb Z\), denominator counts being exact. The actual observation is
\[
Y_i=R(r+h_i)+u_i\epsilon_i,\qquad u_i=(r+h_i)^3/C_{r+h_i}>0.
\]
Decode to the unique nearest ideal \(S_a\) in maximum norm (ties count as failures). Define \(N(M)\) as the least integer \(N\ge1\) giving correct decoding for every \(r\ge N\) and every allowed error vector.

## Theorem A — Exact extreme-coordinate feasibility, arbitrary M

For any number \(k\) of independent bounded integer-error coordinates, rational centers \(x_i\), positive rational steps \(u_i>0\), and two signatures \(S_a,S_b\), write
\(x_i=R(r+h_i)-(S_a)_i\) and \(\Delta_i=(S_b)_i-(S_a)_i\).
A rival signature \(b\ne a\) ties or beats \(a\) for some \(\epsilon\in[-M,M]^k\cap\mathbb Z^k\) **if and only if** there are \(j\in\{1,\ldots,k\}\) and \(\sigma\in\{-1,1\}\) with
\[
\epsilon_j=\sigma M,\quad t=\sigma(x_j+u_j\sigma M)\ge0,\quad
0\le\sigma\Delta_j\le2t,
\]
and for each \(i\ne j\) the integer interval
\[
\left[\max\left(-M,\left\lceil\frac{L_i-x_i}{u_i}\right\rceil\right),
\min\left(M,\left\lfloor\frac{U_i-x_i}{u_i}\right\rfloor\right)\right]\cap\mathbb Z
\]
is nonempty, where \(L_i=\max(-t,\Delta_i-t)\) and \(U_i=\min(t,\Delta_i+t)\).
Thus the full \((2M+1)^k\) cube is decided by at most \(2k\) extreme-coordinate candidates, each requiring \(k-1\) independent exact rational interval tests.

**Proof.** Failure means
\[
\max_i|x_i+u_i\epsilon_i-\Delta_i|
\le\max_i|x_i+u_i\epsilon_i|=:t.
\]
Choose \(j\) attaining the right maximum and its sign \(\sigma\) (either if zero). The rival condition
\(|\sigma t-\Delta_j|\le t\) is \(0\le\sigma\Delta_j\le2t\).
Replace \(\epsilon_j\) with \(\sigma M\), leaving other errors unchanged. Since \(u_j>0\), the new \(t'=\sigma(x_j+u_j\sigma M)\ge t\), preserving the rival condition at \(j\). Other coordinates still have true and rival deviations at most \(t\le t'\). This produces the endpoint witness. Conversely, the specified intervals independently choose allowed integer errors for all \(i\ne j\) keeping both deviations at most \(t\); at \(j\), the true deviation is exactly \(t\) and the rival deviation at most \(t\). Hence the rival ties or beats the truth. QED.

The compression is exact for the chosen observer and future nearest-signature decision. It makes no assertion about source labels or joint provenance under other operations.

## Theorem B — Rigorous infinite-tail control

In this five-source model,
\[
\boxed{0<R(r)-P_{r\bmod6}<1600/r\quad(r\ge516).}
\]
Also
\[
\boxed{C_r\ge r^5/(5!\prod_iw_i)=r^5/4320\quad(r\ge1).}
\]
Indeed the simplex \(\{x_i\ge0:\sum_iw_ix_i<r\}\) is covered by half-open unit cubes indexed by \(k_i=\lfloor x_i\rfloor\in\Omega_r\), giving the volume comparison.

The exact rational generating functions are
\[
\sum_{r\ge1}C_rz^r=\frac z{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{r\ge1}T_rz^r=\frac {z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
They yield period-six quasipolynomials of degrees at most five and six for \(r\ge36\).
For each \(a=0,\ldots,5\) set \(r=516+a+6n\), \(n\ge0\). Exact interpolation gives polynomials \(C_a(n),T_a(n)\), then define
\[
Q_a(n)=r^3T_a(n)-C_a(n)[r^4H_4(r)+P_a].
\]
The degree of \(Q_a\) is four and all its coefficients are strictly positive. Every coefficient of the degree-five polynomial \(1600C_a(n)-rQ_a(n)\) is also strictly positive. The accompanying exact Fraction program reconstructs and checks all six cases, including out-of-sample interpolation checks. Thus \(0<Q_a/C_a<1600/r\).

Leading coefficients of \(Q_a\) and \(1600C_a-rQ_a\), in phase order:
\[
(667/2,879),\ (1378/3,124),\ (2569/6,311),\
(374,636),\ (2297/6,583),\ (1298/3,284).
\]
All lower coefficients are checked by the executable certificate. The six ideal signatures have minimum pairwise maximum-norm separation \(15/2\), so
\[
\|Y-S_{r\bmod6}\|_\infty\le1600/r+4320M/r^2.
\]
If that bound is strictly below \(15/4\), the true signature is uniquely nearest.

For every integer \(M\ge0\), this yields a terminating **exact global algorithm**:
take any integer \(B(M)\ge516\) satisfying
\[
1600/B(M)+4320M/B(M)^2<15/4
\]
and compute
\[
\boxed{N(M)=1+\max\bigl(\{r\in[1,B(M)-1]:
\text{Theorem A detects failure at }r\}\cup\{0\}\bigr).}
\]
Theorem A quantifies every integer error vector exactly; Theorem B proves correctness for the infinite tail.

## Corollary — All 301 global budgets M=0,...,300

Set \(B=900\). For every \(M\le300\),
\[
1600/900+4320\cdot300/900^2=152/45<15/4
\]
with strict margin \(67/180\).
For each \(1\le r<900\), the certificate binary-searches the least budget producing failure by Theorem A. Failure is monotone in M, hence the completed scan yields **global** \(N(M)\) for all 301 integer budgets.

| M | 0 | 1 | 2 | 3 | 10 | 32 | 50 | 100 | 200 | 300 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N(M) | 35 | 53 | 65 | 73 | 125 | 219 | 273 | 387 | 549 | 669 |

The results JSON records the full 301-value sequence and exact adversarial witnesses at \(r=N(M)-1\).
The known predecessor thresholds \(N(0)=35,N(1)=53,N(2)=65\) are reproduced. Across 297 \((r,M)\) cases (\(r=1,\ldots,99\), \(M=0,1,2\)) an independent complete enumeration of the small error cubes agrees with the interval test. All arithmetic uses Python standard-library Fraction and integers. Certificate result: PASS.

## Provenance, scope, further questions

Mathematical status: AUTHOR_EXACT_NOT_REVIEWED. Frozen source pin a72226e2430ffa4786321ac86e7f0c599d5f0389 and the earlier R749SRX first-order threshold asymptotic are unchanged.
The current positive combinatorial observer is not retyped as native signed BRC, a six-axis spatial coordinate, or physical time. Future research can seek the exact bounded oscillatory correction to \(N(M)-24\sqrt{2M}\), improve finite budget complexity, allow coupled denominator and numerator errors, and construct an explicitly typed BRC source-port interface preserving labels, phases and joint relations.
