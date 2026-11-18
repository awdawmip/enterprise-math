# OAI7 r321 — The distinct-offset positive-tail lower coefficient is universal, even with arbitrary repetitions

Date: 2026-11-18. Driver-side source-exposed **mathematical derivation**, preserving earlier researcher EM-EMF6D046-5A2844, the r312 distinct-offset zero-tail argument, r318 general concentration, r319 distinct-offset positive-tail proof, and r320 multiplicity-decomposition lower bound. Authorship of the new weight-class argument belongs to the historical EM-DVR-DEBB5E line; it is not an independent Native review, formally admitted Result, Task closure, DA renewal or typed Heartbeat X6/Gaussian-walk result.

## Question and conclusion

For a prime-order finite additive group $G$ with $|G|=p$, let $u=\lceil\sqrt p\rceil$, $b=17/64$, $L_*=p^{3/4}$. Let $W=(w_1,\ldots,w_n)$ have any law whatsoever on $G^n$ (including repetitions, deterministic vectors, arbitrary correlation or adaptive generation). For each *fixed deterministic* $u$-subset $K$, set
$$
L_K(W)=\left\{x\in G:
\sum_{\ell=1}^n \mathbf1_{\{x+w_\ell\in K\}}\le bnu/p\right\},\qquad
q_p=\max_{|K|=u}\Pr_W\{|L_K(W)|>L_*\}.
$$

**Theorem.** Put
$$
J(b)=1-b+b\log b=0.3822439754975195\ldots,\qquad
c_*=\frac1{4J(b)}=0.6540325447238404\ldots.
$$
For every fixed $0<\varepsilon<c_*$, uniformly over every offset law with
$$
1\le n\le(c_*-\varepsilon)\sqrt p\log p,
$$
we have $q_p\to1$ as $p\to\infty$. Thus, for any fixed $Q<1$, every sequence with $q_p\le Q$ eventually obeys
$$
\boxed{\liminf_{p\to\infty}\frac{n_p}{\sqrt p\log p}\ge c_*}.
$$

This **removes the pairwise-distinctness hypothesis from the leading-coefficient necessity in r319**. It strengthens r318's all-law $1/4$ coefficient and r320's all-law $1/2$ coefficient. It does not determine the optimal sufficient leading constant (the pinned r315 upper certificate has coefficient 128), nor identify an admissible native path.

## 1. A deterministic multivariate-hypergeometric certificate

Fix any realized $w$ and any starting residue $x$. For each positive integer $m$, let $D_m$ be the set of **distinct** residues occurring with multiplicity exactly $m$ in $(x+w_\ell)_{\ell=1}^n$, and put $d_m=|D_m|$. Their sets are pairwise disjoint, and
$$
\sum_{m\ge1}m\,d_m=n,\qquad \sum_{m\ge1}d_m\le n.
$$
Write $\rho=u/p$, $\mu=n\rho$. Choose $M=\lceil(\log p)^{1/3}\rceil$, declare $D_{>M}=\bigcup_{m>M}D_m$, and let $d_{>M}=|D_{>M}|$. Then
$$
\lambda_m=d_m\rho,\quad
\lambda_{>M}=d_{>M}\rho\le\mu/(M+1),\qquad
\sum_{1\le m\le M}\lambda_m\le\mu.                     \tag{1}
$$
Choose an independent uniform $u$-element test set $K\subseteq G$. Require (i) $K$ to miss $D_{>M}$ entirely and (ii) to meet each class $D_m$ ($1\le m\le M$) in *exactly*
$$
j_m=\lfloor b\lambda_m\rfloor
$$
points. Let $J=\sum_{m=1}^M j_m\le b\mu=O(\log p)$. On this event, the full *multiplicity-weighted* hit count is
$$
\sum_{m=1}^M m j_m
\le b\sum_{m=1}^M m d_m \rho\le b\mu,
$$
so $x\in L_K(w)$. No offset distinctness assumption enters.

Writing $d=\sum_{m\le M}d_m+d_{>M}$, the event probability is the **exact** multivariate-hypergeometric mass
$$
P_w(x)=
\frac{\displaystyle
\left(\prod_{m=1}^M\binom{d_m}{j_m}\right)
\binom{p-d}{u-J}}
{\binom pu}.                                            \tag{2}
$$
Zero binomial factors are interpreted normally; for sufficiently large $p$, the chosen counts are feasible. If $j_m\ge1$, then $d_m\rho\ge1/b$, hence $d_m\ge p/(bu)\asymp\sqrt p$, so all factorial expansions with a positive $j_m$ are controlled uniformly.

For all $1\le n\le C\sqrt p\log p$, the following *relative* approximation is uniform over $w,x$:
$$
P_w(x)=
\exp[-d\rho+o(1)]
\prod_{m=1}^M\frac{\lambda_m^{j_m}}{j_m!}.             \tag{3}
$$
Indeed, the exact falling-factorial decomposition is
$$
P_w(x)=
\left(\prod_{m=1}^M\frac{(d_m)_{j_m}}{j_m!}\right)
\frac{(u)_J}{(p)_J}
\prod_{i=0}^{u-J-1}\left(1-\frac{d-J}{p-J-i}\right).
$$
Since $d\le n=O(\sqrt p\log p)$ and $J=O(\log p)$, the logarithmic error from replacing $(d_m)_{j_m}$ by $d_m^{j_m}$, $(u)_J/(p)_J$ by $\rho^J$, and the last product by $\exp(-d\rho)$ is bounded by
$$
O\left(\frac{J^2}{\sqrt p}+\frac{Ju}{p}
+\frac{Jd}{p}+\frac{ud(u+d)}{p^2}\right)
=O((\log p)^3/\sqrt p)=o(1).
$$
The $J^2/\sqrt p$ term uses $j_m>0\Rightarrow d_m\gg\sqrt p$. The approximation also handles all-zero $j_m$ without division by zero, with the convention $0^0=1$.

## 2. Uniform point-mass lower bound and disappearance of multiplicity cost

For every fixed $0<b<1$, there is a constant $C_b$ such that for *all* $\lambda\ge0$ and $j=\lfloor b\lambda\rfloor$,
$$
e^{-\lambda}\frac{\lambda^j}{j!}
\ge\exp[-\lambda J(b)-C_b\log(\lambda+2)].            \tag{4}
$$
For bounded $\lambda$ this follows by enlarging $C_b$ and treating $j=0$ exactly; for large $\lambda$ it follows from Stirling, $j=b\lambda+O(1)$, and the Poisson large-deviation rate $J(b)$. Thus the same constant works at every multiplicity class, including the empty ones.

By (3), (4), and $d\rho=\lambda_{>M}+\sum_{m\le M}\lambda_m$,
$$
\begin{aligned}
\log P_w(x)
&\ge-\lambda_{>M}-J(b)\sum_{m=1}^M\lambda_m
-C_b\sum_{m=1}^M\log(\lambda_m+2)-o(1)\\
&\ge-J(b)\mu-\frac{\mu}{M+1}
-O\bigl(M\log(\mu+2)\bigr)-o(1).                      \tag{5}
\end{aligned}
$$
The first term is **at most** $J(b)\mu$ because $\sum_{m\le M}\lambda_m\le\mu$; the deliberately coarse additional penalty $\mu/(M+1)$ bounds the forced absence of all higher-multiplicity classes. With $\mu=O(\log p)$ and $M=\lceil(\log p)^{1/3}\rceil$, the two penalties are respectively $O((\log p)^{2/3})$ and $O((\log p)^{1/3}\log\log p)$, both $o(\log p)$.

Consequently, uniformly for every realized $w$ and every $x$,
$$
\Pr_K\{x\in L_K(w)\}\ge
\exp[-J(b)\mu-O((\log p)^{2/3})].                     \tag{6}
$$
(The implicit constant is absolute for the fixed $b$ and bounded coefficient $C$.) The key point is that duplicates can be handled **by grouping equal multiplicities**: the cost of banning high weights is sublogarithmic, while each low-weight class pays its own near-mean *unweighted* Poisson lower-tail rate; their sum costs no more than $J(b)\mu+o(\log p)$.

## 3. Fixed-set quantifier order and concentration

Put $V_w(K)=|L_K(w)|$ for the deterministic multiset $w$. Summing (6) over all $p$ starts gives
$$
\mathbb E_K V_w(K)\ge p\,\exp[-J(b)\mu-O((\log p)^{2/3})]. \tag{7}
$$
For $n\le(c_*-\varepsilon)\sqrt p\log p$ and large $p$,
$$
\mu\le(c_*-\varepsilon/2)\log p,
\quad J(b)\mu\le(1/4-\varepsilon J(b)/2)\log p,
$$
so $\mathbb E_K V_w(K)\ge p^{3/4+\varepsilon J(b)/2-o(1)}$ uniformly in $w$.

Replacing one included residue of $K$ by one excluded residue affects the good/bad classification at no more than $2d\le2n$ starting points, irrespective of multiplicities. The r318 uniform-subset transposition coupling and Azuma's inequality yield
$$
\Pr_K\{V_w(K)\le p^{3/4}\}
\le\exp\left[-\frac{(\mathbb E_K V_w-p^{3/4})_+^2}{8un^2}\right]
\le\exp[-p^{\varepsilon J(b)-o(1)}].                 \tag{8}
$$
Indeed $un^2=O(p^{3/2}\log^2p)$ and the square of the mean excess has exponent $3/2+\varepsilon J(b)-o(1)$.

This holds for **every fixed realization** of $w$. Average over *any* probability law of $W$ and interchange the finite $K,W$ averages. The maximum over **fixed deterministic** $K$ dominates the $K$-average, hence
$$
q_p=\max_{|K|=u}\Pr_W\{|L_K(W)|>p^{3/4}\}
\ge1-\exp[-p^{\varepsilon J(b)-o(1)}]\longrightarrow1.
$$
An infinite subsequence with $n_p/(\sqrt p\log p)<c_*-\varepsilon$ contradicts a fixed eventual $q_p\le Q<1$, proving the theorem. The construction of $K$ is for the *averaging proof* only: the adversarial set in the actual assertion is deterministic and selected **before** $W$.

## Contribution and model limits

r312 discovered the numerical $c_*$ for **zero-tail distinct** schedules. r319 extended it to **positive-tail distinct** schedules. r318 proved the universal logarithmic order with a $1/4$ coefficient, and r320 used singleton/non-singleton grouping to improve the universal coefficient to $1/2$. The **new claim here** is the universal *same* $c_*$ lower coefficient without any distinctness, via all multiplicity classes and a uniform multivariate-hypergeometric point-mass estimate. Do not retroactively attribute the original coefficient or the r318 concentration lemma to r321.

The sufficient leading constant remains open, as do fixed base-index count, entropy optimization, exact native ordered X6 provenance-safe carrier and true Gaussian-prime walks. This note is an external finite-group theorem, not a claim of admissible native execution or formal independent review.

Pinned sources: r307 @ baaaabaacaf8543f62a45a00cdfcf03e95389075; r312 @ 34ac9052d5acd8cadb0ea75bf30d4fe07e346e70; r315 @ 91555075510068632a53f02a5b2e1731d4bcb44e; r318 @ f770d2b71bf6371679b37dc9686603fb85abec19; r319 @ d292f14db079dd59fe12b6ee2ce638afb6617723; r320 @ 761e8a8de292c63d70d36a590a6455102978f7f4.
