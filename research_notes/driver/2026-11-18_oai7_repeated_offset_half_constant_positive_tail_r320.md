# OAI7 r320 — Universal 1/2 lower coefficient for positive-tail shared schedules, including repeated offsets

Date: 2026-11-18. Mathematical continuation in the source-exposed historical Driver line `EM-DVR-DEBB5E`. This note is **author-side mathematical work, not a Native independent Result/Review, Task closure, DA activation, or X6 realization**. Original OAI7 contributor `EM-EMF6D046-5A2844` and the prior r307/r309/r312/r315/r318/r319 contributors retain their separate provenance.

## Statement and exact scope

Let (G) be an additive finite group of prime order (p). Put (u=lceilsqrt pceil), (b=17/64) and (L_*=p^{3/4}). For an arbitrary probability distribution on length-(n) offset vectors (W=(w_1,\ldots,w_n)\in G^n), allowing *all* temporal dependence, repetition and nonuniformity, define, for a deterministic (u)-element subset (K),
[
L_K(W)=\left\{x\in G:\sum_{\ell=1}^n {\bf1}_{\{x+w_\ell\in K\}}\le bnu/p\right\},\qquad
q_p=\max_{|K|=u}\Pr_W\{|L_K(W)|>p^{3/4}\}.
]

**Theorem (universal positive-tail improvement).** For every fixed (0<\varepsilon<1/2), uniformly over every law of (W) with
[
1\le n\le(1/2-\varepsilon)\sqrt p\log p,
]
one has (q_p\to1) as (p\to\infty). In fact (q_p\ge1-\exp[-p^{\varepsilon/2}/(\log p)^{O(1)}]) for all sufficiently large (p), with constants depending on (\varepsilon). Consequently any such sequence with (q_p\le Q<1) eventually satisfies
[
\boxed{\liminf_{p\to\infty}\frac{n_p}{\sqrt p\log p}\ge\frac12}.
]
For the homogeneous signed-coordinate construction of r315, this uniform per-coordinate lower bound also applies when the budget is imposed on the average (R_0=(2k)^{-1}\sum_c q_c\le Q<1), regardless of shared randomness or the growth of (k).

This strictly strengthens the *arbitrary-repetition* coefficient (1/4) from r318; it does not supersede the stronger (1/[4(1-b+b\log b)]\approx0.65403) coefficient of r319, which requires pairwise-distinct offsets in every realization. The exponent/order (Θ(\sqrt p\log p)) was already proved by r318+r315 and is **not** a new claim here.

## Proof

Write (\rho=u/p), (\mu=n\rho). Fix one realized offset vector (w). Among its distinct offsets, let (h) denote the number appearing at least twice and (s) the number appearing exactly once. Hence
[
s+2h\le n,\qquad \alpha=s/n,\quad\beta=h/n,\quad
0\le\alpha\le1,\quad0\le\beta\le(1-\alpha)/2.                 \tag{1}
]
For any fixed start (x), the translated heavy-offset set (H_x) and singleton-offset set (S_x) are disjoint, of sizes (h,s). Choose (K) uniformly among all (u)-element subsets of (G), *independently* of (w). If (K\cap H_x=\varnothing) and (j=|K\cap S_x|\le b\mu), then the weighted hit count at (x) is exactly (j\le b\mu), regardless of the heavy multiplicities.

Choose the integer (j=\lfloor\min(s\rho,b\mu)\rfloor). This is a possible intersection count ((j\le s,u)); when (s=0), take (j=0). Its exact probability is
[
\Pr_K\{K\cap H_x=\varnothing,\ |K\cap S_x|=j\}
=\frac{\binom{s}{j}\binom{p-h-s}{u-j}}{\binom pu}.                \tag{2}
]
As (p\to\infty), uniformly for (1\le n\le C\sqrt p\log p), (h,s\le n) and this choice of (j\le O(\log p)), elementary falling-factorial expansions yield
[
\frac{\binom{s}{j}\binom{p-h-s}{u-j}}{\binom pu}
=e^{-(h+s)\rho}\frac{(s\rho)^j}{j!}\,e^{o(1)}.                    \tag{3}
]
A direct derivation uses
[
\binom{s}{j}\frac{(u)_j}{(p)_j}
\prod_{i=0}^{u-j-1}\left(1-\frac{h+s-j}{p-j-i}\right).
]
If (j\ge1), then (s\rho\ge1), so (s\ge p/u\asymp\sqrt p). The logarithmic error in (3) is bounded by (O((1+\log p)^3/\sqrt p)=o(1)) from (j^2/s), (ju/p), (j(h+s)/p), (u(h+s)(u+h+s)/p^2). If (j=0), the analogous product estimate holds directly, including (s=0).

The usual factorial bounds (or Stirling) now give, uniformly in (\alpha,\beta),
[
\log\Pr_K\{x\in L_K(w)\}
\ge -\mu f(\alpha,\beta)-O(\log(\mu+2))-o(1),                \tag{4}
]
where (J(z)=1-z+z\log z) and
[
 f(\alpha,\beta)=
 \begin{cases}
 \beta,&0\le\alpha\le b,\\
 \beta+\alpha J(b/\alpha),&b<\alpha\le1.
 \end{cases}
]
Indeed if (s\rho\le b\mu), the chosen integer lies at the mean of the singleton Poisson approximation, costing only a polynomial factor in (1+\mu); otherwise it lies at the fraction (b/\alpha<1) of that mean.

**Uniform exponent bound.** For (\alpha\le b), (f\le\beta\le1/2). For (b<\alpha\le1), (1) gives
[
f\le\frac12+g(\alpha),\qquad
g(\alpha)=\frac\alpha2-b+b\log(b/\alpha).
]
Here (g''(\alpha)=b/\alpha^2>0), so the maximum on ([b,1]) is at an endpoint. The endpoint values are (g(b)=-b/2<0) and (g(1)=J(b)-1/2<0) for (b=17/64) (indeed (J(b)\approx0.3822439755)). Hence (f(\alpha,\beta)\le1/2) in every case. Combining with (4), there is an absolute (C_0) such that, uniformly over all (w,x),
[
\Pr_K\{x\in L_K(w)\}
\ge\frac{e^{-\mu/2}}{C_0(\mu+2)^{C_0}}.                         \tag{5}
]

Let (V_w(K)=|L_K(w)|). Summing (5) over the (p) starting residues,
[
\mathbb E_K V_w(K)\ge \frac{p e^{-\mu/2}}{C_0(\mu+2)^{C_0}}.      \tag{6}
]
For (n\le(1/2-\varepsilon)\sqrt p\log p) and (u=\lceil\sqrt p\rceil), eventually
(\mu\le(1/2-\varepsilon/2)\log p), so the right side of (6) is
(\ge p^{3/4+\varepsilon/4}/(\log p)^{O(1)}\), uniformly over realized (w).

Swapping one included and one excluded element of (K) changes the good/bad status at at most (2d\le2n) starts, where (d=h+s) is the number of distinct offset values; multiplicities do not change this Lipschitz count. Exposing (K) through (u) draws without replacement and using the same transposition coupling as in r318 yields
[
\Pr_K\{V_w(K)\le p^{3/4}\}
\le\exp\!\left[-\frac{(\mathbb E_K V_w-p^{3/4})_+^2}{8un^2}\right]
\le\exp[-p^{\varepsilon/2}/(\log p)^{O(1)}].                     \tag{7}
]
The last inequality uses (un^2=O(p^{3/2}\log^2p)). Equation (7) is uniform over every realized (w). Average over *any* law of (W), interchange the finite (K,W) expectations, and use that the maximum over fixed deterministic (K) is at least the uniform (K)-average:
[
\max_{|K|=u}\Pr_W\{V_W(K)>p^{3/4}\}\to1.
]
The quantifier order is therefore **fixed (K), then random (W)**, not an adversarial (K) selected after observing (W). The statement on (R_0) follows because each coordinate has the same uniform lower bound. Taking an infinite subsequence below coefficient (1/2) proves the stated liminf claim. \(\square\)

## What is and is not concluded

- The improved (1/2) obstruction is universal over repeated, correlated, adaptive and deterministic schedules **in this external finite-group list-tail model**. It exploits the singleton/repetition decomposition, a hypergeometric local-mass lower estimate and fixed-test-set concentration.
- The sharp universal leading coefficient remains open; the interval between (1/2) (all laws) and (128) (r315 construction) is a coefficient gap, not a new order gap. The (0.65403) distinct-only obstruction is separate.
- No new `CLAIM`, Native Result admission, Source/Activity association, X6/Port/Link realization, formal proof checker certification, Task completion or Foundation promotion is asserted. Prior theorem and source contributors remain distinct.

## Pinned sources

- r307 integrated list-tail definition: `baaaabaacaf8543f62a45a00cdfcf03e95389075`.
- r315 growing-independence upper schedule: `91555075510068632a53f02a5b2e1731d4bcb44e`.
- r318 all-laws (1/4) lower bound and bounded-difference lemma: `f770d2b71bf6371679b37dc9686603fb85abec19`.
- r319 distinct-offset positive-tail (0.65403) bound: `d292f14db079dd59fe12b6ee2ce638afb6617723`.
