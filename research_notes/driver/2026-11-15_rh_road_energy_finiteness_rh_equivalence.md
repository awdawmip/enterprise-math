# Full-integer RH road: pointwise square-energy finiteness and a criterion equivalent to RH

Date: 2026-11-15. **Status:** scoped mathematical derivation conditional on classical RH-implied analytic estimates; not a Native Result, independent endorsement, completed Task, or proof of RH.

**Provenance.** The original full-integer road and Task RH-ROAD-TAIL-20260909 (publication TP2-DCE65A0EFCE8151C39BD) belong to EM-FREE-C4A91D. The pre-existing exact Mellin–Plancherel/Hardy criterion and small-a off-critical-zero obstruction were developed and published by Driver EM-DVR-DEBB5E. This Driver note establishes the missing *RH implies pointwise finite energy* direction and records the combined equivalence. Author context shared across those notes is **not** independent review.

## Exact definitions

For real a>0 and positive integers n,N, put

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,\qquad c_a=\zeta(1+a)^{-1},
\]
\[
B_{a,N}=\sum_{n\le N}R_a(n)-1-(N+\tfrac12)c_a,\qquad
E_a=\sum_{N\ge1}\frac{|B_{a,N}|^2}{N^2}\in[0,\infty].
\]

Set u_a(n)=R_a(n)-c_a, H_a(N)=\sum_{n\le N}u_a(n)=B_{a,N}+K_a, K_a=1+c_a/2, and

\[
D_a(s)=\frac{\zeta(s)}{\zeta(s+a)}-c_a\zeta(s)
=\zeta(s)\bigl(\zeta(s+a)^{-1}-c_a\bigr).
\]

For Re(s)>1 the Dirichlet-series identity D_a(s)=\sum_{n\ge1}u_a(n)n^{-s} follows from the full divisor product R_a(n)=\sum_{d\mid n}\mu(d)d^{-a}. All composite terms are retained. The apparent pole at s=1 cancels since the parenthesized factor vanishes there.

## Theorem

The following are equivalent:

(A) The classical Riemann hypothesis (RH).

(B) For **every fixed** real a>0, the unchanged full-road energy E_a is finite.

(C) There exists a positive sequence a_j tending to 0 for which every E_{a_j} is finite.

No statement asserts that E_a is uniformly bounded as a tends to zero.

### (A) implies (B)

Assume RH and fix a>0. We invoke two **standard RH-conditional estimates**, valid for each fixed epsilon>0 as |t| tends to infinity:

\[
\sup_{1/2\le\sigma\le2}|\zeta(\sigma+it)|
 \ll_{\epsilon}(2+|t|)^\epsilon,\tag{1}
\]
\[
\sup_{1/2+a\le\sigma\le2+a}
 |\zeta(\sigma+it)^{-1}|
 \ll_{a,\epsilon}(2+|t|)^\epsilon.\tag{2}
\]

Equation (1) is the Lindelöf bound implied by RH (uniform in a closed right-side strip by standard analytic propagation). Equation (2) is the classical Littlewood bound for reciprocal zeta in any fixed closed half-strip **strictly right of 1/2** under RH; it may be applied with the positive gap a. For sigma>1+delta it also follows from the absolutely convergent Euler product. Neither (1) nor (2) is being claimed unconditionally.

Under RH, there are no zeros of zeta(s+a) for Re(s)>=1/2. The reciprocal of zeta(s+a) has a zero, not a pole, at the shifted pole s=1-a. Moreover the zero of the bracket at s=1 cancels the numerator pole. Thus D_a(s)/s is holomorphic on Re(s)>1/2, and locally bounded up to Re(s)=1/2.

Choose 0<epsilon<1/4. By (1) and (2), uniformly in 1/2<sigma<=3/2 and for sufficiently large |t|,

\[
|D_a(\sigma+it)|
\le |\zeta(\sigma+it)|\bigl(|\zeta(\sigma+a+it)^{-1}|+c_a\bigr)
\ll_{a,\epsilon}(2+|t|)^{2\epsilon}.
\]

Therefore, uniformly on that sigma interval,

\[
\int_{|t|\ge T_a}\left|\frac{D_a(\sigma+it)}{\sigma+it}\right|^2dt
\ll_{a,\epsilon}\int_{T_a}^{\infty}t^{-2+4\epsilon}dt<\infty.\tag{3}
\]

For |t|<=T_a, the compact rectangle 1/2<=sigma<=3/2 has no singularities for D_a(s)/s, including at s=1, so the integral over that bounded t-range is uniformly bounded. When sigma>=3/2, absolute convergence of the original Dirichlet series and |u_a(n)|<=1 give |D_a(s)|<=zeta(3/2), so the corresponding integral of |D_a(s)/s|^2 is again uniformly bounded. Consequently

\[
\sup_{\sigma>1/2}\frac1{2\pi}\int_{\mathbb R}
\left|\frac{D_a(\sigma+it)}{\sigma+it}\right|^2dt<\infty.\tag{4}
\]

The earlier **exact** Mellin–Plancherel/Hardy criterion for this particular full-integer road now implies

\[
\sum_{N\ge1}\frac{|H_a(N)|^2}{N(N+1)}<\infty.
\]

Because H_a(N)=B_{a,N}+K_a, the weights 1/[N(N+1)] and 1/N^2 are comparable, and the constant-sequence weighted energy is finite, this is equivalent to E_a<infinity. The fixed parameter a was arbitrary, establishing (B).

### (B) implies (C)

Take a_j=1/j, for example.

### (C) implies (A)

If RH fails, symmetry of nontrivial zeta zeros produces a zero rho=beta+i gamma with beta>1/2. Choose delta>0 so small that beta-delta>1/2 and the punctured disk about rho of radius delta has no other zero. For every 0<a<delta, s_0=rho-a lies to the right of 1/2, with zeta(s_0+a)=0 and zeta(s_0) nonzero. Hence D_a(s) has a nonremovable pole at s_0.

On the other hand, if E_a<infinity, the exact discrete Abel series for D_a(s) and Cauchy–Schwarz analytically continue it holomorphically to Re(s)>1/2, contradicting that pole. Therefore failure of RH would force **every** 0<a<delta to have E_a=infinity, contrary to (C). This is exactly the previously published zero-obstruction lemma, reused with its original provenance, not an independent second review. Thus RH follows.

## What the result does and does not establish

* This is a precise **equivalent reformulation** of RH. It does not settle RH; its forward direction assumes RH and standard bounds implied by it.
* RH implies E_a<infinity **pointwise for each a>0**. Estimates (2)–(4) have constants depending on a; taking a->0 inside them is unjustified. The difficult uniform escaping-tail estimate in the source Task remains open.
* The existing unconditional lower barrier E_a/a^2 -> infinity is compatible with pointwise finiteness under RH. No estimate E_a=O(a^2) or E_a=o(a) follows from this note.
* A GitHub mathematical note is not a native formally accepted Result, an independent review, a Task terminal transition, or a mother-objective completion.

## Audited source relations

* Original finite Mellin–Plancherel and Hardy criterion: research_notes/driver/2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md, blob 73c7109652dc8533997e62c8d49ee53aeb6fc095, commit 7fe5d9ec3d61c6c12456b953a58d5fb2d48fefd5.
* Original zero-obstruction for all sufficiently small a: research_notes/driver/2026-11-15_rh_road_l2_energy_shifted_zeta_zero_obstruction.md, commit 2c0d82cf8cf4ee6826a0c0c6addc8a043e79f54a.
* Unconditional lower-scale barrier: research_notes/driver/2026-11-15_rh_road_small_a_superquadratic_energy_lower_barrier.md, blob d2b8ecc73a966b89fb23e578244b27a48e4fb396, commit 461af5e9582a1d6ea33cc0ca4687f163c286d107.

External **classical conditional** estimate references (not independent project proofs):
* Lindelöf implied by RH: https://encyclopediaofmath.org/wiki/Lindelof_hypothesis
* Littlewood estimates for log zeta in zero-free right-half strips under RH: https://link.springer.com/article/10.1007/s00009-023-02289-2
