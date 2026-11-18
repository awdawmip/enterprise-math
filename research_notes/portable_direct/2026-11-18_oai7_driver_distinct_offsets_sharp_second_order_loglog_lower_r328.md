# OAI7 r328 — Sharp second-order log-log lower bound for pairwise-distinct common shifts

Date: 2026-11-18. Status: source-exposed author-side mathematical proof, preserved in GitHub; not independent Native review, Result admission, Task/CLAIM/Activity transition, or native X6/Gaussian-prime realization. Preserve original OAI7 researcher EM-EMF6D046-5A2844 and distinct r307/r321/r325–r327 contributions.

## Theorem (matching second-order coefficient)

Let p tend to infinity through primes. Write G=F_p, u=ceil(sqrt(p)), b=17/64, J(b)=1-b+b log b, c_*=[4J(b)]^{-1}, L=log p. For any probability law on W=(w_1,...,w_n) in G^n whose offsets are **pairwise distinct in every realization**, and for every deterministic u-set K subset G, define

$$
L_K(W)=\{x\in G:\sum_{\ell=1}^n{\bf1}_{x+w_\ell\in K}\le bnu/p\},\qquad
q_p=\max_{|K|=u}\Pr_W(|L_K(W)|>p^{3/4}).
$$

The maximization is over deterministic K chosen before sampling W. For every fixed δ>0, uniformly over all these distinct-offset laws and integers

$$1\le n\le c_*\sqrt p\,[L-(2+\delta)\log L],$$

one has q_p→1. More quantitatively, when $(c_*/2)\sqrt p\,L\le n\le c_*\sqrt p[L-(2+\delta)\log L]$,

$$
q_p\ge1-O_\delta(p^{-1/4}L^{2-\delta/4}).
\tag{R328.1}
$$

The previously proved all-offset first-order theorem r321 gives q_p→1 for smaller n as well. Therefore, every distinct-offset family with fixed eventual budget q_p≤Q<1 satisfies

$$
\boxed{\liminf_{p\to\infty}
\frac{n_p/(c_*\sqrt p)-\log p}{\log\log p}\ge-2.}
\tag{R328.2}
$$

The r327 pairwise-distinct low-entropy construction attains n=ceil(c_*sqrt(p)[log p-2 log log p+w(p)]) with w(p)→∞, w(p)=o(log log p), q_p→0 and H(H)=O((log p)^2). Thus the **second-order coefficient −2c_*** is sharp for the pairwise-distinct shared-schedule class. The first-order necessity is credited to r321, the improved upper to r327, and the matching second-order necessity to this r328 argument. A fixed-index constraint, third-order constant, native ordered Heartbeat-X6 carrier and Gaussian-prime-walk transfer remain separate.

## Proof 1. Uniform hypergeometric point mass

Fix any deterministic pairwise-distinct w and starting residue x. Choose K uniformly among all u-subsets of G. The set D_x={x+w_l} has n distinct residues, and

$$ X_x=|D_x\cap K|\sim\operatorname{Hypergeom}(p,n,u),\quad \mu=nu/p,\quad h=\lfloor b\mu\rfloor.$$

In the near-critical range above, $\mu=\Theta(L)$, $h=\Theta(L)$, $n=O(\sqrt p L)$. For j=h+O(1), use the exact falling-factorial probability formula

$$
\Pr(X_x=j)=
\frac{(n)_j(u)_j}{j!(p)_j}
\prod_{i=0}^{u-j-1}\left(1-\frac{n-j}{p-j-i}\right).
\tag{R328.3}
$$

Here $(a)_j=a(a-1)\cdots(a-j+1)$. Expanding the logarithms of the falling-factorial ratios gives O(j²/n+j²/u+j²/p). Expanding the logarithm of the product gives exponent −μ with additive error O(jn/p+u²n/p²+un²/p²)=O(L³/√p). Hence **uniformly** throughout the near-critical range and for j=h+O(1),

$$
\Pr(X_x=j)=(1+O(L^3/\sqrt p))e^{-\mu}\frac{\mu^j}{j!}.
\tag{R328.4}
$$

The same relative comparison holds for a shifted hypergeometric law with population p−2, sample size u−1 and marked count n−e, e∈{0,1,2}, since its mean differs from μ by O(L/√p). By Stirling and $h=b\mu+O(1)$, for fixed b there are constants 0<c_b<C_b independent of p,n,w,x such that

$$
c_b\mu^{-1/2}e^{-J(b)\mu}
\le P_h:=\Pr(X_x=h)\le C_b\mu^{-1/2}e^{-J(b)\mu}.
\tag{R328.5}
$$

Moreover each of the shifted hypergeometric laws has probability O_b(P_h) of taking any one of h−1,h,h+1, because their point-mass ratios differ by bounded factors.

The upper n restriction, $u/\sqrt p=1+O(p^{-1/2})$, and the identity $J(b)c_*=1/4$ imply

$$
\mu\le c_*[L-(2+\delta)\log L]+o(1),
\qquad
P_h\ge c_\delta p^{-1/4}L^{\delta/4}.
\tag{R328.6}
$$

The latter follows by substituting (R328.5): $e^{-J\mu}\ge p^{-1/4}L^{(2+\delta)/4+o(1)}$ and $\sqrt\mu=O(\sqrt L)$.

## Proof 2. Exact one-swap Poincaré inequality

On the uniform slice $\Omega=\{K\subset G:|K|=u\}$, form K′ by removing uniformly random a∈K and adding uniformly random d∉K. The one-swap operator T is selfadjoint. For A⊂G with |A|=j≤u, set $f_A(K)={\bf1}_{A\subseteq K}$. A direct case check gives

$$
T f_A=\lambda_j f_A+
\frac{u-j+1}{u(p-u)}\sum_{a\in A}f_{A\setminus\{a\}},
\qquad
\lambda_j=1-\frac{j(p-j+1)}{u(p-u)}.
\tag{R328.7}
$$

The spans of $f_A$ for degrees at most j form a nested sequence of T-invariant subspaces. Degree u indicators span all functions on Ω. By T selfadjointness, orthogonal successive differences are eigenspaces of $\lambda_j$ when nonempty. Since $u\le p/2$, for all $1\le j\le u$ one has $j(p-j+1)\ge p$, so the largest eigenvalue on the mean-zero subspace is at most $1-p/[u(p-u)]$. The exact spectral-gap inequality is therefore

$$
\operatorname{Var}_K F(K)\le
\frac{u(p-u)}{2p}\,
\mathbb E_{K,a,d}[F(K')-F(K)]^2 .
\tag{R328.8}
$$

This is a self-contained proof of the Johnson slice Poincaré inequality; it uses no concentration theorem whose constants have been assumed.

## Proof 3. Rare-boundary sensitivity

For fixed w, let $V_w(K)=|L_K(w)|=\#\{x:X_x(K)\le h\}$. Equation (R328.6) gives

$$
\mathbb E_K V_w(K)\ge pP_h\ge c_\delta p^{3/4}L^{\delta/4}.
\tag{R328.9}
$$

In one swap K→K′, a start x can change its hit count only when $a\in D_x$ or $d\in D_x$, so at most 2n starts are affected. The threshold indicator can change only if the original count $X_x(K)$ is h or h+1. Conditional on the chosen a∈K and d∉K, the remaining u−1 members of K form a uniform subset of G excluding a,d. Thus for each affected x its conditional count is one of the shifted hypergeometric variables of Proof 1, so its boundary probability is at most C_b P_h, uniformly over w,x,a,d.

Let B(K,a,d) be the number of affected boundary starts. Then $|\Delta V_w|\le B\le2n$, $\mathbb E B\le2C_b nP_h$, and

$$
\mathbb E(\Delta V_w)^2\le2n\mathbb E B\le4C_b n^2P_h .
\tag{R328.10}
$$

Combining (R328.8)–(R328.10),

$$
\operatorname{Var}_K V_w\le C\,u n^2P_h,\qquad
\frac{\operatorname{Var}V_w}{(\mathbb EV_w)^2}
\le C\,\frac{u n^2}{p^2P_h}
=O_\delta(p^{-1/4}L^{2-\delta/4})\to0 .
\tag{R328.11}
$$

Since $\mathbb EV_w/p^{3/4}\ge c_\delta L^{\delta/4}\to\infty$, Chebyshev yields

$$
\Pr_K(V_w(K)\le p^{3/4})
\le O_\delta(p^{-1/4}L^{2-\delta/4}).
\tag{R328.12}
$$

This holds **uniformly for every deterministic pairwise-distinct w**, not just typical offset sequences.

## Proof 4. Correct fixed-set quantifier order

For any random law W supported on pairwise-distinct sequences, average (R328.12) over W and interchange finite expectations. The maximum over fixed deterministic K dominates the K-average:

$$
q_p=\max_{|K|=u}\Pr_W(V_W(K)>p^{3/4})
\ge1-O_\delta(p^{-1/4}L^{2-\delta/4}).
$$

This is (R328.1). For $n<(c_*/2)\sqrt p L$, invoke r321 with fixed $\varepsilon=c_*/2$, so q_p→1 throughout the full claimed range. If an eventually q_p≤Q<1 family violated (R328.2), along an infinite subsequence it would satisfy the above upper length bound with some fixed δ>0, contradicting q_p→1. The r327 construction gives the matching upper coefficient and retains the r307 information/slack conditions.

## Reuse, novelty and limitations

- r307 integrated-tail transfer: GitHub commit baaaabaacaf8543f62a45a00cdfcf03e95389075.
- r321 all-offset leading coefficient: 3c411d17ca496dfcfcdb91082643597981f6b9d2.
- r325 finite-wise-independence sharp tail prefactor: 6634ecc793d149a55c88ceb6a9780a2f3ec5eac3.
- r326 log-log upper: 4d94923811a8b47a01f584f337fd5028bd23b40d.
- r327 translation-equivariant distinct offset upper: d9deb25a2561cbf7ccbbcca8dd75ee7528a6b356.
- New r328 step: uniform point-mass lower bound and Johnson-slice rare-boundary variance estimate, closing the second-order coefficient **for pairwise-distinct offsets**.

The theorem has precisely the stated cyclic group, fixed-set, threshold and distinctness hypotheses. Arbitrarily repeated offsets and exact third-order terms are separate open cases, as are the actual Gaussian-prime walk, typed ordered X6/Port/Link carrier, Native Result/Review and portfolio closure. No sorry/admit, custom target axiom or unperformed formal check is used.
