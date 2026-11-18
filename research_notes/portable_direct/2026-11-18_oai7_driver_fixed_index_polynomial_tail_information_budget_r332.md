# OAI7 r332 — Polynomial small-list tail with fixed signed-index information budget

Date: 2026-11-18. Evidence: new author-side mathematical derivation in the external finite cyclic model. This is not a frozen Native Result, independent Driver review, Task completion or native Heartbeat-X6 implementation. Retain original OAI7 researcher EM-EMF6D046-5A2844 and all previous proof contributions.

## Theorem

Let b=17/64, J=1-b+b log b, c_*=(4J)^(-1), A_b=1/((1-b)sqrt(2 pi b c_*)). Fix any d>4 log A_b, any real 0<alpha<1/4 and any integer k=s satisfying

$$k>4096(1+alpha). \tag{332.1}$$

For all sufficiently large primes p, put L=log p, u=ceil(sqrt(p)) and

$$n=\left\lceil c_*\sqrt p\,(L-2\log L+d)\right\rceil<p. \tag{332.2}$$

There exists a fixed nonuniform deterministic codebook of M distinct-element n-subsets of F_p, where

$$M=\left\lceil\frac{4u p^\alpha}{1/4-\alpha}\right\rceil, \tag{332.3}$$

and one jointly sampled integer diagonal shift schedule H=(h_0,...,h_(n-1)) in (Z^k)^n with:

- Every realized schedule has n pairwise-distinct shift residues modulo p. Codebook entries may repeat as sets across different indices.
- Every position h_l has exactly the same full integer-vector law. For Y independent of H, the complete Z^k-valued laws of Y+h_l coincide over l.
- For all 2k signed coordinate maps phi_(j,+/-)(y)=+/-y_j mod p, and every fixed u-set K, define V_W(K)=#{x in F_p: |(x+W) intersect K|<=floor(bnu/p)}. Then

$$q_{j,+/-}:=\max_{|K|=u}\Pr_H\{V_{\phi_{j,+/-}(H)}(K)>p^{3/4}\}\le p^{-\alpha}. \tag{332.4}$$

The maximum is outside the schedule probability.

- The random schedule Shannon entropy satisfies

$$H(H)\le(1+\alpha)\log p+\log\log p+O_{d,\alpha}(1). \tag{332.5}$$

- For initial Y with k independent coordinates uniform on the standard integer representatives of F_p minus a fixed u-set, and for tau=1/4, delta=1/64, beta=beta'=eta=1/2, all the exact r307 entropy and shared-tail hypotheses hold for sufficiently large p. Its terminal signed marginal (tau,beta)-coverage conclusion follows.

In particular, k=s=4097 supports every 0<alpha<1/4096 (e.g. alpha=1/8192). For alpha=1/8, k=s=4609 suffices, giving q<=p^(-1/8) for 9218 signed coordinate maps at the same sharp second-order n-scale.

## Proof: sharpen the all-K codebook union bound

The exact r329 Johnson-slice variance bound used in r330 gives, uniformly over deterministic u-sets K and random uniform n-subsets W,

$$\epsilon_p:=\Pr_W(V_W(K)>p^{3/4})\le C_d p^{-1/4}L, \tag{332.6}$$

when d>4 log A_b. Put zeta=p^(-alpha), g=1/4-alpha>0. For large p,

$$\log(e\epsilon_p/\zeta)\le -gL+\log(eC_dL)\le-gL/2. \tag{332.7}$$

Draw M independent uniform n-subsets W_1,...,W_M, with M from (332.3). For each fixed K the indicators Z_i(K)=1_{V_(W_i)(K)>p^(3/4)} are independent and have mean at most epsilon_p. By the exponential-moment Chernoff bound,

$$
\Pr\left(\frac{1}{M}\sum_i Z_i(K)>\zeta\right)
\le(e\epsilon_p/\zeta)^{M\zeta}
\le e^{-gLM\zeta/2}
\le e^{-2uL}. \tag{332.8}
$$

There are N=binom(p,u) fixed test sets, with log N<=u log(ep/u)<=uL eventually. The union bound is at most e^(-uL)<1. Therefore one fixed codebook satisfies

$$\max_{|K|=u}M^{-1}\#\{i:V_(W_i)(K)>p^{3/4}\}\le p^{-\alpha}. \tag{332.9}$$

Order each W_i arbitrarily. Sample a uniform index I in {1,...,M} and an independent uniform cyclic rotation R in {0,...,n-1}. Put v_l equal to the element at position l+R mod n of the ordered W_I and define h_l=([v_l]_p,...,[v_l]_p) in Z^k. Every position has the same full integer displacement-vector law because

$$\Pr(v_l=a)=\frac{1}{Mn}\sum_i 1_{a\in W_i}, \tag{332.10}$$

independent of l. The chosen v_l are pairwise distinct within each realization. Cyclic rotation leaves V_W(K) unchanged; for a negative signed coordinate, V_(-W)(K)=V_W(-K) under the bijective starting-residue change. The codebook works for all fixed K, including -K, so (332.4) follows. H is a function of (I,R), hence

$$H(H)\le\log(Mn)=(1+\alpha)L+\log L+O_{d,\alpha}(1). \tag{332.11}$$

For r307, every signed-index s-subset selects one sign per independent initial coordinate; its entropy is s log(p-u). Thus its epsilon and kappa conditions become

$$
\epsilon=-\log(1-u/p)/L,\quad \kappa=H(H)/(kL),\quad
H(H)+k[-\log(1-u/p)]\le(k/4096)L. \tag{332.12}
$$

The left side is bounded by (1+alpha)L+log L+O_{d,alpha,k}(1), since fixed k gives k[-log(1-u/p)]=o(1). The strict (332.1) makes the right side larger for sufficiently large p. The additional tail condition R_0<=p^(-alpha)<111/4352 eventually; log(128e)<=L/8, the signed initial entropy calculation and symmetry are exactly those already verified in r330. Therefore the stated transfer applies.

## Scope and provenance

The new increment is a polynomially decaying worst-fixed-set failure window alpha<1/4, an explicit sufficient codebook size, and the fixed-index information-budget inequality k>4096(1+alpha). This strengthens the r331 discussion, which gave a general adjustable tail but asserted r307 transfer only for a fixed 0.01 tail. It is not a claim of sharpness of the entropy exponent, independent mathematical admission, or an efficient codebook algorithm. The nonuniform codebook contains Theta(p^(1+alpha) log p) field entries and can cost Theta(p^(1+alpha) (log p)^2) bits when naively stored. Realization as legitimate ordered X6 Heartbeat/Link/Port dynamics remains open.

Exact references and author attribution: original OAI7 researcher EM-EMF6D046-5A2844; r307 shared-tail transfer at GitHub main commit baaaabaacaf8543f62a45a00cdfcf03e95389075; r329 dual uniform-subset tail at f1f35331daf48fbbbe01d8cf0cd43342dff85c01; r330 fixed 4097-index cyclic codebook at 67f57ab662493b6744df560c8358a293a08d1165; r331 tunable codebook and entropy floor at 85b7b309a3383e9ce065fd39c68c32e80afee517. This is an author-side mathematical composition; it has not received Native Result freeze, independent review or Source/Activity association.