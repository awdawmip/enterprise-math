# OAI7 r330: Fixed 4097-index shared schedule at the sharp second-order length (nonuniform codebook)

Date: 2026-11-18. Evidence: author-side existence theorem; no Native Result/Review/Activity admission. External finite cyclic shared-displacement model only. Retain original OAI7 researcher EM-EMF6D046-5A2844 and all prior Driver/author contribution provenance.

## Theorem

Put b=17/64, J=1-b+b log b, c_*=(4J)^{-1}, and A_b=1/((1-b)sqrt(2 pi b c_*))=1.3033409133617793.... For any fixed d>4 log A_b=1.0597236047634222... and all sufficiently large primes p, let

$$
L=\log p,\quad u=\lceil\sqrt p\rceil,\qquad
n=\left\lceil c_*\sqrt p\,(\log p-2\log\log p+d)\right\rceil <p .
$$

There exists **one joint** diagonal-shift random vector H=(h_0,...,h_(n-1)) with each h_l in Z^4097 and the following properties.

* Every realized schedule has n **pairwise-distinct** mod-p shifts.
* For Y independent of H, with 4097 independent coordinates uniform on the standard integer representatives of F_p\B for any fixed u-set B, the **entire lattice-valued** Y+h_l laws are identical over l.
* For all 8194 signed residue homomorphisms phi_(j,±)(v)=±v_j mod p, and every fixed deterministic u-set K, the small-list failure probability is at most 1/log p:
$$
q_c=\max_{|K|=u}\Pr_H\left(
\#\left\{x\in F_p:\sum_{l=0}^{n-1}{\bf1}_{x+\phi_c(h_l)\in K}\le bnu/p\right\}>p^{3/4}\right)
\le1/L\longrightarrow0 .
$$
* The *random-vector Shannon entropy* obeys
$$
H(H)\le\log p+2\log\log p+O_d(1).
\tag{R330.1}
$$

For tau=1/4, delta=1/64, beta=beta'=eta=1/2 and s=k=4097, every r307 integrated-tail transfer condition follows, and all terminal signed marginals achieve (tau,beta)-coverage. Thus fixed signed-index count 4097, O(log p) **random** shift entropy, pairwise-distinct schedules and the sharp second-order coefficient -2c_* are jointly attainable within this nonuniform existential model. This does not assert polynomial-time codebook generation, short public program description, a native X6 path or Gaussian-prime walk realization.

## Proof: all-K codebook from the dual slice concentration

By r329's new n-slice Johnson-spectral-gap bound, for a *uniform n-subset* W of F_p and each deterministic u-subset K, writing

$$ V_W(K)=\#\{x:|(x+W)\cap K|\le\lfloor bnu/p\rfloor\},$$

the uniform failure bound is
$$
\epsilon_p:=\sup_{|K|=u}\Pr_{W\text{ uniform}}\{V_W(K)>p^{3/4}\}
=O_d(p^{-1/4}L).
\tag{R330.2}
$$
This follows because for d>4 log A_b, r329's exact prefactor has limsup M_p/p^(3/4) at most A_b exp(-d/4)<1; the variance/mean-squared rate on the n-slice is O(p^(-1/4)L). In particular epsilon_p<=p^(-1/8) for all sufficiently large p.

Let N=binom(p,u) be the number of deterministic u-sets, and independently select
$$M=\lceil32(\log N+1)\rceil$$
uniform n-subsets W_1,...,W_M. For every fixed K put Z_i(K)=1_{V_(W_i)(K)>p^(3/4)}. Each Z_i is Bernoulli with expectation <=epsilon_p, and the Z_i are independent over i. At zeta=1/L, the exponential-moment Chernoff bound is

$$
\Pr\left(\frac1M\sum_i Z_i(K)>\zeta\right)
\le(e\epsilon_p/\zeta)^{M\zeta}
\le e^{-M/16},
$$

where the second inequality holds eventually since 1+log L-L/8<=-L/16. Union bound over *all* N deterministic K gives

$$
\Pr\left(\exists K:\frac1M\sum_iZ_i(K)>1/L\right)
\le N e^{-M/16}<1.
$$

Therefore one deterministic codebook C=(W_1,...,W_M) exists for which

$$
\max_{|K|=u}\frac1M\#\{i:V_{W_i}(K)>p^{3/4}\}\le1/L .
\tag{R330.3}
$$

Each member W_i has n distinct elements; different codebook members may repeat, harmlessly. The codebook is *fixed prior* to the H distribution and all fixed-K tests.

## Proof: cyclic randomization supplies exact identical full-lattice marginals

Fix an arbitrary ordering a_(i,0),...,a_(i,n-1) for every W_i. Draw a single pair of independent uniform indices I in {1,...,M}, R in {0,...,n-1}, and set

$$
v_l=a_{(I,(l+R)\bmod n)}\in F_p,\quad
h_l=([v_l]_p,\ldots,[v_l]_p)\in Z^{4097}.
$$

For every l and a in F_p,
$$
\Pr(v_l=a)=\frac1{Mn}\sum_{i=1}^M {\bf1}_{a\in W_i},
$$
independent of l. This equality of **entire integer displacement vector** laws and independence of Y imply equality of full-lattice Y+h_l laws. It does not assume v_l uniformly distributed.

Cyclic position rotation does not alter V_W(K); negating shifts satisfies V_(-W)(K)=V_W(-K) after changing the start residue variable x to -x. Consequently (R330.3) establishes q_c<=1/L for every signed coordinate with the correct order max over deterministic K *outside* the schedule probability.

As H is a deterministic function of (I,R),
$$
H(H)\le\log(Mn).
$$
The elementary binomial bound log N<=u log(ep/u)=O(sqrt p L) gives M=O(sqrt p L); also n=O(sqrt p L). Thus log(Mn)<=L+2log L+O_d(1), proving (R330.1).

## Proof: exact r307 budget and conclusion

Set k=s=4097. Every signed-index subset S of size s selects all distinct base indices with exactly one sign per index. Since Y_j are independent uniform on p-u residues,
$$
H(F_S(Y))=s\log(p-u),\qquad
\epsilon=-\frac{\log(1-u/p)}{L}=O(p^{-1/2}/L).
$$
Taking kappa=H(H)/(sL), r307 requires epsilon+kappa <=eta delta beta'/16=1/4096. Because

$$
sL(\epsilon+\kappa)\le L+2\log L+O_d(1)+O(s/\sqrt p)
$$
and
$$
sL/4096=(1+1/4096)L,
$$
the exact information inequality holds for all sufficiently large p. Also log(2e/delta)=log(128e)<=L/8 eventually. Finally

$$
R_0=\frac1{2k}\sum_c q_c\le1/L
<\eta\left(\frac\delta{\tau+\delta}-\frac\delta2\right)
=\frac{111}{4352}
$$

eventually, so r307 gives coverage for all but at most eta of the 2k signed terminal coordinates. Across j all terminal coordinate laws are the same; + and - laws are related by negation and have equivalent coverage verdicts. Hence failure of one coordinate would mean failure of all 2k, contrary to the transfer conclusion. In this symmetric witness all terminal signed coordinates have coverage.

## Information-theoretic and contribution boundaries

The public deterministic codebook contains M n=O(p L^2) field entries, with naive description cost **O(p L^3) bits**. The theorem measures Shannon entropy of the *sampled vector H*, not total storage, preprocessing time or uniform algorithm description. A compressed explicit family is a separate research problem. The codebook method is an existence argument and its vast advice cost must be included in any claimed computational advantage.

This supplies a fixed-index nonuniform route absent from the prior polynomial-seed proofs; it does not retroactively change r311's proven one-*uniform-p-seed* 4097-index lower bound, and it does not claim 4097 is minimal over arbitrary schedule classes.

Provenance: r307 original shared-tail transfer (main@baaaabaacaf8543f62a45a00cdfcf03e95389075); r311 one-seed index bound (@8720c3abc815c45295a922a7dc9e10273cfed1ef); r321 first-order necessary coefficient (@3c411d17ca496dfcfcdb91082643597981f6b9d2); r326 and r327 constructive polynomial-seed second-order bounds (@4d94923811a8b47a01f584f337fd5028bd23b40d and @d9deb25a2561cbf7ccbbcca8dd75ee7528a6b356); r328 distinct second-order necessity (@961b63fca64881cfbd24894803bdaf24f5d5b570); r329 new dual n-slice variance and fixed-d uniform-subset success (@f1f35331daf48fbbbe01d8cf0cd43342dff85c01). New r330 contribution: simultaneous all-K codebook, cyclic equal-marginal randomization, and fixed 4097-index entropy audit. Original OAI7 researcher authorship remains intact.
