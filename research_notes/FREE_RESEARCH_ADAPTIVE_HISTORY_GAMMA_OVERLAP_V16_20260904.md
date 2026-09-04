# Free Research — Adaptive History Gamma-Overlap Hierarchy

Status: `FREE_RESEARCH_FRONTIER / ALL_FIXED_DEPTH_LOG_LAWS / CONSECUTIVE_OVERLAP_EXACT / CENTRAL_POISSON_DEFECT / GROWING_DEPTH_ARITHMETIC_UNIFORMITY_OPEN / BLOCK_RELATION_CONTROL_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PRIME_PARITY_BLOCK_COUPLING_V16_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the adaptive prime-power return kernel, logarithmic scale calculus, and factorial provenance hierarchy.

## 1. Executive advance

The one-history versus two-history overlap `1-e^-1` is the first member of an exact all-depth hierarchy.

In the ideal logarithmic limit, after `k` adaptive prime-power returns the remaining normalized logarithmic scale is

\[
S_k=U_1U_2\cdots U_k,
\]

where the `U_i` are independent `Uniform(0,1)` variables.  Its density is

\[
\boxed{
f_k(s)=\frac{(-\log s)^{k-1}}{(k-1)!},
\qquad0<s<1.}
\tag{1.1}
\]

The overlap between consecutive history depths is

\[
\boxed{
L_k:=\int_0^1\min\{f_k(s),f_{k+1}(s)\}\,ds
=1-e^{-k}\frac{k^k}{k!}.}
\tag{1.2}
\]

Hence the unmatched parity mass is

\[
\boxed{d_k:=1-L_k=e^{-k}\frac{k^k}{k!}.}
\tag{1.3}
\]

This is exactly the central Poisson probability

\[
d_k=\Pr\{\operatorname{Poisson}(k)=k\},
\]

and Stirling gives

\[
\boxed{d_k\sim(2\pi k)^{-1/2}.}
\tag{1.4}
\]

Thus successive parity-history endpoint laws become increasingly overlapping.  The factorial in the provenance hierarchy reappears here as the normalization of the unique crossing defect between depth `k` and depth `k+1`.

The arithmetic fixed-depth version follows from `A(x)=log x+O(1)`.  The new unresolved issue is uniformity when `k` grows with `log log N`, and the control of the within-block relation energy left by coarse coupling.

---

## 2. Ideal adaptive logarithmic chain

Let `T_0=T` and, conditionally on `T_j`, choose

\[
T_{j+1}=U_{j+1}T_j,
\qquad U_{j+1}\sim\operatorname{Uniform}(0,1).
\]

Then

\[
\frac{T_k}{T}=S_k=\prod_{j=1}^kU_j.
\]

Putting

\[
Y_k:=-\log S_k,
\]

we have

\[
Y_k=\sum_{j=1}^k(-\log U_j).
\]

Each `-log U_j` is exponential with mean one, so

\[
\boxed{Y_k\sim\operatorname{Gamma}(k,1).}
\tag{2.1}
\]

The Gamma density is

\[
g_k(y)=e^{-y}\frac{y^{k-1}}{(k-1)!},
\qquad y>0.
\]

Under `s=e^-y`, the Jacobian `ds=e^-y dy` gives (1.1).

---

## 3. Exact consecutive-depth overlap

The density ratio is

\[
\boxed{
\frac{f_{k+1}(s)}{f_k(s)}
=\frac{-\log s}{k}.}
\tag{3.1}
\]

There is exactly one crossing, at

\[
\boxed{s=e^{-k}.}
\tag{3.2}
\]

Equivalently, the Gamma densities cross at `y=k`.

For `y<k`, `g_(k+1)(y)<g_k(y)`; for `y>k`, the inequality reverses.  Therefore

\[
\begin{aligned}
1-L_k
&=\int_0^k(g_k(y)-g_{k+1}(y))\,dy\\
&=F_k(k)-F_{k+1}(k).
\end{aligned}
\]

The incomplete-Gamma recurrence gives

\[
F_k(k)-F_{k+1}(k)
=e^{-k}\frac{k^k}{k!}.
\]

This proves (1.2)--(1.3).

The first values are

\[
d_1=e^{-1},
\qquad
d_2=2e^{-2},
\qquad
d_3=\frac92e^{-3}.
\]

Thus the V16 one/two-history overlap is precisely the `k=1` case.

---

## 4. Factorial provenance interpretation

The defect

\[
d_k=e^{-k}\frac{k^k}{k!}
\]

contains the same two combinatorial quantities that govern the finite history carrier:

- `k^k`: all maps from `k` history positions to `k` scale bins;
- `k!`: ordered full-image provenance normalization.

At the probabilistic level, `e^-k k^k/k!` is the central atom of a Poisson distribution.  At the cutoff-chamber level, `k^k` is partitioned by Stirling image-size classes.

The exact relation is not that the two finite sample spaces are identical.  Rather, the same factorial normalization controls:

1. the full-image ordered provenance sector;
2. the single crossing defect between consecutive adaptive history depths.

This gives a new all-degree meaning to factorial provenance:

\[
\boxed{
\text{factorial history normalization}
\longleftrightarrow
\text{consecutive parity-law overlap defect}.}
\]

---

## 5. Fixed-depth arithmetic convergence

Let `P` be the finite adaptive prime-power return operator.  For fixed `k`, let `mu_(N,k)` be the law of

\[
\frac{\log M_k}{\log N},
\]

where `M_k` is the endpoint after `k` adaptive quotient actions.

The first-mass estimate

\[
A(x)=\log x+O(1)
\]

implies, by induction on fixed `k`, that

\[
\boxed{
\mu_{N,k}\Longrightarrow f_k(s)\,ds.}
\tag{5.1}
\]

Indeed, conditionally on an intermediate logarithmic length `u`, the next normalized ratio is uniform up to discrepancy `O(1/u)`.  For a fixed finite number of steps, the region `u<=1` has mass `O_k(1/log N)`, while the integrated discrepancy on `u>1` is `O_k(log log N/log N)`.

Consequently, for every fixed finite block partition,

\[
\boxed{
L_{N,k,K}
\longrightarrow L_{k,K},}
\tag{5.2}
\]

and after refining the partition,

\[
\boxed{
\lim_{K\to\infty}\lim_{N\to\infty}L_{N,k,K}
=1-e^{-k}\frac{k^k}{k!}.}
\tag{5.3}
\]

Here `L_(N,k,K)` is the block overlap of the depth-`k` and depth-`k+1` endpoint laws.

---

## 6. Growing-depth opportunity

Stirling's formula gives

\[
d_k\le\frac{C}{\sqrt{k}}
\]

for an absolute constant `C`.  Thus choosing

\[
k\asymp c\log\log N
\]

would make the ideal unmatched parity mass

\[
O((\log\log N)^{-1/2}).
\]

At the same time, the typical remaining logarithmic scale is

\[
\mathbb E[\log M_k]\asymp e^{-k}\log N.
\]

For `c<1`, this still tends to infinity, so the residual estimate

\[
|e(M_j)|\ll(1+\log M_j)^{-1}
\]

remains useful through most histories.

This suggests a possible intermediate quantitative theorem:

\[
\boxed{
|r(N)|
\ll(\log\log N)^{-1/2}
+\text{matched block relation energy}^{1/2}
+\text{residual accumulation}.}
\tag{6.1}
\]

However, fixed-depth weak convergence does not justify taking `k` of size `log log N`.  A uniform triangular-array theorem is required.

---

## 7. Required growing-depth theorem

A sufficient arithmetic statement would be:

### Uniform adaptive-history approximation

For some `c>0`, uniformly for

\[
1\le k\le c\log\log N,
\]

and for a fixed or slowly growing logarithmic block partition,

\[
\boxed{
\|\mu_{N,k}^{\rm block}-\gamma_k^{\rm block}\|_{\rm TV}
\le C\frac{e^k\operatorname{poly}(k,\log\log N)}{\log N},}
\tag{7.1}
\]

where `gamma_k` is the product-uniform/Gamma law.

The factor `e^k/log N` is the natural accumulated conditional discrepancy, since the typical logarithmic scale after `j` steps is `e^-j log N`.

For every fixed `c<1`, the right side tends to zero.  This would promote the central-Poisson overlap law to growing depth.

The floor deformation is expected to fit the same error budget because the Chebyshev estimate controls its mean at each intermediate scale.

---

## 8. Matched relation-energy obstruction

Even perfect overlap of coarse logarithmic laws does not identify endpoint values within a block.  The exact finite block-coupling inequality leaves the positive term

\[
\mathcal V_{N,k,K}(r),
\]

the pooled within-block relation energy between depth `k` and depth `k+1` histories.

At growing depth, the unmatched scalar coefficient improves from `e^-1` to `O(k^-1/2)`, but the relation term remains.  A complete theorem therefore needs both:

1. the growing-depth approximation (7.1);
2. a provenance-compatible estimate
   \[
   \mathcal V_{N,k,K}(r)
   \le q_{\rm std}^{\,k}\mathcal E_{\rm initial}
   +F_{\rm low},
   \qquad q_{\rm std}<1,
   \]
   or an all-depth Dirichlet estimate with comparable decay.

The existing degree-three `S_3` mixer supplies a one-step standard energy factor `1/9`, but its stationary product measure has not yet been identified with the maximal block coupling at every growing history depth.

---

## 9. Current classification

Proved exactly in the ideal logarithmic model:

1. the depth-`k` density (1.1);
2. the unique crossing at `e^-k`;
3. the overlap formula (1.2);
4. the central-Poisson defect (1.3);
5. the asymptotic defect `(2 pi k)^-1/2`.

Proved at fixed-depth research-note strength from `A(x)=log x+O(1)`:

1. arithmetic convergence to the product-uniform law;
2. convergence of every fixed finite block overlap.

Open:

1. uniformity for `k` growing with `log log N`;
2. control of the matched within-block relation energy;
3. composition with the exact parity resolvent;
4. any promoted iterated-log or logarithmic prime remainder;
5. any RH-scale conclusion.

The new structural message is:

\[
\boxed{
\text{consecutive parity histories become asymptotically indistinguishable in scale,}
\quad
\text{with the entire defect concentrated in one factorial/Poisson crossing atom}.}
\]
