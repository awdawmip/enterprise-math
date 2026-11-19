# OAI7 r356 — Modular obstruction to minimally supported uniform-marginal minimax samplers

Date: 2026-11-19. Exact mathematical deduction in the existing shared Driver/OAI7 scientific context. The bounds below refine the *lower support* assertion of r353 and correct how r355's explicit construction is compared with r353's earlier existence bound. This is author-side mathematics, not an independent Native Result/Review.

## General theorem (finite fiber mass and uniform coordinate)

Let $X$ be a finite random label with exactly $m$ positive probabilities $p_x$, all in $N^{-1}\mathbb Z$, where $N\ge1$. Let $H=(H_1,\ldots,H_d)$ be a finite-valued ordered output, and assume $X=f$H$$ is a deterministic function of the complete output (for example, a loss-profile label). Suppose the first coordinate $H_1$ is exactly uniform on a set of $p\ge2$ labels and $\gcd(N,p)=1$. Then every such distribution has

\[
\boxed{|\operatorname{supp}$H$|\ge m+p-1.}\tag{1}
\]

Moreover, writing $r=N\bmod p\in\{1,\ldots,p-1\}$, its Shannon entropy in bits satisfies

\[
\boxed{H$H$\ge H$X$+\frac{r$p-r$}{pN\ln2}>H$X$.}\tag{2}
\]

Both statements are universal in the number of available outputs within each fiber, their weights, and the values of the other $d-1$ coordinates. The support argument requires only the first coordinate to be uniform; the other coordinates can impose further constraints.

### Proof of support bound

For every positive fiber $x$, let $S_x\subseteq\operatorname{supp}$H$$ consist of its $k_x\ge1$ positive output atoms, and let $A_x\subseteq\{0,\ldots,p-1\}$ be the distinct first-coordinate symbols that occur among $S_x$. Form an undirected graph on the $p$ symbols: for each $x$, connect the members of $A_x$ by any spanning tree. This uses at most $|A_x|-1\le k_x-1$ edges.

Every connected component $B$ of this graph is a union of whole sets $A_x$: no fiber places first-coordinate mass both inside and outside $B$. Consequently the probability of (H_1\in B) is the sum of complete fiber masses of those $x$ whose $A_x\subseteq B$, hence an integer multiple of $1/N$. Uniformity gives the same probability ( |B|/p). Thus
\[
\frac{|B|}{p}\in\frac1N\mathbb Z
\quad\Longrightarrow\quad p\mid N|B|.
\]
Since $\gcd(N,p)=1$, $p\mid |B|$. Any nonempty component has between 1 and $p$ vertices, so the entire graph is connected. It needs at least $p-1$ edges. Hence
\[
p-1\le\sum_x(|A_x|-1)\le\sum_x(k_x-1)
=|\operatorname{supp}$H$|-m,
\]
which proves (1). Parallel edges or coinciding first-coordinate symbols can only strengthen the inequality.

### Proof of strict quantitative entropy gap

Within each fiber $x$, choose a modal ordered atom $h_x$ with maximal conditional probability (q_x\). Define (Y=h_X), a deterministic function of $X$. The first-coordinate law of $Y$ has probabilities (k_a/N) with nonnegative integers $k_a$ summing to $N$, because each $p_x\in N^{-1}\mathbb Z$.

Write $N=pq+r$, $0<r<p$. Among all these lattice probability vectors, the minimum total variation distance from the uniform $p$-point law is achieved by $r$ entries ((q+1)/N) and $p-r$ entries (q/N). Its exact value is
\[
\operatorname{TV}$\mathcal L$Y_1$,U_p$
\ge \frac{r$p-r$}{pN}.
\]
Couple $H_1$ and $Y_1$ through their common $X$. Then
\[
\operatorname{TV}$\mathcal L$H_1$,\mathcal L$Y_1$$
\le\Pr$H_1\ne Y_1$
\le\Pr$H\ne Y$
=\sum_x p_x$1-q_x$.
\]
The left side is the preceding lattice distance because $H_1\sim U_p$. Finally, $X=f$H$$ gives
\[
H$H$-H$X$=H$H\mid X$
=\sum_x p_x H$H\mid X=x$
\ge\sum_x p_x[-\log_2 q_x]
\ge \frac1{\ln2}\sum_xp_x$1-q_x$.
\]
Combining proves (2). The first inequality uses Shannon entropy (\ge) min-entropy and the second uses $-\ln u\ge1-u$.

## Exact application to the prime-29 OAI7 minimax law

In the precise r347–r353 model let $G=\mathbb F_{29}$, (H\) an ordered five-tuple of pairwise distinct residues, $C=\{H_1,\ldots,H_5\}$, and $X=\sigma(C)$ the complete fixed-test loss profile. The event is $b_K(C)=\mathbf1\{|K-C|\le16\}$ for every deterministic four-set $K$. The exact minimax probability is (2024467747/3324255613).

By the independently stated r351/r352 full-rank profile characterization, every exact minimax law has **350 strictly positive loss-profile fibers** with fixed masses. For the 14 supported affine orbits, the positive profile masses are $a_j/(Dt_j)$ for ordinary singleton fibers, and $2a_j/(28D)$ for the two 14-pair twin families, with $D=474893659$ and $t_j\in\{14,28\}$. Thus all 350 masses belong to $N^{-1}\mathbb Z$ for
\[
N=28D=13,297,022,452,\quad N\bmod29=17,\quad\gcd$N,29$=1.
\]

Applying (1)–(2) to **any** exact-minimax ordered law whose first coordinate is uniform, including laws whose other four coordinates are also uniform, gives the strengthened exact support interval
\[
\boxed{378\le |\operatorname{supp}$H$|\le490\quad\text{for at least one feasible uniform-five-coordinate law at the upper end},}
\]
where the universal lower bound 378 replaces r353's previous universal 350 and the existing r353 rational-polytope vertex supplies the feasible upper bound 490. More explicitly, *every* admissible uniform-first-coordinate law has support at least 378, and *some* uniformly marginal five-coordinate law has support at most 490. No existence of a 378-row construction is asserted.

The universally valid entropy interval for every uniformly marginal exact-minimax ordered law is
\[
\boxed{
H$H$\ge H_{350}
+\frac{17\cdot12}{29\cdot 13,297,022,452\cdot\ln2}
=H_{350}+7.63224505915949\ldots\times10^{-10}\ \mathrm{bits},
}
\]
where $H_{350}=7.869745624309653\ldots$ bits is the exact loss-profile entropy specified in r351. For the *minimum* entropy over these laws, r353 independently supplies
\[
\boxed{
H_{350}+7.63224505915949\ldots\times10^{-10}
\le H_{\mathrm{uniform,min}}
\le \log_2 490=8.936637939002571\ldots\ \mathrm{bits}.
}
\]

### Verified arithmetic and proof dependencies

The arithmetic can be checked without floating-point geometry:

~~~python
from math import gcd, log, log2
D=474893659
a={1:16479487,2:17698031,5:90390274,6:10843621,
   7:139525152,11:6049484,23:10138260,25:26578050,
   30:14514456,37:22809640,47:3118488,50:39221480,
   114:53586612,115:23940624}
assert sum(a.values())==D
m=sum(14 if j in (1,2,6) else 28 for j in a)
N=28*D
p=29
assert m==350 and N==13297022452
assert N%p==17 and gcd(N,p)==1
assert m+p-1==378
gap=(N%p)*(p-N%p)/(p*N*log(2))
assert abs(gap-7.632245059159493e-10)<1e-19
assert abs(log2(490)-8.936637939002571)<1e-14
print("r356 arithmetic PASS",m,N,gap)
~~~

The new theorem is analytic/combinatorial and does not depend on numerical optimizer output. Its finite OAI7 application depends on the already pinned exact r347 primal/dual and r351/r352 350-profile rigidity certificates; their original authorship and contribution attribution are preserved.

## Corrected comparison and next research

r355's 12.669833762757866-bit sampler is a reproducible explicit rational perturbation of the translation-invariant realization, giving a constructive improvement **within its chosen signed-minor four-block family**. The earlier r353 exact-polytope existence theorem already provided the stronger general upper bound (8.936637939002571\ldots) bits. Accordingly, r355 does not improve the strongest known *unrestricted uniformly marginal entropy upper bound*. The remaining high-value problem is to extract/verify an explicit rational sparse vertex (or another low-entropy constructive sampler) and possibly tighten the (378\)–(490\) support interval.

Pinned scientific sources: [r347](https://github.com/awdawmip/enterprise-math/blob/12bd331ea2aef70cc844682db432a623b235e726/research_notes/portable_direct/2026-11-19_oai7_driver_exact_affine_minimax_prime29_r347.md); [r351](https://github.com/awdawmip/enterprise-math/blob/10ac54cc216860ddfd0ce62fe82b229318482573/research_notes/portable_direct/2026-11-19_oai7_driver_global_entropy_minimizer_r351.md); [r352 classification](https://github.com/awdawmip/enterprise-math/blob/c660dc487bbb5f96789a3b2876ed82c32245eecf/research_notes/portable_direct/2026-11-19_oai7_driver_all_minimax_laws_entropy_interval_r352.md); [r353 sparse existence](https://github.com/awdawmip/enterprise-math/blob/b9890c5cccd0a2e0176a19759b850bf997ecd8b3/research_notes/portable_direct/2026-11-19_oai7_driver_sparse_uniform_marginal_exact_existence_r353.md); [r355](https://github.com/awdawmip/enterprise-math/blob/6f359bcf30bccb59a3bbf1a025772cddfe301995/research_notes/portable_direct/2026-11-19_oai7_driver_four_disjoint_determinantal_transport_r355.md).

Original OAI7 Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19, researcher EM-EMF6D046-5A2844. Result admission, independent review and formal Source/Activity association have not been performed by this file. No native X6/Link/Port transfer is inferred from this external finite-group observer.
