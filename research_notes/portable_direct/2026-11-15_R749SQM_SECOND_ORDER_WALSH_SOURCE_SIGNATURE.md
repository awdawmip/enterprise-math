# R749SQM — Universal second-order source signature and cyclotomic exceptions

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Auxiliary 16-atom Walsh source-fiber line; this is not a native X6/Cell/Port equivalence claim, a shared TASK CLAIM, or a promoted theorem. The frozen scientific input is `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; prior exact frontier R749SQK/SQL, Draft PR #2502 and #2503.

## Model and question

Take labeled positive integer weights \(s_1,\dots,s_d\), with at least one weight 1, and one marked coordinate of weight \(h=s_j\). For integer \(r\ge1\), uniformly sample \(\Omega_r=\{n\in\mathbb Z_{\ge0}^d:\sum_i s_in_i<r\}\), define \(C_r=|\Omega_r|\), \(K_r=n_j\), and \(X_r=hK_r/r\). Write

\[
D=\sum_i(s_i-1),\qquad Q=\sum_i(s_i^2-1),\qquad W=\prod_i s_i.
\]

R749SQK proved that the first inverse-resolution moment correction depends only on \((d,D,h)\). The present question is the first way to recover additional provenance at the next order, including possible periodic lattice obstruction.

## Theorem (second-order mean; complete exceptional classification)

For any fixed weight alphabet, the following expansions hold as **integer** \(r\to\infty\). Define
\[
A_0=\frac1{d+1},\qquad
A_1=\frac{D+d-1-h(d+1)}{2(d+1)},\qquad
A_2=\frac{d((d+1)(h^2-1)-Q)}{12(d+1)}.
\]
If the alphabet contains at least two unit-weight coordinates, OR contains exactly one unit-weight coordinate and the gcd of all remaining weights is 1, then
\[
\boxed{\mathbb E[X_r]=A_0+\frac{A_1}{r}+\frac{A_2}{r^2}+O_{\mathbf s}(r^{-3}).}
\]
The same formula holds for the sole unit-weight coordinate when \(d=1\) (in fact it is exact).

In the only remaining case, there is exactly one unit-weight coordinate, \(d\ge2\), and \(g=\gcd\{s_i:s_i>1\}>1\). Put \(n\equiv r-1\pmod g\), \(0\le n<g\), and
\[
S_g(r)=\frac{(g-1)(5-g)}{12}+\frac{n(g-n-2)}2.
\]
Then
\[
\boxed{\mathbb E[X_r]=A_0+\frac{A_1}{r}
+\frac{A_2+\beta S_g(r)}{r^2}+O_{\mathbf s}(r^{-3}),}
\quad
\beta=\begin{cases}
\frac{2d}{d+1},&h>1,\\
-\frac{d(d-1)}{d+1},&h=1.
\end{cases}
\]
For \(d\ge2\) this is a genuinely nonconstant periodic correction, so a single smooth second-order coefficient cannot be claimed in the exceptional case. The error constants depend on the fixed alphabet, not on \(r\).

**Interpretation:** the first-order correction sees only \(d,D,h\); the smooth second-order correction reveals \(Q\). At the same order, when the unique unit coordinate leaves a common nonunit gcd, a nonzero cyclotomic/quasipolynomial residue additionally reveals \(r\pmod g\). This is an auxiliary provenance/residual distinction, not a new spatial dimension or a P000 assertion.

## Proof

Let \(w=1-z\), \(F(z)=\sum_{r\ge1}C_rz^{r-1}\), and \(T(z)=z^h/(1-z^h)\). The exact deletion bijection from R749SQK gives
\[
F(z)=\frac1{1-z}\prod_{i=1}^d\frac1{1-z^{s_i}},
\quad
\sum_{r\ge1}C_r\mathbb E[K_r]z^{r-1}=F(z)T(z).
\]

**Pole at 1.** Taylor expanding each integer-weight factor gives
\[
F(1-w)=\frac{w^{-d-1}}{W}
\left[1+\frac D2w+
\left(\frac{D(D+2)}8-\frac Q{24}\right)w^2+O(w^3)\right],
\]
\[
T(1-w)=\frac1{hw}-\frac{h+1}{2h}
+\frac{h^2-1}{12h}w+O(w^2).
\]
Extract coefficients with \([z^{r-1}](1-z)^{-k}=\binom{r+k-2}{k-1}\). Using \(\binom{r+k-1}{k}
=r^k/k!\,[1+k(k-1)/(2r)+k(k-1)(3k^2-7k+2)/(24r^2)+O(r^{-3})]\), perform polynomial division of \(h[z^{r-1}]FT\) by \(r[z^{r-1}]F\). Its constant, \(1/r\), \(1/r^2\) coefficients simplify to \(A_0,A_1,A_2\) above. In particular, **the whole dependence on \(D\) cancels from \(A_2\)**. The local pole at 1 produces an \(O(r^{-3})\) remainder after division.

**Other roots.** The poles of \(F\) and \(FT\) lie at roots of unity. At \(\zeta\ne1\), the cumulative factor \((1-z)^{-1}\) and each weight-1 coordinate are analytic. If at least two coordinates have weight 1, every nontrivial pole of \(F\) has order at most \(d-2\), and every pole of \(FT\) at most \(d-1\). Their contribution to \(\mathbb E[X_r]\) begins at \(O(r^{-3})\). If there is exactly one unit coordinate but the nonunit gcd is 1, at most \(d-2\) remaining weights vanish at each nontrivial root and the same estimate applies. For \(d=1\), there are no nontrivial poles.

If the sole unit coordinate has \(g>1\), exactly the nontrivial \(g\)-th roots can have maximum pole order \(d-1\) in \(F\). Denote \(W'=\prod_{s_i>1}s_i=W\). With \(v=1-z/\zeta\), their leading germs are
\[
F(z)=\frac{v^{-(d-1)}}{(1-\zeta)^2W'}+O(v^{-(d-2)}).
\]
When \(h>1\), \(g\mid h\), hence
\[
F(z)T(z)=\frac{v^{-d}}{h(1-\zeta)^2W'}+O(v^{-(d-1)}).
\]
When \(h=1\), \(T\) is regular there and cannot increase the pole order. Therefore
\[
C_r\big|_{\zeta}=\frac{\zeta^{-(r-1)}r^{d-2}}{(d-2)!(1-\zeta)^2W'}+O(r^{d-3}),
\]
and for \(h>1\),
\[
\frac hr[z^{r-1}]FT\big|_{\zeta}
=\frac{\zeta^{-(r-1)}r^{d-2}}{(d-1)!(1-\zeta)^2W'}+O(r^{d-3}).
\]
Divide by \(C_r\sim r^d/(d!W')\). The first correction from the denominator is \(-d(d-1)S_g(r)/(d+1)r^2\); the numerator adds \(d S_g(r)/r^2\) precisely when \(h>1\). This gives \(\beta\) in both cases. Every nonmaximal nontrivial-root contribution is \(O(r^{-3})\).

Finally, by the root-of-unity filter,
\[
\sum_{\substack{\zeta^g=1\\\zeta\ne1}}
\frac{\zeta^{-(r-1)}}{(1-\zeta)^2}
=S_g(r).
\]
For completeness let \(U(n)=\sum_{\zeta\ne1}\zeta^{-n}/(1-\zeta)=(g-1)/2-n\), \(0\le n<g\). The difference \(S(n)-S(n-1)=U(n)\) for \(1\le n<g\), and zero average \(\sum_{n=0}^{g-1}S(n)=0\) uniquely gives the displayed quadratic expression. This is exact, including the residue \(n=0\). The latter term cannot be constant for \(g>1\). QED.

## Exact counterexample and distinguishing alphabet pair

For \((s_1,s_2)=(1,2)\) with marked \(h=2\), \((d,D,Q)=(2,1,3)\), the smooth coefficients are \((1/3,-2/3,1/3)\), but the exact finite mean is
\[
\mathbb E[X_r]=
\begin{cases}
1/3-2/(3r),&r\text{ even},\\
1/3-2/[3(r+1)],&r\text{ odd}.
\end{cases}
\]
Thus the second-order coefficient oscillates between 0 and \(2/3\). This defeats an unqualified universal smooth second-order claim with only one unit weight.

For alphabets \(A=(1,1,2,4)\) and \(B=(1,1,3,3)\), mark a weight-1 coordinate in each. Both share \((d,D,h)=(4,4,1)\), but \(Q_A=18\), \(Q_B=16\), and both have two unit coordinates (no leading periodic anomaly). Hence the **proved** asymptotic separation is
\[
\boxed{\mathbb E_A[X_r]-\mathbb E_B[X_r]
=-\frac{2}{15r^2}+O(r^{-3}).}
\]
In particular their means differ for all sufficiently large integer \(r\), despite matching every first-order moment correction.

## Reproducibility and scope

The attached `R749SQM_SECOND_ORDER_SOURCE_CERT.js` is a standalone Node.js BigInt/Euclidean-fraction certificate, with no external dependencies. It recomputes each finite \(C_r\), marked first moment, independent optional-deletion counts for \(1\le r\le128\), all 1,536 exact values in the two-weight periodic example, exact rational second-order residuals at \(r=128,256,512,1024,1536\), and both prior Walsh boundary values \(B_{38},B_{39}\). The included `R749SQM_SECOND_ORDER_SOURCE_RESULTS.json` is the actual execution output; all assertions passed. These finite comparisons support reproduction, not the infinite claims, which follow from the rational-function proof above. The script does not claim to verify native P000 X6 physics or independent theorem review.

**Next mathematical problem:** derive all order-\(r^{-3}\) coefficients, including secondary cyclotomic sectors, and determine the minimal fixed moment/cumulant collection distinguishing source-weight alphabets beyond \((d,D,h,Q,g)\). A further route is a constructive source-residual codec retaining the detected \(Q\) and periodic class without storing the full histogram.

**Activity / ownership:** independent research on a previously exposed auxiliary science line; no shared CLAIM acquired by this paper. R749SQL verified predecessor remains intact. Original recorded Researcher-ID `EM-DIRECT-5AD5C5` / Activity `RA-23D649E29465155706DB0336` are historical metadata and are not by themselves fresh execution authority. Any formal Activity checkpoint requires its own current authenticated write path.

