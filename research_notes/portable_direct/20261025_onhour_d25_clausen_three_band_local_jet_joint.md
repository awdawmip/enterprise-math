# D25/LIFT — exact three-band Clausen jet and signed reflected joint obstruction

2026-10-25 · TASK_RESEARCH · **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Original task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. This is author-side evidence, **not** a native checkpoint, Result, review, accepted theorem or original benchmark. Consumes already-proved signed Clausen cutoff (cefbad99f03e3b79e0cfc9de624481ed2010ae40) and full-band reflected carrier (616b2a66a6a4071368d83aa6be45156ff0da5376). No frozen object or rank was changed.

## Exact product proof (all primes p=6m+1 >=7)

Let \(r_n=(1/6)_n(1/3)_n/[2^n(n!)^2]\), \(M=\sum_{n=0}^{p-1}r_n\), \(N=\sum_{n=0}^{p-1}nr_n\). All expressions are in the p-local rationals, and every displayed denominator is a p-unit. Write \(H_a=\sum_{k=1}^a1/k\), \(H_a^{(2)}=\sum_{k=1}^a1/k^2\), with both zero at a=0.

For \(0\le n\le m\), define
\[
b_n=2^{-n}\binom mn\binom{2m}n,\quad
e_n=-\frac{H_m-H_{m-n}}6-\frac{H_{2m}-H_{2m-n}}3,
\quad
j_n=-\frac{H_m^{(2)}-H_{m-n}^{(2)}}{36}-\frac{H_{2m}^{(2)}-H_{2m-n}^{(2)}}9.
\]
Exactly \(r_n=b_n\prod_{i=0}^{n-1}(1-p/[6(m-i)])(1-p/[3(2m-i)])\). Taking the quadratic product jet gives
\[
\boxed{r_n\equiv b_n[1+pe_n+\tfrac{p^2}{2}(e_n^2+j_n)]\pmod{p^3}}. \tag{1}
\]

For \(m<n\le 2m\), remove the *one exact factor p* at i=m, and define
\[
h_n=\frac{(-1)^{m+n}m!(n-m-1)!(2m)!}{6\cdot2^n(2m-n)!(n!)^2},
\quad f_n=\frac{H_{n-m-1}-H_m}6-\frac{H_{2m}-H_{2m-n}}3.
\]
The remaining exact product is
\[
r_n=ph_n\prod_{\substack{0\le i<n\\i\ne m}}(1+p/[6(i-m)])
\prod_{i=0}^{n-1}(1+p/[3(i-2m)]),
\]
hence
\[
\boxed{r_n\equiv ph_n(1+pf_n)\pmod{p^3}}. \tag{2}
\]

For \(2m<n<p\), remove the two exact p-factors at i=m,2m. Define
\[
g_n=\frac{(-1)^m m!(n-m-1)!(2m)!(n-2m-1)!}{18\cdot2^n(n!)^2};
\qquad \boxed{r_n\equiv p^2g_n\pmod{p^3}}. \tag{3}
\]
These formulas prove valuation-at-least-three errors, not just sample fits.

## Shared reflected bulk and cutoff ports

Reuse the established reflected recurrence \(v_1=1/10\), \(v_{a+1}=v_a36a^2/[(6a+5)(3a+2)]\pmod p\) for \(a<4m\), with \(v_a\equiv r_{p-a}/p^2\pmod p\). Set \(V_j=\sum_{a=1}^jv_a\), \(J_j=\sum_{a=1}^jav_a\). Exact rank reflection gives
\[
\boxed{\sum_{n=2m+1}^{p-1}g_n\equiv V_{4m}\pmod p}. \tag{4}
\]
Keep separately the already-proved signed cutoff
\[
Q=\sum_{\substack{i,k<p\\i+k\ge p}}(6(i+k)+1)r_ir_k,\qquad
\boxed{Q/p^2\equiv T=2\sum_{j=1}^m b_j[(6j+1)V_j-6J_j]\pmod p}. \tag{5}
\]

Set
\[
\begin{aligned}
L_0&=\sum_{0\le n\le m}b_n,&
L_1&=\sum_{0\le n\le m}b_ne_n+\sum_{m<n\le2m}h_n,\\
L_2^{lo}&=\tfrac12\sum_{0\le n\le m}b_n(e_n^2+j_n),&
L_2^{mid}&=\sum_{m<n\le2m}h_nf_n,\\
D_0&=\sum_{0\le n\le m}nb_n,&
D_1&=\sum_{0\le n\le m}nb_ne_n+\sum_{m<n\le2m}nh_n.
\end{aligned}
\]
Sum equations (1)-(4) to obtain the **unconditional exact-precision theorem**
\[
\boxed{M\equiv L_0+pL_1+p^2(L_2^{lo}+L_2^{mid}+V_{4m})\pmod{p^3}},
\quad
\boxed{N\equiv D_0+pD_1\pmod{p^2}}. \tag{6}
\]
The second precision suffices for W modulo p^3 **only when M=0 mod p**; for split primes with M a unit, do not silently use the truncated N.

## Original third-digit joint certificate (explicitly conditional)

The original weighted sum obeys the previously established *exact* cutoff identity
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=M(M+12N)-Q.
\]
When \(L_0\equiv0\pmod p\), define \(U_0=L_0/p+L_1\in\mathbf Z_{(p)}\). **Additionally assuming** the accepted first-digit premise \(W_p\equiv p\pmod{p^2}\), the following quotient is legal, and there is an exact equivalent obstruction:
\[
\boxed{\begin{aligned}
\frac{W_p-p}{p^2}\equiv{}&
\frac{12U_0D_0-1}{p}+U_0^2+12U_0D_1\\
&+12D_0(L_2^{lo}+L_2^{mid})
+\underbrace{12D_0V_{4m}-T}_{\text{shared reflected bulk/cutoff, distinct signed ports}}
\pmod p.
\end{aligned}} \tag{7}
\]
The proof substitutes (5)-(6) into exact Clausen and expands \(M=pU_0+p^2(L_2^{lo}+L_2^{mid}+V_{4m})\). It does **not** prove target-class \(L_0\) vanishing or vanishing of the RHS for all p=13,19 mod24.

An exact finite warning against false cancellation: for p=19, \((D_0,U_0,L_2^{lo},L_2^{mid},V_{4m},T)\equiv(1,8,3,18,10,12)\pmod{19}\). Dropping the low second jet changes the third digit by 17, and dropping the middle first jet changes it by 7 modulo 19, despite full \(W_{19}\equiv19\pmod{19^3}\). At p=13 both local jets happen to vanish, but the reflected high-band 8 still matters. These refute shortcut methods, **not** the original D25 conjecture.

## Verification and source recovery

Independent original r_n/W_n modular recurrences, factorial/harmonic jets and reflected boundary passed 95 primes p=1 mod6 (94 through 1200 plus 19963), including 53 target primes; full term-by-term comparisons passed 26 primes including 19963. No floating point. In 51/53 target cases, combined 12D_0L_2 is nonzero, and in 52/53 cases 12U_0D_1 is nonzero. Sample (p, low L2, middle L2, V4m, T, total 12D0L2): (13,0,0,8,0,9), (19,3,18,10,12,11), (211,152,9,130,119,19), (19963,16929,4842,7392,13363,10178). Local full proof and executable checker are preserved separately.

**Remaining mother goal:** prove/deny target-class L0=0 mod p and joint RHS (7)=0 mod p with a true CM/finite-field/formal-adjoint certificate, not individually assumed auxiliary cancellations. Original frozen Delta_p-R_p and native Hasse/[X]U, kappa, Frobenius direction, benchmark and independent Driver review are still pending.

**Operations:** Research conversation chatgpt-research-onhour-enterprise-math-20260923 is distinct from maintenance chatgpt-hourly-enterprise-math-20260921. Current Site reports no Researcher write authority; direct exact continuation for this run returned CONTROL_QUOTA. Original service session/CLAIM/run and prior receipts not positively recovered. This neutral author note is not a Source checkpoint; do not invent or replay permission-gated actions. No scheduler/notification changes.
