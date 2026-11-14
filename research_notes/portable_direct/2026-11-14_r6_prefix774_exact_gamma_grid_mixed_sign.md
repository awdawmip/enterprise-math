# PREFIX-774 / R6 — Exact mixed-difference phase in a rational 1/768 Gamma square

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: \`AUTHOR_EXACT_INTEGER_GRID_WITNESS / UNREVIEWED / NOT_ADMITTED\`.
Scope: the **external** 189-layer killed-Pascal first-stop / independent two-Gamma-clock auxiliary model. This note proves a finite rectangular mixed-difference sign in the auxiliary parameter square. It does not change the historical original 1/768 comparator exclusion count or claim native X6 transfer.

## 1. Model and exact moment identities

Let \(T_x\le 189\) be the frozen first-stop layer and \(S_i(x)=\Pr(T_x>i)\), \(0\le i\le188\). Given \(T_x=m\), let \(C_x\sim\operatorname{Gamma}(m,1)\), with two independent clocks conditioned on their respective first-stop layers. Write

\[
Y(p,z)=\max(C_p,C_z),\quad
\mu(p,z)=\mathbb E[Y(p,z)],\quad W(p,z)=\operatorname{Var}(Y(p,z)),
\quad V_q(p,z)=q^2W(p,z)-q\mu(p,z).
\]

Set \(s(x)=(S_0(x),\ldots,S_{188}(x))^\top\) and

\[
K_{ij}=\frac{\binom{i+j}{i}}{2^{i+j+1}},
\qquad L_{ij}=(i+j+1)K_{ij}.
\]

The exact survival identity is

\[
\Pr(Y>t)=H_p(t)+H_z(t)-H_p(t)H_z(t),\quad
H_x(t)=e^{-t}\sum_{i=0}^{188}S_i(x)\frac{t^i}{i!}.
\]

Termwise integration of these finite Erlang sums yields

\[
\mu(p,z)=\sum_i s_i(p)+\sum_i s_i(z)-s(p)^\top K s(z),
\]

\[
M_2(p,z)=\mathbb E[Y^2]
=2\sum_i(i+1)s_i(p)+2\sum_i(i+1)s_i(z)
-s(p)^\top Ls(z),\quad W=M_2-\mu^2.
\]

In particular, the mixed contribution to \(M_2\) is \(L\), since
\[
2\int_0^\infty t\,e^{-2t}\frac{t^{i+j}}{i!j!}\,dt
=\frac{(i+j+1)\binom{i+j}{i}}{2^{i+j+1}}=L_{ij}.
\]

## 2. Theorem 774.1 — exact phase switch on one 1/768 square

Fix \(a=38/768\), \(b=39/768\). For any bivariate \(F\), define its square mixed difference by

\[
\Delta_R F=F(b,b)-F(a,b)-F(b,a)+F(a,a),
\qquad R=[a,b]\times[a,b].
\]

The attached pure-standard-library integer verifier reconstructs all 189 survivor rows from the frozen killed-Pascal width predicate. The first 189 rows contain exactly 9,529 nonzero survivor positions and row 189 is empty. It evaluates the four corners (three distinct by symmetry) using exact rational numerators.

The exact integer comparisons prove
\[
\boxed{\Delta_R\mu<0,\qquad \Delta_R W<0.}
\]

Consequently \(q_R=\Delta_R\mu/\Delta_R W\) is strictly positive. The exact integer cross-products further establish

\[
\boxed{\frac{2852034258349}{10^{14}}
<q_R<
\frac{2852034258350}{10^{14}}}.
\]

For **every real \(q>0\)**, the identity

\[
\Delta_RV_q=q\left(q\Delta_RW-\Delta_R\mu\right)
=q\,\Delta_RW\,(q-q_R)
\]

therefore gives the complete rectangular sign classification:

\[
\boxed{\begin{aligned}
0<q<q_R&\implies\Delta_RV_q>0,\\
q=q_R&\implies\Delta_RV_q=0,\\
q>q_R&\implies\Delta_RV_q<0.
\end{aligned}}
\]

In particular, \(2>q_R\) and \(\Delta_RV_2<0\) strictly.

Display-only decimals, rounded from exact integer fractions:

\[
\begin{aligned}
\Delta_R\mu&\approx -0.00493294208071696916036,\\
\Delta_RW&\approx -0.17296223095063648040537,\\
q_R&\approx 0.02852034258349057517836,\\
\Delta_RV_2&\approx -0.68198303964111198330078.
\end{aligned}
\]

## 3. Finite certificate and validation scope

The survivor width predicate is the exact integer inequality

\[
40(n+1)\binom nk\,x^k(2^{18}-x)^{n-k}>(2^{18})^n
\]

with the frozen quartile-width decision; no numerical probability threshold is used. For the rational parameters with denominator \(768\), the common survivor denominator is \(E=768^{188}\). With the common kernel denominator \(T=2^{377}\) and \(H=E^2T>0\), the code computes integer numerators \(\mu_{\rm num},M_{2,\rm num}\) over \(H\) and

\[
W_{\rm num}=M_{2,\rm num}H-\mu_{\rm num}^2
\]

over \(H^2\). All corner variances, two negative mixed differences, the strict rational interval for \(q_R\), and the sign at \(q=2\) are checked by integer assertions.

Reproduce using

\`python3 research_notes/portable_direct/PREFIX774_R6_EXACT_GAMMA_GRID_WITNESS.py\`.

The companion JSON saves the sign results and display-only ratios. The author's local calculation passed its assertions and the three published scientific files were separately read back from immutable GitHub commits. These data concern exactly this external auxiliary square; they do not count any new excluded cell in the original comparator experiment. Independent scientific review and broader continuous-region certification remain open.

## 4. Relation to PREFIX-773 and next frontier

The diagonal stationary point isolated by PREFIX-773 near \(u=0.05029714515369\) lies strictly inside \(R\). This square's rational switching value is larger than the PREFIX-773 certified *diagonal local minimum*, which is consistent with the strict local structure.

The next useful work is to certify additional two-dimensional off-diagonal and boundary boxes with exact interval/Bernstein arithmetic, determine whether any point improves the diagonal minimum, and test the sign-certificate pipeline on original unresolved comparator cells with their original predicates. Shared Task claims remain governed by a fresh canonical Owner receipt.
