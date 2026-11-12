# PREFIX-721-R6 — 71-fold wider Gamma wedge and a local no-maximizer theorem

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675; predecessor: PREFIX-720. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Scope: auxiliary two-parameter BRC stopping-count / Gamma completion-clock observer, **not native X6 spatial dynamics**. Evidence: AUTHOR_EXACT_INTEGER_RECOMPUTED / UNREVIEWED / NOT_ADMITTED.

## 1. Main theorem

Let \(D=[0,1/2]^2\) and \(Y(p,z)=\max(T_p,T_z)\), where the independent completion clocks obey the original frozen 189-level count law and conditional Gamma distributions. Define
\[
\mu=E[Y],\quad M_2=E[Y^2],\quad
W=M_2-\mu^2,\quad f_t=W-t\mu,\quad V_q=q^2 f_{1/q}.
\]
Let
\[
x_0=\frac{11}{96},\quad \varepsilon=\frac{1}{14\,000\,000\,000},\quad
J(p,z)=\mu_p(M_2)_z-\mu_z(M_2)_p=(z-p)K(p,z).
\]
On the *entire closed square*
\[
S_\varepsilon=\{(p,z):|p-x_0|\le\varepsilon,\ |z-x_0|\le\varepsilon\}
\subset\operatorname{int}(D)
\]
the strict rational bound
\[
\boxed{K(p,z)>2\,000\,000}
\]
holds. In particular \(J(p,z)>2\,000\,000(z-p)\) when \(p<z\) and \(J(p,z)<-2\,000\,000(p-z)\) when \(p>z\).

**Maximizer exclusion.** For **every real \(t\)**, the full two-parameter function \(f_t\) has **no local or global maximizer anywhere in \(S_\varepsilon\)**. This covers all real \(q>0\) through the positive scaling \(V_q=q^2 f_{1/q}\). The radius is \(500/7\) times the prior \(10^{-12}\) radius. This local geometric exclusion is recorded separately from the earlier grid-witness area proportion; it is not added to that proportion without a non-overlap check.

## 2. Exact original Gamma kernel

For \(0\le n\le188\), let \(s_n(p)=\Pr(N_p>n)\) be the frozen survivor tails. The independent Gamma-clock kernel is
\[
C_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}}.
\]
Consequently
\[
\mu(p,z)=\sum_n\left(s_n(p)+s_n(z)\right)
-\sum_{n,m}C_{nm}s_n(p)s_m(z),
\]
\[
M_2(p,z)=2\sum_n(n+1)(s_n(p)+s_n(z))
-\sum_{n,m}(n+m+1)C_{nm}s_n(p)s_m(z).
\]
These finite rational polynomials are symmetric in \(p,z\). Thus \(J(z,p)=-J(p,z)\), the polynomial \(J\) is divisible by \(z-p\), and
\[
K(p,z)=\int_0^1 J_z(p,p+u(z-p))\,du .
\]
The old PREFIX-720 exact integer kernel supplies the definitions \(L=768^{188}\), \(Z=2^{377}\), \(d=L^2Z\), and the integers \(P,Q,PP,QQ,C_0,C_1\). With \(x_0=88/768\), the companion checker recomputes all 189 frozen rows, exactly 9,529 nonzero survivor coefficients, and certifies
\[
J_z(x_0,x_0)
=\frac{P(QQ+C_1)-Q(PP+C_0)}{d^2}
>\boxed{40\,800\,000}.
\]
Its exact floor is 40,818,717. Both the sign comparison and the decimal-integer regression hash are checked, so the hash is not used as a substitute for mathematical evidence.

## 3. Sharpened Bernstein derivative lemma

The frozen survivor polynomials have the Bernstein form
\[
s_n(p)=\sum_{k=0}^n \binom nk g_{n,k}p^k(1-p)^{n-k},
\qquad 0\le g_{n,k}=\frac{v_{n,k}}{\binom nk}\le1.
\]
For every integer \(r\ge1\), the alternating finite difference satisfies
\[
|\Delta^r g_{n,k}|\le2^{r-1}
\]
because its positive and negative binomial-coefficient groups each sum to \(2^{r-1}\). The Bernstein derivative identity yields, for \(1\le r\le3\),
\[
|s_n^{(r)}(p)|\le 2^{r-1}(n)_r
\le\frac{376^r}{2}
\quad (0\le p\le1,\ n\le188).
\]
In the Gamma moment formulas, the nonnegative influence coefficients satisfy \(0\le A_n\le1\), \(0\le H_n\le2(n+1)\) and the full Gamma kernel row sums satisfy
\[
\sum_m C_{nm}=1,\qquad \sum_m(n+m+1)C_{nm}=2(n+1).
\]
Therefore for each positive-order *pure or mixed* partial derivative of total order \(r\le3\):
\[
|D^\alpha\mu|\le\frac{N}{2}376^r,\qquad
|D^\alpha M_2|\le\frac{N(N+1)}{2}376^r,
\quad N=189.
\]
In the mixed case, both survivor factors are differentiated and the stronger \(1/4\) factor is available; the displayed \(1/2\) bound remains valid.

Each Leibniz summand in \(J_{zp}\) or \(J_{zz}\) consists of two **positive-order** differentiated moment factors, with derivative orders summing to four. Accounting for all eight Leibniz terms gives
\[
|J_{zp}|,\ |J_{zz}|
\le 2N^2(N+1)376^4.
\]
The integral identity for \(K\) and the mean-value theorem consequently yield, throughout the radius-\(\varepsilon\) square,
\[
|K(p,z)-J_z(x_0,x_0)|\le B\varepsilon,\qquad
B=4N^2(N+1)376^4
=\boxed{542610983324712960}.
\]
An entirely integer comparison verifies
\[
40\,800\,000-
\frac{542610983324712960}{14\,000\,000\,000}
>2\,000\,000 .
\]
Thus the claimed bound follows. The method also proves \(K>0\) for any rational \(0<\varepsilon<40\,800\,000/B\) whose square lies in \(D\).

## 4. Diagonal stationary points have positive transverse curvature

The first derivatives factor as
\[
f_{t,p}=\mu_p(R_p-2\mu-t),\quad
f_{t,z}=\mu_z(R_z-2\mu-t),\quad
R_p=\frac{(M_2)_p}{\mu_p},\quad
R_z=\frac{(M_2)_z}{\mu_z}.
\]
The original frozen survivor positivity ensures \(\mu_p,\mu_z>0\) in the interior. Every off-diagonal stationary point must have \(R_p=R_z\), hence \(J=0\), impossible inside \(S_\varepsilon\).

If a diagonal point \((x,x)\) is stationary, symmetry gives \(R_p=R_z=2\mu+t\). Direct differentiation and cancellation give the exact transverse Hessian identity
\[
\left.\frac{d^2}{ds^2}f_t(x+s,x-s)\right|_{s=0}
=2(f_{t,pp}-f_{t,pz})
=\boxed{\frac{2J_z(x,x)}{\mu_p(x,x)}}>0.
\]
Thus no diagonal stationary point in the square can be a local maximum. Every point of \(S_\varepsilon\) lies inside \(D\), so the two cases prove the no-maximizer theorem for the full parameter domain.

This explains a distinction relevant to PREFIX-719: an extreme point of the *diagonal restriction* can still have a direction of increasing value in the two-parameter problem.

## 5. An explicit exact saddle and its curvature signs

Let
\[
t_0=\frac{(M_2)_p(x_0,x_0)}{\mu_p(x_0,x_0)}
-2\mu(x_0,x_0),\qquad q_0=1/t_0.
\]
The exact computation proves \(\tfrac14<t_0<\tfrac13\), i.e. \(3<q_0<4\); the rational point \((x_0,x_0)\) is stationary for \(f_{t_0}\). It also proves
\[
280<\mu_p(x_0,x_0)<300,\quad
\Theta'(x_0)<-100,\quad
J_z(x_0,x_0)>40\,800\,000,
\]
where \(\Theta(x)=R_p(x,x)-2\mu(x,x)\). Hence the directional curvatures of \(f_{t_0}\) are
\[
\left.\frac{d^2}{ds^2}f_{t_0}(x_0+s,x_0+s)\right|_0
=2\mu_p\Theta'<-56\,000,
\]
\[
\left.\frac{d^2}{ds^2}f_{t_0}(x_0+s,x_0-s)\right|_0
=\frac{2J_z}{\mu_p}>272\,000.
\]
The specified point is therefore an exact saddle for the auxiliary objective, with \(q_0\) in the actual \(q\ge2\) research range.

## 6. Reproduction, evidence scope and continuation

Run the new \`PREFIX721_R6_SHARP_BERNSTEIN_WEDGE.py\` beside the existing \`PREFIX720_R6_LOCAL_TRANSVERSALITY_CHECKER.py\`. The code executes the frozen 189-row integer kernel, recomputes all necessary exact signs, validates the \(K\) Lipschitz bound, saddle parameter, and curvatures, and writes \`PREFIX721_R6_RESULTS.json\`. Author's local execution: **ALL_CHECKS_PASS PREFIX721-R6**. The parent integer numerators' SHA-256 digests remain in the result JSON as reproducibility identifiers. No remote CI or independent mathematical review is asserted.

Parent scientific source: [PREFIX-720 manuscript](https://github.com/awdawmip/enterprise-math/blob/99f89db754940a747c02dee12f246b65d524959c/research_notes/portable_direct/2026-11-12_r6_prefix720_gamma_diagonal_transverse_wedge.md); parent checker blob SHA-1: c0c25c090ae5035853d1cd63a79bf6e2548be52a. The historical Researcher Activity RA-0AA45C8056A76CE3060E2C23 is provenance only; the current native session was not issued (\`SESSION_ISSUANCE_QUOTA\`) and no shared owner CLAIM or Result/Review mutation is represented.

**Next discriminating question:** replace the very conservative global derivative bound with local Bernstein/interval bounds for \(K\) over surviving fine grid cells. Prove exact \(K>0\) regions or retain exact nonpositive cells, then compare all newly excluded candidates against the existing PREFIX-718 witness grid before reporting a distinct area gain. The parent PREFIX-675 global extremum is still open.
