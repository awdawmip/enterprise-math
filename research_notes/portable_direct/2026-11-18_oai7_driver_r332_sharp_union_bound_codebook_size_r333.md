# OAI7 r333 — sharpened all-test-set codebook size and source-aware audit of r332

Date: 2026-11-18. Scope: external finite cyclic shared-shift model, author-side mathematical refinement and technical audit. **Not** an independent Native Driver review, formal Result, Task completion, accepted transfer to Gaussian-prime walks, or native X6 Heartbeat/Link/Port dynamics. Review context overlaps with prior Driver derivations; do not claim independent source isolation or reuse this as a clean independent reviewer pass.

## Exact proposition

Use the constants and domain of [r332](https://github.com/awdawmip/enterprise-math/blob/52125fe8ca34654ad5d9311f0b2703a0f450d0b3/research_notes/portable_direct/2026-11-18_oai7_driver_fixed_index_polynomial_tail_information_budget_r332.md): a fixed $d>4\log A_b$, $b=17/64$, $0<\alpha<1/4$, primes $p\to\infty$, $L=\log p$, $u=\lceil\sqrt p\rceil$, $n=\lceil c_*\sqrt p(L-2\log L+d)\rceil$, $c_*=[4(1-b+b\log b)]^{-1}$. Let $g=1/4-\alpha>0$.

For any fixed slack $\rho>0$, r332's deterministic nonuniform all-(K) codebook can be constructed with
$$
\boxed{M_\rho=\left\lceil\frac{(1/2+\rho)u\,p^\alpha}{g}\right\rceil}
\tag{333.1}
$$
rather than $\lceil 4up^\alpha/g\rceil$, and retain all of its conclusions:
$$
\max_{|K|=u}\Pr_H\{V_{\pm W}(K)>p^{3/4}\}\le p^{-\alpha},
\quad H(H)\le(1+\alpha)\log p+\log\log p+O_{d,\alpha,\rho}(1),
\tag{333.2}
$$
with equal entire $\mathbb Z^k$-valued marginals for all shift positions, pairwise-distinct shifts within each realized schedule, and the r307 integrated-tail transfer when the fixed integer $k=s>4096(1+\alpha)$.

The ratio of the new sufficient codebook size to r332's stated sufficient size tends to $(1/2+\rho)/4$. As $\rho\downarrow0$ **after** choosing a fixed $\rho>0$, this approaches $1/8$, i.e. an almost eightfold reduction in the number of stored schedules. This is an improvement to a *sufficient union-bound construction constant*, not a minimax lower bound for codebooks, and not a change in the first-order Shannon entropy coefficient or preprocessing complexity class.

## Proof

By the dual uniform-(n)-slice Johnson variance estimate in pinned [r329](https://github.com/awdawmip/enterprise-math/blob/f1f35331daf48fbbbe01d8cf0cd43342dff85c01/research_notes/portable_direct/2026-11-18_oai7_driver_dual_slice_concentration_fixed_offset_threshold_r329.md) and the strict $d>4\log A_b$ assumption, for each fixed deterministic (u)-set $K\subset\mathbb F_p$ and $W\sim\mathrm{Unif}\binom{\mathbb F_p}{n}$,
$$
\Pr\{V_W(K)>p^{3/4}\}\le \epsilon_p\le C_d\,p^{-1/4}L.
\tag{333.3}
$$
The same $C_d$ applies uniformly over all (K); no (K) is selected after a sampled (W).

Take $M=M_\rho$ independent such sets $W_i$, and put $Z_i(K)=\mathbf1_{\{V_{W_i}(K)>p^{3/4}\}}$, $\zeta=p^{-\alpha}$. The Bernoulli exponential-moment inequality yields
$$
\Pr\left\{M^{-1}\sum_i Z_i(K)>\zeta\right\}
\le \left(\frac{e\epsilon_p}{\zeta}\right)^{M\zeta}
\le\exp\left[-M\zeta\bigl(gL-\log(eC_dL)\bigr)\right].
\tag{333.4}
$$
The exponent is negative for all sufficiently large $p$. Since $M\zeta\ge(1/2+\rho)u/g$, it is at most
$$
-(1/2+\rho)uL+O_{d,\alpha,\rho}(u\log L).
\tag{333.5}
$$
The complete number of fixed tests $N=\binom pu$ satisfies, using $u=\lceil\sqrt p\rceil$,
$$
\log N\le u\log(ep/u)=\tfrac12 uL+O(u).
\tag{333.6}
$$
The union-bound logarithm is therefore at most $-\rho uL+O(u\log L)\to-\infty$. With positive probability, **one fixed codebook** of $M_\rho$ (n)-sets satisfies the bound simultaneously for *every* (K). Fix that codebook before defining the schedule law.

As in r330/r332, impose an arbitrary order on each $W_i$, choose $I\sim\mathrm{Unif}[M_\rho]$ and independent $R\sim\mathrm{Unif}[n]$, and cyclically rotate the chosen set. Each (v_l) has the identical marginal $\Pr(v_l=a)=(M_\rho n)^{-1}\sum_i\mathbf1_{a\in W_i}$, and $h_l=([v_l]_p,\ldots,[v_l]_p)\in\mathbb Z^k$ has equal full-lattice marginal laws. The negative-sign test reduces to a test at the deterministic set $-K$. Every realization retains distinct offsets. Finally
$$
H(H)\le\log(M_\rho n)=(1+\alpha)L+\log L+O_{d,\alpha,\rho}(1).
\tag{333.7}
$$
The fixed signed-index r307 entropy condition and integrated-tail condition then follow **using the same arguments, assumptions and contribution provenance as r332**; the codebook-size change alone adds no X6 realization or formal acceptance.

## Finitary selection inequality, for auditing

More generally, if a verified uniform bound $0<\epsilon_p<\zeta/e$ is given for a single random schedule, the same method succeeds with failure-of-the-union probability at most $e^{-a}$ whenever
$$
M\ge\left\lceil\frac{\log\binom pu+a}{\zeta\log(\zeta/(e\epsilon_p))}\right\rceil,
\qquad a>0.
\tag{333.8}
$$
Its specialization to (333.3) has leading coefficient $1/(2g)$ in $M/(up^\alpha)$ for fixed (d,\alpha). The arbitrary positive (\rho) absorbs subleading $\log L/L$ corrections. This is a **Chernoff–union-bound sufficiency** statement; no optimality among all random codebooks is claimed.

## Audit boundary and attribution

The r332 argument's quantifiers, tail-to-entropy budget and cyclic equal-marginal reduction were checked against the pinned r307, r329, r330 and r332 written claims. This is a shared-context technical check rather than clean independent review. The inherited Johnson-slice variance lemma and original transfer lemma are cited as prior results; they are not reproved or formally checked here. Any decisive Native review must independently inspect those load-bearing steps and the exact frozen Result/Source bytes, then write through the current Driver/DA-controlled review operation.

Original OAI7 researcher: EM-EMF6D046-5A2844. Existing mathematical contributions: r307 transfer; r329 dual slice; r330 fixed-index codebook and cyclic marginal construction; r331 entropy tail; r332 polynomial-tail budget. This note contributes only the sharpened all-(K) union bound and its explicit finite-$p$ sufficiency certificate. No new Task, CLAIM, frozen Result, Activity, Driver review pass or mother-objective closure is asserted.
