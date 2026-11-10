# PREFIX-668-R6 — Coupled-block Bernstein curvature doubles the certified BRC variance strip again

Date: 2026-11-10 (Asia/Shanghai). Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Subject: the unchanged 189-layer, two-direction BRC first-stop *statistical observer* from PREFIX-659–667. Research mode: TASK_RESEARCH, independent direct scientific work; native session/RA completion is separately recorded if its receipt succeeds. Status: AUTHOR_PROVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Statement — a further doubling of the exact certified area

Let \(\mu(p,z)=E[Y]\), \(H(p,z)=E[Y^2]/2\), \(W(p,z)=2H(p,z)-\mu(p,z)^2=\operatorname{Var}(Y)\) and \(V_q=q^2W-q\mu=\operatorname{Var}(T_q)\). For all real
\[
0\le p\le\frac1{64},\qquad
\frac{607}{4096}\le z\le\frac{609}{4096},
\]
we prove
\[
\boxed{\mu>\frac{434}{5}=86.8,\quad
\mu_{pp}>221,\quad H_{pp}<21691,\quad W_{pp}<-15000.}
\]
Consequently for every real \(12\le q\le24\),
\[
\boxed{(V_q)_{pp}=q^2W_{pp}-q\mu_{pp}<-15000q^2.}
\]
Using the **unchanged** verified PREFIX-660 edge \(z_*(q)\) and its gap \(V_q(0,z_*)-V_q(0,z)\ge6400000(z-z_*)^2\), together with the PREFIX-661 edge normal slope \(\partial_p V_q(0,z)<-76650\), the strip's unique maximum is \((0,z_*(q))\), and
\[
\boxed{M_q-V_q(p,z)\ge76650p+7500q^2p^2+6400000(z-z_*(q))^2,}
\qquad M_q=V_q(0,z_*(q)).
\]
This certified strip is twice the area of PREFIX-667, four times PREFIX-666 and 64 times PREFIX-665. The full \([0,1]^2\) global-maximum objective remains open.

## Exact finite source and moment formulas

Let \(A_n(k)\) denote the surviving path multiplicity in the frozen 189-layer recurrence, and set
\[
f_n(k)=\frac{A_n(k)}{\binom nk}\in[0,1],\qquad
s_n(u)=\sum_{k=0}^n A_n(k)u^k(1-u)^{n-k}.
\]
The companion program **reconstructs every layer** from the frozen exact \`wide(n,k)\` predicate in \`PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE.py\`, confirming the first 25 full-survival layers and empty final layer 189. Write \(t_m(z)=s_m(z)\), \(w_{nm}=2^{-(n+m+1)}\binom{n+m}{n}\), and
\[
\begin{aligned}
a_n(z)&=1-\sum_{m=0}^{188}w_{nm}t_m(z),\\
b_n(z)&=n+1-\sum_{m=0}^{188}\frac{n+m+1}{2}w_{nm}t_m(z),\\
\mu(p,z)&=\sum_{n=0}^{188}a_n(z)s_n(p)+\sum_{m=0}^{188}t_m(z),\\
H(p,z)&=\sum_{n=0}^{188}b_n(z)s_n(p)+\sum_{m=0}^{188}(m+1)t_m(z).
\end{aligned}
\]
The weights satisfy \(0\le a_n(z)\le1\) and \(0\le b_n(z)\le n+1\).

## New method — correlate the *same p subinterval* before multiplying

Put \(Q=19/128\), \(\delta=1/4096\), \(\varepsilon=1/64\), \(R=26\). Construct exact signed derivatives
\(D^\mu_r=\partial_p^r\mu(0,Q)\), \(D^H_r=\partial_p^r H(0,Q)\), and the corresponding \(z\)-derivatives, for \(2\le r\le26\). The exact Bernstein forward-difference identity is
\[
s_n^{(r)}(0)=n^{\underline r}\Delta^r f_n(0),
\]
with the universal derivative envelope \(|s_n^{(r)}(p)|\le2^{r-1}n^{\underline r}\). Define the degree-23 *signed* Taylor polynomial for each \(F\in\{\mu,H\}\):
\[
P_F(p)=\sum_{j=0}^{23}\frac{D^F_{j+2}}{j!}p^j.
\]
Its exact uniform remainder is at most
\[
\rho_\mu=\frac{2^{25}\varepsilon^{24}}{24!}
\sum_{n=26}^{188}n^{\underline{26}},\qquad
\rho_H=\frac{2^{25}\varepsilon^{24}}{24!}
\sum_{n=26}^{188}(n+1)n^{\underline{26}}.
\]
For \(n\le188\), the binomial score bound \(|t_n'(z)|<21\) on the whole \(z\)-band yields
\(|a_n'|\le21\), \(|b_n'|\le21(n+1)\);
by the standard variance-bound second-difference estimate,
\(|a_n''|\le2(n+1)(n+2)\) and
\(|b_n''|\le2(n+1)(n+2)(n+3)\).
Let
\[
\lambda_n=\sum_{r=2}^{25}\frac{\varepsilon^{r-2}}{(r-2)!}|s_n^{(r)}(0)|
+\frac{2^{25}\varepsilon^{24}}{24!}n^{\underline{26}}.
\]
The program constructs exact rational budgets
\[
Z_\mu=\sum_n2(n+1)(n+2)\lambda_n,\quad
Z_H=\sum_n2(n+1)(n+2)(n+3)\lambda_n
\]
and signed-jet first-\(z\) bounds \(G_{\mu,z},G_{H,z}\). Thus uniform \(z\)-perturbation errors are
\[
\eta_\mu=\delta G_{\mu,z}+\tfrac12\delta^2Z_\mu,\quad
\eta_H=\delta G_{H,z}+\tfrac12\delta^2Z_H.
\]

Split \([0,\varepsilon]\) into 16 rational intervals \(I_i=[u_i,u_i+h]\). On each, translate the *same* \(P_\mu\) and \(P_H\) to \(t=(p-u_i)/h\in[0,1]\), and compute their degree-23 exact Bernstein control points. For \(P(t)=\sum_{j=0}^{23}c_j t^j\), these are
\[
B_{i,k}=\sum_{j=0}^{k}\frac{\binom{k}{j}}{\binom{23}{j}}c_j,\quad0\le k\le23.
\]
For each \(I_i\), define the **paired local bounds**
\[
L_i=\min_kB^{\mu}_{i,k}-\rho_\mu-\eta_\mu,\qquad
U_i=\max_kB^H_{i,k}+\rho_H+\eta_H.
\]
Bernstein's convex-hull principle ensures simultaneously \(\mu_{pp}(p,z)\ge L_i\) and \(H_{pp}(p,z)\le U_i\) at *each* \(p\in I_i\). The exact global minimum of \(L_i\) is \(>221>0\). Therefore \(\mu_p\) is increasing in \(p\), and the boundary mean and binomial score bounds give \(\mu(p,z)\ge\mu_{\rm floor}>86.8\).

Crucially, form for **each block separately**
\[
U^{W}_i=2U_i-2\mu_{\rm floor}L_i.
\]
Since \(W_{pp}=2H_{pp}-2\mu_p^2-2\mu\mu_{pp}\), on \(I_i\) we have \(W_{pp}\le U_i^{W}\). Taking \(\max_i U_i^W\) *after* pairing rather than combining unrelated global extrema preserves curvature information. This is a strictly stronger certificate than the separate global \(H_{pp}\) and \(\mu_{pp}\) bounds.

## Exact executed evidence

Python 3 standard library, integers and \`Fraction\`, **no floating-point decisions**, gives \`ALL_CHECKS_PASS 18\`. Compact exact rational brackets for the actually computed certificate objects:
\[
\begin{aligned}
86.8&<\mu_{\rm floor}<86.9,\\
221&<\min_i L_i<222,\\
21690&<\max_i U_i<21691,\\
-15403&<\max_i U_i^W<-15402.
\end{aligned}
\]
The companion \`PREFIX668_R6_COUPLED_BLOCK_CERTIFICATE.py\` prints all 16 **full numerator/denominator rational** block-wise bounds, the complete exact signed Taylor remainder and \(z\)-error envelopes, and the precise theorem metadata. \`PREFIX668_R6_RESULTS.json\` contains the compact exact interval certificate, reproduction route and scope. Verification relies on the same pinned path-predicate/maximum-of-Gamma-clocks formulas as PREFIX-665, and the existing PREFIX-660/661 *edge certificates* only for the maximizer/gap corollary.

Independent mathematical replication and formal Source Result/Review admission are pending. This proof establishes a new local continuous region and is not a claim about the complete native X6 world dynamics.

## Next discriminating unit

For \(p\in[1/64,1/32]\), test sharper **bivariate \(p,z\)** Bernstein bounds (especially on \(\partial_{ppzz}\) and the signed \(z\)-variation) instead of the current broad absolute \(Z_\mu,Z_H\) budgets. Current 1/32 attempt using the old \(z\)-envelopes produces a positive block upper bound and therefore remains inconclusive for that larger domain; the failed bound does not disprove curvature. In parallel, begin verified full-triangle interval upper-bound pruning against the existing strongest \(p=0\) variance competitor, retaining exact symmetry and the frozen science pin.
