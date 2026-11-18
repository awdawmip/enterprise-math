# OAI7 r320 — Universal one-half lower coefficient for positive-tail shared schedules with repeated offsets

Date: 2026-11-18. Source-exposed mathematical continuation attributed to historical Driver line EM-DVR-DEBB5E. This is an **author-side derivation, not an independently accepted Native Result/Review**, DA renewal, official task completion or admissible native X6 realization. Original OAI7 researcher EM-EMF6D046-5A2844 and contributors of r307, r309, r312, r315, r318 and r319 retain their separate provenance.

## Exact model and theorem

Let $G$ be a finite additive group of prime order $p$, let $u=\lceil\sqrt p\rceil$, $b=17/64$ and $L_*=p^{3/4}$. For any random ordered offset vector $W=(w_1,\ldots,w_n)\in G^n$, allowing arbitrary dependence, repeated entries and nonuniformity, and any *fixed deterministic* $u$-element set $K\subseteq G$, define
$$
L_K(W)=\left\{x\in G:\sum_{\ell=1}^n\mathbf 1_{\{x+w_\ell\in K\}}\le bnu/p\right\},
\quad q_p=\max_{|K|=u}\Pr_W\{|L_K(W)|>L_*\}.
$$

**Theorem.** For every fixed $0<\varepsilon<1/2$ and *every* joint law of $W$, uniformly when
$$
1\le n\le (1/2-\varepsilon)\sqrt p\log p,
$$
one has
$$
q_p\ge1-\exp\!\left[-p^{\varepsilon/2}/(\log p)^{O(1)}\right]\longrightarrow1
\qquad(p\to\infty).
$$
Consequently, a sequence with $q_p\le Q<1$ eventually must satisfy
$$
\boxed{\liminf_{p\to\infty}\frac{n_p}{\sqrt p\log p}\ge\frac12.}
$$
The estimate is per-coordinate and uniform, so the same necessary coefficient holds under the homogeneous r315 signed-coordinate average-tail budget $R_0=(2k)^{-1}\sum_c q_c\le Q<1$, even with shared coordinates, repetition and growing $k$.

It strengthens r318's all-law coefficient $1/4$. It does not claim r319's larger $1/[4(1-b+b\log b)]\approx0.65403254$ coefficient for schedules with pairwise distinct offsets.

## Proof: multiplicity decomposition and local hypergeometric mass

Put $\rho=u/p$ and $\mu=n\rho$. Fix one arbitrary realized offset vector $w$. Let $h$ be its number of distinct **non-singleton** offset values (multiplicity at least 2), and $s$ its number of singleton offset values. Necessarily
$$
s+2h\le n,\qquad \alpha=s/n,\quad\beta=h/n,\qquad
0\le\alpha\le1,\quad0\le\beta\le(1-\alpha)/2. \tag{1}
$$
For each starting point $x$, the translates of those $h$ heavy and $s$ singleton values form disjoint subsets $H_x,S_x\subset G$. Sample $K$ uniformly from all $u$-subsets, independently of $w$. If $K\cap H_x=\varnothing$ and exactly $j$ members of $S_x$ lie in $K$, then the weighted hit count of the entire offset multiset is $j$.

Choose $j=\lfloor\min(s\rho,b\mu)\rfloor$, with $j=0$ when $s=0$. This satisfies $0\le j\le s,u$ and $j\le b\mu$, so the event just described guarantees $x\in L_K(w)$. Its exact probability is
$$
P_{h,s,j}=\frac{\binom{s}{j}\binom{p-h-s}{u-j}}{\binom pu}. \tag{2}
$$
For $1\le n\le C\sqrt p\log p$, $h+s\le n$, $j=O(\log p)$, the falling-factorial identity
$$
P_{h,s,j}=
\binom{s}{j}\frac{(u)_j}{(p)_j}
\prod_{i=0}^{u-j-1}\left(1-\frac{h+s-j}{p-j-i}\right)
$$
gives, uniformly over all admissible $h,s,j$,
$$
P_{h,s,j}=
e^{-(h+s)\rho}\frac{(s\rho)^j}{j!}\,\exp(o(1)). \tag{3}
$$
Interpret $(s\rho)^0=1$ also at $s=0$. If $j\ge1$ then $s\rho\ge1$, hence $s\ge p/u\asymp\sqrt p$. The error in logarithms is $O((\log p)^3/\sqrt p)$ using $j^2/s$, $ju/p$, $j(h+s)/p$, and $u(h+s)(u+h+s)/p^2$. When $j=0$, the product formula alone yields the same approximation without needing $s\ge\sqrt p$.

Define $J(z)=1-z+z\log z$ on $(0,1]$. The Poisson local-mass factorial estimate, applied to the last factor of (3), gives
$$
\log\Pr_K\{x\in L_K(w)\}
\ge-\mu f(\alpha,\beta)-O(\log(\mu+2))-o(1),\tag{4}
$$
where
$$
f(\alpha,\beta)=
\begin{cases}
\beta,&0\le\alpha\le b,\\
\beta+\alpha J(b/\alpha),&b<\alpha\le1.
\end{cases}
$$
For $\alpha\le b$ we have chosen $j=\lfloor s\rho\rfloor$, a near-mean Poisson mass; its loss beyond $e^{-h\rho}$ is polynomial in $(1+\mu)$. For $\alpha>b$, we choose $j=\lfloor b\mu\rfloor$, and Stirling gives the explicit rate $\alpha\mu J(b/\alpha)$, with uniform rounding loss $O(\log(\mu+2))$. The bounded-$\mu$ and $j=0$ cases are included in the same bound.

The uniform exponent bound is elementary. If $\alpha\le b$, then $f=\beta\le1/2$. If $\alpha>b$, (1) gives
$$
f(\alpha,\beta)\le\frac12+g(\alpha),\qquad
g(\alpha)=\frac{\alpha}{2}-b+b\log(b/\alpha).
$$
Since $g''(\alpha)=b/\alpha^2>0$, its maximum on $[b,1]$ is at an endpoint. Both are negative:
$$
g(b)=-b/2<0,\qquad
g(1)=J(b)-1/2<0,\qquad J(17/64)=0.3822439754975\ldots.
$$
Therefore $f(\alpha,\beta)\le1/2$ in all cases. There exists an absolute constant $C_0$ such that for sufficiently large $p$ and all $w,x$,
$$
\Pr_K\{x\in L_K(w)\}\ge
\frac{e^{-\mu/2}}{C_0(\mu+2)^{C_0}}. \tag{5}
$$

## Proof: concentration over fixed deterministic test sets

Put $V_w(K)=|L_K(w)|$. Summing (5) over $x$,
$$
\mathbb E_K V_w(K)\ge\frac{p e^{-\mu/2}}{C_0(\mu+2)^{C_0}}. \tag{6}
$$
For the claimed upper bound on $n$ and $u=\lceil\sqrt p\rceil$, eventually $\mu\le(1/2-\varepsilon/2)\log p$. Consequently (6) is at least $p^{3/4+\varepsilon/4}/(\log p)^{O(1)}$.

If two $u$-subsets differ by one element exchange, only starting points whose translated offset support contains one of the two exchanged residues can change membership in $L_K(w)$. Each residue corresponds to at most $d=h+s\le n$ starts. Thus
$$
|V_w(K)-V_w(K')|\le2d\le2n.
$$
Expose the uniform subset as $u$ draws without replacement. The standard transposition coupling gives martingale-difference range at most $2n$ per draw, hence the same conservative Azuma estimate as r318:
$$
\Pr_K\{V_w(K)\le L_*\}
\le\exp\left[-\frac{(\mathbb E_KV_w-L_*)_+^2}{8un^2}\right]
\le\exp[-p^{\varepsilon/2}/(\log p)^{O(1)}].\tag{7}
$$
Here $un^2=O(p^{3/2}\log^2p)$; the bounds are **uniform in $w$**. Average (7) over *any* random law of $W$ and interchange the finite $K,W$ expectations. The maximum over fixed deterministic $K$ is at least the uniform $K$-average, proving the asserted $q_p$ bound with the original r307 quantifier order. Any subsequence with $n_p/(\sqrt p\log p)<1/2-\varepsilon$ contradicts a fixed eventual $q_p\le Q<1$, proving the liminf statement.

## Mathematical limits, provenance and source pins

The theorem applies to the **external finite-group list-tail abstraction**, not an actual bounded-step Gaussian-prime walk or typed native Heartbeat X6/Port/Link path. It does not add a formal Result/Review, independent reviewer status, owner CLAIM, Source/Activity association, Task completion or Foundation promotion. The universal sharp leading constant remains open; r315's upper schedule has coefficient 128, and r319's stronger lower coefficient only covers all-realizations-distinct schedules.

Sources: r307 @ baaaabaacaf8543f62a45a00cdfcf03e95389075; r315 @ 91555075510068632a53f02a5b2e1731d4bcb44e; r318 @ f770d2b71bf6371679b37dc9686603fb85abec19; r319 @ d292f14db079dd59fe12b6ee2ce638afb6617723.


## Later same-day linkage (r321; provenance-preserving)

The one-half coefficient proved above remains a valid independent lower-bound lemma. The later r321 argument partitions **all** repeated-offset multiplicity classes and obtains the stronger universal coefficient $1/[4(1-b+b\log b)]\approx0.65403254$, previously known only under r319's distinct-offset hypothesis. Preserve the original r320 proof, its weaker bound, the original r312/r319 coefficient provenance and the distinction between a GitHub mathematics note and Native Result acceptance. Follow-up: [r321 exact multiplicity-class proof](https://github.com/awdawmip/enterprise-math/blob/3c411d17ca496dfcfcdb91082643597981f6b9d2/research_notes/driver/2026-11-18_oai7_arbitrary_repetitions_sharp_distinct_class_lower_coefficient_r321.md).
